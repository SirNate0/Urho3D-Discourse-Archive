Lichi | 2017-01-02 01:10:59 UTC | #1

Hi, i'm trying to implement this terrain editor [topic783.html](http://discourse.urho3d.io/t/terrain-editor/765/1) to Urho editor, but the terrain editor is written in lua and Urho editor is written in angelscript. There any way to call a lua function fron angelscript?
Thanks.

-------------------------

Shylon | 2017-01-02 01:10:59 UTC | #2

I think the problem is whole Editor is written in AngelScript, while I think [[b]My suggestion[/b]] should be write with C++ completely, I saw Polycode (MIT licence engine ) editor has very nice IDE and has lua editor, Urho3d would be nice to have something like this, current viewport and window of attributes are not nice.

-------------------------

1vanK | 2017-01-02 01:10:59 UTC | #3

U can use component LuaScriptInstance for it

-------------------------

weitjong | 2017-01-02 01:10:59 UTC | #4

Unless JTippetts has used advanced Lua specific constructs like closure or table then it should be possible to convert the Lua script calling the Urho3D Lua API into AngelScript script calling the Urho3D AngelScript API. Or have you tried to do a hybrid? i.e. let the Urho3DPlayer "plays" both the existing AngelScript scripts for Editor functionality and the new Lua scripts for the new functionality. I have actually never tried that but it would be an interesting experiment.

-------------------------

cadaver | 2017-01-02 01:10:59 UTC | #5

I believe you would need to do adaptation of the Lua code in any case so that it wouldn't clash with the AngelScript editor (scene, viewports, UI and such), at which point it shouldn't be that much more work to convert to AngelScript.

A professionally made C++ editor could indeed use Urho just as a "slave" to display the 3D viewport, while its UI would be its own (native probably) and therefore wouldn't clash with the running application or game being edited. We are talking easily of a man-year or more of effort, though.

-------------------------

Shylon | 2017-01-02 01:10:59 UTC | #6

[quote="cadaver"]
A professionally made C++ editor could indeed use Urho just as a "slave" to display the 3D viewport, while its UI would be its own (native probably) and therefore wouldn't clash with the running application or game being edited. We are talking easily of a man-year or more of effort, though.[/quote]

I see the Angel script code for Editor is similar to urho3d, is possible to copy paste AS code to c++ (with some edits) and use it for editor? probably this is the fastest way. 
so difference is all editor code of angle script converted to c++.

-------------------------

cadaver | 2017-01-02 01:10:59 UTC | #7

If it was a direct conversion, and the UI code would be the same (uses Urho UI) it would have the exact same problem of the application and editor UI clashing. In that sense I don't see the benefit of converting the editor to C++ just for the sake of it, unless the editor UI is rewritten to native.

-------------------------

hdunderscore | 2017-01-02 01:11:00 UTC | #8

There was a previous effort to convert the Urho3D Scene Editor to C++: [github.com/scorvi/Urho3DIDE](https://github.com/scorvi/Urho3DIDE)

Since it's an external project, it might not be hard to update it with any changes that were made to the AS editor since then.

One useful possibility of having the c++ editor is building with emscripten, and then potentially integrating the editor with atom.io editor. I'm not sure what would be involved in getting the filesystem working again though.

-------------------------

cadaver | 2017-01-02 01:11:00 UTC | #9

That's a good point. Though not sure if I'd want to risk any substantial creative work under the emscripten runtime :slight_smile: or if the performance would be acceptable for editing complex scenes.

-------------------------

Shylon | 2017-01-02 01:11:00 UTC | #10

[quote="hd_"]There was a previous effort to convert the Urho3D Scene Editor to C++: [github.com/scorvi/Urho3DIDE](https://github.com/scorvi/Urho3DIDE)[/quote]

Interesting, what about using other GUI toolkits and using it for Urho3d Editor like wxWidgets or QT? then I assume should not be any problem of Clashing?

[url]https://en.wikipedia.org/wiki/List_of_widget_toolkits[/url]

-------------------------

thebluefish | 2017-01-02 01:11:04 UTC | #11

[quote="Shylon"][quote="hd_"]There was a previous effort to convert the Urho3D Scene Editor to C++: [github.com/scorvi/Urho3DIDE](https://github.com/scorvi/Urho3DIDE)[/quote]

Interesting, what about using other GUI toolkits and using it for Urho3d Editor like wxWidgets or QT? then I assume should not be any problem of Clashing?

[url]https://en.wikipedia.org/wiki/List_of_widget_toolkits[/url][/quote]

[github.com/thebluefish/JRPGEngi ... Urho3D.cpp](https://github.com/thebluefish/JRPGEngine/blob/master/JRPGEngine/BluEdit/src/wxUI/wxUrho3D.cpp)

I've successfully integrated it into wxWidgets. With some relatively simple modifications, we can also get multi-window support with OpenGL, as DX already supports multiple windows. The current downside is that each wxUrho3D widget runs its own Urho3D Context, which can get expensive memory-wise and it's not easy to pass things between the various contexts. However, while that code has been abandoned a while ago, I do have better wxWidgets integration in a private repo that's going towards my new editor revision. Who knows if it will ever see the light of day  :laughing: However I'm not claiming any license over my current public code so feel free to do with it as you see fit.

-------------------------

Shylon | 2017-01-02 01:11:04 UTC | #12

it would be really nice to have a new editor for Urho3d, the only problem is events and context, but for base gui most widget like wxWidget have Editor (can be found) and can save to a file and loading in, anyway I saw [b]cegui[/b] (mit license crossplatform )
[url]http://cegui.org.uk/[/url]

that has Ogre, OpenGL, Irrilich and ..., ready context, you may look at the documentation,

[url]http://static.cegui.org.uk/docs/0.8.5/rendering_tutorial.html[/url]

-------------------------

cadaver | 2017-01-02 01:11:04 UTC | #13

CEGUI is more to the bloated and over-engineered side of GUI libraries that use the 3D graphics context to render (compare to e.g. TurboBadger which is newer, more lightweight and to-the-point) while it doesn't help with the native UI widgets.

-------------------------

Shylon | 2017-01-02 01:11:04 UTC | #14

[quote="cadaver"]CEGUI is more to the bloated and over-engineered side of GUI libraries that use the 3D graphics context to render (compare to e.g. TurboBadger which is newer, more lightweight and to-the-point) while it doesn't help with the native UI widgets.[/quote]
Yeh, TurboBadger is good, also it seems used in Atomic engine, good to know. :slight_smile:

-------------------------

thebluefish | 2017-01-02 01:11:05 UTC | #15

I used to use CEGUI with Ogre3D a few years back, and my impression of it was less than stellar. I ended up using MyGUI as an alternative since CEGUI was a lot of bloat to accomplish what I was looking for. However it has been a few years and there appears to be some updates since, so maybe it's worth taking a shot  :slight_smile: 

The biggest problem IMO is that these GUI toolkits rest upon rendering, which means it's not possible to mix a toolkit control and a native control. With multi-window rendering this is less of an issue since the toolkit controls can be created as different windows. For example, [url=https://github.com/thennequin/ImWindow]ImWindow[/url]:

[img]https://github.com/thennequin/ImWindow/raw/master/Screenshots/Docking.gif[/img]

Which works with DX11 only. OpenGL is still forced to a single window because of the aforementioned OpenGL context issues.

Once we break that barrier, or find out that you don't need it for a particular project, the underlying GUI toolkit is more of a personal opinion. For example, [url=https://github.com/nem0/LumixEngine]what you can accomplish with something like imgui[/url] might work better for your particular use-case over another library. 

CEGUI *did* power Torchlight, so it's got proof that it can work well for larger games. If it's easy to integrate, it might be a good alternative to the current system.

-------------------------

Shylon | 2017-01-02 01:11:05 UTC | #16

I should say that for my personal game project, what is most important is actual engine, for Game Editor even Blender can be used, so I think Urho3d new editor should be at very list priority (adding feature to current editor is good), focus should be on more demand features, for example in my game i want to reach a very nice cartoonish visual, and Ambient Occlusion is very important for me, so these days I am digging in Urho3d and trying to implement it, so for terrain I think there are some free terrain editor out there and Urho3D developers should focus on other features like Radiosity global illumination ([url]http://codeflow.org/entries/2012/aug/25/webgl-deferred-irradiance-volumes/[/url]) or better soft shadows fo lights (as this one also one of my priority to see how can I reach, cartoons have softer shadows).

-------------------------

cadaver | 2017-01-02 01:11:05 UTC | #17

The ImWindow multi-window system seems to be so far implemented for D3D11. That is fairly straightforward, as you can create a swap chain per window. For working with OpenGL and multi-window I'd assume you would have to detach and attach the context to different windows as your rendering proceeds. I haven't tried that so I've no idea how that works across platforms. Multiple GL contexts or resource sharing between them seems like a can of worms.

-------------------------

thebluefish | 2017-01-02 01:11:05 UTC | #18

[quote="cadaver"] Multiple GL contexts or resource sharing between them seems like a can of worms.[/quote]

The changes that I submitted via a PR and accepted are sufficient to support this use-case. My code's currently messy, but it sounds like there's more interest in this. I'll see about getting something out in the next couple weeks once my job transition smooths over a bit.

Edit: I should note that those changes are good for multiple Urho3D contexts, which in turn support multiple OpenGL contexts. Some additional changes are required to support multiple OpenGL contexts within a single Urho3D context, although it is not that complex.

-------------------------

thebluefish | 2017-01-02 01:11:05 UTC | #19

[quote="cadaver"] In that sense I don't see the benefit of converting the editor to C++ just for the sake of it, unless the editor UI is rewritten to native.[/quote]

My current approach is to write the editor framework in C++, and then define all the functionality in AS/Lua. Currently this means that all of the editor tools are currently loaded as [res://Addons/*.lua](res://Addons/*.lua), with script hooks for loading/unloading the addon and its various parts. Then each addon could use editor-specific events such as "EditorCreateMenu" and "EditorCreateConfigPanel", though I'm still playing around with the structure.

Perhaps something similar could be done in LUA or AS to allow functionality with the other language?

-------------------------

cadaver | 2017-01-02 01:11:06 UTC | #20

Interesting. This hybrid approach can have the downside, similar to the UI, that if you want the full Unity-style start/stop testing of the application, the editor scripts still live within Urho and could be destroyed (unloaded) or be disturbed by the application being tested, whereas in C++ you have stronger guarantee of the separation between editor and the Urho runtime.

-------------------------

Lichi | 2017-01-02 01:11:11 UTC | #21

[quote="weitjong"]Unless JTippetts has used advanced Lua specific constructs like closure or table then it should be possible to convert the Lua script calling the Urho3D Lua API into AngelScript script calling the Urho3D AngelScript API. Or have you tried to do a hybrid? i.e. let the Urho3DPlayer "plays" both the existing AngelScript scripts for Editor functionality and the new Lua scripts for the new functionality. I have actually never tried that but it would be an interesting experiment.[/quote]
Yes, this is what i'm trying, i'm going to register "CallLuaFunction" in the angelscript engine and CallASFunction in the lua engine, then hide the respectives UI (urho editor/terrain editor) to switch edit modes  :smiley:

-------------------------

weitjong | 2017-01-02 01:11:11 UTC | #22

That's not exactly what I have in mind, but don't let me stop you in your experiment.

-------------------------

