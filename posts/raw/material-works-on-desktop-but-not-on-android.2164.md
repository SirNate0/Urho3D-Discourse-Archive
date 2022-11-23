rku | 2017-01-02 01:13:35 UTC | #1

I have a model to which i set a color like so:

[code]    auto technique = cache.GetResource<Technique>("Techniques/NoTexture.xml");
    auto material = new Material(context_);
    material->SetTechnique(0, technique);
    material->SetShaderParameter("MatDiffColor", color);
    model->SetMaterial(material);[/code]

But on android model is not visible at all. From the look at LitSolid.glsl i cant tell why this would be. I am possibly looking in the wrong place. Any idea why this would be happening and where i could look for potential rendering differences between desktop and android?

-------------------------

cadaver | 2017-01-02 01:13:35 UTC | #2

If you use adb logcat, do you see a shader compile error in the log output?

-------------------------

rku | 2017-01-02 01:13:36 UTC | #3

No errors. Tested galaxy s2 and galaxy s5. Could inspect logcat only on s2, but both phones dont show any color and meshes are invisible. Here is entire log:

[code]V/SDL     ( 5301): Device: GT-I9100
V/SDL     ( 5301): Model: GT-I9100
V/SDL     ( 5301): onCreate(): null
W/linker  ( 5301): libBlocktastic_Debug.so: unused DT entry: type 0x6ffffffe arg 0x2b0854
W/linker  ( 5301): libBlocktastic_Debug.so: unused DT entry: type 0x6fffffff arg 0x3
V/SDL     ( 5301): onResume()
D/OpenGLRenderer( 5301): Use EGL_SWAP_BEHAVIOR_PRESERVED: false
D/Atlas   ( 5301): Validating map...
V/WindowManager( 2228): Adding window Window{190d56cb u0 com.rokups.rs/com.rokups.rs.Blocktastic} at 3 of 9 (before Window{36a20d90 u0 Starting com.rokups.rs})
D/libEGL  ( 5301): loaded /system/lib/egl/libEGL_mali.so
D/libEGL  ( 5301): loaded /system/lib/egl/libGLESv1_CM_mali.so
D/libEGL  ( 5301): loaded /system/lib/egl/libGLESv2_mali.so
E/        ( 5301): Device driver API match
E/        ( 5301): Device driver API version: 23
E/        ( 5301): User space API version: 23 
E/        ( 5301): mali: REVISION=Linux-r3p2-01rel3 BUILD_DATE=Wed Oct  9 21:05:57 KST 2013 
I/OpenGLRenderer( 5301): Initialized EGL, version 1.4
D/OpenGLRenderer( 5301): Enabling debug mode 0
V/WindowManager( 2228): Adding window Window{2300cdc1 u0 SurfaceView} at 3 of 10 (before Window{190d56cb u0 com.rokups.rs/com.rokups.rs.Blocktastic})
V/SDL     ( 5301): surfaceCreated()
V/SDL     ( 5301): surfaceChanged()
V/SDL     ( 5301): pixel format RGB_565
V/SDL     ( 5301): Window size: 480x800
I/ActivityManager( 2228): Displayed com.rokups.rs/.Blocktastic: +487ms
V/SDL     ( 5301): onWindowFocusChanged(): true
I/SDL     ( 5301): SDL_Android_Init()
I/SDL     ( 5301): SDL_Android_Init() finished!
I/Timeline( 2228): Timeline: Activity_windows_visible id: ActivityRecord{1837e324 u0 com.rokups.rs/.Blocktastic t631} time:1324198
I/Timeline( 5301): Timeline: Activity_idle id: android.os.BinderProxy@129f3ca4 time:1324202
I/Urho3D  ( 5301): Created 1 worker thread
I/Urho3D  ( 5301): Added resource path /apk/CoreData/
I/Urho3D  ( 5301): Added resource path /apk/Data/
I/Urho3D  ( 5301): Added resource path /apk/GameData/
I/Urho3D  ( 5301): Set screen mode 480x800 windowed
I/Urho3D  ( 5301): Initialized input
I/Urho3D  ( 5301): Initialized user interface
D/Urho3D  ( 5301): Loading resource Textures/Ramp.png
D/Urho3D  ( 5301): Loading temporary resource Textures/Ramp.xml
D/Urho3D  ( 5301): Loading resource Textures/Spot.png
D/Urho3D  ( 5301): Loading temporary resource Textures/Spot.xml
D/Urho3D  ( 5301): Loading resource Techniques/NoTexture.xml
D/Urho3D  ( 5301): Loading resource RenderPaths/Forward.xml
I/Urho3D  ( 5301): Initialized renderer
V/SDL     ( 5301): SDL audio: opening device
V/SDL     ( 5301): SDL audio: wanted stereo 16-bit 44.1kHz, 4096 frames buffer
E/AudioTrack( 5301): AudioTrack::set : Exit
V/SDL     ( 5301): SDL audio: got stereo 16-bit 44.1kHz, 4096 frames buffer
I/Urho3D  ( 5301): Set audio mode 44100 Hz stereo interpolated
I/Urho3D  ( 5301): Initialized engine
D/Urho3D  ( 5301): Loading resource UI/DefaultStyle.xml
D/Urho3D  ( 5301): Loading resource Fonts/Anonymous Pro.ttf
D/Urho3D  ( 5301): Font face Anonymous Pro (11pt) has 624 glyphs
D/Urho3D  ( 5301): Loading resource Textures/UI.png
D/Urho3D  ( 5301): Loading temporary resource Textures/UI.xml
D/Urho3D  ( 5301): MenuState::Start
D/Urho3D  ( 5301): Loading resource UI/MainMenu.xml
D/Urho3D  ( 5301): Font face Anonymous Pro (14pt) has 624 glyphs
D/Urho3D  ( 5301): Reloading shaders
D/Urho3D  ( 5301): Loading resource Shaders/GLSL/Basic.glsl
D/Urho3D  ( 5301): Compiled vertex shader Basic(DIFFMAP VERTEXCOLOR)
D/Urho3D  ( 5301): Compiled pixel shader Basic(DIFFMAP VERTEXCOLOR)
D/Urho3D  ( 5301): Linked vertex shader Basic(DIFFMAP VERTEXCOLOR) and pixel shader Basic(DIFFMAP VERTEXCOLOR)
D/Urho3D  ( 5301): Compiled pixel shader Basic(ALPHAMAP VERTEXCOLOR)
D/Urho3D  ( 5301): Linked vertex shader Basic(DIFFMAP VERTEXCOLOR) and pixel shader Basic(ALPHAMAP VERTEXCOLOR)
D/Urho3D  ( 5301): MenuState::Suspend
D/Urho3D  ( 5301): GameState::Start
D/Urho3D  ( 5301): Loading resource UI/Hud.xml
D/Urho3D  ( 5301): Loading resource Models/Box.mdl
D/Urho3D  ( 5301): Compiled vertex shader Basic(VERTEXCOLOR)
D/Urho3D  ( 5301): Compiled pixel shader Basic(VERTEXCOLOR)
D/Urho3D  ( 5301): Linked vertex shader Basic(VERTEXCOLOR) and pixel shader Basic(VERTEXCOLOR)
D/TaskPersister( 2228): removeObsoleteFile: deleting file=630_task.xml
D/TaskPersister( 2228): removeObsoleteFile: deleting file=630_task_thumbnail.png
D/Urho3D  ( 5301): Loading resource Shaders/GLSL/LitSolid.glsl
W/Urho3D  ( 5301): Shader LitSolid(NOUV) does not use the define NOUV
D/Urho3D  ( 5301): Compiled vertex shader LitSolid(NOUV)
D/Urho3D  ( 5301): Compiled pixel shader LitSolid()
D/Urho3D  ( 5301): Linked vertex shader LitSolid(NOUV) and pixel shader LitSolid()[/code]

-------------------------

