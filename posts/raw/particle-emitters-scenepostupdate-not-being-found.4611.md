Alex-DataSIM | 2018-10-22 17:57:37 UTC | #1

Hi, I'm currently messing around with Urho3d. It's a cool library with some nice features, first impressions are good. The intrusive ref counting for Urho's pointers is a bit iffy, but i've let it slide :)

So I've been messing around, built some objects and effects, and I have encountered an issue where my ParticleEmitter's ScenePostUpdate subscription isn't being found.

Some context..

Firstly, I was building a basic 'game' using a class 'Game' deriving from Urho3D::Application.
My scene, camera, everything was owned by Game. I built a ParticleEmitter, added it to a node which was a child of the scene and everything worked fine. I had a lovely torch like effect in my game!

After some time I found that I was going to want multiple scenes, and was going to have them all inside the Game::Start() function which is called by the Engine. This wasn't what I wanted, I want all scenes in a separate class so they can be switched between easily, whilst keeping my project clean. 

My solution to this was to create a new class 'World' deriving from Urho3D::Object. 
I structured this class virtually the same as how 'Game' was structured. It had a World::Start() function which was called inside Game::Start() which initialises all the same things that Game::Start() used to ( scene, camera, boxes, particleEmitter). However, now the event subscriptions were being setup through scene_->SubscribeToEvent() rather than just SubscribeToEvent(). ( This had something to do with 'Game' using the member function of its derived class 'Object' while my new class 'World' wouldn't let me do that.)

The end result of this transition was the paticleEmitter not showing on my screen. That was the only thing that had broken. I have tired a lot of different things to fix this with no result. 

After some debugging I think I tracked the bug down to the ParticleEmitter's subscription not being called correctly (ScenePostUpdate) OR the subscription itself isn't being setup correctly.

Any advice/help would be very helpful. Also, if anyone has any solutions to the issue of how to store scenes so they can be activated like modules that would be great.

EDIT: It wasn't Context::SubscribeToEvent it was Scene::SubscribeToEvent

Alex!!

-------------------------

Modanung | 2018-10-22 17:37:32 UTC | #2

I cannot find this `Context::SubscribeToEvent` method and your `World` class _should_ inherit it. That's probably where you should look.

Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

Alex-DataSIM | 2018-10-22 17:36:45 UTC | #3

Thanks for the welcome! I look forward to learning a lot here.

-------------------------

Modanung | 2018-10-22 17:39:22 UTC | #4

Could you share some of your code?

-------------------------

Alex-DataSIM | 2018-10-22 17:41:58 UTC | #5

Yeah okay. It's currently in a private repo, I will make a public repo now to share it with all of you.

-------------------------

Alex-DataSIM | 2018-10-22 17:59:04 UTC | #6

Here is the repo with all relevant code. I removed some stuff you dont need to see so if it looks a little messy thats why :P

https://github.com/Vddox/urho3d-game

-------------------------

Modanung | 2018-10-23 07:40:08 UTC | #7

Unfortunately I don't see anything wrong with your code.
Do you get any error messages during run time? Are you sure the emitter is in view?

-------------------------

Alex-DataSIM | 2018-10-23 09:08:36 UTC | #8

No errors, and it should be in view. I created a box on the same node and it was at the correct coords. 

It is a super weird bug, otherwise I would have been able to work it out myself :confused:

Thanks for looking anyways.

-------------------------

Modanung | 2018-10-23 09:18:34 UTC | #9

Could you try leaving out `World`'s private `context_`? It already inherits this from `Object` to which it is passed through the constructor.

-------------------------

Alex-DataSIM | 2018-10-23 10:29:17 UTC | #10

Hi Modanung, 

I just tried what you asked, removed storing a shared pointer to context in my World and instead used the Objects context, this had no effect on my program.

-------------------------

