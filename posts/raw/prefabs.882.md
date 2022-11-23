NiteLordz | 2017-01-02 01:03:47 UTC | #1

In what circumstances should one use a Prefab in regards to Urho3D ?  i am looking through the editor code, and see a prefab resource type, and see that one can be generated from the AssetImporter.  I am curious as to what the use case would be, and how that would differ from using just an imported model.

Thanks much

-------------------------

weitjong | 2017-01-02 01:03:48 UTC | #2

I think the prefab in Urho3D Editor is quite similar in concept to Unity3D. The prefab is a composition of nodes with their child components already attached, with basic attribute values already preset, etc. In short, load the prefabs and they are ready to go literally (if it has logic component to move around).

-------------------------

hdunderscore | 2017-01-02 01:03:48 UTC | #3

To further expand on that, the AssetImporter probably creates a node + StaticModel + material attributes prefab, however if you want something more complex you can put it together in the Urho Editor and then File -> Save Node As. This will create an xml file that describes the node/components/attributes.

Example use: in a game I'm working on I've got buildings and vehicle prefabs (with relevant logic) and instantiate them to populate the game. That way I don't have to have a lot of messy code to set up the components. Similarly, the Ninja War example provided with Urho has prefabs for projectiles, potions and ninja's.

-------------------------

NiteLordz | 2017-01-02 01:03:48 UTC | #4

Ok, that is what I was thinking. So what I already have in my situation is a duplicate method, that copies the node and all children components (and sub nodes). So basically a prefab would replace that concept with an XML based "copy" that can be added into the scene as seen fit.

Thanks guys

-------------------------

