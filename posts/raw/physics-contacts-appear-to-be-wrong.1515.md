thebluefish | 2017-01-02 01:08:13 UTC | #1

Maybe it's just been way too long since I've worked directly with Bullet, but I'm trying to wrap my head around:

[github.com/urho3d/Urho3D/blob/m ... d.cpp#L833](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Physics/PhysicsWorld.cpp#L833)

[code]
for (int j = 0; j < contactManifold->getNumContacts(); ++j)
{
    btManifoldPoint& point = contactManifold->getContactPoint(j);
    contacts_.WriteVector3(ToVector3(point.m_positionWorldOnB));
    contacts_.WriteVector3(ToVector3(point.m_normalWorldOnB));
    contacts_.WriteFloat(point.m_distance1);
    contacts_.WriteFloat(point.m_appliedImpulse);
}
[/code]

It seems to me that both NodeA and NodeB are receiving the same contact positions for NodeB. Shouldn't NodeA receive m_positionWorldOnA and m_normalWorldOnA?

-------------------------

1vanK | 2017-01-02 01:08:13 UTC | #2

No any wrongs. World coordinates of CONTACT is same. It is logical. But normal is inverted. See below

[code]
contacts_.WriteVector3(-ToVector3(point.m_normalWorldOnB));
[/code]

-------------------------

