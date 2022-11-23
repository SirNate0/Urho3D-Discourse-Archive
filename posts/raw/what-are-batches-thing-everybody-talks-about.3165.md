slapin | 2017-05-26 11:27:25 UTC | #1

Hi, all!
What are "batches" thing everybody talks about?
Or do I even need to know?

-------------------------

S.L.C | 2017-05-26 18:42:17 UTC | #2

Grouping drawable geometry that uses the same material to be drawn in bulk/batch without having to switch the textures/shaders. Or something along those lines. But not limited to just that. Basically, it implies grouping things that have common aspects and/or properties in situations where the preparation for performing various operations on said things, has a noticeable penalty. Most times that penalty revolves around performance.

Which is why you group them to reduce the overhead of preparing for each individual object. And then you perform the operations on the whole group at once or in sequence. Thus, performing operations in batches.

Having fewer batches you can expect to have a better use of the hardware that's being used. Otherwise, you'll spend more time communicating with the said hardware than doing some actual work on it. Thus introducing a bottleneck into your application/game. Which results in poor frame-rates and some weird stuttering.

But don't take my word on it. I could be wrong about it in this case.

-------------------------

slapin | 2017-05-26 18:58:06 UTC | #3

Ah, thanks, looks sane. But I wonder which number of batches is considered bad for 5 year old hardware?

-------------------------

Pencheff | 2017-05-27 08:29:02 UTC | #4

That depends on the complexity of a batch, e.g. what material/shaders it uses and how much geometry it consists of...and the type of hardware. It is too generic to just say a number.
I can quote one of my projects which has run on many different platforms and hardware configurations, say Intel GMA950 which is very low end cheap hardware, anything around 15 batches with just billboards (quads), single pass with no lights, no pixel shader (DX9) and 10 textures 512x512 can reduce framerates below 30fps.

-------------------------

slapin | 2017-05-27 17:48:10 UTC | #5

I mean more about modern GLES2-type hardware, like SGX5 or Mali 400, which are common on almost everything.
GMA950 is too specific thing, it does have overhead of communicating PC  RAM in strange (slow) ways
and still outputs large resolutions, so most of issues there are data manipulations...
I actually think more on how to get best graphics for bith mobile hardware and computers (PCs).
I do not want to make other not use all power just because some platform can't do many things. On another hand I want
to be effective in regard to hardware usage and still provide maximum for slower hardware. I.e. I want scaling,
but not in graphics way, but performance and hardware-specific way.
Many of these devices do have single shader unit, so they seriously benefit from batching, as one makes giant shader which does everything and run on hardware for everything, which is done right allows quite nice graphics
you never thought was possible on such small things. But trying stepping from this concept (or even trying fixed pipeline) will drop performance to unmanageable and very hard to debug state...

About 30fps - I do not think that is bad for finished product running on low end hardware. Something less than 20
does have visually noticeable (because it is irregular) stuttering which seriously affects user experience.
So I think as long as I above 30FPS for finished product on embedded hardware, I'm fine.
But that should never be set as goal during development, otherwise last minute features will drop FPS below 15,
which might happen.

-------------------------

S.L.C | 2017-05-27 18:59:25 UTC | #6

5 year old hardware was a bit ambiguous. 5 years ago we had GTX 6xx. 7xx, Titan etc. Radeon HD 7xxx, R9 etc. which can still play AAA+ games released today.

-------------------------

