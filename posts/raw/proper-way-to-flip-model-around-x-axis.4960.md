NessEngine | 2019-02-24 22:22:16 UTC | #1

Hi all,
Probably a noobish question I just recently started with Urho3d (great engine btw! :slight_smile: ), but what's the proper way to flip models around an axis?

I tried the obvious method, negative scale, but that seem to also flip the surfaces render direction, making culling work on the wrong side (model appears inside-out).

Is there a proper way to do this, or should I just use negative scale + change culling mode? (what I don't like about this method is that I need to duplicate the material).

Thanks!

-------------------------

Leith | 2019-02-25 04:51:29 UTC | #2

If I needed to mirror my geometry, I'd probably want to fix the art asset in Blender or Maya, rather than try to deal with it in code.
If I was to do it in code, and the model was static, I would negate the X (or relevant) component of every Vertex Position (and probably, every "U" Texture Coordinate) in the underlying Mesh(es).
If the model was skinned and animated, I would definitely be dealing with the issue in a modelling app, because now my changes have to be made to every single keyframe of every animation on that model as well as the base geometry - is the model symmetrical? If so, life is a little easier - good 3D artists know how to ensure that their geometry is perfectly symmetrical, and they usually do, because it means they really only need to create half of the model, and mirror geom to create the other half.
A final option is to create a modified vertex shader which flips the incoming localspace vertex position component prior to the (proj * view * world * position) calculation, and assign that shader to a modified Technique, and assign the modified technique to a material, jeez it sounds like a lot more work than just fixing the art asset, and causes more shader switching at runtime...

-------------------------

Modanung | 2019-02-25 05:39:34 UTC | #3

Maybe you could set culling to _none_? This _would_ of course be more expensive.

Also... welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

I3DB | 2019-02-25 05:43:30 UTC | #4

[How about use a Quaternion?](https://discourse.urho3d.io/t/how-to-set-rotation-and-position-using-quaternion-functions-in-urho3d/4507)

-------------------------

Sinoid | 2019-02-25 06:03:10 UTC | #5

For each odd-axis flip you have to flip the culling.

Whether you do that via culling switching or building a flipped index-buffer is up to you.

If you're flipping the raw geometry data (ie. not scaling) then you also have to flip the normals ... I can never remember the specifics regarding the tangents - IIRC, as long as you leave the UV coordinates unassed then all is well, if you touch them you have to recalc tangents.

Flip on both X+Y and you don't have to flip primitive winding, flip on all 3 and you do, etc.

-------------------------

Modanung | 2019-02-25 06:10:00 UTC | #6

Quaternions are generally used to specify rotations. Are you suggesting to use its _w_ component to scale the normals? If so a `Vector4` would make more sense to me.

[quote="Sinoid, post:5, topic:4960"]
Flip on both X+Y and you don’t have to flip primitive winding
[/quote]
If you're flipping twice, you might as well rotate. :upside_down_face:

-------------------------

Sinoid | 2019-02-25 06:16:34 UTC | #7

Rotation is not flipping, it's rotating. That should be obvious shouldn't it?

Flipping is is taking `basis - value`, in general cases the basis is `0` - but in others such as flipping a curve the basis of flip is `1` and not `0`.

When you flip UVs to deal with OpenGL's nonsense texcoords you don't rotate them, you literally flip them.

There are other *flips* though, when using reverse-z for instance you just specify the normalization in reverse and things work-out ... only available in gl4.4+ though. When statically determining visibility you do similar, reverse normal of the outer projection slope such that distance objects become larger than near ones.

-------------------------

NessEngine | 2019-02-25 09:58:10 UTC | #8

Woha lots of replies :) I'll try to address all:

1. Quaternions - as people mentioned rotation is not the same as flipping, and the models are not symmetrical enough to make 180 rotation look right.
2. Fix culling - despite not liking this option I tried this but lighting seems to be off, looks like it flip normals.
3. Animation / skinning - there's none it's static models.

I think it's best if I explained better what I'm doing since it's a little weird. Imagine humanoid robot-like creatures that are made of replaceable parts. Every creature is a node tree with all the parts (head, neck, torso, left shoulder, left hand...) and node-based animations. Every node got a mesh attached to it that moves with the node. Now these models can change, left hand can be a cannon model and right hand a blade, and later these can also change. Art style is low poly so the parts don't have to be smoothly connected.

Now my problem is this - if I make a cannon model that can be a hand, for example, I want to flip it when it's on the left hand side (right being the default), and duplicating all parts for left / right seems wasteful.

So now that you have all the info, sounds to me like vertex shared is the best approach right? Or would you recommend maybe doing the flip at the model level but in code rather than duplicating the files (ie for every part I load to create a clone model and flip it's geometry). What would be easier?

Thanks!

-------------------------

Leith | 2019-02-25 10:59:38 UTC | #9

we're working on similar concepts - i want to bond physics bodies to (bones on) models that have a scale node near the root, and attach stuff generally, without scale getting in my way
I recommend fixing the art asset, not doing it in code, its the road to hell, pathed with good intentions
For the record, its a bad idea to assume scaling and descaling will give you clean numbers - floating point is inherently inaccurate

-------------------------

I3DB | 2019-02-25 17:41:58 UTC | #10

[quote="NessEngine, post:8, topic:4960"]
want to flip it when it’s on the left hand side (right being the default), and duplicating all parts for left / right seems wasteful.
[/quote]

Apply a mirror image transform.

-------------------------

NessEngine | 2019-02-25 18:59:09 UTC | #11

@Leith nah I refuse to have all my model assets x2, I rather take the road to hell :slight_smile:

@I3DB I couldn't find anything like that in Urho3d docs, is this an extension or custom shader example? can you post link?

-------------------------

I3DB | 2019-02-26 01:44:39 UTC | #12

[quote="NessEngine, post:11, topic:4960"]
can you post link?
[/quote]

[This discusses the issue as I understand what you're looking for.](https://gamedev.stackexchange.com/questions/149062/how-to-mirror-reflect-flip-a-4d-transformation-matrix)

-------------------------

