Mike | 2017-01-02 00:57:53 UTC | #1

Writing in resource cache is currently prohibited on Android:

In /Engine/IO/File.cpp :

[code]
        if (mode != FILE_READ)
        {
            LOGERROR("Only read mode is supported for asset files");
            return false;
        }
[/code]
If we comment these lines, writing becomes available.
We can for example save and load scenes like on desktop.
So I am wondering why writing is not allowed. Is it unsafe...?

-------------------------

cadaver | 2017-01-02 00:57:54 UTC | #2

SDL does not implement writing to the APK, you should get an error if you try it. If you think about it, you shouldn't be modifying the installed package of an Android app.

Rather, use FileSystem::GetUserDocumentsDir() to get a writable directory that's guaranteed on all systems.

-------------------------

Mike | 2017-01-02 00:57:54 UTC | #3

Awesome, works perfectly! Many thanks  :mrgreen: 

Note: I get no error when writing to the cache and loading back saved data (tried with an xml scene).
But it's definitely safer to use GetUserDocumentsDir.

-------------------------

