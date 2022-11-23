George | 2017-01-02 01:07:10 UTC | #1

It would be useful to have an override scene_->Update to take double value precision.

This is useful for developing realtime application.

Cheers
George

-------------------------

codingmonkey | 2017-01-02 01:07:10 UTC | #2

all moves two times faster - scene->SetTimeScale(2.0f);
 
[code]   /// Set update time scale. 1.0 = real time (default.)
    void SetTimeScale(float scale);[/code]

-------------------------

codingmonkey | 2017-01-02 01:07:11 UTC | #3

oh sorry, he about value precision. Update(float timeStep) -> Update(double timeStep)

-------------------------

cadaver | 2017-01-02 01:07:11 UTC | #4

Nearly all internally used values are floats so this would require a lot of changes to be useful.

If your purpose is using Urho for some sort of scientific application I would advise to do all calculations / updates in your own code and only use Urho as a dumb renderer, similarly how you would use Ogre.

-------------------------

George | 2017-01-02 01:07:11 UTC | #5

Thanks that is what I'm doing at the moment. 

However, I used Node::Translate(direction*deltaTime) for animation and moving child node over to different parent nodes when child node reach a certain distance. Over sometimes, space between child nodes changes.

Regards
George

-------------------------

cadaver | 2017-01-02 01:07:12 UTC | #6

For now you could maintain your own data structures which operate on doubles and just dump the values after your update into the Urho scene graph. This means however that you'll have to bring your own math classes / operations, since the Urho math is floats.

-------------------------

George | 2017-01-02 01:07:12 UTC | #7

Thanks cadaver,
I'll do that.

-------------------------

1vanK | 2017-01-02 01:07:12 UTC | #8

Timers and Sleep() allow to increase the precision?

-------------------------

cadaver | 2017-01-02 01:07:12 UTC | #9

No, the precision is already set to maximum (talking of Windows here.)

Use HiresTimer and busywaiting when you need more precision.

-------------------------

