kestli | 2017-01-02 01:00:31 UTC | #1

I have a problem with [color=#0000BF]Urho3D::SoundSource3D[/color] sound does not start ...
I tried to do it from the code and visually from the scene editor but without success ...
From the scene editor works perfectly. When I open the scene from my program the sound can not be heard.
With [color=#0000BF]Urho3D::SoundSource[/color] I have no problems.
I use C ++ in VisualStudio 2013
Thank you

[code]
Sound                *sound;
SoundSource3D  *sound_source;

rscache->AddResourceDir(GetSubsystem<FileSystem>()->GetCurrentDir() + "/data/scenes/s1");

sound_source = box_node->CreateComponent<SoundSource3D>();

sound = rscache->GetResource<Sound>("sounds/shoot.ogg");

sound_source->SetEnabled(true);
sound_source->SetAngleAttenuation(360.0f,360.0f);
sound_source->SetAttenuation(2);
sound_source->SetFarDistance(100);
sound_source->SetNearDistance(0);
sound_source->SetGain(0.75);
sound_source->SetPlayPosition(0);
sound_source->Play(sound);
[/code]

-------------------------

Mike | 2017-01-02 01:00:31 UTC | #2

SoundSource3D requires a SoundListener component in the scene (audio->SetListener()).

-------------------------

