amit | 2017-01-02 01:02:39 UTC | #1

Hi,
I am tryin to have a voice chat system in a app. (mutiplatform)

I tried raknet, but no proper android/ios support and build system for android seems not so ok with urho (maybe i'll include all sources in urho proj)

the network is there in urho, so i use code in SoundSynthesis sample to make my own system .. with speex.

but this would make me deal with per platform audio input ... any idea or easy way out!

-------------------------

weitjong | 2017-01-02 01:02:40 UTC | #2

There was a topic discussing the RakNet integration with Urho3D ([topic329.html](http://discourse.urho3d.io/t/raknet-open-sourced/338/1)) but the trail has gone cold, I am afraid. Sorry for not able to be more helpful than this.

-------------------------

amit | 2017-01-02 01:02:40 UTC | #3

then anyone with ndk code for android sound input! i know its not 3d specific, but still if someone has exp in it?

-------------------------

amit | 2017-01-02 01:02:40 UTC | #4

what does "	GetSoundSources () const " in [urho3d.github.io/documentation/H ... audio.html](http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_audio.html) does?

also i see "sdl audio", does it has multi platform audio input?

-------------------------

devrich | 2017-01-02 01:02:40 UTC | #5

+1

Just my 2 cents: I love the idea of being able to implement a way of [color=#0040BF][u][i]recording_then_sending----and----recieving/then_playing[/i][/u][/color] audio from in-game content.  It would be great to use this for a race track to "hear" collisions near by.

I really like the idea of voice chatting in-game too  :slight_smile:

-------------------------

cadaver | 2017-01-02 01:02:41 UTC | #6

SDL doesn't seem to have finalized audio recording support yet. You supposedly can open an audio device in capture (input) mode, and some platforms may support it, but as of 2.0.3 there's no API to read the recorded audio data in.

-------------------------

amit | 2017-01-02 01:02:42 UTC | #7

so have to write for each platform or look at some other solution!

-------------------------

boberfly | 2017-01-02 01:02:48 UTC | #8

Feel free to look into my OpenAL port for Urho3D which does add voice recording, but I only got it to work enough on iOS:

[github.com/boberfly/Urho3D/tree ... gine/Audio](https://github.com/boberfly/Urho3D/tree/openal/Source/Engine/Audio)

I never got to get ogg stream decode to work but it was due to time constraints and my app didn't need it.

Cheers
-Alex

-------------------------

amit | 2017-01-02 01:02:53 UTC | #9

Thanks,
I am now doin a separate app on each platform for Voice Chat, not idle, but easy to work as of now.

aah, there should be a forum for "paid work requests on urho"  :bulb:

-------------------------

