nyt0x | 2017-01-02 01:13:20 UTC | #1

Hi!
I'm toying with urho3D and have a question that I can't find a good way to wrap my head around, not being very fluent in CMake stuff.

So I'm building uroh3D in a separate project and link my game project against it (using it as a lib, kinda following that documentation page [urho3d.github.io/documentation/1 ... brary.html](http://urho3d.github.io/documentation/1.5/_using_library.html))

But my problem is the following:
- When generating my game solution the Data folder is just copied from whatever is in "MyProject\bin" folder at the root of my project into "MyProject\Build\bin\Data".
(I have a symbolic link between "MyProject\bin\Data" and "Uroh3D\Build\bin\Data" as I thought it made sens at the time but I'm not so sure anymore)
-This copy step only happen when I generate (or re-generate) the solution through CMake.

My question is: What would be the best way to have a specific folder for the game Data?
Should I add a step in the game CMake to add a symlink to  "Uroh3D\Build\bin\" and then make the RessourceCache point to it when initializing the engine? In that case would that work if I ever need to pak the data after ? (i.e. for a release build )

Is there already something planned in the Urho3D CMake to handle such a case ? I've found a couple of forum post about a shared_path or something but I'm not sure it's still something exposed, as the post were old and the doc does not seem to have it in the build options (or I missed it / was looking for the wrong name?)

I'm not a build master and I admit that project settings and build solution generation is not my strength, so I'm sorry if it feels like a beginner question, but I'm trying to set up a clean bootstrap project rather than hacking something working and ending up having a lot of trouble down the road.

-------------------------

rasteron | 2017-01-02 01:13:20 UTC | #2

You can pretty much define your resource path and probably play around with it first using Urho3D Player.

I'm not sure if this works the same if you're planning to build on Android because the paths are still hardcoded (which does not seem to be a big issue) to Data;CoreData as I recall.

[github.com/urho3d/Urho3D/issues/809](https://github.com/urho3d/Urho3D/issues/809)

Hope that helps.

-------------------------

nyt0x | 2017-01-02 01:13:20 UTC | #3

I should have specified that I'm targeting windows only (vs2015). So the Android issue should not affect me.

Also when you say "play around with it first using Urho3D Player." I'm not sure I understand, you mean play around Urho3D? Or play around the Uroh3D Player code to see how they specify the code ?

Anyway looking at the Uroh3D Player code I found the "ResourcePrefixPaths" param I'll look into it , that might be the best solution. Or maybe from what I see, I could probably just set the URHO3D_PREFIX_PATH environment variable and see if it works the way I want.

But to be even more precise I was more thinking of setting the working directory of the visual studio solution to directly target a loose files folder (and use that as my ressource folder) for my Debug build and enabling the pak for the release Build all from CMake script.

I guess I can probably do an equivalent of the first one by using the ResourcePrefixPaths at engine init time (ifdef to Debug and add my loose file folder it could work for data, but that still mean that the other Data and DataCore folder will be there, which feel clunky), but I still don't know how to make the Release build use pak instead (but just the release build) as the paking operation is a post-build script added when generating the solution if I understand it correctly.

Any idea on that one ? or the whole thing?

-------------------------

jmiller | 2017-01-02 01:13:20 UTC | #4

Hi!

I use symbolic links in Windows all the time. [url=http://schinagl.priv.at/nt/hardlinkshellext/linkshellextension.html]Link Shell Extension[/url] makes it easy to manually link.

For my own projects, I find it most convenient to put the binaries in project root. CMakeLists.txt:
[code]include_directories(${URHO3D_INCLUDE_DIRS}) # just for context
set_output_directories(${CMAKE_BINARY_DIR}/.. RUNTIME PDB) # If your build tree is $project/build, this would put the binary in your project root[/code]

That frees me from using ResourcePrefixPaths, and since I use bleeding-edge Urho, I can symlink its resource directories to my project and just prefix my own.
There are also AutoloadPaths prioritized before the default folders, the default being "Autoload" you can add to your project and go.

If you want to hardcode... Your Application's Setup() is one method in which you can alter most parameters before they are acted upon.
#if !defined(_DEBUG)
engineParameters_["ResourcePaths"] = "ReleaseData;Data;CoreData";
#endif
[github.com/urho3d/Urho3D/blob/m ... e.cpp#L754](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Engine/Engine.cpp#L754)

I can't really speak on .pak as I haven't used them...

And I will just mention that with [b]thebluefish's[/b] ConfigManager, we can have stuff in a .cfg file and much less recompiling. :slight_smile: [topic1502.html](http://discourse.urho3d.io/t/a-more-advanced-ini-parser/1449/1)

HTH

-------------------------

jmiller | 2017-01-02 01:13:20 UTC | #5

I am not sure it helps the pak generation for VS, but for configuration-dependent stuff in cmake, I use

[code]
if(${CMAKE_BUILD_TYPE} STREQUAL "Debug")
  # debug stuff
else()
  # non-debug stuff
endif()
[/code]

-------------------------

rasteron | 2017-01-02 01:13:21 UTC | #6

[code]Also when you say "play around with it first using Urho3D Player." I'm not sure I understand, you mean play around Urho3D? Or play around the Uroh3D Player code to see how they specify the code ?
[/code]

Yes, that's the one.

-------------------------

nyt0x | 2017-01-02 01:13:24 UTC | #7

So basically what I wanted (having Data outside of "Build/bin") is something that should have work out of the box: 
[code]    # Create symbolic links in the build tree
    foreach (I Autoload CoreData Data)
        if (NOT EXISTS ${CMAKE_BINARY_DIR}/bin/${I})
            create_symlink (${CMAKE_SOURCE_DIR}/bin/${I} ${CMAKE_BINARY_DIR}/bin/${I} FALLBACK_TO_COPY)
        endif ()
    endforeach ()[/code]

But with windows10 lovely handling of admins rights CMake is never able to create those symlinks.. like never. So it rely on copy and copy Data folders.. which is what was bugging me out and making me looking for a way to have resource in an external shared folder in the first place.

Had to do the symlink manually. (understood that after a while playing with ressource prefix path, ressource path and the ressource handling in general. Soooo... thanks for pointing me out to playing with Urho3D, as usual stepping through the code is better than any documentation.)

So well, no need for any additional ressource folder now, but at least now I know how to set them up! (And to whoever wondering and reading that post, just my 0.02c but go for the hardcoded "resourcePaths" on the Setup of your application. The ressourcePaths prefix are not worth the headache and the noisy env_var that you would surely miss if deploying on another computer or for a team. But that's just my opinion. ps: by that I mean just go for an additional hardcoded ressource path and add a step in your make process to symlink to it, on the plus side you can now put your data on a different drive, which can come handy)

 Didn't check the whole packing thing but I think what you suggested Carnalis might work, but I'd need to take a better look at Urho3D-CMake-common.cmake first just so I do not miss any edgecase.

Also thanks for the config manager thingy, I've bookmarked that and will make sure to test it out, might come in handy at some point!

Cheers!

-------------------------

weitjong | 2017-01-02 01:13:24 UTC | #8

Just want to point out that you have understood the purpose of having ResourcePrefixPath wrongly. It is, as its name implies, a way to define a "prefix" path to your assets. Assuming all your assets are in a single parent directory (but that is not a must), the prefix path allows that parent directory to be freely located relative to your binary location. You can define it as "../Resources" and the engine will look for your assets there. This is by the way how we can bundle the assets into macOS app and tell the engine they are there. If you have multiple parent directories then your ResourcePrefixPath becomes a list of paths. Hope this clarifies.

-------------------------

nyt0x | 2017-01-02 01:13:28 UTC | #9

So basically [b]resource prefix path[/b] are prefix that are added to all the [b]resource path[/b] registered all the time? or does the resource manager search fort all [b]resource path[/b] first and then all [b]resource path[/b] + the prefix.
Also prefix to a path is the same as assuming all path are relatives. so basically you are just recreating a new relative resource path by concatenating a resource path and the prefix. Which is the same thing as registering the correct relative path to your resource in the first place in the engine init, right?

-------------------------

jmiller | 2017-01-02 01:13:28 UTC | #10

Yes, Engine::Initialize() adds all of the prefix(es) to each ResourcePaths and does AddResourceDir() with those.
[github.com/urho3d/Urho3D/blob/m ... e.cpp#L217](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Engine/Engine.cpp#L217)

The ResourcePrefixPaths engine parameter described: [urho3d.github.io/documentation/ ... _loop.html](https://urho3d.github.io/documentation/HEAD/_main_loop.html)
"ResourcePrefixPaths (string) A semicolon-separated list of resource prefix paths to use. If not specified then the default prefix path is set to executable path. The resource prefix paths can also be defined using URHO3D_PREFIX_PATH env-var. When both are defined, the paths set by -pp takes higher precedence."

-------------------------

weitjong | 2017-01-02 01:13:28 UTC | #11

effective-resource-path = resource-prefix-path + resource-path

Both paths are semi-colon separated lists. Engine search for them in the order given by the list. It stops the search immediately when the effective path is valid/found. The list of resource-path is assumed to be relative path always. The list of resource-prefix-path is optional, when not provided then Urho3D uses the executable path as the prefix for backward compatibility with previous Urho3D releases when the resource prefix path concept hasn't been introduced yet.

-------------------------

