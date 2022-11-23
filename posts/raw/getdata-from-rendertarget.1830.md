vrivotti | 2017-01-02 01:10:29 UTC | #1

Hi.
I have an Android/iOS app running with Urho3D and I need to grab a snapshot. 
I've tried using an aux rendertarget texture and use GetData to get the texture contents, but I'm getting a "Getting texture data not supported" error.
What am I doing wrong? Is there any other way of doing it?
Thank you.

-------------------------

thebluefish | 2017-01-02 01:10:29 UTC | #2

It's not supported on mobile devices. GetData makes an underlying call to glGetTexImage, which is not supported on GL ES. AFAIK, glBlitFramebuffer is going to be needed but I am not sure if it's going to be supported here.

-------------------------

mcosta | 2017-01-02 01:10:30 UTC | #3

glReadPixels, why not?

-------------------------

cadaver | 2017-01-02 01:10:31 UTC | #4

We could add an OpenGL-only method to Graphics to use glReadPixels to read from the backbuffer or the current rendertarget. Doing it yourself carries a risk that the current rendertarget is not actually current, as it's being lazily managed before each draw call.

-------------------------

mcosta | 2017-01-02 01:10:31 UTC | #5

Are guys willing to implement it? We have it working on a custom made engine which is shared between iOS and Android. It was written in c# on top of OpenTK. The function that we have for more than 1 year is the following

        unsafe public byte[] GetTextureBytes()
        {
            byte[] bytes = new byte[Texture.Width * Texture.Height * 4];

            var state = new StateManager ();
            state.Push ();

            FBOManager.Active = FrameBuffer;
            TextureManager.Active = Texture;

            fixed(byte* buffer = &bytes[0]) 
            {
                GL.PixelStore (PixelStoreParameter.PackAlignment, 1);
                GL.ReadPixels (0, 0, Texture.Width, Texture.Height, PixelFormat.Rgba, PixelType.UnsignedByte, (IntPtr)buffer);
            }

            state.Pop ();

            return bytes;
        }

cheers
Manuel

-------------------------

cadaver | 2017-01-02 01:10:31 UTC | #6

It's one possibility, another possibility is to just expose a function which makes sure the selected rendertarget (ie. after Graphics::SetRenderTarget) is current, to allow the user to make the glReadPixels() call themselves.The latter could be desirable in case the parameters of glReadPixels() are not obvious, but I suspect in most cases one wants to read 8bit RGB(A) data.

-------------------------

cadaver | 2017-01-02 01:10:31 UTC | #7

Took a look at the GL rendering code. You can use the following sequence to be able to use glReadPixels from either the backbuffer or a rendertarget:

- Graphics::SetRenderTarget() <- null ptr for backbuffer
- Graphics::SetViewport() <- can be anything you like, this ensures that the proper FBO is active
- Now you're safe to call glReadPixels()

Also for a fullscreen capture of the backbuffer you're already able to just use Graphics::TakeScreenShot().

-------------------------

vrivotti | 2017-01-02 01:10:31 UTC | #8

Thank you cadaver, I'll give it a try.
Nonetheless, it would be great to have a crossplatform way of doing it (we want to support Windows too).

-------------------------

cadaver | 2017-01-02 01:10:32 UTC | #9

The glReadPixels() GLES workaround was rather easy to add directly to Texture2D::GetData() and TextureCube::GetData(), it's in the master branch now. It works if the texture in question is a rendertarget. It induces a rendertarget switch when you read the data, so it possibly isn't very performant.

[github.com/urho3d/Urho3D/commit ... 17102db709](https://github.com/urho3d/Urho3D/commit/6538f3bb4a6ae6906b9f52d01bed8317102db709)

-------------------------

mcosta | 2017-01-02 01:10:32 UTC | #10

Tkx!

-------------------------

