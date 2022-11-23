najak3d | 2020-08-12 00:03:37 UTC | #1

What is the main difference between these 3 classes?   We have a 3D application that shows a 2D map in 3D space (NOT orthographic).  

So far we've been using Texture2D - with no issues.  But it's contained in namespace Urho.Urho2D... which seems weird, and makes me think we might be using an inappropriate class.   

We are converting from straight OpenGL, where we use Texture2D for everything, and so naturally that's what we're using with Urho.  But to be sure, I'm asking the question here -- what's the difference between these three Urho classes?  And which ones are most appropriate for various contexts?

-------------------------

JTippetts1 | 2020-08-12 00:15:32 UTC | #2

Texture is a base class from which Texture2D, Texture3D and Texture2DArray are derived. Texture2D is a 2D texture (your typical diffuse map, normal map, etc....) while Texture3D is a 3D texture (typically used for volumetric-type stuff). Texture2DArray is an array of 2D textures.

Not sure what you mean by Texture2D being in the Urho2D namespace. It's in the base Urho3D namespace as you can see at https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Texture2D.h#L29

-------------------------

najak3d | 2020-08-12 01:32:00 UTC | #3

Thank you.  That aligns with what I was hoping to hear.  All is well.

For UrhoSharp (which is what we use), it's in the Urho.Urho2D namespace, which raised the question for me.   Texture2D is what we have been using and what we should continue to use.

-------------------------

