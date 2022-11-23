csteaderman | 2022-02-15 21:19:33 UTC | #1

I'm developing a cross platform app (Xamarin.Forms), and have successfully integrated Urho (UrhoSharp) and everything works on Android and iOS (as far as I know). I've now been asked for a Desktop (Windows) version of the app. I added a UWP project to my solution, and was pleasantly surprised that I was able to render my Urho model in the UWP project. Unfortunately, I discovered that my morphing is not working in the UWP version. I am using `SetMorphWeight()` in my code. The exception that I am getting is:

`Failed to map vertex buffer (HRESULT 80070057). You can omit this exception by subscribing to Urho.Application.UnhandledException event and set Handled property to True.`

Any pointers about what I should do differently on UWP vs iOS and Android? Additional steps I might perform to determine the cause of the issue?

-------------------------

najak3d | 2022-02-25 00:24:33 UTC | #2

I'm on UrhoSharp too.   IIRC, the last time I face down that error, it was caused by me accessing Urho from a non-Urho thread.    In Urho, gotta make sure all calls to Urho (the ones that write to the GPU especially, like VertexBuffer.SetData/Size, etc, MUST be done from the Urho Update thread.

Once we fixed the couple violations where we did something like this from a Non-URHO thread, this issue went away for us.

===
The best way I've found for diagnosing issues with UrhoSharp is the basic trial/error method, where you just dumb down whatever is failing to something far more basic, and then once it starts working, then reverse the process adding in more things until it starts failing.  In this way, you narrow down the "cause" -- which could be just "one settings", or something else small.

I know it's not a magic solution, but hope this might help.

-------------------------

csteaderman | 2022-02-25 23:04:07 UTC | #3

Thanks for taking time to read and respond.

That is an interesting idea. I think that I'm performing my morph calls on the proper thread:

```
Urho.Application.InvokeOnMain(() =>
{
	if (baseComponent != null)
	{
		baseComponent.SetMorphWeight("Top", morph);
	}
}
);
```
I did have cross-thread issues when I initially implemented the app for Android and iOS. Supporting UWP was a last minute addition. Any idea if MacOS target for the app would have a better chance at working properly?

-------------------------

