Bananaft | 2018-11-19 11:54:19 UTC | #1

I made myself a prefab system. It came out pretty minimalistic. And I'm very happy with it. Even nested prefabs are working (literally better than Unity). Sharing it, so maybe someone will find it useful or give me feedback (because I'm not very confident with C++). And maybe we will make it into PR. Licensed under CC0.

Here is the video demonstration:
https://www.youtube.com/watch?v=PPPIIGSliBI

So, basically, each node has a reference to a XMLfile, if it is empty, then nothing happens, it's a normal node, if it is pointing to a file, then:
 1) on save will skip saving it's children and components 
 2) on load this node will load object from this xml file, and applying it's transform to it.

I also added live reload handling. And save prefab button. (Using [this marvelous hack](https://github.com/urho3d/Urho3D/issues/1507))

Here is a full code: [Node.h and Node.cpp](https://gist.github.com/Bananaft/63b32123e2e3b6909d782fb7f6914406)
I use Urho1.7, so the code is a bit old.

Basically, I added two new attributes:

    URHO3D_MIXED_ACCESSOR_ATTRIBUTE("Prefab", GetPrefab, SetPrefab, ResourceRef, ResourceRef(XMLFile::GetTypeStatic()), AM_FILE);
    URHO3D_ACCESSOR_ATTRIBUTE("Save Prefab", GetFalse, SavePrefab, bool, false, AM_EDIT);

In Node::SaveXML, after saving id and attributes:

    if (prefab_ != NULL)
        return true;

And then this four new functions:
https://gist.github.com/Bananaft/797f0291ede5451d9f50f4126b56ea3d

And lastly I had to make room in the editor interface, AttributeEditor.as

    const uint MIN_NODE_ATTRIBUTES = 7;
    const uint MAX_NODE_ATTRIBUTES = 11;

-------------------------

rku | 2018-11-19 11:36:14 UTC | #2

Great work!

I see you have to select some other node ("base"?) and check "save prefab" checkbox for changes to apply
whats going on there? Bit not very user-friendly. i wonder if we could make it better.

-------------------------

Bananaft | 2018-11-19 11:50:22 UTC | #3

In this scene there are three buildings (bases) prefabs, each of them nesting a bunch of lamp prefabs.
Here is basically whole scene.xml:
![image|567x500](upload://tmawxtyRu1RaNglAt9uudchzkGI.png) 

In the video, I first copy an object in one of the buildings. If I save the scene, this change will be lost. I have to save it into object file. So I select a parent node, the one named "base", click "Save Prefab" and two other bases update themselves with this change.

One improvement I thought about is if you press the "Save prefab" button, but prefab attribute is empty, it goes up the hierarchy until it finds a parent with prefab and saves it.

-------------------------

Bananaft | 2018-11-19 12:01:36 UTC | #4

It would also be great to paint prefab nodes with different colors in the editor.

-------------------------

