henu | 2020-12-28 21:55:42 UTC | #1

Is it possible to disable node replication when you don't need it?

I have a game where lots of projectiles are flying. I'm only interested when nodes for those are created and destroyed. I believe I could easily calculate everything between those using the initial velocity and position on the client side.

If it's not possible and this sounds like a terrible idea, do you have any alternative ideas how to implement it? One that comes to my mind is to keep projectiles always local and create them to client side using remote events. I would also need some unique names so I could later destroy the right projectile with another remote event.

If it's not possible and you think it might be good idea, I can try to write a PR for Urho3D. I think there are too approaches:

1. Optional boolean parameter to all setters to not mark network update.
2. Flag that prevents automatic network update. It could be used like this:

    node->SetAutomaticMarkNetworkUpdate(false);
    node->SetPosition(new_pos);
    node->SetRotation(new_rot);
    node->SetAutomaticMarkNetworkUpdate(true);

-------------------------

1vanK | 2020-12-28 22:29:45 UTC | #2

```
/// Component and child node creation mode for networking.
enum CreateMode
{
    REPLICATED = 0,
    LOCAL = 1
};
```

-------------------------

henu | 2020-12-28 22:47:09 UTC | #3

I meant that the projectiles would be replicated, so clients could see them, but the replication would be disabled at certain times.

But I think I already found a solution. If I understood correctly, I can use NetworkPriority component and set it's priorities to zero and use NetworkPriority::SetAlwaysUpdateOwner(true) at the beginning. I also noticed the node removing event is always replicated, no matter of the NetworkPriority.

EDIT: I realized the create event is also sent, no matter what the NetworkPriority says. So I already got it working perfectly with minimal effort. Nice :slight_smile:

-------------------------

