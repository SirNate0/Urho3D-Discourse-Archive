Enhex | 2017-01-02 01:12:05 UTC | #1

Does Urho provide support for sandboxed scripting for security?
For example restricting file access (read/write/delete) to a paths provided by the application.

-------------------------

weitjong | 2017-01-02 01:12:05 UTC | #2

Yes, I think so and it is not just limited to scripting API, i.e. when the feature is turned on then it is also applicable for C++ API. See if FileSystem::RegisterPath() and FileSystem::CheckAccess() are what you are looking for.

-------------------------

Enhex | 2017-01-02 01:12:05 UTC | #3

What if some malicious script downloads a file using HTTP request and saves it to allowed path, can it execute it, or do something harmful with it?

EDIT:
I see that FileSystem::SystemCommand() and the other system command functions checks if there's paths restriction, that's the only way to execute something via script?

-------------------------

cadaver | 2017-01-02 01:12:05 UTC | #4

It's always possible for a script to lock up or crash the game client, simply by allocating endlessly memory or running an endless loop. Executing anything should be prevented by the FileSystem checks. Though you should audit the code yourself; while the execution restrictions are there, this code has not been tested much.

-------------------------

