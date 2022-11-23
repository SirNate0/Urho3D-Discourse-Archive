Kai | 2017-01-02 00:59:17 UTC | #1

Hi, 
Is there a reason that Urho3D doesn't use DetourCrowd with agents from RecastNavigation library or is it just not implemented yet ?
Thanks.

-------------------------

cadaver | 2017-01-02 00:59:19 UTC | #2

It is not implemented yet. I haven't personally looked into it at all, as back when initially integrating Recast/Detour, in the absence of an actual game project, I was happy to get just the basic navigation mesh and path queries working first.

Note that the scope of Urho3D is rather large (compared to pure rendering engines) and the active development team is small, so the ideal course of action in case of missing functionality is to dive into the integration yourself, and contribute it as a pull request.

I would imagine it would follow a somewhat similar pattern as the Bullet physics integration, which has the PhysicsWorld component in the root scene node (encapsulates the Bullet physics world) and RigidBody components for the individual objects. In the case of DetourCrowd we'd probably have the agent manager encapsulated inside the NavigationMesh component, which already holds the path data, and the individual agents encapsulated as components inside the scene nodes that should be moved by the steering mechanism.

-------------------------

