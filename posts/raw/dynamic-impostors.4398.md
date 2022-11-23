smellymumbler | 2018-07-18 22:34:50 UTC | #1

I just saw this tech and was very impressed: https://www.youtube.com/watch?v=G0ILW1cwuTc

How does this thing work? Does it render the model separately with render-to-texture? Like, flag these meshes with a special flag, they get rendered to texture, use the texture instead? And that's done on scene load?

-------------------------

dev4fun | 2018-07-19 03:08:54 UTC | #2

lol that's amazing. But I agree with you, should be rtt in different angles (on video we can see a lot of cameras to make a 360 rtt). But i dont know about lightning and intersection...

-------------------------

SirNate0 | 2018-07-19 03:41:56 UTC | #3

I haven't watched the video yet if it addresses it, but I'm pretty sure you should be able to render the normals to a texture as well. You'd need to write a new shader for it, I think, but it shouldn't be too hard. Lighting might be more difficult, but if it is just outdoors you're probably only interested in the sun light and ambient lighting.

-------------------------

Eugene | 2018-07-19 09:49:08 UTC | #4

I'm 99% sure they draw color/normal/depth/etc maps.
The most interesting thing is how do they blend different maps.
The trailer is too fast, need more detailed vids.

-------------------------

smellymumbler | 2018-07-19 15:43:51 UTC | #5

Found more details:

http://wiki.amplify.pt/index.php?title=Unity_Products:Amplify_Impostors/Manual
https://forum.unity.com/threads/beta-release-amplify-impostors.539844/

-------------------------

Enhex | 2018-07-20 16:09:48 UTC | #6

I developed something similar few years ago and never got to use it. Used RTT.

-------------------------

