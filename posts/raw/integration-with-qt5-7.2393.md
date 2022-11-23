amit.nath30 | 2017-01-02 01:15:09 UTC | #1

Hello every

for past 7days i have been trying hard to integrate qt5.7 with urho3d but could not figure out the way, I followed aster2013 particle editor 2d (seems to using qt4) but didn't succeed.

I really appreciate if some one show me the way

-------------------------

rasteron | 2017-01-02 01:15:10 UTC | #2

Maybe you should try it first with the same exact version that aster originally used in building the particle editor. Once you are familiar with it then try upgrading and know the difference between these versions. I remember changing the header files and looking up some function equivalents to make it work with some test projects.

Qt is a big library and I think getting some experience building some Qt4 and 5 apps with it is the first step. :slight_smile:

-------------------------

dakilla | 2017-01-02 01:15:11 UTC | #3

I have a project with Qt5.7 and it works fine.

I use a QWidget to draw inside. I use a class based on Urho3D object to communicate easily with urho.

[code]class eRenderView : public QWidget, public Object
{
    Q_OBJECT
    URHO3D_OBJECT(eRenderView, Object)
...[/code]

At Urho init I set the  ExternalWindow param with the QWidget handle.
something like that :

m_hwnd = (void*)m_renderWindow>winId();
...
engineParameters["ExternalWindow"]  = m_hwnd;

I also use a Qtimer to repaint each frame by calling Engine::RunFrame().

For inputs, I also need to map and push the Qwidget events to SDL2 ex :

[code]void eRenderView::keyPressEvent(QKeyEvent *ke)
{
    QWidget::keyPressEvent(ke);

    // add key to held keys list
    if (!m_keysDown.contains(ke->key()) && !ke->isAutoRepeat())
        m_keysDown.append(ke->key());

    // Transmit key press event to SDL
    SDL_Event sdlEvent;
    sdlEvent.type = SDL_KEYDOWN;
    sdlEvent.key.keysym.sym = __convertQtKeyToSDL( Qt::Key(ke->key()) );
    sdlEvent.key.keysym.mod = __convertQtKeyModifierToSDL(ke->modifiers());
    SDL_PushEvent(&sdlEvent);
}[/code]

-------------------------

amit.nath30 | 2017-01-02 01:15:12 UTC | #4

problem I am having is creating the Context. When i use below code in main.cpp

Urho3D::SharedPtr<Urho3D::Context> context(new Urho3D::Context());
or by
Urho3D::Context* context = new Urho3D::Context();

I am getting error in ptr.h at AddRef() and ReleaseRef()

i might overlooking some settings which causing this error, but couldn't able to track it down

-------------------------

dakilla | 2017-01-02 01:15:12 UTC | #5

I created a static context in a class  :

[code]class eGraphics : public Object
{
    URHO3D_OBJECT(eGraphics, Object)

public:
    eGraphics();
    ~eGraphics();

public:
    static void                 createContext();
    static void                 freeContext();
    static Context*           m_gcontext;             // Urho3D global context
...

void eGraphics::createContext()
{
    assert(!m_gcontext);
    m_gcontext = new Context();
    assert(m_gcontext);
}

void eGraphics::freeContext()
{
    delete m_gcontext;
}


[/code]


and in main :

[code]

int main(int argc, char **argv)
{
   ...

    // create urho3d context
    eGraphics::createContext();

    // init and run Qt
    QApplication app(argc, argv);
    eMainWnd mainWnd();
    eDevice* device = new eDevice(eWF_VSYNC, eSize(300, 200), (void*)mainWnd.getRenderWidget()->winId());
    app.setActiveWindow(&mainWnd);
    mainWnd.show();

    // enter Qt event loop
    int ret = app.exec();


    // free Urho3D context
    eGraphics::freeContext();

    ---
[/code]

-------------------------

amit.nath30 | 2017-01-02 01:15:12 UTC | #6

Nope, tried your way but still getting error.

no matter what i do keep getting error when trying to create an instance of Context. which version of urho3d you are using mine is 1.6


[img]https://lh3.googleusercontent.com/wDj9nCFO_UzCC7_LIJfAv3kXnliPz3uiXGbIu3hnYYBDi02MiLoAVbmG5AWZH4CO7_WJdCfq94Qhwjs=w1920-h979[/img]

-------------------------

amit.nath30 | 2017-01-02 01:15:12 UTC | #7

Switch to visual studio 2015 edition of qt getting this error

[img]https://lh3.googleusercontent.com/X3sNWYDFkm9_3Ja2Vt4BYcm0Z0Qkt430pkT6KGdMwQKkB2DPciPuUWMX3c0_SS4qNj1yH1TDXZtN-dg=w1920-h979[/img]

[b]@dakilla[/b] can you share your qt .pro file please

-------------------------

dakilla | 2017-01-02 01:15:13 UTC | #8

I use the current master branch on github, but haven't had any problem in previous versions.

here a minimalist sample (not tested on windows), don't forget to put Data and CoreData in your build directory :

QUrhoWidget.h
[code]#ifndef QTWIDGET_H
#define QTWIDGET_H

#include <QWidget>
#include <QResizeEvent>
#include <Urho3D/Urho3DAll.h>

class QUrhoWidget : public QWidget, public Urho3D::Object
{
    Q_OBJECT
    URHO3D_OBJECT(QUrhoWidget, Object)

private:
    SharedPtr<Engine> engine_;
    SharedPtr<Scene> scene_;
    SharedPtr<Node> cameraNode_;
    int timerId;

public:
    QUrhoWidget(Context* context);

    void timerEvent(QTimerEvent* e) override;
    void resizeEvent(QResizeEvent* e) override;
    void keyPressEvent(QKeyEvent* e) override;

    void Setup();
    void Start();
    void Stop();

    void HandleKeyDown(StringHash eventType, VariantMap& eventData);
    void HandleUpdate(StringHash eventType, VariantMap& eventData);
};


#endif // QTWIDGET_H
[/code]

main.cpp
[code]#include "QUrhoWidget.h"
#include <QApplication>
#include <SDL/SDL.h>

//------------------------------------------------------------------------------------------------------
// key utilities to convert Qt key to SDL key
//------------------------------------------------------------------------------------------------------
static QMap<Qt::Key, SDL_Keycode> __keymap;
static void         __initKeyMap();
static Uint16       __convertQtKeyModifierToSDL(Qt::KeyboardModifiers qtKeyModifiers);
static SDL_Keycode  __convertQtKeyToSDL(Qt::Key qtKey);

//------------------------------------------------------------------------------------------------------
// map keys Qt/SDL
//------------------------------------------------------------------------------------------------------
void __initKeyMap()
{
    __keymap[Qt::Key_unknown]     = SDLK_UNKNOWN;
    __keymap[Qt::Key_Escape]      = SDLK_ESCAPE;
    __keymap[Qt::Key_Tab]         = SDLK_TAB;
    __keymap[Qt::Key_Backspace]   = SDLK_BACKSPACE;
    __keymap[Qt::Key_Return]      = SDLK_RETURN;
    __keymap[Qt::Key_Enter]       = SDLK_KP_ENTER;
    __keymap[Qt::Key_Insert]      = SDLK_INSERT;
    __keymap[Qt::Key_Delete]      = SDLK_DELETE;
    __keymap[Qt::Key_Pause]       = SDLK_PAUSE;
    __keymap[Qt::Key_Print]       = SDLK_PRINTSCREEN;
    __keymap[Qt::Key_SysReq]      = SDLK_SYSREQ;
    __keymap[Qt:]        = SDLK_HOME;
    __keymap[Qt::Key_End]         = SDLK_END;
    __keymap[Qt:]        = SDLK_LEFT;
    __keymap[Qt::Key_Right]       = SDLK_RIGHT;
    __keymap[Qt::Key_Up]          = SDLK_UP;
    __keymap[Qt:]        = SDLK_DOWN;
    __keymap[Qt::Key_PageUp]      = SDLK_PAGEUP;
    __keymap[Qt::Key_PageDown]    = SDLK_PAGEDOWN;
    __keymap[Qt::Key_Shift]       = SDLK_LSHIFT;
    __keymap[Qt::Key_Control]     = SDLK_LCTRL;
    __keymap[Qt::Key_Alt]         = SDLK_LALT;
    __keymap[Qt::Key_CapsLock]    = SDLK_CAPSLOCK;
    __keymap[Qt::Key_NumLock]     = SDLK_NUMLOCKCLEAR;
    __keymap[Qt::Key_ScrollLock]  = SDLK_SCROLLLOCK;
    __keymap[Qt::Key_F1]          = SDLK_F1;
    __keymap[Qt::Key_F2]          = SDLK_F2;
    __keymap[Qt::Key_F3]          = SDLK_F3;
    __keymap[Qt::Key_F4]          = SDLK_F4;
    __keymap[Qt::Key_F5]          = SDLK_F5;
    __keymap[Qt::Key_F6]          = SDLK_F6;
    __keymap[Qt::Key_F7]          = SDLK_F7;
    __keymap[Qt::Key_F8]          = SDLK_F8;
    __keymap[Qt::Key_F9]          = SDLK_F9;
    __keymap[Qt::Key_F10]         = SDLK_F10;
    __keymap[Qt::Key_F11]         = SDLK_F11;
    __keymap[Qt::Key_F12]         = SDLK_F12;
    __keymap[Qt::Key_F13]         = SDLK_F13;
    __keymap[Qt::Key_F14]         = SDLK_F14;
    __keymap[Qt::Key_F15]         = SDLK_F15;
    __keymap[Qt:]        = SDLK_MENU;
    __keymap[Qt:]        = SDLK_HELP;

    // A-Z
    for(int key='A'; key<='Z'; key++)
        __keymap[Qt::Key(key)] = key + 32;

    // 0-9
    for(int key='0'; key<='9'; key++)
        __keymap[Qt::Key(key)] = key;
}

//------------------------------------------------------------------------------------------------------
// get SDL key from Qt key
//------------------------------------------------------------------------------------------------------
SDL_Keycode __convertQtKeyToSDL(Qt::Key qtKey)
{
    SDL_Keycode sldKey = __keymap.value(Qt::Key(qtKey));

    if(sldKey == 0)
        printf("Warning: Key %d not mapped", qtKey);

    return sldKey;
}

//------------------------------------------------------------------------------------------------------
// get SDL key modifier from Qt key modifier
//------------------------------------------------------------------------------------------------------
Uint16 __convertQtKeyModifierToSDL(Qt::KeyboardModifiers qtKeyModifiers)
{
    Uint16 sdlModifiers = KMOD_NONE;

    if(qtKeyModifiers.testFlag(Qt::ShiftModifier))
        sdlModifiers |= KMOD_LSHIFT | KMOD_RSHIFT;
    if(qtKeyModifiers.testFlag(Qt::ControlModifier))
        sdlModifiers |= KMOD_LCTRL | KMOD_RCTRL;
    if(qtKeyModifiers.testFlag(Qt::AltModifier))
        sdlModifiers |= KMOD_LALT | KMOD_RALT;

    return sdlModifiers;
}

//------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------


QUrhoWidget::QUrhoWidget(Context* context) :
    Urho3D::Object(context),
    engine_(nullptr),
    scene_(nullptr)
{
    // init key map Qt => SDL
    __initKeyMap();

    // start timer to refresh engine at each frame
    timerId = startTimer(0);
}

void QUrhoWidget::timerEvent(QTimerEvent *e)
{
    QWidget::timerEvent(e);
    QApplication::processEvents();

    engine_->RunFrame();
}

void QUrhoWidget::resizeEvent(QResizeEvent* e)
{
    QWidget::resizeEvent(e);

    if(engine_->IsInitialized())
    {
        int width = e->size().width();
        int height = e->size().height();

        Graphics* graphics = GetSubsystem<Graphics>();

        SDL_Window * win = (SDL_Window*)graphics->GetWindow();
        SDL_SetWindowSize(win, width, height);
    }
}

void QUrhoWidget::keyPressEvent(QKeyEvent* e)
{
    QWidget::keyPressEvent(e);

    // Transmit key press event to SDL
    SDL_Event sdlEvent;
    sdlEvent.type = SDL_KEYDOWN;
    sdlEvent.key.keysym.sym = __convertQtKeyToSDL( Qt::Key(e->key()) );
    sdlEvent.key.keysym.mod = __convertQtKeyModifierToSDL(e->modifiers());
    SDL_PushEvent(&sdlEvent);
}

void QUrhoWidget::Setup()
{
    VariantMap engineParameters_;
    engineParameters_["FullScreen"]=false;
    engineParameters_["WindowWidth"]=1280;
    engineParameters_["WindowHeight"]=720;
    engineParameters_["WindowResizable"]=true;
    engineParameters_["ExternalWindow"]=(void*)winId();

    engine_ = new Engine(context_);
    engine_->Initialize(engineParameters_);
}

void QUrhoWidget::Start()
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();

    scene_ = new Scene(context_);
    scene_->CreateComponent<Octree>();

    Node* planeNode = scene_->CreateChild("Plane");
    planeNode->SetScale(Vector3(100.0f, 1.0f, 100.0f));
    StaticModel* planeObject = planeNode->CreateComponent<StaticModel>();
    planeObject->SetModel(cache->GetResource<Model>("Models/Plane.mdl"));
    planeObject->SetMaterial(cache->GetResource<Material>("Materials/StoneTiled.xml"));

    Node* lightNode = scene_->CreateChild("DirectionalLight");
    lightNode->SetDirection(Vector3(0.6f, -1.0f, 0.8f));
    Light* light = lightNode->CreateComponent<Light>();
    light->SetLightType(LIGHT_DIRECTIONAL);

    const unsigned NUM_OBJECTS = 25;
    for (unsigned i = 0; i < NUM_OBJECTS; ++i)
    {
        Node* mushroomNode = scene_->CreateChild("Mushroom");
        mushroomNode->SetPosition(Vector3(Random(90.0f) - 45.0f, 0.0f, Random(90.0f) - 45.0f));
        mushroomNode->SetRotation(Quaternion(0.0f, Random(360.0f), 0.0f));
        mushroomNode->SetScale(0.5f + Random(2.0f));
        StaticModel* mushroomObject = mushroomNode->CreateComponent<StaticModel>();
        mushroomObject->SetModel(cache->GetResource<Model>("Models/Mushroom.mdl"));
        mushroomObject->SetMaterial(cache->GetResource<Material>("Materials/Mushroom.xml"));
    }

    cameraNode_ = scene_->CreateChild("Camera");
    Camera* camera = cameraNode_->CreateComponent<Camera>();
    cameraNode_->SetPosition(Vector3(0.0f, 5.0f, 0.0f));


    Renderer* renderer = GetSubsystem<Renderer>();
    Viewport* viewport = new Viewport(context_, scene_, camera);
    renderer->SetViewport(0, viewport);

    SubscribeToEvent(E_KEYDOWN, URHO3D_HANDLER(QUrhoWidget, HandleKeyDown));
    SubscribeToEvent(E_UPDATE, URHO3D_HANDLER(QUrhoWidget, HandleUpdate));
}

void QUrhoWidget::Stop()
{
    // exit urho
    engine_->Exit();

    // close widget
    close();
}


void QUrhoWidget::HandleUpdate(StringHash eventType, VariantMap& eventData)
{
    using namespace Update;
    float timeStep = eventData["TimeStep"].GetFloat();

    cameraNode_->Rotate(Quaternion(30.0f * timeStep, Vector3(0, 1, 0)));

}

void QUrhoWidget::HandleKeyDown(StringHash eventType, VariantMap& eventData)
{
    using namespace KeyDown;
    int key = eventData[P_KEY].GetInt();

    if (key == KEY_ESCAPE)
    {
        Stop();
    }
}



int main(int argc, char *argv[])
{
    int ret;

    QApplication app(argc, argv);

    Urho3D::Context* context = new Urho3D::Context();

    QUrhoWidget* urhoWidget = new QUrhoWidget(context);
    urhoWidget->Setup();
    urhoWidget->Start();
    urhoWidget->resize(800,600);
    urhoWidget->show();

    ret =  app.exec();
}
[/code]

and .pro (linux only version sorry, for window just set rights win libs and urho path directory)
[code]URHO_HOME = /home/fred/Documents/Urho3D/BUILD

QT += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = QtUrho
TEMPLATE = app

INCLUDEPATH += $${URHO_HOME}/include
INCLUDEPATH += $${URHO_HOME}/include/Urho3D/ThirdParty

# Env var pointing to builded Urho3D installation's library
LIBS += -L$${URHO_HOME}/lib

# link urho3d
unix:!macx:LIBS += -lUrho3D

# link linux
unix:!macx: LIBS +=   -lXi -ldl  -lpthread -lGL -lGLU -lX11


SOURCES += main.cpp

HEADERS  += \
    QUrhoWidget.h
[/code]

-------------------------

amit.nath30 | 2017-01-02 01:15:15 UTC | #9

Success at last  :smiley: 
going through the forum I find out that I was missing some macro and library which is needed by Urho3d
adding following flags and libs to .pro file solved the problem

[code]#Then these guys, every single one of them seems to be needed on Windows
LIBS += -LC:/Qt/Qt5.7.0/Tools/mingw530_32/i686-w64-mingw32/lib/ -lkernel32
LIBS += -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -ladvapi32
LIBS += -ldbghelp -limm32 -lversion -lwinmm -lws2_32

QMAKE_CXXFLAGS += -DURHO3D_STATIC_DEFINE
QMAKE_CXXFLAGS += -DWIN32[/code]

Hope someone find it helpful

-------------------------

