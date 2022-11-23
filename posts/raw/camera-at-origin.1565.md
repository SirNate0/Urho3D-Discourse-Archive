AReichl | 2017-01-02 01:08:33 UTC | #1

Hi,
is it possible in Urho3D to keep the camera at origin (meaning shifting the whole scene around the camera)?
In Ogre for example there is an option for it.
If i would have to program it myself, could it be done with an "empty" node which is the parent of all other nodes and only does transformations (reverse to the camera movements / rotation )?

-------------------------

cadaver | 2017-01-02 01:08:33 UTC | #2

Yes, it can be done with parenting all your content to a node. The scene itself cannot be moved/rotated/scaled due to transform calculation optimizations and to avoid weird mistakes where the whole scene would be e.g. scaled.

-------------------------

AReichl | 2017-01-02 01:08:36 UTC | #3

Ok - WHERE should i connect the camera to - the "RootSceneNode" or the above mentioned empty-only-transformation scene node?

-------------------------

Modanung | 2017-01-02 01:08:36 UTC | #4

The camera should have it's own node directly parented to the Scene (not the RootSceneNode).
When the RootSceneNode is moved, the camera should not move along.

-------------------------

AReichl | 2017-01-02 01:08:37 UTC | #5

My fault - i am more used to Irrlicht and with "RootSceneNode" i meant what you call "Scene".

-------------------------

Modanung | 2017-01-02 01:08:39 UTC | #6

Ah right... I assumed the RootSceneNode would be the name of the node you'd create. So yea, that's what the Scene is. [url=http://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_scene.html]Scene[/url] is actually a subclass of Node.
If the camera needn't move nor rotate I guess you could add the Camera component directly to the Scene... and everything else would be parented to your [i]world[/i] node which could move through the scene.

-------------------------

