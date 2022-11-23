Avagrande | 2020-04-30 06:41:09 UTC | #1

Hello 
Currently I am aware of the following functions that affect the state of the node:
    SetEnabled
    SetDeepEnabled
    ResetDeepEnabled
    SetEnabledRecursive

Is there a reason why there needs to be 4 of them?
I found it very tricky to use it and keep a mental note on whats deep enabled or not. 

In my own fork of urho3d I have modified SetEnabled to act recursively such that nodes beneath it preserve their state as "enabled" but their components are disabled following a recursive check performed on each SetEnabled call. 

I noticed that after applying this change I didn't have to use any other functions besides SetEnabled to control node state. I would want to consider providing this for other people to use however I am worried this might not go down well in terms of expected usage as old code would need to be adjusted.  Personally I only had to adjust my own project code to reflect the changes ( removal of SetDeepEnabled and SetEnabledRecursive for SetEnabled ). 

**Is there any significant reason why accessible Deep state is preferred over a recursive SetEnabled?** 
By recursive I mean child nodes maintaining their Enabled state but the parent node sends a event down the chain updating the state of all its child nodes creating a "deep" state but this state is never accessible to the programmer and only adjusted by its parent node. This deep state is then used to determine if components are enabled or not. 

so when you have a node tree like this:
Key: 
 "+" visible
 "-" hidden
 E enabled
 D disabled

Start
----------
E + NodeParent
_E + NodeChildA
_E + NodeChildB

NodeParent:SetEnabled(false)
----------
D - NodeParent
_E - NodeChildA
_E - NodeChildB

NodeChildA:SetEnabled(false)
----------
D - NodeParent
_D - NodeChildA
_E - NodeChildB

NodeParent:SetEnabled(true)
----------
E + NodeParent
_D - NodeChildA
_E + NodeChildB


Similarly if you have a node tree with many parents:

NodeParentA:SetEnabled(false)
----------
D - NodeParentA
_E - NodeParentB
 __E - NodeBChildA
 _E - NodeChildB

NodeParentA:SetEnabled(true)
----------
E + NodeParentA
_E + NodeParentB
___E + NodeBChildA
_E + NodeChildB

NodeParentB:SetEnabled(false)
----------
D + NodeParentA
_D - NodeParentB
___E - NodeBChildA
 _E + NodeChildB

-------------------------

Modanung | 2020-04-30 14:30:08 UTC | #2

`SetDeepEnabled` is always recursive, but - unlike `SetEnabled` and `SetEnabledRecursive` - it does not modify `enabledPrev_`. `ResetDeepEnabled`  recursively sets the enabled state back to `enabledPrev_`. So `SetDeepEnabled` can be used to *store* the enabled state of an *entire branch* of nodes so the state of each can node be easily *restored* with a single call to `ResetDeepEnabled`.

https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Scene/Node.cpp#L1992-L2003

https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Scene/Node.cpp#L718-L734

-------------------------

Avagrande | 2020-04-30 16:31:45 UTC | #3

I understand how these work I am mainly concerned with the fact that I have to call SetEnabledRecursive or SetDeepEnabled on child nodes when I want to disable the tree. I have to then take care of two states: deep and actual enabled state. It might be fine in small case scenarios but for example when I switched my general purpose UI to use Nodes it became very difficult to keep track of the states. 

In my fork I modify it so that I can retrieve the deep enabled state whenever I want from a calculation not something the user decides, this is used internally only.
The point of this is to reduce the need to use either SetEnabledRecursive or SetDeepEnabled because I think they are not actually all that useful and instead create undue stress as I am forced to keep track of the Deep state.  My question is fundamentally why this is done? is there a practical reason for this which is vital to other components such as improved efficiency or net code etc 

https://github.com/Polynominal/Urho3D/blob/test/Source/Urho3D/Scene/Node.cpp#L1987-L1998

Then in my components I check if the component is active using the criteria. 
https://github.com/Polynominal/Urho3D/blob/test/Source/Urho3D/Scene/Component.cpp#L270-L273

-------------------------

SirNate0 | 2020-04-30 18:12:57 UTC | #4

Is it possible with your changes to disable a node but keep it's children enabled?

-------------------------

Avagrande | 2020-05-01 05:41:46 UTC | #5

Yes. 

It will never change the enabled state without the explicit use of SetEnabled. However it will check if its parent node is enabled to see if it should enable its components or not. 

so If you disable the parent note using SetEnable on any of the children this will have no immediate effect as the components will remain disabled. However if you then enable the parent node your previous changes using SetEnabled will still remain.

This is useful because you don't need to decide if you should be using SetDeepEnabled or SetEnabled for any one scenario. Additionally you don't need to use ResetDeepEnabled. 
This was particularly useful in my own UI system as I didn't have to do conditional checks to see which one I should use and when I should reset the deep state.

-------------------------

QBkGames | 2020-05-03 00:34:31 UTC | #6

[quote="Avagrande, post:1, topic:6129"]
Is there a reason why there needs to be 4 of them?
[/quote]

Yes there is. I remember being confused about these functions myself when I first started trying them out, but eventually I ended up using all the variations in my game "Planetoid Escape" (not in the UI though, in the game world itself) and cannot do without them all. I'm sorry I cannot give you concrete examples as this situation was over a year ago (I think), and I forgot the details, but trust me there are cases where they are all needed.
So, yes the code has more complexity to allow more flexibility. I do remember that, once I figured out how they work and what they are useful for, I still thought the function names and/or comments/explanations were confusing (at least to me).

-------------------------

QBkGames | 2020-05-03 00:47:44 UTC | #7

I'm starting to remember a use case. Hypothetically speaking, say you have an UI Panel that contains a number of child elements. While the panel is enabled, you want to be able to enable/disable some of the children. Then, you may want to disable and re-enable the whole panel, but when the panel is re-enabled, the state of the children should stay the same as it was when the panel was disabled. To achieve this functionality, I believe (as far as I can vaguely remember), you need the entire variation of all those functions.

-------------------------

Avagrande | 2020-05-04 18:07:42 UTC | #8

Yep thats exactly the situation I was in. I found it very clumsy to use all the different variations so I just modified how the SetEnabled worked as I previously described. such that SetEnabled alone worked to replace all the deep state related functions. 

The point of this thread is to ask if that change could potentially brake things because if possible I would like to share my change with everyone else as it would make the manual management of the deep state not necessary. I wanted to know why that decision has been made to include so many variations just in case there is something I am not aware of.

-------------------------

SirNate0 | 2020-05-04 18:41:09 UTC | #9

Your changes, as I understand them, would make it impossible to have functionally enabled children (i.e. related to the components, which actually do things like show up on screen). If I'm mistaken feel free to correct me.

Granted, I'd probably be fine with this sort of behavior in general, but I think it would break the present behavior of the engine.

-------------------------

Avagrande | 2020-05-06 15:44:13 UTC | #10

I am not sure what you mean by functionally enabled children? 

Do you mean that if the parent node is not enabled it is not possible at any point to make the children nodes visible ( enabled components ) unless the parent is enabled? if so what parts of the engine make use of this?

Thanks for letting me know btw. Its true that there needs to be a few changes within game scripts but so far I have not really noticed any core engine features that have been broken as a result of this change. I am a bit concerned if I will trip on one or not, but I use the engine quite a lot and so far It hasn't caused problems with how the core of the engine works.

I think for now I will just keep this change for myself.

-------------------------

