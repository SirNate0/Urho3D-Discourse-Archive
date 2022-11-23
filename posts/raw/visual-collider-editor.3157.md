smellymumbler | 2017-05-24 18:29:16 UTC | #1

Is there any way of editing colliders with some visual feedback? Maybe i'm too much of a noob using the editor, or maybe there's a better way in code?

-------------------------

slapin | 2017-05-24 20:10:10 UTC | #2

Well, being noob myself I prefer to make my own tools for my specific needs.
For me, the Editor barely can do what it intends to do, so I never had successful experience with it.
So I do everything in code and make visual tools when I need them (i.e. to combine models from parts).
The Editor can be used as reference to code your own tools though. If I was doing some artistic level design
though I probably would try to use editor again, but to the point I still  not managed to do anything useful with
it.

-------------------------

smellymumbler | 2017-05-24 20:51:25 UTC | #3

...so, you did your own collider editor? Or you edit the code, compile & run and check the debug view, rinse & repeat?

-------------------------

slapin | 2017-05-24 20:57:03 UTC | #4

No, I use model bounding box for rough collider and convex hull for precise one, sometimes switching on the go.
For strange things I use various raycasts/spherecasts.
I generally do not do anything about colliders.
For various trigger stuff, like "awarenes zones" I do not have idea yet, but I think I could just use box or sphere.

I generally never seen problems with colliders in Urho, but I always learn something new, so I might need some visual editor for them, but not ATM.

-------------------------

smellymumbler | 2017-05-24 21:00:26 UTC | #5

You need custom colliders for every complex geometry. Plus, if you are working with ragdolls, you need a visual way to tweak each and every bone.

-------------------------

slapin | 2017-05-24 21:15:41 UTC | #6

I writtem my cool worthy shitty script for ragdoll which more or less automates ragdoll on makehuman skeleton. If only it were not prone to pass through material. But no, you don't need any visual tools for that. At least that tool should be very carefully done specially for ragdolls. Urho editor can make an example. You can setup ragdoll in it if you don't need any extra dynamics/switch from/to ragdoll on the go. But you will not want to live after that.

I heard that artists are kind of folk which often select most mundane workflows and use extremely hard tools for doing their work, but I'm not an artist. I can't draw 1000s of pics or 150 3d models just for different situation. If that can be done in code, I'll do it in code, as it is much simpler than all this drawing and tweaking, crashing and loading. I know my art will always suck this way, but I'm lazy person, I can manage this way. I go to blender and do my drawing only if I'm out of ideas on how to do it in code or I need compromise for performance sake.

-------------------------

