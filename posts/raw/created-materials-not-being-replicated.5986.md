evolgames | 2020-03-13 16:38:24 UTC | #1

I've got another scene replication question here.
When I do the following:

```
    local material=Material:new()
    material:SetShaderParameter("MatDiffColor",Variant(Vector4(.2,.2,.2,1)))
    matInnerWheel=material
```

I get gray (nil) materials. 
However, this works for scene replication:
```
	matHull=cache:GetResource("Material", "Materials/Green.xml")
	matHull:SetShaderParameter("MatDiffColor",Variant(Vector4(.05,.1,.05,1)))
```

Is there a reason for this? I'm using, as you can see, extremely simple coloring, so making a new material on the fly is preferred. It's not a problem to make an .xml file beforehand for each color that I'd need, but in the future it'd be nice to create these via code.

Looks like I can pull up the xml file and then adjust the parameters afterward, though. Any reason this is requiring an actual file?

-------------------------

1vanK | 2020-03-13 18:42:20 UTC | #2

Clone material before changing color

-------------------------

Modanung | 2020-03-13 20:06:45 UTC | #3

Note that if you're using a `StaticModelGroup` this will require a separate group for each material, and as such you might want to consider handling things like colour variations within a shader instead.

-------------------------

George1 | 2020-03-13 22:40:51 UTC | #4

I think most of the questions you asked are on the board if you search for it.  Some may have missing links.

https://discourse.urho3d.io/t/solved-material-clone-vs-setshaderparameter/683

-------------------------

evolgames | 2020-03-13 23:12:13 UTC | #5

@1vanK  I don't think you understand. Why clone a newly created material? I *dont* want to load a material xml file, so cloning it is not a solution. Furthermore, if I load the xml file I dont need to clone it anyway because it works when I load it. I want to create a new material on the fly. Cloning a newly created material doesnt work.

@George1 What does that thread have to do with scene replication?

This is for scene replication multiplayer. Here's the deal:
-host can see every material just fine, on every object, even if they are made with Material:New()
-clients only see material that are loaded from xml files 

If the host can see them, then I have no problem making the materials. Why is it that the clients can't see them?

@Modanung Shaders feel really unnecessary since the host can see newly created materials just fine. Isn't it just a matter of making sure the clients can see the same thing?

Client sees:
![Screenshot-5|690x369, 50%](upload://yoAUlSTtkh0GZIfYhpPNhIkl6Hq.jpeg) 
Host sees:
![Screenshot-6|690x369, 50%](upload://9lVwnNjaQdqpsQ5224e6TGtVC6H.jpeg) 

Only the hull material was loaded via xml, which is why the client sees it.


For example:
```
	 matHull=cache:GetResource("Material", "Materials/Green.xml")
	 matHull:SetShaderParameter("MatDiffColor",Variant(Vector4(.05,.1,.05,1)))
	
	 matWheel=Material:new()
     matWheel:SetShaderParameter("MatDiffColor",Variant(Vector4(.05,.05,.05,1)))
```

-------------------------

Modanung | 2020-03-13 23:15:17 UTC | #6

I think you might have to handle the cloning locally.

Shaders can be used to move more calculations to the GPU that might be expected. But at the same time premature optimization should be considered a pitfall, so it's something to keep in the back of your head.

-------------------------

evolgames | 2020-03-13 23:26:31 UTC | #7

But cloning a new material?
so, Material:new()
then Clone()? I don't understand why it needs to be cloned.

Oh yeah, I figure I'll see how this runs before I consider optimization at all. Aiming for lightweight and simple. My laptop is integrated graphics anyway.

By the way, the host creates the tanks, the clients only see them as replications in the scene. But for whatever reason clients can only see materials loaded by xml.

-------------------------

Modanung | 2020-03-13 23:32:27 UTC | #8

[quote="evolgames, post:7, topic:5986"]
I don’t understand why it needs to be cloned.
[/quote]

Ah, well you could start from scratch for each material. But you could also create a base material, keep a reference to it somwhere and use it as a template to clone from. Maybe even store the resulting materials in a HashMap of team-coloured materials.

-------------------------

evolgames | 2020-03-13 23:38:05 UTC | #9

Well I guess I was more wondering why the code created materials werent passing through. But like I said it isn't an issue to use xml files. And yeah, I'll probably just clone from the same one to make very simple colors. There is no need for any serious graphic work for this.

But it would be nice to know why it works with xml files and not newly created materials. Still wrapping my head around scene replication.

-------------------------

George1 | 2020-03-13 23:54:02 UTC | #10

I think your question is on having different color right?
That thread was on just that.  You could clone the material then overwrite color.   If you search for material clone.  

You need to have spawn event with color initialise for each client?

-------------------------

evolgames | 2020-03-13 23:56:29 UTC | #11

The problem is that only the host sees the materials. Clients can only see materials loaded via xml. Changing the color isn't an issue. I also don't need a lot of colors and I don't mind setting these up beforehand and loading with cache. However, I'd like to know why the code created materials aren't passing through but the xml loaded ones are.

-------------------------

Modanung | 2020-03-14 05:32:11 UTC | #12

[quote="evolgames, post:11, topic:5986"]
However, I’d like to know why the code created materials aren’t passing through but the xml loaded ones are.
[/quote]
I assume the xml ones aren't either, and that if the xml does not exist client-side, the loading will fail.

-------------------------

evolgames | 2020-03-14 00:09:28 UTC | #13

The SceneReplication sample does the same thing. This is run by the server host and the resulting ballNode is replicated in the scene.

```
function CreateControllableObject()
    -- Create the scene node & visual representation. This will be a replicated object
    local ballNode = scene_:CreateChild("Ball")
    ballNode.position = Vector3(Random(40.0) - 20.0, 5.0, Random(40.0) - 20.0)
    ballNode:SetScale(0.5)
    local ballObject = ballNode:CreateComponent("StaticModel")
    ballObject.model = cache:GetResource("Model", "Models/Sphere.mdl")
    ballObject.material = cache:GetResource("Material", "Materials/StoneSmall.xml")

    -- Create the physics components
    local body = ballNode:CreateComponent("RigidBody")
    body.mass = 1.0
    body.friction = 1.0
    -- In addition to friction, use motion damping so that the ball can not accelerate limitlessly
    body.linearDamping = 0.5
    body.angularDamping = 0.5
    local shape = ballNode:CreateComponent("CollisionShape")
    shape:SetSphere(1.0)

    -- Create a random colored point light at the ball so that can see better where is going
    local light = ballNode:CreateComponent("Light")
    light.range = 3.0
    light.color = Color(0.5 + RandomInt(2) * 0.5, 0.5 + RandomInt(2) * 0.5, 0.5 + RandomInt(2) * 0.5)

    return ballNode
end
```

And the client sees that xml loaded material. But if it is not loaded via xml the client wont see it.

I just confirmed this same thing happens with the sample. By changing that ballNode material to a newly created one it comes out grey to client, otherwise the xml will be replicated. Maybe @Miegamicis knows.

-------------------------

Modanung | 2020-03-14 00:25:53 UTC | #14

Resources in general are not _sent_ to clients. The server only tells them where to look.

-------------------------

evolgames | 2020-03-14 00:26:56 UTC | #15

So because the resource is loaded on the cache (I guess?), the client gets access, but if it is just a global material, they aren't able to? Hmmm...

-------------------------

Modanung | 2020-03-14 00:54:09 UTC | #16

No, the client has access because the data exists where it is expect to; in a resource folder on the local drive. But without wading in source I have to guess about the exact inner workings.

-------------------------

evolgames | 2020-03-14 00:54:39 UTC | #17

Ah okay, that makes sense enough for me! I will go ahead and stick to xml materials and cloning for this. Maybe I'll look around at the source when I have a little more experience ;)

-------------------------

