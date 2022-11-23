christianclavet | 2017-01-02 01:06:06 UTC | #1

Hi! I'm really new to URHO3D and just discovered it recently. This project is really incredible with all the features that I always wanted!

I would like to create an editor with URHO3D similar to the one I've worked on. (Working and learning on this for the last 5 years). It used Irrlicht as render/gui. ([url]http://irrrpgbuilder.sourceforge.net[/url])[img]http://irrrpgbuilder.sourceforge.net/forum/download/file.php?id=180&t=1[/img]

This is a simple game editor as I'm not a real programmer, but learning programming as a hobbyist. URHO3D save me  a lot of complexities has all the needed features are there, and I don't think I would need to add other libs/framework to it to redo the game editor.

I would need to add specific GUIs to the URHO3D gui. I've searched in the forum and on google but did not found more information on how to add custom GUIs.
Basically, I would need to create in C++ without patching URHO3D:
- lua code editor with highlighting. Highlighting could be added later. If we can type in multiline would do first, then I could add features. (Would like to add to the URho3D gui)
- Tabbed GUI component. I don't like menus and would use this instead. 

So is there some way of doing a new GUI component (C++) and use it directly from my application with the URHO3D gui? Looking from the editor you seem to have a "generic" UIelement, and it look possible. So could I create a new class using the base UIElement in my application or it would be required that new UIElements be added in URHO3D sources and recompiled?

For the rest, the GUI is more than adequate, the URHO editor showed me a lot of nice stuff!

For now, I've just compiled URHO and checking it. So I have lots of things to learn! The current GUI system is ok for me, I just need to be able to "plug" my own to it and I don't like patching. I will also have to learn how git is working, I'm only familiar with SVN.

-------------------------

thebluefish | 2017-01-02 01:06:06 UTC | #2

Create a class that derives from UIComponent and do everything there.

For example, [url=https://github.com/thebluefish/Urho3DEditor/blob/master/Prime/GameClient/src/UI/TabWindow.h]here's Scorvi's tab control[/url]. 

As far a text editor, that's a bit more advanced. Honestly in that regard I'd look at integrating some third party UI, such as [url=https://github.com/fruxo/turbobadger]Turbo Badger[/url]. It's a bit more advanced integrating a third-party library, but it will allow you to leverage much more mature libraries.

-------------------------

rasteron | 2017-01-02 01:06:06 UTC | #3

I also did a Tab Menu Component workaround and example wayback. This was tested with older versions but since this was done purely via angelscript and xml layout files, it does not require tinkering with engine code and should work on the latest Editor code with some slight or no modifications at all.

[img]https://lh6.googleusercontent.com/-MbXzSUHaJo4/UlLCnXO6xFI/AAAAAAAAADg/WrK4cyxdgPE/s400/tabmenu.jpg[/img]

Original Thread and Files
[groups.google.com/forum/#!topic ... IKM_UJndOg](https://groups.google.com/forum/#!topic/urho3d/7IKM_UJndOg)

*Patch is just for angelscript files only to automate the process but you can manually do those edits without problems.

-------------------------

christianclavet | 2017-01-02 01:06:07 UTC | #4

Wow! Thanks! So it can be done! I'm really happy about this!  :smiley:
Thanks for all the links. I'll only start first at deriving the class and see how it work. The code editor can be simple at first, as I'm no hurry. Once I know more how to use Urho, I might try to put that library (the screenshot of the GUI was really beautiful!)

Is there a URHO guide somewhere on how to make skins for the GUI? The current editor is really nice for the functionalities it offer, but would need little tweaks on the design in my opinion. The icons are really too small for the resolution we have today. (The icons size seem to be from the 1024x768 era, where we have 2K and 4K monitors today)
If we compare with Unreal editor, check the icon size they have:
[img]http://i1.wp.com/blog.digitaltutors.com/wp-content/uploads/2014/05/Interface.jpg[/img]

-------------------------

boberfly | 2017-01-02 01:06:07 UTC | #5

Hi,

From memory there's one texture atlas Textures/UI.png and an xml file which defines the offsets. You could, for instance, 2x the texture but then the offsets are pixel-aligned and not based on points.
[url]https://github.com/urho3d/Urho3D/blob/master/bin/Data/UI/DefaultStyle.xml[/url]

From the docs:
[url]http://urho3d.github.io/documentation/1.4/_u_i.html[/url]

So yeah, it would need to be patched so that it doesn't use integers (IntRect) but rather floating point normalized to the screen co-ords perhaps?
[url]https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/UI/BorderImage.h[/url]
(at the bottom).

Or BYO libRocket/imgui/TurboBadger/nanovg-based GUI and hook up Urho3D's resource/events/gfx/etc.? I've recently played around with kivy (a touch/UI framework for python that also works on mobile) and that brings some nice concepts too, but it's python...

-------------------------

codingmonkey | 2017-01-02 01:06:08 UTC | #6

>The icons are really too small for the resolution we have today
for my 1080p the icons size it's ok. and am do not like unreal style menus there is a lot strange and useless things - they close view, and these biggest icons it's awful, yes this is biggest icons in editor that's why i'm do not install UE4  yet  :laughing: 
IMO better to use a lot of shortcuts than this.

-------------------------

rasteron | 2017-01-02 01:06:08 UTC | #7

If icon sizes or resolution is an issue, perhaps it's time to consider and include SVG rendering for images/sprites. For starters, I found these libraries which supports SDL2 and cross platform..

[github.com/bazzinotti/MultiPlatformSVGRenderer](https://github.com/bazzinotti/MultiPlatformSVGRenderer)
[linuxmotors.com/SDL_svg/](http://www.linuxmotors.com/SDL_svg/)

-------------------------

boberfly | 2017-01-02 01:06:08 UTC | #8

[quote="rasteron"]If icon sizes or resolution is an issue, perhaps it's time to consider and include SVG rendering for images/sprites. For starters, I found these libraries which supports SDL2 and cross platform..

<a class="vglnk" href="https://github.com/bazzinotti/MultiPlatformSVGRenderer" rel="nofollow"><span>https</span><span>://</span><span>github</span><span>.</span><span>com</span><span>/</span><span>bazzinotti</span><span>/</span><span>MultiPlatformSVGRenderer</span></a>
<a class="vglnk" href="http://www.linuxmotors.com/SDL_svg/" rel="nofollow"><span>http</span><span>://</span><span>www</span><span>.</span><span>linuxmotors</span><span>.</span><span>com</span><span>/</span><span>SDL</span><span>_</span><span>svg</span><span>/</span></a>[/quote]

There's also:
[url]https://github.com/memononen/nanovg[/url]
[url]https://github.com/memononen/nanosvg[/url]

Last night I was studying nanovg in bgfx which makes it work on any API bgfx supplies. I'm not too sure which is easier, replace the GL2/3 backend or the bgfx one with a more Urho3D flavour, or use both as a guide to make one...

For performance concerns, there's also a patch someone made that's been tested with KiUi:
[url]https://twitter.com/hugoamnov/status/593449484866199552[/url]

-------------------------

rasteron | 2017-01-02 01:06:08 UTC | #9

[quote="boberfly"]
There's also:
[url]https://github.com/memononen/nanovg[/url]
[url]https://github.com/memononen/nanosvg[/url]
[/quote]

Looks good.

-------------------------

christianclavet | 2017-01-02 01:06:21 UTC | #10

Hi, Been learning and experimenting on how the interface is done in the URHO editor. I'm really impressed with all the features there are! Tried The internal GUI is really FAR SUPERIOR of what I've experienced with Irrlicht!

Here is a screen. Mostly scaled the icons to be a little bigger. On my monitor the icons looked really tiny. The size I've set them is adequate. I found out that the GUI can scale the icons picture without having to scale the image itself. So we could create very high resolutions pictures (for 4k resolution) and simply use a formula to set the desired size. I really find the GUI refresh to be fast!
[spoiler][img]http://www.clavet.org/files/URHO/EditorTweaks.jpg[/img][/spoiler]

One part was easy, I had only to load the XML layout definition in the editor itself and edit the GUI, the other part was editing the XML of the SKIN definition for the styles, and the last part was to edit some .AS files because the toolsbars seem to be generated from code.

There 2 things that I was able to use in Irrlicht that is not there: Tabbed windows, and multi-line edit box.

One thing that would be nice with the editor, is to improve the inspector to have each component in a window (fixed size and collapsable window in a window) that could be put in a single line (title with a direction arrow to expand-collapse). And a content window that take all theses component, so we could use a scrollbar to look at all the component instead of them being squashed and not operable. (This only happen when you have lots of component on a node)

-------------------------

