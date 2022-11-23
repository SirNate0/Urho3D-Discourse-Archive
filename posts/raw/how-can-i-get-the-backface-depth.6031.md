kannsokusha | 2020-03-30 11:05:41 UTC | #1

I'm writing a SSR shader. 
I need to get the depth of the backside to further get the thickness of the object.
How can I get it in Urho3D?
![屏幕截图(51)|690x388](upload://fufxDKqxJOCHSTaTm826F7XWX8L.jpeg)

-------------------------

kakashidinho | 2020-03-31 10:43:14 UTC | #2

Render the scene twice? Render with backface & front face culled in 2 separate passes into 2 different depth buffers.
With DX11+ UAV or OpenGL's SSBO you could write to two depth buffers in one single pass based on orientation of the fragment, but I think Urho doesn't support either of those two.

-------------------------

