Alan | 2018-07-07 21:12:37 UTC | #1

Hello there.
I have a mesh batcher here and it's working wonders, however, whenever I switch to release build the `UpdateBatches` function isn't called. I've tried everything, disabled all optimizations both in Urho (static link) and my code, it simply refuses to work :cry:. I made a simple test class and the problem is reproducible, here you go: 
```
//NOTE: run "context_->RegisterFactory<TestDrawable>();" somewhere
class TestDrawable : public Drawable
{
public:
	URHO3D_OBJECT(TestDrawable, Drawable);
	
	explicit TestDrawable(Context* context) : Drawable(context, DRAWABLE_ANY) {}

	virtual void UpdateBatches(const FrameInfo& frame) override
	{
		printf("CALLED!\n");
	}

	virtual void OnWorldBoundingBoxUpdate() override
	{
		boundingBox_ = BoundingBox(-10000, 10000);
	}
};
```
Any ideas what could be causing that problem? Thanks in advance.

-------------------------

S.L.C | 2018-07-07 22:56:00 UTC | #2

Compiler? (GCC, Clang, MSVC?) Compiler Version? Architecture? (x64,x32,ARM) Platform? (Windows, Linux, Android, Mac, iOS) Engine Version? (last stable, development)

A bit more details would be appreciated, don't you think? I mean, try to ask this question to yourself and see what you would need to answer it.

-------------------------

Alan | 2018-07-08 04:05:57 UTC | #3

You're 100% correct... I wrote that in frustration and omitted all those important details:

Compiler
```text
Microsoft (R) C/C++ Optimizing Compiler Version 19.14.26430 for x64
Visual Studio 2017 Community v15.7.3
```
OS
```text
Microsoft Windows 7 Home Premium version 6.1.7601 Service Pack 1 x64
```
Engine
```text
Git branch up-to-date with 'origin/master'.
b78992ba433f2c20b3db2b8fa1cbd200b13cc78f
```

-------------------------

Alan | 2018-07-10 14:38:22 UTC | #4

Bump.
:notes: *There's something happening here... what it is ain't exactly clear* :notes:
Seriously, I've checked all the configurations that you can access from the GUI and they're all exactly the same now except for the debug defines. Next thing to do is check that filthy xml for configs that don't show in the GUI.

-------------------------

