capelenglish | 2019-04-17 22:22:34 UTC | #1

Can anyone point me to an example that uses the SplinePath component? I'm trying to get one to work, but having trouble including this component in my code. I've included SplinePath.h and SplinePath.cpp in my main directory, but it crashes when I try to move.

splinePath->Move(eventData[P_TIMESTEP].GetFloat());

-------------------------

jmiller | 2019-04-17 17:48:05 UTC | #2

Hi,

While SplinePath is not demonstrated in Urho samples, there are a few informative [posts on SplinePath](https://discourse.urho3d.io/search?q=SplinePath) like https://discourse.urho3d.io/t/how-to-use-logic-splinepath/569

HTH

-------------------------

capelenglish | 2019-04-17 18:19:37 UTC | #3

Thanks for the reply jmiller. I read many of these posts before I asked the question. Maybe I'm missing something more basic, like how to include components. What I've done is include SplinePath.h in my main.cpp file. 

When I go to compile main.cpp it can't find SplinePath.h. So I copied SplinePath.h and .cpp to my main directory from the Scene directory in Urho3D source code. Now it will compile, but when I call Move in my HandleUpdate function, I get a seg fault.

-------------------------

jmiller | 2019-04-22 14:29:59 UTC | #4

This include directive should work:
`#include <Urho3D/Scene/SplinePath.h>`

To see the specific error might need more information or code.

Perhaps [SplinePath::Move()](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Scene/SplinePath.cpp#L222) might fail if passed a bad node pointer in `SplinePath::SetControlledNode(Node* controlled)`, but this is only a guess.

Running your program in a debugger should expose more detailed information about the crash.. unless it's a [Heisenbug](https://en.wikipedia.org/wiki/Heisenbug). :bug: :)

And just found: our very own @sirop has a SplinePath repo. :) https://github.com/sirop/Urho3d_SplinePath

-------------------------

capelenglish | 2019-04-17 19:06:43 UTC | #5

Thank you! I think I've figured out my problem...

-------------------------

dertom | 2019-04-18 08:15:45 UTC | #6

> Thank you! I think I’ve figured out my problem…

So, what was it, @capelenglish ? I personally 'do like' posts with an dead end like this, especially when you have the same problem...(I hope you heard the irony)

-------------------------

capelenglish | 2019-04-22 11:06:17 UTC | #7

Sorry, didn't mean to leave anyone hanging...

jmiller pointed me to an example, which was my original question. My problem was that I was passing a bad node pointer when setting the controlled node. After reviewing the sample code I was able to determine where my problem was.

BTW, I don't see where or how to mark the issue resolved. How do I do that?

-------------------------

jmiller | 2019-04-22 14:18:07 UTC | #8

Glad you got it sorted.

[quote="capelenglish, post:7, topic:5107"]
mark the issue resolved. How do I do that?
[/quote]

The 'mark solution' button is revealed with the ellipsis '`...`' button by 'Reply'.

-------------------------

