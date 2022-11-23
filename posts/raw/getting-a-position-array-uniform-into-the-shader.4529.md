HaeferlKaffee | 2018-09-10 21:02:17 UTC | #1

I've updated the OGL Graphics code in the engine with the functions from this post: [https://discourse.urho3d.io/t/array-shader-parameters/1078/6](https://discourse.urho3d.io/t/array-shader-parameters/1078/6)

Currently I'm setting the array uniform with this snippet:

        VariantVector varvec;
		varvec.Push(Vector3(0.0f, 0.5f, 0.0f));
		varvec.Push(Vector3(1.0f, 0.5f, 0.0f));
		varvec.Push(Vector3(1.0f, 0.5f, 1.0f));
		varvec.Push(Vector3(0.0f, 0.75f, 1.0f));
		grassMaterial->SetShaderParameter("ObjectPositionArray", varvec);

But how should I define the Vector3 array in the material definition? In the shader, I assume it's just the usual GLSL opaque array declaration, but I can't seem to find any material definitions that deal with arrays.

-------------------------

