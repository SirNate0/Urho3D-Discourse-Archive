rogerscg | 2020-08-16 17:33:27 UTC | #1

I'm currently using DEM data at 1/3 arc second resolution for the terrain in my game. The elevation data is stored as floats. I was hoping that Terrain would support the .tiff format directly, but it seems that only BMP, PNG, JPG, and TGA are supported. When using PNG or JPG, I lose support for floats, and end up with contours as shown here:
![](upload://f1nH87XhJXseDhr5Tf6dTVZPC2C.jpeg) 

Is there a supported way to use floats for terrain data?

Thanks!

-------------------------

UrhoIsTheBest | 2020-08-31 06:28:47 UTC | #2

The easiest solution I can think of is to create a ```CustomTerrain``` class by copying the ```Terrain``` class, and slightly change the way it reads from heightmap image data.

If you look at the source code for ```Terrain``` class, luckily, the height data is already stored as float
```
    /// Height data.
    SharedArrayPtr<float> heightData_;
    /// Source height data for smoothing.
    SharedArrayPtr<float> sourceHeightData_;
```

So the only thing you need to change is around line 940-1000 in ```Terrain.cpp```
```
// Reading single channel image data.
float newHeight = (float)src[imgRow * (numVertices_.y_ - 1 - z) + x] * spacing_.y_;
...
// Reading multiple channels data (R and G).
float newHeight = ((float)src[imgRow * (numVertices_.y_ - 1 - z) + imgComps * x] +
                                       (float)src[imgRow * (numVertices_.y_ - 1 - z) + imgComps * x + 1] / 256.0f) * spacing_.y_;
```
where the ```src``` is the source image data you can read whatever you want, e.g. tiff (You can find other library from DEM to read it).

-------------------------

JTippetts1 | 2020-08-31 09:37:23 UTC | #3

Terrain class also supports an encoded PNG format, where the height is stored in the Red and Green channels, with the green channel holding the fractional part. This gives you 65536 levels of elevation, instead of the regular 256 that a basic greyscale heightmap gives you, and should help alleviate the tiering that you see. Additionally, Terrain has a toggleable Smoothing setting which can further smooth out those edges.

-------------------------

Modanung | 2020-08-31 14:25:31 UTC | #4

@rogerscg Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

