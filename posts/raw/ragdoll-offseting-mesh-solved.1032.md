practicing01 | 2017-01-02 01:04:57 UTC | #1

Edit #2: Ran across the problem again and conclude that it has to do with copy/pasting physics components from one node to another.  Creating RigidBody/CollisionShape/Constraints works properly but not when you copy/paste them to try and save time (modifying the transformations won't save).
Edit: Solved: apparently there is a bug somewhere with the editor and it's not updating the transformation values of collision shapes after I set them.  To force a refresh, click on the PhysicsWorld component of the root scene node.

Why does the models arm get offset? The collision mesh is in the right place:

[spoiler][img]http://img.ctrlv.in/img/15/05/01/5543c8ef06798.png[/img][/spoiler]

[spoiler][img]http://img.ctrlv.in/img/15/05/01/5543d3ea85337.png[/img][/spoiler]

-------------------------

Mike | 2017-01-02 01:04:57 UTC | #2

It may come from your ConeTwist constraint settings for shoulder joint. Check your axis, other axis and limits and ensure that rigid bodies are 'parented' to the right nodes. Seems that twist axis limits are not set appropriately (we should see a disc similar to your knee joints). Also check if issue comes from self-collision (you may try to reduce the big sphere for this).

Also using ConeTwist for elbows is overkill (elbow joints have only one rotational degree of freedom) and harder to setup, use Hinge constraint instead.

-------------------------

