godan | 2017-01-02 01:05:39 UTC | #1

So, I'm trying to extend Urho3D lib with some custom functionality that will be callable via the script engine. To do this, I create the most basic case possible:

[code]
#pragma once

#include "../Scene/Component.h"

namespace Urho3D
{
	class URHO3D_API MeshSmooth : public Component
	{
		OBJECT(MeshSmooth);
	public:
		/// Construct.
		MeshSmooth(Context* context);
		/// Destruct. Free the rigid body and geometries.
		virtual ~MeshSmooth();
		/// Register object factory.
		static void RegisterObject(Context* context);
	};
}
[/code]

The problem is, the compiler (I'm using VS2012) isn't recognizing the URHO3D_API declaration... 

[img]https://dl.dropboxusercontent.com/u/69779082/urho_issue.PNG[/img]

And while the project compiles, VS is telling me that URHO3D_API is undefined, so I'm pretty sure something is up. Could it have to do with how cmake creates the project files? Not really sure where to begin here.

-------------------------

v0van1981 | 2017-01-02 01:05:39 UTC | #2

URHO3D_API defined in Urho3d.h, try to include it. This file also included in CMake & Precompiled.h

-------------------------

v0van1981 | 2017-01-02 01:05:39 UTC | #3

In my projects I use a file sdfafx.h 

[code]#pragma once

#include <Urho3D/Urho3D.h>

#include <Urho3D/Revision.h>
#include <Urho3D/Audio/Audio.h>
#include <Urho3D/Audio/AudioDefs.h>
#include <Urho3D/Audio/BufferedSoundStream.h>
#include <Urho3D/Audio/OggVorbisSoundStream.h>
#include <Urho3D/Audio/Sound.h>
#include <Urho3D/Audio/SoundListener.h>
#include <Urho3D/Audio/SoundSource.h>
#include <Urho3D/Audio/SoundSource3D.h>
#include <Urho3D/Audio/SoundStream.h>
#include <Urho3D/Container/Allocator.h>
#include <Urho3D/Container/ArrayPtr.h>
#include <Urho3D/Container/ForEach.h>
#include <Urho3D/Container/Hash.h>
#include <Urho3D/Container/HashBase.h>
#include <Urho3D/Container/HashMap.h>
#include <Urho3D/Container/HashSet.h>
#include <Urho3D/Container/LinkedList.h>
#include <Urho3D/Container/List.h>
#include <Urho3D/Container/ListBase.h>
#include <Urho3D/Container/Pair.h>
#include <Urho3D/Container/Ptr.h>
#include <Urho3D/Container/RefCounted.h>
#include <Urho3D/Container/Sort.h>
#include <Urho3D/Container/Str.h>
#include <Urho3D/Container/Swap.h>
#include <Urho3D/Container/Vector.h>
#include <Urho3D/Container/VectorBase.h>
#include <Urho3D/Core/Attribute.h>
#include <Urho3D/Core/Condition.h>
#include <Urho3D/Core/Context.h>
#include <Urho3D/Core/CoreEvents.h>
#include <Urho3D/Core/Main.h>
#include <Urho3D/Core/MiniDump.h>
#include <Urho3D/Core/Mutex.h>
#include <Urho3D/Core/Object.h>
#include <Urho3D/Core/ProcessUtils.h>
#include <Urho3D/Core/Profiler.h>
#include <Urho3D/Core/Spline.h>
#include <Urho3D/Core/StringUtils.h>
#include <Urho3D/Core/Thread.h>
#include <Urho3D/Core/Timer.h>
#include <Urho3D/Core/Variant.h>
#include <Urho3D/Core/WorkQueue.h>
#include <Urho3D/Engine/Application.h>
#include <Urho3D/Engine/Console.h>
#include <Urho3D/Engine/DebugHud.h>
#include <Urho3D/Engine/Engine.h>
#include <Urho3D/Engine/EngineEvents.h>
#include <Urho3D/Graphics/AnimatedModel.h>
#include <Urho3D/Graphics/Animation.h>
#include <Urho3D/Graphics/AnimationController.h>
#include <Urho3D/Graphics/AnimationState.h>
#include <Urho3D/Graphics/Batch.h>
#include <Urho3D/Graphics/BillboardSet.h>
#include <Urho3D/Graphics/Camera.h>
#include <Urho3D/Graphics/ConstantBuffer.h>
#include <Urho3D/Graphics/CustomGeometry.h>
#include <Urho3D/Graphics/DebugRenderer.h>
#include <Urho3D/Graphics/DecalSet.h>
#include <Urho3D/Graphics/Drawable.h>
#include <Urho3D/Graphics/DrawableEvents.h>
#include <Urho3D/Graphics/Geometry.h>
#include <Urho3D/Graphics/GPUObject.h>
#include <Urho3D/Graphics/Graphics.h>
#include <Urho3D/Graphics/GraphicsDefs.h>
#include <Urho3D/Graphics/GraphicsEvents.h>
#include <Urho3D/Graphics/GraphicsImpl.h>
#include <Urho3D/Graphics/IndexBuffer.h>
#include <Urho3D/Graphics/Light.h>
#include <Urho3D/Graphics/Material.h>
#include <Urho3D/Graphics/Model.h>
#include <Urho3D/Graphics/OcclusionBuffer.h>
#include <Urho3D/Graphics/Octree.h>
#include <Urho3D/Graphics/OctreeQuery.h>
#include <Urho3D/Graphics/ParticleEffect.h>
#include <Urho3D/Graphics/ParticleEmitter.h>
#include <Urho3D/Graphics/Renderer.h>
#include <Urho3D/Graphics/RenderPath.h>
#include <Urho3D/Graphics/RenderSurface.h>
#include <Urho3D/Graphics/Shader.h>
#include <Urho3D/Graphics/ShaderPrecache.h>
#include <Urho3D/Graphics/ShaderProgram.h>
#include <Urho3D/Graphics/ShaderVariation.h>
#include <Urho3D/Graphics/Skeleton.h>
#include <Urho3D/Graphics/Skybox.h>
#include <Urho3D/Graphics/StaticModel.h>
#include <Urho3D/Graphics/StaticModelGroup.h>
#include <Urho3D/Graphics/Tangent.h>
#include <Urho3D/Graphics/Technique.h>
#include <Urho3D/Graphics/Terrain.h>
#include <Urho3D/Graphics/TerrainPatch.h>
#include <Urho3D/Graphics/Texture.h>
#include <Urho3D/Graphics/Texture2D.h>
#include <Urho3D/Graphics/Texture3D.h>
#include <Urho3D/Graphics/TextureCube.h>
#include <Urho3D/Graphics/VertexBuffer.h>
#include <Urho3D/Graphics/VertexDeclaration.h>
#include <Urho3D/Graphics/View.h>
#include <Urho3D/Graphics/Viewport.h>
#include <Urho3D/Graphics/Zone.h>
#include <Urho3D/Input/Controls.h>
#include <Urho3D/Input/Input.h>
#include <Urho3D/Input/InputEvents.h>
#include <Urho3D/IO/Compression.h>
#include <Urho3D/IO/Deserializer.h>
#include <Urho3D/IO/File.h>
#include <Urho3D/IO/FileSystem.h>
#include <Urho3D/IO/FileWatcher.h>
#include <Urho3D/IO/IOEvents.h>
#include <Urho3D/IO/Log.h>
#include <Urho3D/IO/MacFileWatcher.h>
#include <Urho3D/IO/MemoryBuffer.h>
#include <Urho3D/IO/PackageFile.h>
#include <Urho3D/IO/RWOpsWrapper.h>
#include <Urho3D/IO/Serializer.h>
#include <Urho3D/IO/VectorBuffer.h>
#include <Urho3D/Math/AreaAllocator.h>
#include <Urho3D/Math/BoundingBox.h>
#include <Urho3D/Math/Color.h>
#include <Urho3D/Math/Frustum.h>
#include <Urho3D/Math/MathDefs.h>
#include <Urho3D/Math/Matrix3.h>
#include <Urho3D/Math/Matrix3x4.h>
#include <Urho3D/Math/Matrix4.h>
#include <Urho3D/Math/Plane.h>
#include <Urho3D/Math/Polyhedron.h>
#include <Urho3D/Math/Quaternion.h>
#include <Urho3D/Math/Random.h>
#include <Urho3D/Math/Ray.h>
#include <Urho3D/Math/Rect.h>
#include <Urho3D/Math/Sphere.h>
#include <Urho3D/Math/StringHash.h>
#include <Urho3D/Math/Vector2.h>
#include <Urho3D/Math/Vector3.h>
#include <Urho3D/Math/Vector4.h>
#include <Urho3D/Navigation/Navigable.h>
#include <Urho3D/Navigation/NavigationMesh.h>
#include <Urho3D/Navigation/OffMeshConnection.h>
#include <Urho3D/Network/Connection.h>
#include <Urho3D/Network/HttpRequest.h>
#include <Urho3D/Network/Network.h>
#include <Urho3D/Network/NetworkEvents.h>
#include <Urho3D/Network/NetworkPriority.h>
#include <Urho3D/Network/Protocol.h>
#include <Urho3D/Physics/CollisionShape.h>
#include <Urho3D/Physics/Constraint.h>
#include <Urho3D/Physics/PhysicsEvents.h>
#include <Urho3D/Physics/PhysicsUtils.h>
#include <Urho3D/Physics/PhysicsWorld.h>
#include <Urho3D/Physics/RigidBody.h>
#include <Urho3D/Resource/BackgroundLoader.h>
#include <Urho3D/Resource/Decompress.h>
#include <Urho3D/Resource/Image.h>
#include <Urho3D/Resource/JSONFile.h>
#include <Urho3D/Resource/JSONValue.h>
#include <Urho3D/Resource/PListFile.h>
#include <Urho3D/Resource/Resource.h>
#include <Urho3D/Resource/ResourceCache.h>
#include <Urho3D/Resource/ResourceEvents.h>
#include <Urho3D/Resource/XMLElement.h>
#include <Urho3D/Resource/XMLFile.h>
#include <Urho3D/Scene/Animatable.h>
#include <Urho3D/Scene/AnimationDefs.h>
#include <Urho3D/Scene/Component.h>
#include <Urho3D/Scene/LogicComponent.h>
#include <Urho3D/Scene/Node.h>
#include <Urho3D/Scene/ObjectAnimation.h>
#include <Urho3D/Scene/ReplicationState.h>
#include <Urho3D/Scene/Scene.h>
#include <Urho3D/Scene/SceneEvents.h>
#include <Urho3D/Scene/SceneResolver.h>
#include <Urho3D/Scene/Serializable.h>
#include <Urho3D/Scene/SmoothedTransform.h>
#include <Urho3D/Scene/SplinePath.h>
#include <Urho3D/Scene/UnknownComponent.h>
#include <Urho3D/Scene/ValueAnimation.h>
#include <Urho3D/Scene/ValueAnimationInfo.h>
#include <Urho3D/Script/Addons.h>
#include <Urho3D/Script/APITemplates.h>
#include <Urho3D/Script/Script.h>
#include <Urho3D/Script/ScriptAPI.h>
#include <Urho3D/Script/ScriptEventListener.h>
#include <Urho3D/Script/ScriptFile.h>
#include <Urho3D/Script/ScriptInstance.h>
#include <Urho3D/UI/BorderImage.h>
#include <Urho3D/UI/Button.h>
#include <Urho3D/UI/CheckBox.h>
#include <Urho3D/UI/Cursor.h>
#include <Urho3D/UI/DropDownList.h>
#include <Urho3D/UI/FileSelector.h>
#include <Urho3D/UI/Font.h>
#include <Urho3D/UI/FontFace.h>
#include <Urho3D/UI/FontFaceBitmap.h>
#include <Urho3D/UI/FontFaceFreeType.h>
#include <Urho3D/UI/LineEdit.h>
#include <Urho3D/UI/ListView.h>
#include <Urho3D/UI/Menu.h>
#include <Urho3D/UI/MessageBox.h>
#include <Urho3D/UI/ScrollBar.h>
#include <Urho3D/UI/ScrollView.h>
#include <Urho3D/UI/Slider.h>
#include <Urho3D/UI/Sprite.h>
#include <Urho3D/UI/Text.h>
#include <Urho3D/UI/Text3D.h>
#include <Urho3D/UI/ToolTip.h>
#include <Urho3D/UI/UI.h>
#include <Urho3D/UI/UIBatch.h>
#include <Urho3D/UI/UIElement.h>
#include <Urho3D/UI/UIEvents.h>
#include <Urho3D/UI/View3D.h>
#include <Urho3D/UI/Window.h>
#include <Urho3D/Urho2D/AnimatedSprite2D.h>
#include <Urho3D/Urho2D/Animation2D.h>
#include <Urho3D/Urho2D/AnimationSet2D.h>
#include <Urho3D/Urho2D/CollisionBox2D.h>
#include <Urho3D/Urho2D/CollisionChain2D.h>
#include <Urho3D/Urho2D/CollisionCircle2D.h>
#include <Urho3D/Urho2D/CollisionEdge2D.h>
#include <Urho3D/Urho2D/CollisionPolygon2D.h>
#include <Urho3D/Urho2D/CollisionShape2D.h>
#include <Urho3D/Urho2D/Constraint2D.h>
#include <Urho3D/Urho2D/ConstraintDistance2D.h>
#include <Urho3D/Urho2D/ConstraintFriction2D.h>
#include <Urho3D/Urho2D/ConstraintGear2D.h>
#include <Urho3D/Urho2D/ConstraintMotor2D.h>
#include <Urho3D/Urho2D/ConstraintMouse2D.h>
#include <Urho3D/Urho2D/ConstraintPrismatic2D.h>
#include <Urho3D/Urho2D/ConstraintPulley2D.h>
#include <Urho3D/Urho2D/ConstraintRevolute2D.h>
#include <Urho3D/Urho2D/ConstraintRope2D.h>
#include <Urho3D/Urho2D/ConstraintWeld2D.h>
#include <Urho3D/Urho2D/ConstraintWheel2D.h>
#include <Urho3D/Urho2D/Drawable2D.h>
#include <Urho3D/Urho2D/ParticleEffect2D.h>
#include <Urho3D/Urho2D/ParticleEmitter2D.h>
#include <Urho3D/Urho2D/PhysicsEvents2D.h>
#include <Urho3D/Urho2D/PhysicsUtils2D.h>
#include <Urho3D/Urho2D/PhysicsWorld2D.h>
#include <Urho3D/Urho2D/Renderer2D.h>
#include <Urho3D/Urho2D/RigidBody2D.h>
#include <Urho3D/Urho2D/Sprite2D.h>
#include <Urho3D/Urho2D/SpriteSheet2D.h>
#include <Urho3D/Urho2D/StaticSprite2D.h>
#include <Urho3D/Urho2D/TileMap2D.h>
#include <Urho3D/Urho2D/TileMapDefs2D.h>
#include <Urho3D/Urho2D/TileMapLayer2D.h>
#include <Urho3D/Urho2D/TmxFile2D.h>
#include <Urho3D/Urho2D/Urho2D.h>

#include <Urho3D/DebugNew.h>

using namespace Urho3D;
[/code]

And include it anywhere
	
Script for generating stdafx.h (C#):

[code]using System.IO;


class CreateStdafx
{
    const string ???? = @"d:/MyGames/Engine/Build/include/";
    const bool Lua = false;

    static void Main(string[] args)
    {
        StreamWriter ????????? = File.CreateText("stdafx.h");
        ?????????.WriteLine("#pragma once");
        ?????????.WriteLine();
        ?????????.WriteLine("#include <Urho3D/Urho3D.h>");
        ?????????.WriteLine();

        foreach (string ???? in Directory.EnumerateFiles(????, "*.*", SearchOption.AllDirectories))
        {
            string ?????? = ????.Replace('\\', '/');
            ?????? = ??????.Replace(????, "");
            if (??????.StartsWith("Urho3D/ThirdParty"))
                continue;
            if (??????.StartsWith("Urho3D/Graphics/Direct3D"))
                continue;
            if (??????.StartsWith("Urho3D/Graphics/OpenGL"))
                continue;
            if (??????.StartsWith("Urho3D/LuaScript") && !Lua)
                continue;
            if (?????? == "Urho3D/DebugNew.h")
                continue;
            if (?????? == "Urho3D/librevision.h")
                continue;
            if (?????? == "Urho3D/Precompiled.h")
                continue;
            if (?????? == "Urho3D/Urho3D.h")
                continue;
            ?????? = "#include <" + ?????? + ">";
            ?????????.WriteLine(??????);
        }

        ?????????.WriteLine();
        ?????????.WriteLine("#include <Urho3D/DebugNew.h>");
        ?????????.WriteLine();
        ?????????.WriteLine("using namespace Urho3D;");
        ?????????.Close();
    }
}
[/code]

-------------------------

friesencr | 2017-01-02 01:05:39 UTC | #4

When you are working in Urho's source, that error is usually a symptom of another error that prevents the the build from generating the urho3d.h file.

-------------------------

weitjong | 2017-01-02 01:05:39 UTC | #5

It looks like you have superseded the provided "Precompiled.h" with your own "stdafx.h" file. We usually do not advise user to abuse PCH in this way. The purpose of PCH is speeding up the build, not to save typing.

Assuming the "Urho3D.h" is being generated correctly, I suppose your problem come from the "stdafx.h" not being included in all the Urho3D source files as you have claimed. Did you modify the Urho3D's CMakeLists.txt also to tell CMake to configure MSVC to use it? Or you just did this manually via Visual Studio IDE? Observe the last argument in this line. [github.com/urho3d/Urho3D/blob/m ... s.txt#L143](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/CMakeLists.txt#L143). You may want to modify it to "stdafx.h". However, once you do that, you are on your own.

-------------------------

godan | 2017-01-02 01:05:40 UTC | #6

Hi all, 

Thanks for the input. Just to clarify - the whole stdfx.h thing was a suggestion from another user and not actually my situation.

All I've done is within the VS2012 solution (i.e. I've successfully used cmake to create the solution and can build Urho), I've created a new file called MeshSmooth.h and I'm trying to inherit from Component in order to extend Urho's functionality, directly within the Urho lib project. Basically, I'm trying to replicate something like the RigidBody.h class.

However, just creating a new file and including "..Scene/Component.h" doesn't do the trick (see my last post). Do I need to add my new files to the CMake build system? What is the role of "Precompiled.h"?

More generally, if I'm totally on the wrong track here, how would I go about adding a new class directly to the Urho lib source?

-------------------------

godan | 2017-01-02 01:05:40 UTC | #7

Looks like simply including "Precompiled.h" in my MeshSmooth.h class does the trick. Pretty obvious, really :slight_smile:

I might be back with more questions on how to hook up the script API, but for now, onwards!

-------------------------

godan | 2017-01-02 01:05:40 UTC | #8

As anticipated, I'm having issues now with getting AngelScript to recognize my new component. Here's what I've done:

- I've created a new component MeshSmooth that inherits from Component:

[code]

#pragma once

#include "Precompiled.h"
#include "Scene\Component.h"

namespace Urho3D
{
	class URHO3D_API MeshSmooth : public Component
	{
		OBJECT(MeshSmooth);
	public:
		/// Construct.
		MeshSmooth(Context* context);
		/// Destruct. Free the rigid body and geometries.
		virtual ~MeshSmooth();
		/// Register object factory.
		static void RegisterObject(Context* context);
		//main function
		void SmoothMesh();
	};
}
[/code]

I've created a GeometryAPI class (similar to the other API's that implements the various registering functions):

[code]
#include "Precompiled.h"
#include "../Script/APITemplates.h"
#include "../Geometry/MeshSmooth.h"

namespace Urho3D
{
	static void RegisterMeshSmooth(asIScriptEngine* engine)
	{
		RegisterComponent<MeshSmooth>(engine, "MeshSmooth");
		engine->RegisterObjectMethod("MeshSmooth", "void SmoothMesh()", asMETHOD(MeshSmooth, SmoothMesh), asCALL_THISCALL);
	}

	void RegisterGeometryAPI(asIScriptEngine* engine)
	{
		RegisterMeshSmooth(engine);
	}
}
[/code]

And I've hooked up the RegisterGeometryAPI with the rest of them in ScriptAPI.h. The whole things compiles fine and I've made sure that the new source files are included where the UrhoPlayer can see them (i.e. when editing the Urho lib directly, I'm editing the files in /Source/Urho, but the player depends on /my_build_tree/include/Urho3D).

In a simple script, I call

[code]
    //test new script component
    Node@ testNode = editorScene.CreateChild("Test");
    MeshSmooth@ test = testNode.CreateComponent("MeshSmooth");
[/code]

This throws the error: "MeshSmooth is not a Data Type". So clearly, the player is not registering my new component - but I'm at a loss as to why. Any thoughts?

***EDIT*** I modifed Script.cpp so that the lib actually calls RegisterGeometryAPI. Now, I don't get the error above, but I still can't add the component to a game object (or call any of the component's methods).

-------------------------

weitjong | 2017-01-02 01:05:40 UTC | #9

Ah my bad. I should have drunk my morning coffee first before reading the forums.  :wink: 

What you have just explained makes perfect sense to me now. This is the limitation of our build system currently. It is a common limitation I suppose for CMake. The generated project in the build tree "knows" when and what to build based on the timestamp of the dependencies. When new source files are added later into the source tree, there is nothing depends on those newly added source files in the build tree yet, so CMake build rules does not get triggered to reconfigure the build tree automatically. And when the reconfiguration does not happen, then your new source files do not get the same (magic) treatment that makes them "just work". The solution is easy though. When you add new source files, reconfigure the generated project in the build tree manually by invoking cmake_xxxx.bat that you last used one more time. Note that Including the "Precompiled.h" manually happens to work for this particular case, but I am sure the new source files are still being configured differently than the rest of the source files and you want to avoid that.

Regarding your AngelScript API binding issue. I cannot see any problem with the code you have posted so far. Perhaps it is related to the above. I suggest you to reconfigure the project in the build tree first before debugging the AS binding issue.

-------------------------

friesencr | 2017-01-02 01:05:40 UTC | #10

I don't know what I am talking about but would defining a default for URHO3D_API and redefining it in the pch header solve this problem?

-------------------------

weitjong | 2017-01-02 01:05:40 UTC | #11

[quote="friesencr"]I don't know what I am talking about but would defining a default for URHO3D_API and redefining it in the pch header solve this problem?[/quote]
I am not sure I understand your statement. What I am sure though, in general compiler does not like symbol redefinition and also all the defines must remain the same between the time PCH get compiled and the time it get used. In any case, the root cause of the problem is not really the missing URHO3D_API define or the PCH not get force-included in the compiler flags for the new source files. These are just the manifested symptoms of new source files not being configured correctly in the build tree. IMHO, to solve these types of problems permanently then we have to address the root cause by creating smarter build rules to watch the source tree for new source files and trigger the reconfiguration automatically. At the moment the rule only get triggered when any of the CMakeLists.txt in the source tree get modified.

Not directly related to this. I am working on another refactoring work to make our project to play nice within JetBrains's CLion IDE. One of the plan item is to modify all the source files to have the "Precompiled.h" included twice. One in the compiler force-include flag and one in the source file itself. The header will have include guards obviously. The idea is to make our project build-able with or without PCH enabled. At the moment although CLion builds our project just fine (thanks to CMake generated build tree) with PCH enabled , the CLion's indexer trips over on the PCH. It only "sees" the symbols being included directly in the source files.

-------------------------

godan | 2017-01-02 01:05:41 UTC | #12

Nice! So rebuilding the CMake generated build tree does the trick. 

However, I'm still unable to bind my new component to the script engine. Anglescript logs the error "Could not create unknown component of type"

[img]https://dl.dropboxusercontent.com/u/69779082/urho_issue_2.PNG[/img]

Is there some binding magic that I'm missing?

-------------------------

friesencr | 2017-01-02 01:05:41 UTC | #13

You need to register your component in the engine / subsystem.  Defining the method doesn't call it.  That is still manual.

-------------------------

godan | 2017-01-02 01:05:41 UTC | #14

K, got it!

The last piece of the puzzle is (as was said above) to register the component, or library, or subsystem with the engine. This happens in Engine.cpp (somewhere after line 111) during instantiation. Who would have thought :smiley: ?

Gonna make everything in sight scriptable now :slight_smile:.

-------------------------

