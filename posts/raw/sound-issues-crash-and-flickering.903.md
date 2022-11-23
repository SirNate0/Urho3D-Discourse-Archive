gawag | 2017-01-02 01:03:58 UTC | #1

My sound is flickering (making click noises) when the volume is changed by my code or by a changed distance.
And when using FixInterpolation() it just crashes (log says nothing about the crash).
[code]
// at application start:
sound_engine=cache->GetResource<Sound>("Sounds/engine.ogg");
sound_engine->SetLooped(true);
//sound_engine->FixInterpolation();    // this crashes
sound_source=node_plane->CreateComponent<SoundSource3D>();
sound_source->SetNearDistance(1);
sound_source->SetFarDistance(2000);
sound_source->SetSoundType(SOUND_EFFECT);
sound_source->Play(sound_engine);
sound_source->SetGain(0);
...
// when updating:
sound_source->SetFrequency(engine*200);                          // engine is a float between 0.0 and 400.0. Same issues when setting to a constant value.
sound_source->SetGain(Clamp(engine,0.0,200.0)/200.0);   // flickering sound. None when not changing distance and the engine value is not changing.
[/code]
There is also no flickering sound when the last line is commented out and the distance is constant (even if the engine value changes).
I'm using this sound (converted to .ogg, but it's also flickering with the original .wav): [freesound.org/people/Marlon ... ds/242740/](https://www.freesound.org/people/MarlonHJ/sounds/242740/)
And I'm using the current Git master version of Urho.
It's not flickering when I have never changed the frequency.

Does this FixInterpolation() do something useful when the sound is already perfectly looping? I thought it might fix the flickering.

-------------------------

cadaver | 2017-01-02 01:03:59 UTC | #2

Fixed the crash and added better explanation to FixInterpolation(), the short version is that you don't need to call it.

I tested playing the sound on various gains and frequencies and did not hear anything unusual, except when very rapidly panning the sound from left to right. At that point I could hear clicks, which is due to an abrupt change in the amplitude on the left or right channel. Fixing this would mean applying a short ramp to each volume change when mixing, and that's not trivial.

-------------------------

gawag | 2017-01-02 01:04:00 UTC | #3

Yay another fixed bug! :mrgreen: 
But don't worry, I got a whole bag of bugs/issues already!  :laughing: 

I recorded a video with those click sounds. They seem to be worse on low frequencies. The engine value is displayed at the top, so you could get the exact frequency by multiplying with 200 as the code says.
[video]http://youtu.be/wtcJ4TWfLWQ[/video]
They are quite noticeable when turning the camera (0:13), when changing distance (0:24) and when tuning the engine/frequency directly (1:05).
The clicking is less noticeable with high frequencies (0:42 or 1:00) (unless you are turning the camera).

Would it be possible to update the sound more frequently over a short time to smooth the changes? My "game" is running at 60 FPS and the changes seem to be too fast for that. Would it be possible to make an additional thread to make them with 500 "FPS" and interpolate over some time or something like that?
This flickering is quite ruining the game.

-------------------------

thebluefish | 2017-01-02 01:04:00 UTC | #4

FYI, FPS shouldn't be the factor that determines if your sound plays right or not. Making more frequent updates *typically* isn't how to solve this kind of issue.

Can you setup a minimal test project that still reproduces the issue?

-------------------------

gawag | 2017-01-02 01:04:00 UTC | #5

Ah, discovered it's not flickering when only changing the frequency. It's flickering when changing the gain (more or less rapidly). And it's really bad when the frequency is set to something low (strong flicker in the 2000-10000 range but also at other values).

Example code:
[code]
Sound* sound_engine;
SoundSource3D* sound_engine_source;
...
// at application start:
sound_engine=cache->GetResource<Sound>("Sounds/engine.wav");  // the original file I linked to
sound_engine->SetLooped(true);
sound_engine_source=node_plane->CreateComponent<SoundSource3D>();
sound_engine_source->Play(sound_engine);
sound_engine_source->SetFrequency(4000);
SoundListener* listener=cameraNode_->CreateComponent<SoundListener>();
GetSubsystem<Audio>()->SetListener(listener);
...
// In the update function:
static double time=0;
time+=timeStep;
sound_engine_source->SetGain(sin(time)*0.4+0.5);      // change the volume somehow. Doesn't matter if like this per own code, per camera rotation or per distance change.
[/code]
More rapid gain change means more flickering. Though this gain change here is not really rapid. Moving fast or turning the camera makes it worse.

I also just tried changing the speed of the sound in the file and playing it at other frequencies to get (theoretically) the same playback speed. Didn't really help, made it partly worse.

I just tested the NinjaSnowWar-Demo (without changing anything in there like the code). When the NPCs are throwing snowballs and you turn the camera really fast it flickers too. So it's not just when using different or low frequencies, that's only making it worse.
The SoundEffects-Sample is also flickering when changing the music volume, that really surprises me.
Do you have those issues too? Other applications and games don't have a flickering issue so I would be surprised if it's a hardware or driver issue.

[quote]FYI, FPS shouldn't be the factor that determines if your sound plays right or not. Making more frequent updates *typically* isn't how to solve this kind of issue.[/quote]
Tried that by slowing my engine changes down to make the changes slower. You are right that didn't resolve the issues, it just stretched the clicks sounds over a longer duration (amount kept the same).

-------------------------

thebluefish | 2017-01-02 01:04:00 UTC | #6

Well first off, let's get you ramping your sound to see if that helps. Making not-too-significant changes might make it sound more realistic, too.

Let's first define 2 local variables:
[code]
float _target;
float _actual;
[/code]

We'll need to include PhysicsEvents.h, and then hook into our event (Yes I am using MainMenu for my testbed):
[code]
SubscribeToEvent(Urho3D::E_PHYSICSPRESTEP, HANDLER(MainMenu, HandlePhysicsPreStep));
[/code]

Somewhere, we need to increase/decrease our target. I used mouse wheel in my example:
[code]
void MainMenu::HandleMouseAxisMove(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData)
{
	using namespace Urho3D::MouseWheel;

	int wheel = eventData[P_WHEEL].GetInt();

	if (wheel == 1)
	{
		_target += 1;
	}
	else
	{
		_target -= 1;
	}
	_target = Urho3D::Clamp(_target, 0.0f, 200.f);
}
[/code]

Then, in our HandlePhysicsPreStep:
[code]
float timeStep = eventData[P_TIMESTEP].GetFloat();

float targetDelta = 0.1f;
float change = _target - _actual;
float delta = 0;

if (change < 0)
	targetDelta = -targetDelta;

if (Urho3D::Abs(change) > Urho3D::Abs(targetDelta))
	delta = targetDelta;
else
	delta = change;
	

_actual += delta;
_actual = Urho3D::Clamp(_actual, 0.0f, 200.f);

_text->SetText(Urho3D::String(_target));
_text2->SetText(Urho3D::String(_actual));
[/code]

This will smooth out the changes by ramping [b]_actual [/b]by a set interval to match [b]_target[/b]. See if that helps with the issue.

-------------------------

gawag | 2017-01-02 01:04:00 UTC | #7

Limiting the change speed helped a bit but the flickering was still there and disturbing.
Then I sat different lower limits for my frequency: I can't here any flickering when I don't go under 40000 and the flickering is barely noticeable when I don't go under 30000.

Though both only helped for the case of changing the engine speed. The flickering is still the same when the volume is changed quickly by a changed distance or a rotated camera.

Cadaver seems to already have "explained" everything in his post, but I didn't get the real problem at first:
[quote]I tested playing the sound on various gains and frequencies and did not hear anything unusual, except when very rapidly panning the sound from left to right. At that point I could hear clicks, which is due to an abrupt change in the amplitude on the left or right channel. Fixing this would mean applying a short ramp to each volume change when mixing, and that's not trivial.[/quote]
Longer explanation:
Think of a sinus curve with a small amplitude as the sound and when the volume is changed without fading (suddenly switching to a high amplitude), there is a very steep change which makes this click-sound.
That's the same as randomly cutting out a piece of a sound in a sound editor. If the curve changes to rapidly, it makes a noticeable and disturbing click sound too.
So Urho is letting the sound curve jump to rapidly/steeply which creates dozens of clicks sounds within a few seconds.

I hoped it would be possible to update the sounds gain or frequency more often per second as just once per frame (which is one per 1/60s here). But I think we would need to directly manipulate (aka smooth out) the sound buffer because those "cuts" in the 44100 Hz sound output created by volume changes are creating the clicks and not that we are not updating our volume/frequency often enough. In fact, it should help to make less changes per second. With making a volume change 60 times per second we create up to 60 clicks per second (depending on the height of the jump of the sound curve). If Urho would only update the sound ten times per second, we could only get up to ten clicks.
Though this is no real fix since there are still clicks.

Seems like the only real fix is to smooth out the sound buffer. I think typically applications use a 10ms to 30ms sound buffer. It should be theoretically possible to smooth out all changes there that are too steep. Maybe with an additional thread. 60FPS means that every frame lasts ~16ms. Depending on the buffer size and the frame rate that would be enough to smooth once every frame. A better solution may be an additional thread doing only those smoothes and sleeping when it smoothed enough to rest a bit.
What is Urho using to output the sounds? SDL?
I'm surprised that no other application has those issues. Was Urho not able to activate some kind of hardware acceleration that would have prevented this?
The Urho log says: [i]INFO: Set audio mode 44100 Hz stereo interpolated[/i] What does [i]interpolated[/i] mean in that context?

-------------------------

cadaver | 2017-01-02 01:04:00 UTC | #8

We software mix everything (and stuff the final mix to SDL audio output) to depend minimally on anything external, audio-wise, so we never even attempt to use something like hardware acceleration. Admittedly the mixing algorithm is not top-notch. Interpolation means interpolation between sample values when the SoundSource playback frequency is below the mixing frequency. Actually non-interpolated mixing was only needed on 486's or so, so that option could be removed :slight_smile:

Another thing is that we mix the audio output in chunks whose size is at SDL's mercy, and the SoundSources are only checked for changes in the beginning of the chunk. On Windows this usually isn't a problem but in the worst case a SDL chunk might be 1/10 second or something, which would mean only updating positionality at 10FPS.

-------------------------

