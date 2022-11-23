archwind | 2017-10-25 17:40:16 UTC | #1

First off I am using UrhoSharp but should not really be that important since I really don't want to go to source unless I absolutely have to.

Do I need to have my own Scene manager and Terrain manager?

How much management is already in the engine?

Thanks,

-------------------------

Eugene | 2017-10-26 11:28:30 UTC | #2

[quote="archwind, post:1, topic:3686"]
Do I need to have my own Scene manager and Terrain manager?
[/quote]

Yes, if I understood your question.

[quote="archwind, post:1, topic:3686"]
How much management is already in the engine?
[/quote]
The engine provides tools and features, not managers.
There is Scene and Terrain classes that provide bucket of features.
User is responsible for managing these features.
The engine has some high-level managers if such managers are re-usable enough (e.g. ResourceCache)

-------------------------

archwind | 2017-10-26 13:42:34 UTC | #3

Thank you for clarifying it. I wanted to be sure before going through the process of doing it.

About the internal resource manager:

Is it possible to set up this manager to handle existing xml game structure?

-------------------------

Eugene | 2017-10-26 14:00:34 UTC | #4

[quote="archwind, post:3, topic:3686"]
Is it possible to set up this manager to handle existing xml game structure?
[/quote]

Could you elaborate your goals?
Abstract questions tend to result in abstract answers.

-------------------------

archwind | 2017-10-26 19:59:53 UTC | #5

As I mentioned before I am taking Multiverse which uses Axiom engine and installing Urho3D into it.

It already has existing scene manager, terrain manager and resource manager.

I am trying to determine the best approach to resources now. (keep existing or convert)

-------------------------

