camel | 2017-01-02 01:04:38 UTC | #1

hello everyone
i come from china and i like urho3d 
i have some problem and please help me,thanks
for urho3d-master, compiled and completed with vs2012.

I want to create an own skybox in the engines. 
So I created MySkyBox.h, MySkyBox.cpp in D: \ Urho3D-master \ Source \ Urho3D \ Graphics
Here is the code of these two documents

MySkyBox.h
[code]
#pragma once
#include "../Graphics/StaticModel.h"
namespace Urho3D
{
class URHO3D_API MySkyBox:public StaticModel
{
	OBJECT(MySkyBox);
public:
	MySkyBox(Context* context);
	virtual ~MySkyBox();

	static void RegisterObject(Context* context);

	virtual void ProcessRayQuery(const RayOctreeQuery& query, PODVector<RayQueryResult>& results){};
	virtual void UpdateBatches(const FrameInfo& frame){};
protected:
	virtual void OnWorldBoundingBoxUpdate(){};
};
}
[/code]

MySkyBox.cpp
[code]
#include "../Scene/Node.h"
#include "../Graphics/MySkyBox.h"

#include "../DebugNew.h"

namespace Urho3D
{
	MySkyBox::MySkyBox(Context* context):StaticModel(context)
	{

	}
}
[/code]

For simplicity, I just wrote a little code.
But I compile MySkyBox.cpp appeared in the 202 error.

My English is not good, please forgive me
And please help me for the above problem
??! (thanks!)

-------------------------

camel | 2017-01-02 01:04:38 UTC | #2

Picture

[img]http://www.mftp.info/20150401/1428746358x758668068.jpg[/img]

[img]http://www.mftp.info/20150401/1428746422x758668068.jpg[/img]

-------------------------

weitjong | 2017-01-02 01:04:39 UTC | #3

Welcome to our forum (????)

I am not sure why you need to write another skybox component but assuming this is just for exercise to get to know Urho3D library then I suppose the compilation error you encountered was due to missing include of "Urho3D.h". You don't see this include statement explicitly being written in the original library code because it has already been added in the precompiled header file used when building the library. For your own code, you will always need to include this "Urho3D.h" as the first thing you do. Unless you also use the same trick as Urho3D project to add that include into another precompiled header file specific for your own project.

-------------------------

camel | 2017-01-02 01:04:39 UTC | #4

[quote="weitjong"]Welcome to our forum (????)

I am not sure why you need to write another skybox component but assuming this is just for exercise to get to know Urho3D library then I suppose the compilation error you encountered was due to missing include of "Urho3D.h". You don't see this include statement explicitly being written in the original library code because it has already been added in the precompiled header file used when building the library. For your own code, you will always need to include this "Urho3D.h" as the first thing you do. Unless you also use the same trick as Urho3D project to add that include into another precompiled header file specific for your own project.[/quote]

First of all, thank you for your help, it really works.
It makes me feel very friendly forum.
I created another skybox Component is to practice
thanks again

-------------------------

jmiller | 2017-01-02 01:04:40 UTC | #5

Welcome to the forum, camel.

I also started with Skybox when I started creating my own sky component.

You can also use this form of include, if you add your build tree include directory to system headers path.
#include <Urho3D/Graphics/StaticModel.h>

If you would like hints on making a new Component...

Remember to register your component. You can do this in your Application constructor.
MySkyBox::RegisterObject(context);

Method (declared [i]static[/i] in header):
[code]void MySkyBox::RegisterObject(Context* context) {
  context->RegisterFactory<MySkyBox>();
  COPY_BASE_ATTRIBUTES(StaticModel);
}[/code]

If you override OnNodeSet(), you might want to also call the base version there: StaticModel::OnNodeSet(node).

One problem I had (which could be my mistake): My Skybox often did not load the Model + Material automatically, so I used something like this in OnNodeSet():
  SetModel(GetSubsystem<ResourceCache>()->GetResource<Model>("models/box.mdl"));
  SetMaterial(GetSubsystem<ResourceCache>()->GetResource<Material>("materials/Skybox.xml"));

-------------------------

