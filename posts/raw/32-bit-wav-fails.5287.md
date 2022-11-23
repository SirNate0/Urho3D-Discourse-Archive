Avagrande | 2019-07-07 13:05:48 UTC | #1

Hi.

I am currently in the process of migrating a project of mine to urho3d. 
When I attempt to load a 32 bit wav file it fails to load the resource. To be exact I am using audacity to export at  "WAV (Microsoft) 32-bit float PCM" format. This only affects 32 bit wav and not 16 bit or OGG. 

Is this a bug or are 32 bit wav files not supported?

I am using the resource cache in Lua like this: 
    local sound = cache:GetResource("Sound", "noise.wav")

-------------------------

S.L.C | 2019-07-07 19:22:28 UTC | #2

I get a Déjà vu feeling from this.

Gotta look through the issues on Gihub. brb

-------------------------

JTippetts | 2019-07-07 21:05:36 UTC | #3

Could be related to an [issue](https://discourse.urho3d.io/t/wav-sounds-are-just-white-noise/4929) I had awhile back. Make sure your sounds are mono encoded, and not stereo.

-------------------------

Avagrande | 2019-07-07 21:08:47 UTC | #4

The sources in question were all mono. you can test this by making a mono source ( can be just white noise if you want ) and saving it as either 16 bit or 32 bit wav and it wont let you load the 32 bit. 
I decided to bulk convert my sounds to ogg for now.

-------------------------

Leith | 2019-07-08 04:40:17 UTC | #5

I will try to find some time to check this out, its not been an issue for me so far but I am betting that the sound buffer in urho is 16 bit fixed word size

-------------------------

