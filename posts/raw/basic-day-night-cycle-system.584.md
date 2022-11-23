rogerdv | 2017-01-02 01:01:31 UTC | #1

I was thinking to implement some basic day/night cycle in my game, as the view is isomtric, I dont have to worry about changing sky, only simulate the sun/moon movement. I thought that I could simply rotate the directional light in X axis (assuming that X/-X is east/west) n degrees per game "minute". Do you think this could work? 
The most important detail Im missing here is the light color or intensity variation according to time, can somebody illustrate me about what values to use for dawn, dusk, moon light, etc?

-------------------------

ghidra | 2017-01-02 01:01:32 UTC | #2

I was curious the answer to this question. 
Did a quick google and found this post: [opengl.org/discussion_board ... ycle-light](https://www.opengl.org/discussion_boards/showthread.php/167751-day-night-cycle-light)

Simply:
1) full sun : 255,255,220
2) dawn/dusk, linear fade to : 255, 60, 60
3) then to : 0, 0, 0
During 2, spawn a second light source, like the moon, with a blueish tint, like 20, 60, 180, placed 180? opposite to the sun.
Don't forget to rotate both lights around your scene.

-------------------------

codingmonkey | 2017-01-02 01:01:32 UTC | #3

I would like to try to make a 1D texture with gradient daylight (colors theme: sunrise > morning > day > evening > night), and would make a sample of it in the shader, and multiply to the primary color of the material.

-------------------------

