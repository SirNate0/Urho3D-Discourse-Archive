OvermindDL1 | 2017-01-02 00:58:01 UTC | #1

The current way that CMake is used in the library is very non-standard and does not work with many CMake utilities as it stands.  I am currently working on an overhaul on the CMake build system at [github.com/OvermindDL1/Urho3D/t ... e-overhaul](https://github.com/OvermindDL1/Urho3D/tree/CMake-overhaul) and at the moment my quick tests show everything seems to compile and works and now works with the utilities I was needing to use as well.  I expect that the cmake_*.sh/bat build scripts are utterly broken right now (though fixing should be rather simple, but I question more of why they exist?).

Currently though:
[ul]
[li]The project root is actually the project root now instead of "<root>/Source"[/li]
[li]The arguments listed on the README.md file (like ENABLE_64BIT) are actually exposed to the interactive prompts and GUI now with proper documentation strings and default values[/li]
[li]Found a few other arguments that were not listed on the README.md file that are exposed now too (maybe they should be marked as advanced?)[/li]
[li]Can actually use Urho3D as a CMake ExternalProject dependency now!  ^.^[/li]
[li]Been trying to clean up that 'magic' file, it makes a lot of assumptions, as did the FindUrho3D.cmake file, it needs a config file made as per CMake standards too[/li][/ul]

But now I must head to work, shall work more on it later.  If anyone could download and try out my branch that is linked above and see if it still compiles fine (using cmake directly, not the sh/bat script).

Would this as a pull request be accepted once I finish the work in full?  The non-standard CMake setup of the project was really not working well with the normal CMake utilities and I would prefer not to have to keep my fork up to date as the main project gets updated.  :slight_smile:

-------------------------

cadaver | 2017-01-02 00:58:01 UTC | #2

You should coordinate with weitjong, who is the primary build system maintainer, and also check the very recent changes to the master branch build system (for example Urho-CMake-magic.cmake is called Urho-CMake-common.cmake now) Generally, if things become more standardized and flexible and nothing breaks, I wouldn't see a reason to not incorporate the changes.

I'd guess the most straightforward way to get things rolling is to simply post the changes as a pull request once you've merged with latest master.

-------------------------

weitjong | 2017-01-02 00:58:01 UTC | #3

I renamed that module in the master branch exactly because I don't want to see bits that we want to share from being moved back to main CMakeLists.txt :wink:

-------------------------

OvermindDL1 | 2017-01-02 00:58:02 UTC | #4

Sorry about the other thread, that was before I decided to try working on it.

And yep, I noticed the recent work, that did not exist before.  :wink:

Basically I have been using this for a long time to manage remote dependencies:  [url]http://www.cmake.org/cmake/help/v2.8.12/cmake.html#module:ExternalProject[/url]
You basically just it, say, a git repo (svn, raw file url, etc...), it makes multiple directories in the build directory in a subdirectory of the externalproject name to download in, another for building, another for holding some metadata, and another for the installation directory.
It then downloads/clones/etc the external project.
cmake's into the separate build directory it made using whatever extra args you specify.
It then make/builds it in the build directory.
It then installs it in to the install directory.
You then link in the install directory (the ExternalProject_Add can give you the variable of the path) for headers, libraries, etc...

Basically I was just simplifying that from what I am doing now so I can remove the 'commands':
[code]
ExternalProject_Add(urho3d
	GIT_REPOSITORY https://github.com/urho3d/Urho3D.git
	GIT_TAG master
	CONFIGURE_COMMAND cd ../urho3d && ./cmake_gcc.sh
	CMAKE_ARGS
		-DENABLE_64BIT=1
		-DENABLE_LUAJIT=1
		-DENABLE_ANGELSCRIPT=0
		-DUSE_OPENGL=1
		-DENABLE_TOOLS=1
		-DURHO3D_FOUND=ON
		-DUSE_STATIC_RUNTIME=1
		-DURHO3D_LIB_TYPE=STATIC
		-DCMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}
		-DCMAKE_INSTALL_PREFIX:PATH=${URHO3D_INSTALL_DIR}
	BUILD_COMMAND cd ../urho3d/Build && make -j6
	INSTALL_COMMAND cd ../urho3d/Build && make install
)
[/code]
Which is very linux-oriented and not compilable on Windows as it stands, would need to change the commands and what is done for whatever is done for windows, would be nice to be able to use the cmake project, but it cannot unless the root CMakeLists.txt is in the root directory of the project.

-------------------------

weitjong | 2017-01-02 00:58:02 UTC | #5

I think I understand the CMake "External Project" concept. It makes your project as the central of thing and put Urho3D project (not just the Urho3D library) as external. I understand that it could download/build/install the external project automatically for you so that you only need to focus on your own project. I would like to see that being supported by Urho3D project as well.

As it stands today, our existing build scripts are still centered around Urho3D project. Using Urho3D library as an external library is pretty much an after thought. Having said that, in our own way we do support using this use case as documented in [urho3d.github.io/documentation/a00004.html](http://urho3d.github.io/documentation/a00004.html). The drawback with our current approach is, it still put Urho3D project in the center, it needs to be 'pulled' and build separately before building the dependent project. On the other hand, it does provide a 'feature' that is not possible using the "External Project" approach. In our unorthodox way, we could let dependent project refers to Urho3D library in its project root tree. i.e. it does not require Urho3D library to be installed first in the local filesystem. Imagine the scenario where one could have different version of Urho3D project root trees (one tracking remote master, a few from previous release tags, or one that merged with someone's own changes, etc); the dependent project have the option to use any one of these Urho3D library by simply changing the URHO3D_HOME environment variable, without needing to overwrite the Urho3D installation in their filesystem. So, I would like to see we add new "External Project" support into our build scripts without losing our current 'feature' for no reason.

Also, as it stands today, our existing build scripts are friendlier to command line interface than to GUI tools. It is apparent that building of Urho3D using cmake-gui is not even mentioned officially in our documentation. You are welcome to make any changes that would make cmake-gui becomes officially supported and hence building Urho3D using cmake-gui can be properly documented. There is one important thing, however, that I would like to point out. We are just recently completed our change to instruct CMake to configure an "out-of-source" build tree. So, naturally, we would think twice (at least for me) to accept changes that would bring us back to a non "out-of-source" build again. There are a few reasons why an out-of-source build is better. In short, you have to convince us on why we need a new CMakeLists.txt in the project root but outside of "Source" directory.

-------------------------

OvermindDL1 | 2017-01-02 00:58:03 UTC | #6

Actually you could keep the current way too, just need a root CMakeLists.txt that can build out of source by default.

Mostly I like to do it this way so I can link to a specific git tag so I do not need to worry about what my jenkins build server has or I have or whatever else.  My ExternalProject list of things to auto-grab and build is fairly extensive.  :slight_smile:

And I never use the GUI tools, but the variables also work well for the cmake interactive mode (-i).
Take a look at my root CMakeLists.txt in that cmake branch and see what I did to the 'set's, the cache and so forth is how you define variables that are supposed to be set by the user and the defaults.
Basically if the cache entry does not exist, it creates one with the default, if it exists otherwise (being -D defined or set in -i or in the gui) then it uses the existing value.  Along with the help string of course.

Even just a CMakeLists.txt in the project root that just defines the project name and add_subdirectory(Source) would be fine if you fixed the non-relative directory variables used in the rest of the files like I did.

Also, the one in Source includes ../Docs, which is bad bad bad, you should not be accessing outside of the project root directory.

A lot of the ENABLE_* also still try loading things before testing if it should compile them, I moved that to surround the include of the directory in full, which fixed a lot as well.  See my commits before I delete the fork?

-------------------------

weitjong | 2017-01-02 00:58:03 UTC | #7

It appears you have not committed new changes or merged recent changes from main repo. If that is the case then I have seen your work in your fork. As Lasse has mentioned in the second post, it is easier for us to review if you post your final changes as a pull request. If it is possible, please do share with us by also updating the GettingStarted.dox to include a new section on how you use Urho3D project as ExternalProject.

I agree with you that providing a help string and default value for the build options is a good idea. I am not sure though which would be better, using CMake "option()" command or "set(CACHE BOOL)" command.

[quote="OvermindDL1"]Even just a CMakeLists.txt in the project root that just defines the project name and add_subdirectory(Source) would be fine if you fixed the non-relative directory variables used in the rest of the files like I did.[/quote]
If it still being configured as an out-of-source build then it should be OK then. There is a valid reason why we decided to move the main CMakeLists.txt into the Source directory back then. If I recall correctly it was due to CMake warning for Eclipse/CDT generator. I will have to check that again after you have submitted your pull request.

[quote="OvermindDL1"]Also, the one in Source includes ../Docs, which is bad bad bad, you should not be accessing outside of the project root directory.[/quote]
To tell you the truth, I myself even surprised that it actually works. The 'doc' built-in target is added very recently. As opposed to moving the 'Doc' subdirectory into 'Source' directory, using the "../Docs" is more pragmatic. You make it sounds like it is totally broken for your setup without explaining exactly why it is bad. And yet, it is [i]proven[/i] kind of working fine in our use cases. The 'doc' built-in target is used as part of our Travis CI setup to update our site documentation, and so far we don't see any problem.

[quote="OvermindDL1"]A lot of the ENABLE_* also still try loading things before testing if it should compile them, I moved that to surround the include of the directory in full, which fixed a lot as well.  See my commits before I delete the fork?[/quote]
In general I am fine with this refactoring. However, please be careful though with its implication. For example, when ENABLE_TOOLS=0 we still want Urho3DPlayer tool to be added as a CMake target. In your fork, it would inadvertently exclude it.

-------------------------

OvermindDL1 | 2017-01-02 00:58:03 UTC | #8

[quote="weitjong"]It appears you have not committed new changes or merged recent changes from main repo. If that is the case then I have seen your work in your fork. As Lasse has mentioned in the second post, it is easier for us to review if you post your final changes as a pull request. If it is possible, please do share with us by also updating the GettingStarted.dox to include a new section on how you use Urho3D project as ExternalProject.[/quote]
Certainly, I was planning to if I got it working like other projects do so it would be simple and issue-less.

[quote="weitjong"]I agree with you that providing a help string for the build options is a good idea. I am not sure though which would be better, using CMake "option()" command or "set(CACHE BOOL)" command.[/quote]
They do the same thing in basic usage, but set is more idiomatic from what I have seen and has more power if you need to do more special overriding (like adding FORCE for ENABLE_LUA if ENABLE_LUAJIT is enabled).

[quote="weitjong"][quote="OvermindDL1"]Even just a CMakeLists.txt in the project root that just defines the project name and add_subdirectory(Source) would be fine if you fixed the non-relative directory variables used in the rest of the files like I did.[/quote]
If it still being configured as an out-of-source build then it should be OK then. There is a valid reason why we decided to move the main CMakeLists.txt into the Source directory back then. If I recall correctly it was due to CMake warning for Eclipse/CDT generator. I will have to check that again after you have submitted your pull request.[/quote]
I have never tried Eclipse for C++ (used it for Java, it is crashy as heck though, much other better IDE's), but if you have the warning laying around somewhere then there is likely a fix for it.

[quote="weitjong"][quote="OvermindDL1"]Also, the one in Source includes ../Docs, which is bad bad bad, you should not be accessing outside of the project root directory.[/quote]
To tell you the truth, I myself even surprised that it actually works. The 'doc' built-in target is added very recently. As opposed to moving the 'Doc' subdirectory into 'Source' directory, using the "../Docs" is more pragmatic. You make it sounds like it is totally broken for your setup without explaining exactly why it is bad. And yet, it is [i]proven[/i] kind of working fine in our use cases. The 'doc' built-in target is used as part of our Travis CI setup to update our site documentation, and so far we don't see any problem.[/quote]
I did experience an issue as it fell outside of the project directory and was not properly tracked in KDevelop (which uses the project CMakeLists.txt in the root project directory as the build project, it has first-class support for CMake).

[quote="weitjong"][quote="OvermindDL1"]A lot of the ENABLE_* also still try loading things before testing if it should compile them, I moved that to surround the include of the directory in full, which fixed a lot as well.  See my commits before I delete the fork?[/quote]
In general I am fine with this refactoring. However, please be careful though with its implication. For example, when ENABLE_TOOLS=0 we still want Urho3DPlayer tool to be added as a CMake target. In your fork, it would inadvertently exclude it.[/quote]
Shouldn't the Player be moved outside of Tools into a dedicated 'Launcher' or something section with its own ENABLE_STANDALONEBINARY or something?  For my use I do not need tools, that launcher, docs, etc... (well, maybe some tools later, would be nice to have an ENABLE_* for each tool as well, each defined as its own project as well).

Sorry if I pick at things, I am a stickler for simple and expected usage, feel free to say "No" at anything I do and I will not bother working on it as it will reduce my time, I have a tendency to waste time trying to 'perfect' things so it is welcome at times.  ^.^

-------------------------

weitjong | 2017-01-02 00:58:03 UTC | #9

[quote="OvermindDL1"]Shouldn't the Player be moved outside of Tools into a dedicated 'Launcher' or something section with its own ENABLE_STANDALONEBINARY or something?  For my use I do not need tools, that launcher, docs, etc... (well, maybe some tools later, would be nice to have an ENABLE_* for each tool as well, each defined as its own project as well).[/quote]

To keep it short, I just respond to the last paragraph. You can propose anything you like. Any contribution to refactor existing thing or add new thing or delete useless thing are welcome, as long as it does not break other use cases while incorporating new one.

-------------------------

doodloo | 2017-01-02 01:01:04 UTC | #10

Hi devs :slight_smile:

Regarding my post here: [post2910.html#p2910](http://discourse.urho3d.io/t/urho3d-build-system/520/1)
i would like to know if the code is actually undergoing any change? Are there any changes being done right now to the way files are intricated to each other?
Would a pull request be accepted if:
- Using QMake instead of CMake (Just as a dev requirement for building),
- Allowing a clean framework set of files (.so / .dylib / .a + includes + bin) instead of the existing?
Are there any unit tests or test suite available right now to make sure that a change isn't breaking something? If yes, how to run them?

Thanks,
Doodloo.

-------------------------

weitjong | 2017-01-02 01:01:04 UTC | #11

I am not sure how to answer your first two questions. The project's master branch is always moving, sometimes slowly sometimes fast. We have never imposed a code freeze to other contributors because of any reasons before.

If you ask me (and I am the main maintainer of the build script) then I would bluntly say there is no plan to migrate from CMake to QMake at the moment. I am using Gnome on Fedora system. I think that say pretty much already on my lineage. We don't want any Qt dependencies just to configure/generate our project files.

We do not have unit tests yet. All we have now are functional tests (or at least that what I call them). As part of the CI build, we invoke all our sample applications. If they run and shutdown cleanly in a predefined time period then they are considered as passing the test. To execute the test, run "make test" (this only works when the generated Urho3D project is configured with URHO3D_TESTING build option set).

-------------------------

cadaver | 2017-01-02 01:01:07 UTC | #12

I can also weigh in that I would consider use of QMake unacceptable, as it's closely tied to Qt, and Urho itself does not require or use Qt.

-------------------------

OvermindDL1 | 2017-01-02 01:01:17 UTC | #13

[quote="doodloo"]Hi devs :slight_smile:
- Allowing a clean framework set of files (.so / .dylib / .a + includes + bin) instead of the existing?
[/quote]
Ditto on the QMake, it is fairly useless as CMake has all of its functionality that is needed by Urho3D, though a proper set of CMake bindings for external projects would be exceedingly nice, specifically by using CMake's built in resolution system that can output a descriptor file (so you can store the build settings that are needed to bind to the libraries and all) and link to it instead of needing to bring in the rather monolithic CMake system of Urho3D in to your project.

-------------------------

