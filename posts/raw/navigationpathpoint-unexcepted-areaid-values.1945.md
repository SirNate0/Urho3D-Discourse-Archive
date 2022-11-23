codingmonkey | 2017-01-02 01:11:43 UTC | #1

Hi there!
I try to play with navmesh and got strange behavior with areaID values in path.
So I have three planes on scene with some stuff on it.  And each plane have own navArea component with assigned in editor areaID value ~ 1,2,3 for planes
[url=http://savepic.net/7946011.htm][img]http://savepic.net/7946011m.png[/img][/url]

when I try to get navMesh->FindPath(...)

PODVector<NavigationPathPoint> currentPath2_;
unsigned char areaID = currentPath2_[0].areaID_;

the path store within - unusual/unexcepted values: for example my testBot starting from navArea with areaID = 1 but path return 205('H') - value instead 1 
so that I forgot or doing wrong with setup areaID ?

-------------------------

codingmonkey | 2017-01-02 01:11:44 UTC | #2

I suppose I found a problem place, this is it --> pt.areaID_ = pathData_->pathAreras_[i];
because, pathAreras_ never filled with any values anywhere, so within it some kind of garbage I guess

[code]void NavigationMesh::FindPath(PODVector<NavigationPathPoint>& dest, const Vector3& start, const Vector3& end,
    const Vector3& extents,
    const dtQueryFilter* filter)
{
...
    // Transform path result back to world space
    for (int i = 0; i < numPathPoints; ++i)
    {
        NavigationPathPoint pt;
        pt.position_ = transform * pathData_->pathPoints_[i];
        pt.flag_ = (NavigationPathPointFlag)pathData_->pathFlags_[i];
        pt.areaID_ = pathData_->pathAreras_[i];

        dest.Push(pt);
    }[/code]

EDIT:
I fixed this Issue : see comment blocks - fix1 and fix2
[pastebin]PqWPiLiE[/pastebin]

-------------------------

cadaver | 2017-01-02 01:11:44 UTC | #3

Thanks. A pull request at the github project is the preferred way to get fixes in. Is there other places that are affected and need the same fix?

-------------------------

codingmonkey | 2017-01-02 01:11:44 UTC | #4

finally I made some polishing and place code to:

1: class NavigationMesh
[code]    /// NavAreas for this NavMesh
    PODVector<Node*> areas_;[/code]

2: To reduce performance penalty I placed getNodes into CollectGeometries(). So in this case we update areas_ array only when we doing navMesh->Build()
[code]    node_->GetComponents<Navigable>(navigables, true);[/code]

3: simplify NavigationMesh::FindPath 

[code]    // Transform path result back to world space
    for (int i = 0; i < numPathPoints; ++i)
    {
        bool find = false;
        NavigationPathPoint pt;
        pt.position_ = transform * pathData_->pathPoints_[i];
        pt.flag_ = (NavigationPathPointFlag)pathData_->pathFlags_[i];
        pt.areaID_ = pathData_->pathAreras_[i];

        // Fix2-begin for NavArea components
        for (unsigned j = 0; j < areas_.Size(); j++)
        {
            NavArea* area = areas_[j]->GetComponent<NavArea>();
            if (area && area->IsEnabledEffective()) 
            {
                BoundingBox bb = area->GetWorldBoundingBox();
                if (bb.IsInside(pt.position_) == INSIDE)
                {
                    pt.areaID_ = (unsigned char)area->GetAreaID();
                    break;
                }
            }
        }
        // Fix2-end for NavArea components

        dest.Push(pt);
    } 
[/code]
so after this fixes it's works fine for my using case, expect one moment when agent travelling though offMeshConnection, it not get areaID from this offMeshConnection. 
(actually as before they also return garbage values, but now my navAreas override garbage values then by new execution path)

4: also I think if few navAreas have the same point within need doing some kind of sorting by distance to navArea origin for choose nearest navArea

5. so, since this feature works without Detour middleware(above it / over it) there is no need keep only 64 max navAreas i suppose.

-------------------------

cadaver | 2017-01-02 01:11:44 UTC | #5

I believe I'm not qualified enough to comment. By all means make a PR, then we'll hopefully get more eyes (and comments) on this in a structured manner.

-------------------------

