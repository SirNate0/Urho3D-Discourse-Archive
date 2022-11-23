weitjong | 2017-01-02 00:58:02 UTC | #1

In order to fix the 'git describe' command which previously not able to generate any meaningful information, I have converted the last lightweight tag into annotated tag (at the point of its creation time). As part of the last commit, I have to force push the updated tags into remote repository. If you don't re-fetch the tags (git fetch --tags)  then your tag 1.3 would still remain as lightweight tag. In either case, however, 'git describe --always --tags' should give something like this: 1.3-888-gd3382cb. Note the '1.3' was not there before.

Anyway, the subject of this topic is, it is time for a new release? We have 888 commits after the last tag. In Chinese believe, that's an auspicious number to do anything. :smiley:

-------------------------

cadaver | 2017-01-02 00:58:02 UTC | #2

There's certainly been a lot of work since last release, so a new release would be a good idea.

I've got two minor issues listed (transparent object instancing, and Drawable::IsInView() behavior with shadows) which may or may not be easy to resolve. I'd like to take a look at them during the weekend, but either way (solved or not, they're not critical) the release could be prepared eg. in beginning of next week.

There's also Aster's 2D work in the new2d branch. Aster, can you estimate how long that will take to finalize? I don't think we want to delay the next release too long, but rather once the 2D work is done and tested well, we could make yet another release sooner, instead of waiting another half year :slight_smile:

-------------------------

friesencr | 2017-01-02 00:58:03 UTC | #3

sdl 2.03 or 2.02 whatever they are calling it is coming up real soon.  this version of sdl includes 'dynamic api' which is a hack to dynamiclly load a sdl dll for staticly linked versions.  i think this is directly aimed at steam linux releases with their stuggles with their compositor.  they want to be able to fix all the old games when they fix their compositor.  i think this would be a nice thing to get in a release.

-------------------------

aster2013 | 2017-01-02 00:58:03 UTC | #4

Current 2D work just add 2D sprite and 2D particle system. The work for 2D Physics was not start. I think that it is better to release without 2D work.

-------------------------

cadaver | 2017-01-02 00:58:03 UTC | #5

friesencr: do you know if SDL2.02 (or whatever) will fix actual Urho issues you or someone else is having? Of course it will be nice to merge in time, but I don't see us benefiting from dynamic SDL dll loading, considering that we need the hacks/changes we've made.

Usually they thoroughly break Android on each release, or at least the way Urho is using it :wink:

-------------------------

friesencr | 2017-01-02 00:58:03 UTC | #6

cadaver: I am having some issues with my knockoff xbox 360 controller that may be fixed with their latest gamepad fixes.  Steam is starting to crowd source gamepad configurations with big picture mode so they are being  much more aggressive with gamepad xinput remanglings.  I havn't really looked into why its not working; its not a priority for me to have a gamepad working when i don't have much a game.  

My excitement for linux growing as a platform tends to consume a fair bit of my mind.  I have been testing steamos quite a bit.  I am part of their in home streaming beta and let me tell you ... with a mouse it's bad.  I am seeing lots of chatter about relative motion on the mouse being broken.  Much of getting it to work relies on them integrating sdl into the compositor.  I think my thought that it adding it would help make the release more future proof skewed my thinking.  Their new gamepad profile server and dynamic api would be better to toy around with for a while anyways.  I am thinking that steamos / mesa 10.2 / wayland / gnome thing will hit April/May.  I was expecting another long release subconsciously... see I can't think straight!  I have figured out that I have memory leaks up the wazoo.  All of the reference counting inception is blowing my brain.  But I can step through the code; how I love oss.  Hopefully in a few months this will have been a bad dream.  Going to need pizza.

I have 60% of keybinding support for the editor done.  Its probably 4-6 hours.  So 2-4 bad action sci fi movies.  It's hard to get a sense if people want it.  I love that the keyboard shortcuts show up in the tooltips.  My inner ux smiles.

I'll stop rambling.  This release is going to be awesome.  It's by far the most metal version of Urho to date \m/

-------------------------

cadaver | 2017-01-02 00:58:03 UTC | #7

I'm sure SDL new version will incorporate a lot of fixes for things I don't even understand :slight_smile: like various Linux compatibility issues. They are also probably quite close to releasing 2.0.2 at this point. However we use SDL in Urho in a quite precarious way as the modifications always need to be reapplied on top, therefore switching to the new version now would require quite a bit of testing. Of course we can start 2.0.2 integration in a branch at any point.

In general we would need a good workflow for tracking the SDL upstream branch; it's too bad they use Mercurial.

-------------------------

friesencr | 2017-01-02 00:58:04 UTC | #8

[github.com/spurious/SDL-mirror](https://github.com/spurious/SDL-mirror)

It is not official.  If it becomes un maintained I am more then happy to put my raspberry pi back to work.

-------------------------

GIMB4L | 2017-01-02 00:58:04 UTC | #9

I saw a few Bullet warnings about deprecated functionality, so if we were to release a new version those should be cleaned up too. Also, there are a few bugs in the Editor I'd like to fix. First, when scrolling out there is an issue with the far plane of the camera. Second, I don't think we should compile script files in the editor when you select them, because user-defined types not exposed in Urho3D are treated as errors.

EDIT: 

Upon further investigation, the scrolling effect is actually a zoom. Didn't know that feature changed :stuck_out_tongue:. In a version I'm going to file a pull request for, I've switched the scroll so that scrolling down zooms out and scrolling up zooms in. I think users are more familiar with this type of behaviour. 

Also, I added a 'CompileScripts' option in the editor. If it's turned off, any script files the user wants to attach to a node won't be compiled before their added to the node. This helps if the user has exposed their own code to the scripting API.

-------------------------

cadaver | 2017-01-02 00:58:04 UTC | #10

How do you get the Bullet deprecation warnings? In debug mode?

If you add major new functionality to the scripting API, or new C++ components, you should run the editor in a customized Urho3DPlayer that includes those mods. Urho3DPlayer's functionality is actually very simple: load script, run engine loop until exited.

-------------------------

GIMB4L | 2017-01-02 00:58:04 UTC | #11

Yeah, I'm in debug mode. Here's a sample of what I'm getting:

[code][Fri Feb 21 23:28:20 2014] WARNING: The GetNode API binding is deprecated, GetPtr() should be used instead.
[Fri Feb 21 23:28:20 2014] WARNING: The GetNode API binding is deprecated, GetPtr() should be used instead.[/code]

And IMHO to make specific modifications to the engine would be harder than in a C++ project -- reason being, the compile time would be a lot longer. Either way it's a toggle, it's at the user's discretion if they want to lose the compiled functionality in the editor.

-------------------------

weitjong | 2017-01-02 00:58:04 UTC | #12

Those deprecated warnings come from Urho3D AngelScript API and not from Bullet library. You should change your script to use Variant::GetPtr(). All the other forms, such as GetNode(), GetRigidBody(), etc, are now deprecated. Those are also marked as deprecated in the Scripting API documentation.

-------------------------

cadaver | 2017-01-02 00:58:04 UTC | #13

For the scripts to not load I believe it has to be implemented on the ScriptInstance level. I'm not opposed to that feature as a toggle.

But, you don't have to modify the engine to include your C++ customizations. Rather you can make your own application have a mode that runs the editor. As long as you're instantiating the AngelScript subsystem you have everything you need to run it. Urho3DPlayer is strictly not part of the engine either.

The main problem with failing resouce loads (like scripts) is that the corresponding slot gets cleared from the object that is being edited, and if you re-save the resource assignment will be lost. It's worth checking if that behaviour could be changed in general. The easiest way would be to allow ResourceCache to return failed resources, but it may have unwanted side-effects.

-------------------------

cadaver | 2017-01-02 00:58:04 UTC | #14

Ended up adding an optional mode to ResourceCache which returns also failed-to-load resources. This mode is now used by the editor.

-------------------------

cadaver | 2017-01-02 00:58:10 UTC | #15

It's one week later now than I initially anticipated, but any major work or fixes now that still should go into the release?

I'll implement the same "optionally disable automatic execute" to LuaScript subsystem and port the ConsoleInput sample to Lua, then I'm done.

-------------------------

weitjong | 2017-01-02 00:58:11 UTC | #16

Could you hold the release for a couple of days. I am reviewing the Urho2D library and I just found something that needs fixing.

-------------------------

cadaver | 2017-01-02 00:58:11 UTC | #17

Certainly, no hurry. Just notify me when you're done. I committed the changelog already in the meanwhile, but I think that doesn't hurt (also see if you have anything to add.)

-------------------------

weitjong | 2017-01-02 00:58:11 UTC | #18

I have completed the fix that I intend to do (bounding box update and network propagation). You can proceed with the release procedure.

There are still a few issues with the Editor support for the 2D library but I suppose we can fix them after the release.

-------------------------

cadaver | 2017-01-02 00:58:11 UTC | #19

Ok, that was fast! :wink: I'll check the editing experience too, if there's nothing especially serious I agree it can be left for later. In next release the 2D will be more mature anyway, with physics, documentation etc.

-------------------------

cadaver | 2017-01-02 00:58:12 UTC | #20

V1.31 has been tagged in the repository now. I have the usual manually-packaged MSVC executable build with static runtime enabled; will upload that to SourceForge first.

EDIT: uploaded. Thanks & congratulations to everyone involved, this version has a huge amount of new functionality!

-------------------------

weitjong | 2017-01-02 00:58:12 UTC | #21

Congrats!!! Yes, indeed.

I suppose you will announce it in our website too.

-------------------------

cadaver | 2017-01-02 00:58:12 UTC | #22

Yes, the post about the new release should be up. I'm still waiting for the automated 1.31 builds and then I'll finally post announcement in the forum also.

-------------------------

