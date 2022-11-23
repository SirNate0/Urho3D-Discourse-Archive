xalinou | 2017-01-02 01:12:42 UTC | #1

Hi! I'm just starting with Urho and i'm missing one of my favorite features from Unity: there's a bundled FPS control script, that you just have to attach to a capsule collider, and boom, you have some basic WASD + Mouse movement. For example:

youtu.be/-q_daB1aN8w?t=10m20s

Is there something similar for Urho? If not, maybe someone can help me answer the following questions:

[ul]
[li]How do i create a capsule collider? Do i need a capsule mesh?[/li]
[li]How can i render models in separate layers, to avoid weapon clipping?[/li][/ul]

-------------------------

hdunderscore | 2017-01-02 01:12:42 UTC | #2

Sample 18 Character Demo shows third person controller and can be toggled to a basic first person controller.

Capsule collider is just like any other collider, just that it has the CollisionShape shape type set to 'Capsule',  you don't need a mesh for it. You also need to pair it with a RigidBody component.

-------------------------

jmiller | 2017-01-02 01:12:42 UTC | #3

Hi

[quote="xalinou"]
[ul]
[li]How do i create a capsule collider? Do i need a capsule mesh?[/li]
[li]How can i render models in separate layers, to avoid weapon clipping?[/li][/ul][/quote]

To add to what hd_ says: In the Urho3D editor you can add CollisionShape and RigidBody components to a node and edit their properties visually, save the node as a prefab, etc. More here: [urho3d.github.io/documentation/H ... tantiation](http://urho3d.github.io/documentation/HEAD/_scene_model.html#SceneModel_Instantiation)

Question 2 (render order or layers) is similar to these:
[topic756.html](http://discourse.urho3d.io/t/how-to-layer-scenes/740/1)
[topic1284.html](http://discourse.urho3d.io/t/how-to-control-render-order/1240/1)
[topic2111.html](http://discourse.urho3d.io/t/render-order-usage/2015/1)

-------------------------

xelom | 2017-01-02 01:12:43 UTC | #4

@xalinou,

Hi, I'm new to urho3d and came from Unity as well. What's your reason for switching to urho3d recently?

-------------------------

Victor | 2017-01-02 01:12:43 UTC | #5

[quote="xelom"]@xalinou,

Hi, I'm new to urho3d and came from Unity as well. What's your reason for switching to urho3d recently?[/quote]

For what I'm doing, performance, flexibility, and API features, are reasons why I've switched. I was never using Unity for its Editor, for me I was just using it for the API. However, when it comes to performance and getting tied down to the Garbage Collection process, it was hard to come with with enough tricks in Unity to boost it. Plus, having access to the source code is very nice when you're trying to figure things out. I've also tried UE4, although for what I'm working on Urho3D is a much better fit, and the code is SO much cleaner. Don't get me wrong, Unity has a clean API, but Urho just feels like heaven when coding with it.

In the end, you need to figure out what the needs are for your game. All engines (to get their full benefit) will require you to get messy with the code. Even with UE4, if you try to use Blueprints for everything you'll start to notice some huge performance hits. Urho's shining feature (IMO) isn't its editor, but its clean code implementation and the API that goes with it. Again however, a person would need to figure what features their game needs to discover the engine that bests suits it.

-------------------------

xalinou | 2017-01-02 01:12:43 UTC | #6

Regarding the order layers: i don't think a proper solution was found. I've read all three topics and there are many drawbacks involved. Enhex has settled with the additional camera and viewport, which is a suboptimal solution because the arms/weapon model don't get any shadows. 

@xelom: i've moved from Unity because Urho3D is FOSS. Also, it offers better performance and that's crucial for VR.

-------------------------

