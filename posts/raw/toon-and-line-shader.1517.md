adekto | 2017-01-02 01:08:13 UTC | #1

greetings im trying to get a toon shader to work in urho3D but dont know where to start
im personaly interested in the style of shader that is used in the new pokemon games or the shaders used in valkyria chronicles

im looking for somthing like this but i have never done anything like this yet
[img]http://i61.tinypic.com/rjh9at.jpg[/img]

-------------------------

Bananaft | 2017-01-02 01:08:13 UTC | #2

Hi, welcome to the forum!

To do cell shading you can hack GetDiffuse function in CoreData/Shaders/GLSL/Lighting.glsl (assuming you going to use OpenGL), so it will output banded gradient, instead of smooth one.

There are several ways to do outline, most common are:
1) Post-processing effect, like one in Borderlands. Applied to whole frame, works fast with complex scenes, good flexibility, won't work on mobile.
2) Rendering same model second time, with front face culling, and shader, that moves vertices outwards a bit, and paints everything black. Will work on mobile, thick line will look ugly. Can be set to each object separately. Will hit performance if set to every object in a scene.

-------------------------

ghidra | 2017-01-02 01:08:14 UTC | #3

as well, the effect you are refering from pokemon is specifically an edge detection shader. Putting a black pixel where it finds a huge color difference in the normal gradient. Which is a post process as bananaft mentioned.

I've made a very basic edge detection shader "tutorial" (that I'm not even sure works anymore, I need to actually check soon) , that I have plugged a few times on this forum, here:
[nervegass.blogspot.com/2014/12/u ... ction.html](http://nervegass.blogspot.com/2014/12/urho-shaders-edge-detection.html)

-------------------------

adekto | 2017-01-02 01:08:14 UTC | #4

thank you both for the response, as i see it the double model way (that looks allot like Okami) is not what im after and i think pokemon for 3ds is using the edge detection,
therefor im confused why this wont work on mobile? wen the 3ds PICA200 isnt that powerfull compared to current mobile

thank you for this older edge detection example, im going to try it

-------------------------

Bananaft | 2017-01-02 01:08:14 UTC | #5

[quote="adekto"](that looks allot like Okami)[/quote]
That's an extreme case. If your outline is only 1-2 pixels wide, this method can produce decent result.

[quote="adekto"] is not what im after and i think pokemon for 3ds is using the edge detection,
therefor im confused why this wont work on mobile? wen the 3ds PICA200 isnt that powerfull compared to current mobile[/quote]

All post-effects is very expencive on mobile because of poor memory bandwith. After all, phones are not made for games, and there are thousands of them.

Pokemon devs had to optimise their game for only one device, that was made for games. They knew their limits.

-------------------------

