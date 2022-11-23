pldeschamps | 2020-03-28 22:19:46 UTC | #1

Hi,

I need the WorldPosition of a BillboardWrapper.
The WorldPosition method exists for nodes but not for BillboardWrapper.
So I create a node in the BillboardSet node at the BillboardWrapper position.
Then I get this node WorldPosition before I remove it.
This is processor consuming and I observe time lag. Is there a faster solution to get a BillboardWrapper WorldPosition?

Regards,

This is my code (sorry, it is C#)
```
                    BillboardWrapper bbi = StarsBbs.GetBillboardSafe(StarsBillboardItems[starText.Key]);
                    //BillboardWrapper bbi;
                    //StarsBillboardItems.TryGetValue(starText.Key, out bbi);
                    if (bbi != null)
                    {
                        offset = (int)(App.StarsData[starText.Key].StarSize * 20);

                        Node nodeStar = nodeBbs.CreateChild(name: "star");
                        nodeStar.Position = bbi.Position;
                        Vector3 starPosition = nodeStar.WorldPosition;
                        nodeStar.Remove();
                        IntVector2 v2 = viewport.WorldToScreenPoint(starPosition);
```

-------------------------

Dave82 | 2020-03-29 12:04:20 UTC | #2

In c++ you can use 
[code]
worldPos = StarsBbs->LocalToWorld(bbi.position_);
[/code]
I don't use C# so i have no idea how to do this in C# Sorry

-------------------------

pldeschamps | 2020-03-29 12:03:56 UTC | #3

Thank you, that is what I was looking for.
It is 10 times faster!

```
IntVector2 v2 = viewport.WorldToScreenPoint(nodeBbs.LocalToWorld(bbi.Position));
```

-------------------------

