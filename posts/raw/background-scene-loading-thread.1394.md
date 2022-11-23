gabdab | 2017-01-02 01:07:27 UTC | #1

I'd like to show a little animation while loading different levels ( scene transitions ).
Is there a  -threads on Urho3D- example available (performing on mobiles too )?

-------------------------

cadaver | 2017-01-02 01:07:27 UTC | #2

True scene loading on a background thread isn't possible, or recommended.

However you can do async scene loading which loads only a small bit each frame, so that you can run animations in the meanwhile, and keep checking the scene load's progress.

See Scene::LoadAsync() or Scene::LoadAsyncXML() and Scene::GetAsyncProgress(). An event will also be sent upon load completion, see E_ASYNCLOADFINISHED in SceneEvents.h.

-------------------------

gabdab | 2017-01-02 01:07:27 UTC | #3

Cool , thanks .
I just found a similar post , sorry about double posting :
[topic1157.html#p6772](http://discourse.urho3d.io/t/async-loading-help/1120/2)
P.S : Is 'thread unsafety' the norm on 3d engines  ?

-------------------------

cadaver | 2017-01-02 01:07:27 UTC | #4

It depends on the operation being done. Operating on isolated data (like some calculation) is no problem to thread. Scene loading however may invoke graphics resource loading (meshes, textures) and graphics API's are often by default thread-unsafe. Urho contains a mechanism to handle this (resources can be pushed into a background load queue, and will be finalized in the main thread once ready) but it is not prepared for arbitrary scene modifications happening from any thread, so these need to be well-defined, and the easiest rule is that only the main thread should modify the scene. To do otherwise would make the engine prohibitively ineffective, as each operation would need to happen inside a mutex lock, or alternatively scene access would happen only by message passing, which is an approach used by some engines.

-------------------------

gabdab | 2017-01-02 01:07:27 UTC | #5

[gamasutra.com/view/feature/1 ... hp?print=1](http://www.gamasutra.com/view/feature/130247/multithreaded_game_engine_.php?print=1)

-------------------------

codingmonkey | 2017-01-02 01:07:27 UTC | #6

>I'd like to show a little animation while loading different levels ( scene transitions ).
You may use two scenes: 
First for keeping transition animation only.
And second scene will always keep actual world game part (level, room) you may load it async or in sync modes.
also probably you will be needed: fade-in and fade-out frames blending post-effect between two frames (Shaders, postProcess.xml).
And on some game trigger: at first you starts doing blending fade-in(from game frame to animation scene frame) and on moment when blending will be finished (visible are only animation scene frame) just pop viewport of game scene from renderer. 
after this renderer will be have only one Viewport from animation scene.
On this moment you may start load you new level and when it loads you need to do the same things but reverted, use fade-out from animation scene into new game scene frame, on blending finished pop VP of animation scene from renderer.

-------------------------

rasteron | 2017-01-02 01:07:28 UTC | #7

I would also like to see a basic example of LoadAsync for assets here as this is really a critical method for some. It is really awkward when you load a medium to big scene and then the mouse cursor gets busy (as if it is going to crash or some errors will start to show) or simply displaying progress when loading the scene.

-------------------------

friesencr | 2017-01-02 01:07:28 UTC | #8

I had done an experiment with background loading files and gotten less throughput using multiple threads.  File reading isn't more efficient using threads under lots of conditions.  I was rather astounded.  Moar cores = moar perf right?  Also remember that urho's renderer divides its work on the number of physical cores in the render phase.  Until we patch it to use the available threads or single threads you could get a hitch.  I am having a really hard time getting maximal amounts of loading in those 4-5ms per frame.

To load in the background ask the resource cache to BackgroundLoadResource.  If you need it now you can GetResource on the cache and it will check to see if it is loading in the background and wait on the Mutex.  Any work that is done loading will be completed on the begining of the frame.

UPDATE:  I didn't notice that the background loader has it's own Thread so it does not affect the renderer to the same extent.

-------------------------

cadaver | 2017-01-02 01:07:28 UTC | #9

The problem with an async load example is that we don't have realistic content in the repo to showcase meaningful loading progress. We can add async load and progress bar e.g. to SceneAndUILoad example, but it will just flash by in a few frames. However that still shows how it can be used with any scene.

-------------------------

gabdab | 2017-01-02 01:07:28 UTC | #10

Substituting
CODE: SELECT ALL
scene_->LoadAsyncXML(cache->GetFile("Data/Scenes/CharacterDemo.xml"));

to
CODE: SELECT ALL
scene_->LoadXML(loadFile);

segfaults for me on 18_CharacterDemo .
Should you destroy all nodes before invoking it ?

-------------------------

cadaver | 2017-01-02 01:07:28 UTC | #11

There is a logic problem in 18_CharacterDemo that it expects to re-find the character node immediately after invoking the scene load, and when it doesn't, it accesses a null pointer. In case of LoadAsyncXML() this should be done only once the scene has fully loaded, which may take some frames. LoadAsyncXML() will clear the scene properly so you don't have to do it manually.

-------------------------

gabdab | 2017-01-02 01:07:28 UTC | #12

Ok , accomplished, thanks.
I noticed that AssetImporter (Assimp) doesn't convert xml scenes to binaries ..
Can you just basically convert xml to bin in c++ line by line ?

-------------------------

cadaver | 2017-01-02 01:07:28 UTC | #13

You can load the scene in editor and resave as binary, or use -b switch in AssetImporter (There is a textfield in Editor Settings dialog where you can input additional AssetImporter command line switches.)

Note that binary incompatibilities are deadly for your scene if the attributes change, so I suggest to also keep XML files around for more resilient loading, or have a solid process for re-importing all your scene content.

-------------------------

gabdab | 2017-01-02 01:07:29 UTC | #14

Nodes are imported correctly (apparently) but static models inside them are missing (resource path is set to Data folder ) .
A portion of the handmade-sort-of  xml scene :
[code]
<node id="16777217">
<attribute name="Is Enabled" value="true" />
<attribute name="Name" value="Cube_062" />
<attribute name="Position" value="1059.38 81.82 -1227.51 " />
<attribute name="Rotation" value="1.00 -0.00 0.00 -0.00" />
<attribute name="Scale" value="1.00 1.00 1.00" />
<attribute name="Variables" />
<component type="StaticModel" id="16777219" >
<attribute name="Model" value="Model;Models/2015_9_29_9_7/Cube.058.mdl" />
<attribute name="Material" value="Material;Materials/2015_9_29_9_7/stonewall4.xml" />
</component>
</node>
[/code]

-------------------------

