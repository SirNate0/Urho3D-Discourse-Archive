PsychoCircuitry | 2021-09-13 12:14:34 UTC | #1

Hello, I have an instance where I'm trying to write a vector buffer into another vector buffer. I built Urho3D from latest master on 08/28/21

Now when attempting to write a buffer into another buffer, it always returns false.

I've used Cadaver's example from [this](https://discourse.urho3d.io/t/solved-serialize-deserialize-a-vectorbuffer-as/754) post where the feature was added, and this also returns false.

So I had an old build on my system still (sometime around 1.7.1 release) and this works as expected. Writing a buffer into a buffer returns true and the size is > 0.

As example:
```
VectorBuffer mainBuffer;

VectorBuffer addThisBuffer;
addThisBuffer.WriteString("TestData");

mainBuffer.WriteVectorBuffer(addThisBuffer);
```
This will return false with mainBuffer size of zero on latest master branch I've built. However, works as expected on older versions.

I'm wondering if this is a local issue with my build, or if it is an issue with the actual latest master.

I have worked around this temporarily by casting the VectorBuffer I wish to add as a Variant data type, then writing this to the buffer. And this works.

Example:
```
mainBuffer.WriteVariant(Variant(addThisBuffer));
```

This works on the latest build I have.

Is this a bug? A build issue I have? Or a conscious redesign of the VectorBuffer (at least as exposed to AngelScript)?

Any additional thoughts would be appreciated. And also a heads up if anyone else is attempting to do something similar.

Thanks
-PsychoCircuitry

Edit: if anyone else is running into this issue, I thought I'd clarify how to use the work around to retrieve the buffer objects since when you write them as Variant data type, you cant just use the ReadVectorBuffer(UInt) method.

Fortunately the Variant container wraps the buffer with info about its size, so you dont have to worry about the size of the object when reconstructing, as the container itself adds additional size to the object(which could make it tricky).

In the example above, I'd read the data back as:
```
mainBuffer.Seek(0);

VectorBuffer readAddThisBuffer = mainBuffer.ReadVariant().GetBuffer();
```
This seems to be working ok. I have no issues with the reconstructed buffer after this process.

-------------------------

1vanK | 2021-09-13 12:10:34 UTC | #2

Can you test latest master?

-------------------------

PsychoCircuitry | 2021-09-13 12:11:12 UTC | #3

Fixed. Thanks for the quick fix on this, 1vanK. Fantastic!

-------------------------

