artax64 | 2017-01-02 01:00:59 UTC | #1

Hi all, I've just discovered this great engine/environment, but I'm a little confused about one key step. Most editors have a "play" or "test" function to actually run an xml scene. So for example, if I were to set up a simple scene how would I go about actually testing it? I may have missed this somewhere in the documentation and I can't seem to find any hits on google. Any info would be a huge help.

Thanks

-------------------------

cadaver | 2017-01-02 01:00:59 UTC | #2

Urho isn't a completely scene-based system like Unity. Meaning, that there usually is application logic outside the scene(s), which can be either C++ or script. Typically, an application (for example the NinjaSnowWar example game) would load a scene and then proceed to run logic, spawn objects etc., or make transitions such as loading a "title screen" scene first, then the actual game scene.

When running the editor (which is btw. just another script application), you have the ability to enable scene update by pressing the "play button" or Ctrl-P, but this just activates physics, and any scripts in the scene that have update handlers. You can't for example start the full NinjaSnowWar game from within the editor.

-------------------------

rogerdv | 2017-01-02 01:00:59 UTC | #3

Sorry for hijacking the thread, but is there any plan to integrate more the editor inside the engine (again, like Unity)? I really miss the feature of checking how the game works from inside editor.

-------------------------

cadaver | 2017-01-02 01:01:00 UTC | #4

One of the problems is that we don't know what your application is, is it C++ classes that use the engine bundled into a custom executable, an AngelScript script, Lua script etc., or a mixture of them? Making a complete "click play to test the game" solution necessarily dictates to the user how Urho must be used, and I suspect this would actually make Urho unattractive to some users. In this respect, it's more comparable to a library such as Ogre.

I'm fairly sure that Urho could be used (as a library and as the core runtime) to create an editing environment like Unity, that *would* dictate how it needs to be used, and as a reward it would offer similar testing workflow. Due to the reason above and also lack of manpower I don't think it realistically can be the Urho core project's responsiblity. We certainly don't prevent anyone from embarking on such project (after all the engine has a MIT license) and instead would gladly link to it, like we link to other external projects like the Blender-exporter.

-------------------------

thebluefish | 2017-01-02 01:01:00 UTC | #5

This actually sounds like it would be a good idea, especially to get more interest in Urho3D. There's definitely going to be the people who want to use their own workflow, but there's also the people who want something easy-to-use to get eased in to creating a game with this engine.

There's already tools out there to edit practically every resource we need, though some things could definitely benefit from a better editor. We already have the Urho3D Player as a base to actually "launch" the game. An editor could simply be a second program designed to maintain the project files, provide direct editors for each resource (script, scene, materials, etc...), package the files, then invoke the Urho3D player (or a custom wrapper) to actually run the game. It would make for quick and easy prototyping, and by making it open-source it would allow people to customize it for their own preferred workflow.

-------------------------

friesencr | 2017-01-02 01:01:00 UTC | #6

I had thought about adding a 'addon' system to the editor but there are issues with the current code base and inter module communication.  The refactor could be as simple as moving everything into a namespace.  Then addons could communicate via interface.  An addon could easily provide a lightweight opinionated approach.  I have always liked that Urho3d didn't take a stance on lots of my code.  It felt like when I am writing code in Unity it is to make my game work in the editor and not the code first approach that I appreciate.

-------------------------

cadaver | 2017-01-02 01:01:00 UTC | #7

There's a somewhat serious problem related to the "singleton" nature of the engine subsystems: you would have the game and the editor "competing" over things like Renderer, UI etc. To solve that needs more than the editor script code reorganization. One way would be to have only the game actually interface with Urho and the editor would be a native application around it (Qt, WxWidgets etc.). In that approach the editor would need to be rewritten as a C++ application. Another crude solution would be to do a "hard reset" when appropriate, for example do complete teardown of editor UI on game start, then do complete rebuild of it once the game stops.

-------------------------

artax64 | 2017-01-02 01:01:03 UTC | #8

Thanks for the reply, and it confirms how I thought the system worked. It does greatly allow for full-game developers to make something flexible and tangible, but for newbies it makes it slightly difficult to get the ball rolling. However, a good tutorial/documentation walkthrough of a very basic game would be hugely advantageous in helping users adopt Urho.

-------------------------

hdunderscore | 2017-01-02 01:01:03 UTC | #9

The simplest solution would just be to have a 'run external' option in editor, where you can supply a external application + command line arguments.
Eg: Urho3DPlayer Data/Scripts/MyGame.as -w

In the IRC, I walked someone through using the CharacterDemo script to load a scene they were working on in the editor. It's a pretty simple solution that could be polished off, and avoid the complexity of having a deeply integrated solution within the editor.

-------------------------

