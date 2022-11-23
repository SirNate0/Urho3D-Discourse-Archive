I3DB | 2018-12-19 23:31:06 UTC | #1

Is there a good pattern for raycast, so a node only gets raycasted once per some time period, say for 3 or 5 seconds?

In particular a pattern using only Urho library calls?

What I've been doing is using a background task to throw away repeated raycasts to the same node, but the code is tightly bound to the underlying operating system, and have been calling Octree.RaycastSingle in the Update method.

So just wondering if there is an Urho way to do it without going to the underlying OS for coding up raycasts.

-------------------------

rku | 2018-12-19 09:05:40 UTC | #2

Subscribe to `E_UPDATE` and do work there. Make a `Timer` object and check elapsed milliseconds on each call. When more than 5s have passed - do raycast and reset timer.

-------------------------

I3DB | 2018-12-19 15:56:24 UTC | #3

Yes, that will limit the raycasting to once every 5 seconds.

But I'd like to be able to raycast different objects, sometimes several objects per second. But don't want any object to be raycasted twice within the five seconds. When I code up the detection on each new object/node, the code is not so clean.

Currently just holding onto a list of raycasted objects and verifying the list.

But what I was hoping for is some flag on the nodes (like a dirty flag) that the Update routine can quickly check to know the object is already raycasted.

Being rather new to Urho and not really a game developer, some of the gaming concepts embedded into Urho's objects are still unfamiliar. So thought I'd throw out this question to find if there is some specific mechanism built into the engine that can be used, much like a dirty flag, say an IsRaycasted flag on the Node, a threadsafe IsRaycasted.

-------------------------

Dave82 | 2018-12-19 18:29:54 UTC | #4

[quote="I3DB, post:3, topic:4756"]
But I’d like to be able to raycast different objects, sometimes several objects per second. But don’t want any object to be raycasted twice within the five seconds
[/quote]
Why not just set viewMask or collisionMask ?

-------------------------

I3DB | 2018-12-19 19:12:41 UTC | #5

Found this sample code: 
https://github.com/xamarin/urho-samples/blob/b72d055a424d0e6be825c0239683c225d29ee723/HoloLens/05_Physics/Progam.cs#L53

So it does look like it will work, but haven't tried dynamically changing it on an existing node. W

So the approach is ...

When the node is raycasted originallyt, dynamically change it's ViewMask, then when the object is again eligible for raycasts, revert it's viewmask.

Will experiment and see how it goes. The only issue with this approach is when/how to set the ViewMask back to a value allowing Raycasting to it. And wondering if there is some already built in mechanism that does both, the hiding/masking and the unhiding/unmasking once the Raycast is handled. But likely that is best done in the Raycast event handler on that object.

Here are a couple other samples showing uses, one in Samply game and one in Featured Samples ...

https://github.com/xamarin/urho-samples/blob/b72d055a424d0e6be825c0239683c225d29ee723/SamplyGame/Core/Aircrafts/Aircraft.cs#L52

https://github.com/xamarin/urho-samples/blob/b72d055a424d0e6be825c0239683c225d29ee723/FeatureSamples/Core/23_Water/Water.cs#L172-L173

-------------------------

Dave82 | 2018-12-19 22:11:25 UTC | #6

Changing the mask constantly per frame isn't the best idea.AFAIK the function is quite expensive.

-------------------------

I3DB | 2018-12-19 22:20:22 UTC | #7

Setting ViewMask works well in the case where a node only has a single component. If multiple components, then it must be set on all components of that node in order to not again raycast the node.

This helps reduce the code complexity.

Currently setting the ViewMask once raycasted, and then resetting to original after the processing of the raycast event for that node is finished. So it's not very frequently set per raycasted node.

It also seems like it would work well when a node's components are only infrequently available to be raycasted, so they'd be dynamically set as needed.

Also, once raycasted, the pattern currently in use only starts raycasting again in 1.5 seconds in my code.

So there aren't that many ViewMask changes overall, not per Update frame anyway.

But if there are other ideas for less expense actions .... please do tell.

-------------------------

I3DB | 2019-01-15 20:18:24 UTC | #8

Here's the pattern in use now:

The raycasting code:
```
bool NoRaycasts = false;
        protected override void OnUpdate(float timeStep)
        {
            if(!NoRaycasts) Raycast();
        }
        bool IsRaycasting = true;
        DateTime lastRaycast = DateTime.Now;
        void Raycast()
        {
            if (IsRaycasting)
            {
                var result = Scene.GetComponent<Octree>().RaycastSingle(RightCamera.GetScreenRay(0.5f, 0.5f), RayQueryLevel.Triangle, 100, DrawableFlags.Geometry, 0x70000000);
                if (result.HasValue)
                {
                    IsRaycasting = false;
                    lastRaycast = DateTime.Now;
                    nodeQ.Add(result.Value);
                }
            }
            else if (DateTime.Now - lastRaycast > TimeSpan.FromSeconds(.1)) {  IsRaycasting = true; }
        }
```
The raycast processing code ... 
```
Task.Run(() => {
                while (!nodeQ.IsCompleted)
                {
                    var result = nodeQ.Take(); 
                    var OriginalMask = result.Drawable.ViewMask;
                    result.Drawable.ViewMask = 0x80000000;
                    var currentScale = result.Node.Scale.X;
                    InvokeOnMainAsync(() => result.Node.RunActions(new ScaleTo(0.1f, currentScale * 2 / 3f), new Blink(1f, 6), new ScaleTo(0.1f, currentScale), new CallFunc(()=> result.Drawable.ViewMask = OriginalMask)));
                }
            });
```
It's still tightly bound to the OS, as using DateTime, BlockingCollection, Task classes.

Allows multiple items to be in raycasted state at once, only blocks raycasts for .1 seconds at a time, and leaves the object to reset in the raycast processing code. It's not quite done, as every now and then an object disappears, and not sure why yet. Might be something else unrelated to this.

The disappearing object is because the Task to process the nodeQ delay starts and the queue would get multiple occurrences of the same object. So simply started raycasting only after the task started, and everything works perfectly now.

-------------------------

