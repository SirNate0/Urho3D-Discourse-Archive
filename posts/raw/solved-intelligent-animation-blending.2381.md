slapin | 2017-01-02 01:15:04 UTC | #1

Hi, all!

I need help with my animations.

I have "idle" animation, "walk" animation and "breathe" animation.

I need to blend "breathe" into first and second. All animations are exported with translations and rotations
by exporter. 
As I see, it is not possible to blend cleanly, as it produce weird effect (as it uses full bone poses, i.e.
if body is rotated towards front by walk it will be straightened by breathe.
I had high hopes for Urho layered animation for this as I don't want to produce thousands of animations per character in Blender.
I can recombine them in Blender but it looks so 1990s. What is intended workflow?

Also how can I remove unneeded channels for blended-in animations like "breathe"? I just need rotations there.
I don't want to remove all channels by hand...

- Also, is it possible to use additive animation, i.e. translations are added to animations, rotations multiplied?

-------------------------

Dave82 | 2017-01-02 01:15:04 UTC | #2

[quote] Also, is it possible to use additive animation, i.e. translations are added to animations, rotations multiplied?[/quote]
By default there's no support for additive animations , but you can write your own in no time.I wrote my own for bullet hit "twitching" and weapon aim offset.

-------------------------

Lumak | 2017-01-02 01:15:05 UTC | #3

Blending a "breathe" animation with the other two would be tough, indeed, due to the use of spine joints.  Urho3D does has layered animation where you can layer a secondary anim to the main.  An example would be layering Mutant_Wave_LY.anim on w/e primary anim.  If I were to attempt to layer a "breathe" anim, I'd key only the upper two spines and make the movement more prominent.

-------------------------

slapin | 2017-01-02 01:15:05 UTC | #4

well, blending mode of ABM_ADDITIVE actually works great, so I don't need to do complicated things.

-------------------------

namic | 2017-01-02 01:15:10 UTC | #5

[quote="Dave82"][quote] Also, is it possible to use additive animation, i.e. translations are added to animations, rotations multiplied?[/quote]
By default there's no support for additive animations , but you can write your own in no time.I wrote my own for bullet hit "twitching" and weapon aim offset.[/quote]

Would you be kind enough to share some code, or even better, the research material you have used to write your implementation?

-------------------------

