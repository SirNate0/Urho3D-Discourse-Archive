Eugene | 2018-06-10 09:03:22 UTC | #1

I just wanted to do something.
It took about a week of evenings.
Assets are _not_ mine.
Beware of heavy GIFs below (up to 40MB).
![01A|690x389](upload://lJ41Ut3rS3WOifyVBY0wQcAuSLk.jpg)
![01B|690x389](upload://v8d2wBBWccEpOdU8daRR1QnF3Qc.jpg)
![A01|690x389](upload://cAexv8kK02sO44FyHBL953R7COh.jpg)
![A02|690x389](upload://uMjFUUxfPFVLGsaCnEVDsO1S0yK.jpg)
![B01|690x389](upload://fdzfYUZoFfhrny15ia7N52R19Ti.jpg)
![B02|690x389](upload://cf4FYYAhzFN907lRDelI91a03JI.jpg)
https://media.giphy.com/media/w9d4Co3fX913SiBqCV/giphy.gif
https://media.giphy.com/media/5BWVHdvEJarfjfZaxv/giphy.gif
______
This is _not_ code exchange.
Re-check your equipement before looking at the code if you are brave enough to even open it.
All sources are here:
 https://github.com/eugeneko/Urho3D/tree/sample-77
Source/Samples/77_Oddball
bin/Autoload/LargeData/77
bin/Autoload/LargeData/Shaders

Tested only with DX11.
Grass animation works only with DX11.

Assets info is here:
 https://github.com/eugeneko/Urho3D/blob/sample-77/bin/Autoload/LargeData/77/README.txt

-------------------------

smellymumbler | 2018-06-10 18:45:25 UTC | #2

One thing that really bothers me with Urho, but I never found a way to tweak it, is how jaggy vegetation and shadows tends to look like. Is there any config that I'm missing on my materials? Did you manage to find a way to fix it?

-------------------------

Eugene | 2018-06-10 21:53:41 UTC | #3

There's one trick that I found helpful and it has nothing to do with Urho.
You should carefully prepare foliage LODs so they doesn't get too sparse.
In other words, LOD calculation shall be conservative and preserve as much non-transparent pixels as possible...
![image|690x339](upload://aPBq1o0XjuPDrME1bGyOFTQPIaM.jpg)

Alpha to Coverage plus MSAA x4, if properly used, may help too.
It has it's own issues tho.
 https://medium.com/@bgolus/anti-aliased-alpha-test-the-esoteric-alpha-to-coverage-8b177335ae4f
It shall be configured more thoughtfully than just turning switches on like I did below, but it’s enough to get an idea:
![image|689x234](upload://ngPiIS4zJ0z25QfSXPCHjlalnhj.jpg)

-------------------------

Miegamicis | 2018-06-11 06:34:58 UTC | #4

Looks really great!
Compiled and ran it on Ubuntu 16.04 and everything seems to be working except the grass animations as you already mentioned. I always thought that vegetation was one of the missing samples in this project and it could be great if someday it can be created in the master repo.

-------------------------

Eugene | 2018-06-11 09:27:43 UTC | #5

BTW it’s quite easy to port grass shaders for OpenGL. Add some attributes, copy paste code... maybe I’ll do it next time when I touch this code.
DX9, on the other hand, doesn’t allow to sample textures in vertex shader and cannot support all these animations.

-------------------------

smellymumbler | 2018-06-12 15:07:48 UTC | #6

Are these artifacts caused by bad LODs?

![image|689x234](upload://hwYqfI7U6X3oDIayRENUlLyhldW.jpg)

-------------------------

smellymumbler | 2018-06-12 15:41:56 UTC | #7

Runs well on a shitty Intel 4th and Ubuntu:

![image|649x500](upload://8w3pqXVuWAmuPq62IM6lLO1XDov.jpg)

-------------------------

Eugene | 2018-06-12 16:06:34 UTC | #8

Grass noise appeared when I enabled MSAA, don’t know why. Maybe texture mode was set to wrap implicitly. 
Tree model itself is quite strange. It seems it was designed to have one-sided leaves. At least, I had artifacts when made leaf material two-sided. I don’t know.

-------------------------

slapin | 2018-06-12 19:03:09 UTC | #9

Cool, how did you port shaders?

-------------------------

smellymumbler | 2018-06-12 20:16:03 UTC | #10

Didn't port anything. Cloned, built and it worked well.

-------------------------

