extobias | 2017-02-22 16:14:22 UTC | #1

Hi
Im trying to implement a vehicle simulation. In a document from Kester Maddock [[1]]   (https://docs.google.com/document/d/18edpOwtGgCwNyvakS78jxMajCuezotCU_0iezcwiFQc/edit), recommends interpolating the normals to improve the simulation. One of the requirements for this is to implement your own btStridingMeshInterface subclass. From Urho3D source code, I've read that TriangleMeshInterface is a subclass from btStridingMeshInterface through btTriangleIndexVertexArray.
The question is if there is a way to get the normals without modifying TriangleMeshInterface? Also, why this class is hidden for subclassing?
Any help would be appreciated.
Thanks in advance.
Best regards,
Tobias.

-------------------------

jmiller | 2017-02-22 17:43:12 UTC | #2

Hi Tobias,

Urho does not expose much of Bullet, so using it directly could make more sense.
Maybe a core dev will see this and have modified the interface in a matter of hours. :)
And always, we are welcome to propose or pull-request additional API/bindings.

By the way, there are a number of [url=http://discourse.urho3d.io/search?q=vehicle]vehicle-related[/url] bits around for reference.
http://discourse.urho3d.io/t/btraycastvehicle-example/1306

-------------------------

extobias | 2017-02-22 18:45:00 UTC | #3

@jmiller thanks for response. I've been able to implement successfully the vehicle (I use a similar approach of @Lumak offroad vehicle implementation). Now, I want to get a more smoother driving and found Kester's notes.
I've a few ideas on the modifications required for this, but I want to know if there is a more easy way to do it, or at least what's are the base guidelines for this classes.
Best regards,
Tobias.

-------------------------

