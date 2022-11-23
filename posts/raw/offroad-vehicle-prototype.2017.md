Lumak | 2017-10-09 02:04:38 UTC | #1

Initial offroad vehicle prototype. I'll probably tweak it some more.

Let me know what you guys think about this.  Thx.

[b]Vehicle prototype: - replaced with the last vid created[/b]
https://www.youtube.com/watch?v=9ZAnvz2f_hU

[b]Video of AI vehicle pathing testing[/b]
Debug lines:
green - spline path
cyan - point on the path to follow
yellow - ai steering

https://youtu.be/THtkRu9Zrv8

-------------------------

hdunderscore | 2017-01-02 01:12:19 UTC | #2

Looks like a good start. Looks like you got it quite stable at high speeds - nice :smiley:

-------------------------

Lumak | 2017-01-02 01:12:19 UTC | #3

I'm glad that you got what I meant about the offroad prototype: it's about vehicle dynamics, not the model.

Surprisingly, stability can be easily gained when you move the CenterOfMass (CoM) forward a bit in addition to adding a downward force as seen in the 19_vehicle demo.

I'm trying to achieve offroad drifting dynamics.  I thought it worked well in an open terrain but following a track turned out to be a different story - needs more tweaking.

-------------------------

1vanK | 2017-01-02 01:12:19 UTC | #4

Nice! How do you make tire tracks?

-------------------------

Modanung | 2017-01-02 01:12:19 UTC | #5

Looks like a good start indeed. In its current stage it reminds of [url=https://duckduckgo.com/?q=big+red+racing&t=canonical&ia=videos]Big Red Racing[/url], good memories.
Keep it up! :slight_smile:

-------------------------

Lumak | 2017-01-02 01:12:19 UTC | #6

Thanks, Modanung, and also hd_ who I forgot to thank earlier.

1vank - I submitted a code exchange on how to create vehicle skid strips.

-------------------------

codder | 2017-01-02 01:12:19 UTC | #7

Nice! 
Now add some "realistic" damage to car. :slight_smile:

-------------------------

Bananaft | 2017-01-02 01:12:20 UTC | #8

Developing offroad games is fun, I'll watch your progress.

-------------------------

rasteron | 2017-01-02 01:12:21 UTC | #9

Looks great, I like those tire tracks effect as well. :slight_smile:

-------------------------

Lumak | 2017-10-09 01:00:42 UTC | #10

I waited to reply once I had an update.

[quote="codder"]
Nice! 
Now add some "realistic" damage to car. :slight_smile:
[/quote]
That would be cool.  I'll have to look into that.
[quote="Bananaft"]Developing offroad games is fun, I'll watch your progress.[/quote]
Yeah, it is. I enjoy it.  What's ironic is I've never bought a racing game, hah.
[quote="rasteron"]Looks great, I like those tire tracks effect as well. :slight_smile:[/quote]
I get my inspiration from watching you, enhex, and dave's progress on your games, so I try to do more.

[b]Video of AI vehicle pathing testing[/b]
Debug lines:
green - spline path
cyan - point on the path to follow
yellow - ai steering

https://youtu.be/THtkRu9Zrv8

-------------------------

extobias | 2017-10-08 21:02:25 UTC | #11

Hi Lumak,
I have a couple of questions. 
How did you synchronize ball speed with the car? I mean, in the vehicle you apply a force and the ball move at fixed speed. How this force is calculated?
And I know continuos steering is used, did you use dubins paths and all RSL,RSR, etc calculations? Or just adjunt the steering vector using the ball and vehicle positions?

Sorry for my bad english and thanks in advance.
Tobias.

-------------------------

Lumak | 2017-10-09 02:34:08 UTC | #12

I wrote a spline manager that: ai vehicle passes its position, direction,
look ahead distance, and the manager returns exact point on the curve
that the ai should steer to. This method is just a simple follow the spline
algorithm, something that I didn't have to research because it's so simple.
Steering method: adjust the steering vector using the ball and vehicle position.

If I were to actually implement an exact steering control on a restrictive
path, I'd look at this guys work -
https://www.youtube.com/watch?v=hsZVZ6lffzY&spfreload=5

-------------------------

Lumak | 2017-10-09 01:31:21 UTC | #13

or
https://www.youtube.com/watch?v=kkYmn3iBUew

github origin : https://github.com/udacity/CarND-Path-Planning-Project

-------------------------

extobias | 2017-10-10 08:03:57 UTC | #14

Thanks Lumak! this was really helpful.

-------------------------

Lumak | 2017-10-10 18:19:07 UTC | #15

And I just discovered this repo: https://github.com/udacity/self-driving-car-sim
for Unity, MIT license.

-------------------------

