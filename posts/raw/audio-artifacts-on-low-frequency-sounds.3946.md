Bananaft | 2018-01-15 21:11:07 UTC | #1

Hello. I'm playing with spooky ambient sounds and having some annoying issues.

To demonstrate it I made a demo, it's script only, so you can launch it with any Urho 1.7 binary:
https://www.dropbox.com/s/9zwtw9jkbuuknkh/SoundTest_Data.zip?dl=0

And here is the video of it alongside with spectrogram visualizer:
https://www.youtube.com/watch?v=tTFLHEyGJT4&feature=youtu.be

Fist issue is the fact that sound gain and panning are changing very abruptly. You can see these "steps" on spectrogram. If you pause the video, you can see, that those steps are 0.1 seconds wide.

I found this thread: https://discourse.urho3d.io/t/sound-issues-crash-and-flickering/903/8

Where @cadaver wrote:
 
[quote="cadaver, post:8, topic:903"]
Another thing is that we mix the audio output in chunks whose size is at SDL’s mercy, and the SoundSources are only checked for changes in the beginning of the chunk. On Windows this usually isn’t a problem but in the worst case a SDL chunk might be 1/10 second or something, which would mean only updating positionality at 10FPS.
[/quote]

Well, dammit. Worst case on good-spec PC, not cool. If anyone going to try my demo, can you please tell, if it is any different for you?

The second issue are the clicks you can hear when changing gain or panning on certain sounds. I assume, it's a same problem, but even worse.

I tried smoothing the changes out. But first, to smooth out 10 fps problem you have to change parameters very slowly, so much it makes 3d panning useless. Second, on very low volumes changes have to be even slower. First few steps from 0 to something is always very distinct. Third, it does not fix the clicking.

I will be thankful for any advice. Is there any way to fix or work around this problems? Is there a way to force SDL chunk size? Or maybe change parameters gradually inside the chunk? What is your experience with audio system in Urho and what do you think of it?

-------------------------

kostik1337 | 2018-01-16 09:05:43 UTC | #2

Have you tried changing sound buffer length?

-------------------------

Bananaft | 2018-01-16 19:53:48 UTC | #3

Thank you for the tip. I changed default value in Engine.cpp from 100 to 20. Is there any trade offs or possible side-effects?

Now panning is much better. But clicks are still there. There are no audible clicks only on noise 
https://youtu.be/VtUkvgMJjbc

I tested various clean tones and they all have clicks. Clicks happen on low frequency sounds and clean tones because of sudden changes in amplitude. This will happen on any buffer length, even 1ms.

Here is a recorded waveform. Two clicks on the edges of chunk.
![image|690x217](upload://4FMKWqOQG7kUDjWDZ9f2DqFlRHO.png)

-------------------------

kostik1337 | 2018-01-16 20:14:45 UTC | #4

[quote="Bananaft, post:3, topic:3946"]
I changed default value in Engine.cpp from 100 to 20. Is there any trade offs or possible side-effects?
[/quote]

Well, until you are just playing sound without any processing, I believe it's OK. You'll have problems if you'll do some on-the-fly complex processing like FFT or convolution because 20 samples cannot contain enough information about whole signal.
UPD: it's not 20 samples but 20 ms, which means it's 882 samples, that's for sure enough for effects of any kind.

[quote="Bananaft, post:3, topic:3946"]
Clicks happen on low frequency sounds and clean tones because of sudden changes in amplitude.
[/quote]
That's absolutely right, and you can't fix these clicks by just changing buffer size. I don't know the right way to fix it, but you need to make amplitude and panning change not immediately but smoothly. Maybe you'll need to rewrite SoundSource3D, I'm not sure.

-------------------------

Bananaft | 2018-01-16 20:21:18 UTC | #5

Tried to go below 20ms. 9ms is the minimum before sound breaks. At lower values it is actually much better. Clicks turns into quiet crackle, but it is still petty clearly a bad thing. I was afraid, that buffer size  have to be greater than or equal to frametime, but it appears, that it is not the case. Why Audio.cpp has hard coded minimum value of 20ms then? Is it illegal to go below 20? what could happen?

[quote="kostik1337, post:4, topic:3946"]
amplitude and panning change not immediately but smoothly
[/quote]
Yeah, for each sample inside the chunk. I wonder, how much more CPU it will require?

-------------------------

Modanung | 2018-01-16 20:41:42 UTC | #6

[quote="kostik1337, post:4, topic:3946"]
Maybe you’ll need to rewrite SoundSource3D, I’m not sure.
[/quote]

Actually I would expect the `SoundListener` to require modification. Maybe some transform interpolation?
I dunno :balloon:

-------------------------

