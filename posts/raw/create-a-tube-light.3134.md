SteveU3D | 2017-06-21 16:40:05 UTC | #1

Hi,
I need to create a tube lighting in my application like the one here https://discourse.urho3d.io/t/solved-help-with-tube-lighting/2244.

I found the xml code which creates it in PBRExample.xml : 

    <node id="232">
        <attribute name="Is Enabled" value="true" />
	<attribute name="Name" value="" />
	<attribute name="Tags" />
	<attribute name="Position" value="6.54564 5.87075 -16.0652" />
	<attribute name="Rotation" value="1 0 0 0" />
	<attribute name="Scale" value="0.648644 0.648644 0.648644" />
	<attribute name="Variables" />
	<component type="Light" id="251">
	    <attribute name="Brightness Multiplier" value="800" />
	    <attribute name="Use Physical Values" value="true" />
            <attribute name="Radius" value="0.11" />
	    <attribute name="Length" value="6.53" />
	    <attribute name="Range" value="7.61" />
	    <attribute name="Spot FOV" value="62.08" />
	    <attribute name="Light Shape Texture" value="TextureCube;" />
	    <attribute name="Cast Shadows" value="true" />
	</component>
    </node>

I need to create it in C++. So I did : 

    //create a box to see the light
    Node* boxNode = scene_->CreateChild("Box");
    boxNode->SetScale(Vector3(10,10, 2));
    boxNode->SetPosition(Vector3(0, 0, 5));
    StaticModel* boxObject = boxNode->CreateComponent<StaticModel>();
    boxObject->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
    boxObject->SetCastShadows(true);
 
    //tube light
    Node* lightNode = scene_->CreateChild("TubeLight");
    Light* tubeLight = lightNode ->CreateComponent<Light>();
    tubeLight ->SetBrightness(800);
    tubeLight ->SetUsePhysicalValues(true);
    tubeLight ->SetRadius(0.11f);
    tubeLight ->SetLength(6.53f);
    tubeLight ->SetRange(7.61f);
    tubeLight ->SetFov(62.08f);
    tubeLight ->SetColor(Color(1.0f, 0.0f, 0.0f, 1.f));

    //what's the C++ equivalent for  <attribute name="Light Shape Texture" value="TextureCube;" />
    //there are the two following functions but I don't know which param to put
    //tubeLight ->SetShapeTextureAttr(...);
    //tubeLight ->SetShapeTexture(...)

    lightNode ->SetCastShadows(true);
    lightNode ->SetPosition(Vector3(0, 0, 3));
    lightNode ->SetScale(Vector3(0.648644, 0.648644, 0.648644));

With that code, I get the following : 

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/448c635ed1232f37bd105e891bae5d61a2ffdc79.png" width="582" height="500">

Thanks.

-------------------------

dragonCASTjosh | 2017-05-20 01:39:18 UTC | #2

I think i know the issue here. It doesnt look like you have set a material for the box, the default material does not use the PBR render path so can not use tube lights.

As for setting the light shape you shoudnt need to do that as long as you have the light set as a point light.

    tubeLight->SetLightType(LIGHT_POINT);
Any other issues or that doesnt work then let me know

-------------------------

SteveU3D | 2017-05-23 10:16:54 UTC | #3

So I added : 
    
    boxObject->SetMaterial(cache->GetResource<Material>("Materials/DefaultGrey.xml"));
    boxObject->GetMaterial(0)->SetTechnique(0, cache->GetResource<Technique>("Techniques/PBR/PBRNoTextureAlpha.xml"));
and 

    tubeLight->SetLightType(LIGHT_POINT);
    tubeLight ->SetColor(Color(1.0f, 1.0f, 1.0f, 1.f)); //change to white color

And I get the following (I also change the box size) : 
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/2092cf637a3097a9abf429713d7976540b9c0ae4.png" width="690" height="323">

On the right, when the camera is in front of the ligth, I have a point. On the left, when I translate the camera to the left (it does the same if I translate to the right, top and bottom), the light extends like that. I would like to always have that effect on the left, whatever the position of the camera :confused:

-------------------------

dragonCASTjosh | 2017-05-24 02:32:14 UTC | #4

[quote="SteveU3D, post:3, topic:3134"]
On the right, when the camera is in front of the ligth, I have a point. On the left, when I translate the camera to the left (it does the same if I translate to the right, top and bottom), th
[/quote]

So this could be one of many things, the easiest of them is that the light is rotated wrong, so try rotate the light 90 degrees to the right. i also recomend you turn the radius up a little so the tube is more prominent.

If the first thing doesnt work then what are you using D3D11, D3D9 or OpenGL. maybe one of the shaders has an issue (you can use the PBR test map to see if its the shaders)

-------------------------

SteveU3D | 2017-06-21 10:48:04 UTC | #5

[quote="dragonCASTjosh, post:4, topic:3134"]
So this could be one of many things, the easiest of them is that the light is rotated wrong, so try rotate the light 90 degrees to the right. i also recomend you turn the radius up a little so the tube is more prominent.
[/quote]

Thanks, that's the solution and here is the result, one light with  SetRotation(Quaternion(0,90,0)); and the other with SetRotation(Quaternion(90,0,0)); .
 <img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/0a51209ad14530766acfd1a01677f789d8345834.png" width="690" height="437">

-------------------------

