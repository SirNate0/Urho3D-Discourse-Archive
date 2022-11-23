Blackfox | 2018-06-21 08:46:07 UTC | #1

Can I find anywhere balls shooter example. I dig into 11_physic.as example, but there are no classes objects, only rigid physic. Then I look 05_animation*** example. I nearly find answer. Here instances of "rotator" class attached to every created node, and node can be controlled by using update function of rotator class. 
Is every box.mdl loading into memory for each node?
I nearly get what I want, but I need destructor for rotator object, how can I do it? Maybe It`s simple, but I long time no programming and what will be with node, when attached instance of rotator will be destroyed (how can I destroy node?)?

-------------------------

jmiller | 2018-06-22 20:28:43 UTC | #2

Hi,

[quote="Blackfox, post:1, topic:4336"]
Is every box.mdl loading into memory for each node?
[/quote]
No worries; Urho3D does hardware instancing.
  https://urho3d.github.io/documentation/HEAD/_rendering.html#Rendering_Optimizations

https://urho3d.github.io/documentation/HEAD/index.html

Several sections like **Scene Model** and **Object types** seem relevant to your questions.
Script API docs are near the end of the page.
There is Node::Remove() and Component::Remove()..
Otherwise, SharedPtr objects (like nodes kept by **Scene** and components held by nodes) are automatically deleted when going out of scope.

-------------------------

Blackfox | 2018-06-24 07:14:48 UTC | #3

Thank you very much. As I can understand all objets destroyed by node.remove. Ninja.as too. It works.

-------------------------

