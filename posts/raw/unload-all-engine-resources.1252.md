XGundam05 | 2017-01-02 01:06:24 UTC | #1

Is it possible to unload all resources being used by the engine and then reload them?

Basically, I'm evaluating using Urho to write a front-end for the Pi 2. When a user would go to launch an application (e.g. a game), the system would need to minimize the memory being used by the front-end, run the application using a blocking call, and then reload the system resources when the other application exited.

I would like to use Urho for the front-end as it will be a 3d interface instead of the typical 2d-style interface in use by most system front-ends.

-------------------------

1vanK | 2017-01-02 01:06:24 UTC | #2

cache->ReleaseAllResources()
GetResource() reload it if necessary

-------------------------

XGundam05 | 2017-01-02 01:06:24 UTC | #3

Thanks :slight_smile: I really should just read the documentation more, huh. [i]I've spent too many years being spoiled by Intellisense >.>[/i]

-------------------------

