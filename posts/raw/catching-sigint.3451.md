TheComet | 2017-08-15 21:22:56 UTC | #1

Is there an API to react to signals? It looks like Urho3D already catches SIGINT and ignores it. I'd like to change it so it calls ```engine_->Exit()``` instead.

-------------------------

TheComet | 2017-08-15 21:31:11 UTC | #2

I have tried listening to E_EXITREQUESTED but it doesn't get triggered when I CTRL-C

-------------------------

slapin | 2017-08-15 22:41:14 UTC | #3

engine_exit soesn't work this way - it doesn't guarabtee exit.
So on Ctrl-C I'd use some different logic.

-------------------------

TheComet | 2017-08-16 13:08:28 UTC | #4

That doesn't answer question at all.

Ctrl-C does nothing when I start my game in headless mode, it just gets ignored.

What I assume should happen is the SDL_QUIT event should be generated when SIGINT is received, which in turn is handled by Urho3D in Input.cpp and propagated with the E_EXITREQUESTED event. But it doesn't.

-------------------------

cadaver | 2017-08-16 14:49:57 UTC | #5

On Windows / VS2013, I see SDL to not compile in its signal handling code at all, due to HAVE_SIGNAL_H being false. Though that may be just an oddity due to the specific machine & compiler I'm currently testing on.

Urho itself shouldn't have signal handlers.

-------------------------

slapin | 2017-08-16 19:47:12 UTC | #6

I think on windows you should use native code.
For Linux one can just trap SIGINT and do SDL_Quit from there. Actually Ctr^C on Linux works only when
frame handling code is running. If you run something huge from Start() you have to kill -15 to interrupt.

-------------------------

TheComet | 2017-08-16 23:36:18 UTC | #7

I ended up writing wrappers to abstract signal handling, and then wrote a component that sends the E_EXITREQUESTED event on top of that.

I'm not sure whether it's a bug or not that Urho3D doesn't allow you to CTRL-C to quit (on linux). Is this something that needs reporting @cadavar?

Here's my code in case someone comes along in the future:

**signals.h** (platform independent header):

    #pragma once

    #ifdef __cplusplus
    extern "C" {
    #endif

    void signals_register(void);
    int signals_exit_requested(void);

    #ifdef __cplusplus
    }
    #endif

**signals_linux.c** (platform dependent implementation, I wrote one for each platform):

    #include "signals.h"
    #include <signal.h>

    static volatile int g_exit_requested = 0;

    // ----------------------------------------------------------------------------
    static void sig_handler(int signum)
    {
        if (signum == SIGINT)
        {
            g_exit_requested = 1;
        }
    }

    // ----------------------------------------------------------------------------
    void signals_register(void)
    {
        signal(SIGINT, sig_handler);
    }

    // ----------------------------------------------------------------------------
    int signals_exit_requested(void)
    {
        return g_exit_requested;
    }

**SignalHandler.h/cpp** (Register this as a subsystem during Setup() to have E_EXITREQUESTED sent in response to a CTRL-C)

    class SignalHandler : public Urho3D::Object
    {
        URHO3D_OBJECT(SignalHandler, Urho3D::Object);

    public:
        SignalHandler(Urho3D::Context* context);

    private:
        void HandleUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
    };

    // ----------------------------------------------------------------------------
    SignalHandler::SignalHandler(Context* context) :
        Object(context)
    {
        signals_register();
        SubscribeToEvent(E_UPDATE, URHO3D_HANDLER(SignalHandler, HandleUpdate));
    }

    // ----------------------------------------------------------------------------
    void SignalHandler::HandleUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData)
    {
        if (signals_exit_requested())
        {
            URHO3D_LOGINFO("Signal caught, sending exit request");
            SendEvent(E_EXITREQUESTED);
        }
    }

-------------------------

cadaver | 2017-08-17 07:49:27 UTC | #8

In a headless application like NinjaSnowWar server, it may be due to the console input reading happening differently. On Windows I get Ctrl-C. Platform-different behavior like that could be considered a bug so feel free to make an issue.

-------------------------

weitjong | 2017-08-17 14:56:24 UTC | #9

Have you tried to compile a vanilla SDL app on Linux and see how it behaves?

-------------------------

weitjong | 2017-08-18 02:42:35 UTC | #10

The reason I asked because I just got time to test below using Urho3D app. As you may already know SDL detects sigaction availability during CMake configuration as it prefers sigaction over signal. In the debug build config, I could see the sigaction handler being initialized correctly, which should capture the SIGINT and SIGTERM. In the handler it inserts an SDL_QUIT event into its internal event queue. However, setting a breakpoint in the signal handler itself showed that it was not triggered upon CTRL-C being pressed. So something is definitely fishy on the SDL side and hence the question.

-------------------------

slapin | 2017-08-18 00:10:32 UTC | #11

btw, is there some terminal group detachment code somewhere? this detaches from signals generated by
tty.

-------------------------

weitjong | 2017-09-04 23:40:40 UTC | #12

I have retested this again. Running NinjaSnowWar (with unaltered Urho engine) I could see the "Urho3DPlayer" process in my `ps` command output. Although pressing CTRL-C on the NSW itself did not killed it, sending the kill signal to the process using `skill Urho3DPlayer` or `kill` _process-id_ did the trick. Pressing CTRL-C only works on the launching console window (if any).

-------------------------

slapin | 2017-09-14 00:37:35 UTC | #13

Well, the issue is that i doesn't work on running console in some circumstances (no frame code like Update/Fixed update running, doing something heavy in Start) which is a bit not nice (manageable but ability to ^C improves workflow).
Redeclaring own signal handler fixes the problem.

-------------------------

