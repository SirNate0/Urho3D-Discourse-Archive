AntiLoxy | 2019-10-04 19:03:24 UTC | #1

Hello, i recently build this specific editor for two-dimensions world !
This project is done with love and with the idea that it will grow :slight_smile: 

https://github.com/AntiLoxy/Urho2D-Editor

-------------------------

Modanung | 2019-10-03 10:08:25 UTC | #2

Got any screenshots? :slight_smile:

-------------------------

AntiLoxy | 2019-10-03 12:48:16 UTC | #3

Yep !

![0|664x500](upload://eiXv83aiSGNPdjlgYRziB7FkbIC.png) ![2|667x499](upload://nDzCytsL14F9b6JAuB4X0xwGY8Z.png) ![3|665x499](upload://fYbR8uqe1L9zcXSLeyAgo5YgfeX.png) ![4|664x500](upload://7Atf8EkeAbhqTGRiViTfCzvyJC5.png) ![5|666x500](upload://aH2Og65t54kHUWmmLcGrRjrXupf.png) 

You can see on GitHub all futur features that will come when i have the time.

-------------------------

Modanung | 2019-10-03 16:49:21 UTC | #4

Ever heard of [Tiled](https://www.mapeditor.org/)? Urho supports its TMX file format - although this could use an update - it would probably make sense if your editor could load those. As the `TmxFile2D` inherits from `Resource` it should also reload when the `ResourceCache` has auto-reloading enabled and the TMX file is modified.

-------------------------

AntiLoxy | 2019-10-03 17:17:59 UTC | #5

Yes I also think that the support of the tmx map is a good idea, it is also noted on github in future feature, but I also think that it should be limited to static tiles only.

The goal of the editor is precisely to work directly with the Urho3D native format and to avoid the manual transformation of "objects tmx" to "node".
This should contribute to a much clean and lighter game codebase (i hope ^^), no ?

-------------------------

Modanung | 2019-10-03 17:31:01 UTC | #6

I'm not entirely sure what you mean exactly. Tiled is quite a versatile piece of software but as it is engine agnostic your editor could bridge the editorial gap between Tiled and Urho3D.

-------------------------

AntiLoxy | 2019-10-03 17:59:58 UTC | #7

Absolutely. To be honest, for the moment I do not know if it's a good idea, I'll only know when I use it for a project.

-------------------------

