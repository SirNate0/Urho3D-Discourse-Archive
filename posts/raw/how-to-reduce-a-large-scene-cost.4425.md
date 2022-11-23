chenjie199234 | 2018-07-31 10:19:46 UTC | #1

I have a large scene and there are a lot of  models in this scene!Most of them are out of the camera,and i  dont want the graphics to draw them.but when they come into the camera,they will be draw automaticly.
I dont want to iterate all the models and caculate the distance.can this engine do this automaticly.

-------------------------

elix22 | 2018-07-31 12:48:41 UTC | #2

To my understanding  only by reading the code  ,you don't have to take care for it .
Adding  Octree component to your scene will do exactly that .
 i.e.  "scene_->CreateComponent<Octree>();"
You don't have to do anything 

Some reference  in the code :  
It's done each frame.

See file "/Urho3D-master/Source/Urho3D/Graphics/View.cpp" :
See Functions:
"void View::GetDrawables()" 
"void CheckVisibilityWork(const WorkItem* item, unsigned threadIndex)"

Eventually each drawable will contain a list of cameras  from which it will be visible from (or not) .
See file : "/Urho3D-master/Source/Urho3D/Graphics/Drawable.cpp" 
See Function : "bool Drawable::IsInView(Camera* camera) const"

-------------------------

