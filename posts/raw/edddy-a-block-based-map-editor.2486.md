Modanung | 2019-07-02 18:36:58 UTC | #1

https://luckeyproductions.itch.io/edddy

I've been working on [Edddy](https://gitlab.com/LucKeyProductions/Edddy), a map editor that allows you to create worlds using pre-made sets of blocks. If you want to give it a try, you can find the controls [here](https://gitlab.com/luckeyproductions/Edddy/blob/master/Docs/Instructions.md).
Its intended use is to build maps for [A-Mazing Urho](https://gitlab.com/luckeyproductions/AmazingUrho), [KO](https://gitlab.com/LucKeyProductions/KO), [OGTatt](https://gitlab.com/LucKeyProductions/OGTatt) and [Blip 'n Blup](https://gitlab.com/LucKeyProductions/BlipNBlup). Edddy draws inspiration from [Blender](https://www.blender.org/), [Tiled](http://www.mapeditor.org/) and other open creation software.

https://gitlab.com/luckeyproductions/Edddy/raw/master/Screenshots/Screenshot_2018-11-11_00-40-25.png

-------------------------

Lumak | 2017-01-02 01:15:45 UTC | #2

Looks good, Modanung! Why do you prefer GPL over MIT.  Is it so you can split the license into commercial and free, like Qt lib, in the future?

-------------------------

rasteron | 2017-01-02 01:15:47 UTC | #3

Nice one Modanung! Keep it up :slight_smile:

-------------------------

Modanung | 2017-01-02 02:11:54 UTC | #4

[quote="Lumak"]Looks good, Modanung! Why do you prefer GPL over MIT.  Is it so you can split the license into commercial and free, like Qt lib, in the future?[/quote]
I must say I'm not very outspoken about either. But if I understand correctly MIT allows changing of the license which allows for proprietary forks without notice. I do not like the idea of that. Also its part copycat behaviour since a lot of software I use and like carries the GPL license. Like Blender, GIMP, Inkscape, SuperCollider, Tiled, etc..

Would you rather see it licensed MIT? If so, why?

Blip 'n Blup can now load the levels, btw. :slight_smile:
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/2ee5e78e7883e263bd478ef0511909867d24c4e0.png[/img]

-------------------------

jmiller | 2017-01-02 01:15:49 UTC | #5

Nice work! I can see this being useful to people. :slight_smile:

Edddy builds as a standard Urho app and runs fine on Arch here.

If you consider licenses, there is also the LGPL. You can make your own arguments, I only mention it.

-------------------------

Lumak | 2017-01-02 01:15:49 UTC | #6

[quote]Would you rather see it licensed MIT? If so, why?[/quote]

It's your prerogative to license it however you see it fit, doesn't matter what anyone else wants.

Coincidentally, I opened one of your source files and found the answer.
[quote]
/* Edddy
// Copyright (C) 2016 LucKey Productions (luckeyproductions.nl)
//
// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation; either version 2 of the License, or
// (at your option) any later version.
// Commercial licenses are available through [frode@lindeijer.nl](mailto:frode@lindeijer.nl)

[/quote]

-------------------------

Modanung | 2019-05-01 12:27:16 UTC | #7

[quote="Lumak"]
It's your prerogative to license it however you see it fit, doesn't matter what anyone else wants.
[/quote]

I think it does matter since picking a certain license might discourage people from contributing. Also I might not be fully informed or have overlooked use cases.
[quote="Lumak"]
Coincidentally, I opened one of your source files and found the answer.
[quote]
// Commercial licenses are available through [frode@lindeijer.nl](mailto:frode@lindeijer.nl)
[/quote]
[/quote]

Thanks for reminding me I put that there, it is outdated information. LucKey Productions is a non-commercial operation although [url=https://www.patreon.com/LucKeyProductions]donations[/url] will help it thrive... to support myself (and fellow LucKey Devels) and to finance LucKey Orifices and LucKey Gatherings. My main drive is to propagate the idea of open source and to brainwash the world for the better.
My services as a puterdoc and pipe maker are of a more commercial nature.

-------------------------

Modanung | 2019-07-02 01:04:45 UTC | #8

The changes I made to Edddy reached a point where I decided it's time to update the binary on itch. It still needs a lot of work, but it is theoretically usable and already arguably more efficient than the default Urho editor when used for certain projects. Although it's features are still somewhat limited. :slight_smile: 

https://luckeyproductions.itch.io/edddy

![Screenshot_2019-07-02_02-15-10|689x454](upload://5xPJzShktxi0MYI1Dl1sPz3zLLq.jpeg) 

![Screenshot_2019-07-02_03-02-56|690x388](upload://zdaA8YCjAo30z5pRgwk1X5GAsM3.jpeg)

-------------------------

WangKai | 2019-07-02 07:39:47 UTC | #9

The top view is better if it can be Orthographic :wink:

-------------------------

Modanung | 2019-07-02 19:21:50 UTC | #10

Actually view orthogonality is only temporarily dysfunctional. The key for toggling it got disconnected - along with all other existing input - during the implementation of the new (Qt) GUI; most of the required methods are already there. But first my forearm needs a rest. So for now all the other (new) functionality should do. ;)
Including but not restricted to:
- Creation of projects (.edy file, used by Edddy)
- Creating new maps (.emp) and blocksets (.ebs)
- Editing maps (only grid-blocks for now) and blocksets
- Saving, loading and deleting
- Brush (single block or line)
- Fill tool (flood plane)
- Undo/Redo

Blocks are currently limited to having only a single (preexisting) material. All formats are XML-based.

-------------------------

Modanung | 2019-07-13 02:28:51 UTC | #11

Blocks can now have a different material for each geometry:
![Grunnstatt](https://img.itch.zone/aW1nLzIyNzYzMDIucG5n/original/kjSrqM.png)

-------------------------

HeadClot | 2019-07-17 23:29:02 UTC | #12

Hey @Modanung - Bit a few requests for this tool. I am using this with Unreal Engine. BTW I love this tool. Would it be possible to get the ability to export the scene a .FBX or some other file format that is compatible with UE4?

Also custom export profiles for other engines such as UE4, Unity3D, etc. for exporting the scene would be nice. Being able to set scale. Up Axis, etc. depending on the engine.

Also some windows binaries would be nice so I do not have to build it from source :slight_smile:

-------------------------

Modanung | 2019-07-18 10:22:37 UTC | #13

Good to hear you find it useful. :slightly_smiling_face: 
I plan to integrate the AssImp to make Edddy careless about model formats (and I guess other coordinate systems). But there's many other features - like area selection, copy-paste and clusters - that I consider to be of higher priority.

[quote="HeadClot, post:12, topic:2486"]
Also some windows binaries would be nice so I do not have to build it from source :slight_smile:
[/quote]
I'm sorry, LucKey Productions does not condone spyware. Have you considered installing Linux instead?

-------------------------

HeadClot | 2019-07-18 10:37:20 UTC | #14

[quote="Modanung, post:13, topic:2486"]
I plan to integrate the AssImp to make Edddy careless about model formats (and I guess other coordinate systems). But there’s many other features - like area selection, copy-paste and clusters - that I consider to be of higher priority.
[/quote]

How much would it cost to prioritize Assimp support? I could really use support for other file formats. :)

-------------------------

Miegamicis | 2019-07-18 11:49:09 UTC | #15

Case of beer, donations are also good.

-------------------------

HeadClot | 2019-07-18 12:28:54 UTC | #16

If this is the case I can do it come Monday. :slight_smile:

-------------------------

Modanung | 2019-07-18 13:02:27 UTC | #17

[quote="HeadClot, post:14, topic:2486"]
How much would it cost to prioritize Assimp support?
[/quote]
You're more than welcome to [donate](https://www.luckeyproductions.nl/donate.html). But rather than *changing* my priorities at this point I think it would simply motivate me to work faster, next to being grateful. Whether you donate or not won't change the fact that I *will* take your wish into consideration.
[quote="Miegamicis, post:15, topic:2486"]
Case of beer
[/quote]
I do not consider ethanol fit for human consumption. :P
Or are you offering to colaborate?

-------------------------

HeadClot | 2019-07-18 12:47:08 UTC | #18

[quote="Modanung, post:13, topic:2486"]
I’m sorry, LucKey Productions does not condone spyware. Have you considered installing Linux instead?
[/quote]

I just installed Chrome OS on a laptop which has support for Linux binaries. So I will let you know if it works on there.  :slight_smile: 

[quote="Modanung, post:17, topic:2486"]
You’re more than welcome to [donate](https://www.luckeyproductions.nl/donate.html). But rather than *changing* my priorities at this point I think it would simply motivate me to work faster. Whether you donate or not will not change the fact that I *will* take your wish into consideration.
[/quote]

OK, got it. :slight_smile:

-------------------------

Miegamicis | 2019-07-18 13:10:02 UTC | #19

What substances you approve of? 

And sadly I'm not offerring any collaboration at the moment but that might change in the future. Haven't actually tried your project, but I'm planning to try it out at some point.

-------------------------

