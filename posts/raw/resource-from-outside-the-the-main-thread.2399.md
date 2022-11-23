sabotage3d | 2017-01-02 01:15:12 UTC | #1

Hi,
I have a callback form Android that returns a filepath. After that it passes the filepath to an Image.
[code] Image* image = cache->GetResource<Image>(filepath);[/code]

But I am getting a crash with this error:
[code]Attempted to get resource /storage/test.jpg from outside the main thread[/code]

-------------------------

Sir_Nate | 2017-01-02 01:15:12 UTC | #2

See if GetTempResource would work for your situation. Otherwise, you will probably have to create some sort of thread-safe queuing mechanism to store these strings so that you can process them in the main thread.

-------------------------

