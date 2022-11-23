dertom | 2018-11-07 00:04:42 UTC | #1

Hi there, 
is it possible to tell the navmesh generator to take not only the outline-wireframe of the collsionshape (no matter if box or convex) but also the area inside out of the navmesh? See the red marked area in the screenshot. 

(This is me current navmesh generation-code:

    m_navMesh = m_scene->GetOrCreateComponent<NavigationMesh>();
    m_navMesh->SetTileSize(32);
    m_navMesh->SetAgentRadius(0.005f);
    m_navMesh->SetAgentMaxClimb(0.25f);
    m_navMesh->SetPadding(Vector3(0.0f,10.0f,0.0f));
    m_navMesh->Build();
)

![Untitled|690x411](upload://kdHA8MqEm6A53miMZpYMPchTBSs.png) 

Btw, urho3d rocks!

-------------------------

Sinoid | 2018-11-07 09:24:22 UTC | #2

Your only options are to use an `Obstacle` or `NavArea`. If the NavArea's AreaID == 0 then it will mark the overlapping cells as non-walkable (RC_NULL_AREA internally) and they won't appear in the final mesh.

-------------------------

dertom | 2018-11-07 00:35:25 UTC | #3

Thx for the fast reply. I will give it a try.

-------------------------

Sinoid | 2018-11-07 00:52:06 UTC | #4

If boxes aren't good enough you can add cylinders to the code with relative ease (rcMarkCylinderArea). 

No idea why I didn't originally implement those, I think contrib. standards might have been higher back then and Bullet/Box2D were the only things doing really wonky things for shapes.

-------------------------

dertom | 2018-11-07 01:08:39 UTC | #5

Thx dude, using NavArea with AreadID==0 works as wanted. No need for CylinderShape (yet).

-------------------------

