shlomok | 2017-01-02 01:09:11 UTC | #1

Dear All,
I am looking at the SoundEffects demo:
[code]
void SoundEffects::HandlePlaySound(StringHash eventType, VariantMap& eventData)
{
    Button* button = static_cast<Button*>(GetEventSender());
    const String& soundResourceName = button->GetVar(VAR_SOUNDRESOURCE).GetString();

    // Get the sound resource
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    Sound* sound = cache->GetResource<Sound>(soundResourceName);

    if (sound)
    {
        // Create a scene node with a SoundSource component for playing the sound. The SoundSource component plays
        // non-positional audio, so its 3D position in the scene does not matter. For positional sounds the
        // SoundSource3D component would be used instead
        Node* soundNode = scene_->CreateChild("Sound");
        SoundSource* soundSource = soundNode->CreateComponent<SoundSource>();
        soundSource->Play(sound);
        // In case we also play music, set the sound volume below maximum so that we don't clip the output
        soundSource->SetGain(0.75f);
        // Set the sound component to automatically remove its scene node from the scene when the sound is done playing
        soundSource->SetAutoRemove(true);
    }
}
[/code]

What I would like to do is to select an audio file, display a checkbox(s) on the UI, when the chekbox is/are selected I want the audio file(s) to keep playing indefinitely. 
Is that possible?

-------------------------

Enhex | 2017-01-02 01:09:11 UTC | #2

Look at [urho3d.github.io/documentation/HEAD/_audio.html](http://urho3d.github.io/documentation/HEAD/_audio.html)
You can make an XML file with the same name as the audio file and tell it to loop.

-------------------------

shlomok | 2017-01-02 01:09:12 UTC | #3

That worked perfectly thanks.

-------------------------

