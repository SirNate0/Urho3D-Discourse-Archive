QBkGames | 2019-06-19 10:12:24 UTC | #1

![DebugHud%20Profiler|690x388](upload://zbVxFBEAO6OayA6r2lAU1YOutZ2.jpeg) 

It looks like the Profiler is showing a very high timing value for the RenderUI (which is definitely not right for a simple UI such as this), and 0 for ApplyFrameLimit. Is is possible the that idle time that should show under ApplyFrameLimit, is getting accumulated under RenderUI by mistake?

-------------------------

Leith | 2019-06-19 10:52:39 UTC | #2

The UI render time also considers the cost of the debug UI, being rendered per frame. I can't begin to interpret the UI render time, but I can stop it happening by only drawing what I need, and avoiding complex UI elements like graphs.

-------------------------

QBkGames | 2019-06-20 13:33:16 UTC | #3

The profiler shown in this thread: https://discourse.urho3d.io/t/profiler-rework-and-profiling-tool/2726 has more realistic values, 0.48 ms for UI rendering and 11.9 ms for applying frame limiting.

https://cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/221c99ba40e3ad5a03ddf9add16ee494100bf395.png

That's what the Urho profiler should show.

-------------------------

weitjong | 2019-06-20 13:44:01 UTC | #4

Have you narrowed it down to what could be the cause of the difference?

-------------------------

QBkGames | 2019-06-21 02:29:04 UTC | #5

I figured out the problem, it looks like if you set the VSync flag on, the ApplyFrameLimit profiling always shows 0. Which is technically correct, however in practice it's not very useful, since you want to see how much spare frame time you have left before the frame is presented.
IMO a more useful metric would be if the ApplyFrameLimit, was called something like "FrameSpareTime" and it started measuring the time just before the call to Graphics::EndFrame. So, if I have a game that I want to run at 60fps, and I want to know how much spare frame time I have to determine if it's worth my trouble to be spending weeks/months implementing some extra effects. If I only have 2 ms left, I might not bother but if I have a spare 10 ms left then I can definitely try to do more with it.
Looking that my sample above, I'm quite sure that my frame only takes about 2-3 ms to update/render (including the UI), and about 14 ms is spare time, but the Profiler is not showing me that.

-------------------------

QBkGames | 2019-06-21 02:39:33 UTC | #6

You can still think of V-Sync as applying a frame limit, it's just done by the graphics hardware rather than by the engine, so that timing should still be profiled separately, it just feels wrong to show it under the UI Render timing (as it's not really UI render time, it's something else).

-------------------------

Sinoid | 2019-06-21 06:54:30 UTC | #8

@Leith, having written both official and homebrew Nintendo 3ds ports of Urho3D, I assert that everything you've said is false on even the tightly resource constrained 3ds platform and thus as false can be.

This is likely an instrumenting error. Because of how Urho batches 2d UI drawing it's almost inconceivable that 2d drawing would be a real issue. Possibly some compatibility triggers or the user named his output file poorly and his video drivers are doing some nonsense for an exe they think is Doom3 or such.

Regardless, he's getting different timings out of different instrumenting methods. That indicates the instruments have issues.

-------------------------

