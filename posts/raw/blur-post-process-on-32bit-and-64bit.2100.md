Miegamicis | 2017-01-02 01:13:04 UTC | #1

On Urho3D 1.5 32bit version the blur effect looks like this
[img]http://i.imgur.com/KP0uoqS.png[/img]


But on the 64bit version, it looks something like this. 
[img]http://i.imgur.com/muMioLR.png[/img]

Both images should look similar, but they're not, when I look around the world in 64bit version the screen just flickers in different colours, it seems that the screen is only showing the dominant colour of the viewport. 
It seems that on 64bit systems the blur doesnt work at all, does anyone know how to fix this? 
Thanks!

-------------------------

rasteron | 2017-01-02 01:13:04 UTC | #2

Hi,

I'm not sure cpu architecture/build have something to do with post effect results. Probably best to post your details like OS, engine version, etc.

It would also be better to clone or download the latest version, build and check it again.

-------------------------

cadaver | 2017-01-02 01:13:05 UTC | #3

While working on the api-agnostic-header branch I briefly tested this on a VS2013 64bit build. Blur worked OK for me on all of D3D9, D3D11 and OpenGL.

Ah, it could of course be a bug that was fixed post 1.5; don't remember; you could retry against the current master branch.

-------------------------

