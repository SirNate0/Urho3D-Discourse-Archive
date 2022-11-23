GGibson | 2017-01-02 01:01:37 UTC | #1

Hi, I have a stereo audio effect playing in my scene, parented to a particular node/spot. As I move the camera/listener away I get the desired attenuation. However, if I pass by the sound source on either side then I can't actually tell which side the audio is coming from. NinjaSnowWar achieves more by playing a sound from left or right depending where it is in the scene, and you can hear roughly where explosions happen because of it, but I'm working in .cpp not .as so it's more difficult for me to learn from that example. Suggestions? It's as if you're wearing headphones listening to the sound and you turn the volume up or down depending how close you are to the sound source, so you can't tell which side of you it may be on.

[code]
// Snippet from where the listener is created
	 SoundListener* listener = cameraNode_->CreateComponent<SoundListener>();
	 GetSubsystem<Audio>()->SetListener(listener);

// Snippet from where the audio begins playing
	Sound* effect = cache->GetResource<Sound>("Sounds/effect.ogg");
	Node* effectNode = boxNode->CreateChild("soundEffect");
	SoundSource3D* source = effectNode->CreateComponent<SoundSource3D>();
	source->SetSoundType(SOUND_EFFECT);
	source->Play(effect);
[/code]

Edit
listener is parented to the cameraNode, and
source is parented to the node in the scene I walk around (boxNode).

-------------------------

GGibson | 2017-01-02 01:01:37 UTC | #2

So silly me I was thinking Urho would handle a stereo file just fine in spatialization, but no. It really only makes sense to spatialize a mono file, and Urho won't downsample for you. This is fine - I was just expecting it to work differently. Thanks to Scorvi for making a c++ version of NinjaSnowWar so I could verify I wasn't doing something wrong in code. (repo here: [url]https://github.com/scorvi/Urho3dNinjaGameExample[/url])

-------------------------

