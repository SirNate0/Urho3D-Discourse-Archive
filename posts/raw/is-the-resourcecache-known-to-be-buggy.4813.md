I3DB | 2019-01-11 21:24:57 UTC | #1

Using SharpReality/C#, running on Hololens.

Have been working a lot with [this sample](https://github.com/xamarin/urho-samples/tree/master/FeatureSamples/Core/43_BasicTechniques), and about every other launch, there is an exception thrown when working with the ResourceCache on the fly.

So if running in a loop, code like this frequently throws an exception:
```
earthModel.SetMaterial(ResourceCache.GetMaterial($"Sample43/Mat{material}.xml", sendEventOnFailure: false));
```

However, if I pre-populate the ResourceCache with code like this:
```
            var materials = new string[,]
            {
                { "NoTexture", "NoTextureUnlit", "NoTextureNormal", "NoTextureAdd", "NoTextureMultiply" },
                { "Diff", "DiffUnlit", "DiffNormal", "DiffAlpha", "DiffAdd" },
                { "DiffEmissive", "DiffSpec", "DiffNormalSpec", "DiffAO", "DiffEnvCube" },
                { "Water", "Terrain", "NoTextureVCol", "Default", "CustomShader" },
            };

            for (int i = 0; i < materials.GetLength(1); i++)
                for (int j = 0; j < materials.GetLength(0); j++)
                    var throwMeAway = Application.ResourceCache.GetMaterial($"Sample43/Mat{materials[j, i]}.xml", sendEventOnFailure: false);
'''

Then the exceptions go away.

-------------------------

S.L.C | 2019-01-11 22:34:39 UTC | #2

Last time I checked, Urho does not throw exceptions. So if there is an exception, it could be thrown by the bindings that you're using. In which case you can't really blame Urho since it isn't something from the engine itself.

Also `throws an exception` is a bit vague. As sometimes different exceptions have different meanings. Which is supposed to narrow the hunt for issues.

-------------------------

I3DB | 2019-01-12 01:00:18 UTC | #3

My hurried description ... actually it results in memory access violations. But here's how Visual Studio outputs the error in debug mode:

Exception thrown: 'System.AccessViolationException' in Urho.dll
An unhandled exception of type 'System.AccessViolationException' occurred in Urho.dll
Attempted to read or write protected memory. This is often an indication that other memory is corrupt.

In  order to generate this error, on demand, in the [Feature Sample Huge Object coun](https://github.com/xamarin/urho-samples/blob/master/FeatureSamples/Core/20_HugeObjectCount/HugeObjectCount.cs)t,  at this point:

https://github.com/xamarin/urho-samples/blob/b72d055a424d0e6be825c0239683c225d29ee723/FeatureSamples/Core/20_HugeObjectCount/HugeObjectCount.cs#L157

I inserted this line:
```
lastGroup.Material = Material.FromColor(Randoms.NextColor());
```

And sure enough, out pops the violation.

I'm starting to suspect it's not related to the ResourceCache, but to the Material class.

This is that code:
```public static Material FromColor(Color color, bool unlit)
		{
			var material = new Material();
			var cache = Application.Current.ResourceCache;
			float tolerance = 0.001f;
			if (unlit)
				material.SetTechnique(0, Math.Abs(color.A - 1) < tolerance ? CoreAssets.Techniques.NoTextureUnlit : CoreAssets.Techniques.NoTextureUnlitAlpha, 1, 1);
			else
				material.SetTechnique(0, Math.Abs(color.A - 1) < tolerance ? CoreAssets.Techniques.NoTexture : CoreAssets.Techniques.NoTextureAlpha, 1, 1);
			material.SetShaderParameter("MatDiffColor", color);
			return material;
		}
```

Then .SetTechnique
```
public void SetTechnique (uint index, Technique tech, uint qualityLevel = 0, float lodDistance = 0f)
		{
			Runtime.ValidateRefCounted (this);
			Material_SetTechnique (handle, index, (object)tech == null ? IntPtr.Zero : tech.Handle, qualityLevel, lodDistance);
		}
```
And SetShaderParameter
```public void SetShaderParameter (string name, Color value)
		{
			Runtime.ValidateRefCounted (this);
			Material_SetShaderParameter2 (handle, name, ref value);
		}
```

And the ValidateRefCounted
```
		// for RefCounted, UrhoObjects
		internal static void ValidateRefCounted<T>(T obj, [CallerMemberName] string name = "") where T : RefCounted
		{
			//TODO: remove ValidateRefCounted from IsExiting in the Binder
			if (name == "IsExisting")
				return;

			if (IsClosing)
			{
				var errorText = $"{typeof(T).Name}.{name} (Handle={obj.Handle}) was invoked after Application.Stop";
				LogSharp.Error(errorText);
				throw new InvalidOperationException(errorText);
			}
			if (obj.IsDeleted) //IsDeleted is set to True when we receive a native callback from RefCounted::~RefCounted
			{
				var errorText = $"Underlying native object was deleted for Handle={obj.Handle}. {typeof(T).Name}.{name}";
				LogSharp.Error(errorText);
				throw new InvalidOperationException(errorText);
			}
			//if (obj.Handle == IntPtr.Zero)
			//{
			//}
			//TODO: check current thread?
		}
```

-------------------------

I3DB | 2019-01-15 20:30:42 UTC | #4

Haven't researched this through the SharpReality implementation but notice this:

using for example:

var mat = Material.FromColor(Randoms.NextColor());
object.Material = mat;

is more stable than using

object.SetMaterial(Material.FromColor(Randoms.NextColor());

Meaning, some seemingly random exceptions stop when all the .SetMaterial() calls are converted to Material =.

Still prepopulating the ResourceCache though.

And a second area of random exceptions is around execution on the main thread vs background threads.  This exception isn't well exposed to the developer when it happens. I tend to see memory access violations as the clue that it's happening, and go look in the code for something affecting the GUI running on a background thread.

-------------------------

I3DB | 2019-01-22 08:39:34 UTC | #5

Want to add a followup to this.

I've successfully reduced the issues my code experienced down to zero. And have changed my mind the resource cache might be buggy.

There were two primary issues occurring in my code, due to my own mistakes. The first is uncleaned actions still running on nodes that were deleted, and this at times corrupts or complains on memory access. The second is calling functions that affect the UI from a background thread, rather than invoking on the main thread.

After fixing these issues, at this time no unexplained exceptions are happening, at least regarding Materials creation and the resource cache. 

The constantly recurring exception pointed out above that happens consistently with a code change to the Huge Object Count feature sample, to paint each box a different color, will still happen at times, but typically passes the first time. So likely it is still something in my code.

-------------------------

I3DB | 2019-01-23 19:16:12 UTC | #6

Want to add a bit more about materials.

Scenario:

1. Created a new class, and inherit from Component, the class is a simple box that changes colors
2. In OnUpdate method choose the material based on some setting that frequently changes

So the box.Material = matA, or = matB, or = matC.

This frequently throws exceptions. And found the exception is because when re-using the material, say matA or matB or matC, the material is found in the IsDeleted state.

The class creates a reference to each material in the OnAttachedToNode method in a class variable.

To address this exception, after assigning the material, for instance using:
```
matA = Material.FromColor(Color.White);
```

it is necessary to add this line:
```
matA.AddRef();
```

So it seems there is an aggressive cleanup or garbage collection that does not respect the class variable holding the reference to the material, and cleans it up as soon as the box is assigned a new material.

so this code
```
box.Material = matA; 
... //after some other code executes
box.Material = matB;
```

The next access to matA will throw an exception because matA.IsDeleted is true;

Am I missing something? or is the matA.AddRef(); standard code that must be added?

I don't mind adding this code, but finding other cases where I have less control, for instance with using the TintTo action, it will often throw an exception because a material it's using has been deleted. I can rewrite this action class, but don't want to. 

Wondering why the material is being cleaned when references are still held.

-------------------------

