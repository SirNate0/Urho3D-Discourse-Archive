miz | 2017-01-02 01:07:26 UTC | #1

Hi I'm just getting started with my first game using Urho and haven't been able to figure out how to play videos (.mp4 ideally) in a window within the game. Can anybody help? :slight_smile:

-------------------------

cadaver | 2017-01-02 01:07:26 UTC | #2

Welcome to the forums!
Video file playback is not supported by the engine directly. You need to integrate your video player library of choice, create a Texture2D in dynamic mode, and keep updating the texture with SetData() function as your video library decodes frames.

-------------------------

miz | 2017-01-02 01:07:26 UTC | #3

thanks, I'll try and get that going. Any suggestions for which video player library?

-------------------------

miz | 2017-01-02 01:07:26 UTC | #4

Also, is there a way of making the texture2D a (or child of) UI element ?

-------------------------

cadaver | 2017-01-02 01:07:26 UTC | #5

Simply assign the texture to a BorderImage UI element to show it. ( BorderImage::SetTexture() ).

-------------------------

jmiller | 2017-01-02 01:07:26 UTC | #6

[quote="miz"]thanks, I'll try and get that going. Any suggestions for which video player library?[/quote]

[ffmpeg.org/](http://www.ffmpeg.org/)

-------------------------

miz | 2017-01-02 01:07:26 UTC | #7

much appreciated!

-------------------------

codingmonkey | 2017-01-02 01:07:27 UTC | #8

Hi miz!
Try to translate this tut from RU to ENG with helps G... :slight_smile: 

[3d-orange.com.ua/video-in-your-g ... gg_theora/](http://3d-orange.com.ua/video-in-your-games-p1-ogg_theora/)

Or you may just dig in this source code : (TheoraVideo.zip) [3d-orange.com.ua/wp-content/plug ... .php?id=27](http://3d-orange.com.ua/wp-content/plugins/download-monitor/download.php?id=27)

I think this is easy way to play videos on textures, and seems that it also may in easy manner ported to Urho3d

-------------------------

miz | 2017-01-02 01:07:29 UTC | #9

I went with ffmpeg in the end as it seemed best supported and cross-platform etc. I did have trouble installing it but managed to get it going in the end.

Does anyone know of any good tutorials for ffmpeg decoding? Having trouble getting going with it, the documentation hasn't helped much...

-------------------------

Mike | 2017-01-02 01:07:29 UTC | #10

There's a very simple tutorial demonstrating how to get the RGB data, with source code, available at [url]http://dranger.com/ffmpeg/tutorial01.html[/url].
Beware that almost everything in FFmpeg is licensed under LGPL or GPL.

-------------------------

Enhex | 2017-01-02 01:07:32 UTC | #11

[webmproject.org/code/](http://www.webmproject.org/code/) is BSD license.

-------------------------

boberfly | 2017-01-02 01:07:32 UTC | #12

Another codec to consider is:
[openh264.org/](http://www.openh264.org/)

The patent covering is all on cisco, and if you target mobile what I recommend is to target the platform's API so you get the hardware decoder, and only use openh264 on the desktop or as a fallback. WebM is cool too, just you might not find hardware that decodes it.

-------------------------

miz | 2017-01-02 01:07:35 UTC | #13

Hi, I still haven't got things quite working. Can anyone help? 

I'm setting up my Texture2D as follows:
	[code]
BorderImage* video = new BorderImage(context_);
	video->SetSize(640, 480);
	vidtexture = new Texture2D(context_);
	video->SetTexture(vidtexture);
	video->SetAlignment(HA_CENTER, VA_CENTER);
	window_->AddChild(video);
	uiRoot_->SetDefaultStyle(style);
	window_ = new Window(context_);
	uiRoot_->AddChild(window_);
	window_->SetSize(648, 512);
	window_->SetName("Window");
	vidtexture->SetSize(640, 480, SDL_PIXELFORMAT_RGB24, TEXTURE_DYNAMIC);
[/code]


I've then got very nearly identical code to [url]http://dranger.com/ffmpeg/tutorial01.c[/url] except instead of saving 5 frames of data to a file I'm trying this:

[code]vidtexture->SetData(0, 0, 0, 640, 480, pFrameRGB->data);[/code]

Is this the right sort of thing? Any obvious problems?

Currently my  BorderImage/Texture is just black...

-------------------------

