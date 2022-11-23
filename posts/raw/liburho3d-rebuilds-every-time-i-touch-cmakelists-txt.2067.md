TheComet | 2017-01-02 01:12:46 UTC | #1

Whenever I add or remove source files, I have to re-run CMake in order for those new files to be detected (or old files to be removed).

Why does the entire library get rebuilt though? This is kind of annoying. Can it be fixed?

-------------------------

weitjong | 2017-01-02 01:12:46 UTC | #2

It should not happen when you are using symlink or mklink (if your host system is Windows). Without the symlink/mklink, our build system would fallback to hard copying of the header files from source tree to build tree (whenever they are not identical) EACH time CMake rerun itself and as part of the post-build process of the relevant libraries when they get built. This would not only slow down your build unnecessarily but also is susceptible to problem you described. When wrongly configured, the build system could actually fallback to use directory copying without file comparison check. If that happens then the header's timestamp got changed and a rebuild is ensured (each time make checks it will see itself needs to be rebuilt). In fact we have had one such report in our issue tracker recently and the problem has been fixed in the master branch. Having said that, as our code keeps changing and we have more than one devs contributing the changes, the same problem may reoccur again. The only way to get a way from this potential problem is not to use this fallback approach by setting up mklink privilege correctly on your Windows host system (symlink can be taken for granted on all *nix).

-------------------------

TheComet | 2017-01-02 01:12:46 UTC | #3

Ah, I forgot to mention I'm on a linux host. 4.4.6-gentoo x86_64. I am up to date with the current master branch as of this post.

-------------------------

weitjong | 2017-01-02 01:12:46 UTC | #4

You don't say. In that case the fall back copying is not your issue. It then really depends on how you structure your modified version of Urho3D project. In general if you change the source code then the encompassing target library need to be rebuilt. Are you adding new source files into existing Urho3D target? If not then libUrho3D shouldn't be rebuilt. I am not in front of my workstation now, but I am quite sure a CMake rerun won't cause an unnecessary rebuild on my system.

-------------------------

TheComet | 2017-01-02 01:12:46 UTC | #5

[quote="weitjong"]You don't say. In that case the fall back copying is not your issue. It then really depends on how you structure your modified version of Urho3D project. In general if you change the source code then the encompassing target library need to be rebuilt. Are you adding new source files into existing Urho3D target? If not then libUrho3D shouldn't be rebuilt. I am not in front of my workstation now, but I am quite sure a CMake rerun won't cause an unnecessary rebuild on my system.[/quote]

Indeed I am adding new files to the Urho3D target.

I created a new subfolder under [color=#000080]Source/Urho3D/IK[/color] in which I placed various source and header files. I then edited [color=#000080]Source/Urho3D/CMakeLists.txt[/color] and added a new flag, URHO3D_IK:

[code]if (NOT URHO3D_IK)
    list (APPEND EXCLUDED_SOURCE_DIRS IK)
endif ()[/code]

Now whenever I add new source files to [color=#000080]Source/Urho3D/IK/[/color] I have to touch [color=#000080]Source/Urho3D/CMakeLists.txt[/color], which causes the entire libUrho3D target to rebuild.

Perhaps this is the intended behaviour, but what I expected was for only the new files to be compiled. In the case of removing files, it should only cause libUrho3D to be linked again. Is this expectation wrong?

-------------------------

weitjong | 2017-01-02 01:12:47 UTC | #6

The linker or ar should regenerate the lib in any case but of course the compiler should not recompile the compilation units unnecessarily. Again not unless you have reconfigured the project wrongly. Say, you have created an all encompassing header file and that header file is being referenced all over the places, and that header file is regenerated at each CMake rerun. Now, I am not saying this is your case, just cite an example where you can shoot yourself in the foot.

-------------------------

TheComet | 2017-01-02 01:12:47 UTC | #7

So I tested the following things. Simply touching [color=#000080]Source/Urho3D/CMakeLists.txt[/color] and running make does [b]not[/b] cause a rebuild.

If I add a new file [color=#000080]Source/Urho3D/IK/Test.cpp[/color] containing this code:
[code]void foo()
{
}[/code]

If I then touch CMakeLists.txt and run make, it rebuilds everything. This is my output:
[code]$ make -j5
-- Could NOT find Esound development library (missing:  ESOUND_LIBRARIES ESOUND_INCLUDE_DIRS) 
-- Could NOT find aRts development library (missing:  ARTS_LIBRARIES ARTS_INCLUDE_DIRS) 
-- Could NOT find NetworkAudioSystem development library (missing:  NAS_LIBRARIES NAS_INCLUDE_DIRS) 
-- Could NOT find RoarAudio development library (missing:  SNDIO_LIBRARIES SNDIO_INCLUDE_DIRS) 
-- Could NOT find Mir display server (missing:  MIR_CLIENT MIR_COMMON MIR_CLIENT_INCLUDE_DIR MIR_COMMON_INCLUDE_DIR) 
-- Could NOT find Wayland display server (missing:  WAYLAND_CLIENT WAYLAND_CURSOR WAYLAND_EGL WAYLAND_INCLUDE_DIRS) 
-- Configuring done
-- Generating done
-- Build files have been written to: /home/thecomet/documents/programming/cpp/Urho3D/build-debug
[  1%] Built target JO
[  1%] Built target rapidjson
[  1%] Built target PugiXml
[  1%] Built target StanHull
[  1%] Built target LZ4
[  1%] Built target STB
[  5%] Built target FreeType
[  5%] Built target Civetweb
[  8%] Built target Lua
[  9%] Built target toluapp
[ 12%] Built target AngelScript
[ 13%] Built target Detour
[ 15%] Built target kNet
[ 16%] Built target DetourCrowd
[ 16%] Built target DetourTileCache
[ 17%] Built target Recast
[ 17%] Built target GLEW
[ 18%] Built target LibCpuId
[ 29%] Built target SDL
[ 34%] Built target Box2D
[ 35%] Built target tolua++
[ 35%] Built target lua_interpreter
[ 35%] Built target luac
[ 50%] Built target Bullet
Scanning dependencies of target Urho3D
[ 50%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LuaScript/LuaScriptEventInvoker.cpp.o
[ 50%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LuaScript/LuaScript.cpp.o
[ 50%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LuaScript/LuaScriptInstance.cpp.o
[ 50%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LuaScript/LuaFile.cpp.o
[ 50%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LuaScript/LuaFunction.cpp.o
[ 50%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LuaScript/ToluaUtils.cpp.o
[ 50%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/CheckBox.cpp.o
[ 50%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/UI.cpp.o
[ 50%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/FontFaceBitmap.cpp.o
[ 51%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/Button.cpp.o
[ 51%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/LineEdit.cpp.o
[ 51%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/MessageBox.cpp.o
[ 51%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/DropDownList.cpp.o
[ 51%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/Sprite.cpp.o
[ 51%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/FileSelector.cpp.o
[ 51%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/Slider.cpp.o
[ 51%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/Window.cpp.o
[ 51%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/ToolTip.cpp.o
[ 52%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/Text3D.cpp.o
[ 52%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/UIElement.cpp.o
[ 52%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/ScrollView.cpp.o
[ 52%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/View3D.cpp.o
[ 52%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/ListView.cpp.o
[ 52%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/ScrollBar.cpp.o
[ 52%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/FontFace.cpp.o
[ 52%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/UIBatch.cpp.o
[ 52%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/Font.cpp.o
[ 52%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/Menu.cpp.o
[ 53%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/Cursor.cpp.o
[ 53%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/BorderImage.cpp.o
[ 53%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/FontFaceFreeType.cpp.o
[ 53%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/UI/Text.cpp.o
[ 53%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/IO/Deserializer.cpp.o
[ 53%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/IO/FileSystem.cpp.o
[ 53%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/IO/VectorBuffer.cpp.o
[ 53%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/IO/NamedPipe.cpp.o
[ 53%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/IO/Serializer.cpp.o
[ 53%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/IO/Log.cpp.o
[ 54%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/IO/MemoryBuffer.cpp.o
[ 54%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/IO/Compression.cpp.o
[ 54%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/IO/PackageFile.cpp.o
[ 54%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/IO/File.cpp.o
[ 54%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/IO/FileWatcher.cpp.o
[ 54%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LibraryInfo.cpp.o
[ 54%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Input/Input.cpp.o
[ 54%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Input/Controls.cpp.o
[ 54%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/ConstraintWeld2D.cpp.o
[ 54%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/Sprite2D.cpp.o
[ 55%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/Drawable2D.cpp.o
[ 55%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/SpriterInstance2D.cpp.o
[ 55%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/StaticSprite2D.cpp.o
[ 55%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/ConstraintRevolute2D.cpp.o
[ 55%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/ConstraintPulley2D.cpp.o
[ 55%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/ConstraintDistance2D.cpp.o
[ 55%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/ParticleEmitter2D.cpp.o
[ 55%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/PhysicsWorld2D.cpp.o
[ 55%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/CollisionBox2D.cpp.o
[ 56%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/TileMapDefs2D.cpp.o
[ 56%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/Urho2D.cpp.o
[ 56%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/ConstraintMouse2D.cpp.o
[ 56%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/CollisionCircle2D.cpp.o
[ 56%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/Constraint2D.cpp.o
[ 56%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/RigidBody2D.cpp.o
[ 56%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/CollisionChain2D.cpp.o
[ 56%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/SpriterData2D.cpp.o
[ 56%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/ConstraintFriction2D.cpp.o
[ 56%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/TmxFile2D.cpp.o
[ 57%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/TileMap2D.cpp.o
[ 57%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/ConstraintMotor2D.cpp.o
[ 57%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/ConstraintRope2D.cpp.o
[ 57%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/CollisionPolygon2D.cpp.o
[ 57%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/TileMapLayer2D.cpp.o
[ 57%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/ConstraintPrismatic2D.cpp.o
[ 57%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/CollisionEdge2D.cpp.o
[ 57%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/Renderer2D.cpp.o
[ 57%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/AnimatedSprite2D.cpp.o
[ 57%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/ConstraintGear2D.cpp.o
[ 58%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/CollisionShape2D.cpp.o
[ 58%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/ConstraintWheel2D.cpp.o
[ 58%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/AnimationSet2D.cpp.o
[ 58%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/SpriteSheet2D.cpp.o
[ 58%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Urho2D/ParticleEffect2D.cpp.o
[ 58%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Engine/Console.cpp.o
[ 58%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Engine/Engine.cpp.o
[ 58%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Engine/DebugHud.cpp.o
[ 58%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Engine/Application.cpp.o
[ 58%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/MathAPI.cpp.o
[ 59%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/IOAPI.cpp.o
[ 59%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/Addons.cpp.o
[ 59%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/GraphicsAPI.cpp.o
[ 59%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/NavigationAPI.cpp.o
[ 59%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/ScriptAPIDump.cpp.o
[ 59%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/ResourceAPI.cpp.o
[ 59%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/PhysicsAPI.cpp.o
[ 59%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/AudioAPI.cpp.o
[ 59%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/SceneAPI.cpp.o
[ 59%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/ScriptFile.cpp.o
[ 60%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/EngineAPI.cpp.o
[ 60%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/Urho2DAPI.cpp.o
[ 60%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/ScriptInstance.cpp.o
[ 60%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/ScriptAPI.cpp.o
[ 60%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/Script.cpp.o
[ 60%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/CoreAPI.cpp.o
[ 60%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/UIAPI.cpp.o
[ 60%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/NetworkAPI.cpp.o
[ 60%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/InputAPI.cpp.o
[ 61%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/DatabaseAPI.cpp.o
[ 61%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Container/Allocator.cpp.o
[ 61%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Container/HashBase.cpp.o
[ 61%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Container/Str.cpp.o
[ 61%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Container/Swap.cpp.o
[ 61%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Container/VectorBase.cpp.o
[ 61%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Container/RefCounted.cpp.o
[ 61%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Core/Thread.cpp.o
[ 61%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Core/Spline.cpp.o
[ 61%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Core/ProcessUtils.cpp.o
[ 62%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Core/StringUtils.cpp.o
[ 62%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Core/MiniDump.cpp.o
[ 62%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Core/Context.cpp.o
[ 62%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Core/Object.cpp.o
[ 62%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Core/Timer.cpp.o
[ 62%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Core/EventProfiler.cpp.o
[ 62%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Core/Condition.cpp.o
[ 62%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Core/Variant.cpp.o
[ 62%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Core/Profiler.cpp.o
[ 62%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Core/Mutex.cpp.o
[ 63%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Core/WorkQueue.cpp.o
[ 63%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Skeleton.cpp.o
[ 63%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Octree.cpp.o
[ 63%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/AnimatedModel.cpp.o
[ 63%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/StaticModelGroup.cpp.o
[ 63%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/RenderPath.cpp.o
[ 63%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/ParticleEmitter.cpp.o
[ 63%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/AnimationState.cpp.o
[ 63%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Shader.cpp.o
[ 63%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Tangent.cpp.o
[ 64%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/AnimationController.cpp.o
[ 64%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/GraphicsDefs.cpp.o
[ 64%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Model.cpp.o
[ 64%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/OcclusionBuffer.cpp.o
[ 64%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Zone.cpp.o
[ 64%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/TerrainPatch.cpp.o
[ 64%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/ParticleEffect.cpp.o
[ 64%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/OctreeQuery.cpp.o
[ 64%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/ShaderPrecache.cpp.o
[ 65%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Renderer.cpp.o
[ 65%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Drawable.cpp.o
[ 65%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/DebugRenderer.cpp.o
[ 65%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Skybox.cpp.o
[ 65%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Batch.cpp.o
[ 65%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Terrain.cpp.o
[ 65%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Viewport.cpp.o
[ 65%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Light.cpp.o
[ 65%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Camera.cpp.o
[ 65%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/CustomGeometry.cpp.o
[ 66%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Geometry.cpp.o
[ 66%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/OpenGL/OGLGraphics.cpp.o
[ 66%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/OpenGL/OGLTexture3D.cpp.o
[ 66%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/OpenGL/OGLIndexBuffer.cpp.o
[ 66%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/OpenGL/OGLTexture2DArray.cpp.o
[ 66%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/OpenGL/OGLTextureCube.cpp.o
[ 66%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/OpenGL/OGLShaderVariation.cpp.o
[ 66%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/OpenGL/OGLTexture.cpp.o
[ 66%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/OpenGL/OGLGraphicsImpl.cpp.o
[ 66%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/OpenGL/OGLRenderSurface.cpp.o
[ 67%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/OpenGL/OGLTexture2D.cpp.o
[ 67%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/OpenGL/OGLShaderProgram.cpp.o
[ 67%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/OpenGL/OGLVertexBuffer.cpp.o
[ 67%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/OpenGL/OGLGPUObject.cpp.o
[ 67%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/OpenGL/OGLConstantBuffer.cpp.o
[ 67%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/DecalSet.cpp.o
[ 67%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/BillboardSet.cpp.o
[ 67%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Material.cpp.o
[ 67%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Technique.cpp.o
[ 67%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Animation.cpp.o
[ 68%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/StaticModel.cpp.o
[ 68%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/View.cpp.o
[ 68%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Physics/RigidBody.cpp.o
[ 68%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Physics/CollisionShape.cpp.o
[ 68%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Physics/Constraint.cpp.o
[ 68%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Physics/PhysicsWorld.cpp.o
[ 68%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Network/Connection.cpp.o
[ 68%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Network/HttpRequest.cpp.o
[ 68%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Network/NetworkPriority.cpp.o
[ 69%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Network/Network.cpp.o
[ 69%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Resource/JSONValue.cpp.o
[ 69%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Resource/JSONFile.cpp.o
[ 69%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Resource/ResourceCache.cpp.o
[ 69%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Resource/PListFile.cpp.o
[ 69%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Resource/Resource.cpp.o
[ 69%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Resource/Localization.cpp.o
[ 69%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Resource/Decompress.cpp.o
[ 69%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Resource/XMLFile.cpp.o
[ 69%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Resource/Image.cpp.o
[ 70%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Resource/BackgroundLoader.cpp.o
[ 70%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Resource/XMLElement.cpp.o
[ 70%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Scene/SceneResolver.cpp.o
[ 70%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Scene/ValueAnimation.cpp.o
[ 70%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Scene/Animatable.cpp.o
[ 70%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Scene/Node.cpp.o
[ 70%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Scene/SmoothedTransform.cpp.o
[ 70%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Scene/Scene.cpp.o
[ 70%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Scene/Component.cpp.o
[ 70%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Scene/SplinePath.cpp.o
[ 71%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Scene/Serializable.cpp.o
[ 71%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Scene/ValueAnimationInfo.cpp.o
[ 71%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Scene/UnknownComponent.cpp.o
[ 71%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Scene/LogicComponent.cpp.o
[ 71%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Scene/ObjectAnimation.cpp.o
[ 71%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Navigation/NavigationMesh.cpp.o
[ 71%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Navigation/Obstacle.cpp.o
[ 71%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Navigation/NavArea.cpp.o
[ 71%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Navigation/CrowdAgent.cpp.o
[ 71%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Navigation/DynamicNavigationMesh.cpp.o
[ 72%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Navigation/Navigable.cpp.o
[ 72%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Navigation/CrowdManager.cpp.o
[ 72%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Navigation/NavBuildData.cpp.o
[ 72%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Navigation/OffMeshConnection.cpp.o
[ 72%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Math/Polyhedron.cpp.o
[ 72%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Math/Matrix3x4.cpp.o
[ 72%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Math/Quaternion.cpp.o
[ 72%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Math/Sphere.cpp.o
[ 72%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Math/Frustum.cpp.o
[ 72%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Math/StringHash.cpp.o
[ 73%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Math/AreaAllocator.cpp.o
[ 73%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Math/Matrix2.cpp.o
[ 73%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Math/Random.cpp.o
[ 73%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Math/Color.cpp.o
[ 73%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Math/Matrix4.cpp.o
[ 73%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Math/MathDefs.cpp.o
[ 73%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Math/Rect.cpp.o
[ 73%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Math/BoundingBox.cpp.o
[ 73%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Math/Vector4.cpp.o
[ 74%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Math/Vector2.cpp.o
[ 74%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Math/Vector3.cpp.o
[ 74%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Math/Matrix3.cpp.o
[ 74%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Math/Plane.cpp.o
[ 74%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Math/Ray.cpp.o
[ 74%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Audio/Sound.cpp.o
[ 74%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Audio/SoundSource.cpp.o
[ 74%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Audio/OggVorbisSoundStream.cpp.o
[ 74%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Audio/SoundSource3D.cpp.o
[ 74%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Audio/SoundListener.cpp.o
[ 75%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Audio/BufferedSoundStream.cpp.o
[ 75%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Audio/SoundStream.cpp.o
[ 75%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Audio/Audio.cpp.o
[ 75%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/IK/FABRIKSolver.cpp.o
[ 75%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/IK/IKRoot.cpp.o
[ 75%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/IK/IK.cpp.o
[ 75%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/IK/IKEffector.cpp.o
[ 75%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/IK/JacobianTransposeIKSolver.cpp.o
[ 75%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/IK/Test.cpp.o
[ 75%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/IK/JacobianInverseIKSolver.cpp.o
[ 76%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/IK/IKConstraint.cpp.o
[ 76%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LuaScript/generated/UILuaAPI.cpp.o
[ 76%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LuaScript/generated/Urho2DLuaAPI.cpp.o
[ 76%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LuaScript/generated/IOLuaAPI.cpp.o
[ 76%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LuaScript/generated/ResourceLuaAPI.cpp.o
[ 76%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LuaScript/generated/GraphicsLuaAPI.cpp.o
[ 76%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LuaScript/generated/InputLuaAPI.cpp.o
[ 76%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LuaScript/generated/SceneLuaAPI.cpp.o
[ 76%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LuaScript/generated/AudioLuaAPI.cpp.o
[ 76%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LuaScript/generated/PhysicsLuaAPI.cpp.o
/home/thecomet/documents/programming/cpp/Urho3D/build-debug/Source/Urho3D/LuaScript/generated/AudioLuaAPI.cpp: In function ?int tolua_AudioLuaAPI_SoundSource_SetAutoRemove00(lua_State*)?:
/home/thecomet/documents/programming/cpp/Urho3D/build-debug/Source/Urho3D/LuaScript/generated/AudioLuaAPI.cpp:2332:29: warning: ?void Urho3D::SoundSource::SetAutoRemove(bool)? is deprecated (declared at /home/thecomet/documents/programming/cpp/Urho3D/Source/Urho3D/Audio/SoundSource.h:74) [-Wdeprecated-declarations]
   self->SetAutoRemove(enable);
                             ^
/home/thecomet/documents/programming/cpp/Urho3D/build-debug/Source/Urho3D/LuaScript/generated/AudioLuaAPI.cpp: In function ?int tolua_AudioLuaAPI_SoundSource_GetAutoRemove00(lua_State*)?:
/home/thecomet/documents/programming/cpp/Urho3D/build-debug/Source/Urho3D/LuaScript/generated/AudioLuaAPI.cpp:2587:48: warning: ?bool Urho3D::SoundSource::GetAutoRemove() const? is deprecated (declared at /home/thecomet/documents/programming/cpp/Urho3D/Source/Urho3D/Audio/SoundSource.h:103) [-Wdeprecated-declarations]
   bool tolua_ret = (bool)  self->GetAutoRemove();
                                                ^
/home/thecomet/documents/programming/cpp/Urho3D/build-debug/Source/Urho3D/LuaScript/generated/AudioLuaAPI.cpp: In function ?int tolua_get_SoundSource_autoRemove(lua_State*)?:
/home/thecomet/documents/programming/cpp/Urho3D/build-debug/Source/Urho3D/LuaScript/generated/AudioLuaAPI.cpp:2821:54: warning: ?bool Urho3D::SoundSource::GetAutoRemove() const? is deprecated (declared at /home/thecomet/documents/programming/cpp/Urho3D/Source/Urho3D/Audio/SoundSource.h:103) [-Wdeprecated-declarations]
  tolua_pushboolean(tolua_S,(bool)self->GetAutoRemove());
                                                      ^
/home/thecomet/documents/programming/cpp/Urho3D/build-debug/Source/Urho3D/LuaScript/generated/AudioLuaAPI.cpp: In function ?int tolua_set_SoundSource_autoRemove(lua_State*)?:
/home/thecomet/documents/programming/cpp/Urho3D/build-debug/Source/Urho3D/LuaScript/generated/AudioLuaAPI.cpp:2838:1: warning: ?void Urho3D::SoundSource::SetAutoRemove(bool)? is deprecated (declared at /home/thecomet/documents/programming/cpp/Urho3D/Source/Urho3D/Audio/SoundSource.h:74) [-Wdeprecated-declarations]
 )
 ^
[ 77%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LuaScript/generated/LuaScriptLuaAPI.cpp.o
[ 77%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LuaScript/generated/NavigationLuaAPI.cpp.o
[ 77%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LuaScript/generated/CoreLuaAPI.cpp.o
[ 77%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LuaScript/generated/MathLuaAPI.cpp.o
[ 77%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LuaScript/generated/EngineLuaAPI.cpp.o
[ 77%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LuaScript/generated/NetworkLuaAPI.cpp.o
[ 77%] Linking CXX shared library ../../lib/libUrho3D.so
../ThirdParty/Lua/libLua.a(loslib.c.o): In function `os_tmpname':
/home/thecomet/documents/programming/cpp/Urho3D/Source/ThirdParty/Lua/src/loslib.c:60: warning: the use of `tmpnam' is dangerous, better use `mkstemp'
[ 79%] Built target Urho3D
[ 79%] Linking CXX executable ../../../bin/tool/OgreImporter
[ 80%] Linking CXX executable ../../../bin/tool/RampGenerator
[ 80%] Linking CXX executable ../../../bin/Urho3DPlayer
[ 80%] Linking CXX executable ../../../bin/tool/PackageTool
[ 80%] Built target Urho3DPlayer
[ 80%] Linking CXX executable ../../../bin/tool/SpritePacker
[ 97%] Built target Assimp
[ 97%] Built target PackageTool
[ 97%] Built target RampGenerator
[ 97%] Built target OgreImporter
[ 97%] Linking CXX executable ../../../bin/tool/ScriptCompiler
[ 97%] Linking CXX executable ../../../bin/tool/AssetImporter
[ 98%] Built target SpritePacker
[ 98%] Built target ScriptCompiler
[100%] Built target AssetImporter
[/code]

Removing the file [color=#000080]Source/Urho3D/IK/Test.cpp[/color] and touching CMakeLists.txt and running make again produces the same output (minus building Test.cpp.o of course).

-------------------------

weitjong | 2017-01-02 01:12:47 UTC | #8

I am back to my workstation now. That the good news. The bad news is, it is reproducible on my system as well  :wink: 
It just that in my system I have ccache enabled, so the recompilation of all the existing source files took a fraction of a second to fetch the cache objects instead of actually recompiling them. So, I have not paying attention to it. Interesting.

-------------------------

weitjong | 2017-01-02 01:12:47 UTC | #9

I think I know why already. On one hand it is how CMake works when custom compiler flags per compilation unit is being used, so it is CMake/Makefile generator limitation. On the other hand, it is us who told CMake we need custom flags. When there is a new source files or deletion, the number of compilation units changes. This alone does not cause problem as the modified CMakefiles does not cause a rebuild in itself. However when the list of compilation units has custom compiler flags then the "flags.make" file is forced to be modified and that file alone is being referenced by all the compilation rules in the Makefile. So when it changes, all the rules get triggered. I will see whether we can do away with custom compiler flags. No promise.

-------------------------

weitjong | 2017-01-02 01:12:47 UTC | #10

I think I am able to make it so. The custom flags was used for PCH (precompiled header). It was using using custom flags per compilation unit because I wanted to be able to exclude compilation units that do not want to use PCH. However, this feature is not being used anymore. So we could just simply set the flags globally at the library target and avoid the problem all together. Will commit it soon to the master branch. Thanks for bringing this up.

-------------------------

TheComet | 2017-01-02 01:12:47 UTC | #11

No problem, look forward to the fix!

-------------------------

weitjong | 2017-01-02 01:12:47 UTC | #12

It is in.

-------------------------

TheComet | 2017-01-02 01:12:47 UTC | #13

Pulled and rebased, everything works as intended now. Thanks!

-------------------------

