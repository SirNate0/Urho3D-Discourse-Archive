archwind | 2020-05-02 04:19:27 UTC | #1

I changed start of the application to a delayed start and now it won't render even when I restart it with new opts.

How does it work? I do not have start, stop and resume functions in UrhoSharp.

-------------------------

throwawayerino | 2020-05-02 12:50:55 UTC | #2

Delayed start is for components, it delays starting components until the scene is done so that you get to avoid race conditions. Obviously you cant have a delayed start if the application never starts at all!

-------------------------

archwind | 2020-05-05 00:32:32 UTC | #3

After a lot of testing and tracing code, it is doing exactly what I want it to do. :blush:

-------------------------

