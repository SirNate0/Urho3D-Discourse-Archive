Lumak | 2017-07-06 19:20:40 UTC | #1

No title as yet but I'll post my progress on this thread.

[b]Sound test[/b]
https://youtu.be/yxzvDf2sg8k

-------------------------

Lumak | 2017-07-06 23:23:55 UTC | #2

I don't know if this is worth mentioning, but I'm using Bullet's raycastvehicle, obviously w/o wheel models, for better handling and for the car to closely follow terrain instead always being straight horizontal.

-------------------------

darkirk | 2017-07-07 14:34:28 UTC | #3

That's fantastic! I love all your experiments, Lumak. :smiley:

-------------------------

Lumak | 2017-07-07 15:36:06 UTC | #4

Thanks. There's so much to experiment when it comes to game development, which is nice... if you love programming heh.

-------------------------

Lumak | 2017-07-08 18:39:30 UTC | #5

Experimenting with importing a model as "node," rotating staticmodels independently, blowing it up, and reconstructing it at runtime. No rigidbodies are used in the destroyed state, as it's just for aesthetics and the duration is short.

[img]http://i.imgur.com/nWdyGEy.gif[/img]

-------------------------

Lumak | 2017-07-09 17:33:29 UTC | #6

In some games that I've seen, I wondered if the temporary enemy HP bar pop-up when you damage an enemy was in 3D space or UI. UI looks pretty clean to me.

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/708d4993960ea35ac97f81599beee727a1a32ef4.jpg[/img]

-------------------------

Alex-Doc | 2017-07-10 07:14:01 UTC | #7

Well done!

[quote="Lumak, post:6, topic:3327"]
I wondered if the temporary enemy HP bar pop-up when you damage an enemy was in 3D space or UI
[/quote]

I've also opted for UI in AX:EL but experience then told me it was hard to find a correct color for the various backgrounds, especially on smaller aircrafts. 
At last the best solution for me was to use both the life bar and a smoke effect that gets more intensity as the life goes down.

-------------------------

Lumak | 2017-07-10 20:07:47 UTC | #8

[quote="Alex-Doc, post:7, topic:3327"]
At last the best solution for me was to use both the life bar and a smoke effect that gets more intensity as the life goes down.
[/quote]
Good to know, as I only have placed one hp bar so far for testing so I might have to do a similar thing for my game.

-------------------------

Lumak | 2017-07-11 19:48:54 UTC | #9

I'll place my turret's head and barrel rotation code here, as some might find it useful dealing with world rotation to local. More specifically, turret is imported as "node" which means it has hierarchical node structure similar to having a skeleton. So, knowing the internal structure of the model but not knowing the world orientation of each node, you can calculate the world rotation via LookAt() then acquire its local rotation to limit the rotation axis and angles.

edit: I keep editing this to clarify this routine...
edit: you have to know the node hierarchy to know that barrel is a child of the head 

[details=Turret rotate code]
[code]
void Turret::FixedUpdate(float timeStep)
{
    if (enemyNode_)
    {
        Vector3 enemyPos = enemyNode_->GetWorldPosition();
        Vector3 distSeg = enemyPos - node_->GetWorldPosition();
        if (distSeg.Length() < detectDistance_)
        {
            // head rot
            Quaternion qrot;
            headNode_->LookAt(enemyPos, Vector3::UP, TS_WORLD);
            Vector3 euHead = headNode_->GetRotation().EulerAngles();
            qrot.FromEulerAngles(0.0f, euHead.y_, 0.0f);
            headNode_->SetRotation(qrot);

            // barrel rot
            barrelNode_->LookAt(enemyPos, Vector3::UP, TS_WORLD);
            Vector3 euBarrel = barrelNode_->GetRotation().EulerAngles();
            qrot.FromEulerAngles(euBarrel.x_, 0.0f, 0.0f);
            barrelNode_->SetRotation(qrot);
        }
    }
}

[/code]
[/details]

-------------------------

Lumak | 2017-07-11 22:43:09 UTC | #10

Trying my hand at car customization with decals and colors. I've yet to apply PBR.

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/f7a266152568918e385c2ee9b972f24e01d5f46c.jpg[/img]

-------------------------

slapin | 2017-07-12 04:33:54 UTC | #11

Looks really good!
Could you please explain decals customization?

-------------------------

Lumak | 2017-07-12 18:00:51 UTC | #12

I'm using a decal texture similar to how diffuse is used, just that decal texture is mostly transparent.

-------------------------

