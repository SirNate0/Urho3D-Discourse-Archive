rogerdv | 2017-01-02 01:04:14 UTC | #1

I want to load an specific image inside a BorderImage element, through this code:
[code]UIElement@ grid = invWin.GetChild("grid", true);
BorderImage@ itemPort = BorderImage();
				itemPort.SetSize(32, 32);
				itemPort.texture = Texture();
				itemPort.texture.Load(cache.GetFile("Textures/portraits/2h-axe.png"));
				itemPort.imageRect = IntRect(0, 0, 128, 128);
				grid.AddChild(itemPort);[/code]

But I just get a white square. Whats wrong in my code?

-------------------------

cadaver | 2017-01-02 01:04:15 UTC | #2

Texture is the base class that doesn't actually know how to allocate a GPU texture. Instantiate a Texture2D instead.

-------------------------

