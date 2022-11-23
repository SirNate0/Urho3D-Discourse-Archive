slapin | 2017-05-16 16:14:19 UTC | #1

@Lumak could you please elaborate on how do you make cool car sound in your raycast vehicle demo?

Thanks!

-------------------------

slapin | 2017-05-16 16:17:35 UTC | #2

The reason I ask is

1. How to make good sound for car which is controlled by player, so the sound changes on speed,
accelerating/deccelerating, etc.
2. How to make sound for cars which pass player which is on feet?
3. How to make sound for cars which pass player, who drives his own car?

I could not get any way close to this, I want effects level of GTA3 or something.
There is some theory involved, I think, but I can't understand where to look for it.

-------------------------

Pencheff | 2017-05-16 17:39:17 UTC | #3

1. I would have different sounds for different RPM ranges. For example, 800-1200 RPM, 1200-2000, and so on. Depending on the RPM of the engine, you play the sound for that range (or a list of sounds so it doesn't sound monotonic and use some random function) and change the sound pitch. Sound for 800-1200 would be 1000 RPM, if you are running at 800, you pitch down the sound 10% of its speed.
2. Same as above, attach the sound to the moving car. Do some sound effect over maybe.
3. Same as above, car that passes the player has its sound attached to it, player's car has its own sound attached to it.

You can simplify step 1 with having only one RPM range (800-8000) and one sound, then pitch it up and down depending on the RPM speed but it would sound kinda boring. Changing gears is simple - every gear has some range of engine RPM, say gear 1 800-3000, gear 2 1000-3000, gear 3 1000-4000 and so on. These are random values that pop from my head, gear change depends on the driving style and the car model. 

I'm not in any way expert on this subject tho, but I've played alot of (driving) games and sims :)

-------------------------

Modanung | 2017-05-16 20:35:11 UTC | #4

Actually shifting gears is for keeping the RPM within a range of about roughly a 1000 to 2500 (highly dependent on both engine and situation) so the engine can do it's work best. That's why the frequency drops when you shift up. High RPM means more pulling power and cleaner burn, low RPM is more efficient fuel-wise.
When releasing the clutch with too low an RPM - and too much resistance on the driven wheels - the engine stops running. Too high an RPM for too long and it overheats.
That's mostly from first hand experience as a driver and passenger. ;)

Someday I plan to experiment with using ![SCIcon](http://supercollider.github.io/favicon.ico) [SuperCollider](http://supercollider.github.io/) in games and dynamic engine sounds would be one of the applications I'm looking to explore. Which would be synthesised with an RPM parameter read from the vehicle instead of bending the pitch afterwards. But maybe Urho's [sound synthesis](https://github.com/urho3d/Urho3D/tree/master/Source/Samples/29_SoundSynthesis) capabilities would suffice.

-------------------------

Lumak | 2017-05-16 19:06:28 UTC | #5

I watched this video [https://www.youtube.com/watch?v=GRMnN6Xd-yU](https://www.youtube.com/watch?v=GRMnN6Xd-yU)

-------------------------

