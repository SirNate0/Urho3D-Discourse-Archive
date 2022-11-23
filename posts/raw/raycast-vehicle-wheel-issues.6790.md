evolgames | 2021-04-07 07:27:37 UTC | #1

Ive been messing around with a raycast vehicle for a while now. The wheels keep getting stuck in the floor. Changing the settings to prevent this results in less realistic motion. The default gravity is far too low in my opinion. Using something like -20 or lower seems to look a lot better. Ive looked examples online and they seem to have the same floaty look to them. Is there a smarter way to do this? My vehicle will be doing lots of stunts and I can't have the wheels so finnicky. But gravity lighter than -20 looks awful.

Do wheel raycasts get false positives from the hull of the car? I tried changing the hull collision shape and it was less error prone. I tried putting collision shapes on the wheels too but that made things worse. It feels silly to check if the wheels have sunk into the floor with raycasts, too.

I've tried Ccds, changing physics substeps and other ideas. Messing with suspension stiffness, compression, dampness, etc is like black magic. The settings are so interdependently sensitive.

Should I just go for a suspension made from hinges and sliders and physical wheels? Or is there something I can do to have raycast wheels/suspension behave without looking cartoony and floaty? The only times I've gotten them not to sink into the floor the car is bouncing off the ground and acts even worse. Thanks guys

-------------------------

Modanung | 2021-04-07 08:08:42 UTC | #2

What's your floor made of?

-------------------------

evolgames | 2021-04-07 14:32:28 UTC | #3

Just a box.MDL. same thing happenson terrain

-------------------------

Modanung | 2021-04-07 16:41:43 UTC | #4

What's the size of the vehicle; could it be scale related?

-------------------------

evolgames | 2021-04-07 18:03:05 UTC | #5

Hmmm, It's like 1 by .3.

-------------------------

Modanung | 2021-04-07 18:44:31 UTC | #6

Does the glitch occur when applying the same `PhysicsWorld` parameters to sample 46? There it's roughly the size of a wheel.

-------------------------

evolgames | 2021-04-08 05:07:48 UTC | #7

The problem goes away with default gravity, but then it looks floaty. I've tried to solve both but I can only seem to get one working at a time.

So I tried doing physical wheels like in sample 19 and it actually works really well. maybe I should do that, but make suspension with joints and stuff

-------------------------

Modanung | 2021-04-08 07:02:22 UTC | #8

[quote="evolgames, post:7, topic:6790"]
The problem goes away with default gravity, but then it looks floaty.
[/quote]

But does it occur *in* sample 46 after modifying it?

-------------------------

evolgames | 2021-04-08 15:52:52 UTC | #9

It doesn't! I finally figured it out, thanks. The reason it didn't work for me despite messing with nearly every setting is that the raycast wheel width/radius was too small I guess. I had lined mine up (the purple raycast lines in physics debug) with the actual limits of the static model, so mine were about half of these values. I also set all of the suspension settings to the same as the sample and -20 gravity works now. In my trial and error I never changed the wheel width/radius.

In the sample:
```
Wheel Width = .4
Wheel Radius  = .5
Raycast Wheel Node Scale = Vector3(1.0, 0.65, 1.0)
```

Changing wheel width to .2 is the deciding factor that (with stronger gravity) will submerge the wheels in the ground/terrain.

-------------------------

Modanung | 2021-04-08 17:20:08 UTC | #10

That's good to know; the vehicles in *OG Tatt* are about the same size. :slight_smile:

-------------------------

evolgames | 2021-04-09 01:34:03 UTC | #11

Not sure what that is. got a link?

-------------------------

Modanung | 2021-04-09 01:50:26 UTC | #12

Just one of many projects. ;)

https://gitlab.com/luckeyproductions/games/OGTatt

-------------------------

