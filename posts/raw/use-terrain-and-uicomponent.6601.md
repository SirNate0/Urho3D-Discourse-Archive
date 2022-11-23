baiyqukq | 2020-12-07 01:10:51 UTC | #1

In "Hello3DGUI" sample, if create a terrain, just copy the code from "VehicleDemo", there are lots of warnings:
WARNING: RAY_TRIANGLE_UV query level is not supported for TerrainPatch component

-------------------------

1vanK | 2020-12-07 07:56:53 UTC | #3

Looks like we need way to set ray mask for UIComponent

-------------------------

baiyqukq | 2020-12-07 08:57:58 UTC | #6

Thank you. I have added "CHECK" code and tested, but warnings still appear, and performance is bad as before.

-------------------------

Eugene | 2020-12-07 09:18:46 UTC | #7

[quote="baiyqukq, post:1, topic:6601"]
WARNING: RAY_TRIANGLE_UV query level is not supported for TerrainPatch component
[/quote]
Can you check what callstack leads to this warning? Who is trying to ray-cast TerrainPatch with level `RAY_TRIANGLE_UV`?

-------------------------

1vanK | 2020-12-07 09:22:31 UTC | #8

> Who is trying to ray-cast TerrainPatch with level `RAY_TRIANGLE_UV` ?

UIComponent

-------------------------

baiyqukq | 2020-12-07 10:22:51 UTC | #9

Making this warning is very simple, just copy code from 19_VehicleDemo in CreateScene() as follow:
// Create heightmap terrain with collision
 Node* terrainNode = scene_->CreateChild("Terrain");
...
shape->SetTerrain();
To 48_Hello3DUI sample in InitScene() as follow:
light->SetSpecularIntensity(0.5f);
###copied here###
auto* zone = scene_->CreateComponent<Zone>();

callstack:
1  Urho3D::TerrainPatch::ProcessRayQuery        TerrainPatch.cpp 113  0xa21a42 
2  Urho3D::Octant::GetDrawablesInternal         Octree.cpp       273  0x60eab9 
3  Urho3D::Octant::GetDrawablesInternal         Octree.cpp       280  0x60eb0d 
4  Urho3D::Octant::GetDrawablesInternal         Octree.cpp       280  0x60eb0d 
5  Urho3D::Octant::GetDrawablesInternal         Octree.cpp       280  0x60eb0d 
6  Urho3D::Octree::Raycast                      Octree.cpp       506  0x60fffb 
7  Urho3D::UIElement3D::ScreenToElement         UIComponent.cpp  120  0x4324a0 
8  Urho3D::UI::GetElementAt                     UI.cpp           796  0x439f0d 
9  Urho3D::UI::ProcessHover                     UI.cpp           1346 0x43c3ad 
10 Urho3D::UI::Update                           UI.cpp           376  0x438100 
11 Urho3D::UI::HandlePostUpdate                 UI.cpp           2048 0x43f8d2 
12 Urho3D::EventHandlerImpl<Urho3D::UI>::Invoke Object.h         323  0x44aae9 
13 Urho3D::Object::OnEvent                      Object.cpp       127  0x6aa1b6 
14 Urho3D::Object::SendEvent                    Object.cpp       364  0x6aacc9 
15 Urho3D::Engine::Update                       Engine.cpp       696  0x691902 
16 Urho3D::Engine::RunFrame                     Engine.cpp       517  0x691254 
17 Urho3D::Application::Run                     Application.cpp  86   0x69de05 
18 RunApplication                               Hello3DUI.cpp    53   0x40a163 
19 main                                         Hello3DUI.cpp    53   0x40a1fd

-------------------------

