elemusic | 2017-01-02 01:11:09 UTC | #1

I am trying to create a Triangle with texture,code below
Run at 15_Navigation,i suppose i create a triangle facing Vector3(0,0,-1),facing my camera.
And from some other example code,i think i don't need to load texture cause they already in that xml file,right?
the code below does not display texture at all.and i have tried other material like StoneTiled.xml,Particle.xml,ect...
none of them work.what's wrong.

and there is another thing,why there is no indices to set?can't find any function about how to set indices about CustomGeometry

[code]
SharedPtr<Node> customNode(scene_->CreateChild("customNode"));
CustomGeometry* myGeometry = customNode->CreateComponent<CustomGeometry>();
myGeometry->DefineGeometry(0, TRIANGLE_LIST, 3, true, true, true, false);

myGeometry->BeginGeometry(0, TRIANGLE_LIST);
float dx = 5;
float dy = 5;
float dz = -5;
float offsetY = 10;
Vector3 pt0 = Vector3(-dx, dy + offsetY, dz);
Vector3 pt1 = Vector3(dx, dy + offsetY, dz);
Vector3 pt2 = Vector3(-dx, -dy + offsetY, dz);
	
Vector2 uv0 = Vector2(0, 0);
Vector2 uv1 = Vector2(1, 0);
Vector2 uv2 = Vector2(0, 1);

Vector3 n0 = Vector3(0, 0, -1);
	

myGeometry->DefineVertex(pt0);
myGeometry->DefineVertex(pt1);
myGeometry->DefineVertex(pt2);

myGeometry->DefineTexCoord(uv0);
myGeometry->DefineTexCoord(uv2);
myGeometry->DefineTexCoord(uv1);

myGeometry->DefineNormal(n0);
myGeometry->DefineNormal(n0);
myGeometry->DefineNormal(n0);

myGeometry->DefineColor(Color(1, 1, 1));

myGeometry->SetCastShadows(true);
myGeometry->SetMaterial(cache->GetResource<Material>("Materials/Mushroom.xml"));
myGeometry->Commit();
[/code]

-------------------------

cadaver | 2017-01-02 01:11:09 UTC | #2

You must interleave the calls. DefineVertex() always begins a new vertex, so follow it with DefineTexCoord, DefineNormal etc. Also DefineColor must be repeated for each vertex if you want colors (else it'll be undefined rubbish for the vertices you didn't call it for)

-------------------------

elemusic | 2017-01-02 01:11:11 UTC | #3

ok,i get it.works correct now,thanks

-------------------------

