rdpeake | 2017-01-02 01:14:01 UTC | #1

Hey All,

This will probably be a long one, but bare with me.

I have an existing Xamarin app, which uses a floating opengl surface to move our 3d scene in front of, and behind, other xamarin components. I have, via urhosharp (search xamarin/urho on github) created an android and iOS surface within the app which can be freely moved between layers. The issue is that the background of that layer does not clear transparent like the old engine could. Whilst could be possible that this is an UrhoSharp problem, and i will be asking there as well, i tried to achieve a test project using urho3d source.

In order to test if SDL allows for transparent clear colours, on windows, i started with the hello world sample and attempted to render a transparent clear colour - by setting the fog colour. As the Zone component always makes the fog colour opaque i modified the 'setfogcolor' method to be full alpha. what i hoped to achieve when running this, was to see the windows form (white, by default i believe) show through and my clear colour to not be there at all. Instead, i see a full opaque version of my clear colour.

Now, the question is, Is this a limitation of Windows -> though i have seen many other GL apps which can render transparent clear, SDL, or Urho3D, or am i doing something wrong? I'd like to point out, part of the graphics initialisation is to clear transparent black, which also shows up as opaque black. Also, if this is a windows problem, what would i need to do to get this to work on Androidn/iOS targets?

Thanks for any help.

-------------------------

Sir_Nate | 2017-01-02 01:14:03 UTC | #2

It's a limitation of SDL (for now). It's possible this is what you're looking for, but it's only available in the unstable versions of SDL 2.0.4.

You can try to set up your window using one of these, but I've not tried it with Urho, there may be some configuration needed to get it to support a transparent window. Though I think a transparent fog color will not work (I think it just ignores alpha), but I don't know what you've changed, so perhaps it will work.

[url]http://stackoverflow.com/questions/4052940/how-to-make-an-opengl-rendering-context-with-transparent-background[/url] <- windows and linux
[url]http://stackoverflow.com/questions/9363491/how-to-make-transparent-window-on-linux[/url] <- linux

-------------------------

rdpeake | 2017-01-02 01:14:03 UTC | #3

Thanks For your reply.

The fog colour by default sets the alpha channel to 1, regardless of what you try to set it at.

Do you have any examples or such for allowing the openGL surface being transparent (alpha enabled) and transparent to views behind on android/iOS. Android seems to set the surface view format to 535 colour, not sure what the iOS surface is being set to, but neither allow manual clear colour with the alpha channel below max.

-------------------------

Sir_Nate | 2017-01-02 01:14:04 UTC | #4

You can try adapting [url]http://stackoverflow.com/questions/2034822/android-opengl-es-transparent-background[/url] or [url]http://stackoverflow.com/questions/16762633/android-glsurfaceview-transparent-background-without-setzorderontop[/url] for Android, but I haven't really looked into the Urho Android window creation code so I can't say if that might help. I have no idea for iOS, though -- if you want to show the home-screen on iOS it might not even be possible (but for the moment I only develop for Android (and that only secondarily to the Desktop, mostly just to make sure I won't have to change too much for my game to get it to work)).

-------------------------

rdpeake | 2017-01-02 01:14:04 UTC | #5

I'm not trying to show the homescreen through the window. I'm trying to show other, non openGL views from my own app though the surface.

-------------------------

Sir_Nate | 2017-01-02 01:14:06 UTC | #6

This may be a starting point for iOS then, but I even less of an idea about Urho's iOS stuff, so...
[url]http://stackoverflow.com/questions/15425149/making-uiview-transparent[/url]

-------------------------

rdpeake | 2017-01-02 01:14:06 UTC | #7

Hey, The problem with what you have posted so far is that my GLSurface does not allow for a transparent clear colour.

If i manually call the following
[code]Graphics.BeginFrame();Graphics.Clear(1, new Color(Color.Green, 0.0f), 1.0f, 0);Graphics.EndFrame();[/code]

I still end up with an opaque green display - i should expect the screen to be black, or white, depending on what the default background colour for an app should be.

Do i need to do something in order to achieve this?

-------------------------

Sir_Nate | 2020-06-30 06:27:37 UTC | #8

I don't really know how to fix it. I did get a transparent window working on Desktop (Linux), passing it a native window from that Stack Overflow question's code, but I don't know how you could fix it for mobile. You can see if this helps, but I don't even know how you would go about creating another surface in mobile, so I can't really help with that.


UrhoApp.hpp
[code]
#ifndef URHOAPP_HPP
#define URHOAPP_HPP

//#include <Urho3D.h>
//#include <Engine/Application.h>
#include "/usr/local/include/Urho3D/Urho3D.h"
#include "/usr/local/include/Urho3D/Engine/Application.h"


#include <Core/Object.h>
#include <Container/Str.h>
#include <Scene/Scene.h>
#include <Container/Ptr.h>
#include <Container/RefCounted.h>
#include <Scene/Node.h>
#include <UI/UIElement.h>
#include <Core/CoreEvents.h>
#include <Graphics/Viewport.h>

using namespace Urho3D;

class UrhoApp: public Urho3D::Application
{
public:
    OBJECT(UrhoApp,Application)
    UrhoApp(Context* context, void* window);

    void Start();
    void Setup();

    int MyInit();
    void UrhoFrame();
    void MyStop();

    void Update(StringHash eventType, VariantMap& eventData);

private:
    void* window_;
    SharedPtr<Scene> scene_;//a pointer to the scene -- it can be another state's scene, or a different one entirely
    Node* localRootNode;//a node for all of the state-local objects to be children of
    UIElement* localRootUIElement;//a UI Element for adding all of the state local UI stuff (since UI is a subsystem, unlike scene)
    SharedPtr<Node> cameraNode_;
    SharedPtr<Viewport> viewport_;
    bool active;
    bool isFocus;
};

//URHO3D_DEFINE_APPLICATION_MAIN(UrhoApp)
UrhoApp* RunApplication(void* window);

#endif // URHOAPP_HPP
[/code]

UrhoApp.cpp
[code]
#include <Urho3D.h>
#include "UrhoApp.hpp"
#include <Graphics/Graphics.h>
#include <IO/File.h>
#include <Resource/XMLFile.h>
#include <Engine/Engine.h>
#include <Input/Input.h>
#include <IO/Log.h>
#include <Core/Variant.h>
#include <Core/Context.h>
#include <Scene/Scene.h>
#include <Graphics/Octree.h>
#include <Graphics/Camera.h>
#include <Graphics/Zone.h>
#include <Resource/ResourceCache.h>
#include <Graphics/Renderer.h>
#include <UI/Text.h>
#include <UI/UIElement.h>
#include <UI/UI.h>
#include <UI/Font.h>
#include <Container/Str.h>
#include <UI/Menu.h>
#include <Audio/Audio.h>
#include <Graphics/RenderPath.h>
#include <Graphics/Model.h>
#include <Graphics/StaticModel.h>
#include <Graphics/DebugRenderer.h>
#include <Graphics/GraphicsEvents.h>

using namespace Urho3D;

UrhoApp::UrhoApp(Context *context, void *window): Urho3D::Application(context), window_(window)
{

}

void UrhoApp::Start()
{
    Scene* scene_ = new Scene(context_);
        scene_->CreateComponent<Octree>();

        //enable touch on android
    //    if (GetPlatform() == "Android" || GetPlatform() == "iOS")
    //        // On mobile platform, enable touch by adding a screen joystick
    //        InitTouchInput();
    //    else if (GetSubsystem<Input>()->GetNumJoysticks() == 0)
    //        // On desktop platform, do not detect touch when we already got a joystick
    //        SubscribeToEvent(E_TOUCHBEGIN, HANDLER(BattleState, HandleTouchBegin));

        const String str("ROOTUI");
        localRootUIElement = context_->GetSubsystem<UI>()->GetRoot()->CreateChild<Urho3D::Menu>(str, -1); //(String("Root") + this->GetTypeName() + "UINode");
        Text* text = localRootUIElement->CreateChild<Text>();
        text->SetText("Press Enter to Continue \n- OR -\n0 for Root | 9 for Mon | 8 for Move");
        text->SetColor(Color::WHITE);
        text->SetFont(GetSubsystem<ResourceCache>()->GetResource<Font>("Fonts/BlueHighway.ttf"), 14);
        text->SetTextAlignment(HA_CENTER);
        localRootUIElement->SetHorizontalAlignment(HA_CENTER);
        localRootUIElement->SetVerticalAlignment(VA_CENTER);
        text->SetHorizontalAlignment(HA_CENTER);
        text->SetVerticalAlignment(VA_CENTER);

        cameraNode_ = scene_->CreateChild("Camera");
        Urho3D::Camera* camera = cameraNode_->CreateComponent<Urho3D::Camera>();
        camera->SetFarClip(300.0f);
//        cameraNode_->SetPosition({0,20,0});
//        cameraNode_->LookAt({0,0,0});

        StaticModel* model = scene_->CreateChild()->CreateComponent<StaticModel>();
        model->SetModel(GetSubsystem<ResourceCache>()->GetResource<Model>("Models/Box.mdl"));
        model->SetMaterial(GetSubsystem<ResourceCache>()->GetResource<Material>("Materials/Stone.xml"));

    //    terminatorNode = scene_->CreateChild("Terminator");
    //    ScriptInstance* terminatorInstance = terminatorNode->CreateComponent<ScriptInstance>();
    //    terminatorInstance->CreateObject(GetSubsystem<ResourceCache>()->GetResource<ScriptFile>("Scripts/Terminator.as"), "Termination");

//    #ifdef DEBUG
        DebugRenderer* rend = scene_->CreateComponent<DebugRenderer>();
        rend->SetView(camera);
//    #endif // DEBUG

        // Set an initial position for the camera scene node above the plane
        cameraNode_->SetPosition(Vector3(0.0f, 5.0f, 0.0f));

        cameraNode_->LookAt(Vector3(0.0f, 0.0f, 0.0f));

    //    ScriptInstance* camInstance = cameraNode_->CreateComponent<ScriptInstance>();
    //    camInstance->CreateObject(GetSubsystem<ResourceCache>()->GetResource<ScriptFile>("Camera.as"), "TargetCam"); // "Mover");

        Renderer* renderer = GetSubsystem<Renderer>();

        viewport_ = new Viewport(context_, scene_, cameraNode_->GetComponent<Urho3D::Camera>());
        renderer->SetViewport(0, viewport_);
        auto rp = viewport_->GetRenderPath();
//        rp->RemoveCommands("clear");
        rp->GetCommand(0)->clearFlags_ = CLEAR_COLOR;//CLEAR_STENCIL;//CLEAR_DEPTH | CLEAR_STENCIL;
        rp->GetCommand(0)->clearColor_ = Color(1.0,0.0,0.0,0.5);
//        rp->AddCommand(*(rp->GetCommand(0)));

//        Urho and Tangram fight over GPU stuff
        rend->AddLine({-30,-30,-30},{30,30,30},0xaaaaaaaa,false);


        Node* zoneNode = scene_->CreateChild("Zone");
        Zone* zone = zoneNode->CreateComponent<Zone>();
        zone->SetBoundingBox(BoundingBox(-1000.0f, 1000.0f));
        zone->SetAmbientColor(Color(0.15f, 0.15f, 0.15f, 0.5f));
        zone->SetFogColor(Color(0.5f, 0.5f, 0.7f, 0.5f));
        zone->SetFogStart(100.0f);
        zone->SetFogEnd(300.0f);

    //    fieldNode = scene_->CreateChild("Field");
    //    ScriptInstance* instance = fieldNode->CreateComponent<ScriptInstance>();
    //    instance->CreateObject(GetSubsystem<ResourceCache>()->GetResource<ScriptFile>("BattleLoad.as"), "Load");

//        good = true;
//        e = new EditorManager(GetContext());

        LOGINFO("Completed Game State Root Menu Start!");
    //	GetSubsystem<Input>()->AddScreenJoystick(GetSubsystem<ResourceCache>()->GetResource<XMLFile>("TestAxes"));

    //	if (GetSubsystem<Input>()->GetNumJoysticks() == 0)
    //		new Stick(context_->GetSubsystem<UI>()->GetRoot(), GetSubsystem<Input>()->AddScreenJoystick(GetSubsystem<ResourceCache>()->GetResource<XMLFile>("UI/TestAxes.xml")), 0, {20,20,800,1800}, false);

        GetSubsystem<Audio>()->SetMasterGain(SOUND_MUSIC,0.15);

        GetSubsystem<Input>()->SetMouseMode(MM_FREE);
        GetSubsystem<Input>()->SetMouseVisible(true);


        SubscribeToEvent(E_BEGINRENDERING,HANDLER(UrhoApp,Update));
}

void UrhoApp::Setup()
{
    engineParameters_["ExternalWindow"] = window_;
}

int UrhoApp::MyInit()
{
//    int Application::Run()
    {
        // Emscripten-specific: C++ exceptions are turned off by default in -O1 (and above), unless '-s DISABLE_EXCEPTION_CATCHING=0' flag is set
        // Urho3D build configuration uses -O3 (Release), -O2 (RelWithDebInfo), and -O0 (Debug)
        // Thus, the try-catch block below should be optimised out except in Debug build configuration
        try
        {
            Setup();
            if (exitCode_)
                return exitCode_;

            if (!engine_->Initialize(engineParameters_))
            {
                ErrorExit();
                return exitCode_;
            }

            Start();
            if (exitCode_)
                return exitCode_;

            // Platforms other than iOS and Emscripten run a blocking main loop
//    #if !defined(IOS) && !defined(__EMSCRIPTEN__)
//            while (!engine_->IsExiting())
//                engine_->RunFrame();

//            Stop();
//            // iOS will setup a timer for running animation frames so eg. Game Center can run. In this case we do not
//            // support calling the Stop() function, as the application will never stop manually
//    #else
//    #if defined(IOS)
//            SDL_iPhoneSetAnimationCallback(GetSubsystem<Graphics>()->GetWindow(), 1, &RunFrame, engine_);
//    #elif defined(__EMSCRIPTEN__)
//            emscripten_set_main_loop_arg(RunFrame, engine_, 0, 1);
//    #endif
//    #endif

            return exitCode_;
        }
        catch (std::bad_alloc&)
        {
            ErrorDialog(GetTypeName(), "An out-of-memory error occurred. The application will now exit.");
            return EXIT_FAILURE;
        }
    }
}

void UrhoApp::UrhoFrame()
{
    engine_->RunFrame();

}

void UrhoApp::MyStop()
{
    Stop();

}

void UrhoApp::Update(StringHash eventType, VariantMap &eventData)
{
//    GetSubsystem<Graphics>()->Clear(CLEAR_COLOR,Color(1.0,0.0,1.0,0.5));
}


UrhoApp* RunApplication(void *window)
{
    /*Urho3D::SharedPtr<Urho3D::Context>*/Urho3D::Context* context(new Urho3D::Context());
    /*Urho3D::SharedPtr<UrhoApp> application*/return (new UrhoApp(context,window));
//    return application->Run();
}
[/code]

main.cpp
[code]
//http://stackoverflow.com/questions/4052940/how-to-make-an-opengl-rendering-context-with-transparent-background
//http://stackoverflow.com/questions/9363491/how-to-make-transparent-window-on-linux

/*------------------------------------------------------------------------
* A demonstration of OpenGL in a  ARGB window
*    => support for composited window transparency
*
* (c) 2011 by Wolfgang 'datenwolf' Draxinger
*     See me at comp.graphics.api.opengl and StackOverflow.com

* License agreement: This source code is provided "as is". You
* can use this source code however you want for your own personal
* use. If you give this source code to anybody else then you must
* leave this message in it.
*
* This program is based on the simplest possible
* Linux OpenGL program by FTB (see info below)

The simplest possible Linux OpenGL program? Maybe...

(c) 2002 by FTB. See me in comp.graphics.api.opengl

--
<\___/>
/ O O \
\_____/  FTB.

------------------------------------------------------------------------*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

#include <GL/gl.h>
#include <GL/glx.h>
#include <GL/glxext.h>
#include <X11/Xatom.h>
#include <X11/extensions/Xrender.h>
#include <X11/Xutil.h>

#include "/usr/local/include/Urho3D/Urho3D.h"
#include "UrhoApp.hpp"

UrhoApp* myApp;

#define USE_CHOOSE_FBCONFIG

static void fatalError(const char *why)
{
 fprintf(stderr, "%s", why);
 exit(0x666);
}

static int Xscreen;
static Atom del_atom;
static Colormap cmap;
static Display *Xdisplay;
static XVisualInfo *visual;
static XRenderPictFormat *pict_format;
static GLXFBConfig *fbconfigs, fbconfig;
static int numfbconfigs;
static GLXContext render_context;
static Window Xroot, window_handle;
static GLXWindow glX_window_handle;
static int width, height;

static int VisData[] = {
GLX_RENDER_TYPE, GLX_RGBA_BIT,
GLX_DRAWABLE_TYPE, GLX_WINDOW_BIT,
GLX_DOUBLEBUFFER, True,
GLX_RED_SIZE, 8,
GLX_GREEN_SIZE, 8,
GLX_BLUE_SIZE, 8,
GLX_ALPHA_SIZE, 8,
GLX_DEPTH_SIZE, 16,
None
};

static int isExtensionSupported(const char *extList, const char *extension)
{

const char *start;
const char *where, *terminator;

/* Extension names should not have spaces. */
where = strchr(extension, ' ');
if ( where || *extension == '\0' )
 return 0;

/* It takes a bit of care to be fool-proof about parsing the
  OpenGL extensions string. Don't be fooled by sub-strings,
  etc. */
for ( start = extList; ; ) {
 where = strstr( start, extension );

 if ( !where )
   break;

 terminator = where + strlen( extension );

 if ( where == start || *(where - 1) == ' ' )
   if ( *terminator == ' ' || *terminator == '\0' )
 return 1;

 start = terminator;
}
return 0;
}

static Bool WaitForMapNotify(Display *d, XEvent *e, char *arg)
{
 return d && e && arg && (e->type == MapNotify) && (e->xmap.window == *(Window*)arg);
}

static void describe_fbconfig(GLXFBConfig fbconfig)
{
 int doublebuffer;
 int red_bits, green_bits, blue_bits, alpha_bits, depth_bits;

 glXGetFBConfigAttrib(Xdisplay, fbconfig, GLX_DOUBLEBUFFER, &doublebuffer);
 glXGetFBConfigAttrib(Xdisplay, fbconfig, GLX_RED_SIZE, &red_bits);
 glXGetFBConfigAttrib(Xdisplay, fbconfig, GLX_GREEN_SIZE, &green_bits);
 glXGetFBConfigAttrib(Xdisplay, fbconfig, GLX_BLUE_SIZE, &blue_bits);
 glXGetFBConfigAttrib(Xdisplay, fbconfig, GLX_ALPHA_SIZE, &alpha_bits);
 glXGetFBConfigAttrib(Xdisplay, fbconfig, GLX_DEPTH_SIZE, &depth_bits);

 fprintf(stderr, "FBConfig selected:\n"
 "Doublebuffer: %s\n"
 "Red Bits: %d, Green Bits: %d, Blue Bits: %d, Alpha Bits: %d, Depth Bits: %d\n",
 doublebuffer == True ? "Yes" : "No",
 red_bits, green_bits, blue_bits, alpha_bits, depth_bits);
}

static void createTheWindow()
{
 XEvent event;
 int x,y, attr_mask;
 XSizeHints hints;
 XWMHints *startup_state;
 XTextProperty textprop;
 XSetWindowAttributes attr = {0,};
 static char *title = "FTB's little OpenGL example - ARGB extension by WXD";

 Xdisplay = XOpenDisplay(NULL);
 if (!Xdisplay) {
 fatalError("Couldn't connect to X server\n");
 }
 Xscreen = DefaultScreen(Xdisplay);
 Xroot = RootWindow(Xdisplay, Xscreen);

 fbconfigs = glXChooseFBConfig(Xdisplay, Xscreen, VisData, &numfbconfigs);
 fbconfig = 0;
 for(int i = 0; i<numfbconfigs; i++) {
 visual = (XVisualInfo*) glXGetVisualFromFBConfig(Xdisplay, fbconfigs[i]);
 if(!visual)
     continue;

 pict_format = XRenderFindVisualFormat(Xdisplay, visual->visual);
 if(!pict_format)
     continue;

 fbconfig = fbconfigs[i];
 if(pict_format->direct.alphaMask > 0) {
     break;
 }
 }

 if(!fbconfig) {
 fatalError("No matching FB config found");
 }

 describe_fbconfig(fbconfig);

 /* Create a colormap - only needed on some X clients, eg. IRIX */
 cmap = XCreateColormap(Xdisplay, Xroot, visual->visual, AllocNone);

 attr.colormap = cmap;
 attr.background_pixmap = None;
 attr.border_pixmap = None;
 attr.border_pixel = 0;
 attr.event_mask =
 StructureNotifyMask |
 EnterWindowMask |
 LeaveWindowMask |
 ExposureMask |
 ButtonPressMask |
 ButtonReleaseMask |
 OwnerGrabButtonMask |
 KeyPressMask |
 KeyReleaseMask;

 attr_mask =
 CWBackPixmap|
 CWColormap|
 CWBorderPixel|
 CWEventMask;

 width = DisplayWidth(Xdisplay, DefaultScreen(Xdisplay))/2;
 height = DisplayHeight(Xdisplay, DefaultScreen(Xdisplay))/2;
 x=width/2, y=height/2;

 window_handle = XCreateWindow(  Xdisplay,
         Xroot,
         x, y, width, height,
         0,
         visual->depth,
         InputOutput,
         visual->visual,
         attr_mask, &attr);

 if( !window_handle ) {
 fatalError("Couldn't create the window\n");
 }

#if USE_GLX_CREATE_WINDOW
 int glXattr[] = { None };
 glX_window_handle = glXCreateWindow(Xdisplay, fbconfig, window_handle, glXattr);
 if( !glX_window_handle ) {
 fatalError("Couldn't create the GLX window\n");
 }
#else
 glX_window_handle = window_handle;
#endif

 textprop.value = (unsigned char*)title;
 textprop.encoding = XA_STRING;
 textprop.format = 8;
 textprop.nitems = strlen(title);

 hints.x = x;
 hints.y = y;
 hints.width = width;
 hints.height = height;
 hints.flags = USPosition|USSize;

 startup_state = XAllocWMHints();
 startup_state->initial_state = NormalState;
 startup_state->flags = StateHint;

 XSetWMProperties(Xdisplay, window_handle,&textprop, &textprop,
     NULL, 0,
     &hints,
     startup_state,
     NULL);


 XFree(startup_state);

 XMapWindow(Xdisplay, window_handle);
 XIfEvent(Xdisplay, &event, WaitForMapNotify, (char*)&window_handle);

 if ((del_atom = XInternAtom(Xdisplay, "WM_DELETE_WINDOW", 0)) != None) {
 XSetWMProtocols(Xdisplay, window_handle, &del_atom, 1);
 }
}

static int ctxErrorHandler( Display *dpy, XErrorEvent *ev )
{
 fputs("Error at context creation", stderr);
 return 0;
}

static void createTheRenderContext()
{
 int dummy;
 if (!glXQueryExtension(Xdisplay, &dummy, &dummy)) {
 fatalError("OpenGL not supported by X server\n");
 }

#if USE_GLX_CREATE_CONTEXT_ATTRIB
 #define GLX_CONTEXT_MAJOR_VERSION_ARB       0x2091
 #define GLX_CONTEXT_MINOR_VERSION_ARB       0x2092
 render_context = NULL;
 if( isExtensionSupported( glXQueryExtensionsString(Xdisplay, DefaultScreen(Xdisplay)), "GLX_ARB_create_context" ) ) {
 typedef GLXContext (*glXCreateContextAttribsARBProc)(Display*, GLXFBConfig, GLXContext, Bool, const int*);
 glXCreateContextAttribsARBProc glXCreateContextAttribsARB = (glXCreateContextAttribsARBProc)glXGetProcAddressARB( (const GLubyte *) "glXCreateContextAttribsARB" );
 if( glXCreateContextAttribsARB ) {
     int context_attribs[] =
     {
     GLX_CONTEXT_MAJOR_VERSION_ARB, 3,
     GLX_CONTEXT_MINOR_VERSION_ARB, 0,
     //GLX_CONTEXT_FLAGS_ARB        , GLX_CONTEXT_FORWARD_COMPATIBLE_BIT_ARB,
     None
     };

     int (*oldHandler)(Display*, XErrorEvent*) = XSetErrorHandler(&ctxErrorHandler);

     render_context = glXCreateContextAttribsARB( Xdisplay, fbconfig, 0, True, context_attribs );

     XSync( Xdisplay, False );
     XSetErrorHandler( oldHandler );

     fputs("glXCreateContextAttribsARB failed", stderr);
 } else {
     fputs("glXCreateContextAttribsARB could not be retrieved", stderr);
 }
 } else {
     fputs("glXCreateContextAttribsARB not supported", stderr);
 }

 if(!render_context)
 {
#else
 {
#endif
 render_context = glXCreateNewContext(Xdisplay, fbconfig, GLX_RGBA_TYPE, 0, True);
 if (!render_context) {
     fatalError("Failed to create a GL context\n");
 }
 }

 if (!glXMakeContextCurrent(Xdisplay, glX_window_handle, glX_window_handle, render_context)) {
 fatalError("glXMakeCurrent failed for window\n");
 }
}

static int updateTheMessageQueue()
{
 XEvent event;
 XConfigureEvent *xc;

 while (XPending(Xdisplay))
 {
 XNextEvent(Xdisplay, &event);
 switch (event.type)
 {
 case ClientMessage:
     if (event.xclient.data.l[0] == del_atom)
     {
     return 0;
     }
 break;

 case ConfigureNotify:
     xc = &(event.xconfigure);
     width = xc->width;
     height = xc->height;
     break;
 }
 }
 return 1;
}

/*6----7
 /|   /|
3----2 |
| 5--|-4
|/   |/
0----1

*/

GLfloat cube_vertices[][8] =  {
 /*  X     Y     Z   Nx   Ny   Nz    S    T */
 {-1.0, -1.0,  1.0, 0.0, 0.0, 1.0, 0.0, 0.0}, // 0
 { 1.0, -1.0,  1.0, 0.0, 0.0, 1.0, 1.0, 0.0}, // 1
 { 1.0,  1.0,  1.0, 0.0, 0.0, 1.0, 1.0, 1.0}, // 2
 {-1.0,  1.0,  1.0, 0.0, 0.0, 1.0, 0.0, 1.0}, // 3

 { 1.0, -1.0, -1.0, 0.0, 0.0, -1.0, 0.0, 0.0}, // 4
 {-1.0, -1.0, -1.0, 0.0, 0.0, -1.0, 1.0, 0.0}, // 5
 {-1.0,  1.0, -1.0, 0.0, 0.0, -1.0, 1.0, 1.0}, // 6
 { 1.0,  1.0, -1.0, 0.0, 0.0, -1.0, 0.0, 1.0}, // 7

 {-1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0, 0.0}, // 5
 {-1.0, -1.0,  1.0, -1.0, 0.0, 0.0, 1.0, 0.0}, // 0
 {-1.0,  1.0,  1.0, -1.0, 0.0, 0.0, 1.0, 1.0}, // 3
 {-1.0,  1.0, -1.0, -1.0, 0.0, 0.0, 0.0, 1.0}, // 6

 { 1.0, -1.0,  1.0,  1.0, 0.0, 0.0, 0.0, 0.0}, // 1
 { 1.0, -1.0, -1.0,  1.0, 0.0, 0.0, 1.0, 0.0}, // 4
 { 1.0,  1.0, -1.0,  1.0, 0.0, 0.0, 1.0, 1.0}, // 7
 { 1.0,  1.0,  1.0,  1.0, 0.0, 0.0, 0.0, 1.0}, // 2

 {-1.0, -1.0, -1.0,  0.0, -1.0, 0.0, 0.0, 0.0}, // 5
 { 1.0, -1.0, -1.0,  0.0, -1.0, 0.0, 1.0, 0.0}, // 4
 { 1.0, -1.0,  1.0,  0.0, -1.0, 0.0, 1.0, 1.0}, // 1
 {-1.0, -1.0,  1.0,  0.0, -1.0, 0.0, 0.0, 1.0}, // 0

 {-1.0, 1.0,  1.0,  0.0,  1.0, 0.0, 0.0, 0.0}, // 3
 { 1.0, 1.0,  1.0,  0.0,  1.0, 0.0, 1.0, 0.0}, // 2
 { 1.0, 1.0, -1.0,  0.0,  1.0, 0.0, 1.0, 1.0}, // 7
 {-1.0, 1.0, -1.0,  0.0,  1.0, 0.0, 0.0, 1.0}, // 6
};

static void draw_cube(void)
{
 glEnableClientState(GL_VERTEX_ARRAY);
 glEnableClientState(GL_NORMAL_ARRAY);
 glEnableClientState(GL_TEXTURE_COORD_ARRAY);

 glVertexPointer(3, GL_FLOAT, sizeof(GLfloat) * 8, &cube_vertices[0][0]);
 glNormalPointer(GL_FLOAT, sizeof(GLfloat) * 8, &cube_vertices[0][3]);
 glTexCoordPointer(2, GL_FLOAT, sizeof(GLfloat) * 8, &cube_vertices[0][6]);

 glDrawArrays(GL_QUADS, 0, 24);
}

float const light0_dir[]={0,1,0,0};
float const light0_color[]={78./255., 80./255., 184./255.,1};

float const light1_dir[]={-1,1,1,0};
float const light1_color[]={255./255., 220./255., 97./255.,1};

float const light2_dir[]={0,-1,0,0};
float const light2_color[]={31./255., 75./255., 16./255.,1};

static void redrawTheWindow()
{
 float const aspect = (float)width / (float)height;

 static float a=0;
 static float b=0;
 static float c=0;

 glDrawBuffer(GL_BACK);

 glViewport(0, 0, width, height);

 // Clear with alpha = 0.0, i.e. full transparency
 glClearColor(0.0, 0.0, 0.0, 0.0);
 glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);

 glMatrixMode(GL_PROJECTION);
 glLoadIdentity();
 glFrustum(-aspect, aspect, -1, 1, 2.5, 10);

 glMatrixMode(GL_MODELVIEW);
 glLoadIdentity();

 glEnable(GL_DEPTH_TEST);
 glEnable(GL_CULL_FACE);

 glEnable(GL_BLEND);
 glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

 glLightfv(GL_LIGHT0, GL_POSITION, light0_dir);
 glLightfv(GL_LIGHT0, GL_DIFFUSE, light0_color);

 glLightfv(GL_LIGHT1, GL_POSITION, light1_dir);
 glLightfv(GL_LIGHT1, GL_DIFFUSE, light1_color);

 glLightfv(GL_LIGHT2, GL_POSITION, light2_dir);
 glLightfv(GL_LIGHT2, GL_DIFFUSE, light2_color);

 glTranslatef(0., 0., -5.);

 glRotatef(a, 1, 0, 0);
 glRotatef(b, 0, 1, 0);
 glRotatef(c, 0, 0, 1);

 glEnable(GL_LIGHT0);
 glEnable(GL_LIGHT1);
 glEnable(GL_LIGHTING);

 glEnable(GL_COLOR_MATERIAL);
 glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE);

 glColor4f(1., 1., 1., 0.9);

 glCullFace(GL_FRONT);
 draw_cube();
 glCullFace(GL_BACK);
 draw_cube();

 a = fmod(a+0.1, 360.);
 b = fmod(b+0.5, 360.);
 c = fmod(c+0.25, 360.);

 glXSwapBuffers(Xdisplay, glX_window_handle);
}

int main(int argc, char *argv[])
{
 createTheWindow();
 createTheRenderContext();

 myApp = RunApplication((void*)window_handle);
 myApp->MyInit();

 while (updateTheMessageQueue()) {
 redrawTheWindow();
 myApp->UrhoFrame();
 }

 return 0;
}


//// code nicked mainly from here:
//// http://lazyfoo.net/tutorials/SDL/50_SDL_and_opengl_2/index.php


///* to compile

//    ### installation on ubuntu
//    # install compiler etc
//    sudo apt-get install --yes software-properties-common g++ make
//    # install sdl2
//    sudo apt-get install --yes libsdl2-dev
//    # install opengl
//    sudo apt-get install --yes freeglut3-dev

//    # compile with
//    g++ main.cpp -I /usr/include/SDL2/ -lSDL2  -lGL

//    ## installation on mac
//    # install xcode with command line tools
//    # install sdl2*.dmg, put everything in ~/Library/Frameworks

//    # compile with with g++ (or with clang++)
//    g++ main.cpp -I ~/Library/Frameworks/SDL2.framework/Headers -I OpenGL -framework SDL2  -F ~/Library/Frameworks -framework OpenGL

//*/

//#include <SDL2/SDL.h>
//#include <SDL2/SDL_opengl.h>
//#include <SDL2/SDL_video.h>
//#include <stdio.h>


////Screen dimension constants
//const int SCREEN_WIDTH = 640;
//const int SCREEN_HEIGHT = 480;


////Main loop flag
//bool quit = false;


////Starts up SDL, creates window, and initializes OpenGL
//bool init();

////Initializes matrices and clear color
//bool initGL();

////Input handler
//void handleKeys( unsigned char key, int x, int y );

////Per frame update
//void update();

////Renders quad to the screen
//void render();

////Frees media and shuts down SDL
//void close();

////The window we'll be rendering to
//SDL_Window* gWindow = NULL;

////OpenGL context
//SDL_GLContext gContext;

////Render flag
//bool gRenderQuad = true;

//bool init()
//{
//    //Initialization flag
//    bool success = true;

//    //Initialize SDL
//    if( SDL_Init( SDL_INIT_VIDEO ) < 0 )
//    {
//        printf( "SDL could not initialize! SDL Error: %s\n", SDL_GetError() );
//        success = false;
//    }
//    else
//    {
//        //Use OpenGL 2.1
//        SDL_GL_SetAttribute( SDL_GL_CONTEXT_MAJOR_VERSION, 2 );
//        SDL_GL_SetAttribute( SDL_GL_CONTEXT_MINOR_VERSION, 1 );

//        //Create window
//        gWindow = SDL_CreateWindow( "SDL Tutorial", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_OPENGL | SDL_WINDOW_SHOWN );
//        if( gWindow == NULL )
//        {
//            printf( "Window could not be created! SDL Error: %s\n", SDL_GetError() );
//            success = false;
//        }
//        else
//        {
//            //Create context
//            gContext = SDL_GL_CreateContext( gWindow );
////            gWindow->driverdata->dispman_window.element
//            SDL_SetWindowOpacity(gWindow,0.5);
//            if( gContext == NULL )
//            {
//                printf( "OpenGL context could not be created! SDL Error: %s\n", SDL_GetError() );
//                success = false;
//            }
//            else
//            {
//                //Use Vsync
//                if( SDL_GL_SetSwapInterval( 1 ) < 0 )
//                {
//                    printf( "Warning: Unable to set VSync! SDL Error: %s\n", SDL_GetError() );
//                }

//                //Initialize OpenGL
//                if( !initGL() )
//                {
//                    printf( "Unable to initialize OpenGL!\n" );
//                    success = false;
//                }
//            }
//        }
//    }

//    return success;
//}

//bool initGL()
//{
//    bool success = true;
//    GLenum error = GL_NO_ERROR;

//    //Initialize Projection Matrix
//    glMatrixMode( GL_PROJECTION );
//    glLoadIdentity();

//    //Check for error
//    error = glGetError();
//    if( error != GL_NO_ERROR )
//    {
//        success = false;
//    }

//    //Initialize Modelview Matrix
//    glMatrixMode( GL_MODELVIEW );
//    glLoadIdentity();

//    //Check for error
//    error = glGetError();
//    if( error != GL_NO_ERROR )
//    {
//        success = false;
//    }

//    //Initialize clear color
//    glClearColor( 0.f, 0.f, 0.f, 1.f );

//    //Check for error
//    error = glGetError();
//    if( error != GL_NO_ERROR )
//    {
//        success = false;
//    }

//    return success;
//}

//void handleKeys( unsigned char key, int x, int y )
//{
//    if( key == 'q' )
//    {
//        quit = true;
//    }
//}

//void update()
//{
//    //No per frame update needed
//}

//void render()
//{
//    //Clear color buffer
//    glClear( GL_COLOR_BUFFER_BIT );

//    //Render quad
//    if( gRenderQuad )
//    {
//        glRotatef(0.4f,0.0f,1.0f,0.0f);    // Rotate The cube around the Y axis
//        glRotatef(0.2f,1.0f,1.0f,1.0f);
//        glColor3f(0.0f,1.0f,0.0f);

//        glBegin( GL_QUADS );
//            glVertex2f( -0.5f, -0.5f );
//            glVertex2f( 0.5f, -0.5f );
//            glVertex2f( 0.5f, 0.5f );
//            glVertex2f( -0.5f, 0.5f );
//        glEnd();
//    }
//}

//void close()
//{
//    //Destroy window
//    SDL_DestroyWindow( gWindow );
//    gWindow = NULL;

//    //Quit SDL subsystems
//    SDL_Quit();
//}

//int main( int argc, char* args[] )
//{
//    //Start up SDL and create window
//    if( !init() )
//    {
//        printf( "Failed to initialize!\n" );
//    }
//    else
//    {

//        //Event handler
//        SDL_Event e;

//        //Enable text input
//        SDL_StartTextInput();

//        //While application is running
//        while( !quit )
//        {
//            //Handle events on queue
//            while( SDL_PollEvent( &e ) != 0 )
//            {
//                //User requests quit
//                if( e.type == SDL_QUIT )
//                {
//                    quit = true;
//                }
//                //Handle keypress with current mouse position
//                else if( e.type == SDL_TEXTINPUT )
//                {
//                    int x = 0, y = 0;
//                    SDL_GetMouseState( &x, &y );
//                    handleKeys( e.text.text[ 0 ], x, y );
//                }
//            }

//            //Render quad
//            render();

//            //Update screen
//            SDL_GL_SwapWindow( gWindow );
//        }

//        //Disable text input
//        SDL_StopTextInput();
//    }

//    //Free resources and close SDL
//    close();

//    return 0;
//}
[/code]


Edit: Playing with it a bit more (trying to add FXAA), I noticed that with the transparency, the UI text doesn't show up (I didn't realize I left it in the program so didn't notice before). This only occurs with the transparency, which doesn't work with FXAA (or Bloom) enabled, but with those effects enabled on the render path, the text is visible. Any guesses as to why?

-------------------------

