CE184 | 2020-09-13 06:29:49 UTC | #1

Hi,
I have a map with different speed areas. I want the agent to reach the destination with shortest time instead of shortest distance. I found there is a SetAreaCost() api for NavMesh. I played with it but could not figure out how to use it. The #15 sample is too simple to cover this.

I tried
```
  Node* area_node = scene_->CreateChild("AreaNode");
  auto* nav_area = area_node->CreateComponent<NavArea>();
  nav_area->SetAreaID(1);
  nav_area->SetBoundingBox(BoundingBox(Vector3(40, 0, 40), Vector3(60, 0, 60)));
  navMesh->SetAreaCost(1, 10);
  // ...
  navMesh->Build();
  // ...
  navMesh->SetDrawNavAreas(true);
  navMesh->SetDrawOffMeshConnections(true);
```
But the agent is ignoring the cost value for the area, just find the shortest path as usual.

-------------------------

