GoldenThumbs | 2019-08-06 20:51:14 UTC | #1

I've been working on soft shadows. I am getting good results for Spot and Directional lights, but not point lights. I know why too. Point lights use 6 different cameras to achieve omni-directional shadows. This works really well most of the time, but when I'm blurring the shadows it reveals the seams where the edges of the different depth textures meet. ![PNG|690x378](upload://bExFAGEib67mep8GCsTCjUgvpW5.jpeg) 
Point Light
![softshadow_directional|690x366](upload://od9Aq6FudTGtrJ88HgF7ZqmO0dV.png) 
Directional Light

-------------------------

Leith | 2019-08-07 05:59:40 UTC | #2

We'll cover cascading shadow maps shortly, have patience

-------------------------

Sinoid | 2019-08-10 06:44:42 UTC | #3

Which space are you doing the blurring in?

Point-lights and directional lights (if more than 1 cascade) atlas their individual tiles. In the case of cube-maps that's what the `indirection cube` is for - finding the tile. So you can't blur or dither in shadow-texture-space without the risk of crossing the tile boundaries.

The directional light cascades have some extra *fill / waste* space (from frustum fitting) that would make the problem less readily presented, it's probably still there though if cube-maps are doing it.

-------------------------

Modanung | 2019-08-10 11:40:23 UTC | #4

I guess we could use the same technique for blurring skyboxes?

-------------------------

GoldenThumbs | 2019-10-07 21:20:26 UTC | #5

*waits forever to respond* Welp, I don't think I actually ever read this until now. I get what you are saying though, I wasn't sure there was another way though. I HAVE been blurring in texture space. Is there another way to do it? I'm using pretty standard PCF filtering now.

-------------------------

SirNate0 | 2019-10-08 03:02:17 UTC | #6

You could see if this approach will work for you. If I had to guess, you could even create the cubemap that way from the start by increasing the field of view of each of the 6 cameras, though you'd have to make sure everything else using the cubemap before you correct for that can handle the difference.

https://stackoverflow.com/questions/4353528/blurring-a-cubemap/4353670#4353670

-------------------------

GoldenThumbs | 2019-10-08 15:22:30 UTC | #7

Was looking at something written about [Tesseract](http://tesseract.gg/)'s omnidirectional shadows and it looks like they do exactly what you are suggesting to deal with the seams issue. http://tesseract.gg/renderer.txt ![TesseractShadows|690x22](upload://vWK2WNohrtJnhcDMBClcSbt6eIg.png)

-------------------------

