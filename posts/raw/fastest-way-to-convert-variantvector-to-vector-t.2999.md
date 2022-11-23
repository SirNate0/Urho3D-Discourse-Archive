godan | 2017-04-11 18:11:57 UTC | #1

In my projects, I do a *ton* of work with VariantVectors and Variants in general. Something that comes up a lot is that I have say, a typed Vector:

```
Vector<Vector3> myPoints;
```
and I want to convert this to a VariantVector. The obvious way is:

```
VariantVector myVarVec;
int numPoints = myPoints.Size();
myVarVec.Resize(numPoints);

for(int i = 0; i < numPoints; i++){
myVarVec[i] = myPoints[i];
}
```

Is there a mem_copy I can do? A cast?

-------------------------

1vanK | 2017-04-11 20:55:47 UTC | #2

(Some offtopic) Use
```
PODVector<Vector3>
```
istead 
```
Vector<Vector3>
```
for speed.

-------------------------

Eugene | 2017-04-12 05:22:06 UTC | #3

[quote="godan, post:1, topic:2999"]
The obvious way is:
[/quote]

The _only_ way is that one.
You may perform per-element cast from Variant to Vector3, but I am unsure that it would be faster.

-------------------------

