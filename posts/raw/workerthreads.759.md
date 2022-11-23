OvermindDL1 | 2017-01-02 01:02:43 UTC | #1

Is there any reason that WorkerThread is a boolean instead of an unsigned integer?  I would love to be able to control this a little more.  Perhaps test if it is set, see if number and if so then use it as-is else use it as a boolean else fall back to defaults?
[code] // In Source/Urho3D/Engine/Engine.cpp:190
unsigned numThreads = GetParameter(parameters, "WorkerThreads", true).GetBool() ? GetNumPhysicalCPUs() - 1 : 0;
[/code]

-------------------------

cadaver | 2017-01-02 01:02:43 UTC | #2

The system is supposed to automatically determine the optimal amount of worker threads from the amount of physical processors. You could submit a pull request that changes the behavior to more configurable, if you want.

-------------------------

