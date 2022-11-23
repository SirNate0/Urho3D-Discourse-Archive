att | 2017-01-02 00:58:52 UTC | #1

I need to blend two different animations just like orge3d, did Urho3D support this feture?

-------------------------

cadaver | 2017-01-02 00:58:52 UTC | #2

Yes and no. We support simultaneous playback and blending between multiple animations. The animations can also be applied partially to a skeleton (with per-bone weight control as the most fine-grained level) and the blending order or priority can be controlled. NinjaSnowWar demonstrates this.

However we do not have "difference" or additive animations like Ogre does. In Ogre every animation is a difference from the bind pose, whereas Urho stores absolute local position & rotation of the bones. Ogre's advantage is that using the additive mechanism it can apply a "modifying animation" to existing animations, but the disadvantage is that the animation data is totally dependent on the bind pose and if you play back incompatible animations with too large weight values, you can totally mutilate your character.

-------------------------

