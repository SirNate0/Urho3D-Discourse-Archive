brojonisbro | 2019-09-17 10:01:31 UTC | #1

urho3d read completly hex dumped files?

example: 
i got a 3dmodelcharacter.dae (collada) or any other file (.txt) and i use xxd:

xxd -i 3dmodelcharacter.dae 3dmodelcharacter.h

:to convert collada to hex dump header

how can i make urho3d read the models and animations by this?

-------------------------

johnnycable | 2019-09-13 15:26:06 UTC | #2

Here. [AssetImporter](https://urho3d.github.io/documentation/HEAD/_tools.html) is your lead.

-------------------------

brojonisbro | 2019-09-14 15:12:15 UTC | #3

but it will convert the model or any file to a urho3d specific file, right?
i was to get it reading from the header hex dump byte arrays, directly

3dmodelcharacter.h
bla bla bla byte[] array bla bla bla
(loading with collada or etc)

but if its impossible , ok! : /

-------------------------

Leith | 2019-09-13 23:06:08 UTC | #4

A custom Urho resource may be a way to read foreign file formats directly into Urho, but I don't think it will be a trivial exercise - nonetheless, as Johnny pointed out, the AssetImporter sourcecode will likely be invaluable as a reference to constructing Urho objects in memory from foreign data.

-------------------------

johnnycable | 2019-09-14 14:54:16 UTC | #5

Sure thou. If no format in asset importer is good for you, then you have a custom format, and in binary. Then you have to create your own importer.

-------------------------

brojonisbro | 2019-09-14 15:10:53 UTC | #6

thx for information ppls ^^

yesterday searching about tihs, i find this little tutorial : 

[CPP / C++ - Embed Resources Into Executables]
https://caiorss.github.io/C-Cpp-Notes/resources-executable.html

i'll try to use this and what u guys said to find a solution, thx again!

-------------------------

Valdar | 2019-09-17 03:25:16 UTC | #7

I feel like I must be missing something, but I’m not sure why you are trying to do a hex dump of an existing model. If you have a model in virtually any format, you can use the standalone version of AssImp (found in the tools folder) to convert to mdl. From there all you have to do is reference the .mdl file in your code to use it. [s]If you also want to embed the model file into your project’s executable, you can use Urho’s built-in packaging mechanism. Just build Urho from source with CMake and tick the URHO3D_PACKAGING  box. All your models should get packed into your EXE file automatically (at least if you are using C++)[/s]

-------------------------

brojonisbro | 2019-09-16 10:23:28 UTC | #8

Hey, thanks, i'll take a look at this but
URHO3D_PACKAGE isnt about .pak files? Its not embed on the exe O.o
I'm trying to do this not just for models, "models" were just examples cause the file is, based what i see on 3d ripper forums, to read is a complicated hex file

-------------------------

Valdar | 2019-09-16 12:57:20 UTC | #9

> URHO3D_PACKAGE isnt about .pak files?

I stand corrected, it is held in a separate package file. I should have double-checked my facts (that's what I get for tinkering with too many engines) :slight_smile:

-------------------------

Modanung | 2019-09-16 16:51:36 UTC | #10

Maybe you could use Qt's [rcc](https://doc.qt.io/qt-5/rcc.html)? Just a (little explored) though.

-------------------------

brojonisbro | 2019-09-16 16:59:36 UTC | #11

I think that's it! Thanks!!! :slight_smile:

* * insert a meme thank you gif here

-------------------------

Modanung | 2019-09-16 17:16:37 UTC | #12

Maybe you could make a little how-to of sorts once you have it working? I bet others would like to read it.

-------------------------

brojonisbro | 2019-09-16 18:11:05 UTC | #13

(What is written below was with the help of Google Translate that I used to better express myself, giving a little fix on some words)

As I am learning (newbie), I may be completely wrong with what I am going to write now, but I still hope to try or see if it works.
I haven't tested it yet but I would also like to share the idea, maybe you or someone else can and I don't.

So ... currently I would not have a complete solution on how to do this in QT, and would have to research more about this tool even though it seems a much easier solution, but with GCC and xxd I could already talk because I already have two (or at least i think).

First (i think its trash):
It's easier, but I think it could go wrong and its a little bit non-sense and noob. (You can jump and read the second if u want, marked **BOLD**, but still interesting)

Using the Collada library as a PARSER itself and simply call the file in HEX Header and try to read from there.
In some engines for example some people usually just rename, change extension, change a part of HEX and obfuscate a part of a file to another random, so people who extract can not read the file directly by Blender or image reader. And people think it's a new binary (or would we be creating one from Collada?)

**Second:** (Bingo?)

**For example, not only knowing the name and how to call the file using the Collada library, but learning how it works in the extension (we can easily read a Collada file with Kate, for example), source code and using this understanding to try to understand in HEX. .**

**We would be doing the same process if we were to extract a 3D model from an AAA game, open the Collada with Bless (Hex Editor) or Radare2-Cutter (Radare2 GUI version) file and try to understand it from there and then PARSER it. archive.**
**It may seem complicated or costly performance, but the intention is to protect some important or SECRET file or character. Doing this and using imagemagick to convert image to header image would also include in the binary (more performance loss?), which would increase the size and weight of the game, using more RAM / VRAM and more CPU to open the game but protecting something important.**

I don't know if I'm thinking too high, but as programming 99.9% of things are possible, why not?

I'll try,or i don't know. LOL

-------------------------

Modanung | 2019-09-16 18:35:16 UTC | #14

Personally I'm not that interested in hiding data (surely others are), but the ability to include immutable resources within the binary *does* seem enticing. If only because it simplifies distribution and installation.

-------------------------

Valdar | 2019-09-17 03:30:37 UTC | #15

I’ll be interested in obfuscation, if and when I have something good enough to hide. :laughing:  I think anyone using Urho commercially would want that ability. Not suggesting it should be in Core, but a plugin would be nice.

It was once common for executables to carry data payloads, especially simple programs. It made it a lot easier to transfer a single file over modems, so it’s definitely feasible. The problem is that the size could get huge with modern multiple levels, and you’d lose the ability to easily load and off-load  scenes, and models.

A better approach might be to just obfuscate the data files. I haven’t given it a lot of thought yet, but It shouldn’t be too difficult. A simple and cheap technique could be to use an external MDL file, but do bit shifts and/or increments/decrements on each byte and re-write the files(s) for production. You could use an advanced encryption algorithm instead if you regarded your work that highly, but it would more costly. Then, modify the Urho code to reverse the process when the file is read from disk so that the result in memory is your original model. I’m guessing that the code alteration would be done in the resource cache, but I’m not nearly familiar enough with the engine to do this. Maybe one of the long-time users could chime in on this. Anyway, just some food for thought.

-------------------------

Leith | 2019-09-17 05:44:10 UTC | #16

Obfuscation of what exactly?
Code?
Scripts?
Should we use stenographic techniques?
Do we subscribe to principles of DLC?
It's a minefield, who holds the keys? etc.
I have experience in cryptography, and cyphers in general, including blockchain cyphers, courtesy of my friend kevin, who works for the signals department of the us navy

-------------------------

Modanung | 2019-09-17 08:24:14 UTC | #17

[quote="Valdar, post:15, topic:5576"]
I think anyone using Urho commercially would want that ability.
[/quote]

Commercially is not the same as proprietary, although they often go together this is not always the case.
Someone could be secretive about their freeware.

-------------------------

Valdar | 2019-09-17 09:00:25 UTC | #18

[quote="Modanung, post:17, topic:5576, full:true"]
[quote="Valdar, post:15, topic:5576"]
I think anyone using Urho commercially would want that ability.
[/quote]

Commercially is not the same as proprietary, although they often go together this is not always the case.
Someone could be secretive about their freeware.
[/quote]

I'm well aware of the definitions of 'commercially' and 'proprietary' and wasn't claiming that they are the same, nor was I implying that authors of freeware **wouldn't** desire obfuscation. I only meant that it would be necessary for commercial use.

-------------------------

Modanung | 2019-09-17 09:50:35 UTC | #19

[quote="Valdar, post:18, topic:5576"]
I only meant that it would be necessary for commercial use.
[/quote]
It isn't. Open source software can be commercialized.

Generally things can be hacked and backwards engineered. It is the license that makes it illegal or not to reuse another person's assets. If you're going for the money, it's probably most profitable to *not* encode your assets and sue anyone that uses them illegally.

-------------------------

brojonisbro | 2019-09-17 10:06:41 UTC | #20

i don't now if i'm getting this talk wrong but...

Calm down guys, u guys are mixing and fighting all about:

Premium vs Free
OpenSource vs ClosedSource

Its a question of opnions, its hard to explain and maintain a asnwer for this

I have to agreed and decline somethings here, but i'm pratically, to create a game, like Platinum Games.
(Bayonetta's Extensions) Own package files, secrets into binary on pc version, own text file, own animation file, compressed, obfuscated and packaged just to protect the game, having Copyright or not

We're all open source aspiring guys but sometimes we need protect something, why not?

-------------------------

Valdar | 2019-09-17 11:08:41 UTC | #21

I’m calm :relaxed: I just don’t see the point in arguing the semantics of the words ‘commercial’ or ‘necessary’.

Sure, almost anything **can** be reverse engineered, but it takes effort. Logically, the greater the effort required, the greater the deterrent.

I disagree that it is “most profitable to not encode your assets and sue anyone that uses them illegally”. Legal fees, lost revenue, lost time, the burden of proof, the likelihood of dealing with international laws, are all reasons to **avoid** having to sue. If you are Epic, you can afford to open your source and take that risk. Indie developers don’t have that luxury. Even in Epic’s case, they opened their source to make it more attractive to people to use the product, not so they could sue people.

Sorry,  [**brojonisbro** ](https://discourse.urho3d.io/u/brojonisbro), I wasn’t trying to hijack your thread, only to help. I completely agree with you that sometimes our work needs protecting.

-------------------------

Modanung | 2019-09-17 11:25:23 UTC | #22

Indeed we are somewhat off-topic here.
I believe you may be applying physical logic in a virtual environment, or at least one differing from mine.  Allowing your assets to bleed out, as it were, can form trails that lead people back to your full product. Hobbyists would basically provide you with free marketing. This does not require freedom beyond personal use but _is_ hampered by the encryption of assets.

-------------------------

johnnycable | 2019-09-17 14:48:32 UTC | #23

Was checking the same for some project of mine. Found:

https://github.com/fritzone/obfy

That hides the code, which in turn needs to be hidden otherwise they'll reverse engineer your data reader...

-------------------------

Valdar | 2019-09-17 14:59:23 UTC | #24

[quote="Modanung, post:22, topic:5576, full:true"]

Allowing your assets to bleed out, as it were, can form trails that lead people back to your full product. Hobbyists would basically provide you with free marketing. This does not require freedom beyond personal use but _is_ hampered by the encryption of assets.
[/quote]

We’re actually closer in opinion on this one. For example, the popularity of the girls from DOA has made a lot of people aware of the game that might not have heard of it otherwise. I’ve even heard of devs putting their own games on Pirate Bay to promote themselves. That may not be a terrible idea. One could argue that a huge percentage of the pirates would have never purchased the game anyway.

But then there are situations like this one regarding the [theft of the game Raft](https://steamcommunity.com/app/648800/discussions/0/1643166649104433378/). Looking at the details of both games and the user comments, it appears that the competitor’s product is a blatant copy. Raft makers are definitely losing money over that one, but is it worth suing? Probably not.

All things considered, I’ll personally still try to mitigate the theft of my intellectual property (at least the source code and assets). If a few people pirate the finished product, like it, and spread mass awareness, that might not piss me off as much :laughing:

-------------------------

Valdar | 2019-09-17 15:13:16 UTC | #25

Thanks, @johnnycable. I just skimmed it and it looks interesting for obfuscating the code. I'll have a closer look tomorrow.

BTW, since the OP brought it up; I’d still like to hear from anyone who knows the engine internals well regarding the best way to use encrypted resource files (given the encryption method of course). Would it be as simple as reading the encrypted file, decrypt, and pass to the resource cache, or am I completely on the wrong track?

-------------------------

SirNate0 | 2019-09-18 16:45:49 UTC | #26

That path is what I would go with. Read the file, probably as some byte array, pass to the decryption library, which probably returns a byte array, and then store that in a VectorBuffer (or hold on to it separately and use a MemoryBuffer), load the resource with it, and then add it as a manual resource to the resource cache. If you have a lot of files you need to load like this you might consider modifying the ResourceCache or File to handle your encrypted files behind the scenes so that you can just use the resource cache like normal. If you want to go down that road, I have a branch that supports multiple types of file sources for the resource cache (see [this pull request](https://github.com/urho3d/Urho3D/pull/2210/files) and [this example with a gzip file source](https://github.com/SirNate0/Urho-GZIP-File-Source)) if you want some inspiration (or want to use the code directly).

-------------------------

Valdar | 2019-09-21 12:00:24 UTC | #27

@SirNate0 , that looks very similar to what I was looking for. Thanks for the info, definitely inspirational!

-------------------------

