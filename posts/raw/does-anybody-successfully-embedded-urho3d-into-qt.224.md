umen | 2017-01-02 00:59:00 UTC | #1

Hey 
does anybody successfully embedded SDL2 / Urho3D into Qt GUI or any other GUI system ? 
or knows any examples ?

-------------------------

Hevedy | 2018-10-30 11:00:49 UTC | #2

[quote="umen"]
Hey 
does anybody successfully embedded SDL2 / Urho3D into Qt GUI or any other GUI system ? 
or knows any examples ?
[/quote]

I have this [dl.dropboxusercontent.com/u/280 ... DevKit.zip](https://dl.dropboxusercontent.com/u/28070491/Urho3D/UDK_Urho3DevKit.zip) created by ASTER. (changed don't is the original)

-------------------------

umen | 2017-01-02 00:59:00 UTC | #3

Hey who is ASTER?
any way i compile fine BUT im getting linker erros .. allot 
have idea why ? same configurations as the examples in urho3d using the latest sources 

[code]1>     Creating library debug\\UDK.lib and object debug\\UDK.exp
1>Urho3D_d.lib(Timer.obj) : error LNK2019: unresolved external symbol __imp__timeGetTime@0 referenced in function "public: unsigned int __thiscall Urho3D::Timer::GetMSec(bool)" (?GetMSec@Timer@Urho3D@@QAEI_N@Z)
1>Urho3D_d.lib(SDL_systimer.obj) : error LNK2001: unresolved external symbol __imp__timeGetTime@0
1>Urho3D_d.lib(Timer.obj) : error LNK2019: unresolved external symbol __imp__timeBeginPeriod@4 referenced in function "public: void __thiscall Urho3D::Time::SetTimerPeriod(unsigned int)" (?SetTimerPeriod@Time@Urho3D@@QAEXI@Z)
1>Urho3D_d.lib(SDL_systimer.obj) : error LNK2001: unresolved external symbol __imp__timeBeginPeriod@4
1>Urho3D_d.lib(Timer.obj) : error LNK2019: unresolved external symbol __imp__timeEndPeriod@4 referenced in function "public: void __thiscall Urho3D::Time::SetTimerPeriod(unsigned int)" (?SetTimerPeriod@Time@Urho3D@@QAEXI@Z)
1>Urho3D_d.lib(SDL_systimer.obj) : error LNK2001: unresolved external symbol __imp__timeEndPeriod@4
1>Urho3D_d.lib(OGLGraphics.obj) : error LNK2019: unresolved external symbol __imp__glClearDepth@8 referenced in function "public: void __thiscall Urho3D::Graphics::Clear(unsigned int,class Urho3D::Color const &,float,unsigned int)" (?Clear@Graphics@Urho3D@@QAEXIABVColor@2@MI@Z)
1>Urho3D_d.lib(OGLGraphics.obj) : error LNK2019: unresolved external symbol __imp__glClipPlane@8 referenced in function "public: void __thiscall Urho3D::Graphics::SetClipPlane(bool,class Urho3D::Plane const &,class Urho3D::Matrix3x4 const &,class Urho3D::Matrix4 const &)" (?SetClipPlane@Graphics@Urho3D@@QAEX_NABVPlane@2@ABVMatrix3x4@2@ABVMatrix4@2@@Z)
1>Urho3D_d.lib(OGLGraphics.obj) : error LNK2019: unresolved external symbol __imp__glDrawBuffer@4 referenced in function "private: void __thiscall Urho3D::Graphics::CommitFramebuffer(void)" (?CommitFramebuffer@Graphics@Urho3D@@AAEXXZ)
1>Urho3D_d.lib(OGLGraphics.obj) : error LNK2019: unresolved external symbol __imp__glPolygonMode@8 referenced in function "public: void __thiscall Urho3D::Graphics::SetFillMode(enum Urho3D::FillMode)" (?SetFillMode@Graphics@Urho3D@@QAEXW4FillMode@2@@Z)
1>Urho3D_d.lib(OGLGraphics.obj) : error LNK2019: unresolved external symbol __imp__glReadBuffer@4 referenced in function "private: void __thiscall Urho3D::Graphics::CommitFramebuffer(void)" (?CommitFramebuffer@Graphics@Urho3D@@AAEXXZ)
1>Urho3D_d.lib(glew.obj) : error LNK2019: unresolved external symbol __imp__wglGetCurrentDC@0 referenced in function _wglewGetExtension@4
1>Urho3D_d.lib(glew.obj) : error LNK2019: unresolved external symbol __imp__wglGetProcAddress@4 referenced in function __glewInit_GL_VERSION_1_2
1>Urho3D_d.lib(OGLTexture2D.obj) : error LNK2019: unresolved external symbol __imp__glGetTexImage@20 referenced in function "public: bool __thiscall Urho3D::Texture2D::GetData(unsigned int,void *)const " (?GetData@Texture2D@Urho3D@@QBE_NIPAX@Z)
1>Urho3D_d.lib(OGLTexture3D.obj) : error LNK2001: unresolved external symbol __imp__glGetTexImage@20
1>Urho3D_d.lib(OGLTextureCube.obj) : error LNK2001: unresolved external symbol __imp__glGetTexImage@20
1>Urho3D_d.lib(SDL_windowskeyboard.obj) : error LNK2019: unresolved external symbol _GetFileVersionInfoSizeA@8 referenced in function _IME_GetId
1>Urho3D_d.lib(SDL_windowskeyboard.obj) : error LNK2019: unresolved external symbol _GetFileVersionInfoA@16 referenced in function _IME_GetId
1>Urho3D_d.lib(SDL_windowskeyboard.obj) : error LNK2019: unresolved external symbol _VerQueryValueA@16 referenced in function _IME_GetId
1>Urho3D_d.lib(SDL_windowskeyboard.obj) : error LNK2019: unresolved external symbol _ImmGetIMEFileNameA@12 referenced in function _IME_SetupAPI
1>Urho3D_d.lib(SDL_windowskeyboard.obj) : error LNK2019: unresolved external symbol _ImmGetContext@4 referenced in function _IME_HandleMessage
1>Urho3D_d.lib(SDL_windowskeyboard.obj) : error LNK2019: unresolved external symbol _ImmReleaseContext@8 referenced in function _IME_HandleMessage
1>Urho3D_d.lib(SDL_windowskeyboard.obj) : error LNK2019: unresolved external symbol _ImmAssociateContext@8 referenced in function _IME_HandleMessage
1>Urho3D_d.lib(SDL_windowskeyboard.obj) : error LNK2019: unresolved external symbol _ImmGetCompositionStringW@16 referenced in function _IME_GetCompositionString
1>Urho3D_d.lib(SDL_windowskeyboard.obj) : error LNK2019: unresolved external symbol _ImmSetCompositionStringW@24 referenced in function _IME_ClearComposition
1>Urho3D_d.lib(SDL_windowskeyboard.obj) : error LNK2019: unresolved external symbol _ImmGetCandidateListW@16 referenced in function _IME_GetCandidateList
1>Urho3D_d.lib(SDL_windowskeyboard.obj) : error LNK2019: unresolved external symbol _ImmNotifyIME@16 referenced in function _IME_ClearComposition
1>debug\\UDK.exe : fatal error LNK1120: 22 unresolved externals[/code]

-------------------------

thebluefish | 2017-01-02 00:59:00 UTC | #4

You'll need the to add the following Additional Dependencies (Project Properties -> Linker -> Input -> Additional Dependencies):
[code]winmm.lib
opengl32.lib
imm32.lib[/code]

Possibly others as well.

-------------------------

rasteron | 2017-01-02 00:59:00 UTC | #5

The engine's built-in UI seems fine but it would be interesting to see this in action just like QtOgre or other implementation..

-------------------------

thebluefish | 2017-01-02 00:59:00 UTC | #6

Urho3D works with an external window handle no problem. The first version of my map editor utilized QT and worked pretty well, but I hated the extra build steps. Currently my external editor is done through wxWidgets and works no problem.

You can view my wxWidgets code here: [github.com/thebluefish/Urho3D-M ... r/wxUrho3D](https://github.com/thebluefish/Urho3D-Misc/tree/master/wxUrho3D)

As you can see the integration code is very minimal. Qt is actually not that much different, though I remember a few things took a little playing around with to get right. It took me maybe a day or two to get it running in QT relatively well. As long as you can find a barebone template for defining a widget/control/etc... in QT, making an Urho3D widget/control/etc... shouldn't prove to be difficult.

-------------------------

umen | 2017-01-02 00:59:00 UTC | #7

does it worked well on mac and and linux as in windows ?

-------------------------

umen | 2017-01-02 00:59:01 UTC | #8

wow and in mac its even worst 
compilation said :
file compile in x86_64 
[code]lipo -info ./Lib/libUrho3D.a
input file ./Lib/libUrho3D.a is not a fat file
Non-fat file: ./Lib/libUrho3D.a is architecture: x86_64[/code]

and when trying to compile the Qt latest 5.2.1 with the Urho3d latest I'm getting  sorry of the long output :

the error is said :
[code]Undefined symbols for architecture x86_64:[/code]
[code]
 .....
....
....
AGL.framework/Headers -I. -I. -F/Users/meiryanovich/Qt5.2.1/5.2.1/clang_64/lib -o moc_urho3dqtmainwindow.o moc_urho3dqtmainwindow.cpp
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ -headerpad_max_install_names -Wl,-syslibroot,/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.8.sdk -mmacosx-version-min=10.6 -o Qt3d.app/Contents/MacOS/Qt3d main.o mainwindow.o urho3dqtapplication.o urho3dqtcentralwidget.o urho3dqtmainwindow.o moc_mainwindow.o moc_urho3dqtapplication.o moc_urho3dqtcentralwidget.o moc_urho3dqtmainwindow.o   -F/Users/meiryanovich/Qt5.2.1/5.2.1/clang_64/lib -L/Users/meiryanovich/Documents/3d/urho3d/QtTest2/Qt3d/../../git/Urho3D_macos/Lib/ -lUrho3D -L/Users/meiryanovich/Documents/3d/urho3d/QtTest2/Qt3d/../../git/Urho3D_macos/Build/ThirdParty/SDL/Debug/ -lSDL -framework QtWidgets -framework QtGui -framework QtCore -framework OpenGL -framework AGL 
Undefined symbols for architecture x86_64:
  "_AudioObjectGetPropertyData", referenced from:
      _build_device_list in libUrho3D.a(SDL_coreaudio.o)
      _find_device_by_name in libUrho3D.a(SDL_coreaudio.o)
  "_AudioObjectGetPropertyDataSize", referenced from:
      _build_device_list in libUrho3D.a(SDL_coreaudio.o)
  "_AudioOutputUnitStart", referenced from:
      _prepare_audiounit in libUrho3D.a(SDL_coreaudio.o)
  "_AudioOutputUnitStop", referenced from:
      _COREAUDIO_CloseDevice in libUrho3D.a(SDL_coreaudio.o)
  "_AudioUnitInitialize", referenced from:
      _prepare_audiounit in libUrho3D.a(SDL_coreaudio.o)
  "_AudioUnitSetProperty", referenced from:
      _COREAUDIO_CloseDevice in libUrho3D.a(SDL_coreaudio.o)
      _prepare_audiounit in libUrho3D.a(SDL_coreaudio.o)
  "_CFArrayApplyFunction", referenced from:
      _AddHIDElements in libUrho3D.a(SDL_sysjoystick.o)
  "_CFArrayCreate", referenced from:
      -[MacFileWatcher initWithPathName:recursive:] in libUrho3D.a(MacFileWatcher.o)
      _CreateHIDManager in libUrho3D.a(SDL_sysjoystick.o)
  "_CFArrayGetCount", referenced from:
      _AddHIDElements in libUrho3D.a(SDL_sysjoystick.o)
      _Cocoa_GetDisplayModes in libUrho3D.a(SDL_cocoamodes.o)
  "_CFArrayGetValueAtIndex", referenced from:
      _Cocoa_GetDisplayModes in libUrho3D.a(SDL_cocoamodes.o)
  "_CFDataGetBytePtr", referenced from:
      _UpdateKeymap in libUrho3D.a(SDL_cocoakeyboard.o)
  "_CFDictionaryCreate", referenced from:
      _CreateHIDDeviceMatchDictionary in libUrho3D.a(SDL_sysjoystick.o)
  "_CFDictionaryGetValue", referenced from:
      _MacHaptic_MaybeAddDevice in libUrho3D.a(SDL_syshaptic.o)
      _HIDGetDeviceProduct in libUrho3D.a(SDL_syshaptic.o)
  "_CFGetTypeID", referenced from:
      _AddHIDElement in libUrho3D.a(SDL_sysjoystick.o)
  "_CFNumberCreate", referenced from:
      _CreateHIDDeviceMatchDictionary in libUrho3D.a(SDL_sysjoystick.o)
  "_CFNumberGetValue", referenced from:
      _GetDeviceInfo in libUrho3D.a(SDL_sysjoystick.o)
      _MacHaptic_MaybeAddDevice in libUrho3D.a(SDL_syshaptic.o)
  "_CFRelease", referenced from:
      -[MacFileWatcher initWithPathName:recursive:] in libUrho3D.a(MacFileWatcher.o)
      _CreateHIDManager in libUrho3D.a(SDL_sysjoystick.o)
      _SDL_SYS_JoystickQuit in libUrho3D.a(SDL_sysjoystick.o)
      _CreateHIDDeviceMatchDictionary in libUrho3D.a(SDL_sysjoystick.o)
      _GetDeviceInfo in libUrho3D.a(SDL_sysjoystick.o)
      _build_device_list in libUrho3D.a(SDL_coreaudio.o)
      _GetDisplayMode in libUrho3D.a(SDL_cocoamodes.o)
      ...
  "_CFRunLoopGetCurrent", referenced from:
      _ConfigHIDManager in libUrho3D.a(SDL_sysjoystick.o)
      _JoystickDeviceWasAddedCallback in libUrho3D.a(SDL_sysjoystick.o)
  "_CFRunLoopGetMain", referenced from:
      -[MacFileWatcher initWithPathName:recursive:] in libUrho3D.a(MacFileWatcher.o)
  "_CFRunLoopRunInMode", referenced from:
      _ConfigHIDManager in libUrho3D.a(SDL_sysjoystick.o)
  "_CFStringCompare", referenced from:
      _GetDisplayMode in libUrho3D.a(SDL_cocoamodes.o)
  "_CFStringGetCString", referenced from:
      _GetDeviceInfo in libUrho3D.a(SDL_sysjoystick.o)
      _build_device_list in libUrho3D.a(SDL_coreaudio.o)
      _HIDGetDeviceProduct in libUrho3D.a(SDL_syshaptic.o)
  "_CFStringGetLength", referenced from:
      _build_device_list in libUrho3D.a(SDL_coreaudio.o)
  "_CFStringGetMaximumSizeForEncoding", referenced from:
      _build_device_list in libUrho3D.a(SDL_coreaudio.o)
  "_CFStringGetSystemEncoding", referenced from:
      _HIDGetDeviceProduct in libUrho3D.a(SDL_syshaptic.o)
  "_CFUUIDGetConstantUUIDWithBytes", referenced from:
      _SDL_SYS_HapticEffectType in libUrho3D.a(SDL_syshaptic.o)
  "_CGAcquireDisplayFadeReservation", referenced from:
      _Cocoa_SetDisplayMode in libUrho3D.a(SDL_cocoamodes.o)
  "_CGAssociateMouseAndMouseCursorPosition", referenced from:
      _Cocoa_SetRelativeMouseMode in libUrho3D.a(SDL_cocoamouse.o)
  "_CGCaptureAllDisplays", referenced from:
      _Cocoa_SetDisplayMode in libUrho3D.a(SDL_cocoamodes.o)
  "_CGDisplayBounds", referenced from:
      _Cocoa_GetDisplayBounds in libUrho3D.a(SDL_cocoamodes.o)
  "_CGDisplayCapture", referenced from:
      _Cocoa_SetDisplayMode in libUrho3D.a(SDL_cocoamodes.o)
  "_CGDisplayCopyAllDisplayModes", referenced from:
      _Cocoa_GetDisplayModes in libUrho3D.a(SDL_cocoamodes.o)
  "_CGDisplayCopyDisplayMode", referenced from:
      _Cocoa_InitModes in libUrho3D.a(SDL_cocoamodes.o)
  "_CGDisplayFade", referenced from:
      _Cocoa_SetDisplayMode in libUrho3D.a(SDL_cocoamodes.o)
  "_CGDisplayIDToOpenGLDisplayMask", referenced from:
      _Cocoa_GL_CreateContext in libUrho3D.a(SDL_cocoaopengl.o)
  "_CGDisplayIOServicePort", referenced from:
      _Cocoa_GetDisplayName in libUrho3D.a(SDL_cocoamodes.o)
  "_CGDisplayIsMain", referenced from:
      _Cocoa_InitModes in libUrho3D.a(SDL_cocoamodes.o)
      _Cocoa_SetDisplayMode in libUrho3D.a(SDL_cocoamodes.o)
  "_CGDisplayMirrorsDisplay", referenced from:
      _Cocoa_InitModes in libUrho3D.a(SDL_cocoamodes.o)
  "_CGDisplayModeCopyPixelEncoding", referenced from:
      _GetDisplayMode in libUrho3D.a(SDL_cocoamodes.o)
  "_CGDisplayModeGetHeight", referenced from:
      _GetDisplayMode in libUrho3D.a(SDL_cocoamodes.o)
  "_CGDisplayModeGetRefreshRate", referenced from:
      _GetDisplayMode in libUrho3D.a(SDL_cocoamodes.o)
  "_CGDisplayModeGetWidth", referenced from:
      _GetDisplayMode in libUrho3D.a(SDL_cocoamodes.o)
  "_CGDisplayModeRelease", referenced from:
      _Cocoa_ReleaseDisplayMode in libUrho3D.a(SDL_cocoamodes.o)
  "_CGDisplayModeRetain", referenced from:
      _Cocoa_GetDisplayModes in libUrho3D.a(SDL_cocoamodes.o)
  "_CGDisplayMoveCursorToPoint", referenced from:
      -[Cocoa_WindowListener mouseMoved:] in libUrho3D.a(SDL_cocoawindow.o)
      _Cocoa_SetWindowGrab in libUrho3D.a(SDL_cocoawindow.o)
  "_CGDisplayPixelsHigh", referenced from:
      _ConvertNSRect in libUrho3D.a(SDL_cocoawindow.o)
      _Cocoa_HandleMouseEvent in libUrho3D.a(SDL_cocoamouse.o)
  "_CGDisplayRelease", referenced from:
      _Cocoa_SetDisplayMode in libUrho3D.a(SDL_cocoamodes.o)
  "_CGDisplaySetDisplayMode", referenced from:
      _Cocoa_SwitchMode in libUrho3D.a(SDL_cocoamodes.o)
  "_CGGetDisplayTransferByTable", referenced from:
      _Cocoa_GetWindowGammaRamp in libUrho3D.a(SDL_cocoawindow.o)
  "_CGGetOnlineDisplayList", referenced from:
      _Cocoa_InitModes in libUrho3D.a(SDL_cocoamodes.o)
  "_CGMainDisplayID", referenced from:
      _ConvertNSRect in libUrho3D.a(SDL_cocoawindow.o)
      -[Cocoa_WindowListener mouseMoved:] in libUrho3D.a(SDL_cocoawindow.o)
      _Cocoa_SetWindowGrab in libUrho3D.a(SDL_cocoawindow.o)
      _Cocoa_HandleMouseEvent in libUrho3D.a(SDL_cocoamouse.o)
  "_CGReleaseAllDisplays", referenced from:
      _Cocoa_SetDisplayMode in libUrho3D.a(SDL_cocoamodes.o)
  "_CGReleaseDisplayFadeReservation", referenced from:
      _Cocoa_SetDisplayMode in libUrho3D.a(SDL_cocoamodes.o)
  "_CGSetDisplayTransferByTable", referenced from:
      _Cocoa_SetWindowGammaRamp in libUrho3D.a(SDL_cocoawindow.o)
  "_CGSetLocalEventsSuppressionInterval", referenced from:
      -[Cocoa_WindowListener mouseMoved:] in libUrho3D.a(SDL_cocoawindow.o)
      _Cocoa_WarpMouse in libUrho3D.a(SDL_cocoamouse.o)
  "_CGShieldingWindowLevel", referenced from:
      _Cocoa_SetWindowFullscreen in libUrho3D.a(SDL_cocoawindow.o)
      _Cocoa_SetWindowGrab in libUrho3D.a(SDL_cocoawindow.o)
  "_CGWarpMouseCursorPosition", referenced from:
      _Cocoa_WarpMouse in libUrho3D.a(SDL_cocoamouse.o)
  "_CGWindowLevelForKey", referenced from:
      -[Cocoa_WindowListener windowDidExitFullScreen:] in libUrho3D.a(SDL_cocoawindow.o)
      _Cocoa_SetWindowFullscreen in libUrho3D.a(SDL_cocoawindow.o)
      _Cocoa_SetWindowGrab in libUrho3D.a(SDL_cocoawindow.o)
  "_CloseComponent", referenced from:
...
...
..


[/code]

-------------------------

aster2013 | 2017-01-02 00:59:01 UTC | #9

I think you'd better use qt4 than qt5. Qt4 is smaller and easy to configuration with cmake.

-------------------------

umen | 2017-01-02 00:59:01 UTC | #10

qt 5 is just fine also i don't need to configure it with cmake .
i compile the urho3d 
then i link it with Qt , but somehow it complain about architecture conflict Although they both compiled the same

-------------------------

aster2013 | 2017-01-02 00:59:06 UTC | #11

It is write in Qt

[img]https://dl.dropboxusercontent.com/u/56770481/QQ%E5%9B%BE%E7%89%8720140509133154.jpg[/img]

-------------------------

umen | 2017-01-02 00:59:06 UTC | #12

did you did it ?
how did you mange with to work with the Qt and SDL event loops in the same time ?

-------------------------

aster2013 | 2018-10-30 11:00:10 UTC | #13

I use a Qt timer to drive engine's frame, and not use Qt's event.

[code]
    QTimer timer;
    connect(&timer, SIGNAL(timeout()), this, SLOT(OnTimeout()));
    timer.start(30);

void Urho3DEditor::OnTimeout()
{
    if (engine_ && !engine_->IsExiting())
        engine_->RunFrame();
}
[/code]

-------------------------

umen | 2017-01-02 00:59:07 UTC | #14

Hey thanks , 
does it work without a problem ? 
any chance to test your app ? 
is it open source ?

-------------------------

aster2013 | 2017-01-02 00:59:07 UTC | #15

It is not open source now. I just write it on my local repo.

-------------------------

delrios | 2017-04-14 12:38:13 UTC | #16

Hey @thebluefish, could you send me or upload to git your wxUrho3D code again? Thank you in advance.

-------------------------

