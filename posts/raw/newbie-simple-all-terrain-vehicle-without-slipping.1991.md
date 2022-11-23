JulesW | 2017-01-02 01:12:07 UTC | #1

I am trying to make a simple Vehicle travel over the Terrain. I have copied the code from the 19: Sample set.  But using this Vehicle it slipping and sliding on moderate inclines.  I guess the pure cylinders on the Terrain surface acts like glass surface, without any real surface area or grip to climb inclines. 

I just want to model a simple 'all terrain' vehicle that can climb 40 degree inclines, without any slipping, toppling.  

But when I set and experiment with different values for  Friction to 1.0, Rolling Friction =0.8f, Restitution 0.25f, Angular damping 0.285 etc etc for the wheel bodies, and Terrain surface, I still get slipping, wheelspins, toppling vehicles. I have also tried to apply normal downforce, based upon the Downforce model used in the 19: Vehicle Sample, so that Friction force should be higher.   Its getting frustrating, as UrHo3D API is so powerful, but also too complex to achieve game effects for newcomers.  

Its all very complicated, when in Unity I can use Wheel Colliders and create a Vehicle pretty easily.  
Is anyone aware of any alternative Tutorial settings or  Examples in Urho3D for a Vehicle models, or an equivalent  Wheel Collider models.

-------------------------

jmiller | 2017-01-02 01:12:08 UTC | #2

Hi JulesW, and welcome to the forum.

Lumak posted a nice vehicle Sample which may be a helpful study: [topic1354.html](http://discourse.urho3d.io/t/btraycastvehicle-example/1306/1)
I have not done much comparison, but it uses wheelFriction = 1000, which if analogous to your setting is much larger.
It also seems the suspension design gives better contacts.

Also, a more functional forum search might turn up other relevant information for you:
[google.com/search?q=vehicle ... ophpbb.com](https://www.google.com/search?q=vehicle+site%3Aurho3d.prophpbb.com)

As you note, Bullet simulations can take some tweaking.
(probably unrelated to your issue, but PhysicsWorld::FPS and Scene::timeScale can even change the apparent mass of objects in motion).

-------------------------

