davemurphy | 2018-01-05 15:12:16 UTC | #1

Hi,

I've been using both Urho3D and UrhoSharp on the HoloLens. My application is CPU intensive and the HoloLens only has an atom processor, so I've been looking for some ways to reduce CPU usage. 

I read an article about [stereo rendering performance](https://blogs.unity3d.com/2017/11/21/how-to-maximize-ar-and-vr-performance-with-advanced-stereo-rendering/) from the Unity blog. They have an outline of single pass stereo rendering in the article and they mention using a double wide render target and binding both eye's view projection matrices and using a constant buffer to index for each eye. The graphs at the end of the article claim a significant decrease in CPU when using this technique.

What I want to know is will this be possible to implement inside of Urho3D or are there parts of the Urho3D rendering pipeline that would fundamentally prevent an implementation?

Thanks

-------------------------

