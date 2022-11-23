GIMB4L | 2017-01-02 00:58:17 UTC | #1

I've taken a look at the documentation, and I've noticed that since the automatic garbage collection has been turned off, it is our responsibility to manage the references on objects. However, I see no option in the scripting language to facilitate this. How does one manage the references of an object?

-------------------------

aster2013 | 2017-01-02 00:58:17 UTC | #2

What script you used? AngelScript or Lua?

-------------------------

GIMB4L | 2017-01-02 00:58:17 UTC | #3

I'm in AngelScript. I should say that the node I'm trying to delete has a ScriptObject attached, which is where I'm doing the delete from.

-------------------------

cadaver | 2017-01-02 00:58:17 UTC | #4

Check the scripts in NinjaSnowWar game, they successfully delete their owning nodes from the scene. For example GameObject.as, which implements a lifetime counter:

[code]
    void FixedUpdate(float timeStep)
    {
        // Disappear when duration expired
        if (duration >= 0)
        {
            duration -= timeStep;
            if (duration <= 0)
                node.Remove();
        }
    }
[/code]

Managing references means just that you're responsible for setting all long-living (not local in a function) handle variables that point to your node to null, because they're "strong refs" and keep the node alive. For example holding a handle to your cameraNode would prevent it from being destroyed, even if it's removed from the scene. You can use the WeakHandle type to avoid that effect, which holds a weak ref instead and returns automatically null when the object has been destroyed. A WeakHandle returns a normal AngelScript handle by calling Get() on it.

-------------------------

GIMB4L | 2017-01-02 00:58:19 UTC | #5

Alright, makes sense. Thanks!

-------------------------

GIMB4L | 2017-01-02 00:58:19 UTC | #6

I'm still having issues deleting the node. Let me go into more detail.

So we fire a missile from a jet. The missile tracks another jet, and upon making contact will explode with a particle effect, and be deleted.

The missile initialization code is like so:

[code]
void FireMissile(Node@ targetNode = null)
{
	Node@ missileNode = LoadGameObject("Missile", node.scene, cameraNode.worldPosition, node.worldRotation);
		
	Missile@ newMissile = cast<Missile>(missileNode.scriptObject);
		
	newMissile.Init(missileNode, targetNode, true);
}
[/code]

Now, with my new knowledge of references, I tried this:
[code]
void FireMissile(Node@ targetNode = null)
{
	WeakHandle missileNode = LoadGameObject("Missile", node.scene, cameraNode.worldPosition, node.worldRotation);
		
	Missile@ newMissile = cast<Missile>(cast<Node>(missileNode.Get()).scriptObject);
		
	newMissile.Init(cast<Node>(missileNode.Get()).scriptObject, targetNode, true);

	@newMissile = null;
}
[/code]

That also doesn't work. When I go to call the Node.Remove() inside the Missile class, the node remains.

Any help with this?

-------------------------

friesencr | 2017-01-02 00:58:19 UTC | #7

You wouldnt use a weakhandle inside a method generally.  As soon as the variable goes out of scope the reference is subtracted.  If you have a class that holds onto a Node that would be a good canidate for a weakhandle since that variables scope is lived to the object's duration.  The code you are showing looks like it wouldn't add a reference it must be from somewhere else.  What does the Init method do?  I hate to give any advice on this matter as I am fighting this stuff myself.  Like i mentioned in another post, I hope to one day look back and think this memory stuff a bad dream.

Question:
Does calling Remove defer the removal until the counter reaches 0 or will it skip over the command and need to be issued again?

-------------------------

