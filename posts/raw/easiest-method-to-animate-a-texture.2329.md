TheComet | 2017-01-02 01:14:47 UTC | #1

Say I had a model of a computer and I wanted to texture the screen of the computer with one of these 6 frames:

[img]http://i.imgur.com/5zlFZi9.gif[/img]

What would be the best approach switch textures dynamically? Should the 6 frames be put into an atlass and the UV coordinates be changed, or should the 6 frames be separate textures (or something else)?

-------------------------

Enhex | 2017-01-02 01:14:47 UTC | #2

There are several approaches I can think about:

a frame for each state.

single frame, animate the mesh so it exposes more every stage.

UIElement for each bar. Can have a single white bar texture and tint it with the color.

-------------------------

