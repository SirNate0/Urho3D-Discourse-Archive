Modanung | 2017-01-02 01:11:14 UTC | #1

This [url=http://discourse.urho3d.io/t/jack-animation/1877/1]thread[/url] inspired me to start on this [url=http://luckeyproductions.nl/B4W/ahab.html]Ahab[/url] character yesterday.

I intend to add:
- Idle, walk and run animations
- Diffuse and specular textures

-------------------------

1vanK | 2017-01-02 01:11:14 UTC | #2

Its great :). When choosing a character should be considered model will be used in ragdools example, so I think, model shuld has tight clothes

-------------------------

Modanung | 2017-01-02 01:11:16 UTC | #3

[quote="1vanK"]When choosing a character should be considered model will be used in ragdools example, so I think, model shuld has tight clothes[/quote]
I shortened his coat. Would that suffice?

-------------------------

1vanK | 2017-01-02 01:11:16 UTC | #4

[quote="Modanung"][quote="1vanK"]When choosing a character should be considered model will be used in ragdools example, so I think, model shuld has tight clothes[/quote]
I shortened his coat. Would that suffice?[/quote]

I think yes :)

-------------------------

Modanung | 2017-01-02 01:11:17 UTC | #5

I also added a rig with exactly 32 bones and a first pose.

-------------------------

weitjong | 2017-01-02 01:11:17 UTC | #6

Cool! Not cute (kawaii in Japanese) as I have hoped though  :wink:

-------------------------

Modanung | 2017-01-02 01:11:20 UTC | #7

[quote="weitjong"]Cool! Not cute (kawaii in Japanese) as I have hoped though  :wink:[/quote]
He's more kawaii now; Ahab can now smile and blink.
[img]http://luckeyproductions.nl/ahab_kawaii.png[/img]

-------------------------

1vanK | 2017-01-02 01:11:20 UTC | #8

[quote="Modanung"]
He's more kawaii now; Ahab can now smile and blink. ;)[/quote]

He needed a bandage on the eye, leg prosthesis, saber and parrot :)

-------------------------

Modanung | 2017-01-02 01:11:23 UTC | #9

Testing with [url=https://vimeo.com/159730688]ragdolls sample[/url]. Ahab's bones are oriented differently than Jack's. I seemed to have fixed the colliders, but the constraints are a bit more tricky.

-------------------------

weitjong | 2017-01-02 01:11:23 UTC | #10

No, I think the way Ahab's fall currently is the cutest part.  :laughing:   Thanks for the work.

I believe you have used debug renderer to debug the problem. I think it should be possible to slow down the animation speed and use a pre-defined random seed (should be already the case) and configure the sample to fire a single precise canon ball to hit a Ahab each time you start the sample (or just start the ragdoll sequence immediately at start). This way the ragdoll bones and constraints can be fine tuned to your heart's content easily because you can verify the result in a deterministic way. Too bad our editor cannot help with that.

-------------------------

Modanung | 2017-01-02 01:11:23 UTC | #11

Thanks for the tip. I turned the [url=https://vimeo.com/159734545]timescale down[/url]. :slight_smile:

-------------------------

Modanung | 2017-01-02 01:11:26 UTC | #12

Having a [url=https://vimeo.com/160036284]blast[/url]. :wink:

-------------------------

