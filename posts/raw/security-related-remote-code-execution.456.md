weitjong | 2019-01-15 16:22:13 UTC | #1

I have been updating all my VMs to apply the fix for the bash bug (shellshock) for the past few hours. While performing this, it got me to think about the security on Urho3D, especially on the possibility of remote code execution. The bad news is, I do believe that inherently our networking code does have such loop hole to allow arbitrary code execution from a client to a server, and vice versa. I have also managed to create a proof of concept for that using networking sample 17_SceneReplication to execute arbitrary command. There are two things that make it possible:


1) Remote event.
Although the documentation warns that for safety reason the allowed (incoming) remote event types must be first registered, the default behavior of the networking code does exactly the opposite for the sake of convenience. When none of the remote event types are registered then it implies nobody cares and it allows all remote events to be processed.
2) Console command event.
The console command is intended to be sent and handled locally ONLY, however, currently nothing stopping user to send that event type remotely. So, a client could easily just prepare any command string in the event data and even to choose whether to interpret the string by using command line shell or by one of the scripting subsystems, then send the console event to be executed on the remote server. The payload could potentially instruct the server to broadcast more harmful commands on other connected clients.  

I think we should definitely do something about it. Reject all incoming remote event types when none are registered. Add an event type blacklist instance variable which lists out local event type that should never ever be processed as remote event. Anymore ideas on how to mitigate this?

-------------------------

friesencr | 2017-01-02 01:00:34 UTC | #2

Angel script has the notion of a mask.  The context of the app sets the mask and when each method is run it validates against that mask.  The concept could extend to c/lua. Io and shell commands would be something to mask out.

-------------------------

weitjong | 2017-01-02 01:00:34 UTC | #3

I haven't checked how AngelScript masking works but to have a bit mask on the event type sounds like a good idea such as an event type could have just the 'local' bit set or the 'remote' bit set or both bits set. The bitwise operation should be faster than checking against the blacklist as I proposed earlier.

BTW, it appears that the "bash bug" also in a way hits my Windows 7 virtual machine. Originally I thought it should be just limited to my Linux and Mac systems. I am using a command line version of git client from git-scm.com on my Win7 VM. Their latest version 1.9.4 (released about 1 month ago) still ships with the vulnerable bash.

-------------------------

thebluefish | 2017-01-02 01:00:34 UTC | #4

I agree, this is dangerous to include as a default. Anyone who's working with Networking could potentially allow intruders the instant they begin accepting connections. I believe we should, by default, set to reject all unregistered events. A developer should have a way of overriding this, but I think a default of safety-first is the better approach before someone develops a commercial game and gets hit.

I'm not too concerned for those who take the necessary precautions, though. However I wonder how the engine handles specially crafted network messages, is there some other vulnerability if we start messing with raw network data?

However outside of registering events, just remember to sanitize your inputs :p It's not enough to simply assume that a field exists or even contains the data you're expecting. Make sure to check each parameter before doing anything with it can prevent odd or potentially crippling behavior.

-------------------------

cadaver | 2017-01-02 01:00:34 UTC | #5

I committed remote event mandatory registration and a fixed blacklist of events in Network.cpp you can never allow (eg. ConsoleCommand). The blacklist can be added to, I just added obvious cases (core, network, input, io events)

-------------------------

thebluefish | 2017-01-02 01:00:35 UTC | #6

[quote="cadaver"]I committed remote event mandatory registration and a fixed blacklist of events in Network.cpp you can never allow (eg. ConsoleCommand). The blacklist can be added to, I just added obvious cases (core, network, input, io events)[/quote]

I just updated my copy of Urho3D. So on my gameclient I call:

[code]
network->RegisterRemoteEvent(E_SERVER_LOGINSTATUS);
[/code]

Later on in my server, I call:

[code]
connection->SendRemoteEvent(E_SERVER_LOGINSTATUS, true, map);
[/code]

Yet on my client, I get the error message:
[quote]
WARNING: Discarding not allowed remote event 5C9CF278
[/quote]

I debug it and can verify that E_SERVER_LOGINSTATUS = 1553789560 aka 5C9CF278. I verify that the events are registered before it is called by the server. What's happening here?

-------------------------

cadaver | 2017-01-02 01:00:35 UTC | #7

Hard to know what is going on without seeing all the code. If you run the 17_SceneReplication C++ sample, does that work? If you compare your code to that, is the sequence different? Do you get the "Attempted to register blacklisted remote event type" log message, which would imply a clash with the existing event types?

-------------------------

thebluefish | 2017-01-02 01:00:35 UTC | #8

Huh, that was weird. On this machine (my home machine), I pulled down the latest build of Urho3D, compiled it, and everything's working fine. There must be some build issues that I can't figure out on my work machine. Might have also missed something entirely, long hours at work means my head isn't working right  :laughing:

-------------------------

