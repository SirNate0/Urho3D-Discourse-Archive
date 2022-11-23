patnav | 2020-02-10 02:48:48 UTC | #1

Hi Urho team, thanks a lot for your amazing job !

I'd like to create a minimap in my game. 

To do that , I have to 2 viewports and 2 cameras with different view mask
- Game viewport with mask 0x0001
- Map viewport with mask 0x0002 and an ortho camera

For each node, I add :
- a StaticModel or particule (whatever) with mask 0x0001 for game viewport
- a StaticSprite2D with mask 0x0002 for mini map

Everything work perfectly except, the StaticSprite2D take the rotation XYZ from the node
I need the node XYZ rotation for game view
but for map view I only need the Z rotation

Should I make my own "StaticMapSprite" component or make a pullrequest with a function to disable X,Y or Z rotation in StaticSprite2D ?

Thanks

-------------------------

Modanung | 2020-02-10 02:00:08 UTC | #2

Maybe a `BillboardSet` behaves closer to what you are looking for. There is a sample demonstrating its use included with the engine.

-------------------------

patnav | 2020-02-10 15:33:58 UTC | #3


You're right but:
- a BillboardSet per node with only one billboard is much more expensive
- a billboard  is updated to be face front to the camera
- Sprite and ortho camera are already XY aligned no update needed

I will create a specific code inherited from Drawable2D for my minimap

Thanks

-------------------------

Modanung | 2020-02-10 15:55:50 UTC | #4

On second thought: Could you not simply use a different rotation - possibly by adding a child node or a separate scene - to overcome this problem? Depending on the style of your minimap and the elements in your game there might be more elegant solutions. There is no need to render a landscape, for instance, if most of the world and the minimap camera are stationary. It could be rendered to a texture instead, once.
Could you share a screenshot of what you are working on?

-------------------------

Modanung | 2020-02-10 16:00:45 UTC | #5

[quote="patnav, post:3, topic:5910"]
* a BillboardSet per node with only one billboard is much more expensive
* a billboard is updated to be face front to the camera
[/quote]
You would only have to create one BillboardSet for each material/texture/icon. Different colours can be handled by  vertex colours.

-------------------------

patnav | 2020-02-14 19:42:00 UTC | #6

Screenshoot of game:
![image|690x478](upload://5cGe2YXRntXH0dVdXF1zeU3hVx7.jpeg) 

Minimap:
![image|489x500](upload://rwkpNP4o0tIfdHdyZvTU1LoWCzy.jpeg) 



Finally it's was a good choice to make a custom "MapSprite2D" largely inspired from StaticSprite2D

I can customize the node matrix
Ignore XY Rotation, Z translation and apply a custom scale factor

    Matrix3x4 worldTransform = node_->GetWorldTransform();

    Vector3 Translation;
    Quaternion Rotation;
    Vector3 Scale;

    worldTransform.Decompose(Translation, Rotation, Scale);
    Rotation.FromEulerAngles(0,0, Rotation.RollAngle());
    Scale*=scaleFactor_;
    Translation.z_ = 0;

    worldTransform = Matrix3x4(Translation, Rotation, Scale);


On 3D view (viewmask 0x01), Spaceship and Asteroid are static model 
The minimap (viewmask 0x02) Spaceship and Asteroid are custom 2D sprite inherited from Drawable2D

All the scene is replicated from server and all nodes are mobile with physics

-------------------------

Modanung | 2020-02-14 19:59:11 UTC | #7

I'm glad you found an elegant solution. Also; looking good, maybe you could share your progress in a dedicated thread or over at the [random project screenshots](https://discourse.urho3d.io/t/random-projects-shots/2431)?

-------------------------

