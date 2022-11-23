godan | 2017-01-14 18:37:53 UTC | #1

So, I've been thinking about trying to create a little code editor written with (and also for) Urho. After fixing up a [pull request I found](https://github.com/urho3d/Urho3D/pull/1443) and writing some modular window code, I was able to get a pretty decent first draft working:

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/5c8e2daa6cd6285726fb6049f20d6c9b0036747d.gif[/img]

However, this is still a really long way from a functional code editor :) 

Also, a question: How would I go about setting different colors for different characters in a single Text element? Is it possible? I'm fine with writing some additional code at the engine level, but if it's a huge architectural change, then maybe not...

-------------------------

hdunderscore | 2017-01-14 23:07:44 UTC | #2

Thanks for those Multi-line edit changes !

Taking a quick peek, it looks like it would be very simple to have multiple colours by changing `Text::ConstructBatch`, eg:

```C++
for (unsigned i = 0; i < pageGlyphLocation.Size(); ++i)
    {
        const GlyphLocation& glyphLocation = pageGlyphLocation[i];
        const FontGlyph& glyph = *glyphLocation.glyph_;
        pageBatch.SetColor(Color(((i * 5) % 255) / 255.0f, ((i * 15) % 255) / 255.0f, ((i * 25) % 255) / 255.0f));
        pageBatch.AddQuad(dx + glyphLocation.x_ + glyph.offsetX_, dy + glyphLocation.y_ + glyph.offsetY_, glyph.width_,
            glyph.height_, glyph.x_, glyph.y_);
    }
```

With that in mind, it would be good to expose a light-weight multi-colour option (via code), eg: `Text::SetColors(Vector<Color> colors, PODVector<unsigned> colorVector, unsigned firstCharacter = 0)` where in the case of a large file code editor, you would want to use the firstCharacter option to narrow the range and update colours for what can be seen only. I may submit a PR for this.

This could work well even for implementing the classic type-writer effect in many games, by tweaking the alphas on the colours, avoiding the typical word-wrap popping bug of messier implementations.

-------------------------

George1 | 2017-01-15 14:44:48 UTC | #3


I think it is better to leave coding for code editor (e.g. like NotePad++ and others editor...). But instead have the ability to compile multiple files or project scripting files and update or commit changes to these scripts inside Urho3D. This way we don't need to support the code editor feature. 

Multi-line Gui object is good for chat interface, display debug information and useful for in game help information and dialog.

Best

-------------------------

Victor | 2017-01-16 13:11:10 UTC | #4

Very cool! Multi-line text is something I've been meaning to do as well, but I haven't had the time to get around to it. Nice work man! :)

-------------------------

godan | 2017-01-16 15:16:48 UTC | #5

[quote="Victor, post:4, topic:2707"]
Very cool! Multi-line text is something I've been meaning to do as well, but I haven't had the time to get around to it
[/quote]

@Victor Thanks! Just to be clear - the bulk of the code for MultiLineEdit was already done (by@markomiz I think?).

[quote="George1, post:3, topic:2707"]
I think it is better to leave coding for code editor (e.g. like NotePad++ and others editor...).
[/quote]

@George For sure. But I think passable syntax highlighting and formatting isn't out of reach...

-------------------------

godan | 2017-01-16 15:21:23 UTC | #6

@hdunderscore Hmm interesting. Doesn't look too difficult. Presumably `colorVector` defines how many chars to sequentially color with each color in `colors`? 

Would it make any sense in defining a `RichText` class that inherits from `Text`, but that uses bbcode or tags or something to render the chars?

-------------------------

hdunderscore | 2017-01-16 18:31:08 UTC | #7

I think it does make sense to expose some method to load text with formatted code with colors (and maybe later size, boldness etc? although I haven't looked into what would be involved for that).

-------------------------

hdunderscore | 2017-01-17 06:14:53 UTC | #8

Here is an attempt at what I was suggesting, with some example usage in the C++ HelloWorld sample: 

https://github.com/hdunderscore/Urho3D/tree/MultiColorText

-------------------------

godan | 2017-06-01 19:11:35 UTC | #9

Man, syntax highlighting is a pain! Here is a first attempt...

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/551e1cb9208d7be50dbcfd99762102595df13541.jpg'>

-------------------------

godan | 2017-06-01 20:53:54 UTC | #10

One more: here you can see the graph, source, and scene representation of the same object. In this case, an edge renderer...

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/df0f563ce47654a81488860c5e2b1402aaf5a677.jpg'>

-------------------------

