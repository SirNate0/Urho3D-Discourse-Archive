indie.dev | 2017-01-02 00:58:37 UTC | #1

When I add an new AnimationController component into the scene I find no attributes of it... the atrribute inspector panel is empty.
How can I use this to controll the animation?
Thanks.

-------------------------

cadaver | 2017-01-02 00:58:37 UTC | #2

AnimationController doesn't expose the animations it's playing in a meaningful way that would be editable; instead it's meant to be called from code.

You can make a little helper script and attach it to the same node; by live-editing the animationName string you can make it play animations, when the scene update is running, for example:

[code]
class AnimationTest : ScriptObject
{
    String animationName;

    void Update(float timeStep)
    {
        AnimationController@ ctrl = node.GetComponent("AnimationController");
        ctrl.PlayExclusive(animationName, 0, true);
    }
}
[/code]

-------------------------

indie.dev | 2017-01-02 00:58:37 UTC | #3

That makes sense!
I'd try your suggestion, thank you very much!

-------------------------

