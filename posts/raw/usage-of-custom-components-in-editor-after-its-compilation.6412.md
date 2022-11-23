Stuur | 2020-10-04 10:30:46 UTC | #1

Disclaimer: I am aware of the fact that this question was already asked on the forum, but I have a different, strict case, description of which I could not find anywhere on the Internet.

I am currently working on a project, where my game's logic is being provided after the actual core engine/editor is already compiled (Long story short: I am using Urho as a library in order to provide JIT C++ mod support), and because of that, there is no way for me to actually register anything afterward in a code form. As far as I am aware, the editor does not REALLY need the class implementation, since it simply assigns component names to nodes, and allows to edit their attributes. When I was working with Source engine, they used a technique with a declaration of the class name, and its attributes in a separate text file, which the engine afterward used to supply logic for by providing backend C++ implementation. Could anybody help me out with this one? I am currently using variable editor per node in my prefabs in order to emulate this behavior, but I would really like to provide a better editor experience to modders of the game.

Edit: My current solution is going to be a compilation of core game/mods into a separate library, then linking that library to UrhoPlayer and compiling it in order to provide all the necessary codebase/registrations that would be needed by the editor to use components properly.

-------------------------

Modanung | 2020-10-04 14:28:30 UTC | #2

If the goal is providing a better modding experience, you may want a more project-specific editor.
Like those that came with the Blizzard RTS games I played.

Making something that does less can be easier for both developer and user.

-------------------------

jmiller | 2020-10-04 16:42:35 UTC | #3

[Dertom's Blender Exporter](https://discourse.urho3d.io/t/blender-2-8-exporter-with-additonal-features-e-g-urho3d-materialnodes-and-components/5240) presents a nice Blender node interface to components, using a text resource (json) produced by `Urho3D-Blender-Runtime` and specifically [Urho3DNodeTreeExporter](https://github.com/dertom95/urho3d-blender-runtime/blob/master/src/tools/SceneLoader/LoaderTools/ComponentExporter.cpp) which can be adapted for custom controls. In this way, the Model component even improves on Urho's: with automatic mesh selection it can be assigned without changes to any number of objects.
Being able to assign multiple trees to objects allows for modular design with components sharing common properties: standard CollisionShapes, RigidBody with some standard properties, etc.

-------------------------

