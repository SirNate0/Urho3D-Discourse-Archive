slapin | 2018-03-21 11:36:20 UTC | #1

Hi, all!
Is there anybody using Urho on Linux and using Urho GUI and running in window?
I guess nobody, as in this configuration GUI is as broken as it possibly could be.
What I guess, the layout is never updated on window changes. 3D layout works great,
this only affects GUI. Window change event works fine, but GUI seems to be ignoring it and
always works in 1024x768 which is set as default. In full screen everything works fine.

In the code I see that it should react on resolution, but for some reason it completely ignores
the changes.

I know Linux user base and especially desktop is in decline and probably will be at 0 soon,
so current support is not worth it, but are there any alternatives to stock GUI which would work
on Linux and be cross-platform? (I need Linux and Android support). I asked this question before,
but probably something changed over years?

Thanks.

-------------------------

jmiller | 2018-03-21 14:02:18 UTC | #2

./Editor.sh -w -s -x 1920 -y 1080
Urho editor (current git master) seems to be working as expected on Linux here. :penguin:
although the right/bottom panels do not automatically fit to an expanded main window (this can be done manually).

I don't see customizable architecture (i.e., desktop) or Linux going obscure soon. :)

TurboBadger also works on Android.

-------------------------

slapin | 2018-03-21 14:16:49 UTC | #3

I know I can do everything manually, redrawing from root widget, but
that is extremely tedious.
Also you manually set window resolution, which is not common case, as
generally it is set
by window manager.
As about desktop - I generally being told by windows people that there
is zero GUI problems
(at least no problems I report) so I guess it is either
system-specific problem or
I'm being trolled (which is not too impossible too).

What I do:
1. I create dumb program which listens to resolution events, and I see
valures change as I
change window size, so SDL does everything right.
2. I create single button which is aligned to center on top level. It
is centered at
1024x768 window center (the default resolution)
No resolution changes affect this.

So to make GUI work for windowed resolution I have to manually redraw
all GUI elements,
right? I see that resolution change events are handled within GUI,
what is their purpose then?

-------------------------

Eugene | 2018-03-21 14:21:50 UTC | #4

[quote="slapin, post:3, topic:4112"]
I create single button which is aligned to center on top level. It

is centered at

1024x768 window center (the default resolution)

No resolution changes affect this.
[/quote]

Do you mean that the button stays at (512,384) regardless of resolution changes?

-------------------------

slapin | 2018-03-21 14:55:12 UTC | #5

Yes, it is not following window center.
Also it looks like initially UI is fed by some default setting (1024x768) and
after wm changes resolution to 2560x1440 (in my case) the center ends
up near top left.
If I manually update (remove all GUI and re-create it), it sort of works.
I currently did manual GUI reset using timed updates. But if I
implement full GUI instead
of single button, I think that will not work too well. Is there some
shortcut instead of full manual update?

-------------------------

Eugene | 2018-03-21 14:56:38 UTC | #6

[quote="slapin, post:5, topic:4112"]
Is there some

shortcut instead of full manual update?
[/quote]

Try anchors of UI elements, (0.5, 0.5) for centering.

-------------------------

slapin | 2018-03-22 05:35:25 UTC | #7


        Graphics *graphics = GetSubsystem<Graphics>();
        ResourceCache *cache = GetSubsystem<ResourceCache>();
        Input *input = GetSubsystem<Input>();
        UI *ui = GetSubsystem<UI>();

        graphics->SetWindowTitle("Dungeon");
        input->SetMouseVisible(true);
        XMLFile *style = cache->GetResource<XMLFile>("UI/DefaultStyle.xml");
        ui->GetRoot()->SetDefaultStyle(style);
        Button *button = new Button(context_);
        button->SetName("new");
        ui->GetRoot()->AddChild(button);
        button->SetMinAnchor(0.5f, 0.5f);
        button->SetMaxAnchor(0.5f, 0.5f);
        button->SetEnableAnchor(true);
        button->SetFixedSize(100, 60);
        button->SetStyleAuto();
        SubscribeToEvent(button, E_RELEASED, URHO3D_HANDLER(Urho3DPlayer, StartGame));


Result is the same - centered around 1024x768 window.

-------------------------

slapin | 2018-03-22 05:40:31 UTC | #8

I guess root UIElement is not updated on window changes.

-------------------------

Eugene | 2018-03-22 06:55:49 UTC | #9

True. Resize root in resize event handler. This plus anchors shall make things work.

-------------------------

slapin | 2018-03-22 06:59:38 UTC | #10

Thanks a lot! The problem is gone now.
I wonder, it should have worked even without this hack, but for some reason it won't...
Anyway I now finally can continue with GUI. Thank you so much!

-------------------------

Eugene | 2018-03-22 07:33:55 UTC | #11

[quote="slapin, post:10, topic:4112"]
I wonder, it should have worked even without this hack, but for some reason it won’t…
[/quote]

I've just checked. There's `UI::ResizeRootElement` that's called sometimes. I suppose it was designed to resize root element when needed. I'll check it later.

-------------------------

Eugene | 2018-03-25 11:42:03 UTC | #12

I’ve just checked things. On windows, both for dx9 and gl, root element is resized automatically because of ChangeMode event.
IDK ashy it doesn’t work for you. What resize event do you subscribe in order to fix the problem?

-------------------------

slapin | 2018-04-02 01:41:14 UTC | #13

Sorry for not answering, I was very sick for a while, so I could not find energy to check and post.

I did some investigation on my side. I do not do anything fancy, and GUI starts working.
```#C++
void Urho3DPlayer::HandleScreenMode(StringHash eventType, VariantMap& eventData)
{
...
}
```
And I subscribe as
`SubscribeToEvent(E_SCREENMODE, URHO3D_HANDLER(Urho3DPlayer, HandleScreenMode));`

Using that I set size of root component with SetSize()

This is what I did first, and it works. When I dig farther, I see that it is already done in engine, so why
do I need this is a question. So I added log message to event handler and see that everything works fine and the same in both engine and my code. After that I disabled SetSize() in my event handler and it STILL WORKS.
After that I reverted changes to my code and checked, so no, problem is still there. So I left with
event handler printing log message, which makes thing work. No, I don't want to touch it anymore.
Something weird is going on...

Anyway, moving forward from it - is there some way to address element size issues. While position issues can be handled by anchors, is there some similar way for sizes? The problem is that some UI elements
fail to size off parent and have to be sized manually (i.e. ScrollView). Is there some relative solution to make ScrollView to be of parent size without need to manually resize it every time window size changes?
I now use the above handler for that, but it looks not nice at all.
Thanks!

-------------------------

Eugene | 2018-04-02 05:44:47 UTC | #14

Sounds like really weird problem. 

Sizes could be controlled via layout, I always prefer this way. It may be hard to configure sometimes tho.

-------------------------

slapin | 2018-04-02 06:51:44 UTC | #15

What do you mean by layout? SetLayout() seems to have no effect on
ScrollView at all,
I still have to SetSize() to make it work. UIElement, Button, Window
do not have this problem.
The effect of SetLayout() is there but it does not affect size. i.e I
see LM_VERTICAL
effect or LM_FREE effect on child elements after I set ScrollView size
via SetSize() but it refuses to use parent's size, which is expected.

-------------------------

Eugene | 2018-04-02 08:18:10 UTC | #16

Urho UI is explicit. It does exactly what is said to do.
Sometimes it may be tricky to say what to do tho.

If you call SetSize, your element would have this size, whatever you do. Because you _asked_ this element to have exactly this size.
If you want element to be resizable, set min and max sizes separately, then set parent layout, and it would resize elements according to min/max sizes and layout properties. Same with position and anchors.

-------------------------

slapin | 2018-04-02 09:39:27 UTC | #17

The problem is that one have to guess what to do every time, because
behavior is not consistent and for no apparent reason. I.e. you don't
need to Set{Min/Max/}Size() for majority of components (at least ones,
which I use, UIElment, Window, Button, Text) but need to do this for
some of them (ScrollView). I think consistency would be nice in this
case. Also, when you need resizeable UI it is often hard to properly
set sizes for all components, and it looks like attempt to patch-up
something broken, as I see no design idea in it. It looks random at
best. I think it doesn't affect most game UIs as these do not use
anything except UIElement, Button and Text, but it looks like wanting
impossible things is my curse.

-------------------------

Eugene | 2018-04-02 09:45:47 UTC | #18

[quote="slapin, post:17, topic:4112"]
The problem is that one have to guess what to do every time, because

behavior is not consistent and for no apparent reason.
[/quote]

If you explain/draw _excatly_ what kind of UI you'd like to have, it'd be easier to deal with.

-------------------------

slapin | 2018-04-02 11:37:28 UTC | #19

Well, I do not want to put this burden on anyone, but since you're asking...
I need 2 GUIs for different things - 1 is in-game relationship editor
and 2 - AI behavior tree
editing tool.
First one is (root is excluded)
UIElement(LM_VERTICAL)
-- Window(LM_VERTICAL)
---- ScrollView(LM_VERTICAL)
------ UIElement(LM_VERTICAL) (many of this)
-------- Text (Category1)
---------- UIElement(LM_VERTICAL) (many of this)
------------ Text (Category2)
-------------- UIElement(LM_VERTICAL) (many of this)
----------------UIElement(LM_HORIZONTAL) (many of this)
------------------Button(LM_VERTICAL, vcentered) (5 or less), person
-------------------Text(hcentered) (person name)
--Window(LM_HORIZONTAL)
----Button (LM_VERTICAL) (about 8, actions on person object)
------Text (description of action for each button)
----UIElement (LM_VERTICAL) (property list)
------UIElement(LM_HORIZONTAL) (for each property)
--------Text (property name)
--------Text (property value)

Second one:

UIElement(LM_HORIZONTAL)
--Window(LM_VERTICAL)
----ScrollView(LM__FREE) (node editor)
------Button (for each node, draggable, clickable)
------Sprite (making arrows using these, any other way?, lots for each
node connection)
--Window(LM_VERTICAL)
----Button (for each control)
------Text (each button description)
----UIElement(LM_VERTICAL) (property editor)
------UIElement(LM_HORIZONTAL) (for each property)
--------Text (property name)
--------LineEdit (property data)

Both were implemented but are very rigid and unstable, unscalable,
hard to modify.

-------------------------

Eugene | 2018-04-02 11:44:44 UTC | #20

Then, what kind of scalability do you want to achieve?
Do you want to move&scale items within ScrollView automatically?

-------------------------

slapin | 2018-04-02 12:11:21 UTC | #21

I want application window to be scaled with UI updating.

Currently I have to do weird math to set size of ScrollView, which is
really looks hacky at best.

 Ideally I want it so that I do not have to manually fixup things.
Basically this means ScrollView is automatially filling its parent in
the same way as other UI elements do. So if I have LM_VERTICAL parent
with 5 elements, 4 buttons and 1 ScrollView I should not need to
handle ScrollView specially for it to behave like buttons
(filling 1/5 of parent vertically and 100% horizontally), so for it to
have intuitive behavior.
If that is not possible, this should be documented among with widget
list which need special handling and what that special handling is to
make it standard. This is worst feeling - not intuitive behavior and
nowhere to go for information.

-------------------------

Eugene | 2018-04-02 12:15:01 UTC | #22

[quote="slapin, post:21, topic:4112"]
Basically this means ScrollView is automatially filling its parent in

the same way as other UI elements do.
[/quote]

Meh... basically, Editor Hierarchy window _is_ ScrollView plus some buttons. AFAIK it works automatically in some way, no?
If you set min/max size to 0/inf, `ScrollView` _must_ automatically scale when parent has non-free layout.

-------------------------

slapin | 2018-04-02 12:28:52 UTC | #23

Well, the observed behavior is inconsistent with other elements.
Why min/max values are set to 0 for ScrollView?
Why difference with other elements?

Either way thanks for help - I'm not trying to make you fix it or something,
I don't think anything really can be done here in current circumstances.
I was just curious. Will try to use @Sinoid approach to imgui for node editor and will look for some other solution for in-game UI.

-------------------------

Eugene | 2018-04-02 13:01:54 UTC | #24

[quote="slapin, post:23, topic:4112"]
Why min/max values are set to 0 for ScrollView?

Why difference with other elements?
[/quote]

Min/max sizes are _defaulted_ to 0/inf for UIElement and its descendants.
So, each UI element will always fill parent with non-free layout till the borders (by default).

`Text`, on the other hand, automatically sets min width (to avoid unwanted text clipping) and also set fixed height (to maintain contant line height)

Then, every element with non-free layout can't be less than its children. So, `Button` with text has restricted min size (inherited from underlying `Text`) and unrestricted max size.

So, if you make vertical `Window` and put there `Button` with `Text` and `ScrollView` w/o any settings, they would fill the window 1/1 unless you squash it.

Note that `ScrollView` breaks this chain of size inheriting. Sizes of inner elements doesn't affect size of host `ScrollView` in any way.

[quote="slapin, post:23, topic:4112"]
Either way thanks for help - I’m not trying to make you fix it or something,

I don’t think anything really can be done here in current circumstances.
[/quote]
Such kind of issues means either bug or lack of docs. Nice chance to shoot it down.

-------------------------

slapin | 2018-04-02 13:15:28 UTC | #25

Well, but ScrollView gets size of 0x0 unlike other elements. I think it should get size required by parent container element, as if it was button or other element. It is not logical to set it to 0x0. Also I think Urho UI is too verbose with settings and lacks defaults.
i.e. for Button one have to SetLayout(), SetStyle/SetStyleAuto(), etc. which have to be always present. In most GUI toolkit you create container, put widgets in it and you have something working immediately. In Urho UI code looks very verbose and too much code for what it does. I do overcome this using fancy functions, but I think there is something which needs to be done there... At least for SetLayout()/SetStyle() stuff.

-------------------------

Eugene | 2018-04-02 18:58:22 UTC | #26

[quote="slapin, post:25, topic:4112"]
Well, but ScrollView gets size of 0x0 unlike other elements. I think it should get size required by parent container element, as if it was button or other element. It is not logical to set it to 0x0.
[/quote]

Default ScrollView takes exactly the same amout of space as other stretchable things.
![image|482x500](upload://3yqtUMRaB4lRvaApiD92FrZ3MVV.png)

However, `Window` is always squashed to min size by default, so objects with zero height would be invisible.
There _is_ logic.
Take as little space as possible, but not less than minimum required.
If size is greater than minimum, stretch everything equally, but no more than allowed by element restriction.

-------------------------

Sinoid | 2018-04-04 09:40:50 UTC | #27

ImGui isn't going to do you any favors for layout. It'll probably just make it an exponentially larger headache. The paradigm sucks at layout.

-------------------------

slapin | 2018-04-04 11:07:27 UTC | #28

It (ImGui) allows for lighter/easier node editor than with stock UI
which is very serious plus for me. It also looks like it is more
predictable regarding what goes where, but I did not dig it seriously
(except for node editor capabilities). I will of course check its
usability,
but it seems to be able to create scalable/resizeable UIs, as I see
its applications.

-------------------------

