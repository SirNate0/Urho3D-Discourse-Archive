1vanK | 2017-10-02 13:18:48 UTC | #1

[img]http://s017.radikal.ru/i424/1508/95/e274abb54a08.jpg[/img]

I try
[code]
if (RaycastDown(hitPos, hitDrawable, normal))
{
    node.rotation = Quaternion(normal.x, node.rotation.yaw, normal.z);
}
[/code]
but it does not work. Please help me :)

Source: [github.com/1vanK/Habr/blob/mast ... oScript.as](https://github.com/1vanK/Habr/blob/master/Result/Data/Scripts/HeroScript.as)

-------------------------

1vanK | 2017-01-02 01:06:37 UTC | #2

Do I understand correctly that normal is not calculated really ?
```
void Drawable::ProcessRayQuery(const RayOctreeQuery& query, PODVector<RayQueryResult>& results)
{
    float distance = query.ray_.HitDistance(GetWorldBoundingBox());
    if (distance < query.maxDistance_)
    {
        RayQueryResult result;
        result.position_ = query.ray_.origin_ + distance * query.ray_.direction_;
        result.normal_ = -query.ray_.direction_;  // <------------------------------------------------------------
        result.distance_ = distance;
        result.drawable_ = this;
        result.node_ = GetNode();
        result.subObject_ = M_MAX_UNSIGNED;
        results.Push(result);
    }
}
```

-------------------------

cadaver | 2017-01-02 01:06:37 UTC | #3

That is in the base class, which doesn't actually understand the geometry. E.g. StaticModel raycast should return the normal correctly.

-------------------------

rasteron | 2017-01-02 01:06:37 UTC | #4

If I'm not mistaken, there's already a snippet from Vehicle or Water Demo which demonstrates actual placement (or something similar) of objects (mushrooms) parallel from Terrain. Maybe you could derive something from that example..

-------------------------

1vanK | 2017-10-02 13:17:58 UTC | #5

Oh, thanks. It works

[code]
if (RaycastDown(hitPos, hitDrawable, normal))
{
    Quaternion grndTilt = Quaternion(Vector3(0.0f, 1.0f, 0.0f), normal);
    node.rotation = grndTilt * Quaternion(0.0f, node.rotation.yaw, 0.0f);
}
[/code]

-------------------------

1vanK | 2017-01-02 01:06:38 UTC | #6

Another method from [answers.unity3d.com/questions/16 ... ormal.html](http://answers.unity3d.com/questions/168097/orient-vehicle-to-ground-normal.html)
It gives smoother results.

[code]
        Vector3 corner1 = node.position + Vector3(-1.0f, 0.0f, -1.0f);
        Vector3 corner2 = node.position + Vector3(1.0f, 0.0f, -1.0f);
        Vector3 corner3 = node.position + Vector3(1.0f, 0.0f, 1.0f);
        Vector3 corner4 = node.position + Vector3(-1.0f, 0.0f, 1.0f);
        
        Vector3 hit1, hit2, hit3, hit4;
        
        bool b1 = RaycastDown(corner1, hit1, hitDrawable);
        bool b2 = RaycastDown(corner2, hit2, hitDrawable);
        bool b3 = RaycastDown(corner3, hit3, hitDrawable);
        bool b4 = RaycastDown(corner4, hit4, hitDrawable);
        
        if (!b1) log.Warning("b1");
        if (!b2) log.Warning("b2");
        if (!b3) log.Warning("b3");
        if (!b4) log.Warning("b4"); // fix it case

       
        Vector3 normal = hit1.CrossProduct(hit2) + hit2.CrossProduct(hit3) +
                         hit3.CrossProduct(hit4) + hit4.CrossProduct(hit1);
        normal.Normalize();
        normal = -normal;

        Quaternion grndTilt = Quaternion(Vector3(0.0f, 1.0f, 0.0f), normal);
        node.rotation = grndTilt * Quaternion(0.0f, node.rotation.yaw, 0.0f);

...

    bool RaycastDown(Vector3 from, Vector3& hitPos, Drawable@& hitDrawable)
    {
        hitDrawable = null;
        Ray ray(from + Vector3(0.0f, 1.0f, 0.0f), Vector3(0.0f, -1.0f, 0.0f));
        RayQueryResult result = scene.octree.RaycastSingle(ray, RAY_TRIANGLE, 1000, DRAWABLE_GEOMETRY, 1);

        if (result.drawable is null)
            return false;

        hitPos = result.position;
        hitDrawable = result.drawable;
        return true;
    }
[/code]

-------------------------

