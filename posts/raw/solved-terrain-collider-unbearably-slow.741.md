setzer22 | 2017-01-02 01:02:35 UTC | #1

Hello all!

NOTE: For anyone that might have seen the old post I deleted that one because the issue isn't fixed. I got confused.

So I have a simple scene with a rigidbody (capsule collider attached) and a terrain (terrain collider attached). Even with such a simple scenario the Physics simulation is taking 30ms on average per update, going all the way up to 100ms at some moments. 

Even with a debug build I don't think this is too much for my computer. I have a more than decent processor (an 4 year old intel i7) and I've used Terrain Colliders in other engines without a problem. If a Terrain would be so much of a performance killer I don't think they would exist in any single engine out there nor they would be used in many games. It seems like I'm missing something, or there's actually a problem somewhere with terrain colliders.

The issue is even worse when any more complex collision detection is being done, like "climbing" a mountain in the terrain.

Any ideas?

-------------------------

cadaver | 2017-01-02 01:02:36 UTC | #2

How is your performance in the VehicleDemo sample, which has a moderate-sized terrain and a car (cylinder & box colliders + constraints) moving against it? I get about 0.5 ms maximum for physics in RelWithDebInfo and 3.0 ms max in Debug.

-------------------------

rasteron | 2017-01-02 01:02:36 UTC | #3

@setzer22

Yes, at least try out the VehicleDemo sample first and compare your results :slight_smile:

-------------------------

rasteron | 2017-01-02 01:02:37 UTC | #4

..downloaded and recompiled the latest git version. Launched the sample vehicle demo (AS) and it runs at 200 FPS fullscreen 1366x768 on my GTX 650 i5 setup


[video]https://www.youtube.com/watch?v=-D-ZkvDW8-M[/video]

-------------------------

setzer22 | 2017-01-02 01:02:37 UTC | #5

Ok, something's definitely wrong with my code, as the 19_VehicleDemo script works flawlessly (physics simulation takes almost no time).

Should I open a new thread to ask about my issue or ask here?

For now I'll provide a bit more data that might be relevant:

- The rigidbody is being moved by an script that calls SetLinearVelocity each FixedUpdate frame, although removing all that code doesn't fix a thing.

- The terrain is set up with a terrain collision shape (set to terrain, everything else default settings) and a rigidbody (no mass, set to isKinematic). 

- The character is a node with the following components: AnimationController, AnimatedModel, CollisionShape (capsule), RigidBody (mass 75, gravity (0,-100,0), And also a custom component that's not really relevant for the physics. I should also say that the whole node has a scale value of 10.

- Trying to deactivate the the character node successfully removes the lag. Using anything else, like a sphere, also creates some undesired lag (much less though, something like 13-14ms). Anyway that's much more than what I get for the VehicleDemo. I'll keep looking at the issue myself...

Any ideas?

-------------------------

thebluefish | 2017-01-02 01:02:37 UTC | #6

There definitely sounds like a problem with your setup. I have an 8 year-old dual-core and I'm getting ~80-100 FPS in the vehicle demo as well.

Can you post a sample project?

-------------------------

setzer22 | 2017-01-02 01:02:38 UTC | #7

This is weird indeed.

I'll try to isolate the issue in a small project and if I don't figure it out by myself I'll upload it here. I'll edit the post once I have it.

Thanks for your help so far!

[b]EDIT:[/b] After removing all code I made from the project the issue still remains. I've made this sample project:

    [dropbox.com/s/lzv7oretb3zur ... ar.gz?dl=0](https://www.dropbox.com/s/lzv7oretb3zurgy/PhysicsTest.tar.gz?dl=0)

To compile it (URHO3D_HOME should be defined and point to the Urho3D git root in your machine). In a Unix environment:

[code]cd Build
cmake ../Source
make #(or whatever cmake generated for you)[/code]

Nothing too fancy here, it's just an out-of-source build Using Urho3D as an external library as described in the documentation. I thought it would make it easier for you to build it.

And to run it you should tell it the resource path, both the default resource paths from Urho and this project's resource path. I run it like:

[code]PhysicsTest/Bin/MainPhysicsTest -p "$TESTPHYSICS_HOME/PhysicsTest/;"$URHO3D_HOME"Bin/Data/;"$URHO3D_HOME"Bin/CoreData/" -w -s[/code]

I chose this example because I get a particular BAD framerate, way worse than I've described before. I tried to use all resources from Urho3D, although the heightmap it's one I did myself (maybe that's the issue? Its size is 512x512, Nothing too heavy for a modern CPU). The profiler is already on.

I've also made a video to show the awful framerate I'm getting if you just want to look into the code (framerate is actually a bit better but you can clearly see the problem in the profiler numbers):

[webmshare.com/o8rgv](http://webmshare.com/o8rgv)

Note that I've changed the heightmap there, this one came with Urho so I guess my heightmap's not the issue.

-------------------------

jmiller | 2017-01-02 01:02:38 UTC | #8

Hello setzer22,
I built and tested your app. The density of Terrain (in conjunction with a CollisionShape) affects how many contacts Bullet has to resolve. The sim is smooth if you change 
[color=#0080BF]<attribute name="Vertex Spacing" value="0.1 0.1 0.1" />[/color] to [color=#0080BF]<attribute name="Vertex Spacing" value="1 1 1" />[/color]

When the capsule is upright, it's contacting less of the terrain's shape and performing better. When it's lying on its side, there are more contacts (whether Bullet is being optimal here, I can't say for sure). Turning on debug geometry could help visualize issues.

Other ways to optimize CD could be changing gravity, CollisionShape, RigidBody, etc.
Can also use different collision layers so different objects perform differently.

-------------------------

setzer22 | 2017-01-02 01:02:38 UTC | #9

Yes, it appears that lowering the vertex spacing makes things a lot more smooth. Even though that increases the size of the terrain, and scaling it down makes the lag come back. Any tips on how can I change the size of the terrain while keeping the low vertex density then?

Also scaling everything up (so the capsule is bigger) results in the same lag as before. And keeping the same vertex spacing as in my example but making the capsule smaller makes lag go away.

-------------------------

jmiller | 2017-01-02 01:02:39 UTC | #10

Can think of nothing else specific at the moment, just trying to reduce the number of collision pairs that occur in the physics step.
Physics world parameters, CollisionShapes, RigidBody parameters, forces.. some combinations can get out of hand.

Some web searching [b]btHeightfieldTerrainShape[/b] (or Bullet collision pairs in general) will probably find this issue being discussed.

-------------------------

devrich | 2017-01-02 01:02:39 UTC | #11

[quote="setzer22"]Yes, it appears that lowering the vertex spacing makes things a lot more smooth. Even though that increases the size of the terrain, and scaling it down makes the lag come back. Any tips on how can I change the size of the terrain while keeping the low vertex density then?

Also scaling everything up (so the capsule is bigger) results in the same lag as before. And keeping the same vertex spacing as in my example but making the capsule smaller makes lag go away.[/quote]

I have a crazy thought and I don't know if it'll work but could you try keeping the scale of the terrain as you had before and [i][u]then instead of making the capsule smaller[/u][/i] change the physics shape to something other than capsule? like box or mesh ( or maybe make your own semi-capsule but with less curvy detail and using that but set the physics shape to mesh because you are supplying the capsule which bullet wouyld interpret as a mesh ) ?

if the lag goes away or gets better then that may be a work-around.

In either case; i suspect that bullet may be doing some extra calculations on the lower-end of the built-in capsule againt the terrain.  This may be due to complex ( lots of smaller ) triangle structure of the terrain. if that's the case then it would explain why making the terrain's scale larger removes the lag because then bullet doesn't have to go through as many calculations.  In that case the easier solution might be to determine what paths your characters would be traveling and make those paths use larger triangles to decrease the amount of physics calculations that bullet needs to do on them...


I don't know if any of that helps or not but good luck.  :slight_smile:

-------------------------

setzer22 | 2017-01-02 01:02:40 UTC | #12

[quote="devrich"]If that's the case then it would explain why making the terrain's scale larger removes the lag because then bullet doesn't have to go through as many calculations.  In that case the easier solution might be to determine what paths your characters would be traveling and make those paths use larger triangles to decrease the amount of physics calculations that bullet needs to do on them...[/quote]

It's very possible that that's the case. Is there a way to define the size of the triangles with the current Terrain code? Or should I dive into the implementation (or model the terrain shape by myself...).

-------------------------

jmiller | 2018-09-14 16:00:58 UTC | #13

Depending on the resolution you need, maybe you could use two Terrains: one for only rendering without a CollisionShape, and a collision terrain generated from a downsampled version of the heightmap, scaled to fit?

[b]edit:[/b] Note some resampling methods (Lanczos, sinc... in apps like The GIMP) popular for images create values outside the original bounds.  I found that topic illustrated:
https://gis.stackexchange.com/questions/10931/what-is-lanczos-resampling-useful-for-in-a-spatial-context

As far as modeling.. heightmap CD is supposedly faster than hull/mesh-only collisions. In some cases a combination works.

-------------------------

setzer22 | 2017-01-02 01:02:41 UTC | #14

What you suggested works nicely as a workaround, for now I'll use that. 

Thank you all for your time and help!

-------------------------

