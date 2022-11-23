n91 | 2017-01-02 01:13:22 UTC | #1

When I am rendering scene to texture and displaying only UI elements, screen doesn't seem to be cleared:

[img]http://i.imgur.com/p6NCHft.gif[/img]

The simplified code (in C# via UrhoSharp) producing this is following:

[code]
        Text helloText;

        protected override void Start()
        {
            helloText = new Text();
            helloText.SetFont(font: ResourceCache.GetFont("Fonts/Font.ttf"), size: 15);
            UI.Root.AddChild(helloText);

            var scene = new Scene();
            scene.CreateComponent<Octree>();

            var camera = scene.CreateChild("camera").CreateComponent<Camera>();

            var tx = new Texture2D();
            tx.SetSize(10, 10, Graphics.RGBFormat, TextureUsage.Rendertarget);

            var rs = tx.RenderSurface;
            rs.UpdateMode = RenderSurfaceUpdateMode.Updatealways;
            rs.SetViewport(0, new Viewport(scene, camera, null));
        }

        protected override void OnUpdate(float timeStep)
        {
            helloText.Value = ((char)(DateTime.Now.Second % 4 + 'A')).ToString();
        }
[/code]

However when I the render surface part. The output is what I want:

[img]http://i.imgur.com/3epPv8U.gif[/img]

What I am doing wrong? Is it a feature/bug of UrhoSharp/Urho3d?

-------------------------

cadaver | 2017-01-02 01:13:22 UTC | #2

This is a bug, or rather an unhandled situation. The Renderer checks if there are no views, and in that case it clears the screen each frame, instead of relying on the views overwriting the screen contents. However in this case there are views, though not backbuffer views. So it really should be checking that there is at least one active view that renders to the backbuffer, and if not, clear the screen.

-------------------------

cadaver | 2017-01-02 01:13:22 UTC | #3

Fixed in Urho master branch.

-------------------------

n91 | 2017-01-02 01:13:23 UTC | #4

Thank you.

-------------------------

