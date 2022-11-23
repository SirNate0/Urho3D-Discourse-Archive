johnnycable | 2017-04-20 09:47:26 UTC | #1

Hello, I'm porting an app to urho and I'd like someone to consider on the following.

In my old architecture I'm using EntityX. This is a pure ECS, where components are just data, and systems are function which operates on that data.
I'm trying to relate this to Urho. In Urho, nodes are containers, and components looks like a specialization of nodes, where one node becames a skybox, a model, and so on.
Then there are logic components, which looks like a behavioural specialization of components.

My app is based on a specialized form of flocking. I have a group of nodes which acts as a whole, moved by specialized path functions, sort of screen-walking sprites grouped together and creating harmonies and disharmonies.

Until now, I've put all these things into the update cycle and manage everything from a generalized form of AI over data management.

To my understanding, in urho I should:
- transform the whole group in different nodes under a group parent node;
- create related sprites components
- put all the flocking AI into the parent logic component

Moreover, part of ECS is used as a FSM game manager for level AI. Is this to be managed as a subsystem? To my understanding, subsystems are application-wide objects so that'd like to be its place... but not sure about it.

Can someone share its thought about?

-------------------------

