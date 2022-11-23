haolly | 2017-12-16 12:17:02 UTC | #1

I find the code `ResourceCache::GetResource(StringHash type, ...)` checks the load happens in the main thread,
but I do not understand why it does this check, why Urho could not load resource in another thread

My knowledge tells me that use multiply thread will accelerate the progress when loading multiply resource 
 :confused:

-------------------------

spwork | 2017-12-16 12:30:37 UTC | #2

see the document,you can use <code>BackgroundLoadResource() </code>load resource in background thread

-------------------------

SirNate0 | 2017-12-16 15:33:37 UTC | #3

As to why I'm pretty sure it's just because various graphics resources (like textures) have to be uploaded to the GPU from the main thread, and that is a part of the loading process.

-------------------------

WangKai | 2017-12-19 14:44:04 UTC | #4

There are two phases for background resource loading: 

    bool Resource::BeginLoad(Deserializer& source)
    {
        // This always needs to be overridden by subclasses
        return false;
    }

    bool Resource::EndLoad()
    {
        // If no GPU upload step is necessary, no override is necessary
        return true;
    }

BeginLoad is on the background loading thread and EndLoad is executed on the main thread for the GPU resource creatation, since all graphics stuff are on the main thread.

We can use a rendering thread for all the GPU stuff, it's another topic anyway.

-------------------------

Eugene | 2017-12-19 15:00:01 UTC | #5

[quote="haolly, post:1, topic:3852"]
but I do not understand why it does this check, why Urho could not load resource in another thread
[/quote]

1. Because there shall be locks to get an existing resource in multiple threads, so it would end up with deadlocks and multiple loadings of single resource. And other MT bullshit that nobody want to care about.

2. Because not every resource could be loaded in worker threads.

-------------------------

haolly | 2017-12-21 14:43:04 UTC | #6


This is the document in [resource]( https://urho3d.github.io/documentation/1.7/_resources.html) says,
>  Depending on the resource, only a part of the loading process may be moved to a background thread, for example the finishing GPU upload step always needs to happen in the main thread.

It seems that whether or not  a resource could be loaded in background thread depends on the type of the process,
So, could I say that when loading any resource that does not involve GPU stuff, it could be a loading at background thread ?
but @Eugene  's words make me think  that it depends on the type of the resource :disappointed_relieved:
[quote="Eugene, post:5, topic:3852"]
Because not every resource could be loaded in worker threads.
[/quote]

-------------------------

Eugene | 2017-12-21 14:48:12 UTC | #7

[quote="haolly, post:6, topic:3852"]
So, could I say that when loading any resource that does not involve GPU stuff, it could be a loading at background thread ?
[/quote]
Yes. So it depends on the type of the resource.

-------------------------

