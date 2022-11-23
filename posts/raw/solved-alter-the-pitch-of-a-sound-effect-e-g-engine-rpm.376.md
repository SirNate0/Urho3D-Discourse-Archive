gunnar.kriik | 2017-01-02 00:59:58 UTC | #1

Hi,

I am attempting to create vehicle engine sounds based on the engine RPM where I have multiple sound loops for various baseline RPMs (1000, 2000, 3000, etc.). I will then mix between these sounds to to match the engine RPM. But ideally I would also like to alter the pitch up/down of each sample when they overlap, e.g. at 1500 RPMs. At 1500 RPMs there are two effects playing - the 1000 and 2000 RPM sounds, but I would like to alter the pitch of these slightly based on the current vehicle engine load. So my question is really - is it possible to alter the pitch (or speed) of a sample using SDL? I have done this previously with OpenAL which allowed me to alter the pitch of a sound directly, but from what I see SDL has no such feature. Does anybody know if this is possible with SDL, or will I need to implement the audio using OpenAL? 

There is a branch that has simple OpenAL playback implemented here: [github.com/boberfly/Urho3D/tree/openal](https://github.com/boberfly/Urho3D/tree/openal) and this works well, although it's missing music streaming. I am aware of the licensing conflicts with Urho3D and OpenAL, so I know OpenAL will likely not be officially supported.

-------------------------

cadaver | 2017-01-02 00:59:58 UTC | #2

Urho's audio system does the mixing in software; SDL just outputs the mixed audio stream. You can alter the pitch of a playing SoundSource by calling SetFrequency() on it. Note that it expects the parameter directly in Hz - but you can inspect the default frequency of the currently playing sound:

[code]
float pitchFactor = 1.0f;
Sound* playingSound = soundSource->GetSound(); // Make sure this is non-null
soundSource->SetFrequency(pitchFactor * playingSound->GetFrequency());
[/code]

-------------------------

gunnar.kriik | 2017-01-02 00:59:58 UTC | #3

Awesome - thanks. Completely overlooked the SetFrequency() function. That'll do the trick!  :smiley:

-------------------------

