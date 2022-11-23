justanotherdev | 2020-04-26 17:43:38 UTC | #1

Hi, I'm evaluating using Urho3D for an upcoming project and I have a few questions about OpenGL support.

The project page says that Urho has support for OpenGL 3.2 and I can see from that source that it doesn't have direct support for any features that have been introduced in OpenGL 4.x versions (SSBO's, atomic counters, etc.). 

Is support for OpenGL 4.x planned? Or maybe support for some portions have been implemented in some experimental branch or fork?

I know that I could always use these features from the GL context directly but it would be preferable to not have pipeline state that isn't reflected in the Graphics subsystem. Or is there some other way that people usually handle this?

Thanks!

-------------------------

