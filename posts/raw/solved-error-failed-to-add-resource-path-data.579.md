danieru | 2017-01-02 01:01:30 UTC | #1

Hello everyone,

I'm trying to compile the 01_HelloWorld sample code with: [code]g++ -o HelloWorld HelloWorld.cpp `pkg-config --cflags --libs Urho3D`[/code] 

But at run time says:
[quote]
[Mon Nov 24 18:01:59 2014] INFO: Opened log file /home/bran/.local/share/urho3d/logs/HelloWorld.log
[Mon Nov 24 18:01:59 2014] INFO: Created 3 worker threads
[Mon Nov 24 18:01:59 2014] ERROR: Failed to add resource path Data
[/quote]

I installed Urho3D using a deb package " Urho3D-1.32-Linux-64bit-STATIC.deb ", and had to change the prefix in " /usr/lib/pkgconfig/Urho3D.pc " from " /usr/local " to " /usr ".

-------------------------

weitjong | 2017-01-02 01:01:30 UTC | #2

Welcome to our forum.

All the Urho executables (regardless of how they are being compiled and linked) need the CoreData and Data subdirs in order to execute them successfully.

-------------------------

weitjong | 2017-01-02 01:01:30 UTC | #3

[quote="danieru"]I installed Urho3D using a deb package " Urho3D-1.32-Linux-64bit-STATIC.deb ", and had to change the prefix in " /usr/lib/pkgconfig/Urho3D.pc " from " /usr/local " to " /usr ".[/quote]
Are you saying the deb package get installed to the /usr instead of /usr/local by default? If that is the case, we may have to actually set the pkgconfig to defaulted to /usr as well.

-------------------------

danieru | 2017-01-02 01:01:30 UTC | #4

Thank you weitjong for your help and fast reply, I'm really excited to start using this engine :smiley:

[quote]All the Urho executables (regardless of how they are being compiled and linked) need the CoreData and Data subdirs in order to execute them successfully.[/quote]
I see, the directories at " /usr/share/Urho3D ". Actually, I could've known that if I was paying more attention, but it was not the case at the early morning :unamused:
Anyway... Thanks! That solved the problem.

[quote]Are you saying the deb package get installed to the /usr instead of /usr/local by default? If that is the case, we may have to actually set the pkgconfig to defaulted to /usr as well.[/quote]
Yes, all the files was at " /usr " by default, but " Urho3D.pc " pointed to " /usr/local ". It was installed in Trisquel 7 (Ubuntu 14.04) BTW.

-------------------------

weitjong | 2017-01-02 01:01:30 UTC | #5

On the second thought, I have decided to to change the default RPM and DEB installation directory to /usr/local instead of the other way around.

-------------------------

