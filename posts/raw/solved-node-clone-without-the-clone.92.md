friesencr | 2017-01-02 00:57:55 UTC | #1

On my game I am doing some a grid based dungeony thing and I am creating lots of duplicate models.  when doing a larger grid my create method was spending all its time in InstantiateXML.  So I made prototypes of each object and executed Clone on each of the nodes.  This was wonderfully fast but now i have 2200 draw calls for 5 objects :slight_smile:  I was wondering what the pro way of doing this is?

Thanks

-------------------------

cadaver | 2017-01-02 00:57:55 UTC | #2

How many draw calls do you have if you use InstantiateXML? Objects should instance instead of multiple draw calls if they have the same materials and light conditions.

Some options which come to mind:
- Delete or disable the "prototypes" after you're done
- Use Instantiate instead of InstantiateXML (binary data)
- Use Instantiate from a memory buffer so it doesn't have to access an actual file. I'm not 100% certain if this is doable in script

-------------------------

cadaver | 2017-01-02 00:57:56 UTC | #3

Btw. now I see the reason to so many drawcalls: the glass material uses alpha blending, which requires distance sorting back to front. These are not instanced. If you can convert those to regular materials, eg. ones using the Diff technique, you'll see a dramatic drawcall reduction.

-------------------------

friesencr | 2017-01-02 00:57:56 UTC | #4

that makes a lot of sense.

Thank you

-------------------------

