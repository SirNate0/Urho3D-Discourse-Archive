halcyonx | 2017-06-04 20:11:20 UTC | #1

There is way to use rasterized resources in Urho3D? I have psd file with buttons, tabs, panels, text and other interface stuff, also I have rastersized this psd to swl + png/webp. There is a way to display this resources?

-------------------------

johnnycable | 2017-06-03 11:35:16 UTC | #2

Load every png/jpg and so on with 

    auto createNode = [&](String spriteName) ->Node* {
        Node* node = scene_->CreateChild();
        StaticSprite2D* spriteComp {node->CreateComponent<StaticSprite2D>()};
        Sprite2D* sprite = cache->GetResource<Sprite2D>(spriteName);
        spriteComp->SetSprite(sprite);
        return node;
    };

Node* pong {createNode("GameData/2D/pong.jpg")};
pong->SetPosition(Vector2::ZERO);

you need to use urho2d for this. For 3d, turn StaticSprite2D in StaticSprite...
Check example 24 Urho2dSprite.cpp

-------------------------

halcyonx | 2017-06-03 11:52:31 UTC | #3

I work with one proprietary C++ engine, and it supports referencing to layers of image from code. If psd containse layer: button_ok, tab_content1, it psd can be rastersized to swl + png and there is possible to make call from code:
    menu = CreateFlashObject("Menu") // Menu is png and swl file
    menu.children("button_ok").children("text").setText("Ok")
    menu.children("button_ok").children("text").setColor(GREEN)
    menu.children("tab_content1").hide()
My interest is can I do similar things in Urho3D?

-------------------------

johnnycable | 2017-06-03 12:06:05 UTC | #4

Ah, I see. Afaik, there's no direct access from code to multi-layer psd / tga or so from urho. But I may be wrong.
Alternatively you can export each layer separated, and use a spritesheet. Check https://urho3d.github.io/documentation/1.6/_urho2_d.html under static sprites

-------------------------

smellymumbler | 2017-06-03 15:01:13 UTC | #5

I'm using nanovg to render my old FLAs as SVGs. Works great!

-------------------------

Modanung | 2017-06-03 15:07:39 UTC | #6

[quote="johnnycable, post:4, topic:3199"]
Alternatively you can export each layer separated
[/quote]
[GIMP](https://www.gimp.org/) supports PSD and using [this](https://github.com/khalim19/gimp-plugin-export-layers/) plug-in it can do exactly that in a few clicks.

-------------------------

johnnycable | 2017-06-03 18:49:02 UTC | #7

I'm trying that, too, but only made nanosvg to work, that is, straight from an svg image to ui widget. Does nanovg alone works? 

@Modanung I had forgot about that plugin!:sunglasses:

-------------------------

halcyonx | 2017-06-03 19:40:16 UTC | #8

What nanovg/nanosvg is? Is its functionality available from Urho3D?

-------------------------

smellymumbler | 2017-06-03 19:48:05 UTC | #9

They are libraries. You can find good integration samples here: https://github.com/scorvi/Urho3DSamples

-------------------------

halcyonx | 2017-06-03 19:58:59 UTC | #10

Is U3D supports flash animations, swf format? There is list of supported resource formats in U3D engine?

-------------------------

smellymumbler | 2017-06-03 20:18:15 UTC | #11

Nope. That would be super complex, because it means having a built-in SWF player. Even AAA engines didn't had that built-in. Unreal Engine 3, for example, relied on Scaleform to add SWF functionality into the engines. And it sucked.

You'll have to redo your animations with SVG objects and Urho's animation system.

-------------------------

smellymumbler | 2017-06-03 20:19:52 UTC | #12

BTW: if you come from a Flash background and you want to do 2D games, i recommend you choose something like OpenFL: http://www.openfl.org/learn/tutorials/using-swf-assets/

Haxe is heavily inspired by ActionScript and OpenFL is a game engine modelled after the "golden" flash game years. Almost everyone that did Flash games moved to that engine.

-------------------------

halcyonx | 2017-06-03 21:00:31 UTC | #13

No, I've no flash background. I work in project (my main job) with following workflow: 
1. interfaces created and saved in swf or psd
2. psd or swf reraterized into internal proprietary format swl (behaviour) + png (image)
3. swl + png used via engine in game code C++/lua 

I want find the standard way in U3D to create dynamic/juicy/beautiful interfaces.

-------------------------

slapin | 2017-06-03 22:18:26 UTC | #14

Very long time ago I used library which came with gnash + swftools to write my custom converter from swf resources
to sets of images when converted some flash game to pygame, however I written all logic from scratch
using python and used .swf only to extract graphics.
Well, Urho UI is not juicy, but with some effort you can get some basic functions.
I just added fully transparent region to UI.png and implemented fully-transparent button,
and I add such buttons on top of prepared images + sprites. All animation is done using sprites.
I think you can ad-hoc such UI system in a hour or so. You just draw all your UIs in Krita or MyPaint or Gimp and put invisible buttons on it, using sprites (UI element) for all animation. This works for me.
For something else I think you better search forum for alternate GUI systems, but I'm fine with stock Urho GUI
for the time.

-------------------------

smellymumbler | 2017-06-04 00:34:09 UTC | #15

Yeah, Urho UI is definitely not juicy. You should look into alternatives like:

https://github.com/libRocket/libRocket
https://github.com/realrunner/urho3d-librocket

OR:

https://github.com/Lumak/Urho3D-1.4-TurboBadger

-------------------------

smellymumbler | 2017-06-04 00:34:36 UTC | #16

Or this: https://github.com/Enhex/Urho3D-CEF3

-------------------------

slapin | 2017-06-04 01:28:57 UTC | #17

There was IMGUI somewhere, and also there is PR with Nuklear, but something is not right with it.

For myself i will use whatever GUI is provided by stock installation and usable by scripts.
No current alternate GUI projects provide script integration, so I use stock UI.

-------------------------

johnnycable | 2017-06-04 10:27:37 UTC | #18

Exactly that. I was able to make the nanosvg (read from a file) work almost immediately, but not the nanovg one (render to opengl). That's probably because it renders directly to the buffers, and that's doesn't seem a good strategy. The Nanovg GUI classic example is kind of broken... <img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/e2a38d8d0d2fb07d2f3ad4441ccc1bf9f59b093e.jpg" width="666" height="499">
Anyway the examples are from a couple of urho releases ago, i had to update, and I maybe made st wrong or who knows...

-------------------------

halcyonx | 2017-06-11 05:54:04 UTC | #19

I think is more easy way in urho it simulate gui with group separated layers loaded as sprites, is it right?

-------------------------

johnnycable | 2017-06-11 05:54:02 UTC | #20

Guess so. This is the general way of doing in 2d games, because you can batch-bind sprites to hw graphic cards.
If you use a flash/svg layer, you just add a layer of conversion, one more operation to get to the same result. You need to have a good reason to do that.
Graphic cards eat triangles and bitmaps, not curves and functions...:disappointed_relieved:

-------------------------

