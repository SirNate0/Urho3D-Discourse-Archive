xahon | 2018-05-01 10:42:06 UTC | #1

I've created a simple model and rigged it and created 2 animations. In blender animations work well. When exporting through `Urho exporter` plugin this message pops up. ![image|506x396](upload://v4tTaTRD3mfaxwAML4GeUJ86Vgo.jpg)

In urho I'm creating `AnimationController` like this:

    void Character::Start() {
      animation_ = node_->CreateComponent<AnimationController>();

    //  animation_->SetTime("Test/Walk.ani", 0.0f);
      animation_->SetWeight("Test/Walk.ani", 1.0f);
      animation_->SetLooped("Test/Walk.ani", true);
      animation_->PlayExclusive("Test/Walk.ani", 0, false, 0.2f);
    }

After start it logs a lot of such warnings:
 
> [Tue May  1 19:38:56 2018] WARNING: Node Trunk5 not found for node animation Test/Walk.ani
> [Tue May  1 19:38:56 2018] WARNING: Node Trunk4 not found for node animation Test/Walk.ani
> [Tue May  1 19:38:56 2018] WARNING: Node Trunk3 not found for node animation Test/Walk.ani
> [Tue May  1 19:38:56 2018] WARNING: Node Trunk2 not found for node animation Test/Walk.ani
> ... and other bones excluding IKs, Poles, etc ...

Of course animation is not working in game, but model is ok
![image|639x388](upload://aB27XhVXcrLeMgs2cHmqQZ33TjH.jpg)

Here is how my model looks in blender
![image|411x354](upload://lmUwkkGcfcLa9wMf3Eg6xbcQ2Cy.jpg)

It has multiple root bones. Rear paws parented to `Root` bone and front paws parented to `Spine3`

I tried to export model with one bone (Cube) and it worked well in Urho3d. 
<strike>Is the problem because of multiple root bones?</strike>

I may be exported my object from blender wrong (https://github.com/reattiva/Urho3D-Blender/issues/84)

-------------------------

Eugene | 2018-05-01 17:37:15 UTC | #2

How does your scene look like in blender?
I haven't played with animation, but just model with skeleton exported fine for me w/o Derigifying
![image|270x263](upload://6T6TZeEWLQLAc2ExWV9PJ4o9bsc.png)

-------------------------

slapin | 2018-05-02 20:34:13 UTC | #3

What is version of blender?
What is your scene setup in blender?
Check if your node paths in animation are the same as paths in your scene.
i.e. you need to create your animation controller in the same node where you create AnimatedModel.

-------------------------

slapin | 2018-05-02 20:39:10 UTC | #4

Also if you use Rigify you need to know that currently Rigify from blender-2,79 will not export to Urho. Just in case.

If your bone set is created manually, there should be no problems (just keep bone count per geometry according to hardware limits (20, 32, 64). Also keep bones per vertex limit under 4, but I never had to care about this.

-------------------------

