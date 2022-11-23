NoobBeggar | 2022-06-17 04:59:43 UTC | #1

I'm not a Urho3d guy; I just need to convert files. I have *no* idea what I'm doing, but it would be helpful to have a one-on-one convo with someone who knows how to use Urho3d.

I want to export .fbx to .ani according to this tutorial:
http://teamfriesen.com/blog/2013/09/07/finally.html

To launch Urho3D, I go to the bin folder and click the "Editor" batch file. I get the message:
 "Windows cannot find... Urho3D-1.7.1\bin\Urho3DPlayer_D"

Apologies for being clueless. I wish you guys had a Discord; It would be easier to chat in real-time.

-------------------------

Eugene | 2022-06-17 11:55:17 UTC | #2

[quote="NoobBeggar, post:1, topic:7281"]
Apologies for being clueless. I wish you guys had a Discord; It would be easier to chat in real-time.
[/quote]

There is Urho-related Discord server. It's "unofficial", but it's decently active.
https://discord.gg/XKs73yf

[quote="NoobBeggar, post:1, topic:7281"]
I’m not a Urho3d guy; I just need to convert files.
[/quote]
Just curious, *why* do you need to convert files to Urho format if you are not Urho3D guy? It may or may not be XY problem.

-------------------------

1vanK | 2022-06-17 12:31:54 UTC | #3

AssetImporter is ugly and incomplete. You can use Blender plugin for convert fbx files

<https://discourse.urho3d.io/t/exporting-materials-from-blender-2-83-to-urho3d/5845>

-------------------------

NoobBeggar | 2022-06-17 22:18:51 UTC | #4

I'm modding a game that only takes primitive/obsolete animation types. I can "get around" this problem via the .ani format, thanks to some programming work done by the community. 

Urho3d is the only software I found that seems to convert .fbx to .ani.

-------------------------

1vanK | 2022-06-17 23:41:33 UTC | #5

Urho3d uses own custom file formats (including .ani). Are you sure that your game is on the Urho3D engine?

-------------------------

NoobBeggar | 2022-06-18 18:44:04 UTC | #6

The game is *Carnivores: Dinosaur Hunter*. I don't know what engine it uses, but the community editor allows modifications with the .ani animation type. Here is an example of the .ani files I'm working with: 

https://drive.google.com/file/d/140ovPaiJYUfSWD6kiQjubOlLTnLMapfv/view?usp=sharing

-------------------------

JTippetts1 | 2022-06-18 21:11:14 UTC | #7

.ani isn't a standard format. It is highly unlikely that the .ani format you need matches Urho3D's .ani format.

-------------------------

NoobBeggar | 2022-06-18 21:45:12 UTC | #8

Well there's gotta be a way to find out.

If you can, please describe the function of a Urho3d .ani file. Is it a fully animated model, or animation information for an existing model? Does it contains mesh/skeleton information, or only vertex information? How about textures?

-------------------------

1vanK | 2022-06-18 23:00:53 UTC | #9

https://urho3d.io/documentation/HEAD/_file_formats.html

-------------------------

SirNate0 | 2022-06-19 02:53:04 UTC | #10

The Urho3D .ani files are just the animation information, not the textures and vertex data. In your words, it is
[quote="NoobBeggar, post:8, topic:7281"]
animation information for an existing model
[/quote]
and the link @1vanK provided describes it in greater detail.

-------------------------

NoobBeggar | 2022-06-19 03:42:13 UTC | #11

Sounds like the same kind of .ani I'm working with. Fingers crossed.

-------------------------

Eugene | 2022-06-19 10:16:18 UTC | #12

This file doesn’t start with UANI magic word, so it’s not the same format

-------------------------

NoobBeggar | 2022-06-19 18:02:49 UTC | #13

Thank you! That saves me a lot of time.
How did you view the file source code?

-------------------------

SirNate0 | 2022-06-20 16:21:59 UTC | #14

If you open the file in a hex editor you will see that the first 4 bites of the file you provided are "0C 00 00 00", which are not representable in ASCII. If you instead open one of Urho's .ani files you will see that the first four bytes are "55 41 4E 49" which correspond to ASCII "UANI", the `byte[4]    Identifier "UANI"` from the documentation. Hence your file is not an Urho .ani file.

Technically, you can probably get away with a regular plain text editor to view it, as it will probably just skip the non-representable characters and still show the good ones, so if it does start with UANI it should still look like that in a text editor. For example:
![image|158x43](upload://f0dCAPSmJ1GBeIEFNJc80tZ9wPq.png)

-------------------------

