apat | 2017-01-02 01:10:29 UTC | #1

Not exactly related to Urho3D but anyway..

I'm using StaticModel to render some terrain (basically derived from a heightmap), now I would like to add roads, fields and other stuff to the terrain/surface. I would like to carve/stitch the roads, so that there will be no geometry beneath the road causing z fighting and such. I dont want to have the roads slightly above the terrain and use offsetting.

What would be the easiest way to accomplish this?. I dont know of any clipping/cutting API in Urho3D, anyone done something similar using 3rd party libraries?

Another option would be to use some savvy shaders but thats beyond my capabilities!

-------------------------

Bananaft | 2017-01-02 01:10:30 UTC | #2

Hi, welcome to the forum!

Do you want your roads to be static, always the same, or dynamic generated, by the game, and changable at runtime?

If first, you better just edit your mesh in 3d editor, and cut out the roads.

If second, you better look towards decals.

-------------------------

gawag | 2017-01-02 01:10:30 UTC | #3

Edit: Oh wait, whoops. You are using a StaticModel. You should be able to edit a mesh though. I played around with creating meshes by code once but had some issues but it worked Urho wise. You could change or replace parts of your terrain with code created meshes.

If you would be using the normal terrain you could do this:
You can change the heightmap and splatting map of the terrain during runtime.

This code increases the height of the terrain under the camera Node:
[code]
    IntVector2 v=terrain->WorldToHeightMap(cameraNode_->GetWorldPosition());
    Image* i=terrain->GetHeightMap();
    for(int x=-10;x<10;x++)
        for(int y=-10;y<10;y++)
            i->SetPixel(v.x_+x,v.y_+y,i->GetPixel(v.x_+x,v.y_+y)+Color(0.1,0.1,0.1));
    terrain->ApplyHeightMap();
[/code]
You could use such code to flatten the terrain where the road should be.

I also found code to change the splatting map but I'm not sure if it works, there may have been an issue:
[code]
    Texture2D* t=(Texture2D*)terrain->GetMaterial()->GetTexture(TU_DIFFUSE);
    Color c(1,0.1,0.1);
    for(int x=-10;x<10;x++)
        for(int y=-10;y<10;y++)
            t->SetData(0,x,y,1,1,&c);
    terrain->GetMaterial()->SetTexture(TU_DIFFUSE,t);
[/code]
Does that help you?

I don't think the terrain can actually be cut (out of the box) to replace it with custom models. You would have to extend the code to allow that. Such a feature would really be useful though.

Also ApplyHeightMap or SetTexture may have had a performance impact. It could be fixed by updating not all terrain parts at once but I don't know if that's currently possible. Such a feature would really be useful though, too.

-------------------------

apat | 2017-01-02 01:10:31 UTC | #4

Thanks for your answers!

The roads will be generated runtime but i'm not aiming to get them changable. 

The heightmap data is the dataset from SRTM (I will only use a part of it, not the whole globe), 3 arc sec so one triangle from the terrain is pretty large so there is no need for flattening where roads will be.

The heightmap is mapped to an earth size sphere (so the StaticModel is actually curved), its at/before this mapping I plan to cut out  roads/rivers and stuff (while it still is flat/2D). I found a library called clipper ([angusj.com/delphi/clipper/do ... /_Body.htm](http://www.angusj.com/delphi/clipper/documentation/Docs/_Body.htm)) that seems to be able to do what I want, so I'm going to try that.

-------------------------

