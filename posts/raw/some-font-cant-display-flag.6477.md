spwork | 2020-10-30 06:15:09 UTC | #1

![image|506x500](upload://ppka2p8jJlUN94HY4OdOIHF0EgX.png) some font can't display '-' flag,but that font can display '-' n other applications
![image|280x144](upload://2zvfcRgNS3huqCkZcXzA23aGybG.png) 
,how should i fix it?

-------------------------

SirNate0 | 2020-10-29 14:14:33 UTC | #3

Pretty sure it's a known issue. Unfortunately, I have no idea how to fix it. My suspicion is that it's some sort of off-by-one bug where a font library is using base 1 positions and we are using base 0 positions or it is saying the bounds of a character are given as a rectangle with the upper bounds meant to be included and we treat it as upper bounds that are meant to be excluded. But I have no evidence for that, so take it with a grain of salt.

https://github.com/urho3d/Urho3D/issues/2638

-------------------------

Modanung | 2020-10-29 17:08:24 UTC | #4

Then, maybe this could fix that *per font*?
https://fontforge.org/en-US/

-------------------------

Modanung | 2020-10-29 22:51:42 UTC | #5

https://discourse.urho3d.io/t/ui-not-displaying-minus-sign-with-most-fonts/6163/5?u=modanung

-------------------------

spwork | 2020-10-30 06:15:18 UTC | #6

https://discourse.urho3d.io/t/ui-not-displaying-minus-sign-with-most-fonts/6163/4?u=spwork
I use this to fix it.

-------------------------

