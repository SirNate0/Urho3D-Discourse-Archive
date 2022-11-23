desmond | 2017-11-28 13:43:52 UTC | #1

This is a critical issue for me because it affects the environment scene significantly. I'm building a 2D environment.

When my sprites are zoomed in, the overlap seems fine, there's no dark line. When zoomed out with multiple sprites organized in a grid format, there're dark lines that appear around each StaticSprite2D object. 

The lines are not part of the original resource image for sure. No texture offset.

class: Node, StaticSprite2D, Sprite2D
resource file: .png

Does any one know what's the issue? 

![full|690x271](upload://7bMSmbWBCJIf8wMR5ZOch8tBT29.jpg)

-------------------------

desmond | 2017-11-28 13:43:24 UTC | #2

I realized its due the filter we need to set for the resource. Based on some searching, only option I can find is filter="nearest", but that affects the quality of image. 

Is there any way to create a custom filter that retains quality but detects edges accordingly?

-------------------------

Victor | 2017-11-28 14:17:05 UTC | #3

Not sure if this is available for sprites, but are you able to use Texture2DArrays? That might be a solution.

https://discourse.urho3d.io/t/how-to-use-texture2darray/2695

-------------------------

Eugene | 2017-11-28 16:21:33 UTC | #4

In order to use linear filtering you have to ensure that your atlas have some gaps between sprites filled with edge color. That would be the simplest workaround

-------------------------

orefkov | 2017-11-28 20:19:30 UTC | #5

Possibly you use images with transparent areas on edges?
Its common problem for that images - sometimes in transparent pixels writed black color in RGB channels, and it blended with edge pixels on filtering.
GPU first do filter RGB channels in texture, without respect to alpha channel, and second apply alpha.
Look at any editor, which may show RGB channels without alpha in your image, and paint nearest with edges transparent pixels in same color, as non transparent.

In Godot engine exist options on import sprites - "Fix black edges".
Sometime I take algoritm from it and implement on AngelScript for Urho3D:

    void fixPngColors(const String& name) {
    	File file;
    	file.Open(name);
    	Image image;
    	image.Load(file);
    	file.Close();
    	Print("Load image " + image.width + " x " + image.height);
    	int repl = 0;
    	for (int r = 0; r < image.height; r++) {
    		for (int c = 0; c < image.width; c++) {
    			Color clr = image.GetPixel(c, r);
    			if (clr.a < 0.1) {
    				repl++;
    				Color nearestColor(0, 0, 0, 0);
    				int minX = Max(c - 4, 0), maxX = Min(c + 4, image.width),
    					minY = Max(r - 4, 0), maxY = Min(r + 4, image.height),
    					closestDist = 900;
    				for (int x = minX; x < maxX; x++) {
    					for (int y = minY; y < maxY; y++) {
    						int dist = (c - x) * (c - x) + (r - y) * (r - y);
    						if (dist < closestDist) {
    							Color pix = image.GetPixel(x, y);
    							if (pix.a > 0.2) {
    								nearestColor = pix;
    								closestDist = dist;
    							}
    						}
    					}
    				}
    				nearestColor.a = 0;
    				image.SetPixel(c, r, nearestColor);
    			}
    		}
    	}
    	if (repl > 0) {
    		image.SavePNG(name.Substring(0, name.length - 4) + "-1.png");
    		Print("Saved to " + name.Substring(0, name.length - 4) + "-1.png repl=" + repl);
    	} else {
    		Print("No replaced");
    	}
    }

    void fixAllPngs() {
    	Print("Scan files...");
    	String path = "Data/Sprites/";
    	auto files = fileSystem.ScanDir(path, "*.png", 1, true);
    	for (uint i = 0; i < files.length; i++) {
    		fixPngColors(path + files[i]);
    	}
    }

It scan pixels in image, and if it alpha < 0.1 - search nearest non alpha pixel, and set color to that color.
Also it zeroed alpha of all pixel, where it less than threshold value.
You can tray play with threshold level of alpha in this code, for get desired result.

-------------------------

desmond | 2017-11-30 16:49:43 UTC | #6

Tried this and works perfectly :) thanks so much

-------------------------

