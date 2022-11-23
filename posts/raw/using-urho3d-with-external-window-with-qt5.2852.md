mazataza | 2017-03-05 00:58:18 UTC | #1

i am tring to bind Urho3D to Qt widgets and it works.
i created Qt Mainwindow with two widgets the center widgets is the window used by Urho3d rendering and the second is just a list widgets.

for Urho3d widgets i use the Hello example which display only a text.
the problem I have i that when resizing window the Urho3d widgets flickert and i don't know why?
any idea which can case this?

the following code is what i use to initialized the render

    int URHO3DWidget::Run() {
    	MainWindow->createDockWindows();
    	VariantMap engineParameters;
    	engineParameters[Urho3D::EP_FRAME_LIMITER] = false;
    	engineParameters[Urho3D::EP_RESOURCE_PATHS] = "CoreData;Data";
    	engineParameters[Urho3D::EP_LOG_NAME] = "URHO3DWidget.log";
    	engineParameters[Urho3D::EP_EXTERNAL_WINDOW] = (void*)(MainWindow->centralWidget()->winId());
    	engineParameters[Urho3D::EP_WINDOW_RESIZABLE] = true;
    	engineParameters[Urho3D::EP_FULL_SCREEN] = false;
    	if (!engine->Initialize(engineParameters))
    		return -1;

    	QTimer timer;
    	connect(&timer, SIGNAL(timeout()), this, SLOT(OnTimeout()));
    	timer.start(0);

    	ResourceCache* cache = GetSubsystem<ResourceCache>();

    	// Construct new Text object
    	SharedPtr<Text> helloText(new Text(context_));

    	// Set String to display
    	helloText->SetText("Hello World from Urho3D!");

    	// Set font and text color
    	helloText->SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"), 30);
    	helloText->SetColor(Color(0.0f, 1.0f, 0.0f));

    	// Align Text center-screen
    	helloText->SetHorizontalAlignment(HA_CENTER);
    	helloText->SetVerticalAlignment(VA_CENTER);

    	// Add Text instance to the UI root element
    	GetSubsystem<UI>()->GetRoot()->AddChild(helloText);
    	QSize s(800, 600);


    	MainWindow->setMinimumSize(s);

    	MainWindow->show();

    	return QApplication::exec();
    }

the timer function do the following

    void URHO3DWidget::OnTimeout()
    {
    	if (engine && !engine->IsExiting()) {
    		engine->RunFrame();
    	}
    }

-------------------------

Eugene | 2017-03-05 09:44:34 UTC | #2

What's the 'flickering'?
Almost any graphical artifact may be called so,

-------------------------

mazataza | 2017-03-05 10:05:38 UTC | #3

sorry for my bad english ..
i mean with flickering : 
the main window (where Urho3D rendered the string "Hello World from Urho3D!") during resizing the painting of the text appear and disappear and this happend until stop resizing. The background of the window change quickly to white and then the text appear with black background.

-------------------------

Eugene | 2017-03-05 11:42:43 UTC | #4

Then I understood.
I also have some artifacts when resizing, but I have no such flickering.
I have almost the same code, so I don't know where the problem is.

What GAPI did you use in Urho?

-------------------------

mazataza | 2017-03-05 15:29:18 UTC | #5

i you mean with GAPI which 3D rendering i use then i use opengl.
i build Urho3D with openGl only for visual studion 2015 64bit.

-------------------------

Eugene | 2017-03-05 16:14:45 UTC | #6

I see. I use DX11.
Try DX9 or DX11, try to share some demo, this may help to localize this issue.

However, I suggest you not to think about it too much.
GAPIs and engines usually don't care a lot about corner cases like switching from fullscreen to window or resizing viewport. It is a kind of 'implementation-specific' behaviour that works... somehow, but not always perfectly.
Such flickering may be caused by some dirty logic at the level of your code, Qt, Urho, SDL or even graphic driver.

-------------------------

mazataza | 2017-03-05 19:38:36 UTC | #7

you are right about it.
this can be sort later
thanks for your replay

-------------------------

