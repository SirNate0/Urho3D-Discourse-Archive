Spongie | 2017-01-02 01:02:45 UTC | #1

Hello.

I've been mucking about with Urho3D for a few days now. Yesterday I tried to start and run the engine without any of the file-based resources that come with Urho3D. That involves setting up the render path manually, also creating geometries and shaders on the fly. It works, but the API doesn't make it easy for people to use the engine from scratch.

Here's a few suggestions that would help a lot with gaining control of the API without adding much overhead for the API user:

1. Ditch the current prefix / data paths setup.
    Is the extra code of having to write cache->AddResourceDir(mypath) really worth reducing flexibility over? I suggest a build time const char * or define that holds the Urho3D data home. It CAN be used, but      
    nobody is forced to use it. Thusly, the exact same thing done by the engine parameters could be done in Setup with cache->AddResourceDir(URHO3D_DEFAULT_PATH + "/Data")   
    and cache->AddResourceDir(URHO3D_DEFAULT_PATH + "/CoreData"). Two lines of code to replace the enigne parameters and the sort of messy code in Engine::Initialize. You could also ditch the whole "prefix" and "actual   
    path" separation, this is bread and butter code, we don't need the engine to handle this. (also Urho3D provides nice portable filesystem features, so all in all this is better to leave to the user)
    Trying to figure out every use case is impossible, so I'm better of finding and adding my own resource directories as I please and also handle possible errors. At worse, the poor user must write two lines of code to replace
    everything that's automagic through engine parameters and Initialize right now.
    This would also help with the ridiculous install policy to put data in $PREFIX/bin (it should be in $PREFIX/share), the sample binaries should use the URHO3D_DEFAULT_PATH as set during Urho3D build to know where the data is.

2. Default render path, textures, style and UI should NOT be loaded automatically. 
    Again, what if I don't want to use them? Try to break this out into a separate call after the engine has been initialized, it will also allow the user to
    catch missing file errors and react accordingly, perhaps add more resource dirs or whatever. No reason to limit the API usability for this tiny extra bit of automagic.
    Perhaps just add a convencience call like Engine::InitializeDefaultResources, but really, I think users should explicitly have to load the resources. It's 6 lines of code you're saving us from.

3. RenderPath needs helper methods to create or set specific RenderPathCommand's. Right now it's a pain to set up a 7 command render pass manually. It wouldn't hurt if there was a way to "zero" it or maybe a const somewhere 
    with an empty, like RenderPathCommand::EMPTY. 

Thank you for taking time to read through all of that. I hope it isn't all nonsense, my focus is bad when I write so much text that isn't code. :slight_smile:

-------------------------

cadaver | 2017-01-02 01:02:45 UTC | #2

Interesting points. Some of them actually echo the direction I've taken in the Turso3D experimental engine, which is strictly a library (instead any framework-like tendencies Urho3D has) and does not access any files on its own.

However, in Urho some of the default data you need to produce is complex, for example the attenuation texture for a spot light, so providing it all programmatically will be involved and I'm not sure if it's worth it. For practical use of renderpaths I'd say the same thing. Though in that case file access shouldn't need to be a necessity; it's probably shorter code if you define the renderpath XML as a string literal, stuff it to eg. VectorBuffer, then load from there.

-------------------------

weitjong | 2017-01-02 01:02:45 UTC | #3

I will just comment on #1 (actually just a small part of it), as involved a mistake I had done yesterday (and the mistake has been fixed now). Before yesterday, the runtime install destination was "share/Urho3D/Bin". This destination was used for both the target executables and resource dirs  (CoreData and Data). There was no "resource prefix path" engine parametr back then, so both target executables and resource dirs had to be installed in a same location previously. This was exactly the reason why we had chosen to install to "share/Urho3D/Bin" instead of "bin" in the first place. But since now we have introduced the "resource prefix path" engine parameter in the new build system, it opens up the possibility to have the target executables and the resource dirs to be installed in different location. It also opens the possibility for the Mac OS X Bundle build option. It was a simply mistake on my part yesterday when I change the runtime install destination for the target executables to "bin", without readjusting the install destination for the resource dirs so the resource dirs got installed to "bin" too (which was bad, of course).

Re. Putting the resource prefix path as a constant in the C++ code. Personally, I like our current way better. It has proven to work for all the use cases and platforms. If you want to hard-wired the resource path in your own project, you can also do so with our current code. I.e by initializing the engine parameter statically in your code. 

For the rest of your points, I think you have to wait for the engine author to respond.

EDIT: it looks like he already did :slight_smile:

-------------------------

Spongie | 2017-01-02 01:02:46 UTC | #4

Hey. Thanks for quick replies. You guys are amazing!

"Putting the resource prefix path as a constant in the C++ code. Personally, I like our current way better."

It's just the system default that was used at build time, you don't have to use it. You can still use your own environment variables, configurations or even hardcoded engine parameters. This is how things have traditionally been done to handle default paths for a system. It's nothing special, it's like a version string or whatever. And it's not a prefix path anymore, it's just a resource directory.

As for the more flexible aproach to handling paths and resource loading, I got rid of all the defaults and wrote my own render path and shaders. It works, but I have to work against the API and abuse somewhat instead of working with it.
Not all projects must be file resource dependent, Urho3D is already well designed enough to allow me to do this, just a few minor API changes really, no new work on the use flow/cases needed.

You can make both use cases (either you want to load default resources or you don't) very easy by accomodating some of the points I made. Save ~9 lines of code to get the defaults up and working, this would be an OK "compromise" between the "boxed in framework" and a regular API.

EDIT: and yes, you can define the XML as a literal string, that would be an acceptable form of creating render paths on the fly. Same with any other resource that works the same way. But the path handling is still an issue, I should've split it up into two subjects I suppose.

-------------------------

Spongie | 2017-01-02 01:02:46 UTC | #5

Oh, I checked out Turso3D. I'm wondering why you discarded the component design in favour of subclassing nodes. Tried buildling it, first problem I found is that FLT_MAX is defined in float.h (cfloat), not limits.h, then some template problems. I'll just leave it alone for now. :slight_smile: Anyway, you do keep yourself busy with some great stuff.

-------------------------

cadaver | 2017-01-02 01:02:46 UTC | #6

Turso3D has no window creation code for non-Windows systems yet, so indeed (for most) it's best to leave alone for now. 

Not to derail this thread too much with Turso3D discussion, but I'll say that in it the roles of child node and component are merged to simplify the scene hierarchy and the amount of API calls needed to get something going on, and it seems to fit my line of thinking well, as I've always written components more as "active" objects instead of passive data containers acted on by systems (which seems to be the "orthodox" entity-component thinking)

-------------------------

OvermindDL1 | 2017-01-02 01:02:46 UTC | #7

[quote="cadaver"]Turso3D has no window creation code for non-Windows systems yet, so indeed (for most) it's best to leave alone for now. 

Not to derail this thread too much with Turso3D discussion, but I'll say that in it the roles of child node and component are merged to simplify the scene hierarchy and the amount of API calls needed to get something going on, and it seems to fit my line of thinking well, as I've always written components more as "active" objects instead of passive data containers acted on by systems (which seems to be the "orthodox" entity-component thinking)[/quote]
That 'orthodox' method is always the way I have done it in the past, it has worked out for me and has great speed boons *if* you combine your data in the right way for your game, every game is different though so it is impossible to make, say, even a fully generic 'position' node if you want it to be very efficient, though still quite possible to include a few variants.

-------------------------

