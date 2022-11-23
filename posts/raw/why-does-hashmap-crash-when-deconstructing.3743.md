SeeSoftware | 2017-11-14 21:15:49 UTC | #1

Im trying to create a new subsystem:

    class Keybinds: public Object
    {
        URHO3D_OBJECT(Keybinds, Object)

    //...

    private:
        HashMap<StringHash, Vector<int>> m_keybinds;
        HashMap<StringHash, bool> m_actionPressed;
    }

and register it with 

    context_->RegisterSubsystem(new Keybinds(context_));

in the Start() function of the application

but when i call

    engine_->Exit();

to close the application then the application crashes in the destructor of the HashMaps i defined in the SubSystem:

    ~HashMap()
    {
        Clear();
        FreeNode(Tail());
        AllocatorUninitialize(allocator_);
        delete[] ptrs_; // <-- Here !
    }

i tried multiple things but i dont know what is happening!
Can someone help me out?

compiled with Visual Studio 2017, Debug x64  Urho3D Shared

After the application crahses i get this message:

    HEAP[Minecraft Clone.exe]: Invalid address specified to RtlValidateHeap( 000002796A5C0000, 00000279714FE140 )
    Minecraft Clone.exe hat einen Haltepunkt ausgelöst.

EDIT: Wow i tried to run it in the Release build and it seems that it doenst crash anmyore, so why does it happen only in the debug build ?!

-------------------------

Eugene | 2017-11-14 21:23:21 UTC | #2

Do you use Static MSVC Runtime?

-------------------------

SeeSoftware | 2017-11-14 21:46:07 UTC | #3

Debug: Multithreaded-Debug-DLL
Release: Multithreaded-DLL

i changed it to Multithreaded-Debug and it fixed it but is there a reason you need a static runtime?

EDIT: i dont know what is happening it seems to allways change. i like switched back and forth with the configurations and then completely rebuild the whole project but now it doenst work anymore on any debug runtime. I created a console with

	AllocConsole();
	#pragma warning(disable:4996)
	freopen("CONOUT$", "w", stdout);

and when switching the configurations sometimes the log (the log you would find in the log file) will appear in the console and sometimes not.

-------------------------

Eugene | 2017-11-14 22:41:16 UTC | #4

The simplest way is to just link Urho statically (I mean Urho library, regardless of runtime). I'm 99% sure it will work perfectly.

-------------------------

SeeSoftware | 2017-11-19 13:27:56 UTC | #5

Ok turns out i cant use the Release build of urho3d for my debug application its works perfectly now!

-------------------------

