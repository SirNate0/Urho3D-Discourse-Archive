xDarkShadowKnightx | 2017-01-02 01:00:00 UTC | #1

Hello! 

I'm having trouble getting output to show in the terminal when running Urho3DPlayer from the terminal/command prompt in Windows (Windows 8.1 to be exact). It seems that its just creating the application window (but not staying attached to the terminal window). Linux stays attached to the terminal when you run the player from a terminal though. Is there anyway to do this in windows? I want to be able to run a headless server, but still see messages and stuff (for when it crashes, or when I call Print in my scripts)

Thank you for any help

-------------------------

cadaver | 2017-01-02 01:00:00 UTC | #2

Urho Windows applications don't use the console subsystem, so they don't attach to a console window.

You can use the OpenConsoleWindow() function to open a separate window to which stdout / stderr prints will appear. Alternatively you can comment out (add # symbol) line 576 from Source/CMake/Modules/Urho3D-CMake-common.cmake to make applications use the console subsystem:

[code]
            set (EXE_TYPE WIN32)
[/code]

-------------------------

xDarkShadowKnightx | 2017-01-02 01:00:00 UTC | #3

Awesome, this worked. I don't see why this isn't default/consistent across all platforms though. But I appreciate the help!

-------------------------

weitjong | 2017-01-02 01:00:02 UTC | #4

We can make this configurable, if we really want it. However, it is harder to say that using main (console) instead of WinMain as entry point is the best default setting for Windows platform.

BTW, welcome to our forum!

-------------------------

cadaver | 2017-01-02 01:00:02 UTC | #5

Using the AttachConsole() function could also be possible, but it doesn't work flawlessly:

[stackoverflow.com/questions/7072 ... achconsole](http://stackoverflow.com/questions/7072893/the-problem-of-attachconsole)

-------------------------

friesencr | 2017-01-02 01:00:02 UTC | #6

Something I have done in the past is to download the gnuwintools for windows and tailed the log file.  It sucks but so does the windows terminal :frowning:

-------------------------

JeriX | 2017-01-02 01:00:28 UTC | #7

I just can't get it to work :frowning: 
[code]
void App::Setup()
{
    engineParameters_["LogQuiet"] = false;
    OpenConsoleWindow();
}
[/code]
[code]
    LOGINFO("test log message");
    PrintUnicodeLine("test print message");
[/code]
Console window appears but it's blank.
I use mingw for compilation for Windows 7.
Am I missing something?

-------------------------

JeriX | 2017-01-02 01:00:29 UTC | #8

I've figured this out. My bad!
I use Qt Creator for development and it seems this IDE somehow mixes standart outputs when launching from it. When I launch exe in system by myself everything is normal

-------------------------

