Elendil | 2017-12-13 22:52:19 UTC | #1

I know Urho have some GUI, but I like to use another gui library, more complete and customizable.

My idea is, use some render layer on top of 3D. Firstly will be rendered 3D scene and then UI layer. How can I do that? Is it good idea?

I found there are only viewports, maybe create another viewport which will render only GUI?

-------------------------

Eugene | 2017-12-13 23:11:28 UTC | #2

There is open PR with Nuclear UI in Urho's GitHub and there is ImGUI integration [here](https://github.com/rokups/Urho3D-Toolbox)
Just look here and check how it is implemented.
BTW, what UI library you are going to use?

-------------------------

Elendil | 2017-12-13 23:24:38 UTC | #3

Thanks, I'll look at it tomorrow.

[Noesis GUI](http://www.noesisengine.com), it is WPF for C++ and it is intended as game gui, but I try use it as gui for my program.

-------------------------

jmiller | 2017-12-15 04:48:11 UTC | #4

We also have the two TB implementations. Updated 2016-08,  https://discourse.urho3d.io/t/turbo-badger-implementation/1364/13
  and Lumak's, which I've used as well:  https://discourse.urho3d.io/t/turbobadger-full-integration/1457 

There has been a bit of discussion on [url=https://discourse.urho3d.io/search?q=renderui]renderui[/url] - the [url=https://urho3d.github.io/documentation/HEAD/_render_paths.html]Render path[/url] command.

-------------------------

Elendil | 2017-12-15 15:31:29 UTC | #5

Thanks, maybe I'll try later, because my skills are very low, and I am unable integrate Noesis in to Urho. Btw Noesis is not new but still under development and better in each release. New documentation will be updated with new updates.

I am now trying [Sciter](https://sciter.com), which use HTML / CSS and JS like script, but it is not JavaScript. There are some examples for openGL, DirectX or GLFW integration and I try get some inspiration from it. Sciter is complete and used by big companies like Esset for his antivirus, Avast use sciter too. And it is free, if you don't need static linking.

-------------------------

SirNate0 | 2017-12-16 00:48:35 UTC | #6

If you just want something like HTML/CSS, you can try libRocket, which some people have already integrated (I don't know if I'd call it a finished integration, but it works well enough for me). I have a branch [here](https://github.com/SirNate0/Urho3D/tree/librocket) with it, though you should just need the last few commits. Granted, you may have better luck with Sciter, as it does seem to be professional, and libRocket does have some flaws like no longer being developed (as best I can tell).

-------------------------

