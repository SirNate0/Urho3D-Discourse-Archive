Taqer | 2019-06-02 10:56:48 UTC | #1

Hi, I want to achieve fog of war effect like this:
![obraz|690x329](upload://v8FlERzlkSq3r7ImnP2Rn90IcNu.png) 
I got a code for changing alpha of fog, but I need to first render ground and buildings, and then fog, beacuse fog is lower than buildings.

I was trying to change renderpasses, techniques, like here: https://discourse.urho3d.io/t/how-to-control-render-order/1240/12
But the objects are still rendered above fog and I dont see transparency on texture

Now I made two viewports and cameras with different view masks but can't get to render them at the same time (or I render one and second is covering firsts render), I have either only fog or objects and map. I need to somehow set the fog camera to render only fog object and not background, but how?

btw. I'm new to this engine, but I really like it, good work guys.

-------------------------

Leith | 2019-06-02 11:47:13 UTC | #2

one way to achieve the fog of war is to use blend modifiers on the terrain vertices - take a look at how the terrain shader uses 'blend mapping' to mix n input textures in the fragment shader
basically, we paint vertex colours, and give the colours a meaning...

-------------------------

Modanung | 2019-06-02 14:22:06 UTC | #3

If your fog consists of 3D geometry you might get away with setting a depth bias in its material akin to:
```
<depthbias constant="-0.0000023"/>
```

Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

Taqer | 2019-06-02 14:21:48 UTC | #4

@Modanung That works. I just have to decrease that value a bit, many thanks! :smiley:

-------------------------

Leith | 2019-06-06 12:46:57 UTC | #5

Lucky you, I needed to paint vertex colour for another purpose, which the editor does not support well - material properties on terrains for sound effects let alone physics - I feel I am reaching the end of the stuff that Urho supports out of the box

-------------------------

