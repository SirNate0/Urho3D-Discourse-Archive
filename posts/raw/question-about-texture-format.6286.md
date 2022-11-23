UrhoIsTheBest | 2020-07-26 03:25:30 UTC | #1

**TL;DR:**
I notice there is ```format_``` member for ```Texture``` class. This should be the value we set like ```GL_RGB``` texture format for OpenGL.
Since ```format_``` is just ```unsigned```, I was wondering the mapping relation between the ```integer``` and different OpenGL texture format ```GL_XXXX```. I searched the Urho3D source code but could not find anything.
I only found it's only been set in 
```
bool Texture2D::SetSize(int width, int height, unsigned format, TextureUsage usage, int multiSample, bool autoResolve)
``` 
functions.

I noticed the opengl ```texture``` function returns color as ```float [0.0, 1.0]```. I wonder if there is any ```format_``` setting that I could directly use the raw 8 bit data, e.g. ```integer [0, 255]```.



**=====================================================**  
**Background**
I am using the default texture unit 0 for my heightmap terrain texture.

When I generate the texture image, I simply do:
```
const float height = GetHeightFromSource(x, y);
const int16_t height_16bit = static_cast<int16_t>(height);
const unsigned char r = height_16bit >> 8;
const unsigned char g = height_16bit & 0xFF;
```
Notice I have **negative values in my heightmap**. This is not a problem since we can deal with it when decode the texture. And I verified it works as expected.
```
Height height = (R << 8) + G;
```


Now when I use this texture image in opengl vertex shader for heightmap displacement.
I noticed the opengl ```texture``` function returns color as ```float [0.0, 1.0]```. That's fine since we can always map back to ```integer [0, 255]```.
I can either simply do
```
int height = int(r * 255) * 256 + int(g * 255);
```
or as someone on stackoverflow mentioned:
```
int r = int(floor(r >= 1.0 ? 255 : r * 256.0));
int g = int(floor(g >= 1.0 ? 255 : g * 256.0));
```

As for negative values, unfortunately we don't have bit manipulation in shader but that's not a problem.
I can do
```
vec2 heights = texture(sHeightMap0, texCoord).rg;
if (heights.r >= 0.5) {
    return ((int(heights.r * 255) * 256  + int(heights.g * 255)) - 256 * 256) * scale;
} else {
    return (heights.r * 256 + heights.g) * 256 * scale;
}
```

I thought this is correct.
For example, for ```height = -1```, we encode into ```R = 1111 1111```, ```G = 1111 1111```.
So in shader we get: ```heights.r = 1.0, heights.g = 1.0```.
Then we should get ```-1 * scale``` as the final result.

**However, there are many sharp spikes in my terrain for those negative value regions.**

![image|674x500](upload://jf25oD0GnvKMCSGBPmbG0Rmk2B2.jpeg) 

**I verified those height raw values and calculated them using my formula, everything should be correct.**
**This does not make any sense to me unless I've made some stupid mistakes somewhere?**

-------------------------

UrhoIsTheBest | 2020-07-26 03:26:25 UTC | #2

Ah, yes, it's a stupid mistake!
It's because the default **```TextureFilterMode```**.

I spent the whole afternoon debugging this and did not realize it until I clicked the ```Create Topic``` button.
:rofl:


But the original question is still valid:
Since  `format_`  is just  `unsigned` , I was wondering the mapping relation between the  `integer`  and different OpenGL texture format  `GL_XXXX`

-------------------------

Eugene | 2020-07-26 10:26:27 UTC | #3

[quote="UrhoIsTheBest, post:2, topic:6286"]
I was wondering the mapping relation between the `integer` and different OpenGL texture format `GL_XXXX`
[/quote]
It should be 1-to-1. Meaning that the `integer` _is_ OpenGL texture format `GL_XXXX`.

-------------------------

UrhoIsTheBest | 2020-07-26 18:52:31 UTC | #4

Right, but I was wondering the exact mapping, like which integer means GL_RGB, and 0 -> GL_XXXX, 1 -> GL_YYYY, 2 -> GL_ZZZZ, etc.
I briefly checked the opengl online documentation, I can only find all those GL_XXXX description, but could not related to the raw integer value (e.g. could not find the source enum definition).

-------------------------

Eugene | 2020-07-27 03:02:08 UTC | #5

You can find OpenGL header somewhere in your system or find it online, if you need exact numbers for some reason.

This one may work, even tho it’s OSX
https://opensource.apple.com/source/X11server/X11server-85/libGL/AppleSGLX-57/specs/enum.spec

-------------------------

