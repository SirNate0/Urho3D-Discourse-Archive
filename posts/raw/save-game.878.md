sabotage3d | 2017-01-02 01:03:44 UTC | #1

Hey guys,

What would be the recommended way of saving game and game states ?
In the NinjaSnowWar example .dat file is used.  Have anyone tried json or sqlite ?
This one seems really neat: [doc.qt.io/qt-5/qtcore-json-savegame-example.html](http://doc.qt.io/qt-5/qtcore-json-savegame-example.html)
But it is QT dependant. Do we have something similar in Urho3d ?

Thanks in advance,
Alex

-------------------------

thebluefish | 2017-01-02 01:03:44 UTC | #2

Scene::Save and Scene::SaveXML should serialize the entire scene out, which can be loaded by calling Scene::Load or Scene::LoadXML respectively.

-------------------------

GoogleBot42 | 2017-01-02 01:03:45 UTC | #3

No only custom .dat and .xml files but because Urho3D has the ability built in to serialize data.  You could look at how the xml and .dat savers work and use that to write your own!  I imagine that json would be pretty easy but sqlite might be somewhat more challeging but it should be doable.  If you get it working you could post the code here and maybe it will be added into the engine!  :slight_smile:

-------------------------

sabotage3d | 2017-01-02 01:03:45 UTC | #4

Thanks, I have missed Scene::SaveXML . Is it possible to serialize custom classes and variables, like health, score and game states with it.

-------------------------

cadaver | 2017-01-02 01:03:45 UTC | #5

If your custom classes are components and registered with object factories, saving them along with the scene is no problem.

Do not attempt to subclass Node, that will not work with scene load/save as loading will always instantiate bare Nodes.

For simple custom data like score and health you can use the nodes' "user variables" system (Node::GetVar, Node::SetVar)

-------------------------

sabotage3d | 2017-01-02 01:03:46 UTC | #6

Thanks a lot I will try that :slight_smile:

-------------------------

thebluefish | 2017-01-02 01:03:46 UTC | #7

Note that only attributes are saved. Any local variables in your custom components that isn't setup with an attribute will not be saved/loaded. Essentially when your component gets loaded, it's going to use the loaded values for your attribute, and must handle that accordingly. It's surprisingly easy to stop your component from working right if you don't set it up properly.

-------------------------

