vitej | 2017-01-02 01:08:54 UTC | #1

hey i am from svifylabs and 
I am currently working on an integration of ImGui to Urho3D. 
I opened an issue for this and was told to open a thread for this too ... so here i am ^^


The imgui integration as of now works for windows, have to test android and linux. (helpers always welcome)
The ImGui library is not fully wrapped in the IMUI class so you have to use the ImGui namespace for the ui elements and include "imgui/imgui.h". 
You can use the ImGui functions between the BeginFrame and EndFrame event. 
ImGui uses their own font implementation so you have to load the fonts manualy and it uses an ini file for saving the position and size of the generated windows between app sessions.

There some todos i am working on but it should work for now. 

For those who want to help:
- look through the IMUI::RenderDrawLists function, you coudl find a better way to render the provided data ...
- how can i tell cmake to use ImGui not as an library but copy the source into Urho3d so we can use the provided imconfig.h for converting Uhro3d Vector2/4 to ImVec2/4 classes. 
- should i wrap all ImGui functions ? if so should i use static funtions for that  ? 
- i dont think Lua or angelscript bindings are needed ? ?
[spoiler][img]http://i.imgur.com/X8F4OxL.png?1[/img]
[img]http://i.imgur.com/7Uu5Hqe.png?1[/img][/spoiler]

-------------------------

cadaver | 2017-01-02 01:08:54 UTC | #2

I believe wrapping everything is wasted work if script bindability is not a goal. Ie. a C++ user can just as well use the library directly.

-------------------------

vitej | 2017-01-02 01:08:57 UTC | #3

[quote="cadaver"]I believe wrapping everything is wasted work if script bindability is not a goal. Ie. a C++ user can just as well use the library directly.[/quote]
ok that is what i thought.

-------------------------

globus | 2017-01-02 01:08:57 UTC | #4

I think it gives me the opportunity to not care about binding imgui to Urho.

And also the ability to modify or create my own functions. 
But there are two ways: modify IMUI or imgui_user.

Perhaps IMUI could be as translator for imgui in Urho (fonts, vectors, render etc.) 
And can be provide an interface for modification as it makes imgui using imgui_user files.

(it's just reflections)

-------------------------

empirer64 | 2017-01-02 01:09:00 UTC | #5

I have tested the newest source code, and it works on linux just fine.

-------------------------

globus | 2017-01-02 01:09:00 UTC | #6

Text icons can placed as UTF-8 characters

In HelloIMUI code:
// ImGui::Text("\uF04B"); isn't correct it is 16-bit unicode whereas ImGui takes UTF-8.
// so use in c++11 use u8"\uf016" or
ImGui::Text("[b]\xef\x80\x96[/b]" " Line A"); // use string literal concatenation, ouputs a file icon and File as a string

I found big list of all UTF-8 characters. It help understand how it use.
[utf8-chartable.de/unicode-ut ... ng-literal](http://www.utf8-chartable.de/unicode-utf8-table.pl?number=512&utf8=string-literal)
@ - \x40
A - \x41
B - \x42
C - \x43
D - \x44
etc.

It very useful addon.
Icons save screen space (not need draw long string) - only single symbol (can be with tooltip)
Also, not used big memory how it do full-color icons. And you can change color of icons.

-------------------------

globus | 2017-01-02 01:09:00 UTC | #7

Compilation on XP, OpenGL, MinGW (GCC) have small c++11 warnings:

[b]imconfig.h[/b]

warning: non-static data member initializers only available with -std=c++11 or -std=gnu++11

 struct ImDrawVert \
{\
    ImVec2  pos;\
    [b]float	z = 0.0f;\[/b]
    ImU32   col;\
    ImVec2  uv; \
};

[b]HilloIMUI.cpp[/b] strings 218, 219, 220, 221.

warning: extended initializer lists only available with -std=c++11 or -std=gnu++11

static ImVec2 point1[3] = { {0.10f,0.0f},{ 0.0f,0.0f} , {.0f,.10f} };
static ImVec2 point2[3] = { { 0.0f,0.0f },{ 0.0f,0.0f } ,{ .0f,.10f } };
static ImVec2 point3[3] = { { 0.0f,0.0f },{ 0.0f,0.0f } ,{ .0f,.0f } };
static ImVec2 point4[3] = { { 0.10f,0.0f },{ 0.0f,0.0f } ,{ .0f,.10f } };

But, It compiles and runs well.

-------------------------

globus | 2017-01-02 01:09:01 UTC | #8

[img]http://i.piccy.info/i9/e0799534901f20cacfda2d3cf0d4c29f/1450994093/28563/912050/text_color_test.jpg[/img]

Need easy way to set text color for Title, Button, Header. Or may be this method already exists?
Begin("Title text")
CollapsingHeader("Header Text")
Button("Button text", ImVec2(100.0f, 20.0f))

If i do them dark color and default text also dark colored - text will be unreadable.
The same otherwise.

-------------------------

sabotage3d | 2017-01-02 01:09:01 UTC | #9

I really like the curve editor it is really good for animation curves and for interpolation visualization.

-------------------------

globus | 2017-01-02 01:09:01 UTC | #10

What you think about integration dockable windows from ImWindow to IMUI?
[b]ImWindow[/b] - [github.com/thennequin/ImWindow](https://github.com/thennequin/ImWindow)

I think - it is not imgui part, but it can be IMUI window manager.
And also, it can be switchable (enable/disable) managment during compilation or runtime.

-------------------------

sabotage3d | 2017-01-02 01:09:05 UTC | #11

Is it C++98 backward compatable?

-------------------------

globus | 2017-01-02 01:09:05 UTC | #12

You have compilation problems?
I have only small c++11 warnings.

-------------------------

globus | 2017-01-02 01:09:05 UTC | #13

I do small hacks in RenderFrame() function in imgui for Border 3D effects.
On screenshots you can see borders-effects for Headers, Buttons, Input areas.
Dark theme
[img]http://i.piccy.info/i9/79f1ed67a0c19e75143ba5975daf9963/1451257388/99711/912050/lines_test1.jpg[/img]
Light theme
[img]http://i.piccy.info/i9/b175bae764610e4520dbd2b18fc39b65/1451257506/85135/912050/lines_test2.jpg[/img]

-------------------------

vivienneanthony | 2017-01-02 01:09:24 UTC | #14

Hi

What is the URHO equivalent example file? Is it the DEMO file in the Thirdparty folder?

Vivienne

-------------------------

vivienneanthony | 2017-01-02 01:09:25 UTC | #15

Hi,

Do anyone know what's up with this error?

[i.imgur.com/gveww9I.png](http://i.imgur.com/gveww9I.png)

I'm trying.

[github.com/svifylabs/Urho3D/tre ... ThirdParty](https://github.com/svifylabs/Urho3D/tree/f_imgui/Source/ThirdParty)

I am getting compile errors on those specific lines. I'm assuming the code  worked on prior Urho3D versions.

Viv

-------------------------

vivienneanthony | 2017-01-02 01:09:26 UTC | #16

Hi

This is the compile error attempting to implement IMGUI placed in AlphaEngine and tested in the beginning part of AlphaEditor. It could be applied to Urho3D fully once working if anyone wants to. I'm doing it as a LogicComponent allowing muiltiple instances of the GUI to be run possibly.

[pastebin.com/sNNg9hf0](http://pastebin.com/sNNg9hf0)

This is the base code I'm testing it on.

[github.com/vivienneanthony/MyFo ... evelopment](https://github.com/vivienneanthony/MyForkEditor/tree/development)

Vivienne

-------------------------

globus | 2017-01-02 01:09:26 UTC | #17

Error with Draw() function:

IMUI add small changes to Urho.

First step
In OGLGraphics (cpp, h) add his version of Draw() function.

Second step
And in Engine.cpp (in Engine::Initialize() function)
context_->RegisterSubsystem(new IMUI(context_));

Second step can be easy moved in you code (removed from Engine code)
Is all changes. And only new GLSL HLSL files in Data folder.

---------------------------------
Border effect was discussed in [github.com/ocornut/imgui/issues/447](https://github.com/ocornut/imgui/issues/447)

-------------------------

vivienneanthony | 2017-01-02 01:09:26 UTC | #18

[quote="globus"]Error with Draw() function:

IMUI add small changes to Urho.

First step
In OGLGraphics (cpp, h) add his version of Draw() function.

Second step
And in Engine.cpp (in Engine::Initialize() function)
context_->RegisterSubsystem(new IMUI(context_));

Second step can be easy moved in you code (removed from Engine code)
Is all changes. And only new GLSL HLSL files in Data folder.

---------------------------------
Border effect was discussed in [github.com/ocornut/imgui/issues/447](https://github.com/ocornut/imgui/issues/447)[/quote]


Hmmm. Thanks. I'm going copy the Draw functions and rename so the original code stays. I'm rebuilding now so I'll see what happens once it finishes.

-------------------------

globus | 2017-01-02 01:09:26 UTC | #19

You can also compare Urho master branch and f_imgui branch to see all changes
[github.com/urho3d/Urho3D/compar ... bs:f_imgui](https://github.com/urho3d/Urho3D/compare/master...svifylabs:f_imgui)
But, it big and heavy loadable Html page.

-------------------------

vivienneanthony | 2017-01-02 01:09:26 UTC | #20

[quote="globus"]You can also compare Urho master branch and f_imgui branch to see all changes
[github.com/urho3d/Urho3D/compar ... bs:f_imgui](https://github.com/urho3d/Urho3D/compare/master...svifylabs:f_imgui)
But, it big and heavy loadable Html page.[/quote]

I wish it was that simple.

Covering the steps you mentioned.

1) Updated the functions which still did not resolve the DrawList so I betting it's a memory issue.

2) Update the syntax to 

[code] 
    // Get the game client context
    context_->RegisterSubsystem(new ImGuiInterface(context_));
    m_pGuiInterface = context_->GetSubsystem<ImGuiInterface>();[/code]

The first  part is not needed. I think but I still added.

Bug

1. I'm think the ImGuiInterface is not created hence the failure with this part.  (Possibly *this is invalid)

[code]Program received signal SIGSEGV, Segmentation fault.
Urho3D::String::Append (this=this@entry=0x7fffffffd160, str=...) at /media/home2/vivienne/Urho3D-Hangars-MyForkEditor/Source/Urho3D/Container/Str.cpp:310
310         return *this += str;
(gdb) bt 5
#0  Urho3D::String::Append (this=this@entry=0x7fffffffd160, str=...)
    at /media/home2/vivienne/Urho3D-Hangars-MyForkEditor/Source/Urho3D/Container/Str.cpp:310
#1  0x0000000000d712af in ImGuiInterface::SetSettings (this=0x24804a0, settings=...)
    at /media/home2/vivienne/Urho3D-Hangars-MyForkEditor/Source/AlphaEngine/Interfaces/ImGui/ImGuiInterface.cpp:173
#2  0x00000000007899ab in Editor::Create (this=0x17c0e70, scene=0x23958a0, sceneUI=0x24bf170)
[/code]

2. Removing the set settings out the editor part. So I'm not sure if it's another memory list which I don't think DrawList is part of the Unity functions but ImGui specific.
[code]
Program received signal SIGSEGV, Segmentation fault.
0x0000000000d45da2 in ImGui::Begin (name=name@entry=0x10ce4d6 "Hello", p_opened=p_opened@entry=0x0, size_on_first_use=..., bg_alpha=0.699999988, 
    bg_alpha@entry=-1, flags=flags@entry=0) at /media/home2/vivienne/Urho3D-Hangars-MyForkEditor/Source/AlphaEngine/ThirdParty/ImGui/imgui.cpp:3667
3667            window->DrawList->PushTextureID(g.Font->ContainerAtlas->TexID);
(gdb) bt 5
#0  0x0000000000d45da2 in ImGui::Begin (name=name@entry=0x10ce4d6 "Hello", p_opened=p_opened@entry=0x0, size_on_first_use=..., bg_alpha=0.699999988, 
    bg_alpha@entry=-1, flags=flags@entry=0) at /media/home2/vivienne/Urho3D-Hangars-MyForkEditor/Source/AlphaEngine/ThirdParty/ImGui/imgui.cpp:3667
#1  0x0000000000d496b5 in ImGui::Begin (name=name@entry=0x10ce4d6 "Hello", p_opened=p_opened@entry=0x0, flags=flags@entry=0)
    at /media/home2/vivienne/Urho3D-Hangars-MyForkEditor/Source/AlphaEngine/ThirdParty/ImGui/imgui.cpp:3544
#2  0x000000000078a696 in Editor::Create (this=0x24a0bd0, scene=<optimized out>, sceneUI=<optimized out>)
    at /media/home2/vivienne/Urho3D-Hangars-MyForkEditor/Source/AlphaEditor/Core/Editor/Editor.cpp:356
#3  0x000000000072d9b3 in MainEditorView::EditorInstance (this=0x2396a30)
    at /media/home2/vivienne/Urho3D-Hangars-MyForkEditor/Source/AlphaEditor/GameView/MainEditorView.cpp:115
#4  0x000000000072cfa5 in MainEditorView::FinishIntroductionPartDelegate (this=0x2396a30, eventType=..., eventData=...)
    at /media/home2/vivienne/Urho3D-Hangars-MyForkEditor/Source/AlphaEditor/GameView/MainEditorView.cpp:76
(More stack frames follow...)
[/code]

-------------------------

vivienneanthony | 2017-01-02 01:09:28 UTC | #21

Got it working.

-------------------------

vivienneanthony | 2017-01-02 01:09:31 UTC | #22

Hi

Do anyone know how the glyph system work for fonts? Im making a font type .ttf and .svg that contains all the editor icons in a letter slash icon type. I figure it can be useful. If i can get any help. I submit the font type to be added to Urho. 

It works partially but because of my understanding of ImGui and Urho. The font replaces the ImGui default type. So I see some characters thats been replaced.

Vivienne

-------------------------

vivienneanthony | 2017-01-02 01:09:31 UTC | #23

I'll probably have room for 4 more icons if anyone have any idea of what to put. 0 to 9 I'm doing for some things I need.

[i.imgur.com/auU9gjT.png](http://i.imgur.com/auU9gjT.png)

-------------------------

vivienneanthony | 2017-01-02 01:09:37 UTC | #24

Hi

I've managed to replicate the UI of the Editor adding some extras using ImGui. Also, using the Icon Set created font.

[youtube.com/watch?v=g92xG8ZMMA0](https://www.youtube.com/watch?v=g92xG8ZMMA0)

Vivienne

-------------------------

billyquith | 2017-01-02 01:09:43 UTC | #25

[quote="vitej"]
I am currently working on an integration of ImGui to Urho3D.[/quote]

What is the purpose of this UI toolkit in Urho? Urho already has a UI. Is this to replace the existing UI? Urho is supposed to be a "lightweight" engine, but it already has 2 different languages. Now 2 different GUIs?

I'm not against experimentation, and forks of the engine that try out different ideas, but if Urho is going to get bloated with many options, it just brings more maintenance overhead. It also strays away from the lightweight objective, which makes Urho attractive.

I don't think ImGui is an appropriate UI for building integrated editing tools within Urho. Its purpose is as a drop in solution for tuning and debugging applications. As has been pointed out elsewhere, what Urho needs is a pixel perfect UI (similar to the existing one, but perhaps improved), and if a second one is added, one that supports varying screen resolutions (like responsive web design, or QML).

If this is to be added, surely it should be like libRocket, as a standalone library that just depends on Urho?

-------------------------

vivienneanthony | 2017-01-02 01:09:43 UTC | #26

[quote="billyquith"][quote="vitej"]
I am currently working on an integration of ImGui to Urho3D.[/quote]

What is the purpose of this UI toolkit in Urho? Urho already has a UI. Is this to replace the existing UI? Urho is supposed to be a "lightweight" engine, but it already has 2 different languages. Now 2 different GUIs?

I'm not against experimentation, and forks of the engine that try out different ideas, but if Urho is going to get bloated with many options, it just brings more maintenance overhead. It also strays away from the lightweight objective, which makes Urho attractive.

I don't think ImGui is an appropriate UI for building integrated editing tools within Urho. Its purpose is as a drop in solution for tuning and debugging applications. As has been pointed out elsewhere, what Urho needs is a pixel perfect UI (similar to the existing one, but perhaps improved), and if a second one is added, one that supports varying screen resolutions (like responsive web design, or QML).

If this is to be added, surely it should be like libRocket, as a standalone library that just depends on Urho?[/quote]

I'm using it as a separate library for the purpose of a editor UI that isn't directly Urho. So, the UI editor and scene can be edited without conflicting each other.

I also like the cleaner UI.

[i.imgur.com/G6UZwnS.png](http://i.imgur.com/G6UZwnS.png)

-------------------------

billyquith | 2017-01-02 01:09:44 UTC | #27

[quote="vivienneanthony"]
I also like the cleaner UI. - [i.imgur.com/G6UZwnS.png](http://i.imgur.com/G6UZwnS.png)[/quote]

Could you describe what you mean by "cleaner"? To me, the icons make no sense, and the dialog boxes have no edges, there is just text floating the air, without context.

-------------------------

vivienneanthony | 2017-01-02 01:09:44 UTC | #28

[quote="billyquith"][quote="vivienneanthony"]
I also like the cleaner UI. - [i.imgur.com/G6UZwnS.png](http://i.imgur.com/G6UZwnS.png)[/quote]

Could you describe what you mean by "cleaner"? To me, the icons make no sense, and the dialog boxes have no edges, there is just text floating the air, without context.[/quote]

The Icons are the same as the current Editor pretty much. Each person has their own personal preferences. I can tell where a window is by the top bar and the bottom right resize, and I don't think border edges is necessary around everything. The UI seems minimum. Just showing what's needed.

-------------------------

vivienneanthony | 2017-01-02 01:09:50 UTC | #29

Hello,

Can the modified Draw function be added to Urho3D? I'm not asking for the whole IMGUI integration. 

I'm asking for the Draw functions so I can easily implement ImGui using my addon API without modifying Urho3D every time I download it or update.

Vivienne

-------------------------

