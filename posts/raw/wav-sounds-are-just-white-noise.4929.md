JTippetts | 2019-02-16 05:24:57 UTC | #1

So, I'm playing around with adding sound effects to projects since it's not a thing I've done much of. I'm having an issue where some sounds I play are simply white noise. I downloaded some free RPG sounds from opengameart.org, and when I play the sounds in isolation from the folder they sound fine, but when I try to play them in Urho3D using a SoundSource, they're just white noise. The sounds that come with Urho3D sound fine, but those are the only sounds that work well. I've tried numerous different .WAV files from 3 or 4 different archives on opengameart, but they all just sound the same.

Any ideas on what to look for as the cause of this?

-------------------------

weitjong | 2019-02-16 05:31:16 UTC | #2

All the samples in Urho3D samples asset dir are PCM encoded mono sound source.

```
[weitjong@igloo bin]$ find . -name \*.wav |xargs file
./Data/Sounds/PlayerLand.wav:     RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 44100 Hz
./Data/Sounds/PlayerFistHit.wav:  RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 44100 Hz
./Data/Sounds/BigExplosion.wav:   RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 44100 Hz
./Data/Sounds/SmallExplosion.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 44100 Hz
./Data/Sounds/Powerup.wav:        RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 44100 Hz
./Data/Sounds/NutThrow.wav:       RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 44100 Hz
./Data/Sounds/PlayerFist.wav:     RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 44100 Hz
```

-------------------------

Leith | 2019-02-16 05:38:20 UTC | #3

You can't play stereo sounds using 3D audio. If you want to use a 3D sound source and listener, you need to force your sounds to be mono.
I used this free website service to force my sounds to be mono:
https://audio.online-convert.com/convert-to-wav

-------------------------

JTippetts | 2019-02-16 05:51:04 UTC | #4

Alright, looks like converting them to mono works. Thanks, guys.

-------------------------

Leith | 2019-02-16 06:15:08 UTC | #5

You're very welcome :)

-------------------------

Modanung | 2019-02-16 06:55:30 UTC | #6

It think it might have been the sample rate.

@Leith `sudo apt-get install` [`soundconverter`](http://soundconverter.org/)? :)

-------------------------

Leith | 2019-02-16 07:52:12 UTC | #7

Modanung, if you try to play a stereo sound in 3D, the fact that both channels exist in the audio stream is ignored, this causes a sound like white noise. We simply need to recognize the fact that in 3D audio, a sound is coming from a 3D source, so it does not need (and cannot be) stereo. I am not saying we can't play stereo sounds, but I am saying we do that with a 2D listener and no sound source... effectively, we have two ears, but sounds are not naturally stereoscopic

-------------------------

Leith | 2019-02-16 07:53:31 UTC | #8

It would be nice if the audio system in urho automatically could deal with mixing down stereo channels, for use in a 3D context... but it doesn't.

-------------------------

Leith | 2019-02-16 08:21:07 UTC | #9

It's easier for me to use a drag and drop interface, than type stuff into my linux terminal
I am lazy - I respect the potential for batching, but I don't tend to batch asset operations often.

-------------------------

Modanung | 2019-02-16 08:27:00 UTC | #10

SoundConverter _has_ a GUI, the command can simply be copy pasted into a terminal to install it.

-------------------------

Leith | 2019-02-16 08:23:27 UTC | #11

oh, it has a gui? I'll take a look in that case :slight_smile:

-------------------------

Leith | 2019-02-16 08:35:30 UTC | #13

I have installed it, preferences look simple enough, and I save a few hundred kb of network band a month :stuck_out_tongue:
I'm on a fixed cable connection, traffic shaping is engaged at 500 GB per month, I've never managed to touch the sides of it, but still cool, I didn't know about this.

-------------------------

Modanung | 2019-02-16 08:36:25 UTC | #14

[quote="Leith, post:7, topic:4929"]
I am not saying we can’t play stereo sounds, but I am saying we do that with a 2D listener and no sound source… effectively, we have two ears, but sounds are not naturally stereoscopic
[/quote]

If I remember correctly I ran into a similar issue with a music track and had to change the sample rate in that case. There may be more then one way playing a sound can result in noise since what we're hearing is basically scrambled data.

-------------------------

Leith | 2019-02-16 08:36:34 UTC | #15

Could be, well I ran into the 3D sounds with stereo issue almost immediately, it seemed most likely

-------------------------

