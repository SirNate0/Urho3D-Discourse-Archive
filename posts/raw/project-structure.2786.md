shipiz | 2017-02-12 01:11:20 UTC | #1

So i'm working in Urho for some time and coming from cocos2d-x i feel that setup is a bit more complicated to get started. So i was thinking how it could be simplified and looking at cocos2d-x workflow, which is really easy to use, i couldn't help but suggest to have some kind of project generator which would generate full project, totally independent and self sufficient.

Here is how could potential project structure look like:

    - game
    -- macos-ios (xcode project containing both targets referencing shared folder which contains all cpp game code and per target specific classes)
    -- android (gradle + Urho3d library and shared game classes, which could be compiled directly from AndroidStudio, also easy to create JNI to connect various 3rd party SDKs like Ads, Analytics etc.)
    -- windows (visual studio project with reference to shared folder and platform specific files)
    -- linux (same as windows/mac)
    -- shared (game cpp files which would be included in every target)
    -- scripts (script files as/lua separated from resources)
    -- urho3d (source or compiled, if it is source, it could be added as submodule to be easily updated, thought it will have longer build times for a game project)
    -- resources (CoreData and Data copied here or just empty folder)

Basically when you generate project structure like this (the idea is taken from cocos2d-x and libgdx), you don't rely on anything except what is in this folder. It is easy to iterate and test on all platforms, really easy to get started since everything is already setup for you.

Tell me what you think.

-------------------------

hdunderscore | 2017-02-12 04:58:01 UTC | #2

Something that I often do and have thought about submitting as a PR is to break up the Data folder into SampleData, EditorData and SharedData or something like that, and then I start my project by placing all my generated resources into GameData to keep everything clean and separate.

For a c++ project, I share a similar thought with:
- Game
-- Android
-- Bin
-- CMake
-- Source
-- Urho3d
-- [cmake generated build directories]
-- CMakeLists.txt

Mostly mirroring the set-up described in the documentation. To save time I have just saved the template rather than regenerating every time, although I do believe there is a rake generator ?

Having more refined tools for project generation would definitely help with getting started with Urho though !

-------------------------

weitjong | 2017-02-12 11:12:24 UTC | #3

Our approach is to have a platform-agnostic source tree structure as possible. It is the build trees that are platform-specific, not the source tree itself. As for the asset directory, there is no hard rule how you want to do it. By default, the build system expects to find CoreData and Data but this is totally configurable. And for scaffolding, I use rake tasks all the way. We do not highlight those rake tasks strong enough because we don't want to say having Ruby is a must (although most of the host systems, except one, always have it installed by default).

-------------------------

shipiz | 2017-02-12 12:52:53 UTC | #4

I do understand the idea of current project setup. Though if you are developing a multiplatform game, you will only use cmake initialy to generate project for specific platform, or use it until you start implementing platfrom specific things (Ads, Analytics etc). After that you either have to modify cmake to include additional frameworks and source code for specific platform or just keep it as it is. That is why i'm suggesting this. In my opionion i would use cmake to generate a structure similar to this, and basically just use that, with option to easly update Urho3d to a newer version.

Edit:
As for the resources, something that bugs me is that urho is relying on me to have CoreData in my project. I would love that to be embedded with Urho3d, then with my own project. Updating Urho will update CoreData also. I would even include Editor inside the generate game project to have easy access and just jump in when you need it to build scenes/prefabs.

Workflow like this would give you easy way to code in c++, extend in as/lua, build in editor.

-------------------------

