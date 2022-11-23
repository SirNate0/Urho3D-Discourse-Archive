yushli1 | 2017-12-23 11:20:48 UTC | #1

git clone the latest master branch, run it on windows and then error occurs:

ERROR: Could not initialize audio output, 16-bit buffer format not supported

The same PC with the same config works before upgrading sdl. Any idea what causes this error?

-------------------------

Eugene | 2017-12-22 14:36:21 UTC | #2

@weitjong You were right! xD

> I guess it is as usual, we have to merge it to master branch first and that's when shit hits the fan.

-------------------------

weitjong | 2017-12-22 16:20:33 UTC | #3

If it is a runtime error, perhaps you can retry the binary on a machine with SSE3 support (or AVX, not sure). SDL 2.0.7 uses SSE3 for audio conversion, if I recall correctly. The problem is, Visual Studio does not provide a compiler flag to enable SSE3. It has flags for SSE, SSE2, and directly jump to AVX and AVX2. So, that what I did. Setting the VS flags to target AVX when URHO3D_SSE build option is enabled.

I have asked for feedback in my development (b)log while I was at it, but there was no feedback. https://github.com/urho3d/Urho3D/issues/2146#issuecomment-343940722

-------------------------

yushli1 | 2017-12-23 07:26:29 UTC | #4

It is run time error. I stepped into audio.cpp and the obtained.format is 0x8210, which is 32bit sample AUDIO_F32LSB . thus cause error in line 122
    if (obtained.format != AUDIO_S16SYS && obtained.format != AUDIO_S16LSB && obtained.format != AUDIO_S16MSB)
    {
        URHO3D_LOGERROR("Could not initialize audio output, 16-bit buffer format not supported");
        SDL_CloseAudioDevice(deviceID_);
        deviceID_ = 0;
        return false;
    }
Is there any flag that can be set to avoid this error?

-------------------------

weitjong | 2017-12-23 03:14:08 UTC | #5

I am afraid I cannot help you to troubleshoot at this time. Just booted into my Windows 10 partition after not using it for a long time and what I got was, INACCESSIBLE BOOT DEVICE and go into a reboot loop. You may try to change the code at the line you mentioned to accept that format and see it can get you far or not. In the AppVeyor CI build we run all the samples and they all passed, so there could be something more to it in your case (again I am not sure, didn't really personally test on Windows platform when I did the SDL upgrade). I have decided not to introduce URHO3D_SSE2/3 build option, so no there is no option you can try, aside from URHO3D_SSE.

-------------------------

cadaver | 2017-12-22 18:51:33 UTC | #6

Potentially the best solution would be to add support for outputting the audio in 32bit floating point for the case that it's all that the hardware driver supports. It's just a simple per-sample conversion.

-------------------------

weitjong | 2017-12-23 09:24:33 UTC | #7

Agree with Lasse. Your issue could be more related to new SDL audio driver for Wasapi than the SSE3 support in your hardware. Based on this below, it seems the new audio driver is F32 only and it is chosen as the new default over XAudio. 

https://discourse.libsdl.org/t/sdl-2-0-6-released/23109

If so, you can try to pass an environment variable to choose the now deprecated XAudio driver explicitly when running your app until we have adapted Urho engine to take advantage of the new driver.

-------------------------

yushli1 | 2017-12-23 09:24:29 UTC | #8

SDL_setenv("SDL_AUDIODRIVER", "directsound", true); solves the problem. Thanks for all the help. 
And I look forward to the adaption of the new audio driver.

-------------------------

weitjong | 2018-01-03 15:41:51 UTC | #9

I have done a little experiment. Based on this, https://wiki.libsdl.org/Tutorials/AudioStream, we could just leave the current mixing logic alone and still be able to support F32 audio devices, by utilizing the internal SDL audio stream to do the audio conversion on the fly. Peeking at the SDL audio code, the internal audio streaming will be enabled when there is a mismatch of any of the desired vs obtained options. And so by altering the last parameter in this line https://github.com/urho3d/Urho3D/blob/136b84e351331bed32fc394649a884f733657707/Source/Urho3D/Audio/Audio.cpp#L106, from `SDL_AUDIO_ALLOW_ANY_CHANGE` to `SDL_AUDIO_ALLOW_FREQUENCY_CHANGE|SDL_AUDIO_ALLOW_CHANNELS_CHANGE`, i.e. not allowing format change, then it potentially enables this internal audio conversion and allowing us to just always feed data using the desired "AUDIO_S16". I have tested this to be working for "wasapi" (F32) and "directsound" (S16) on Windows platform, "pulseaudio" (S16) on Linux platform, and also "emscripten"  (F32/WebAudio) on Web platform.

My conclusion:
1) Unless we really want to support audio data files using float format (currently all our samples don't), then the above is the only thing need to be changed to get the sound on the wasapi audio driver.
2) The existing code branch for `__EMSCRIPTEN__` in the `Audio` class can actually be eliminated now (i.e. let the SDL does the conversion for us).
3) SDL supports multiple channels audio and Urho hasn't taken any advantage of it.

-------------------------

