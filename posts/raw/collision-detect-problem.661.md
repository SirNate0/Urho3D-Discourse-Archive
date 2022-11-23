rogerdv | 2017-01-02 01:01:57 UTC | #1

I have set up a node as a  trigger to detect when the player reaches the area. I create a CollisionShape component, expand its size in X and Y to cover the desired area, then add a RigidBody, set its Collision Event Mode to Always and enable Trigger checkbox. Also added an StaticModel (the box), just in case, and make it invisible by unchecking all the View mask checkboxes. 
In the player creation code I have this:
[code]node = scn.CreateChild(id);
		model = node.CreateComponent("AnimatedModel");
		body = node.CreateComponent("RigidBody");
		shape = node.CreateComponent("CollisionShape");
		shape.model = model.model;[/code]

In the gameplay code I subscribe collision event and set up a basic handler:

[code]
SubscribeToEvent("NodeCollision", "HandleTriggers");
***
void HandleTriggers(StringHash eventType, VariantMap& eventData)
	{
		Node@ n = eventData["OtherNode"].GetPtr();
		Print("collided with "+n.name );
	}
[/code]

But when I make the player model walk to the area, nothing happens. Is there any missing step in the shape and body creation?

-------------------------

codingmonkey | 2017-01-02 01:01:57 UTC | #2

>Also added an StaticModel (the box), just in case, and make it invisible by unchecking all the View mask checkboxes.
make your cube visible, and check is it on same place as before in editor. may be it's gone somehow, no ?

also read this [urho3d.github.io/documentation/1 ... ysics.html](http://urho3d.github.io/documentation/1.32/_physics.html)
"An example of reading collision event and contact point data in script, from NinjaSnowWar game object collision handling code:"

-------------------------

rogerdv | 2017-01-02 01:01:57 UTC | #3

The cube is in the right place, I can make the character walk trhough it. Also tried enlarging the collisionShape, but doesnt works.

-------------------------

codingmonkey | 2017-01-02 01:01:57 UTC | #4

may be you forgot node parameter ?

SubscribeToEvent(node, "NodeCollision", "HandleNodeCollision");

are you using like in ninga classes hierarchy?

[spoiler][ul]class [b]GameObject[/b] : ScriptObject ?
{
void HandleNodeCollision(StringHash eventType, VariantMap& eventData)
{
...[b]WorldCollision[/b](eventData);
}

void WorldCollision(VariantMap& eventData){...}
}

class Ninja : [b]GameObject[/b] 
{
    void Start()
    {
        SubscribeToEvent(node, "NodeCollision", "HandleNodeCollision");
    }
    void [b]WorldCollision[/b](VariantMap& eventData) 
    {
     ...
    }
{
...
}
}[/ul][/spoiler]

-------------------------

rogerdv | 2017-01-02 01:01:57 UTC | #5

I looked at ninja as guide, but I skipped the node parameter because I thought it was optional and that the event handler would catch all collisions. Will try with that.

-------------------------

rogerdv | 2017-01-02 01:01:57 UTC | #6

Well, this is what I do:

[code] Array<Node@> snodes = gameScene.GetChildren();
    Print(snodes.length);
    for (int i=0;i<snodes.length;i++) {
			if (snodes[i].name=="emarker") {
				//Found an entity marker
				Variant val = snodes[i].vars["entity"];
				snodes[i].name=val.ToString();
				ent.CreateFromScene(gameScene, snodes[i],val.ToString());
			} else if (snodes[i].name.Contains("trig")) {
				//found a trigger
				SubscribeToEvent(snodes[i], "NodeCollision", "HandleTriggers");
			}//if
    }//for
[/code]

It finds the trigger node, but no event is called.

-------------------------

