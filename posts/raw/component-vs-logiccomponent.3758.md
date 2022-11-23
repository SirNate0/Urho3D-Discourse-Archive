Jetmate | 2017-11-19 03:06:49 UTC | #1

Beginner here. Are LogicComponents essentially just Components built for script? If so, how are they different?

Since I'm trying to write my project entirely from code (I haven't opened the editor a single time), when is it even necessary to use Components to implement code logic? For example, if I want to implement a Player class, should I create a Player component or implement a Player class that creates the node and encapsulate the logic in that class, rather than a dedicated component?

Final question - since Components have to have a Constructor that only takes a pointer to the Urho3D Context, what's the best way to pass arguments to custom Components?

Thanks in advance!

-------------------------

Eugene | 2017-11-19 10:22:44 UTC | #2

[quote="Jetmate, post:1, topic:3758"]
Are LogicComponents essentially just Components built for script?
[/quote]

LogicComponents are more friendly for implementing custom game logic because they have more nice callbacks.

[quote="Jetmate, post:1, topic:3758"]
when is it even necessary to use Components to implement code logic? For example, if I want to implement a Player class, should I create a Player component or implement a Player class that creates the node and encapsulate the logic in that class, rather than a dedicated component?
[/quote]
I recommend to use Components for all logic linked to scene objects.
It simplifies life-time management, serialization, editing and code reuse.

[quote="Jetmate, post:1, topic:3758"]
Final question - since Components have to have a Constructor that only takes a pointer to the Urho3D Context, what’s the best way to pass arguments to custom Components?
[/quote]
Any custom data of Components shall be exposed as attributes (in the perfect world).
If you create the Component from code, it'd look like a bunch of setters.
On the other hand, you could specify the content in some XML and just load it.

-------------------------

Jetmate | 2017-11-20 18:20:12 UTC | #3

When does it make sense to use a regular Component versus a LogicComponent?

-------------------------

Eugene | 2017-11-20 19:32:07 UTC | #4

[quote="Jetmate, post:3, topic:3758, full:true"]
When does it make sense to use a regular Component versus a LogicComponent?
[/quote]

When you don't need any of `LogicComponent` virtual callbacks, you could use `Component`.
It's the matter of taste, more syntax sugar than functional difference.

-------------------------

