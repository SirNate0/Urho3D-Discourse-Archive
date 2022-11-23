krstefan42 | 2017-01-02 01:05:44 UTC | #1

Hi there. I've been working on a parallax mapping shader, using the iterative parallax mapping method. The number of iterations is currently a dynamic parameter, but for best performance I'll also release some versions with a fixed number of iterations. It also has a customizable offset-limiting factor, which lets you reduce texture swimmimg at low surface viewing angles, at the cost of reducing the strength of the effect.

Since it's just multiple iterations of classic parallax mapping, and not parallax occlusion mapping or any newer techniques, that means that it technically doesn't have self-occlusion, it just stretches and scrunches the texture in different places. But it's fast and looks good. You can get good results with only 2 iterations, which means only 2 additional texture samples are needed.

The actual shader will be up soon, I have some things I need to finish. For now, here are some screenshots. First image is without parallax, second is with.
[url=http://postimg.org/image/8u0updc03/][img]http://s29.postimg.org/8u0updc03/Parallax_Off.jpg[/img][/url]
[url=http://postimg.org/image/g8p2ypawt/][img]http://s30.postimg.org/g8p2ypawt/Parallax_On.jpg[/img][/url]

-------------------------

szamq | 2017-01-02 01:05:44 UTC | #2

Awesome, looks cool.

-------------------------

Mike | 2017-01-02 01:05:44 UTC | #3

Stunning!  :stuck_out_tongue:

-------------------------

GoogleBot42 | 2017-01-02 01:05:45 UTC | #4

Nice!   :smiley:   That looks great!

-------------------------

weitjong | 2017-01-02 01:05:46 UTC | #5

Eye popping.

-------------------------

krstefan42 | 2017-01-02 01:05:47 UTC | #6

You can now download the shader here: [url]http://discourse.urho3d.io/t/parallax-mapping-opengl-only-for-now/1158/2[/url]
No DirectX support yet, unfortunately.

-------------------------

rasteron | 2017-01-02 01:06:44 UTC | #7

This is a cool shader krstefan42. The only problem that I am having was running it on Android build and displaying a black terrain. Is this GL ES compatible?  :wink:

-------------------------

