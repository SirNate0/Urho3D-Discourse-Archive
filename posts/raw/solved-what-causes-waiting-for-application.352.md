friesencr | 2017-01-02 00:59:49 UTC | #1

What causes an application, while doing some intense processing, to pop a dialog and say that the application may not be responding?  How do you prevent from happening.  In this case I am loading up a bunch of custom geometries.  I am having a hard time knowing what to call this and can't really find information on it because of it.

Thanks :smiley:

-------------------------

jmiller | 2017-01-02 00:59:49 UTC | #2

It seems that could be a [b]Desktop Window Manager[/b] "feature".
You can kill dwm.exe or stop the service, but will lose "desktop composition" - transparency etc.
I don't care for the popup either. Maybe there's a specific setting for that, but I kinda doubt it..

-------------------------

weitjong | 2017-01-02 00:59:49 UTC | #3

[quote="friesencr"]I am having a hard time knowing what to call this and can't really find information on it because of it.[/quote]

How about "hang" or "freeze"? At least it appears to be in that state to the operating system, so it pops the warning. Probably your app does not yield enough.

-------------------------

cadaver | 2017-01-02 00:59:49 UTC | #4

I would assume this is when the main thread is doing a long continuous processing and doesn't pump window messages, which causes Windows to think the program is unresponsive. A typical solution would be to do the heavy processing in another thread and let the main thread stay pumping events normally. Unfortunately this is not really applicable to CustomGeometries as they're not safe to create from other threads, so what comes to mind next is to have a timer and break the operation if "enough" time is passed, and continue on the next frame.

-------------------------

friesencr | 2017-01-02 00:59:50 UTC | #5

I ended up rewriting the iterator to hold its state so it could resume like you all suggested.  The solution is straight forward and only slightly annoying.  The more annoying thing is how often it seems that I have to over engineer everything I am working on.  A precarious pattern  :confused: 

Thank you.

-------------------------

