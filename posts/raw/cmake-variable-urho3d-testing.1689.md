atai | 2017-01-02 01:09:29 UTC | #1

Using the default way of building and turning on testing support (as I may want to run the tests to ensure things are working well), on GNU/Linux (Fedora or Ubuntu) the following are the settings as seen in CMakeCache.txt in the build tree:

//Enable testing support
URHO3D_TESTING:BOOL=1


Using the "normal" way of including the build tree my own project  via setting URHO3D_HOME to point to the build tree, the variable  URHO3D_TESTING is set to 0 in my project build tree.  This creates a situtation that the Urho3d library has the struct layout including some optional fields only present with TESTING set, but in my application code including the Urho3d headers these testing-only fields are absent.  
example:

/// Urho3D engine. Creates the other subsystems.
class URHO3D_API Engine : public Object
{
...
#ifdef URHO3D_TESTING
    /// Time out counter for testing.
    long long timeOut_;
#endif
...
};

Then my project will still link, but there would be memory write errors that access the structs from the libraries but the structs are actually different in sizes! And thus memory corruption error.

This seems a dangerous risk for people to watch out.

Maybe it is better to have the all the struct fields present regardless of the TESTING is turned on or off, to avoid such risks?

-------------------------

weitjong | 2017-01-02 01:09:30 UTC | #2

Thanks for highlighting this. In the beginning our documentation for using Urho3D as external library has stated that one needs to pass similar build options to the downstream project when configuring its build tree. But later we have updated the doc to loosen up this restriction. Instead of wasting the space just to keep the structure the same size, I think we can just bake this URHO3D_TESTING build option in the export header. Will do that when I am free later, unless someone else beats me to it.

-------------------------

weitjong | 2017-01-02 01:09:31 UTC | #3

The change is already in the master branch.

-------------------------

atai | 2017-01-02 01:09:32 UTC | #4

Thank you.

-------------------------

