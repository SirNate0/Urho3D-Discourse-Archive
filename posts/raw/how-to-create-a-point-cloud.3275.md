SteveU3D | 2017-06-26 08:36:22 UTC | #1

Hi,
I have a set of 3D points and I would like to create it in my scene. I know how to create a dynamic mesh with vertex and face informations, but in the case of a point cloud, I have no information about the faces as there is no face.
So how to create a point cloud, with good performance of course :slight_smile: ?
Thanks.

-------------------------

johnnycable | 2017-06-22 10:37:48 UTC | #2

That is, are you trying to tessellate your point cloud?

-------------------------

glebedev | 2017-06-22 10:55:48 UTC | #3

2 ways of doing it as far as I know:
- custom mesh with point draw primitive 
- I can give you a MDL file with 32k points. You can update their position when it's needed. I'm using it with Google Tango.

-------------------------

slapin | 2017-06-22 13:45:53 UTC | #4

I think particles...

-------------------------

Modanung | 2017-06-22 17:44:43 UTC | #5

[quote="SteveU3D, post:1, topic:3275"]
I have no information about the faces as there is no face
[/quote]


Is this a requirement for custom geometry?

You could create your own `PointCloud` component that is linked to custom geometry for drawing and has a `Vector<Vector3> data_`.

-------------------------

SteveU3D | 2017-06-26 08:36:33 UTC | #6

Thanks for your answers. So, no tessallation, I just display the set of points with no treatment on it. I think particles is a bit too much for my case as I don't need transformation on the points.
I finally did it like any other dynamic mesh, using VertexBuffer, IndexBuffer and Geometry, and indeed, face information is not a requirement.

-------------------------

simonsch | 2018-03-29 10:29:08 UTC | #7

Could you provide a code example? I am trying to achieve an equal problem.

-------------------------

johnnycable | 2018-03-29 17:17:50 UTC | #8

in kabucode:

for "a vector3" in "a lot of vectors":
      ->change "vector3 intensity" by "random something"
      ->change "vector3 direction" by "random something"

you may want to set minimal scattering distance / harmonic function to avoid strange things...

-------------------------

simonsch | 2018-04-03 10:24:46 UTC | #9

It would really help if you could provide code how to build up the vertexbuffer, how to fill it dynamically in the scene update and how you bind it through the CustomGeometry.

-------------------------

johnnycable | 2018-04-03 11:35:34 UTC | #10

You may want to:
1) build an cloud of points thru some random / scattering technique
2) use a tessellation algorithm to obtain the external shape
3) pass the object to urho in a form it can understand

for 1) you can follow the previous kabucode I posted. Make a loop, take a point in space (vector3) and scatter it by its lenght (intensity) and direction (angle). Guess it's in urho.math
for 2) I don't know if urho has a tessellation system... guess not. (maybe somewhere scattered in the forum there's an implementation). You may be confortable using a 3d party tessellation library. There's a compact one here, [yoctogl](https://github.com/xelatihy/yocto-gl). Or you can try st like libigl, voro++, libtess2
for 3) I think you need to take all verts/edges/faces and create a static model or so. The process is roughly this:

        auto triangleMan = [&](){
    // custom geometry

        triangleNode = scene_->CreateChild("triangleNode");
        CustomGeometry* cg = triangleNode->CreateComponent<CustomGeometry>();
        cg->Clear();
        cg->SetNumGeometries(1);
        cg->BeginGeometry(0, PrimitiveType::TRIANGLE_LIST);
        // TRIANGLE MAN!
        // points are clockwise-ordered!
        cg->DefineVertex(Vector3(-1,0,0));
        cg->DefineColor(Color::GREEN);
        cg->DefineVertex(Vector3(0,1,0));
        cg->DefineColor(Color::RED);
        cg->DefineVertex(Vector3(1,0,0));
        cg->DefineColor(Color::BLUE);
        Material* mat = new Material(context_);
        auto teq = cache->GetResource<Technique>("Techniques/NoTextureUnlitVCol.xml");
        mat->SetTechnique(0, teq);
        cg->SetMaterial(mat);
        mat->SetFillMode(FillMode::FILL_SOLID);
        cg->Commit();
        // center of screen, ortho 2d elevation
        auto scp = camera->ScreenToWorldPoint(Vector3(0.5f,0.5f,-1));        
        triangleNode->SetPosition(scp);

    };

basicly if you can create a triangle you can create everything. You only need to feed all items in the right order...
In custom geometry you only need to pass points... if you pass them in the correct order, edges and faces are made for you... so theorically you _could_ skip tessellation if you follow the route correctly and build everything euclidean...
But given what you want you probably are better fit with a "normal" urho geometry object... but this is your skill

(p.s.) moreover, there's [iogram](https://discourse.urho3d.io/t/iogram-first-release/2340), a tool based on urho for building live geometry...

-------------------------

simonsch | 2018-04-03 14:41:54 UTC | #11

Thy for your answer, okay i think i have another problem i understand creating the CustomGeometry now. But i have large NEW pointclouds in each sceneupdate, which i need to add to the scene graph ~ 40 k points. This data is put into a std::vector from a library containing vertices, normals and color as float values. So i don't want to call ->DefineVertex(), etc.. for each point. I want to use something like VertexElements to tell urho how my data struct is build and then bind new data via indices directly through the VertexBuffer of the 'Geometry' which is basically just a List for PointPrimitives.

No Meshing, no tesselation. ;D

-------------------------

johnnycable | 2018-04-03 14:50:58 UTC | #12

Only other thing I remember is https://discourse.urho3d.io/t/a-mesh-generator/2361/5
but probably that's just what the solution above will do.

-------------------------

