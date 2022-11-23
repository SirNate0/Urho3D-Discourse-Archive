Pyromancer | 2017-01-02 01:07:28 UTC | #1

Heyo! Gotta say, I've been tinkering with this engine and I really love how it is set up! The code is very straightforward and simple to understand, and leaves the user with the same level of fine-grained control that I am used to working with at my day job. However, one of the best features of any reflection system, I feel, is the ability to query the system and discover if one type inherits from another and (or implements, in the case of interfaces) traverse the inheritance hierarchy. Unfortunately, I did not see any obvious way of being able to do this through reading the documentation and was wondering if anyone could provide some insight. I noticed that there is a way to query for the base type of an object, but that only gets me so far for what I have in mind. I modified the Context to provide this sort of functionality easily enough (among other things, including some expansions to the OBJECT macro to make use of a helper class I wrote that makes the definition of classes much nicer to look at... And maaaaaybe I added user-definable properties to the AttributeInfo class :laughing:), but I was wondering if there was perhaps a built-in way to check these sorts of things.

-------------------------

cadaver | 2017-01-02 01:07:29 UTC | #2

No, there isn't built support apart from what you have already seen. Dynamic casts are sometimes used in the engine code itself to detect base/derived connections.

If your improvements don't impact memory use or performance overly negatively, they could be useful for everyone as a pull request.

-------------------------

Pyromancer | 2017-01-02 01:07:29 UTC | #3

EDITED!

Alright, so I lied. I decided to try applying the class definition helper to everything that leverages the reflection system, and so far it's been working beautifully.

An example of what I'm working on that would be exposed to the end user. The RegisterObject static function is being abstracted away from the user and wrapped into the existing OBJECT macro as well as being implemented through what is basically a DSL for the engine. 

[code] // Audio/SoundSource.h
// Nothing to change except removing the outward facing definition of RegisterObject. The OBJECT macro is modified to do that for you.

// Audio/SoundSource.cpp
REGISTER_OBJECT(SoundSource) // Defines SoundSource::RegisterObject under the hood, though there's a bit more than that going on.
{
    // Couldn't avoid this, otherwise we wouldn't have our snazzy curly braces.
    // Also, since we are technically in a function block here, we could do logical inclusions and exclusions of certain attributes.
    Definition
    .Base<Component>() // Added to a helper structure under the hood.
    .Attribute<bool>("Is Enabled",         &SoundSource::IsEnabled,       &SoundSource::SetEnabled, true)// AM_DEFAULT set as the default for calls that don't have any modes set.
    .Attribute<ResourceRef>("Sound",       &SoundSource::GetSoundAttr,    &SoundSource::SetSoundAttr, ResourceRef(Sound::GetTypeStatic()))
    .Attribute<String>("Type",             &SoundSource::GetSoundType,    &SoundSource::SetSoundType, SOUND_EFFECT) // Mixed call attributes? Mixed call attributes.
    .Attribute<float>("Frequency",         &SoundSource::GetFrequency,    &SoundSource::SetFrequency, 0.0f)
    .Attribute<float>("Gain",              &SoundSource::GetGain,         &SoundSource::SetGain, 1.0f)
    .Attribute<float>("Attenuation",       &SoundSource::GetAttenuation,  &SoundSource::SetAttenuation, 1.0f)
    .Attribute<float>("Panning",           &SoundSource::GetPanning,      &SoundSource::SetPanning, 0.0f)
    .Attribute<bool>("Is Playing",         &SoundSource::IsPlaying,       &SoundSource::SetPlayingAttr, false)
    .Attribute<bool>("Autoremove on Stop", &SoundSource::GetAutoRemove,   &SoundSource::SetAutoRemove, false, AM_FILE)
    .Attribute<int>("Play Position",       &SoundSource::GetPositionAttr, &SoundSource::SetPositionAttr, 0, AM_FILE)
    ;
}[/code]

Personally, I think this is much nicer to look at than the collections of macros that currently exist. The helpers I am writing also take the liberty of calling Context::RegisterFactory for you so that it's one less thing to forget.

The one downside is that I haven't yet implemented support for memory offset based attributes. Since the Urho3D reflection system uses offsetof under the hood rather than pointers to member fields, it might require a bit more work. I'll also be adding a REGISTER_OBJECT_NO_FACTORY macro for objects that you didn't tell the context to make a factory for (such as what seems to be the case with Drawable).

I will update when I have more done.  :mrgreen:

-------------------------

