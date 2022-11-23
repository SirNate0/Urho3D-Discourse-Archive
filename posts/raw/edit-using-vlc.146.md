GIMB4L | 2017-01-02 00:58:22 UTC | #1

So I'm implementing a simple cutscene using LibVLC, and I want to follow this process to render the video:

1. Take the pixels LibVLC gives me.
2. Put them into a texture
3. Display that texture on screen.

I know a texture is a part of a render surface, and I've accomplished setting the texture's pixels. Now I just need to get this texture to render directly to the screen.

I know viewports require a camera and a scene, but what if I just want to render a texture? I've thought about using a big sprite as a UIElement, but that seems rather hacky.

-------------------------

friesencr | 2017-01-02 00:58:22 UTC | #2

I am not certain but I would try Graphics.SetTexture

-------------------------

GIMB4L | 2017-01-02 00:58:22 UTC | #3

Alright, what I'm doing is using a BorderImage and just rendering to that. However, everything shows up black, so I don't know if the problem lies with VLC or Urho's SetData function in the texture.

Here's the relevant code:

[code]static void* _videoLock(void *data, void **pixels)
	{
		VideoPlayer::VideoData *videoData = (VideoPlayer::VideoData *)data;

		*pixels = videoData->pixelData;

		return nullptr;
	}

	static void _videoUnlock(void *data, void *picture, void *const *planes)
	{
		VideoPlayer::VideoData *videoData = (VideoPlayer::VideoData *)data;

		videoData->renderTexture->SetData(0, 0, 0, videoData->renderTexture->GetWidth(), videoData->renderTexture->GetHeight(), videoData->pixelData);
	}[/code]

-------------------------

weitjong | 2017-01-02 00:58:22 UTC | #4

I have not used libVLC before so I have no idea whether your code to construct the render texture from it is correct or not. But assuming you have done it correctly, I would perhaps do it differently to render that texture. Not that I have done it before but instead of using UIElement or BorderImage, I would try to construct a new material that uses that texture and apply that material to a flat object in a 3D drawable component (or even a 2D one). That way, I believe you can stretch the component to fill the whole screen. Or, the 3D drawable component could also be just a "flat TV screen" in a bigger scene that user could navigate in (similar to setup in 10_RenderToTexture).

-------------------------

GIMB4L | 2017-01-02 00:58:22 UTC | #5

I believe the issue may lie with the SetData function. I tried memset-ing the buffer I'm about to pass in to values of 1, which means it should display a white texture, but it remains black.

-------------------------

GIMB4L | 2017-01-02 00:58:22 UTC | #6

Okay, I got it to work. Using a material was the right idea. I switched from VLC to Theora.

However, I'm now having issues getting the decoded audio to play. Here's the code:

[code]void VideoPlaybackAudioInterface::insertData(float *data, int nSamples)
	{
		sound->SetData((void *)data, nSamples * sizeof(*data));

		soundSource->Play(sound);
	}[/code]

-------------------------

