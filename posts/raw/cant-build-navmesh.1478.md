Dave82 | 2017-01-02 01:08:03 UTC | #1

Hi whenever try to build the navmesh i get a "Could not build navigation mesh tile data". i tried with simple and complex meshes the result is always the same. Here's how i try to do it :

i have a segment node all nodes in the scene are children of this node. Some of these nodes have a StaticMesh Navigable and RigidBody component.
after i created these nodes and components , i create a nvamesh in the segment node (padding = 0,10,0 tileSize = 64) the result is always the same.

i keep getting the "Could not build navigation mesh tile data" message multiple times during the build process. The smaller the tileSize parameter is , the more frequent the error mesage is and vice versa
if i set tile size to very large value (larger than the mesh's bounding box) the error is gone but i'm not sure it's the right way to make the error go away

i'm using a very simple mesh that covers the walkable areas of the scene , basically it is a flat triangle mesh :

[img]http://s20.postimg.org/6id922xd9/navmesh.jpg[/img]

But the same error happens if i try to use complex level geometry as navmesh.
Is there a tutorial what the navMesh parameters do and how to set up ?

Also will the DetourCrowd system work with simple NavigationMesh or it requires a DynamicNavigationMesh ?
Thanks

-------------------------

Dave82 | 2017-01-02 01:08:03 UTC | #2

Well i managed to build a dynamic navmesh. (debug rendered it and its seems ok) 

[quote="Sinoid"]Recast isn't designed to deal with that, it voxelizes geometry to form a navigation mesh.

If you want your infinitely small geometry slice to be a navigation mesh you're going to have to turn it into dtPoly's yourself or write your own navigation. It's completely against how Recast works.[/quote]

i don't understand what you mean, so how will Recast build a navmesh from a flat plain mesh ? (lets say a ground formed from 2 polygons).

-------------------------

Dave82 | 2017-01-02 01:08:04 UTC | #3

Hi ! The DynamicNavigationMesh is building fine now and the CrowdAgents are navigating perfectly! The simple NavigationMesh still won't work. I found another issue with DetourCrowdManager. The number of Active agents don't change in DetourCrowdManager after you remove CrowdAgent component from nodes.

[code]DetourCrowdManager * dtcManager = scene->GetComponent<DetourCrowdManager>();

dtcManager->GetActiveAgents().Size();
// Returns 4 which is ok , i have 4 enemies in the scene

// Remove CrowdAgent component  from an enemy node :
Node * n = scene->GetChild("Enemy1",true);
n->GetComponent<CrowdAgent>()->Remove();

dtcManager->GetActiveAgents().Size();
// Still returns 4 it should be 3... it seems that DetourCrowdManager isn't informed when a CrowdAgent component is removed from a node.[/code]


And is there a way to determine is a path betwen an Agent and target pos a straight line ? Or retreiving the current path of the agent ?

-------------------------

Dave82 | 2017-01-02 01:08:07 UTC | #4

Thanks Sinoid !

[quote]For the CrowdManager agent count stuff: how recent of a checkout are you using? I'm pretty sure Weitjong caught that one when he was refactoring a while ago?[/quote]

Once i downloaded the official 1.4 (2015-05-14) and was satisfied with it so i stoped checkout from github long time ago.I will download the 1.5 tomorow.

-------------------------

