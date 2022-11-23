vivienneanthony | 2017-01-02 01:09:20 UTC | #1

Hello

1. What's the highest and lowest a node ID and component ID can be?  (solved)
2. How in the style .xml you get the background of a window to show up in the stylesheet? 
3. Is PBR available yet in some form? (PBRCoreData, Trying.)
[b]4. How do you prevent Editor.sh and NinjaSnowWar.sh from being created?[/b]

Vivienne

-------------------------

rasteron | 2017-01-02 01:09:20 UTC | #2

[quote="vivienneanthony"]
3. Is PBR available yet in some form?
Vivienne[/quote]

Try this:
[github.com/souxiaosou/UrhoPBRCoreData](https://github.com/souxiaosou/UrhoPBRCoreData)

-------------------------

vivienneanthony | 2017-01-02 01:09:21 UTC | #3

[quote="rasteron"][quote="vivienneanthony"]
3. Is PBR available yet in some form?
Vivienne[/quote]

Try this:
[github.com/souxiaosou/UrhoPBRCoreData](https://github.com/souxiaosou/UrhoPBRCoreData)[/quote]

I'll check it out. Thanks.

-------------------------

vivienneanthony | 2017-01-02 01:09:22 UTC | #4

Hello

Is the component Id valid?

[pastebin.com/PN7NV6NC](http://pastebin.com/PN7NV6NC)

For Example
[code]<component type="TransformComponent" id="-1630470170" />
		<component type="StaticModelComponent" id="-224212233" />[/code]

If I read Urho code right. It's not?

Vivienne

-------------------------

jmiller | 2017-01-02 01:09:22 UTC | #5

[quote="vivienneanthony"]Hello

Is the component Id valid?

If I read Urho code right. It's not?

Vivienne[/quote]
Hello Viv,
I think you're right and those IDs should be unsigned.

-------------------------

vivienneanthony | 2017-01-02 01:09:23 UTC | #6

[quote="carnalis"][quote="vivienneanthony"]Hello

Is the component Id valid?

If I read Urho code right. It's not?

Vivienne[/quote]
Hello Viv,
I think you're right and those IDs should be unsigned.[/quote]

I created this issue on Github.

[github.com/urho3d/Urho3D/issues/1150](https://github.com/urho3d/Urho3D/issues/1150)

I tested my editor adding 146 nodes with 3 components afterward saving and reloading. It was fixed.

Considering that a ID is a unsigned integer both the SaveJSON and SaveXML should be using SetUInt not SetInt

-------------------------

vivienneanthony | 2017-01-02 01:09:24 UTC | #7

Hello

How do I prevent from these two files being generated?

Vivienne

[code]      57 Jan 13 23:27 Editor.sh -> /media/home2/vivienne/Urho3D-Hangars-MyFork/bin/Editor.sh
      63 Jan 13 23:27 NinjaSnowWar.sh -> /media/home2/vivienne/Urho3D-Hangars-MyFork/bin/NinjaSnowWar.sh
[/code]

-------------------------

weitjong | 2017-01-02 01:09:27 UTC | #8

The question is why? But wait, actually I don't want to know. If it is within your own project then you can customize the original build system to your heart's content :wink:  But I have a feeling you are not using it as intended and I guess you have used Urho3D project as the "carrier" for your own project source code. Anyway, these two symlinks are installed when Urho3DPlayer is built and currently there is no way to tell the build system not to build Urho3DPlayer target, unless you modify the Source/Tools/CMakeLists.txt directly to comment it out. Forgive me if my guess is wrong.

BTW, since Urho is an open source project, next time you can just search for it yourself to answer your last question. Finders, keepers.
[code]git grep -A5 -B5 create_symlink |egrep -A2 'Editor|NinjaSnowWar'[/code]

-------------------------

