vivienneanthony | 2017-01-02 01:05:51 UTC | #1

Hello,

I want to add components to the Urho3DPlayer for use in the Editor. THe problem I have in a separate folder I have the components basically in ExistenceClient like GameObject.cpp and Character.cpp.

The cmake is coded to use all files in Tools/Urho3DPlayer which I need to compile the other files at the same time.

The only thing I can think of is adding lines in the cmake file in Tools/Urho3DPlayer to include specifc source in the ExistenceClient folder specifically components.  Or tell Cmake to use the Urho3D library + my components when compiling.

Vivienne

-------------------------

cadaver | 2017-01-02 01:05:52 UTC | #2

There's still the problem of registering your components before running, which I don't think is possible without modifying Urho3DPlayer code. You could go that route, but it's probably easier and more future-proof making a mode in your application which is able to behave like Urho3DPlayer when it's running the editor. For example when there's a command line switch "--editor" or similar.

Ther's nothing "magic" in what Urho3DPlayer does, you'll only need to:
- Register your components 
- Instantiate the Script subsystem
- Load the editor script and run its Start() function
- Run Urho engine loop until exited

-------------------------

vivienneanthony | 2017-01-02 01:05:52 UTC | #3

[quote="cadaver"]There's still the problem of registering your components before running, which I don't think is possible without modifying Urho3DPlayer code. You could go that route, but it's probably easier and more future-proof making a mode in your application which is able to behave like Urho3DPlayer when it's running the editor. For example when there's a command line switch "--editor" or similar.

Ther's nothing "magic" in what Urho3DPlayer does, you'll only need to:
- Register your components 
- Instantiate the Script subsystem
- Load the editor script and run its Start() function
- Run Urho engine loop until exited[/quote]

[code]#
# Copyright (c) 2008-2015 the Urho3D project.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

# Define target name
set (TARGET_NAME Urho3DPlayer)

# Find Urho3D library
find_package (Urho3D REQUIRED)
include_directories (${URHO3D_INCLUDE_DIRS})

# Define source files
define_source_files ()

#ddd more file
FILE(GLOB Character ${CMAKE_SOURCE_DIR}/Source/ExistenceApps/ExistenceClient/Character.cpp)
FILE(GLOB GameObject ${CMAKE_SOURCE_DIR}/Source/ExistenceApps/ExistenceClient/GameObject.cpp)
FILE(GLOB InteractObject ${CMAKE_SOURCE_DIR}/Source/ExistenceApps/ExistenceClient/InteractObject.cpp)

# Setup target with resource copying
setup_main_executable (NOBUNDLE)

# Setup test cases
if (URHO3D_ANGELSCRIPT)
    setup_test (NAME Editor OPTIONS Scripts/Editor.as -w)
    setup_test (NAME NinjaSnowWar OPTIONS Scripts/NinjaSnowWar.as -w)
    setup_test (NAME SpritesAS OPTIONS Scripts/03_Sprites.as -w)
endif ()
if (URHO3D_LUA)
    setup_test (NAME SpritesLua OPTIONS LuaScripts/03_Sprites.lua -w)
endif ()

# Symlink/copy helper shell scripts or batch files to invoke Urho3DPlayer
if (NOT IOS AND NOT ANDROID AND NOT EMSCRIPTEN)
    # Ensure the output directory exist before creating the symlinks
    file (MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
    foreach (FILE Editor NinjaSnowWar)
        create_symlink (${CMAKE_SOURCE_DIR}/bin/${FILE}${SCRIPT_EXT} ${CMAKE_BINARY_DIR}/bin/${FILE}${SCRIPT_EXT} FALLBACK_TO_COPY)
    endforeach ()
endif ()[/code]

-------------------------

vivienneanthony | 2017-01-02 01:05:57 UTC | #4

Hello

Which file to load?

I think I can now build individiual editor without messing with urho3dplayer? Not "Editor.as"

Vivienne

[quote="vivienneanthony"][quote="cadaver"]There's still the problem of registering your components before running, which I don't think is possible without modifying Urho3DPlayer code. You could go that route, but it's probably easier and more future-proof making a mode in your application which is able to behave like Urho3DPlayer when it's running the editor. For example when there's a command line switch "--editor" or similar.

Ther's nothing "magic" in what Urho3DPlayer does, you'll only need to:
- Register your components 
- Instantiate the Script subsystem
- Load the editor script and run its Start() function
- Run Urho engine loop until exited[/quote]

[code]#
# Copyright (c) 2008-2015 the Urho3D project.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

# Define target name
set (TARGET_NAME Urho3DPlayer)

# Find Urho3D library
find_package (Urho3D REQUIRED)
include_directories (${URHO3D_INCLUDE_DIRS})

# Define source files
define_source_files ()

#ddd more file
FILE(GLOB Character ${CMAKE_SOURCE_DIR}/Source/ExistenceApps/ExistenceClient/Character.cpp)
FILE(GLOB GameObject ${CMAKE_SOURCE_DIR}/Source/ExistenceApps/ExistenceClient/GameObject.cpp)
FILE(GLOB InteractObject ${CMAKE_SOURCE_DIR}/Source/ExistenceApps/ExistenceClient/InteractObject.cpp)

# Setup target with resource copying
setup_main_executable (NOBUNDLE)

# Setup test cases
if (URHO3D_ANGELSCRIPT)
    setup_test (NAME Editor OPTIONS Scripts/Editor.as -w)
    setup_test (NAME NinjaSnowWar OPTIONS Scripts/NinjaSnowWar.as -w)
    setup_test (NAME SpritesAS OPTIONS Scripts/03_Sprites.as -w)
endif ()
if (URHO3D_LUA)
    setup_test (NAME SpritesLua OPTIONS LuaScripts/03_Sprites.lua -w)
endif ()

# Symlink/copy helper shell scripts or batch files to invoke Urho3DPlayer
if (NOT IOS AND NOT ANDROID AND NOT EMSCRIPTEN)
    # Ensure the output directory exist before creating the symlinks
    file (MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
    foreach (FILE Editor NinjaSnowWar)
        create_symlink (${CMAKE_SOURCE_DIR}/bin/${FILE}${SCRIPT_EXT} ${CMAKE_BINARY_DIR}/bin/${FILE}${SCRIPT_EXT} FALLBACK_TO_COPY)
    endforeach ()
endif ()[/code][/quote]

-------------------------

vivienneanthony | 2017-01-02 01:05:57 UTC | #5

[quote="cadaver"]There's still the problem of registering your components before running, which I don't think is possible without modifying Urho3DPlayer code. You could go that route, but it's probably easier and more future-proof making a mode in your application which is able to behave like Urho3DPlayer when it's running the editor. For example when there's a command line switch "--editor" or similar.

Ther's nothing "magic" in what Urho3DPlayer does, you'll only need to:
- Register your components 
- Instantiate the Script subsystem
- Load the editor script and run its Start() function
- Run Urho engine loop until exited[/quote]

That's what I did. It seems to not pick up the components and it seems if the scene doesn't fully load the "open scene" does not disappear?

[pastebin.com/v6KTEDsH](http://pastebin.com/v6KTEDsH)

It does compile.

-------------------------

cadaver | 2017-01-02 01:05:57 UTC | #6

Do you need to register attributes for your custom components? Also, maybe include them all in a single editor category (the string parameter for RegisterFactory). However, RegisterFactory should be enough for them to appear in the editor menu.

-------------------------

vivienneanthony | 2017-01-02 01:05:58 UTC | #7

[quote="cadaver"]Do you need to register attributes for your custom components? Also, maybe include them all in a single editor category (the string parameter for RegisterFactory). However, RegisterFactory should be enough for them to appear in the editor menu.[/quote]

Yes. They are set on default in the code.

[github.com/vivienneanthony/Urho ... meObject.h](https://github.com/vivienneanthony/Urho3D-Mastercurrent-Existence/blob/development/Source/ExistenceApps/ExistenceClient/GameObject.h)
[github.com/vivienneanthony/Urho ... Object.cpp](https://github.com/vivienneanthony/Urho3D-Mastercurrent-Existence/blob/development/Source/ExistenceApps/ExistenceClient/GameObject.cpp)

This is one of the codes. I did the register factory line in the post but I am not sure if that's enougth.

E[code]xistenceEditor::ExistenceEditor(Context* context) :
    Board index ? Urho3D User Forum ? Support
    Change font size
    E-mail friend
    Print view

    User Control Panel (0 new messages) ? View your posts

    FAQ
    Members
    Logout [ vivienneanthony ]


    Application(context)
{
    /// Register

    context_ -> RegisterFactory<Character> ("Character");
    context_ -> RegisterFactory<GameObject> ("GameObject");
    context_ -> RegisterFactory<InteractObject> ("InteractObject");
    context_ -> RegisterFactory<ProceduralTerrain> ("PoceduralTerrain");

    cout << "Debig: Existence Client  Existence " << &applicationPtr << endl;

    /// Register states
    cout << "Debug: Existence Client Base Class Constructor context" << &context << " context_"<< &context_ << endl;

    return;
}[/code]


[img]http://i.imgur.com/cCmP2A6.png[/img]

-------------------------

cadaver | 2017-01-02 01:05:58 UTC | #8

Ok, when your classes have attributes and you have defined a ClassName::RegisterObject() function for them, you should rather call that instead of just registering the factory.

-------------------------

