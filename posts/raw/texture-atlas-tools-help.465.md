practicing01 | 2017-01-02 01:00:39 UTC | #1

Hello, I'm new to this engine and would like to make 2D and 3D games with it.  The Urho2D page of the documentation tells of a few tools I can use to create texture atlases.  I'm on 32bit linux so I can't use texturepacker or shoebox.  I tried darkFunction Editor but the output doesn't look similar to the coin example provided, is the format still usable?  Are there any other options, thanks for any help.

-------------------------

gwald | 2017-01-02 01:00:39 UTC | #2

[quote="practicing01"]Hello, I'm new to this engine and would like to make 2D and 3D games with it.  The Urho2D page of the documentation tells of a few tools I can use to create texture atlases.  I'm on 32bit linux so I can't use texturepacker or shoebox.  I tried darkFunction Editor but the output doesn't look similar to the coin example provided, is the format still usable?  Are there any other options, thanks for any help.[/quote]

Hi wecome!
Yes, your right the 2D tilemap is not right in 32bit (mint linux) also, I did a youtube video of the samples and it's just the green grass layer no water.
For 2D tiles I read the document page supports tiled (great program!) it's on github, uses QT if I remember correctly.

-------------------------

practicing01 | 2017-01-02 01:00:39 UTC | #3

I'm looking for a tool that creates atlases in the format Urho3D can read.  The tilemap example works fine for me, I see both grass and water.

-------------------------

friesencr | 2017-01-02 01:00:39 UTC | #4

this tool [darkfunction.com/editor/](http://darkfunction.com/editor/) run on java

-------------------------

practicing01 | 2017-01-02 01:00:39 UTC | #5

I tried darFunction editor.  The xml output is invalid to urho3d.  Am I doing something wrong?

-------------------------

thebluefish | 2017-01-02 01:00:39 UTC | #6

Make sure that you're exporting in starling/sparrow format, most tools usually output to some other format by default.

-------------------------

practicing01 | 2017-01-02 01:00:39 UTC | #7

darkFunction Editor doesn't have options to change the output type in any of the menus.
[img]http://s27.postimg.org/ehu4wznrn/Screenshot_from_2014_10_04_00_17_49.png[/img]

-------------------------

Mike | 2017-01-02 01:00:39 UTC | #8

DarkFunction Editor exports in its own xml format that you can't easily customize. You will have to manually edit the exported file to match Starling/Sparrow format (the format used by Urho). From what I remember, only ShoeBox and TexturePacker allow direct export to Starling/Sparrow.

For Ubuntu32 there's an old build of TexturePacker available at [url]https://www.codeandweb.com/texturepacker/download-verify-license?os=ubuntu&version=3.0.10&file=TexturePacker-3.0.10-ubuntu32.deb[/url].

For linux mint32 you can try to run ShoeBox with Wine (ShoeBox is an Air app).

-------------------------

practicing01 | 2017-01-02 01:00:39 UTC | #9

The old version of TexturePacker worked, thanks Mike.  However, it's not a good idea to buy an outdated version of any program (the demo version defaces sheet output).  Shoebox would be the next thing to try..

-------------------------

weitjong | 2017-01-02 01:00:40 UTC | #10

Although I don't think we should have all the tools to be built in-house, but I believe that if one intends to create a texture packer tool then it can be accomplished rather easily because Urho3D has already all the necessary C++ classes. One would just need to creatively put those good bits together into a command-line tool and optionally enhance the Editor as the front-end for this tool. These are the classes I have in mind:

[ol][li]AreaAllocator class: it can be used to pack sprites into a smallest area.[/li]
[li]FontFaceBitmap class: it demonstrates how to use the AreaAllocator to pack glyphs into a texture, save the texture, and even output an xml file containing the information to access the individual glyph from the texture file.[/li][/ol]
The latter is not using Starling/Sparrow format, but you got the idea. One can output the xml file in any format he/she wishes. Just substitute font glyph with sprite :slight_smile:.

-------------------------

lexx | 2017-01-02 01:02:18 UTC | #11

Libgdx comes with texturepacker. 
And older texturepacker with gui:  [code.google.com/p/libgdx-textur ... loads/list](https://code.google.com/p/libgdx-texturepacker-gui/downloads/list) 
Java programs.

-------------------------

