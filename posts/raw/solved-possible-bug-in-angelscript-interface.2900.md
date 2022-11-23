Sasha7b9o | 2017-03-16 07:32:23 UTC | #1

Hi.
When I call function **CScriptArray* VectorToArray(const Vector<T>& vector, const char* arrayName)** (`VectorToArray <String>   (GetArguments(), "Array<String>");`), 
linker write error **"can not find funciton asGetActiveContext();"** (Urho3D compiled with option -DURHO3D_LIB_TYPE=SHARED)
If link library ActionScript.lib manually, game compiles, but function asGetActiveContext() return 0. In comments function write: 

	// tld can be 0 if asGetActiveContext is called before any engine has been created.

	// Observe! I've seen a case where an application linked with the library twice
	// and thus ended up with two separate instances of the code and global variables.
	// The application somehow mixed the two instances so that a function called from
	// a script ended up calling asGetActiveContext from the other instance that had
	// never been initialized.

When engine compiled with option DURHO3D_LIB_TYPE=STATIC , everything is fine.

Sorry for bad english

-------------------------

weitjong | 2017-03-15 01:41:11 UTC | #2

Something like this has been discussed before, but I cannot remember where. This is the drawback (or benefit, depending on how you see it) of using SHARED lib type because the library target is produced by invoking a linking phase which does a dead code elimination. That is, all symbols not referenced directly or indirectly by Urho itself are being eliminated. Note that in our current setup, the internal 3rd-party libs are always statically linked regardless of Urho3D lib type chosen. 

There are a few ways to workaround this. Two that do not require modifications to the engine code and build system would be:

- Using Urho3D STATIC lib, which is basically just an archive of all symbols there are (like you have pointed out); Or
- Add a new SHARED lib target in your own project that statically linked to Urho3D lib, which references the symbols you want from AngelScript lib. Then make your app depends on your new SHARED lib target.

-------------------------

Sasha7b9o | 2017-03-15 09:16:10 UTC | #3

[quote="weitjong, post:2, topic:2900"]
Add a new SHARED lib target in your own project that statically linked to Urho3D lib, which references the symbols you want from AngelScript lib. Then make your app depends on your new SHARED lib target.
[/quote]
Thanks. But this method does not work, or I misunderstood. Could you explain in more detail?

-------------------------

cadaver | 2017-03-15 09:26:11 UTC | #4

This particular case looks like that there should be a Urho3D wrapper for asGetActiveContext() which should be used by the template functions so that it would work for both cases.

-------------------------

weitjong | 2017-03-15 11:00:46 UTC | #5

I didn't look at the code yet so far. But yes, I think so. If it is referenced somewhere then the symbol would be kept.

-------------------------

cadaver | 2017-03-15 15:38:08 UTC | #6

In master branch, template functions no longer call asGetActiveContext() directly.

-------------------------

Sasha7b9o | 2017-03-16 07:10:08 UTC | #7

Very nice.
Now everything works as it should)

-------------------------

