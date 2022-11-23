rku | 2017-11-09 10:40:29 UTC | #1

Less than two weeks ago i started working on yet another Urho3D editor. It is not usable just yet, but it probably is in good-enough shape to be showed off, so here it is.
![editor|690x398](upload://rwQlMkABHsmMCQ04xLfVMMmaEu2.jpg)

Features:
* Uses [imgui](https://github.com/ocornut/imgui) for UI
* Scene hierarchy widget
* Attribute inspector widget supporting 99% of Urho3D variant types
* Material resource editor
* Mask widget (for light masks etc)
* Resource path browser widget
* Drag&drop for (some) resources
* Scene settings (renderpath, postprocess)
* Open multiple scene tabs
* Save/Open existing scenes
* Save/Open projects (project includes widget layout, opened scenes, various settings)
* HDPI support

Missing but planned features:
* Create/delete objects
* Undo/redo
* Objects for representing invisible scene nodes (like lights and cameras)
* Icons for components
* Save scene as a new resource
* Create new materials from scratch and save them
* Resource browser with previews
* Drag&Drop with previews
* UI layout editing in a new dedicated tab
* Many more i cant think of right now

Code at: https://github.com/rokups/Urho3D
If you wish to test it - be sure to use `-DURHO3D_TOOLS=ON` cmake parameter.

-------------------------

yushli1 | 2017-11-09 10:12:15 UTC | #2

That looks quite nice.Will try it out. Thank you for sharing it.
What is the priority of the UI layout editor? I think it will be nice to have that as well.

-------------------------

rku | 2017-11-09 10:15:06 UTC | #3

[quote="yushli1, post:2, topic:3718"]
What is the priority of the UI layout editor? I think it will be nice to have that as well.
[/quote]

That really is low in my TODO list. UIEditor itself is somewhat done, but it is in separate application and needs to be "just wired in". It's code too could definitely use some love too.

-------------------------

yushli1 | 2017-11-09 10:21:06 UTC | #4

I am just wondering how to design the UI editor that can let people design the UI once, then run seamlessly on any phones with different screen sizes and resolutions. Or how to do screen adaptation generally in Urho3D.

-------------------------

rku | 2017-11-09 10:24:44 UTC | #5

I solved this problem like so:
```cpp
GetSubsystem<UI>()->SetScale((float)GetGraphics()->GetWidth() / 1920.f);
```
UI was designed for 1080p resolution. It scales up or down on phones fine. Not sure how it would do on 4k screen on desktop though.

-------------------------

yushli1 | 2017-11-09 10:32:14 UTC | #6

Suppose you design for a screen size of 1000x1000(just an example), then it now needs to run on a screen with size of 1200x1000. The upper right button which is designed at the position of (1000,1000) can only be at position(1000,1000) and cannot reach the real upper right corner. A better solution may be to add a anchor choice to the UI editor, so that we can set this property to "upper right", then the button will stay at the actual desirable position at the running device.

-------------------------

rku | 2017-11-09 10:38:57 UTC | #7

UI already has these settings. They are called "Horiz Alignment" and "Vert Alignment".

-------------------------

yushli1 | 2017-11-09 10:40:36 UTC | #8

Will these settings be configurable in your up coming UI editor?

-------------------------

rku | 2017-11-09 10:51:04 UTC | #9

UIEditor (and Editor) present any registered attributes (`URHO3D_ATTRIBUTE` and similar macros) so yeah - these options are already available in standalone UIEditor and will be available once it gets merged to editor. In fact i am pretty sure official editor exposes them as well.

-------------------------

yushli1 | 2017-11-09 10:54:35 UTC | #10

Got it. I didn't use the official UI editor because there is no tutorial for a beginner. I will wait for your new UI editor, and hopefully you will have at least a simple beginner tutorial for some basic operations.

-------------------------

Eugene | 2017-11-09 13:12:56 UTC | #11

Looks interesting. I also wanted to try ImGUI for Editor but didn't actually tried it yet.
Have you faced any problems with ImGUI? Are built-in widgets bug-free?
What's performance of Hierarchy? Is it possible to implement drag&drop of hierarchy items in ImGUI?
Does ImGUI support OS files drag&drop?
I'll try the Editor this evening. Probably I should move this way.

-------------------------

rku | 2017-11-09 13:28:51 UTC | #12

> Have you faced any problems with ImGUI? Are built-in widgets bug-free?

Overall i am extremely happy with imgui. I havent noticed any bugs i would need to work around. One notable thing is that built in widgets for integers and doubles cast them to floats internally, so that may be source of issues at some point.

> What’s performance of Hierarchy?

I have not noticed any performance issues so far. I even do some string formatting on every frame.

> Is it possible to implement drag&drop of hierarchy items in ImGUI?

Sure, and it actually is very simple. My drag&drop support is probably less than 40 lines long. It goes something like this:

1. Set "drag data" to some global spot, like subsystem driving UI
2. Subsystem renders frameless imgui window at mouse position if there is drag data set and left mouse button is down
3. Widget accepting drop checks if there is drag data set and mouse was released on this frame, if so - gets drag data from the subsystem and uses it, subsystem no longer stores drag data.

For hierarchy it would work the same.

> Does ImGUI support OS files drag&drop?

ImGui itself does not handle drag&drop at all, but we can possibly make it work. Urho3D supports dropping OS files on to window, with coordinates where it is dropped. That is enough to make imgui widgets accept that drop.

> Probably I should move this way.

I want to collaborate. Thing is biggest turndown for contributing to Urho3D is the fact that bundings have to be maintained manually. That is neither fun, nor straightforward at times.. In case of editor that could be less of a problem though.

-------------------------

Eugene | 2017-11-09 13:32:39 UTC | #13

Could I PM you somewhere?
Skype/Gitter/WhatsUp/Slack etc...

-------------------------

rku | 2017-11-09 13:33:25 UTC | #14

im on gitter, in Urho3D room as well. Username is @rokups

-------------------------

Eugene | 2017-11-19 22:10:51 UTC | #15

The Editor is now compatible with main Urho repo.
Could be checked out from https://github.com/rokups/Urho3D-Toolbox

-------------------------

johnnycable | 2017-11-20 09:28:20 UTC | #16

How am I supposed to integrate it with the master? Drag and drop somewhere then cmake and rebuild everything?

-------------------------

rku | 2017-11-20 09:31:12 UTC | #17

You are supposed to build master branch of Urho3D and use it as SDK to build Urho3D-Toolbox. At the moment it is little more than a demo. Do not expect useful tool just yet.

-------------------------

johnnycable | 2017-11-20 10:13:44 UTC | #18

![32|622x499](upload://tYbVOBzZgM3LhtzltDvMo1gByTy.jpg)

![29|690x468](upload://n9vDYqPctj2SEbtWpgwCAWnYPLY.png)

That's OK

-------------------------

slapin | 2017-11-20 10:13:58 UTC | #19

    cmake .. -DURHO3D_HOME=/home/slapin/Urho3D/build
    -- The C compiler identification is GNU 6.3.0
    -- The CXX compiler identification is GNU 6.3.0
    -- Check for working C compiler: /usr/bin/cc
    -- Check for working C compiler: /usr/bin/cc -- works
    -- Detecting C compiler ABI info
    -- Detecting C compiler ABI info - done
    -- Detecting C compile features
    -- Detecting C compile features - done
    -- Check for working CXX compiler: /usr/bin/c++
    -- Check for working CXX compiler: /usr/bin/c++ -- works
    -- Detecting CXX compiler ABI info
    -- Detecting CXX compiler ABI info - done
    -- Detecting CXX compile features
    -- Detecting CXX compile features - done
    -- Found Urho3D: /home/slapin/Urho3D/build/lib/libUrho3D.a (found version "1.7-66-g1fe5fdac2")
    failed to create symbolic link '/home/slapin/Urho3D-Toolbox/build/bin/Autoload': No such file or directory
    failed to create symbolic link '/home/slapin/Urho3D-Toolbox/build/bin/Data': No such file or directory
    failed to create symbolic link '/home/slapin/Urho3D-Toolbox/build/bin/CoreData': No such file or directory
    failed to create symbolic link '/home/slapin/Urho3D-Toolbox/build/bin/EditorData': No such file or directory
    -- Configuring done
    -- Generating done
    -- Build files have been written to: /home/slapin/Urho3D-Toolbox/build
    slapin@slapin-pc:~/Urho3D-Toolbox/build$ ls
    AssetViewer  bin  CMakeCache.txt  CMakeFiles  cmake_install.cmake  Editor  Makefile  ThirdParty  Toolbox  UIEditor
    slapin@slapin-pc:~/Urho3D-Toolbox/build$ ls bin
    EditorData
    slapin@slapin-pc:~/Urho3D-Toolbox/build$ make
    Scanning dependencies of target IconFontCppHeaders
    [  2%] Building CXX object ThirdParty/IconFontCppHeaders/CMakeFiles/IconFontCppHeaders.dir/INTERFACE.cpp.o
    [  5%] Linking CXX static library libIconFontCppHeaders.a
    [  5%] Built target IconFontCppHeaders
    Scanning dependencies of target imgui
    [  8%] Building CXX object ThirdParty/imgui/CMakeFiles/imgui.dir/imgui.cpp.o
    /home/slapin/Urho3D-Toolbox/ThirdParty/imgui/imgui.cpp:576:0: warning: "IMGUI_DEFINE_MATH_OPERATORS" redefined
     #define IMGUI_DEFINE_MATH_OPERATORS
     
    <command-line>:0:0: note: this is the location of the previous definition
    [ 11%] Building CXX object ThirdParty/imgui/CMakeFiles/imgui.dir/imgui_draw.cpp.o
    /home/slapin/Urho3D-Toolbox/ThirdParty/imgui/imgui_draw.cpp:16:0: warning: "IMGUI_DEFINE_MATH_OPERATORS" redefined
     #define IMGUI_DEFINE_MATH_OPERATORS
     
    <command-line>:0:0: note: this is the location of the previous definition
    [ 14%] Building CXX object ThirdParty/imgui/CMakeFiles/imgui.dir/imgui_freetype.cpp.o
    [ 17%] Linking CXX static library libimgui.a
    [ 17%] Built target imgui
    Scanning dependencies of target ImGuizmo
    [ 20%] Building CXX object ThirdParty/ImGuizmo/CMakeFiles/ImGuizmo.dir/ImGuizmo.cpp.o
    [ 23%] Linking CXX static library libImGuizmo.a
    [ 23%] Built target ImGuizmo
    Scanning dependencies of target tinyfiledialogs
    [ 26%] Building C object ThirdParty/tinyfiledialogs/CMakeFiles/tinyfiledialogs.dir/tinyfiledialogs.c.o
    [ 29%] Linking C static library libtinyfiledialogs.a
    [ 29%] Built target tinyfiledialogs
    Scanning dependencies of target Toolbox
    [ 32%] Building CXX object Toolbox/CMakeFiles/Toolbox.dir/Common/UndoManager.cpp.o
    /home/slapin/Urho3D-Toolbox/Toolbox/Common/UndoManager.cpp: In member function ‘virtual void Urho3D::Undo::XMLParentState::Apply()’:
    /home/slapin/Urho3D-Toolbox/Toolbox/Common/UndoManager.cpp:191:17: error: ‘class Urho3D::XMLElement’ has no member named ‘AppendChild’; did you mean ‘GetChild’?
             parent_.AppendChild(item_);
                     ^~~~~~~~~~~
    /home/slapin/Urho3D-Toolbox/Toolbox/Common/UndoManager.cpp: In member function ‘void Urho3D::Undo::Manager::XMLRemove(Urho3D::XMLElement&)’:
    /home/slapin/Urho3D-Toolbox/Toolbox/Common/UndoManager.cpp:328:13: error: ‘class Urho3D::XMLElement’ has no member named ‘Remove’
         element.Remove();
                 ^~~~~~

-------------------------

johnnycable | 2017-11-20 10:14:43 UTC | #20

Upgrade the master and copy autoload, data and coredata by hand

-------------------------

rku | 2017-11-20 10:22:27 UTC | #21

@slapin you need latest SDK build.

@johnnycable that part is bit wonky. Build system is supposed to symlink them automatically from `${URHO3D_HOME}/bin` but sometimes that requires to run cmake twice. If it is normal SDK install then yeah you would have to copy over resources. In the future editor should work within your project's resource path instead.

-------------------------

johnnycable | 2017-11-20 10:33:53 UTC | #22

I have a urho3d_home/build/bin/autoload etc. installation. Those are symlink already. It's trying to create the symlink of a symlink, which on Os X results in creating an "symlink name copy" symlink in the original directory, and not in your build/bin...

-------------------------

slapin | 2017-11-20 13:09:58 UTC | #23

I don't know where you got that SDK from but the error is from latest github master build.

-------------------------

rku | 2017-11-20 13:11:33 UTC | #24

[quote="slapin, post:19, topic:3718"]
AppendChild
[/quote]

Please verify if you have this method: https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Resource/XMLElement.h#L74

-------------------------

Eugene | 2017-11-20 13:24:50 UTC | #25

I tested build with MSVC 2015 before posting here.

-------------------------

slapin | 2017-11-20 16:18:53 UTC | #26

Linux gcc build doesn't work.
Sorry I did not konw this editor was windows-only.
Sorry for the noise then.

-------------------------

Eugene | 2017-11-20 16:21:11 UTC | #27

Does you Urho include dirrectory contain `XMLElement::Remove`?

-------------------------

slapin | 2017-11-20 16:28:47 UTC | #28

    slapin@slapin-pc:~/Urho3D-Toolbox/build$ grep Remove /home/slapin/Urho3D/build/include/Urho3D/Resource/XMLElement.h
        /// Remove a child element. Return true if successful.
        bool RemoveChild(const XMLElement& element);
        /// Remove a child element by name. Return true if successful.
        bool RemoveChild(const String& name);
        /// Remove a child element by name. Return true if successful.
        bool RemoveChild(const char* name);
        /// Remove child elements of certain name, or all child elements if name is empty. Return true if successful.
        bool RemoveChildren(const String& name = String::EMPTY);
        /// Remove child elements of certain name, or all child elements if name is empty. Return true if successful.
        bool RemoveChildren(const char* name);
        /// Remove an attribute by name. Return true if successful.
        bool RemoveAttribute(const String& name = String::EMPTY);
        /// Remove an attribute by name. Return true if successful.
        bool RemoveAttribute(const char* name);

-------------------------

rku | 2017-11-20 16:30:43 UTC | #29

See, no [XMLElement::Remove](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Resource/XMLElement.h#L76). Update your SDK.

-------------------------

Eugene | 2017-11-20 16:34:12 UTC | #30

So you don't have latest Urho revision or haven't built it.

-------------------------

slapin | 2017-11-20 16:36:09 UTC | #31

Well, I pulled in the morning and build with that. Now I pulled in today's changes so I will check with these.

-------------------------

slapin | 2017-11-20 16:40:18 UTC | #32

    [ 88%] Linking CXX executable ../bin/Editor
    ../ThirdParty/imgui/libimgui.a(imgui_freetype.cpp.o): In function `ImGuiFreeType::BuildFontAtlas(ImFontAtlas*, unsigned int)':
    imgui_freetype.cpp:(.text+0x67b): undefined reference to `FT_Get_Glyph'
    imgui_freetype.cpp:(.text+0x9c1): undefined reference to `FT_Glyph_To_Bitmap'
    imgui_freetype.cpp:(.text+0xb87): undefined reference to `FT_Done_Glyph'
    imgui_freetype.cpp:(.text+0xfc7): undefined reference to `FT_GlyphSlot_Oblique'
    imgui_freetype.cpp:(.text+0xfd4): undefined reference to `FT_GlyphSlot_Embolden'
    collect2: error: ld returned 1 exit status

Well, it looks like for some reason the freetype lib is not picked up. Ideas?

-------------------------

rku | 2017-11-20 16:44:42 UTC | #33

Try using engine as SDK without installing it. That is how i am using it. Just set `URHO3D_HOME` to cmake build dir of engine.

-------------------------

slapin | 2017-11-20 16:47:28 UTC | #34

Always did it like this, like since forever.

-------------------------

rku | 2017-11-20 16:49:18 UTC | #35

Weird. Now that i think of it - not sure why on earth it builds for me with freetype.. Anyhow do this:

1. Remove `imgui_freetype.cpp` from [here](https://github.com/rokups/Urho3D-Toolbox/blob/master/ThirdParty/imgui/CMakeLists.txt#L26)
2. Comment out [this](https://github.com/rokups/Urho3D-Toolbox/blob/master/Toolbox/SystemUI/SystemUI.cpp#L37)
3. Comment out [this](https://github.com/rokups/Urho3D-Toolbox/blob/master/Toolbox/SystemUI/SystemUI.cpp#L331)

-------------------------

slapin | 2017-11-20 17:24:47 UTC | #36

I fixed it like here: https://stackoverflow.com/questions/23888274/linking-freetype-with-cmake

works now.

-------------------------

slapin | 2017-11-20 17:27:04 UTC | #37

Thanks for help!  (20 characters)

-------------------------

vivienneanthony | 2017-12-07 20:00:26 UTC | #38

I'm interested in this. As I have been working with ImGui

-------------------------

