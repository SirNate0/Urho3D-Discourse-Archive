Elendil | 2017-12-21 18:28:25 UTC | #1

I want force OpenGL 2.
in documentation 
|void |SetForceGL2 (bool enable)|
|---|---|
| |Set forced use of OpenGL 2 even if OpenGL 3 is available. Must be called before setting the screen mode for the first time. Default false. No effect on Direct3D9 & 11.|

If I call SetForceGL2 inside setup before screen mode (as I guess it is here), program crash.
if I use
`GetSubsystem<Graphics>()->SetForceGL2(true);` inside void Start() function. _(If I add it in setup() or initial class function MyApp(){}, it compile without problem but after run program it crash.)_
Program don't crash, but I am not sure if OpenGL 2 is set up.
It is right what I am doing?

-------------------------

JTippetts | 2017-12-21 21:28:52 UTC | #2

If you're using Engine (which I recommend, as it's a pain to do everything that Engine does yourself, and with no real benefit) then you don't need to call SetForceGL2() explicitly. Just pass the flag into Engine::Initialize as one of the parameters. Engine::Initialize will call it at the proper time if needed.

-------------------------

Elendil | 2017-12-23 10:23:17 UTC | #3

Thanks, but to be sure I do it correctly
I add inside 
>     virtual void Setup()
>     {
>     	engineParameters_[EP_FORCE_GL2] = true;
>     }

it is right?

-------------------------

Modanung | 2017-12-23 16:34:24 UTC | #4

Yes, that seems correct. Any luck?

-------------------------

