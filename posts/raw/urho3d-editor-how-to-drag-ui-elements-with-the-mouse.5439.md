HappyWeasel | 2019-08-08 21:30:38 UTC | #1

Hi,

I can use the editor to create my UI Elements, all works fine. But I have to manually edit the Position and Size Attributes in the Attribute Inspector of an UI Element. Is there a possibility to drag UI Elements with the mouse ? 

Thanks.

-------------------------

dertom | 2019-08-09 00:13:58 UTC | #2

Hi there and welcome.

[quote="HappyWeasel, post:1, topic:5439"]
Is there a possibility to drag UI Elements with the mouse ?
[/quote]

I would say no. The closest thing to dragging would be to start dragging on the little "arrow up/down"-icon beside the value in the attribute panel for fine tuning. But inplace resize is not possible (at least not that I know of)

-------------------------

Leith | 2019-08-09 06:47:50 UTC | #3

Hi, yes we can drag UI elements - at least I have applied it to entire windows...
[code]

        SubscribeToEvent(window_,     E_DRAGMOVE,     URHO3D_HANDLER(MyApp, HandleWindowDragMove));

...


    /// User is dragging our GUI window
    void HandleWindowDragMove(StringHash eventType, VariantMap& eventData){
        /// Unpack the 2D position delta
        using namespace DragMove;
        int dx = eventData[P_DX].GetInt();
        int dy = eventData[P_DY].GetInt();
        /// Compute new window position
        IntVector2 pos = window_->GetPosition();
        pos.x_ += dx;
        pos.y_ += dy;
        /// Apply new window position
        window_->SetPosition( pos );
        /// Display new position in window title
        auto* windowTitle = window_->GetChildStaticCast<Text>("WindowTitle", true);
        windowTitle->SetText( String(pos.x_)+", "+String(pos.y_));

   //     URHO3D_LOGINFO(String(dx)+", "+String(dy));

    }
[/code]

-------------------------

Leith | 2019-08-09 06:48:34 UTC | #4

You also need to set the ui element as movable...

-------------------------

HappyWeasel | 2019-08-09 07:06:52 UTC | #5

Hi Leith,

Thanks for taking your time to answer.. There was a bit of misunderstanding, though: I know how to programmatically do this in code at runtime :-), I was only wondering whether the provided Urho3D Editor supported dragging of UI elements when I am layouting them.

Thanks

-------------------------

Leith | 2019-08-09 07:11:43 UTC | #6

Ah, my mistake.
To be honest, I only recently got the editor to run reliably, and I don't know it well enough to comment. What I do know, is that I had to refactor my code, to make it editor friendly. Example? My app had two scenes, one for the game, and one for scene manager and gamestates ... this was a terrible fit with the editor - I got it to work in the end, but I think it was ultimately a bad design pattern for working with the editor.

-------------------------

HappyWeasel | 2019-08-09 07:10:07 UTC | #7

Thanks dertom,

I might hack around the urho editor code to provide that functionality (maybe: picking UI element and pressing shift allows dragging the element) ..

PS: I know layouts are the way to go, but I like fixed positoning for prototyping purposes . 

Greetings

-------------------------

guk_alex | 2019-08-09 08:20:42 UTC | #8

Actually, you can drag window element inside editor (and the game too) - 'Is Movable' option make it happen. But it does work only with one Horiz/Vert Alignment setting - Left/Top.

-------------------------

guk_alex | 2019-08-09 08:46:28 UTC | #9

And yes, you can just hack into editor to allow you key combination to set the 'Position' field of the current selected element, it seems quite easy.

-------------------------

codexhound | 2019-08-09 09:10:27 UTC | #10

Is there any good tutorial on the editor? I have played around with it a little but haven't been able to use it for UI development as I creating the ui elements don't show up on the screen when I create them though I do see the property box. Mostly I've been doing that programmatically so far. And yes, to make something movable just set its movable property.

-------------------------

dertom | 2019-08-09 09:35:30 UTC | #11

For the UI elements created in the editor you need to set the size values in the attribute panel. E.g. if you start with the uiwindow. Worked for me.

-------------------------

Modanung | 2019-08-09 19:58:15 UTC | #12

Welcome @HappyWeasel! :confetti_ball: :smiley:

I'll consider this a feature request for [ManaWarg](https://discourse.urho3d.io/t/manawarg/5403/).

-------------------------

HappyWeasel | 2019-08-09 19:26:19 UTC | #13

Hi,

> as I creating the ui elements don’t show up on the screen when I create them though I do see the property box

I think for UI Elements (the generic container / baseclass), the initial size is zero. So you have to set the size property for it to show up (blue border) and probably also set the position to some free space on your screen 

Bye

-------------------------

Leith | 2019-08-10 05:34:20 UTC | #14

I tried to load a movable window layout into the editor - layout for a window created in code, and dumped to xml for inspection in the editor / reload in the app.
I see what you mean - you can't (in the editor) move ui elements marked as movable - the dragmove event is not being serviced. We could get around this by either using script or injecting custom components into the UrhoPlayer host app... but simply moving something marked as movable seems fairly reasonable to expect of our editor!
There's more - the value of sliders never changes (in the inspector), it looks from here like the editor is fairly useless for editing/testing UI without additional support. On the bright side, drop down lists seem well-behaved :slight_smile:

-------------------------

Modanung | 2019-08-10 12:05:39 UTC | #15

Unmovable UI elements should also be draggable and mouse-scalable when designing them. I think we just need a better editor, and I could use some help making this a reality.

-------------------------

Leith | 2019-08-10 12:37:16 UTC | #16

It's all in script, this is really not my thing, but I could lower myself...
If I saw benefit for myself, what avenue? PR? :slight_smile:

-------------------------

Modanung | 2019-08-10 12:53:34 UTC | #17

[quote="Leith, post:16, topic:5439"]
It’s all in script, this is really not my thing
[/quote]

That's one of the reasons I started the [ManaWarg](https://discourse.urho3d.io/t/manawarg/5403) project instead of modifying the AS editor.
[![Gitter](https://badges.gitter.im/LucKeyProductions/ManaWarg.svg)](https://gitter.im/LucKeyProductions/ManaWarg)

-----

https://discourse.urho3d.io/t/new-urho3d-editor-update-from-2017-11-03/2407/2

-------------------------

Leith | 2019-08-10 13:04:01 UTC | #18

Hooking up execution of named functions to c++ callers was never a problem - but getting data back used to be. Hopefully I've helped to put some cracks in the language barrier - we no longer need to start in script land and have script land own our objects, we can now use script to get work done, and mostly stay in native land. I see it as a positive, and like you, I've started some very early work on a realtime editor. It's not as fancy as yours, but its fully stateful, and rock solid. It will serve as a good lesson on GUI basics as well as data persistence in Urho projects :) To be honest, if there was any one part of the editor I wanted to touch immediately, it would be the terrain editor controls - adding realtime terrain painting is fairly trivial.

-------------------------

Modanung | 2019-08-10 13:18:58 UTC | #19

Seen?
https://discourse.urho3d.io/t/u3d-terrain-editor/765

-------------------------

Leith | 2019-08-10 13:19:59 UTC | #20

Why is this stuff not already in there? What are we waiting for?

-------------------------

Modanung | 2019-08-10 13:22:13 UTC | #21

Nobody's waiting. We're just scattered.

> [:musical_note: **Staple It Together** by _Jack Johnson_](https://www.youtube.com/watch?v=xTe4oFZial4)

@HappyWeasel Sorry for hijacking your thread.

-------------------------

Leith | 2019-08-10 13:21:53 UTC | #22

I'm sure he won't mind - I'll start looking closer at the editor script tomorrow with a view to adding some missing functionality that I expect in a production tool

-------------------------

