patnav | 2019-03-08 22:45:13 UTC | #1

When using ParticleEmitter2D in network/replication context

It seems ParticleEmitter2D::SetEmitting doesn't call MarkNetworkUpdate ?

-------------------------

Leith | 2019-03-09 03:20:56 UTC | #2

It shouldn't need to.
URHO3D_ACCESSOR_ATTRIBUTE("Is Emitting", IsEmitting, SetEmitting, bool, true, AM_DEFAULT);

There is an attribute with default (disk +network) access mode. It should rightly be serialized automatically. The "setter" generated automatically contains the MarkNetworkUpdate, if I recall correctly.

-------------------------

patnav | 2019-03-10 20:06:19 UTC | #3

Thanks for your response

But SetEmitting is not a setter

I thnik MarkNetworkUpdate should be call like this:


    void ParticleEmitter2D::SetEmitting(bool enable)
    {
        if (enable != emitting_)
        {
            emitting_ = enable;
            emitParticleTime_ = 0.0f;
        
            // ==> Missing call ??
            MarkNetworkUpdate();

        }
    }

-------------------------

Leith | 2019-03-10 22:24:13 UTC | #4

The macro "URHO3D_ACCESSOR_ATTRIBUTE" automatically generates a getter and a setter for the named attribute.
Your class (which invokes this macro) derives from Serializable, which in turn contains a method called "Serializable::OnSetAttribute".
That method is called internally from the generated setter method, and the last thing OnSetAttribute does is call MarkNetworkUpdate (depending on the attribute mode flag, which is AM_DEFAULT = disk + networking).

I know, it's all hidden away and not as thoroughly documented as it might be, nonetheless it will just magically work, with one exception.
If your attribute contains the default value (defined by your URHO3D_ACCESSOR_ATTRIBUTE invocation), then it will never be serialized (on disk, or network). You have to change its value to anything other than the default value in order for the attribute to be serialized. This is a deliberate attempt to reduce unnecessary network bandwidth, but sure confused me for a while when I started playing with serializing/deserializing using files on disk.
It's also worth mentioning that the macro does not actually initialize the attribute to its default value!
It could, but it doesn't. You still need to manually initialize your attributes or they may contain random values at runtime - particularly in Release builds.

-------------------------

Modanung | 2019-03-11 06:32:35 UTC | #5

@patnav It seems like you may have found a bug. The ParticleEmitter2D was lacking the possibility to stop it from emitting without disabling or removing it [until about two years ago](https://github.com/urho3d/Urho3D/commit/448b3a66b1471185a72a0390075acc5ab2aae543#diff-88ca5a9c19d6b2fdfb300c86b8c02a8e). But it seems @kostik1337 forgot marking it for network updates.

I think you could just add the line and issue a pull request.

-------------------------

patnav | 2019-03-12 17:58:20 UTC | #6

Thanks for your response

Pull request:
[https://github.com/urho3d/Urho3D/pull/2430](https://github.com/urho3d/Urho3D/pull/2430)

-------------------------

