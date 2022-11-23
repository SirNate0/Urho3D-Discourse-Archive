ezark | 2018-12-22 07:47:39 UTC | #1

Hi everybody. I read the samples in the .sln and all ui is created directly in the c++ code. So is there more acceptable solution?  All i know id store all ui components in a xml file and we just load the xml file and render it.
thanks very much.

-------------------------

orefkov | 2018-12-22 10:11:05 UTC | #2

You can create ui in editor, save in xml and load it in runtime, sample in AngelScript

    UIElement@ uiface = ui.LoadLayout(cache.GetFile("UI/done.xml"));
    ui.root.AddChild(uiface);

-------------------------

ezark | 2018-12-22 10:36:25 UTC | #3

Thank you very much! It helps.

-------------------------

Leith | 2019-01-28 06:22:41 UTC | #4

If the editor was stable on linux, I'd use it too.
Since it is virtually useless to me, I construct my UI in c++ and dump them to XML for further editing, then remove the code I used to generate them, and replace it with code to load them.

-------------------------

ezark | 2019-01-28 12:46:30 UTC | #5

But if your ui is too complicated, you should write too many c
++ code without using the editor.

-------------------------

Modanung | 2019-01-30 16:55:33 UTC | #6

There's bound to be room for generalizing your UI generation code by wrapping stuff into functions specific to your project.

-------------------------

johnnycable | 2019-01-30 15:44:33 UTC | #7

Maybe this [FairyGui](http://en.fairygui.com/)?
But it takes to be adapted to Urho...

-------------------------

Modanung | 2019-01-30 17:19:17 UTC | #8

There's also:
https://discourse.urho3d.io/t/external-imgui-integration/1815

-------------------------

Leith | 2019-01-31 10:20:13 UTC | #9

imgui is quite slow and does not come with a custom shader for gl3+, I do not recommend unless you want to hack a lot

-------------------------

smellymumbler | 2019-01-31 15:19:45 UTC | #10

Slow? Can you elaborate on that? I've got plenty of debug stuff with imgui and hasn't affected the performance of my debug build in any way.

-------------------------

Leith | 2019-02-01 03:39:20 UTC | #11

One of the main reasons that Dear Immediate Mode GUI is slow, is that it issues a draw call for each and every gui element being rendered - it does not attempt to batch draw calls in any way.
At least that's how it worked when I last used it.
This can be remedied fairly easily, and is worth doing if you can be bothered replacing its ancient rendering system for a modern GL3+ version.

I noticed this when I started using expensive gui elements like 2D graphs, in a very gui-intensive application that was meant to spend most of its time performing calculations on the GPU (OpenCL) for an experiment in neural networked evolution of AI for video games.

-------------------------

smellymumbler | 2019-02-01 19:48:02 UTC | #12

You're not supposed to use the built-in renderer, unless you're in a rush and you just need some GUI. Here's a highly-efficient sample implementation: https://github.com/r-lyeh-archived/gpulib

-------------------------

smellymumbler | 2019-02-01 19:51:46 UTC | #13

https://ourmachinery.com/post/one-draw-call-ui/

-------------------------

Leith | 2019-02-02 15:27:01 UTC | #14

damn straight, where on the packet does it say this product is not fit for consumption? and still no batching mechanism in the latest sourcecode

-------------------------

smellymumbler | 2019-02-02 18:16:19 UTC | #15

Right here: https://github.com/ocornut/imgui/blob/master/imgui.cpp#L172

You provide the drawing logic, not them. If you want to use theirs, fine. But stop complaining about free and open source software as if it was commercial.

-------------------------

Leith | 2019-02-03 12:13:48 UTC | #16

It's a great api, don't get me wrong, it got the job done, but out of the box, it's not what I would call shipping quality - I did state it's fairly easy to remedy too. It's not a bad lib, but it is presented using 20 year old technology.

-------------------------

Sinoid | 2019-02-04 05:28:54 UTC | #17

If you split DearIMGUI into a layout and render pass it'd be disturbingly similar to the GUI systems I've worked with on *big-ticket* products.

![image|668x500](upload://1fbVoSwhYrUE2qlbeD9dwPEh1cq.jpeg)  

Life critical application above, that features only 2 MFC CWnds, everything else is IM style custom controls ... most of that code goes back to 1998. You can see the aged attempt to reach out to the modern era with the inset forms and use of shade to indicate pane focus.

There's diddly wrong with DearImGui beyond it's incompetency at rich-text and varying font-size. It's trivial to port to GDI or QT's QPainter, as I've done both, and that's a good thing.

---

In a more serious reply, Noesis is awesome - fairly straight-forward to integrate and cheap.

FairyGUI is stupid awesome, but is Cocos based C++ side so it's a complete pain to tie into anything since Cocos is a special kind of psychotic. Would be interesting if the FairyGUI# stuff could be done in Urho# though.

-------------------------

