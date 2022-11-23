Hevedy | 2017-01-02 00:58:20 UTC | #1

Migrate from Xml to custom or Json
Because Xml is hard to read and takes much time to load.

Idea #1:
[b]Custom Script:[/b]
Like in Id tech or Cube 2

Example of Material:
Old Snow.xml
[code]
<material>
    <technique name="Techniques/Diff.xml" />
    <texture unit="diffuse" name="Textures/Snow.dds" />
    <parameter name="MatSpecColor" value="0.25 0.25 0.25 16" />
</material>
[/code]

New Snow.mtr (MaTeRial .mtr)
[code]
/*
Multiline Comment
*/
//Line Comment
Material Snow {
   //Here add maps and types and def of map (collisions, twosided, impacts...)
   Technique Techniques/Diff.tch
   Diffusemap Textures/Snow.dds
   Specularmap 0.25 0.25 0.25 16
}
[/code]

Old MatBody.xml
[code]
<?xml version="1.0"?>
<material>
	<technique name="Techniques/DiffNormalSpecAlphaMask.xml" quality="0" loddistance="0" />
	<texture unit="diffuse" name="Textures/Nyra/body_d.png" />
	<texture unit="normal" name="Textures/Nyra/body_n.png" />
	<texture unit="specular" name="Textures/Nyra/head_s.png" />
	<texture unit="environment" name="Textures/Nyra/reflect.png" />
	<parameter name="UOffset" value="1 0 0 0" />
	<parameter name="VOffset" value="0 1 0 0" />
	<parameter name="MatDiffColor" value="0.4 0.4 0.4 1" />
	<parameter name="MatEmissiveColor" value="0 0 0 1" />
	<parameter name="MatEnvMapColor" value="1 1 1" />
	<parameter name="MatSpecColor" value="0.5 0.5 0.5 384.314" />
	<cull value="ccw" />
	<shadowcull value="ccw" />
	<depthbias constant="0" slopescaled="0" />
</material>
[/code]

New MatBody.mtr
[code]
Material MatBody {
   Technique Techniques/DiffNormalSpecAlphaMask.tch {
      Quality 0
      Loddistance 0
   }
   Diffusemap {
      Map Textures/Nyra/body_d.png
      Color 0.4 0.4 0.4 1
   }
   Normalmap Textures/Nyra/body_n.png
   Specularmap {
      Map Textures/Nyra/head_s.png
      Color 0.5 0.5 0.5 384.314
   }
   Emissivemap 0 0 0 1
   Environmentmap {
      Map Textures/Nyra/reflect.png
      Color 1 1 1
   }
   UOffset 1 0 0 0
   VOffset 0 1 0 0
   Cull_0
   Shadowcull_0
   Depthbias {
      Constant 0
      Slopescaled 0
   }
}
[/code]


Idea #2:
[b]Use Json[/b]

-------------------------

aster2013 | 2017-01-02 00:58:20 UTC | #2

Currently, we use Pugixml, if you fell is slow on loading, You can replace it with RapidXml ([url]http://rapidxml.sourceforge.net/[/url]).

But as I know, C++ Json parser is slower than xml parser,  the fastest Json parser call RapidJson ([url]https://code.google.com/p/rapidjson/[/url]).

-------------------------

weitjong | 2017-01-02 00:58:20 UTC | #3

Don't forget we use pugixml library not only for its XML parser but also for its XPath implementation. So, any replacement should address for both needs. Although there are XPath equivalent implementation for JSON, there is no standard at all unlike XPath. Urho3D uses XPath query in a few places. IMHO, we should focus our energy on other area than this.

-------------------------

cadaver | 2017-01-02 00:58:21 UTC | #4

When I profiled scene and XML loading, the most significant CPU hotspot I remember was the parsing of floats from string data, for example Vector3's. Moving away from XML would not change this. Rather, large data files like scenes / object prefabs should be binary in a final production.

-------------------------

Hevedy | 2017-01-02 00:58:21 UTC | #5

[quote="cadaver"]When I profiled scene and XML loading, the most significant CPU hotspot I remember was the parsing of floats from string data, for example Vector3's. Moving away from XML would not change this. Rather, large data files like scenes / object prefabs should be binary in a final production.[/quote]

How you profile? What use ?

-------------------------

cadaver | 2017-01-02 00:58:21 UTC | #6

AMD CodeAnalyst.

-------------------------

Hevedy | 2017-01-02 00:58:21 UTC | #7

[quote="cadaver"]AMD CodeAnalyst.[/quote]

Work that with Intel/Nvidia ?
I think would be nice add to the engine some debug/profiler like this [freesdk.crydev.net/display/SDKDO ... ling+Tools](http://freesdk.crydev.net/display/SDKDOC2/Debugging+and+Profiling+Tools)
Ty.

-------------------------

cadaver | 2017-01-02 00:58:21 UTC | #8

CodeAnalyst works with Intel CPU's in a limited fashion. You can get the percentage of time spent in parts of code, which is often the most important knowledge. On AMD CPU's it also shows hardware counters like cache misses etc.

Urho3D already has its own hierarchic execution time profiler, which is already used quite extensively in the engine (F2 to show it in the examples). In addition there are some additional profiling/dumping functions in Engine class, but they're not always usable, for example the memory allocation dump works only in MSVC debug mode.

Total rewrite of memory allocations to always go through a custom memory allocation profiler is not planned.

-------------------------

aster2013 | 2017-01-02 00:58:52 UTC | #9

I will add JSON support before next release. But I don't want to replace current xml data file. If you like, you can use JSON for your custom data file.

-------------------------

Hevedy | 2017-01-02 00:59:09 UTC | #10

[quote="aster2013"]I will add JSON support before next release. But I don't want to replace current xml data file. If you like, you can use JSON for your custom data file.[/quote]

Oh nice thanks. But is ready to read the materials and others ?

-------------------------

OvermindDL1 | 2017-01-02 00:59:21 UTC | #11

I am unsure if a C++ lib exists for it, but I would recommend hocon over JSON.  It is a strict superset of JSON, but allows for includes, more readable formatting, comments, etc.  The 'spec', is at [github.com/typesafehub/config/b ... r/HOCON.md](https://github.com/typesafehub/config/blob/master/HOCON.md) and it is very much used in the java world now at least, it is definitely superior to JSON while being a strict superset, thus JSON works as-is with it.

Something that is not JSON based but is very powerful, very fast, easy, succinct, type safe(woo!) with many useful features (including comments) that is a C++ lib is:  [hyperrealm.com/libconfig/](http://www.hyperrealm.com/libconfig/)
It is lgpl thankfully.

-------------------------

cadaver | 2017-01-02 00:59:21 UTC | #12

LGPL libraries are not OK for Urho3D, as we need to be able to compile into static libraries on iOS, and embed into .apk's on Android, and both scenarios don't readily allow the user to replace the library in question. We can take only permissive licenses with no restriction on static linking (BSD/MIT/Apache etc.)

-------------------------

jorbuedo | 2017-01-02 00:59:33 UTC | #13

How about using Lua itself? It's already in use for the scripting. You can find a lot of discussions on using it instead of xml on google.
The parser it's the lua interpreter itself so it's already in the engine and it's as fast as a parser can be. The data has a nice syntax, and as it is a programming language you have much more flexibility. The only drawback is that you have to validate it, as it may include harmful executable code, but there are things done for that already. 


    Entry{
      author = "Donald E. Knuth",
      title = "Literate Programming",
      publisher = "CSLI",
      year = 1992
    }
    
    Entry{
      author = "Jon Bentley",
      title = "More Programming Pearls",
      publisher = "Addison-Wesley",
      year = 1990
    }

[lua.org/pil/12.html](http://www.lua.org/pil/12.html)

-------------------------

cadaver | 2017-01-02 00:59:33 UTC | #14

Otherwise a good idea, but Urho3D also needs to work without Lua (pure C++ or AngelScript use cases)

-------------------------

