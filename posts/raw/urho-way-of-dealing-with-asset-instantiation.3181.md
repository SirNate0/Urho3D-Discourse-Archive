smellymumbler | 2017-05-31 14:51:02 UTC | #1

So, i'm starting to advance in my prototypes in Urho and i'm curious about the "Urho" way of instantiating dynamic assets. For example, in my component code i have direct references to cache->GetResource<Model> and everything. So, when the player gets a new weapon or something, i call that and instatiate it on the right spot. The same happens for muzzleflashes and grenades. 

However, i don't think that's very maintainable. If an artist wants to quickly prototype a new model or a particle, he needs to change the C++ code. Or the script, if i were using AS. Is that how you guys do it? Or do you have some sort of configuration file with paths and everything? Any example with the best practices for dealing with data that changes a lot?

In Unity, i usually handle that with prefabs. And in the UI, the artist can "link" to a prefab or an asset.

-------------------------

johnnycable | 2017-05-31 15:00:45 UTC | #2

You need a configurator. Something you can go "asset drag n drop" and/or "auto command line put-everything in game dir (possibly with transformations)"

-------------------------

lezak | 2017-05-31 18:04:30 UTC | #3

You can use ResourceRef or String (for path) as one of the attributes of Your component and store this attributes in seperate xml/json file. Then You'll be able to change model  by editing this file. When object is created just load it. 

There's also very useful <a href=https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_file_system.html#a7cfc8edbdae22a13ba0f720fe008d8fa>ScanDir </a> function in FileSystem - staying with Your weapon example, to easly create different weapons "outside" of game code, You can create component "weapon" with attributes like: name, model (ResourceRef), damage, max ammo etc. Then create separate folder in data dir and for each weapon type create xml/json file with values for those attributes. At the startup of game use ScanDir on this folder and store results in Vector/HashMap, then all You need to implement is some code to pick right weapon (attributes) to load at right time.

-------------------------

smellymumbler | 2017-05-31 18:27:31 UTC | #4

Is it possible to tie those ResourceRef or String to an editor attribute? So they can be changed in the editor, at runtime?

-------------------------

lezak | 2017-05-31 18:38:48 UTC | #5

Yes, check out source file for StaticModel or any other component using resources to see how it is done.

-------------------------

