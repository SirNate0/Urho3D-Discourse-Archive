capelenglish | 2018-05-25 15:37:31 UTC | #1

When I run the samples, it creates a log file in my AppData/Roaming/urho3d/logs folder on my PC. I'm trying to figure out how to write to this log file as I play with the samples. Is there an example somewhere? I can't seem to find one or any beginner discussion on the topic.

-------------------------

TheComet | 2018-05-25 16:27:12 UTC | #2

In your Application::Setup() function you can specify as one of the engine parameters where you want Urho3D to write the log:

    MyApplication::Setup()
    {
        engineParameters_[EP_LOG_NAME] = GetSubsystem<FileSystem>()->GetAppPreferencesDir("urho3d", "logs") + GetTypeName() + ".log";
    }

The normal log macros, e.g. URHO3D_LOGINFO() found in Urho3D/IO/Log.h will then write to this location.

-------------------------

capelenglish | 2018-05-25 17:48:57 UTC | #3

Thanks. 

When I use URHO3D_LOGINFO(), it logs a couple of messages and then the logging just stops. It's not obvious to me why. Any suggestions?

-------------------------

TheComet | 2018-05-25 18:20:12 UTC | #4

Can you verify that URHO3D_LOGINFO() is actually getting called?

if so, then a possible explanation is the messages are getting buffered (which honestly shouldn't be the case with loggers, but you never know)

-------------------------

capelenglish | 2018-05-25 18:36:50 UTC | #5

If I set a breakpoint on the first call and step into it, it goes through str.h and then log.cpp. If I set a breakpoint on the second call and step into it, it goes through str.h, but not log.cpp. Seems odd...

-------------------------

jmiller | 2018-05-25 22:08:59 UTC | #6

A long shot: myself and at least one other have noticed Urho3D::Log*() being ignored when called repeatedly/unconditionally during fast update events like E_UPDATE. I was curious if this was an intentional throttle mechanism, or perhaps due to some user error, but I do not generally want to write a line every frame (instead using DebugHud) so I did not follow up.

-------------------------

capelenglish | 2018-05-29 11:18:43 UTC | #7

That's interesting. I don't want to write to the log every frame. I just wanted to write to the log during start-up.

-------------------------

jmiller | 2018-05-29 18:58:43 UTC | #8

[quote="capelenglish, post:3, topic:4264"]
When I use URHO3D_LOGINFO(), it logs a couple of messages and then the logging just stops.
[/quote]
Meaning that a couple of your calls do get logged properly? and if so, when are they called, exactly?

Don't know if this is any help but the Log subsystem is normally only opened by Engine::Initialize(), so I do it earlier at the begin of Application::Setup():

[code]
using namespace Urho3D;

void App::Setup() {
  const Vector<String>& args(GetArguments());

  engineParameters_[EP_LOG_NAME] = /* @TODO GetSubsystem<FileSystem>()->GetAppPreferencesDir("urho3d", "logs") + */ GetTypeName() + ".log";

  // Open log now, even though Engine::Initialize() will do it again.
  Log* log(GetSubsystem<Log>());
  log->Open(engineParameters_[EP_LOG_NAME].GetString());
  log->SetLevel(LOG_INFO);
[/code]

-------------------------

capelenglish | 2018-05-29 19:05:52 UTC | #9

@jmiller That did it. Thanks for your help.

-------------------------

