kaapa | 2017-01-02 01:12:49 UTC | #1

Hello,

I am pretty new to Urho3D. As a side project, I've decided to make a simple rubik's cube game. Everything works fine, except that I can't get the texturing right. Basically, what I want to achieve is to have just one model, which will represent a single cubie which will be colored differently based on to which cube face it belongs. My problem is that, I don't know where to start. The documentation of materials tells me nothing. The one interesting thing I found was Cubemap, which to my understanding, will provide me with the ability to set different texture to different faces of the model. But, when using cubemap (I set all cubemap faces to be red), my whole cube went completely black.

To sum up:

1) I want to have just one model.
2) I want to set different colors to different cube faces.

And I completely don't know how to do that, or even search for info/examples on how to do it. Do you guys know how to do it? Do you have any examples of something like this working?

What I've done is this

material - rubiks.xml

[code]<material>
    <technique name="Techniques/DiffNormal.xml" />
    <texture unit="normal" name="Textures/rubiks.xml" />
    <cull value="none" />

</material>[/code]

texture - rubiks.xml

[code]<cubemap>
    <face name="red.png" />
    <face name="red.png" />
    <face name="red.png" />
    <face name="red.png" />
    <face name="red.png" />
    <face name="red.png" />
    <quality low="0" />
</cubemap>
[/code]

Where red.png is just 16x16 png image.

Thanks,
Kacper

-------------------------

Modanung | 2017-01-02 01:12:50 UTC | #2

A cubemap is not what you're looking for. Those are used for reflections and backgrounds.

[url=http://luckeyproductions.nl/mdl/RubixCubie.mdl]This model[/url] [url=http://luckeyproductions.nl/blends/RubixCubie.blend][Blend][/url] uses vertex colors. Applying a material with a VCol technique will show the colors.
There's a lot of ways you could do this, but I think this is the most straightforward one.

I know it's better to teach a person how to fish than to give one a fish. But I think this is more like providing a hook. :slight_smile:

-------------------------

kaapa | 2017-01-02 01:12:50 UTC | #3

great, thanks for help!

Meanwhile I've figured out that I can make a blender cube model which will have 6 different materials (one per side), and then just use SetMaterial method (with proper material index as a first argument) to set different colored materials. Is it going to work?

Thanks,
Kacper

-------------------------

1vanK | 2017-01-02 01:12:50 UTC | #4

Why do you need 6 materials? Just unwrap cube model and paint texture with 6 colored rectangles.

-------------------------

Modanung | 2017-01-02 01:12:50 UTC | #5

[quote="kaapa"]Meanwhile I've figured out that I can make a blender cube model which will have 6 different materials (one per side), and then just use SetMaterial method (with proper material index as a first argument) to set different colored materials. Is it going to work?[/quote]
Yes, that would be another way. Mind you that for the Geometry indices to match the material order in Blender you usually need to [url=https://www.blender.org/manual/modeling/meshes/editing/misc.html]sort the elements[/url] by material.
Eight months ago CodeMonkey provided this image to help me find it:
[url=http://savepic.su/6184007.png][img]http://savepic.su/6184007m.png[/img][/url]

In case you need to do this for many objects in the future, this python script will do the same for all selected objects:
[code]
import bpy

for ob in bpy.context.selected_objects:
    bpy.context.scene.objects.active = ob
    
    bpy.ops.object.mode_set(mode = 'EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.sort_elements(type='MATERIAL', elements={'FACE'})
    bpy.ops.object.mode_set(mode = 'OBJECT')[/code]

For assigning the materials (in C++11) you're probably best of using something like:
[code]
for (int i{0}; i < model->GetNumGeometries(); ++i) {

    Material* material{ GetResource<Material>(path)->Clone() };
    switch (i){
    default:
    case 0: material->SetShaderParameter("MatDiffColor", Color::WHITE);
    break;
    case 1: material->SetShaderParameter("MatDiffColor", Color::RED);
    break;
    ...
    }
    model->SetMaterial(i, material);
}

[/code]
That way you don't have to create and edit six materials and the glossiness or technique can be changed by editing this one material. Cloning the materials once for the entire cube would be more efficient though.

-------------------------

