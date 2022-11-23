umen | 2017-01-02 00:58:50 UTC | #1

Hello all
sorry for the threads I'm posting , i just starting to work with the engine and i try to figure things out .
2 questions about logging 
1. when i deploy to iOS in max using xcode5.1 , where is the logging file is written , i can't find is any where , 
2 .also which macro should i use to see logging massages in Xcode output window and in to file 
now if i try to print like this :
[code]LOGERRORF("input->GetNumTouches(): %d",input->GetNumTouches());[/code]

i can't find the file under urho3d directory , and in the Xcode 5.1 output windows i got : (lldb)

-------------------------

cadaver | 2017-01-02 00:58:50 UTC | #2

Android / iOS do not currently write a log file anywhere to avoid requiring file write permissions. An iOS debug build should output to the XCode console, but doing this in a final build would cause App Store rejection, so release builds won't output anything.

-------------------------

umen | 2017-01-02 00:58:50 UTC | #3

Thanks for the fast replay , so whice log macro should I use to out put to console only?

-------------------------

cadaver | 2017-01-02 00:58:50 UTC | #4

Any log macro should work. 

If you're not seeing any output even in debug mode, check the function SDL_IOS_LogMessage(const char *message) in Source/ThirdParty/SDL/src/video/uikit/UIKitAppDelegate.m. That's a custom function that has been added to SDL for Urho3D use.

-------------------------

