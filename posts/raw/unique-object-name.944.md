vivienneanthony | 2017-01-02 01:04:18 UTC | #1

Hi
Is there a specific way to get all occurrences of a object name. For example, if I want to add a node name "Oddbox". I would like the name to be unique like "Oddbox1" if it's a new name, or "Oddbox2" if oddbox exist. Incrementing.

The psuedo/code I cam up with so far is

[code]   unsigned int count = 1; /// Count of "name" occurrences
    String newname=(count>0?String("name")+String(count++_as_string):String("mame")+String("1"));
[/code]

I'm thinking the major thing is getting the "name" occurrences

Vivienne

-------------------------

GoogleBot42 | 2017-01-02 01:04:18 UTC | #2

Each object is assigned a unique id in a scene if that helps...
[url]https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Scene/Node.cpp#L563[/url]
[url]https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Scene/Node.cpp#L1397[/url]

-------------------------

vivienneanthony | 2017-01-02 01:04:18 UTC | #3

[quote="GoogleBot42"]Each object is assigned a unique id in a scene if that helps...
[url]https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Scene/Node.cpp#L563[/url]
[url]https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Scene/Node.cpp#L1397[/url][/quote]

Thanks.  It's not exactly what I'm looking for.

Although each node is unique with a uniqueid number. I want to differ the names and be able to find nodes by name or give it clearer definitions.

It's easier to decipher a name and purpose like "OddBoxStacticModelNode2"  then uniqueid "1283733" for example or any other rudiementary number.

-------------------------

thebluefish | 2017-01-02 01:04:19 UTC | #4

How about:
[code]
Node* GetChild(const String& name, bool recursive = false) const;
[/code]

Something like this should work:
[code]
Urho3D::String name("Object");
Urho3D::String newName(name);
Urho3D::Node* node = parentNode->GetChild(name, true);
for (int x = 1; node; x++)
{
	newName = name.Append(x);
	node = parentNode->GetChild(newName, true);
}
node = parentNode->CreateChild(newName);
[/code]

Edit: Just want to point out that this is horribly inefficient in that it will take longer the more nodes you have. It simply doesn't scale well. If I were serious about object management, I would probably create a component that actively tracks when nodes are created/removed and automatically renames a node if it detects a naming conflict. By tracking the name IDs in your naming scheme, there wouldn't be additional overhead regardless of how many nodes with the same naming scheme exist, at the cost of a little memory overhead.

-------------------------

TikariSakari | 2017-01-02 01:04:19 UTC | #5

I am not sure if there is something that lets you find partial names with wildcard characters, but if there isn't one, I would probably use something like map, which has a string as an indexer, and the value of the current added object. If the string doesn't exist in the map, then just add the object in the map and set it to have value pair of 0.

I would then probably use some coding syntax for the node names such as nodename_number, and if i had to go through all the nodes to populate the map, I would find the last index of character '_', then just get the highest number out of all the nodes.

You might run into problems if you delete and copy paste object a lot of times, as the counter increases, but most likely there would not be overflow with normal use and even this could be avoided if you use some sort of string indexer instead of number.

-------------------------

vivienneanthony | 2017-01-02 01:04:20 UTC | #6

[quote="thebluefish"]How about:
[code]
Node* GetChild(const String& name, bool recursive = false) const;
[/code]

Something like this should work:
[code]
Urho3D::String name("Object");
Urho3D::String newName(name);
Urho3D::Node* node = parentNode->GetChild(name, true);
for (int x = 1; node; x++)
{
	newName = name.Append(x);
	node = parentNode->GetChild(newName, true);
}
node = parentNode->CreateChild(newName);
[/code]

Edit: Just want to point out that this is horribly inefficient in that it will take longer the more nodes you have. It simply doesn't scale well. If I were serious about object management, I would probably create a component that actively tracks when nodes are created/removed and automatically renames a node if it detects a naming conflict. By tracking the name IDs in your naming scheme, there wouldn't be additional overhead regardless of how many nodes with the same naming scheme exist, at the cost of a little memory overhead.[/quote]

Hmmm. I have a manager that tracks createdobjects so technically I can search through that for naming conflicts.

Because, objects can be retrieved from a network, or other node files with children. I think any method would be highly inefficient.

-------------------------

