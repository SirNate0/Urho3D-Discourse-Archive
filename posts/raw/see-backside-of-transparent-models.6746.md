Lunarovich | 2021-03-03 08:09:30 UTC | #1

I've tried many combos of materials and techniques and yet can't achieve the simple effect of seeing backsides of a transparent object. Namely, I get this:

![screen11|395x500](upload://li80eZ1M3wxfsXaUmY26cmLkZFw.jpeg) 

As you can see the backsides of the cubes are invisible. I've tried to to set `cul` to `none`, to set `occlusion` to false, to use unlit material, to use different blends, lie `alpha`, `addalpha`, but nothing seems to work. I expect backsides to be less transparent (darker) due to some sort of blending of front faces and backfaces of the cube - this can be seen on the image above when models overlap.

What I want to achieve is something like this ![cube](https://upload.wikimedia.org/wikipedia/commons/7/78/Hexahedron.jpg). 
Normally, I understand that edges would require a line shader, so I'm not talking about that. Just about the visibility of the backsides.

Thank you very much!

-------------------------

Eugene | 2021-03-03 07:33:25 UTC | #2

[quote="Lunarovich, post:1, topic:6746"]
I’ve tried to to set `cul` to `none` , to set `occlusion` to false, to use unlit material, to use different blends, lie `alpha` , `addalpha` , but nothing seems to work.
[/quote]
Depth write should be disabled for transparent objects, too.

-------------------------

Lunarovich | 2021-03-03 07:48:00 UTC | #3

Thanks. `depthwrite` is also set to false, i've just forgot to mention it.

-------------------------

SirNate0 | 2021-03-03 16:02:22 UTC | #4

Just wanted to check, you said you set `cul` to `none`, but that's spelled wrong. When you tried it, did you actually use `cul`? And are you sure you're not seeing the back faces? Without the edges, the overall cube would just look a bit darker/bluer than when it is not on, like the overlapping cubes in the picture.

-------------------------

Lunarovich | 2021-03-04 07:37:05 UTC | #5

@SirNate0 Sorry, it was just a spelling mistake here. In the code, I've checked it with `grep` (a tool for reg exp), it's correct, it's `cull`. Model actually has two geometries. So I've set the "edge" geoemtry to `cull` `none` and I see the "infrastructure". So this part is ok. 

However, as hard as I try, I don't get that "a bit darker/bluer" and that's what bothers me. No combo of techniques and material values seems to work.

-------------------------

Eugene | 2021-03-04 08:15:41 UTC | #6

![image|616x409](upload://3rLdcMkAuYkGbjVX20XuMHwO7nX.png) 
![image|516x459](upload://84YTbKIJsQn1HhOHKzxfTC0AXjA.png) 
![image|640x178](upload://pFCHVAn9ktsXCh2kK9NdUG4Ujlk.png) 
![image|690x149](upload://gXYv8wjwJRts9hSJZl3xV2EA0a7.png) 
I checked it and it works just as intendent.  These dirty patches are caused by messed up render ordering, which is expected.

In general, you have to render model twice, back faces and then front faces, with different render order, in order to keep it at least basic visual appeal.

-------------------------

JSandusky | 2021-03-05 04:46:50 UTC | #7

In some fringe cases you can use additive blending with negatives equaling the sum of the positive (like 0.5, -0.25, -0.25) for very limited OIT that only works for "*I need all of this same-colored tinted glass*" situations. It's difficult to hit precise colors that way though. You still have other probable sorting needs on top of it though that make it moot (particles, etc)

See 2nd answer of: https://gamedev.stackexchange.com/questions/43635/what-is-the-order-less-rendering-technique-that-allows-partial-transparency

-------------------------

Lunarovich | 2021-03-11 06:48:44 UTC | #8

@Eugene Thank you, I will try it. Do you render model twice in your cube example?

@JSandusky Thank you, I'll consult the article.

-------------------------

Eugene | 2021-03-11 10:21:14 UTC | #9

[quote="Lunarovich, post:8, topic:6746"]
Do you render model twice in your cube example?
[/quote]
Nope, I was lazy and I only disabled culling, and nothing more.

-------------------------

