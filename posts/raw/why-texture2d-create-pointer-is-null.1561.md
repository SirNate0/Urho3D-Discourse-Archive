simple | 2017-01-02 01:08:30 UTC | #1

Hello I have something weird with my code.
I just code something like this for test:

[code]
void test()
{
	Urho3D::Engine *engine = new Urho3D::Engine(g_pEngineContext);
	Urho3D::VariantMap engineParameters;
	engineParameters["FrameLimiter"] = false;
	engineParameters["WindowTitle"] = "Engine";
	engineParameters["LogName"] = "Engine.log";
	engineParameters["FullScreen"] = false;
	engineParameters["ExternalWindow"] = 0;
	if (!engine->Initialize(engineParameters)) return;

	Urho3D::Texture2D *tex = new Urho3D::Texture2D(g_pEngineContext);
	tex->SetSize(2, 2, Urho3D::Graphics::GetRGBAFormat());
};
int main(int argc, char* argv[])
{
	_CrtSetDbgFlag(_CRTDBG_ALLOC_MEM_DF | _CRTDBG_LEAK_CHECK_DF);
	g_pEngineContext = new Urho3D::Context();
	test();
	return 0;
};
[/code]

My code crashing in line: [b]"tex->SetSize(2, 2, Urho3D::Graphics::GetRGBAFormat());"[/b]
I just debug what exacly crashing, and here you go:
"Texture2D::Create() pointer is NULL. Why?"

[img]http://images.tinypic.pl/i/00734/vpbzl45t0nxj.png[/img]

-------------------------

simple | 2017-01-02 01:08:31 UTC | #2

I solved this problem but this is really little weird:

I changed: 
[b]return Create();[/b]
to:
[b]return Texture2D::Create();[/b]

and no longer crashing.

-------------------------

thebluefish | 2017-01-02 01:08:31 UTC | #3

I assume this is in OpenGL? Or are you using the default DX11?

Visual Studio can tell you which function Create(); was originally pointed to. Please let us know where that points to.

Also is this the 1.5 stable release or from the master branch?

-------------------------

simple | 2017-01-02 01:08:31 UTC | #4

[quote="thebluefish"]I assume this is in OpenGL? Or are you using the default DX11?[/quote]
OpenGL.

[quote]Also is this the 1.5 stable release or from the master branch?[/quote]
master branch.

[quote]Visual Studio can tell you which function Create(); was originally pointed to. Please let us know where that points to.[/quote]
I not really sure where exacly show me this. but tooltip show me (0x5417cbc0 where body of Texture2D::Create):
[img]http://pics.tinypic.pl/i/00734/37w2x395hqpk.png[/img]

but '[b]call edx[/b]' still have NULL address.
[img]http://pics.tinypic.pl/i/00734/gdn4saibmzpk.png[/img]

-------------------------

simple | 2017-01-02 01:08:32 UTC | #5

Well, i definately found a solution.
In OpenGL Application i need set Preprocessor definition: [b]URHO3D_OPENGL[/b]
If i not set this then would cause heap corruptions etc...

-------------------------

Enhex | 2017-01-02 01:08:32 UTC | #6

[quote="simple"]Well, i definately found a solution.
In OpenGL Application i need set Preprocessor definition: [b]URHO3D_OPENGL[/b]
If i not set this then would cause heap corruptions etc...[/quote]
Did u set Urho to use OpenGL in the cmake build options?

-------------------------

thebluefish | 2017-01-02 01:08:32 UTC | #7

[quote="simple"]Well, i definately found a solution.
In OpenGL Application i need set Preprocessor definition: [b]URHO3D_OPENGL[/b]
If i not set this then would cause heap corruptions etc...[/quote]

That would be it! The graphics implementation headers are weird in that regard. I'm hoping this gets changed later down the road.

-------------------------

