mrchrissross | 2018-11-19 16:31:19 UTC | #1

In Urho3D is there an easy way to implement an explosion? 

For example, I have missiles in my game and I would like to instantiate an explosion for when they collide with something.

Any help would be greatly appreciated, thank you.

-------------------------

JTippetts | 2018-11-19 16:49:32 UTC | #2

You're probably going to be using a combination of different effects to achieve an explosion: UV animated geometry, particle systems, full-screen whiteflash if the explosion is powerful enough, etc... For a jumpstart on some ideas, you might check out this [game art trick](https://simonschreibt.de/gat/fallout-4-the-mushroom-case/) regarding mushroom clouds in Fallout. It uses a combination of various systems to simulate the components of a mushroom cloud explosion, and it goes into discussions of a number of different techniques that you can use.

-------------------------

mrchrissross | 2018-11-19 19:01:05 UTC | #3

Hi, thanks a lot for the reply, unfortunately I'm currently doing a space game. Mushroom clouds may not make much sense in my game as there wont any solid ground around the player. I'm just looking for a simply explosion like the ones you typically get in a game where a player dies by explosion or a simple grenade type explosion.

Again thanks so much for the reply :slight_smile:

-------------------------

JTippetts | 2018-11-19 19:09:56 UTC | #4

Well, most of the same tricks should still apply. The only difference is the columnar shape. You'll still make use of the same kinds of techniques, that's why I suggested that article as a jumping off point. It talks about the kinds of billowy textures you'll want, color grading them, adjusting alpha and falloff to smoke colors, etc...

-------------------------

Sinoid | 2018-11-19 19:37:49 UTC | #5

At its' simplest you can create a node with a `ParticleEmitter` that's set to `auto-remove` at the explosion location. 

If you need debris/shrapnel you can use `Scene::Instantiate____` functions to insert a *prefab* and iterate over it's contents applying physics forces as necessary (ie. radially from center, in a cone around contact normal, etc).

If you need to apply a *blast wave* of physics forces you can use an expanding sphere query over-time (keyed on whatever physics mask is desired) and apply forces as needed.

If you need a visual *shock-wave* you can use a model and an `AttributeAnimation` on it's scale along with material-animation for any fade/ramp. Model is a bit more versatile than a BillboardSet here since the shock-wave can then be whatever (a *shell*, a *card*, *death-star exploding ring mesh*, w/e) and oriented however (along normal, looking at view, randomly, etc).

---

There's a ton of different ways you can tackle it depending on what you want.

-------------------------

WangKai | 2018-11-22 12:03:17 UTC | #6

Also, you can use camera shake to make the impact shocking :grin:
You could move the camera in update or make camera animation in Blender or something and export the animation and then apply the animation to the camera.

-------------------------

Modanung | 2018-11-22 12:09:41 UTC | #7

@WangKai Something like this?
https://discourse.urho3d.io/t/execute-code-over-time-camera-shake-example/4664

-------------------------

WangKai | 2018-11-22 12:14:57 UTC | #8

Exactly! And pre-made animation can be very high quality but static.

-------------------------

Dave82 | 2018-11-24 00:36:48 UTC | #9

The best way is to someone (probably someone with more spare time than me) expand the current particleEmitter class and implement template based interpolators for various parameters (e.g scale , velocity , gravity , force , etc) very similar like how in SPARK was done.
[code]
<interpolator>
  <param = Scale|Rotation|Velocity|Force|Color|Texcoord|Texture />
  <type = Constant|Graph|Random />
  <operation = Add|Subtract|Multiply|Override />
  <values = "value , time" />
</interpolator>
[/code]

Note : There is a Texture param which could be a really useful parameter.Using two different textures (Perhaps diffuse and enviroment)  and fade into each other.Just imagine a yellow flame texture fades into a grey smoke texture.

-------------------------

Sinoid | 2018-11-27 04:11:31 UTC | #10

@Dave82

I don't think there's **that** much missing from the built-in particles.

The only changes I've had to make:

- Emissions
    - Ring (min degree -> max degrees, with axis)
    - Point-list, point cloud with velocity
    - Edge-list, line-strips that particles follow from start to finish
    - Inner distance on sphere/ring/cone emitter
- Card facing mode (in local transform space), it always orients the particle to face the local Y axis `Quaternion(90, Vector3::RIGHT) * rotation`
    - It's like the Quake3 plasma-rifle hit effect basically (twirl some cards aligned to Y-up)
- Velocity rotation around a local axis, for twists and pseudo-vortices

Path-following GIF: there's a wagon-wheel illusion with the gif framerate, they actually go up - not down

https://imgur.com/a/i3rCFxQ

I could make a PR for those changes.

---

Only really major thing I feel missing is aggregate effects so multiple emitters with different effects sort together - that'd be full of of hacks though so I haven't touched it. Means same material, same FaceCameraMode (shader cares), etc. Only the emitter behaviour can really change. 

That's arguably a small price to pay to not have to use 8 different partial ring emitters so ring particles don't render in-front of a plume.

---

**Edit:** cleaning up what I have and porting it back to master (aka: actually testing the daylights out of it). Aggregate effects were actually really trivial once I set down to it (let the children all be but deny them rendering responsibility, master memcpy's their billboards into itself - done and not insane), though the constraints I mentioned still apply.

-------------------------

