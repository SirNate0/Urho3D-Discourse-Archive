UrhoIsTheBest | 2020-07-13 04:03:14 UTC | #1

I've been trying to implement [CDLOD Terrain Algorithm](https://github.com/fstrugar/CDLOD/blob/master/cdlod_paper_latest.pdf) in Urho3D engine.

I finished the QuadTree and LOD node selection part, and it works as expected.
I created a single grid mesh of fixed dimensions and set it into vertex buffer.
![image|673x500](upload://waIiyrD5dJlFfaBihxMPgU5RKMY.png) 

The next step is to "duplicate" this grid mesh vertices in vertex shader, scale and translate it to fill all the square areas.
**Now I have some difficulties in understanding how to do that in Urho3D.**

I guess I should use [Instancing](https://learnopengl.com/Advanced-OpenGL/Instancing) for such task. For example, I can add ```scale``` and ```translation``` variables in ```vertex shader```.
```
uniform vec3 translation;
uniform float scale;
...
// then in main()
WorldPosition = scale*position + translation;
float height = getHeight(WorldPosition.xz);
...
```
Then set those two variables differently for each of the square terrain area (as each separate instance).

But I am not sure how to implement it in Urho3D framework. For example, I noticed there is ```Graphics::DrawInstanced()``` method using the instancing technique I mentioned, and that function is called by ```BatchGroup::Draw()```. I also noticed there is ```instancingData_``` for ```Batch``` class. But I don't see examples using similar things.
 
*BTW: I checked Samples and found ```20_HugeObjectCount``` is using ```StaticModelGroup``` and clone lots of static model for similar things. But I guess that's probably not what I want.*

Any help or sample code I could follow?

-------------------------

extobias | 2020-07-13 12:15:34 UTC | #2

Hi urho, this steps allow me to use instance rendering and pass data to each instance.
First setup the renderer 
>     Renderer* renderer = GetSubsystem<Renderer>();
>     renderer->SetNumExtraInstancingBufferElements(1);
>     renderer->SetMinInstances(1);
    
Inherit from Drawable (here you create the vertex/index buffers) and set

>     batches_[0].geometryType_ = GEOM_INSTANCED;

Override UpdateBatches and set instance data
>     unsigned offset = 0;
>     unsigned char* instanceData = static_cast<unsigned char*>(batches_[0].instancingData_);
>     for(unsigned i = 0; i < numWorldTransforms_; i++)
>     {
>         // transform
>         Matrix3x4 transform(Matrix3x4::IDENTITY);
>         transform.SetTranslation(*worldTransform * vertexOffset_[i]);
>         worldTransforms_[i] = transform;
> 
>         // color is passed as instanced
>         memcpy(instanceData + offset, color.ToVector4().Data(), sizeof(Vector4));
>         offset += sizeof(Vector4);
>     }
    
Add your atribute to (here is iTexCoord7) CoreData/Shaders/GLSL/Transform.glsl
>     #ifdef INSTANCED
>     attribute vec4 iTexCoord4;
>     attribute vec4 iTexCoord5;
>     attribute vec4 iTexCoord6;
>     attribute vec4 iTexCoord7;
>     #endif
    
Finally had to make some modification to Batch.h, without this the same value
is passed to all instances
>     void AddTransforms(const Batch& batch)
>     {
>         InstanceData newInstance;
>         newInstance.distance_ = batch.distance_;
> 
>         unsigned char* buffer = static_cast<unsigned char*>(batch.instancingData_);
>         if(!buffer)
>         {
>             newInstance.instancingData_ = batch.instancingData_;
>         }
> 
>         for (unsigned i = 0; i < batch.numWorldTransforms_; ++i)
>         {
>             newInstance.worldTransform_ = &batch.worldTransform_[i];
>             if(buffer)
>             {
>                 newInstance.instancingData_ = buffer + sizeof(Vector4) * i;
>             }
> 
>             instances_.Push(newInstance);
>         }
>     }

-------------------------

coldev | 2020-07-13 13:46:42 UTC | #3

no mans sky URHO :star_struck:

-------------------------

UrhoIsTheBest | 2020-07-17 23:45:12 UTC | #4

Thanks extobias!

Generally, your solution makes sense to me. It looks similar to [Defining extra instancing data](https://urho3d.github.io/documentation/HEAD/_rendering.html) section in the Urho3D documentation.

Although I haven't figured out all the details for this implementation, which I could ask you later. *(I am having some difficulties so I may need to look at all code for a fully running example.)*

On the other hand, **I feel there should be a simpler solution for my particular question. Because I don't need extra instance data, all I need is a different world_transform for each piece of terrain square.** 
For example, I believe all I need is just to set the correct ```batch[0].worldTransform_[i]``` for ```terrain[i]```, and set ```batch.numWorldTransform_ = total number of terrains```. This should be very similar to how ```StaticModelGroup``` is used in ```20_HugeObjectCount``` example.

I tried the following method:
First set the vertex buffer for a single geometry as before
```
  batches_[0].geometry_ = geometry_;
  batches_[0].geometryType_ = GEOM_INSTANCED;

  ...  // calculate vertex buffer and index buffer...

  geometry_->SetIndexBuffer(indexBuffer_);
  geometry_->SetVertexBuffer(0, vertexBuffer_);
  geometry_->SetDrawRange(TRIANGLE_LIST, 0, indices.Size(), 0, total_vertices);

  vertexBuffer_->Unlock();
  vertexBuffer_->ClearDataLost();
```
Then set basic material for ```batches_[0]```. I assume I only need just one ```batch``` with many ```worldTransforms_```.
```
  auto *cache = GetSubsystem<ResourceCache>();
  batches_[0].material_ = (cache->GetResource<Material>("Materials/CdlodTerrain.xml"));
  batches_[0].material_->SetCullMode(CullMode::CULL_NONE);
  
  // Testing, just manually add several world_transforms_.
  world_transforms_  = {
      Matrix3x4(Vector3(0, 0, 0), Quaternion::IDENTITY, 1.f),
      Matrix3x4(Vector3(0, 0, 50 * kLengthPerPixel), Quaternion::IDENTITY, 1.f),
      Matrix3x4(Vector3(50 * kLengthPerPixel, 0, 0), Quaternion::IDENTITY, 1.f),
      Matrix3x4(Vector3(50 * kLengthPerPixel, 0, 50 * kLengthPerPixel), Quaternion::IDENTITY, 2.f),
  };
  batches_[0].numWorldTransforms_ = world_transforms_.Size();
  batches_[0].worldTransform_ = &world_transforms_[0];
```  
Finally override the ```UpdateBatches()``` function to empty to avoid override ```batches_[0].worldTransform_```.

But this is not working for me. I can still only see one piece of mesh grids.

I was following the example in ```StaticModelGroup``` and ```20_HugeObjectCount```. The key point there I noticed, is to have a vector of different ```worldTransform_```. But I could not figure how those ```worldTransform_``` data is passed to shader to render multiple object with same material but only different positions.


*Nit: I only started to learn all the 3D rendering pipeline very recently so it's still hard for me to understand the low level Urho3D code without enough examples and documentation.*

-------------------------

QBkGames | 2020-07-18 00:57:30 UTC | #5

For this scenario, if the grid is being generated every frame, instancing may not be the best (performance) option, since you have to send to the graphics device a large number of matrices every frame.
I think a better way (both in terms of performance but also simplicity) would be to generate the vertices you need for each square area based on the height field and grid spacing (avoiding if possible any matrix operations at all) all in one dynamic/custom mesh on the CPU and then upload the vertex data to the CPU.

-------------------------

UrhoIsTheBest | 2020-07-18 01:41:33 UTC | #6

The mesh grid is only generated once and uploaded to GPU, with a planar structure.
It's identical for all terrain pieces, only with different scale (2^n) and translation.
The height data is obtained during vertex shader stage and applied with vertex displacement.
That's the key for CDLOD to render huge terrain in real time.

All the code above I mentioned, is only run for once, not per frame.
Only the scale and translation data is calculated per frame, which is minimal (only Matrix3x4).

A simplified pseudo code is:
```
void Initialize() {
  // calculate vertex buffer, index buffer
  // assign to geometry and upload to GPU
}

void UpdatePerFrame() {
  SelectLodForEachTerrainNodeFromQuadTree();
  // Then pass the "scale" and "translation" variables for each terrain node to GPU.
  // GPU uses instancing to render each terrain with given initial vertex structure and "scale" & "translation".
}
```

-------------------------

UrhoIsTheBest | 2020-07-18 01:36:34 UTC | #7

BTW, I am getting things working by simply using a custom version ```StaticModelGroup``` for a quick demo test. I am going to dig deeper following this path.

![image|673x500](upload://lVv31yp6YlafUwk4KPH1AueYE13.png)

-------------------------

UrhoIsTheBest | 2020-07-18 08:17:55 UTC | #8

I roughly got it work.
I am using exactly the same method I mentioned [above](https://discourse.urho3d.io/t/instancing-rendering-in-urho3d/6260/4?u=urho).
I have no idea why it did not work in the first place.

There are total 7 LOD levels, box colored by: red -> green -> blue -> yellow -> magenta -> cyan -> red.
Roughly ~70 FPS on my 2014 MacBook (the fps in the screenshot is lower due to switch to other application for the screenshot).

I applied a simple vertex color according to the height.

The next step is to do the morphing between different LOD neighbors.

![image|680x500](upload://zDr0hljpzcaUHD5DjvhSHiKFGnU.png) 

![image|677x500](upload://fyL3uEKa0FEChrf9SbkXaQiDh9i.png) 

![image|679x500](upload://rJGVpjBAKDOdn8TJmFgIjg8cnTx.png) 

![image|677x500](upload://hA3IhviOM0HxoZXxf11pKyR5fuk.png)

-------------------------

QBkGames | 2020-07-19 02:12:35 UTC | #9

Sorry, I should have read the article and understood better what you are trying to do before jumping in with (the possibly wrong) advice :slight_smile:. 

However, I did do some investigation into how instancing works (in general, not Urho specific) and I was broken hearted :broken_heart: to discover that instancing is not the silver bullet solution to all my rendering problems as I naively thought, and in fact, it only improves performance in only some (rather rare) circumstance and in the wrong circumstance it can actually make rendering slower.

I'm interested in your terrain rendering algorithm (though I don't have much time for it now, but plan to look at it later), how do you calculate the vertex normals, also in the shader? (Or do you not need normals for your specific game right now?)

-------------------------

UrhoIsTheBest | 2020-07-19 03:47:18 UTC | #10

No worry :slight_smile:

Just wondering, what kind of rendering problem are you trying to solve that could not be improved by instancing?
For my terrain problem, it's working great as those papers demonstrated. From my limited understanding, if there are lots of meshes that use the same vertex structure, vertex order, index buffer, etc, but only have small difference. Then it could be improved by instancing. Though I don't know how much improvement it has compared to batching all geometry in a single draw call. I believe you've done enough research or someone with more knowledge could understand all these questions.

As for my vertex normals, that would be the next question for me after morphing is done. I'd happy to try to do it in the shader first. Partly because I'd like to see things on-the-fly without degrading performance, since it would be more flexible for later changes; Also I'd like to educate myself with such an example. I am not an expert on 3D rendering but found it's super interesting so I started to learn it through my project recently.
But I am not super worried about the normal map itself, since I can always pre-compute it and store it in the GPU as the texture. It's just a tradeoff between memory and real time latency.
However, I do vision lots of similar questions waiting ahead. For example, 
- What if I want to procedurally generate more detailed terrain for a small area? e.g. from the strategy map to combat map.
- What if I want procedurally generated vegetation? according to a rough (low resolution Google vegetation map). Also what about those trees, flowers, etc.

I read some posts and game dev slides about those fancy open world implementation. It's not practical for a personal project like mine. But I would like to explore the power of procedurally generation for most everything.

-------------------------

