I3DB | 2019-02-06 07:54:09 UTC | #1

Using the SharpReality binding and using the FeatureSample Navigation.

[The line of code throwing the exception is this one](https://github.com/xamarin/urho/blob/050fdf9943b154549e7928b32f398e727191202a/Bindings/Portable/NavigationMesh.cs#L15), as shown:
```
var ptr = urho_navigationmesh_findpath(Handle, start, end, out int count);
```
All the arguments look fine. The definition of the dll call just before that call at the link above is:
```
[DllImport(Consts.NativeImport, CallingConvention = CallingConvention.Cdecl)]
internal extern static IntPtr urho_navigationmesh_findpath(IntPtr navMesh, Vector3 start, Vector3 end, out int count);
```
Upon making that call, the error generated is:
```
Exception thrown: 'System.AccessViolationException' in Urho.dll
An unhandled exception of type 'System.AccessViolationException' occurred in Urho.dll
Attempted to read or write protected memory. This is often an indication that other memory is corrupt.
```

Other platforms I've run this on work fine. (WPF, winForms). But it fails on any UWP platform.

[glue.cpp](https://github.com/xamarin/urho/blob/050fdf9943b154549e7928b32f398e727191202a/Bindings/Native/glue.cpp#L328) defines the call as:
```
DllExport Interop::Vector3 *
urho_navigationmesh_findpath(NavigationMesh * navMesh, const class Urho3D::Vector3 & start, const class Urho3D::Vector3 & end, int *count)
	{
		PODVector<Vector3> dest;
		navMesh->FindPath(dest, start, end);
		if (dest.Size() == 0)
			return NULL;
		*count = dest.Size();
		Interop::Vector3 * results = new Interop::Vector3[dest.Size()];
		for (int i = 0; i < dest.Size(); i++) {
			auto vector = *((Interop::Vector3  *) &(dest[i]));
			results[i] = vector;
		}
		return results;
	}
```

Immediately preceeding that call, a call to navMesh.FindNearestPoint is made, and it runs flawlessly.

```
[DllImport (Consts.NativeImport, CallingConvention = CallingConvention.Cdecl)]
internal static extern Vector3 NavigationMesh_FindNearestPoint (IntPtr handle, ref Urho.Vector3 point, ref Urho.Vector3 extents, dtQueryFilter* filter, uint* nearestRef);
		/// <summary>
		/// Find the nearest point on the navigation mesh to a given point. Extents specifies how far out from the specified point to check along each axis.
		/// </summary>
		public Vector3 FindNearestPoint (Urho.Vector3 point, Urho.Vector3 extents, dtQueryFilter* filter = null, uint* nearestRef = null)
		{
			Runtime.ValidateRefCounted (this);
			return NavigationMesh_FindNearestPoint (handle, ref point, ref extents, filter, nearestRef);
		}
```

[binding.cpp](https://github.com/xamarin/urho/blob/050fdf9943b154549e7928b32f398e727191202a/Bindings/Portable/Generated/binding.cpp#L23986), a generated file, defines that call as:
```
DllExport Interop::Vector3 
NavigationMesh_FindNearestPoint (Urho3D::NavigationMesh *_target, const class Urho3D::Vector3 & point, const class Urho3D::Vector3 & extents, const class dtQueryFilter * filter, dtPolyRef * nearestRef)
{
	return *((Interop::Vector3  *) &(_target->FindNearestPoint (point, extents, filter, nearestRef)));
}
```

More details on the error occurring. [At this call:](https://github.com/xamarin/Urho3D/blob/4862691d18c0ed40895ba532dd7ba6f17cd2c763/Source/Urho3D/Navigation/NavigationMesh.cpp#L677)
```
[navMesh->FindPath(dest, start, end);](https://github.com/xamarin/urho/blob/050fdf9943b154549e7928b32f398e727191202a/Bindings/Native/glue.cpp#L331)
```

The start and end vectors cannot be read by the debugger, both start and end are read as 
```<Struct At NULL>```

The actual crash is when calculating localEnd, the localStart works, this is code from [NavigationMesh.cpp](https://github.com/xamarin/Urho3D/blob/4862691d18c0ed40895ba532dd7ba6f17cd2c763/Source/Urho3D/Navigation/NavigationMesh.cpp#L677):
```
 Vector3 localStart = inverse * start;
 Vector3 localEnd = inverse * end;
```

-------------------------

I3DB | 2019-02-06 07:54:02 UTC | #2

This is a bug in the SharpReality binding.

To make this work for UWP, requires the start and end be passed in as ref. [Here's the original dll call definition](https://github.com/xamarin/urho/blob/050fdf9943b154549e7928b32f398e727191202a/Bindings/Portable/NavigationMesh.cs#L8), and my proposed follows:
```
[DllImport(Consts.NativeImport, CallingConvention = CallingConvention.Cdecl)]
internal extern static IntPtr urho_navigationmesh_findpath(IntPtr navMesh, ref Urho.Vector3 start, ref Urho.Vector3 end, out int count);
```

Next, the two vectors must be passed as ref. [The original is here](https://github.com/xamarin/urho/blob/050fdf9943b154549e7928b32f398e727191202a/Bindings/Portable/NavigationMesh.cs#L15), my suggested changes is as shown:
```
var ptr = urho_navigationmesh_findpath(Handle, ref start, ref end, out int count);
```

Then it works.

-------------------------

