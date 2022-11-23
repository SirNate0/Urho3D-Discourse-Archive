Lichi | 2017-01-02 01:01:31 UTC | #1

Hi, i need help. I tried to compile the hello world in c ++ but when i run the .exe, the program crash.
These are the steps that I follow (use CodeBlocks and mingw):
1) Add HelloWorld.cpp, HelloWorld.h and Sample.h to the project.
2) Add the include and lib folder to settings.
3) Compile.
PS: sorry for my english.
Thanks :slight_smile:

[quote]The problem was that I was using the mingw of codeblocks, using mingw64 worked :slight_smile:[/quote]

-------------------------

hdunderscore | 2017-01-02 01:01:32 UTC | #2

You also need the CoreData and Data directories for the samples. You will probably see in the log files that there was issues finding the resourcces.

-------------------------

Lichi | 2017-01-02 01:01:32 UTC | #3

[quote="hd_"]You also need the CoreData and Data directories for the samples. You will probably see in the log files that there was issues finding the resourcces.[/quote]
Thanks for responding.

After copying the folders and also Urho3D.dll when I run the program, it loads a while and nothing happens, but in the task manager you can see the "HelloWorld.exe" process.
There is something in the settings need to change?
PS: in type of application select "GUI Application" also probe with "Console Application"

-------------------------

