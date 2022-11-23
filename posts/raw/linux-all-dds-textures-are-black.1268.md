NCrashed | 2017-01-02 01:06:30 UTC | #1

Platform: Fedora 21 x86_64 
Graphic card: Radeon HD 7970
Urho3D commit: 0e031852d15d5c5f4798993216f7f4523da43f59

Hi, I've just compiled Urho3D from source and all samples are loading DDS textures filled with black color (although all other info: width, height - shows as should be). The problem affects only DDS format, others are fine.

Compiled with:
```
./cmake_generic.sh build -DURHO3D_SAMPLES=1 -DURHO3D_EXTRAS=1  -DCMAKE_INSTALL_PREFIX=/usr -DURHO3D_LIB_TYPE=SHARED
```

Tried with static build, there are no changes.

Screenshots:
[dropbox.com/s/vydo95vtdghc2 ... 7%3A32.png](https://www.dropbox.com/s/vydo95vtdghc2fs/Screenshot%20from%202015-08-17%2014%3A17%3A32.png)

[dropbox.com/s/8pcbluw7gohny ... 7%3A52.png](https://www.dropbox.com/s/8pcbluw7gohny5i/Screenshot%20from%202015-08-17%2014%3A17%3A52.png)

-------------------------

NCrashed | 2017-01-02 01:06:31 UTC | #2

> Are you using only the DDS textures that are part of the included sample data in Textures? Also which sample(s) are those that you're running?

All DDS textures are from sample data (installed at "/usr/share/Urho3D"). All samples with DDS are broken. First screenshot is 02_HelloGUI, the second is 04_StaticScene. 

Also I tried to convert DDS to PNG with ImageMagick, it seems as should be (not corrupted) and operates fine (if you replace DDS with PNG everywhere).

-------------------------

cadaver | 2017-01-02 01:06:31 UTC | #3

This would appear like a driver problem. Personally never seen it when running on Linux.

Urho3D uses GLEW for OpenGL extensions. There is the problem that on OpenGL 3 it cannot check extensions properly (as they would always fail) so it can't reliably check if DXT compression is supported. However a driver which would allow running on GL3.2 but didn't support DXT compression would be extremely odd.

Try running with the -gl2 switch to force GL2. On GL2 extensions *should* be checked properly.

There's however one possibility that the conversion from DXT to RGBA (in case DXT isn't supported) has been recently broken. I'll check.

EDIT: Tested DXT -> RGBA decompression to still work properly.

-------------------------

NCrashed | 2017-01-02 01:06:31 UTC | #4

"-gl2" flag fixed the problem. Thank you!

Are there any caveats when using fall back OpenGL2 mode?

-------------------------

cadaver | 2017-01-02 01:06:31 UTC | #5

You don't get to use GL3 niceties, like constant buffers.

In practice the engine used to run on GL2 for years, and only acquired GL3 support this spring, so if anything the GL2 is much more tested.

-------------------------

