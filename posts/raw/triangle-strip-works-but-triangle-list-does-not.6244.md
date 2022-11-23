UrhoIsTheBest | 2020-07-07 20:30:15 UTC | #1

So I've been trying to generate meshes.
I have a new class copied from ```CustomGeometry```.
I create a test function
```c++
void TestDrawable::DrawTestGeometry() {
  batches_.Clear();
  geometries_.Clear();
  primitiveTypes_.Clear();

  batches_.Resize(1);
  geometries_.Resize(1);
  primitiveTypes_.Resize(1);
  geometries_[0] = new Geometry(context_);
  batches_[0].geometry_ = geometries_[0];

  // Current geometry being updated.
  geometryIndex_ = 0;

  Vector<Vector3> position = {
      {0, 0, 0}, {0, 0, 1}, {0, 0, 2},
      {1, 0, 0}, {1, 0, 1}, {1, 0, 2},
      {2, 0, 0}, {2, 0, 1}, {2, 0, 2},
  };
  PODVector<unsigned short> indices{3, 1, 0, 3, 4, 1, 4, 2, 1, 4, 5, 2, 6, 4, 3, 6, 7, 4, 7, 5, 4, 7, 8, 5};

  vertexBuffer_->SetSize(position.Size(), MASK_POSITION);
  auto *dest = (float *) vertexBuffer_->Lock(0, position.Size(), true);
  for (int i = 0; i < position.Size(); ++i) {
    *dest++ = position[i].x_;
    *dest++ = position[i].y_;
    *dest++ = position[i].z_;
  }

  SharedPtr<IndexBuffer> indexBuffer_(new IndexBuffer(context_));
  indexBuffer_->SetSize(indices.Size(), false);
  indexBuffer_->SetData(&indices[0]);
  geometries_[0]->SetIndexBuffer(indexBuffer_);
  geometries_[0]->SetVertexBuffer(0, vertexBuffer_);
  geometries_[0]->SetDrawRange(PrimitiveType::TRIANGLE_LIST,
                               0,
                               indices.Size(),
                               0,
                               position.Size());
  vertexBuffer_->Unlock();
  vertexBuffer_->ClearDataLost();
}
```

However, this function draws nothing! 
![image|672x500](upload://xVPQFXnyiKKOmzJdzkCuCnMJSjr.png) 


When I just simply change the TRIANGLE_LIST to TRIANGLE_STRIPE, the drawing is what I want.
```
geometries_[0]->SetDrawRange(PrimitiveType:: TRIANGLE_STRIP,
                               0,
                               indices.Size(),
                               0,
                               position.Size());
```
![image|678x500](upload://1mD2SUWENP7Ojzh2iLokrojtIpw.png) 

**But this does not make any sense to me!**
The TRIANGLE_LIST should draw from the ```IndexBuffer``` while TRIANGLE_STRIP should have a specific order to draw the vertices.

What's wrong?

-------------------------

Eugene | 2020-07-07 20:26:09 UTC | #2

[quote="UrhoIsTheBest, post:1, topic:6244"]
What’s wrong?
[/quote]
Are you sure you have correct culling? Try disabling it in material.

-------------------------

UrhoIsTheBest | 2020-07-07 06:35:44 UTC | #3

The funny thing is: I don't have material set for the geometry at all. I removed all materials stuff in my custom new class. I only want to draw raw meshes, probably with vertex color later:
```
drawable->SetMaterial(cache->GetResource<Material>("Materials/VColUnlit.xml"));
```
So am I doing the wrong thing?
Does all geometry needs basic material setting?

Also, I know we need to update the ```BoundingBox``` to make the camera frustum detection. If we don't set that, the bounding box is simply (0,0,0)-(0,0,0), but that does not cause any problem if (0,0,0) is in the camera frustum. I tested it for the other case.

-------------------------

UrhoIsTheBest | 2020-07-07 06:55:11 UTC | #4

Oh! you are right. The default culling mode is CULL_CCW

When I added a material and set it to CULL_NONE in the code above. It works!
```
auto *cache = GetSubsystem<ResourceCache>();
batches_[0].material_ = (cache->GetResource<Material>("Materials/VColUnlit.xml"));
batches_[0].material_->SetCullMode(CullMode::CULL_NONE);
```

But why the other TRIANGLE_STRIPE works without setting material?

-------------------------

Eugene | 2020-07-07 07:05:40 UTC | #5

For stripe you have completely different triangles than for lists, and stripes follow different culling rules. So you have different result.

-------------------------

UrhoIsTheBest | 2020-07-07 07:24:59 UTC | #6

From my understanding, the [STRIPE](https://en.wikipedia.org/wiki/Triangle_strip) has totally different pre-defined order, e.g. (v0, v1, v2), (v2, v1, v3), (v2, v3, v4) and so on. If that's true, then the triangles mesh would be totally different.
e.g. same as:
```
PODVector<unsigned short> indices{0, 1, 2, 2, 1, 3, 2, 3, 4, 4, 3, 5, 4, 5, 6, 6, 5, 7, 6, 7, 8};
```

![image|690x479](upload://AoQr6zDJzODuxCumzCV1DcCFpMo.png)

-------------------------

UrhoIsTheBest | 2020-07-07 07:39:19 UTC | #7

I might understand why it works like this after several tests.

If we set the index buffer, then we are drawing TRIANGLE_LIST even we set STRIPE type. However, the culling mode will use the STRIPE one. So there is some inconsistency here (or default fallback). Maybe it's intended behavior which I am just not familiar with.

TRIANGLE_STRIPE drawing will only work when we do not explicitly set the index buffer.

Does that sounds correct?

This does not make sense to me when tracking down the source code to ```OGLGraphics.cpp```. But I don't have better explanation for those tests. I might miss something.

-------------------------

Eugene | 2020-07-07 07:47:00 UTC | #8

[quote="UrhoIsTheBest, post:7, topic:6244"]
However, the culling mode will use the STRIPE one.
[/quote]
Exact stripe/list culling algorithm is chosen by GPU basing on primitive type. Urho has no control over it. Urho can only choose whether to draw one side or both.

Although there may be some magic inside Urho that interferes with... something. Or maybe bug. I don’t feel like debugging right now, but it can be checked. What kind of primitive goes into glDrawElements when you draw stripes?

-------------------------

Modanung | 2020-07-07 16:37:17 UTC | #9

Could the typo be affecting the outcome? I guess that must be just forum spelling.

[spoiler]Strips are not stripes.[/spoiler]

-------------------------

UrhoIsTheBest | 2020-07-07 20:27:41 UTC | #10

Ah! I know why!

**Short Answer**
Everything works as expected, no bug or anything.

**Long Answer**
If we don't set index buffer for ```TRIANGLE_STRIP```. The drawing triangles will iterate from v0, v1, v2 ...
If we do set index buffer for ```TRIANGLE_STRIP```. The drawing triangles will iterate through the index defined in the index buffer.
So in our case, we set the index buffer
```
PODVector<unsigned short> indices{3, 1, 0, 3, 4, 1, 4, 2, 1, 4, 5, 2, 6, 4, 3, 6, 7, 4, 7, 5, 4, 7, 8, 5};
```
The triangles would be (3, 1, 0), (0, 1, 3), (0, 3, 4), (4, 3, 1).... total ```indices.Size() - 2``` triangles.

If we set a material and make sure culling mode is ```CULL_NONE```.
We can see the following draws:
![image|650x500](upload://zpWCAPNs4m65pINZf4dhEMbmu8g.png) 
Notice that lone line on the right side is from triangle (5, 2, 6), which is from the sequence in the index buffer.

**Then why do we see the correct triangles before?**
That's because we did not set the culling mode, so many of triangles shown above is counter direction, thus not rendered.
The remaining triangles look like exactly the same as result for ```TRIANGLE_LIST```. **THIS IS JUST COINCIDENCE!**

So @Eugene is right. The simple answer for my question is **culling mode**.
Although there are many other things I learned here.

-------------------------

UrhoIsTheBest | 2020-07-07 20:29:53 UTC | #11

LOL, I wish, only if compiler is broken :)
But I corrected the title and code in the question. Thanks for typo checking!

-------------------------

Modanung | 2020-07-10 10:43:40 UTC | #12

[quote="UrhoIsTheBest, post:11, topic:6244"]
[...] only if compiler is broken :slight_smile:
[/quote]

Yea, I quickly realized that too... but the ubiquity of the typo made me seriously consider it as a possibility for a moment. :slightly_smiling_face:

-------------------------

