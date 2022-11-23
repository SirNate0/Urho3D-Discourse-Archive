Sinoid | 2019-05-23 13:20:00 UTC | #1

Edits: fix ephemeral links.

Because I have seen an increasing number of stars/watches etc on my QT based editor at https://github.com/JSandusky/UrhoEditor I'm starting this thread so that persons interested can be aware of what is going on and where it is as well as state their items of concerns.

Superficially it looks like it's been static ... but it really hasn't been.

Recently I have been exploring avoiding data-binding in order to minimize the woes of GUI programming. Because I use the same code-base for that QT editor and a different project it is often difficult to reconcile the two. A lot of potential is lost in dealing with the data-binding woes of retained GUIs. Reconciling Core Urho3D and "my version of Urho3D" has been unpleasant to say the least. Never mind that I intend this toolset to be usable outside of Urho3D.

In trying to find ways to make exploratory efforts and easier UI I gave IMGUI paradigms a shot. For this I turned to Nuklear as it has a draw scheme that fits QT whereas IMGUI does not (barring writing a barycentric-rasterizer in QT ... good luck with that).

![Nuklear in QT](upload://s1HEPUc2Y2zryF77lGsTkBRPJ6a.png)

The results were excellent. While Nuklear's widgets are very janky, I've already put in the effort of making several of them (text edit and slider) less janky and more usable. I will continue to do so for other widgets as is viable.

In the UI pictured above there are more than 1k draw commands being issued to QPainter per IMWidget (6 of them) and there is no consequence on the real-time performance of the viewport. It's viable ... that's just a debug build.

Once the editor is bound to AngelScript I believe that this approach will give Urho3D users the same editor powers that Unity users have ... if not much more by virtue of having the source.

Progress has been happening, even if you don't see it in github. So many options are opening up, prepare for an influx - this is a geyser.

- Why no CMake files?
     - CMake hates QT, it was a shit-storm to compile Aster's QT particle editor on windows via CMake, a complete shit-storm ... it just doesn't work - you'll get things working faster doing it yourself
     - CMake falls on its face when dealing with code generation, this project will very quickly encounter automatic reflection scenarios that require code generation

**Note:** I do not consider Nuklear suitable for Node-graphs ... I'll be exposing the node-graphs used for the texture graph editor in a couple of weeks. Node-graphs really do need to be retained, they're systems of often absurd consequences.

-------------------------

Sinoid | 2019-05-23 13:20:00 UTC | #2

This has definitely been the right choice so far. After implementing "hotspots" (areas that indicate mouse cursor, repaint needs, and tooltips) in Nuklear I've eliminated 90% of unnecessary repaints and I'm interacting more closely with QT. Once I slap in QIcon/QImage support it's basically as done as it can get.

![Image](upload://j3qp6jl5WYd6t2h8soij1p92FRV.png)

[Direct Image Link](http://imgur.com/a/8CHRh)

IMWidget now provides adequate helper methods that return true/false as to whether or not the value was actually changed (taking the value by reference/pointer). Out of the box Nuklear doesn't care ... and was never really designed for scenarios where the consequences of a "false edit" could be substantial (in my case that means rerunning contouring, regenerating bone weights, regenerating UV coordinates, and lastly regenerating textures .... not a fast enough process to have happen for false edits).

There's still a lot to do to catch up with where I was at with pure QT and custom QT widgets, but it's looking very promising. At this point, nothing can be as bad as the hell I went through to make combo-boxes happen through Nuklear in QT.

That bit of work, for not having to care about what undo/redo does, is priceless. By the end of tomorrow, I'll know for sure when I dive into collections and curves whether this is the right way or the wrong way ... but since collections drove me here (the tree on the far left of the image is also an IMGUI-style widget, just a custom one I wrote designed for tree/list/layer scenarios) I suspect it'll go well (uses a similar hotspot based model, which I've used before for real-time report editing [column widths, fonts, etc]).

And I'm using crap-hardware (Surface Pro 1 - Intel HD4000) to judge what's okay and what is not.

-------------------------

Sinoid | 2019-05-23 13:20:00 UTC | #3

I couldn't have been more wrong about Dear-IMGUI. With just a little bit of evil (of the slap a bunch of structs in a union variety) it was an easy job to write a backend for a pure QT scenario.

![Low resolution](upload://xRKVI3zQOjH7CieH05bgMBON0fb.jpg)

[Full Resolution Version](http://i.imgur.com/ZagQj2T.png)

What's going on in the above:

- Dual-contouring is running at 60fps in OpenCL (not a lot of cells though, it's just a ball)
    - Which is just a stupid stress test to be running constantly
- Urho3D is rendering at 60fps the slightly late results of the contouring
- A custom immediate-mode tree is painting every 50ms
- 2 Instances of Dear IMGUI context are running the Dear IMGUI demo
    - Both @ 50ms refresh rate
    - They're 100% freestanding from each other (stylable independently, etc)
- Old QT based property editor is sitting there, flashing a cached paint image like QT does
- Nuklear is running the same property editor as the above
    - Updating @ 50ms 
    - Not visible but there's embedded QT widgets in the Nuklear IMGUI instance for dealing with tricking situations like combo-boxes ... they are very unhappy about being embedded in an IMGUI

---

I've settled on my direction now. 

Nuklear was promising but it was going to be a lot of work to bring it up to something livable for extended use. Extensive swathes were going to have to be torn out and replaced in order to make TAB/SHIFT+TAB'ing through the UI viable globally ... that's pretty much required for anything you're going to use regularly.

Code for the base of Nuklear stuff in QT: https://gist.github.com/JSandusky/71b50cd7addf7daea02060f25a0f18b1 (IMWidget.h/.cpp is what you're really after, most of the Nuklear file changes are just "make me happy changes").

---

So I gave Dear-IMGUI another look and it pretty much fell right into place (most likely because I had just done similar with Nuklear).

DearIMGUI really won me over. There's a bannana-ton of OSS already using it (if you need something special you can probably find something you can slap into a lambda, toss the widget in a dock, and be done), I had to write fewer helper methods, and it's sufficiently well-behaved and well-written to be easy to match the places QT widgets are still used without creating a jarring experience.

A bit more work tying it all into QT for drag/drop, embedded QT widgets, and making sure my image/icon caching from the Nuklear stuff wasn't incredibly dumb/misguided and it's off to the races.

-------------------------

johnnycable | 2017-05-19 11:19:46 UTC | #4

Looks gorgeous. Yes Imgui is the way imho if you want s.t. oss, lots of projects using it.
Are you using QT for replacing Imgui missing features?

-------------------------

Eugene | 2017-05-19 12:02:32 UTC | #5

What are your plans for this Editor, BTW?

I've started thinking about joining you in Editor's developing, since I think it's a kind of dumb to do duplicate work, and you definetely have done more than me on that way.

-------------------------

sabotage3d | 2017-05-19 12:35:51 UTC | #6

Looks really good can't wait to try it out.

-------------------------

smellymumbler | 2017-05-19 18:06:15 UTC | #7

I love your translation/scale/rotation widget. I've been struggling a lot when trying to create one, so much that i eventually gave up and now i just use a matrix and a bunch of textfields. It works for me and my game, but i would love to learn how to do this properly. Do you recommend any specific material about it?

-------------------------

slapin | 2017-05-19 19:03:22 UTC | #8

I currently use draggable buttons for everything. Should be easier to do. Anyway, why don't you use Editor's gizmos?

-------------------------

Sinoid | 2017-05-20 03:49:44 UTC | #9

[quote="johnnycable, post:4, topic:3119"]
Are you using QT for replacing Imgui missing features?
[/quote]

Sort of, the two live together mutually. QT is still responsible for the main 'shell', OS dialogs and dialog shells, as well as drag/drop and clipboard data ... and obviously all of the QT goodness (QDir, QFile, QXml, etc ... the stuff where QT really shines for mostly working everywhere). Most likely QT will remain responsible for settings/configuration as well.

IMGUI popups though are ... interesting. I use QT for tooltips but there is witchcraft in handling the pop-ups.

Running an IMGUI inside of QT probably seems odd to some but it's actually eerily similar to what we used in MFC at a previous employer for multiple chem/safety products, only real difference is we were slightly more clever with painting in ways that make no sense with an IMGUI.

[quote="Eugene, post:5, topic:3119"]
What are your plans for this Editor, BTW?
[/quote]

In the idealogical sense? The 'viewport' and all the other data-files are the most important thing. Just "redoing the Urho3D editor in QT" is silly as it's there and it does in fact work. I consider core editor functionality + brushes to be the mandatory minimum.

Ideally, I'd like to do *run-within-editor* as long as the project follows "fashion XYZ" - though I haven't really looked at what that will really entail, not the slightest idea. Extended usage over "usage" basically, an example of that policy is that all *Mask* / *Flag* attributes have settings for naming each of the bits - showing the bit-name in a tooltip or in a side-by-side popup that lists all of the bits by name.

In a more life/push-cycle sense before "and now it's safe to actually fiddle with"? Wrapping up this IMGUI stuff, then pushing it all out. It should be much more approachable once the heaps of custom controls have been eliminated - much less noise to distract.

I could go on and on.

If you'd like to hop onboard I'd certainly appreciate the help. I'm on this full-time for the next couple of days so the latest should be in git relatively soon. If you're too gung-ho to wait, screwing around with CMake + QT to confirm whether I'm just an idiot or not would be super helpful ... it's wayyy back on my todo list and actually effects viability to non-Windows folks - or 'shell' sketches as I'm still not sold on the ribbon for how much real-estate it eats.

[quote="smellymumbler, post:7, topic:3119, full:true"]
I love your translation/scale/rotation widget. I've been struggling a lot when trying to create one, so much that i eventually gave up and now i just use a matrix and a bunch of textfields. It works for me and my game, but i would love to learn how to do this properly. Do you recommend any specific material about it?
[/quote]

It's based on ofxManipulator, painting is done through Urho3D::DebugRenderer, I only tweaked it for alpha-blend. There's [LibGizmo](https://github.com/CedricGuillemet/LibGizmo), [ImGizmo](https://github.com/CedricGuillemet/ImGuizmo), and Sony's ATF LevelEditor gizmos are pretty convenient to use. Technically the subject matter is "direct manipulation" ... not that it matters since that doesn't actually help googling. I'll inevitably ditch it for something less cludgy.

[quote="slapin, post:8, topic:3119, full:true"]
I currently use draggable buttons for everything. Should be easier to do. Anyway, why don't you use Editor's gizmos?
[/quote]

Originally I did use them early on, but I wanted planar handles, camemberts in rotation, and needed adding additional handles to be viable (such as manipulating a split ellipse function for sag).

-------------------------

Sinoid | 2019-05-23 13:20:00 UTC | #10

Almost there. Though I'll most likely post the basis of the DearIMGUI in QT stuff later today and update with a link to the files.

Shot of scene tree (Urho3D tree still hasn't moved over to *Repeater* yet, definitely not going to use DearIMGUI for manipulable trees), Resource cache browser, Profiler, and properties.

![Low Resolution](upload://7LfIcJIVSgMJ2LDRGNfyknxYK5s.jpg)
[Full-Res Version](http://i.imgur.com/FZQ8Yz5.png)

Although the Resource cache and Profiler are accessible through the debug HUD having them in GUI eliminates the screen space constraints so that the profiler can show **everything** and all resources from the cache (plus their reference counts) can be viewed ... which is pretty useful.

They're both really just *baseline* widgets. There's room for a lot more stuff going on in the Resource cache widget ([CPP file for resource cache widget](https://gist.github.com/JSandusky/f684a0be15984c84ed1e59d13a166538)) such as forcing dumps/reloads/OS-thumbnail-previews/etc (though the whole ResourceDirs thing makes OS thumbnails a big "WTF do I do" or I'd have done it already for rule of cool).

---

To-do list before a safe push has gotten tiny: 

- Missing support for a few types:
    - This new variant structure insantiy **[tiny]**
    - VariantMap **[tiny]**
    - Hack around Tags automatic cleaning **[???]**
- Drop targets (partial) **[just event hell]**
    - I'm far more concerned about supporting drop targets than drag sources
- Reduce jankiness of popup windows **[eternal]**
    - They work well, but they're probably an indefinite source of continued tweaking ... forever
- Move scene-tree over to `Repeater` **[refactor tedium]**
- Implement a reference for a 'resource document,' probably particle editor. **[minor]**
- External querying of QImGui state **[Pipe-dream]**
    - Hovering on a material resource-ref of a static-model? FLASHING DEBUG DRAW!
- Upgrade test windows to replacing old windows **[Reference hunting]**

-------------------------

johnnycable | 2017-05-24 12:53:57 UTC | #11

Wow. Looks gorgeous! :grinning:

-------------------------

smellymumbler | 2017-05-24 18:30:51 UTC | #12

Absolutely fantastic! :grinning:

-------------------------

Sinoid | 2019-05-23 13:20:00 UTC | #13

@johnnycable and @smellymumbler, thanks!

![Latest shot](upload://zoGK8M1mq2LKX26ooyxcqdsNP2N.jpg)
[Full Res](http://i.imgur.com/Krre48D.png)

I've been pushing out periodically over the past couple of hours. The latest pushes include everything pictured above. The scene tree has fully moved over to repeater now. And those release build issues should be gone.

I'll be returning to the property editor for completeness. After that I'll be rounding out the missing functionality from the Urho3D scene editor. I expect to have all core functionality there by next weekend.

Finally added [binary dir requisites](https://github.com/JSandusky/UrhoEditor/blob/master/BinDirSetup.md) and a [todo list](https://github.com/JSandusky/UrhoEditor/blob/master/ToDo.md).

@Eugene, and anyone interested in helping out, now that core stuff is pushed out it's viable to tackle specific types of documents (particle effects, materials, etc) (see [DocumentBase](https://github.com/JSandusky/UrhoEditor/blob/master/EditorLib/DocumentBase.h), [UrhoBaseDocument](https://github.com/JSandusky/UrhoEditor/blob/master/UrhoEditor/Documents/Urho/BaseUrhoDocument.h), and [UrhoSceneDocument](https://github.com/JSandusky/UrhoEditor/blob/master/UrhoEditor/Documents/Urho/UrhoSceneDocument.h)). Pre-empt your document's global property page in [UrhoDockBuilder](https://github.com/JSandusky/UrhoEditor/blob/master/UrhoEditor/Documents/Urho/UrhoDockBuilder.cpp) ahead of UrhoIMPropertyEditor's addition (or add index/priority support before I do). Do what you have to do for your sanity, it can always be amalgamized later.

If any build issues are encountered please raise a Github issue for it so I can fix it. CMake scripts are inbound, though they will require environment variables and potentially single line fixes for your use. Those scripts aren't a cross-platform bullet though as the InputManager for the viewport, video-card/CPU stats, and thumbnail reading are all OS specific things that require support elsewhere.

-------------------------

George1 | 2017-05-30 01:47:00 UTC | #14

Great progress mate.
I notice, the grid line doesn't display correctly on the last picture. 
Is that due to z-fight. Are you going to fix that?

-------------------------

Sinoid | 2017-05-31 07:26:19 UTC | #15

[quote="George1, post:14, topic:3119"]
I notice, the grid line doesn't display correctly on the last picture. 
Is that due to z-fight. Are you going to fix that?
[/quote]

Yeah, depth-test failing where it intersects the other grid-lines. Never noticed it amongst all of the other aliasing until you mentioned it, cake to fix.

---

I'll be carrying through for the week, but I expect to drop this completely soon. QT is absolutely pathetic compared to MFC in many ways. QT is designed for single document type scenarios and completely falls on its face when presented with multiple document types.

Essentially, I have to write MFC on-top of QT to make anything sane and not tightly coupled as QT is the epitome of tight coupling with signal/slot. It cannot cope with ephemeral existences, it does not work well with undo/redo (nothing in QT does), etc.

Whereas in MFC, no one actually uses it like you think they do. All shipping cases are closer to DearIMGUI. We just use CWnd and the other helpers, and do everything else ourselves ... that's how it has always been.

I'm going to give replicating CCmdUI in QT a whirl, if it works great, but if it doesn't this project is dead.

-------------------------

Eugene | 2017-05-31 08:42:10 UTC | #16

May you explain what are your plans?
What are you going (trying) to implement?
What features do you miss in Qt?

-------------------------

TheSHEEEP | 2017-05-31 09:24:27 UTC | #17

[quote="Sinoid, post:15, topic:3119, full:true"]
QT is designed for single document type scenarios and completely falls on its face when presented with multiple document types.[/quote]
That one I just don't get.
Qt absolutely features scenarios with different kinds of documents. What are you even trying to do?

[quote="Sinoid, post:15, topic:3119, full:true"]Essentially, I have to write MFC on-top of QT to make anything sane and not tightly coupled as QT is the epitome of tight coupling with signal/slot. It cannot cope with ephemeral existences, it does not work well with undo/redo (nothing in QT does), etc.

Whereas in MFC, no one actually uses it like you think they do. All shipping cases are closer to DearIMGUI. We just use CWnd and the other helpers, and do everything else ourselves ... that's how it has always been.

I'm going to give replicating CCmdUI in QT a whirl, if it works great, but if it doesn't this project is dead.
[/quote]
Quite honestly, all of this just sounds like you don't know how to use Qt.

If you want undo/redo in any kind of editor that goes beyond simple text, you will have to implement it yourself.
Which you can do with Qt as well as with every other library. Hell, to my surprise, Qt actually offers undo/redo functionality out of the box: http://doc.qt.io/qt-5/qundo.html
And those actions can be completely customized so they do not limit you in any way.
Claiming that signal/slot cannot deal with any instance existing just a brief amount of time is also wrong, since a QObject destructor automatically disconnects it from whatever it was listening to according to docs. And even if that wasn't so, you can always disconnect() manually.

You are right that Qt is not MFC, but that should have been clear from looking at a few examples.
The only thing really bothersome about Qt I found to be that getting multithreading and signals/slots working together requires some extra effort, because for some weird reason, QObjects belong to a thread and depending on what you want to do, they will complain about being touched from a "wrong" thread.
Also, the Qt Designer is just... not very good.

-------------------------

Pencheff | 2017-05-31 09:34:07 UTC | #18

Multithreading is not so hard either, its safe to emit a signal from any thread and the QObject will receive it in its own.

-------------------------

TheSHEEEP | 2017-05-31 09:56:59 UTC | #19

[quote="Pencheff, post:18, topic:3119, full:true"]
Multithreading is not so hard either, its safe to emit a signal from any thread and the QObject will receive it in its own.
[/quote]
By default, yes. But sometimes that is not what you need.

-------------------------

johnnycable | 2017-05-31 10:50:00 UTC | #20

I guess you're using QT to bridge over the native OS, a thing urho as a library-type sw cannot do. So you're probably using it for:
- drag'n'drop ? (isn't that in sdl?)
- some advanced document mgmt (like NSDocument on os X?). Indeed, there's no such thing as an "urho document type" if I'm not mistaken...
- advanced widgets... this is probably the biggest one missing... 
is that?

-------------------------

Sinoid | 2017-06-03 06:16:24 UTC | #21

[quote="Eugene, post:16, topic:3119, full:true"]
May you explain what are your plans?
What are you going (trying) to implement?
[/quote]

Sure can.

So, right now I've hacked around the command woes with a non-intuitive zero-interval repeating timer to trigger the commands to update (RegisteredAction class, derived from QAction) - it's as close to a cross-platform WM_IDLE I could find. Most commands will be able to fit in with the added types that limit a command's availability to a document type, type of selected datasource, state of a setting, etc. That's really just an expansion of the existing DocumentRegisteredAction which up until now was only used for filtering in the "Quick Action" (CTRL+SPACEBAR) menu.

The localization stuff is going away for QT's localization as #1) it doesn't fit the switch-over to mostly IMGUI at all, #2) it didn't actually work in tests ... notifying every single LocalizedLabel that I switched to Esperanto reliably crashes QT during the resulting layout updates. It could probably work, but it's not worth it. Safer to just stick with QT's restart based localization, at the time I started it I didn't know that you can't change IME while QT is running - had I known that I wouldn't have gone that road.

I've been investigating ImGizmo in a "base-code" fashion to simplify gizmo handling but ditching it's IMGUI ties for different painting and input handling. I want to get to that sooner rather than later.

I need to investigate better handling of IMGUI popups. I suspect everything I need is there in the IMGUI context, but I haven't checked it out yet. Worst case it's just slapping an extra pointer on the ImWindow since I know all of the windows/sub-windows are there, so the problem is just knowing who belongs to who.

Priority is finishing the main Urho3D scene document and particle effect document. The particle-effect document has more "interesting" things to it than materials do so that's a best case minimal document.

Lastly I'd like to expand more on top-level documentation explaining what is going on and why it is going on. In general I believe the code to be commented fairly well, with funky-stuff being noted and everything else as "should be obvious." But the structural decisions and where things are, what they are, and why they are still isn't clear. This is definitely getting better as the switch to IMGUI based widgets has resulted in removing many files, reducing both cognitive and exposure load.

These are the things I feel comfortable promising that I will do, even if I abandon ship, though I'm taking time to make sure that abandoning ship is the right choice for my other projects .... CMake + modern-MFC doesn't work (probably a cannot) at all so there's that.

> What features do you miss in Qt?

More than anything I miss sane message dispatch. To arrive at something sane you have to attach each parent as an event filter to every single child ... that's just nasty.

The dock widget is also complete garbage. That may be my biggest issue with QT overall (aside from MOC basically breaking every 30 minutes). Their dock widgets aren't even worthy of being called garbage. I'm looking at porting over some dock-widgets I wrote before MFC had official dock-widgets to it to ditch the non-sense.

Seems trite, but that widget has to form one of the main back-bones of a program. It cannot be as useless as QT's version, it just can't.

IME that isn't fixed at startup would be nice ... also known as "requried" since the first publication of IBM's CUA.

---

[quote="TheSHEEEP, post:17, topic:3119"]
That one I just don't get.
Qt absolutely features scenarios with different kinds of documents. What are you even trying to do?[/quote]

As close to zero tight coupling as possible (signals/slots are tight coupling) and optimal reuse of all commands across documents ... again without unnecessary coupling for the enabled/disabled/checked/unchecked/etc states.

I can only tolerate explicit coupling for so long.

[quote="TheSHEEEP, post:17, topic:3119"]
Quite honestly, all of this just sounds like you don't know how to use Qt. ... You are right that Qt is not MFC, but that should have been clear from looking at a few examples.
[/quote]

I had a pretty solid idea walking into it what to expect and put a fair bit of time in screwing about with it first, but I greatly misjudged it. I had expected much closer to the usual WinForms/wxWidgets/WPF hack woes in practice.

If I had to slap a "biggest fault" on my considerations, it'd be that I never gave the "polish" stage a look, and that is the stage right now where everything is just plain awful beyond anything I have ever worked with before. Super duper awesome when slapping some things together, absolutely horrible when polishing it into behaving sanely.

> Also, the Qt Designer is just... not very good.

Yeah, I don't use that ... because it's just as horrible as those nasty MFC, WinForms, wxWidgets, and WPF editors. They're all awful, that's not exclusive to QT, though QT designer is a cut above the most for awfulness (wxWidgets is so much worse).

-------------------------

Sinoid | 2017-06-03 06:31:47 UTC | #22

[quote="Pencheff, post:18, topic:3119, full:true"]
Multithreading is not so hard either, its safe to emit a signal from any thread and the QObject will receive it in its own.
[/quote]

Provided you aren't in the middle of a paint or relying on the status of any opaque QT object. There's threading behind the scenes that will invalidate the hidden "d_ptr" and lead to awesome "invalid access 0x0000000000000018" errors and the like if you touch signals that in some way come back around to your QObject.

Was the whole reason for "PushDeferredCall" in the IMGUI stuff, so that those calls would go out through lambdas after paint was done so that their consequences wouldn't nuke the d_ptr of the QPainter. There are plenty of other similar cases, if a signal somehow comes back to your class all bets are off regardless of your connection settings.

Edit: 0x0000000000000018 would be a call to QPainter::setClipRect on a QPainter whose d_ptr has been destroyed. Also the same generic error for setting text on a QLineEdit while it's resizing.

-------------------------

urho3d | 2017-06-03 11:00:48 UTC | #23

8 posts were split to a new topic: [JS - My QT Editor removed posts](/t/js-my-qt-editor-removed-posts/3198)

-------------------------

Bluemoon | 2017-06-03 08:53:10 UTC | #28

It's awesome to know that we all want Urho3D to develop better, but it seems we've mistakenly pulled out our arsenals of war when there is actually no battle cry... Why don't we all pull back our arsenals and look for a common way the Urho3D community can move forward :grin:

-------------------------

urho3d | 2017-06-03 10:58:57 UTC | #32



-------------------------

urho3d | 2017-06-03 11:07:50 UTC | #33

Since the author has withdrawn from this project and the topic became derailed, it has been closed. Please remain respectful towards all members of the community, as listed in the General Forum Rules. 

https://discourse.urho3d.io/t/urho3d-forum-rules/8

-------------------------

