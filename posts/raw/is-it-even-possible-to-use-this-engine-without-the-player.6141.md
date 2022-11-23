archwind | 2020-05-06 03:39:34 UTC | #1

I may be forced to surrender and use something else. It is not worth my time to convert some 400,000 lines of code to C++

I’m lost on this. Is it even possible to use this without the player?

This works! I have it in a menu on the editor. I’m using message boxes to debug so I can see what is happening.

[code]
        async void Gogo()
        {
            MessageBox.Show("ready to test?", "Test", (MessageBoxButtons)1);
            
            Type app = typeof(HelloWorld.HelloWorld);
            var ap = await window.Show(app, new ApplicationOptions("Data"));

            Time.Sleep(5000); //display it for 5 seconds.

            if (!Setup())
            {
                MessageBox.Show("Application could not setup", "error", (MessageBoxButtons)1);
                window.Stop();
                application.Dispose();
                Time.Sleep(500);
                Application.Exit();
            }
        }

[/code]

So I now remove this process and try it with my own code.
I will NOT render.

[code]
        protected bool Setup()
        {

            // allow for setting up resource gathering
            foreach (string s in RepositoryClass.AxiomDirectories)
            {
                List<string> repositoryDirectoryList = RepositoryClass.Instance.RepositoryDirectoryList;
                List<string> l = new List<string>();
                foreach (string repository in repositoryDirectoryList)
                {
                    l.Add(Path.Combine(repository, s));
                }

                ResourceManager.AddCommonArchive(l, "Folder");
            }

            object ret = Registry.GetValue(Config.WorldEditorBaseRegistryKey, "Disable Video Playback", false);
            ret = ret == null || string.Equals(ret.ToString(), "False") ? false : (object)true;
            disableVideoPlayback = (bool)ret;

            MessageBox.Show("Going to dispose of the engine", "testing", (MessageBoxButtons)1);

            window.Dispose();

	     //make new controls.
            InitRenderControl();

            window.UnderlyingPanel = new Panel { Dock = DockStyle.Fill };
            window.Controls.Add(window.UnderlyingPanel);
            window.UnderlyingPanel.Visible = false;   // tried this both true and false
            opts = new ApplicationOptions();
            opts.ExternalWindow = window.UnderlyingPanel.Handle;
            opts.DelayedStart = true;
            opts.LimitFps = false;
            opts.UseDirectX11 = true;
            opts.ResizableWindow = true;
            opts.AutoloadCoreData = true;

	     /Make new application
            application = new Urho.Application(opts);
            application.Run();
            engine = application.Engine;

            var cache = application.ResourceCache;
            var helloText = new Text()
            {
                Value = "Hello World from UrhoSharp",
                HorizontalAlignment = Urho.Gui.HorizontalAlignment.Center,
                VerticalAlignment = VerticalAlignment.Center
            };
            helloText.SetColor(new ColorEx(0f, 1f, 0f));
            helloText.SetFont(font: cache.GetFont("Fonts/Anonymous Pro.ttf"), size: 30);
            UI ui = new UI();
            ui.Root.AddChild(helloText);
            engine.RunFrame();    
            Time.Sleep(5000); //Display it for 5 seconds but nothing is displayed.

            Debugger.Break(); // forced stop in testing

            <snip>

            return true;

        }

[/code]

-------------------------

archwind | 2020-05-06 08:00:05 UTC | #2

https://youtu.be/eBDkDSIdz2Y 

is what is happening when I run it.

-------------------------

SirNate0 | 2020-05-06 12:56:00 UTC | #3

Run() is a blocking operation (in c++ at least). Either override the application class and use your own setup code and such or use RunOneFrame() and your own main loop.

-------------------------

archwind | 2020-05-06 21:31:11 UTC | #4

Thanks for the information.

At least now I know where to address this issue. I'll work on overriding the application. If that doesn't work, there are two options

Make a new application class to replace it.

or

Make the editor a loadable application and capture the render surface from the loader.

There is no reference to RunOneFrame() in UrhoSharp by the way.

-------------------------

archwind | 2020-05-08 08:42:26 UTC | #5

I’m at a loss here on what to do. Maybe UrhoSharp is designed around making a game only and not capable of expanding on the platform. The Application Class is tightly integrated into the engine’s functions.  I have traced all this into the internals on the application side. The code execution is the SAME except one is a file (The loaded application is in a render thread) and the other is from memory.

The items get passed into the internal engine but it is not executing the render process. In other words I would have to make the entire project a render thread?

When I use the application.Run() it executes what ever is sent in the program (which is nothing sine the application is a proxy application.  The return values has no errors.

 I added var results = application.Run();

The results is zero or no error.

 whereas the file executes one line at a time internally until it reaches end of file and the entire file is sent internally when the engine is initialized? The render thread uses the same functions I’m using where the application is delayed start and delay and loops through the program by using RunFram() (RunFrame() must be executing on line of code?  See below.

[code]
		public async Task<Application> Show(Type appType, ApplicationOptions opts = null)
		{
//my comments added.
//this is the setup section which is close to my code.

			paused = false;
			opts = opts ?? new ApplicationOptions();
			await Semaphore.WaitAsync();

// this section assures the application is withing the main thread.
// if execution happens outside this window the application will throw
// a unhandled exception

			if (Application.HasCurrent)
				Application.InvokeOnMain(async () => {
					if (Application.HasCurrent)
						await Application.Current.Exit();
				});

			RenderThread?.Join();

// set up the mouse callbacks

			if (UnderlyingPanel != null)
				UnderlyingPanel.MouseDown -= UrhoSurface_MouseDown;
			Controls.Clear();

//Create the underlying panel and make it invisible.
// tested it visible and it makes no difference.

			UnderlyingPanel = new Panel { Dock = DockStyle.Fill };
			UnderlyingPanel.MouseDown += UrhoSurface_MouseDown;
//add the panel to the render box.
			Controls.Add(UnderlyingPanel);
			UnderlyingPanel.Visible = false;

			opts.ExternalWindow = UnderlyingPanel.Handle;
//set to delayed start
			opts.DelayedStart = true;    
			opts.LimitFps = false;
// thread reset 
			var mre = new ManualResetEvent(false);
			Urho.Application.Started += () => { mre.Set(); };

//this is the threading section which executes each frame one line at a time;
// the application sends a delayed start and the runs frames.

			RenderThread = new Thread(_ =>
			{
				Application = Application.CreateInstance(appType, opts);
// tells engine to start execution
				Application.Run();             
				var sw = new Stopwatch();

				var engine = Application.Engine;

// tells engine to render the first frame
// the first frame is ‘hello world’ of course.

				engine.RunFrame();
             
//This is the execution loop
//tested in Gogo and it runs one loop.
//because the application is proxy and has nothing in it.
// No callbacks to frame started or frame ended.

				while (Application != null && Application.IsActive) // execute this render thread until the end of file.
				{
					if (!Paused)
					{
						sw.Restart();
						engine.RunFrame();
						sw.Stop();

						var elapsed = sw.Elapsed.TotalMilliseconds;
						var targetMax = 1000f / FpsLimit;
						if (elapsed < targetMax)
							Thread.Sleep(TimeSpan.FromMilliseconds(targetMax - elapsed));
					}
					else
					{
						Thread.Sleep(500);
					}
				}
			});

// this executes after the initial thread is created.
//start the main thread.
			RenderThread.Start();

//do manual reset on the thread.
			mre.WaitOne();
			Semaphore.Release();

//Set the underlying panel visible
			UnderlyingPanel.Visible = true;
			UnderlyingPanel.Focus();
			return Application;
		}

[/code]

I had already set the editor up for loading I removed the startup code and put in the menu to initialize the application as per the first posting so it wasn’t a big problem to build a loader however the application engine won’t allow it to load because there is a conflict with single threading and multithreading. I tried making all processes single threaded but it still won’t load. The application throws Internal error with DragDrop (even after I disabled these callbacks)

I still haven’t rewritten the application class because I don’t think it will solve this issue.

-------------------------

SirNate0 | 2020-05-08 09:30:19 UTC | #6

I'm sorry about this, but I think I may have led you wrong, though I think you probably figured out most of it on your own anyways. If you want to do your own main loop you will probably want to just skip the Application class and work with the Engine class directly.

Part of your problem may be that a large number of things in the engine can only be done from the main thread (basically, things that will require graphics API calls, maybe a few more things, if I remember this correctly).

Possibly your problem is that you called Run on the Application, and once that has finished I'm pretty sure the engine is shut down.

Note: I'm not looking at the code or the documentation at present, so take what I just said with a grain of salt (this is what went wrong the first time).

-------------------------

archwind | 2020-05-08 19:45:05 UTC | #7

It doesn’t make sense that this engine can’t render from a proxy application. It’s based on OGRE and so is Axiom. Axiom functions about the same way, in fact I’ve had to do very little modifications to get the code to execute. The only thing I have to do is assign the pointers before making calls instead of having the engine assign them and functions names are different. There are a few exception such as Axiom does not have an application class as far as I can tell.

I’m missing something simple here.  Below is the Axiom code to run the setup I have put it all in one call instead of making calls to each process now since running into the problem of displaying so this code was modified to fit the Urho library.

Entry into the form. My comments added here about the application issue and render issue. I don’t know how I can bypass the application.

[code]

        public bool Start(string[] args)
        {

            if (!Setup())
            {
                return false;
            }
            this.args = new List<string>();
            foreach (string arg in args)
            {
                this.args.Add(arg);
            }

            if (this.args.Count > 0 && File.Exists(args[0]))
            {
                LoadWorld(this.args[0]);
            }

           // start the engines rendering loop
// as long as the rendering is happening the form 
// stays active in the main internal loop. When signaled from the
// form close ‘Quit’ variable.

            engine.StartRendering(); // Urho  engine.Run()

            return true;
        }

[/code]

The setup.

[code]
        protected bool Setup()
        {
            // get a reference to the engine singleton

 // This is different here as Urho needs an Application active in order to take instructions.
 // if there is no application active then the Urho engine throws a unhandled exception when trying to
 // set call backs or create any object (scene, camera, nodes, text, engine render commands and so on).
 // I have not found a method to bypass this so I had to add in application creation. This is probably
 // where the problem is.

            engine = new Root("", "trace.txt");    // Urho  engine = new Engine(Context);
            // retrieve the max FPS, if it exists
            getMaxFPSFromRegistry();
            activeFps = Root.Instance.MaxFramesPerSecond; //Urho  activeFps = engine.MaxFps;


            // add event handlers for frame events
            engine.FrameStarted += new FrameEvent(OnFrameStarted);
            engine.FrameEnded += new FrameEvent(OnFrameEnded);

            // allow for setting up resource gathering
            SetupResources();

            object ret = Registry.GetValue(Config.WorldEditorBaseRegistryKey, "Disable Video Playback", (object)false);
            if (ret == null || String.Equals(ret.ToString(), "False"))
            {
                ret = (object)false;
            }
            else
            {
                ret = (object)true;
            }
            disableVideoPlayback = (bool)ret;

            //show the config dialog and collect options
            if (!ConfigureAxiom())
            {
                // shutting right back down
                engine.Shutdown(); // Urho  engine.Dispose()

                return false;
            }

            if (!CheckShaderCaps())
            {
                MessageBox.Show("Your graphics card does not support pixel shader 2.0 and vertex shader 2.0, which are required to run this tool.", "Graphics Card Not Supported", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
                engine.Shutdown();
                return false;
            }

            ChooseSceneManager(); //Not needed with Urho
            CreateCamera();
            CreateViewports();

            // set default mipmap level
            TextureManager.Instance.DefaultNumMipMaps = 5;

            // call the overridden CreateScene method
// Makes a default scene and displays it when the engine starts rendering.
            CreateScene();

            // setup save timer
            saveTimer.Interval = (int)autoSaveTime;
            saveTimer.Tick += new EventHandler(saveTimerEvent);
            saveTimer.Start();

            InitializeAxiomControlCallbacks();

            return true;
        }

[/code]

After the configuration is completed 

[code]
        protected bool ConfigureAxiom()
        {
            // HACK: Temporary
            RenderSystem renderSystem = Root.Instance.RenderSystems[0];
            Root.Instance.RenderSystem = renderSystem;

            bool hasMovie = false;

            if (File.Exists(".\\Multiverse.Movie.dll") && !disableVideoPlayback)
            {
                hasMovie = true;
                renderSystem.SetConfigOption("Multi-Threaded", "Yes");
                PluginManager.Instance.LoadPlugins(".", "Multiverse.Movie.dll");
            }

		// Stops the engine from rendering and sets up the render window.

            Root.Instance.Initialize(false);  

            window = Root.Instance.CreateRenderWindow("Main Window", axiomControl.Width, axiomControl.Height, false,
                                                      "externalWindow", axiomControl, "useNVPerfHUD", true,
                                                      "multiThreaded", hasMovie);

            Root.Instance.Initialize(false);

            return true;
        }

[/code]

-------------------------

archwind | 2020-05-08 23:08:44 UTC | #8

Couple things I want to add here. I checked the source and verified the following.

Was it in headless mode? NO
Is the graphics subsystem of the application initialized? YES
The run frame is working.

[code]
void Engine::RunFrame()
{
    assert(initialized_);

    // If not headless, and the graphics subsystem no longer has a window open, assume we should exit
    if (!headless_ && !GetSubsystem<Graphics>()->IsInitialized()
        exiting_ = true;

    if (exiting_)
        return;

    // Note: there is a minimal performance cost to looking up subsystems (uses a hashmap); if they would be looked up several
    // times per frame it would be better to cache the pointers
    auto* time = GetSubsystem<Time>();
    auto* input = GetSubsystem<Input>();
    auto* audio = GetSubsystem<Audio>();

#ifdef URHO3D_PROFILING
    if (EventProfiler::IsActive())
    {
        auto* eventProfiler = GetSubsystem<EventProfiler>();
        if (eventProfiler)
            eventProfiler->BeginFrame();
    }
#endif

    time->BeginFrame(timeStep_);

    // If pause when minimized -mode is in use, stop updates and audio as necessary
    if (pauseMinimized_ && input->IsMinimized())
    {
        if (audio->IsPlaying())
        {
            audio->Stop();
            audioPaused_ = true;
        }
    }
    else
    {
        // Only unpause when it was paused by the engine
        if (audioPaused_)
        {
            audio->Play();
            audioPaused_ = false;
        }

        Update();
    }

    Render();
    ApplyFrameLimit();

    time->EndFrame();
}
[/code]

I tried to initialized the console does not activate. The commands in code never reach this except when in a program.
 

[code]

Console* Engine::CreateConsole()
{
    if (headless_ || !initialized_)
        return nullptr;

    // Return existing console if possible
    auto* console = GetSubsystem<Console>();
    if (!console)
    {
        console = new Console(context_);
        context_->RegisterSubsystem(console);
    }

    return console;
}

[/code]

Never reached when sent. Except when in a program.

[code]

DebugHud* Engine::CreateDebugHud()
{
    if (headless_ || !initialized_)
        return nullptr;

    // Return existing debug HUD if possible
    auto* debugHud = GetSubsystem<DebugHud>();
    if (!debugHud)
    {
        debugHud = new DebugHud(context_);
        context_->RegisterSubsystem(debugHud);
    }

    return debugHud;
}
[/code]

I was really hoping to get this engine to work. The latest Axiom is way behind and not very active. It is still using DirectX9.

Multiverse is different engine. It has a unique paging system where the scene manager handles the world. The world is virtually endless (well it is limited to a unsigned integer of 2^32 x 2^32 tiles and each tile can be designed from 256^2 to 4096^2 points per tile). Currently it supports a two dimensional plane which can be expanded into a third dimension or cubes. The total system would then be capable of handling a cubic world of (2^32x2^32x2^32) or ‭6.2771017353866807638357894232077e+57‬ cubes.

My goal is to make it run on modern graphics.

-------------------------

JTippetts | 2020-05-09 01:05:52 UTC | #9

You're aware that UrhoSharp is a downstream project, right? It's unlikely you are going to receive any better support for it here than others have.

-------------------------

archwind | 2020-05-09 01:55:02 UTC | #10

Yeah, I'm aware it is a downstream project. I also don't think it will work anyway since it's basically made to make games. I have a choice to switch to C++ or back to Axiom. I have considered Stride(xenko).

-------------------------

George1 | 2020-05-09 05:18:30 UTC | #11

No engine can have that many cubes.
They just cheated using cache, and if you center the world around the player, then the world is endless.

-------------------------

archwind | 2020-05-09 19:09:02 UTC | #12

Actually that is how this engine works. The world is always centered around the player however there is a limitation since it is not procedurally drawn to a fixed number of tiles which by the way exceeds most hard drive capacity.

-------------------------

archwind | 2020-05-09 19:25:14 UTC | #13

I know exactly what the problem is now just don’t know how to solve it yet.

The C++ examples are opposite design of the C# samples. The C++ sample programs execute a loader that points back to the main entry whereas the C# samples use a loader to execute the sample externally by loading it as a library.

Hope that made sense.

-------------------------

adhoc99 | 2020-05-09 19:31:44 UTC | #14

Take a look at [rbfx](https://github.com/rokups/rbfx). It’s a Urho3D fork with extensive C# support.

Their Github repository has a link to their Gitter. Maybe you could ask them if it supports what you need.

-------------------------

archwind | 2020-05-09 19:55:10 UTC | #15

Thanks, I'll check it out and see if it will work.

-------------------------

