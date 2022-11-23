projector | 2017-03-01 07:45:15 UTC | #1

I have been trying to fix the small but frequent stuttering frame-rate in a very simple scene with just few moving objects, the stuttering happens in iOS devices but not in Android devices. I have tested few simple examples that come with Urho3D sdk, it looks like the examples also suffers different degree of stuttering issue in iOS devices.

For an example, 
I tested stuttering using RenderToTexture example comes with Urho3D, using xcode profiler to test for performance, most of the time the example demo runs at 60(or 59) FPS, but every 20-40 seconds, the fps would drop to 56-58 FPS and get back to 60(or 59) in 1 or few frames later. Reducing the rotating cube to just 1 does not fix the small stuttering.


I tested it in iPhone 6 Plus, iPhone SE, iPhone 6S, all iOS devices suffer the stuttering fps in running simple demos, no stuttering observed in my android devices. Vsync and HighDPI are enabled on in all the demo I've tested.

I 've spent 2 days trying to figure out but still can't manage to know the reason of stuttering FPS. The stuttering is small but could be quite noticeable in a scene with high speed moving objects. Has anyone ever experienced the stuttering frame rate with Urho3D? or anyone has any idea to fix this issue?

-------------------------

projector | 2017-03-03 10:37:25 UTC | #2

I tested it with iPhone5, it runs with no stuttering at all. It kind of gives a glue that it could be something to do with support of CPU architecture, iPhone5 is the last model to use armv7 cpu, where the later iPhone models use arm64. 

The stuttering issue is easy to be reproduced with Urho3D example, can anyone who is using Urho3D for iOS development help to confirm the stuttering?

-------------------------

rku | 2017-03-03 13:00:58 UTC | #3

This is not iOS-exclusive. My simple game also has this problem. Object moving across the screen in a straight line is stutter-free on galaxy s2, but stutters on galaxy s5. That is what kicked off my [profiler rework](http://discourse.urho3d.io/t/profiler-rework-and-profiling-tool/2726). Why it happens i do not know. I am in process of optimizing my code in hopes ill get rid of the stutter. You should try profiling your application using my branch with profiler code and seeing if anything obvious comes up.

-------------------------

projector | 2017-03-03 15:08:30 UTC | #4

 I used the Urho3d examples(especially RenderToTexture) and few simple demos to test, those demos are so simple that there is very little space left to optimise(no dynamic allocation for objects, and I've tried to make the scene simple to avoid any possible pixel/texel fill-rate bottleneck). Thanks for your response and suggestion, I will try to use your profiler code to check if there is anything comes up.

-------------------------

projector | 2017-03-03 15:08:38 UTC | #5

I understand many reasons could cause the stuttering fps, but this time in my case it has raised me to question if it's  incompatibility of Urho3D with newer iOS devices, if anyone is using iOS devices that is newer than iPhone5, it will be very helpful if you can help to test and confirm the stuttering with Urho3D example by using xcode profiler(Instrument->Core Animation).

-------------------------

rku | 2017-03-03 18:39:04 UTC | #6

If you google around you will find that many unity users are also complaining about same thing. This is not a problem unique to urho3d. There is nothing in urho3d inherently incompatible. I bet we are hitting some obscure cornercase here. Especially odd is my case where newer and more powerful device performs worse than older less capable device. Gremlins, must be them at fault here.

-------------------------

projector | 2017-03-04 03:44:01 UTC | #7

My case so far seems to be iOS exclusive, it runs smoothly in all mid to high end Android devices. Besides, I have no issue to use Unity, Cocos2d-x or plain OpenGL ES to make a simple demo to run stutter-free and consistent 60FPS, especially if the demo was very simple and it was handled very carefully not to hit GPU or CPU bottleneck.

Sometimes it's easier to cause stuttering in higher-end device by hitting fill-rate or GPU bottleneck due to the higher resolution of the devices. Although the more powerful devices usually have higher GPU processing power, but in some devices, the bump of GPU processing power is not high enough to cater the increase of number of pixels. For my testing, it seems not to be the same case, the demo is simple enough that it should not hit any kind of GPU bottleneck in all those devices, I've also tested it with with iPhoneSE and iPhone5, both devices are having the same resolution, but the more powerful device suffers the stuttering issue.

I agree with you that we could be hitting some obscure corner case, that's why I need others to help to test and confirm if all iOS devices newer than iPhone5 suffer stuttering FPS running Urho3D examples.

-------------------------

rku | 2017-03-08 09:31:51 UTC | #8

Got around to do more profiling using easy_profiler and it is revealing:
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/a8848f9ce9aada95b63f5050ca596d3c3776b0b7.png" width="690" height="73">
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/353a99326b34cdd3cd1ae2489ab8a99771ee091c.png" width="690" height="73">
My primary suspected offenders are these two - they alone quite often exceed frame budget (that dashed line crossing graphs is frame target of 16.(6)ms). These areas could use some optimizing. Ill investigate further, if anything comes out of it ill post here.

Edit: more digging revealed all the slowdowns happen in sections that contain `queue->Complete(M_MAX_UNSIGNED);`. `ProcessLights` section is also causing issues, although in this case slowdowns are much more rare. Multithreading is biting us in the read. @cadaver do you have any suggestions how we could possibly optimize/fix this?

-------------------------

cadaver | 2017-03-08 12:35:04 UTC | #9

Try to run without worker threads? (engineParameters[EP_WORKER_THREADS] = false) Thread synchronization primitives are on the mercy of the OS, so if the scene doesn't actually benefit from them, it's safer to run without.

-------------------------

projector | 2017-03-08 13:07:36 UTC | #10

I just tested running without worker threads, now the Urho3D examples as well as my testing demo run stutter-free and consistent 60FPS :smiley:

I really appreciate rku for finding out the cause of stuttering. Thanks cadaver for the workaround suggestion.

-------------------------

rku | 2017-03-08 14:02:49 UTC | #11

After disabling worker threads stutter is almost gone, but some of it still visible to the naked eye. Interesting thing: often workers do not run in parallel for some reason (PC). On android they do not run in parallel like 80% of the time. That explains why disabling them improves performance.

`Present` code block also behaves rather interesting (android):
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/d6a54fc87db450bee4b2416031a9e6a3f2823b2b.png" width="690" height="44">

Although it always fits within frame budget now and there should not be any stuttering. I am observing objects animated through `ValueAnimation` so probably there isnt much i could do wrong to cause the stutter myself. I guess this is were we have to dig deeper.

For comparison this is graph from running application on PC (opengl/linux/nvidia proprietary drivers):
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/73edac73a46ee21d9727c26ad2417f5d6548c4d8.png" width="690" height="55">
`Present` is way more consistent and takes way less time (as expected). but some hiccups still do happen.

Anyhow  to get rid of remaining stuttering i enabled vsync. Oddly enough now object movement is very smooth. Have to look very hard for any stuttering and it is hard to see. Honestly i suspect there is tiny tiny bit of stuttering left, but i am not 100% sure. Also frames pretty much always miss 16.(6)ms frame budget:
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/6b7055da6698a9f49d777b66715bf5a8c91c7c63.png" width="690" height="52">

All these tests run with frame limiter turned off.

-------------------------

