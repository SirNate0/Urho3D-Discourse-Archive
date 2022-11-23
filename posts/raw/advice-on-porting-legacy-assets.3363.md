lazypenguin | 2017-07-16 18:16:12 UTC | #1

Hey all, I'm starting to dive into Urho3D and my project is porting of an old 3D game to this engine. My question is mostly engine-agnostic but since I have decided to use Urho3D I thought I would seek advice here. 

The old game has a significant amount of assets (textures, models, animations, skeletons, terrain, etc.) stored in proprietary binary file formats. The formats are known so there is no issue in reading them but there are a lot of internal references to the files (e.g. model references texture file by relative path string). I've narrowed down my options to 2 options but I am curious what the community thinks and if maybe there's an option I've missed.

1) Should I keep the legacy file formats/file hierarchy and implement custom loaders that will convert from these file types to Urho3D's file types at runtime?

or

2) Should I do some work ahead-of-time to convert these assets to Urho3D friendly formats in the spirit of the Assimp/Blender converters? (e.g. build a scene XML file, build a .mdl, etc.)

Would appreciate any insights, thank you!

-------------------------

S.L.C | 2017-07-16 19:06:23 UTC | #2

If I knew I was going to stay with Urho3D and not switch to another engine. I'd go with the second option. Much easier to maintain and be consistent. At least that's how it seems to me.

-------------------------

jmiller | 2017-07-17 13:00:16 UTC | #3

Proactively lazy penguin, thinking like S.L.C.
 :penguin:
Open formats like Urho uses (XML) lend themselves well to all sorts of things, and you get to avoid runtime conversions.

-------------------------

lazypenguin | 2017-07-17 21:32:21 UTC | #4

> Proactively lazy 

Always ;)

I think you guy are right. I spent a couple of hours writing a terrain converter and imported it into Urho I'm already convinced this strategy is better like you said. Rather than fighting with the internals of Urho I can just hand it my image resource and let it do all its magic.

-------------------------

