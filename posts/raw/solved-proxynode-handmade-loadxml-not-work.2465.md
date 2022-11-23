f1af | 2017-01-02 01:15:35 UTC | #1

Hellow! I have
vehicle.xml and vehicle.as
It's _one_ vehicle for one million level locations.
I have level_00.xml, it have Node, Node have ScriptInstance component and this script:
[code]
class ProxyNode : ScriptObject
{
    String sourceXML;

    void DelayedStart()
    {
        log.Info("ProxyNode: sourceXML = " + sourceXML);
        XMLFile@ xmlfile = cache.GetResource("XMLFile", sourceXML);
        if ((xmlfile !is null) and (node.GetComponents().length == 1))
        {
            if (node.LoadXML(xmlfile.GetRoot(), true))
            {
                log.Warning("LoadXML!!!");
            }
        }
    }
}
[/code]

And I load scene like this:
[code]    scene_ = Scene("level_00");
    scene_.LoadXML(cache.GetFile("Scenes/level_00.xml"));
[/code]

And Urho is crashed =(

It's bug or I do somthing wrong?

-------------------------

f1af | 2017-01-02 01:15:35 UTC | #2

I resolve this problem!
Scheme of my code was hare:

[code]
main.as, load ->
level.xml, have ->
Node + ScriptInstance component, linked ->
ProxyNode.as, loadXML ->                     // Not work, becouse:
PlayerVehicle.xml, have ->
Node + ScriptInstance component, linked ->  // Error is here!
main.as, include ->                         // Error is here!
PlayerVehicle.as
[/code]

And [b]loadXML[/b] is crashed Urho.

I just change last step:

[code]
PlayerVehicle.xml, have ->
Node + ScriptInstance component, linked ->
PlayerVehicle.as
[/code]

and all works fine.

------------------------------------

But now I need handle and change Save process of this node.. Mayde someone have similar ProxyNode class?

-------------------------

f1af | 2017-01-03 20:19:11 UTC | #3

It's worked solution:

[code]class ProxyNode : ScriptObject
{
	String sourceXML;

	void DelayedStart()
	{
	    XMLFile@ xmlfile = cache.GetResource("XMLFile", sourceXML);
	    if (xmlfile !is null)
	    {
	        Node@ newNode = scene.CreateChild();
	        if (newNode.LoadXML(xmlfile.GetRoot(), true))
	        {
	            newNode.SetTransform(node.position, node.rotation);
	            log.Info("ProxyNode: load successful, filename \"" + sourceXML + "\"");
	        }
	        newNode.temporary = true;
	    }
	}
}
[/code]

-------------------------

