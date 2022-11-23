timob256 | 2022-01-21 15:37:59 UTC | #1

collected Urho3D-1.8-ALPHA (everything is assembled)

decided to collect the simplest example from Urho3D

But for some reason, it writes a file that is not even in the project (protected internal) that there is no header SDL_gamecontroller.h, while it is not there such a file is in SDL2 / SDL_gamecontroller.h BUT I don’t want to fix the internal system files

I can't understand how he (cmake) was able to collect all the examples, but I can't cope (I connected all the libraries), here is a localized error: 



**urno_example1.pro**

    #-------------------------------------------------
    #
    # Project created by QtCreator 2021-12-21T11:52:47
    #
    #-------------------------------------------------
    
    QT       += core gui
    
    greaterThan(QT_MAJOR_VERSION, 4): QT += widgets
    
    TARGET = urno_example1
    TEMPLATE = app
    
    # The following define makes your compiler emit warnings if you use
    # any feature of Qt which has been marked as deprecated (the exact warnings
    # depend on your compiler). Please consult the documentation of the
    # deprecated API in order to know how to port your code away from it.
    DEFINES += QT_DEPRECATED_WARNINGS
    
    # You can also make your code fail to compile if you use deprecated APIs.
    # In order to do so, uncomment the following line.
    # You can also select to disable deprecated APIs only up to a certain version of Qt.
    #DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0
    
    
    SOURCES += \
    #        main.cpp \
    #        mainwindow.cpp
        HelloWorld.cpp \
        Sample.inl
    
    HEADERS += \
    #        mainwindow.h
        HelloWorld.h \
        Sample.h
    
    INCLUDEPATH +=/home/dima/ogre/Urho3D-1.8-ALPHA/Source/ThirdParty/SDL/include \
            /home/dima/ogre/Urho3D-1.8-ALPHA/build/Source/ThirdParty/SDL/include/generated \
            /usr/local/include/Urho3D                                             \
    #    /home/dima/ogre/Urho3D-1.8-ALPHA/build/include/Urho3D                    \
    #    /home/dima/ogre/Urho3D-1.8-ALPHA/build/include/Urho3D/ThirdParty/SDL     \
    #    /usr/include/SDL                                                         \
    #    /usr/include/SDL2
    
    
    unix:!macx: LIBS += -L$$PWD/../../../../usr/local/lib/Urho3D/ -lUrho3D
    
    INCLUDEPATH += $$PWD/../../ogre/Urho3D-1.8-ALPHA/Source/Urho3D
    DEPENDPATH += $$PWD/../../ogre/Urho3D-1.8-ALPHA/Source/Urho3D
    
    unix:!macx: PRE_TARGETDEPS += $$PWD/../../../../usr/local/lib/Urho3D/libUrho3D.a
    
    unix:!macx: LIBS += -L$$PWD/../../ogre/Urho3D-1.8-ALPHA/build/Source/ThirdParty/SDL/ -lSDL
    
    INCLUDEPATH += $$PWD/../../ogre/Urho3D-1.8-ALPHA/Source/ThirdParty/SDL/include
    DEPENDPATH += $$PWD/../../ogre/Urho3D-1.8-ALPHA/Source/ThirdParty/SDL/include
    
    unix:!macx: PRE_TARGETDEPS += $$PWD/../../ogre/Urho3D-1.8-ALPHA/build/Source/ThirdParty/SDL/libSDL.a
    
    
    # --- linux ---
    
    unix:!macx: LIBS += -L$$PWD/../../../../usr/lib/x86_64-linux-gnu/ -lOpenGL
    
    INCLUDEPATH += $$PWD/../../../../usr/include/GL
    DEPENDPATH += $$PWD/../../../../usr/include/GL
    
    unix:!macx: LIBS += -L$$PWD/../../../../usr/lib/x86_64-linux-gnu/ -lGLEW
    
    INCLUDEPATH += $$PWD/../../../../usr/include/GL
    DEPENDPATH += $$PWD/../../../../usr/include/GL
    
    unix:!macx: LIBS += -L$$PWD/../../../../usr/lib/x86_64-linux-gnu/ -lglut
    
    INCLUDEPATH += $$PWD/../../../../usr/include/GL
    DEPENDPATH += $$PWD/../../../../usr/include/GL
    
    unix:!macx: LIBS += -L$$PWD/../../../../usr/lib/x86_64-linux-gnu/ -lGLU
    
    INCLUDEPATH += $$PWD/../../../../usr/include/GL
    DEPENDPATH += $$PWD/../../../../usr/include/GL
    
    
    //
    // Copyright (c) 2008-2019 the Urho3D project.
    //
    // Permission is hereby granted, free of charge, to any person obtaining a copy
    // of this software and associated documentation files (the "Software"), to deal
    // in the Software without restriction, including without limitation the rights
    // to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    // copies of the Software, and to permit persons to whom the Software is
    // furnished to do so, subject to the following conditions:
    //
    // The above copyright notice and this permission notice shall be included in
    // all copies or substantial portions of the Software.
    //
    // THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    // IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    // FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    // AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    // LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    // OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    // THE SOFTWARE.
    //
    
**HelloWorld.h**
    
        #pragma once
        #include "SDL.h"
        #include "Sample.h"
        
        /// This first example, maintaining tradition, prints a "Hello World" message.
        /// Furthermore it shows:
        ///     - Using the Sample / Application classes, which initialize the Urho3D engine and run the main loop
        ///     - Adding a Text element to the graphical user interface
        ///     - Subscribing to and handling of update events
        class HelloWorld : public Sample
        {
            URHO3D_OBJECT(HelloWorld, Sample);
        
        public:
            /// Construct.
            explicit HelloWorld(Context* context);
        
            /// Setup after engine initialization and before running the main loop.
            void Start() override;
        
        protected:
            /// Return XML patch instructions for screen joystick layout for a specific sample app, if any.
            String GetScreenJoystickPatchString() const override { return
                "<patch>"
                "    <add sel=\"/element/element[./attribute[@name='Name' and @value='Hat0']]\">"
                "        <attribute name=\"Is Visible\" value=\"false\" />"
                "    </add>"
                "</patch>";
            }
        
        private:
            /// Construct a new Text instance, containing the 'Hello World' String, and add it to the UI root element.
            void CreateText();
            /// Subscribe to application-wide logic update events.
            void SubscribeToEvents();
            /// Handle the logic update event.
            void HandleUpdate(StringHash eventType, VariantMap& eventData);
        };

    /usr/local/include/Urho3D/Input/InputConstants.h:31: ошибка: SDL/SDL_gamecontroller.h: No such file or directory
     #include <SDL/SDL_gamecontroller.h>
                                        ^
    
    жалуется на /usr/local/include/Urho3D/Input/InputConstants.h 

Как  бы пропустить эту придирку всёравно контролер не буду подключать. 


--------------

[![введите сюда описание изображения][2]][2]




  [2]: https://i.stack.imgur.com/PSF5h.png

-------------------------

timob256 | 2022-01-21 15:37:57 UTC | #2

 [![введите сюда описание изображения][3]][3]


 
  [3]: https://i.stack.imgur.com/rPCD8.png

-------------------------

SirNate0 | 2021-12-21 15:40:34 UTC | #3

You did not set up the include paths correctly in your project I'm pretty sure. I would very much recommend just using CMake for the project, as Qt Creator supports it and then you don't run into these sorts of issues. That said, if you want to continue not using CMake I would recommend using it once for a build, and doing a VERBOSE=1 build with make so it shows the actual commands used to compile the samples, and then you can copy the necessary defines and include paths from that.

-------------------------

timob256 | 2021-12-21 15:55:21 UTC | #4

@SirNate0  but how should **CMake** look like for the simplest example ("hello world") ???

It's just that I'm not a hacker and it's hard for me to work with complex systems (**CMake**)

-------------------------

SirNate0 | 2021-12-21 16:16:28 UTC | #5

Here's the project template I've made, and below I'll go through how to get it set up.

https://github.com/SirNate0/Urho-Project-Template

1. Download the project (either clone or download a zip and extract it somewhere)
2. Delete or rename the build directory. The CMakeCache.txt in it will point to a different path, and it's not worth editing that instead of just starting from scratch.
3. Call the script to generate the new build folder (I'm sticking with "build" as the name) 
    ```./script/cmake_generic.sh build```
4. You should see an error in the output telling you that it couldn't find the Urho3D library.

    ```text
    ...
    CMake Error at CMake/Modules/FindUrho3D.cmake:330 (message):
      Could NOT find compatible Urho3D library in Urho3D SDK installation or
      build tree or in Android library.  Use URHO3D_HOME environment variable or
      build option to specify the location of the non-default SDK installation or
      build tree.
    Call Stack (most recent call first):
      CMake/Modules/UrhoCommon.cmake:244 (find_package)
      CMakeLists.txt:23 (include)
    ```

5. To fix the error, you need to specify where your Urho3D build is (the 1.8-ALPHA you downloaded, in your case). I'm not sure about how the directories are structured for the prebuilt packages, but for me this can be done by changing the call to:
    ```
    URHO3D_HOME=~/Projects/Urho3D/Build ./script/cmake_generic.sh build
    ```
6. If you selected the right directory for the last one, you should get a message like the following at the end of the CMake output:
    ```text
    -- Found Urho3D: /home/nathan/Projects/Urho3D/Build/lib/libUrho3D.a (found version "1.8-ALPHA-486-g93dcb6959")
    -- Configuring done
    -- Generating done
    -- Build files have been written to: /home/nathan/Downloads/tmp/Urho-Project-Template-master/build
    ```
7. Switch to the build directory. `cd build/`
8. Call `make`
    ```text
    Scanning dependencies of target projectExe
    [ 50%] Building CXX object CMakeFiles/projectExe.dir/MultipleViewports.cpp.o
    [100%] Linking CXX executable bin/projectExe
    [100%] Built target projectExe
    ```
9. If that succeeds, you should be able to switch to the build/bin directory (`cd bin`) and run the build executable (`./projectExe`).

10. If you have errors running it, you can try replacing the CoreData and Data directories with the ones from the Urho3D download you have, as sometimes the shaders/scripts change a little and become incompatible. I'm not sure which version this sample was from.

That should hopefully get you started. You can change the ProjectName in the CMakeLists.txt to what you want the project to be called in QtCreator, and you can change projectExe to what you want the executable to be called. Note also that some of the parts of the define_source_files call are unnecessary (there is no Editor directory in my template project, and I believe GLOB_CPP_PATTERNS already includes *.cpp and *.h).

-------------------------

timob256 | 2021-12-22 15:32:44 UTC | #6

`cmake_minimum_required (VERSION 3.10.2)`
changed 
`cmake_minimum_required (VERSION 3.6.2)`

tsanks @SirNate0 

in all work :grinning:

-------------------------

