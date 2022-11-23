KerMatt | 2018-12-19 00:14:37 UTC | #1

 I'm trying to create some background music in my game.
I've change the sample.inl to enable sounds and such, but whenever i attempt to call SetLooped i get a read access violation as the Sound is null. The music is there in the Data folder.

   	Sound* music = cache->GetResource<Sound>("Music/background.ogg");
	music->SetLooped(true);
	backgroundMusic = scene_->CreateComponent<SoundSource>();
	backgroundMusic->SetSoundType(SOUND_MUSIC);
	backgroundMusic->Play(music);

-------------------------

Dave82 | 2018-12-19 00:43:27 UTC | #2

[quote="KerMatt, post:1, topic:4762"]
Sound* music = cache-&gt;GetResource&lt;Sound&gt;("Music/background.ogg");
[/quote]

If the returned Sound* is null at this point , the file you're trying to load does not exists or it's format is invalid and could not be loaded.make sure the file and path exists.
Also you should check the console for errors (on windows at least)

-------------------------

KerMatt | 2018-12-19 01:07:02 UTC | #3

The file is there, and plays fine out of Urho.
Is .ogg not a good format? Could it be an issue with the file itself?

-------------------------

Sinoid | 2018-12-19 02:11:57 UTC | #4

Were there any mentions of failing to read the vorbis ogg file in the log?

You'll need to step through the Sound::Load function in the debugger to see why your file is failing. stb vorbis is used, so it may not support particulars of your file.

---

Also, OggVorbisSoundStream is the resource type you probably want to use for music, not Sound. Sound loads the entire audio file (decoded if ogg) into memory, OggVorbisSoundStream incrementally decodes while playing.

-------------------------

KerMatt | 2018-12-19 11:50:17 UTC | #5

Thanks! turns out it must've been an issue with the file. stepped through the load function like you said and it wasn't reading it in properly. Do i need to include any header files for a OggVorbisSoundStream?

-------------------------

Modanung | 2018-12-19 12:17:46 UTC | #6

I'm not sure if using a sound stream could work if using the sample as `Sound` doesn't work. Maybe streams are more versatile, but you could try changing the samplerate or bitrate of the audio file first.
On Linux I use [SoundConverter](http://soundconverter.org/) for this: `sudo apt-get install soundconverter`

Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

Sinoid | 2018-12-19 19:13:04 UTC | #7

> I’m not sure if using a sound stream could work if using the sample as `Sound` doesn’t work.

If specifics of the vorbis file are the problem, it won't matter since both use stb vorbis.

Only real thing that can be done is to open up the file in a DAW/audacity/etc and see if there's anything odd about the format/encoding/bitrate as stb vorbis isn't very clear about what it supports other than multi-voice not being supported.

-------------------------

