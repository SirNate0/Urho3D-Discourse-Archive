sabotage3d | 2017-01-02 01:08:38 UTC | #1

Hi what would be the best way to add additional vertex attribute on a already loaded StaticModel? I need to add an index integer attribute, if it is not possible I will add UV2 and convert one of the components to integer. I had a look into these helpers: [github.com/urho3d/Urho3D/blob/m ... terUtils.h](https://github.com/urho3d/Urho3D/blob/master/Source/Tools/OgreImporter/OgreImporterUtils.h)  But I am not sure how to do it with already loaded StaticModel.

-------------------------

codingmonkey | 2017-01-02 01:08:38 UTC | #2

Hi, as far as i know the vertex attributes it's very solid construction and it very hard to do changes in it.
May be you mean uniform for vertex shader, and not attributes ?
Anyway you may try to use std layout as you wish.
MASK_TEXCOORD2 allow use additional 2 float if you don't need really texCoord2 within
MASK_BLENDINDICES - 4 integers, if you model are not using animation you may write to it some useful info for VS.

-------------------------

sabotage3d | 2017-01-02 01:08:38 UTC | #3

Hi I need to add additional UV2 to already existing geometry. I will need to access the vertex buffer and just append this attribute value. It needs to be outside of the shader using custom geometry.

-------------------------

cadaver | 2017-01-02 01:08:38 UTC | #4

It's not really recommended to do this at runtime, since it's a performance hit (rather you should have the data already in the model), but you can get the model's vertex buffer, lock it, copy the data to CPU, set new buffer vertex format with the added element, convert the vertex data to the new format, and push it back to the vertex buffer.

-------------------------

sabotage3d | 2017-01-02 01:08:38 UTC | #5

Thanks cadaver the idea is to add instance index to each duplicate of the same geometry. I am trying to do dynamic batching but without modifying the engine's code. After getting the vertex buffer how can I add index vertex attribute? I will also need to access this attribute in the shader.

-------------------------

cadaver | 2017-01-02 01:08:38 UTC | #6

OK, if it's for instancing (which is constantly changing data) you shouldn't go the route I explained.

Rather, check Urho's inbuilt instancing code in Batch.cpp. It does a bit dirty trick of modifying the Geometry being rendered on the fly. It adds a second vertex buffer alongside the model's own, which contains the instance transforms. Then, after instance rendering is done, the extra buffer is removed from Geometry.

-------------------------

sabotage3d | 2017-01-02 01:08:38 UTC | #7

On systems where instancing is not supported do I have to revert to duplicating the vertex buffer and adding the index attribute myself? Or is there a way to force the instancing? I had a look at Batch.cpp, but I can't fully understand it. How does it assume the instance index is it the index of the transform array?

-------------------------

cadaver | 2017-01-02 01:08:39 UTC | #8

The instancing has a fallback rendering mode where it doesn't add the second vertex buffer, but loops through the instances and updates the model matrix uniform per instance.

-------------------------

sabotage3d | 2017-01-02 01:08:39 UTC | #9

Basically I am trying to setup the instances manually. Like just duplicating the existing vertex buffer by the number of the instances and applying the transforms manually. Would it be slower if I just duplicate and merge the vertex buffer of all the instances and send it as single StaticModel and apply the transforms in the shader?

-------------------------

cadaver | 2017-01-02 01:08:39 UTC | #10

You will have to profile and see which way works better. I would imagine that if this is for the lego brick particle effect instancing, and you'll be working on mobile hardware, just (re)uploading the whole vertex buffer with all geometry baked in could in fact work better. Supposedly this is how Unity does its small object instancing.

-------------------------

sabotage3d | 2017-01-02 01:08:39 UTC | #11

Thanks cadaver. Yeah it is indeed for the lego/bricks explosion, but it could be used for debris and sparks as well. I will try duplicating the vertex buffer and use UV2 as index.

-------------------------

