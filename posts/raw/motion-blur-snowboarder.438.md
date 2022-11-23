ucupumar | 2017-06-28 14:05:50 UTC | #1

Hello everyone!

As the subject said, I'm implementing motion blur on Urho. This thread will track my progress. 
I'm planning to implement camera-based, object-based, and if I had enough brain, I will implement bone deformation-based motion blur too.  :wink: 

Actually, I've already implementing camera-based motion blur. The code still messed up and GLSL only, but it's already produce this screenshots:

http://i.minus.com/ibo0VDLzwGP7uM.jpg
http://i.minus.com/iYXZDeKuz6Zel.jpg

FPS capped to 30fps to exaggerate the effects. The implementation is based from:
http://john-chapman-graphics.blogspot.co.uk/2013/01/what-is-motion-blur-motion-pictures-are.html

Code and more stuff coming soon!  :slight_smile:

-------------------------

izackp | 2017-01-02 01:00:23 UTC | #2

Looks awesome.

I wonder, though, how it would look in high fps games. I believe there's monitors that can go up to 120 fps. I believe motion blur was done in movies because the low fps it's played at (20 fps) made it look less choppy, so it was done as a compensation for low fps. Taking a wild guess, I think 120 fps would make motion blur notable and less realistic unless the magnitude of it is scaled down as fps goes up. But then again, I don't really know lol. Just let us know how it goes.

-------------------------

ucupumar | 2017-01-02 01:00:24 UTC | #3

Thanks izackp.

Motion blur indeed low fps effects. It's because exposure time will be longer on low fps. If objects/camera moves during exposure, it will create blurry image.
It was my reason to limit fps to 30. If I unlock fps, the blur will unnoticeable. 

However, the [url=http://john-chapman-graphics.blogspot.co.uk/2013/01/what-is-motion-blur-motion-pictures-are.html]blog I mentioned above[/url] has a solution to scale motion blur based on current-per-target fps, so motion blur will still showing even on high fps. But unfortunately, it looks really weird and inconsistent after I tested it. Maybe I will take another look for this problem.

-------------------------

ucupumar | 2017-01-02 01:01:44 UTC | #4

It's tricky to implement object motion blur on Urho3D because it still can't pass per-object custom uniform. I ended up modifying Urho3D source code and add previous frame matrix attribute to Node object. 
It updated every UpdateBatches() function is called. For now it can only passed to shader if the object isn't instanced. I will upload these changes my Github branch, I haven't got time do it yet.

For now, these are the screenshots:
[img]http://i.minus.com/ibo9skWqLl1oL2.jpg[/img]

Sample vehicle drifting
[img]http://i.minus.com/ivJGSfnHFoWST.jpg[/img]

-------------------------

hdunderscore | 2017-01-02 01:01:44 UTC | #5

That looks really slick !

-------------------------

weitjong | 2017-01-02 01:01:44 UTC | #6

Lihai sekali!

-------------------------

Azalrion | 2017-01-02 01:01:45 UTC | #7

[quote]It's tricky to implement object motion blur on Urho3D because it still can't pass per-object custom uniform.[/quote]

Didn't primitive add per drawable shader parameters a week or two back?

-------------------------

weitjong | 2017-01-02 01:01:45 UTC | #8

[quote="Azalrion"][quote]It's tricky to implement object motion blur on Urho3D because it still can't pass per-object custom uniform.[/quote]

Didn't primitive add per drawable shader parameters a week or two back?[/quote]

It is still in a topic/feature branch, and not in the master branch yet.

-------------------------

ucupumar | 2017-01-02 01:01:54 UTC | #9

Thanks for all the comments. 

I have create [url=https://github.com/ucupumar/Urho3D/tree/motion-blur]motion blur branch[/url] if you want to test this. It's still OpenGL only and don't support instancing.
To see motion blur in action, just see sample 98_ObjectMotionBlur. It will produce scene like this:
[img]http://i.minus.com/jqfkSUNmqTwzX.jpg[/img]
If you look closely, it looks somewhat weird and teapot don't look blended to background. That's happen because velocity buffer only store it's own pixel velocity. Surrounding background pixels didn't have velocity data, so it don't get blurred. There are some solutions to solve this problem, the common method used in other engines are from this [url=http://graphics.cs.williams.edu/papers/MotionBlurI3D12/]paper[/url]. I plan to look into this too.

Anyway, if you want to use motion blur to other samples or your projects, just add this before set your viewport:
[code]
// To see motion blur more clearly
Engine* engine = GetSubsystem<Engine>();
engine->SetMaxFps(30);

ResourceCache* cache = GetSubsystem<ResourceCache>();
Renderer* renderer = GetSubsystem<Renderer>();
renderer->SetDynamicInstancing(false);
renderer->SetDefaultRenderPath(cache->GetResource<XMLFile>("RenderPaths/ForwardMotionBlur.xml"));[/code]Hope this will be useful.  :smiley: 

[quote="weitjong"][quote="Azalrion"][quote]It's tricky to implement object motion blur on Urho3D because it still can't pass per-object custom uniform.[/quote]

Didn't primitive add per drawable shader parameters a week or two back?[/quote]

It is still in a topic/feature branch, and not in the master branch yet.[/quote]
What branch is that? 
In my implementation, I passed previous frame camera and object matrix at UpdateBatches() function. I feels like this method isn't optimal because batch will always calculate and send the matrix to GPU despite if you don't want to use them. Unrelated to motion blur, I found this behavior common in Urho, for example, cCameraPos uniform still passed to shader even tough it's in rendering post processing quad. Sometimes it's useful to some method, but most of the times, it doesn't. I'm not expert on OpenGL (or DirectX), but does this really affect performance?

-------------------------

weitjong | 2017-01-02 01:01:55 UTC | #10

[quote="ucupumar"][quote="weitjong"][quote="Azalrion"]Didn't primitive add per drawable shader parameters a week or two back?[/quote]
It is still in a topic/feature branch, and not in the master branch yet.[/quote]
What branch is that?[/quote]
The branch is [github.com/urho3d/Urho3D/commit ... parameters](https://github.com/urho3d/Urho3D/commits/drawable-shader-parameters). Note that I was just responding to Azalrio's post, I am not sure whether it addresses your need or not. BTW, thanks for sharing it.

-------------------------

