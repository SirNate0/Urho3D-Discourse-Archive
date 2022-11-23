bukkits | 2017-01-02 01:06:09 UTC | #1

[img]http://i.imgur.com/su9oxCT.png[/img]


The linked image is from Crowd Navigation. The black is the terrain and objects. The white is the character. All samples have this error, and I suspect that there is a similar problem in the editor as well, but I haven't explored it enough to confirm.

It looks like materials aren't loading to me, but I'm new to Urho3D, so if anyone knows what might be going on I would be very excited to get this fixed.


Linux Mint 17.1
Radeon mobile card with mesa graphics drivers

If you think that this is a hardware issue I can get a full dump of system specs.

-------------------------

rasteron | 2017-01-02 01:06:09 UTC | #2

This looks like a mesa driver or shader issue but I'm not sure. I have a Ubuntu 64 VM with old Nvidia drivers and it renders ok with Urho3D.

-------------------------

bukkits | 2017-01-02 01:06:10 UTC | #3

I'm hoping it's not the mesa drivers, but I wouldn't be too shocked either. 

Is there more detailed log information that I can get besides just loading from terminal? It doesn't report any problems that I can see.

-------------------------

rasteron | 2017-01-02 01:06:10 UTC | #4

[quote="bukkits"]I'm hoping it's not the mesa drivers, but I wouldn't be too shocked either. 

Is there more detailed log information that I can get besides just loading from terminal? It doesn't report any problems that I can see.[/quote]

Logs are located on: [b].local/share/urho3d/logs[/b] in your home or root directory.

In any case, you should post your full system specs so others could help you out and may have a solution.

-------------------------

JimMarlowe | 2017-01-02 01:06:13 UTC | #5

I run Mint also and see this, add -gl2 to the command line.

-------------------------

bukkits | 2017-01-02 01:06:18 UTC | #6

Oh, guessing that just forces OpenGL 2?

What is the default, and is there any reason that this would be a common issue on Mint? Are you using Mesa drivers as well?

-------------------------

thebluefish | 2017-01-02 01:06:19 UTC | #7

Default is OpenGL 3.2 (or DX9 on Windows). The update to OpenGL 3.2 is relatively recent, so I'm not surprised there's a particular problem with the mesa drivers.

-------------------------

bukkits | 2017-01-02 01:06:19 UTC | #8

Forcing OpenGL 2 immediately fixed the issue with lighting and/or materials and textures

however...



[img]http://i.imgur.com/vW8qM8U.png[/img]

-------------------------

rasteron | 2017-01-02 01:06:20 UTC | #9

Hey bukkits,

I do now have a related OpenGL problem with my recent build using Intel HD Gfx with my Core i3 laptop (Win 7 64) but not a problem on older engine versions. Just submitted an issue earlier.

BTW, did you use the milestone 1.4 or latest from the repo?

-------------------------

JimMarlowe | 2017-01-02 01:06:21 UTC | #10

Going back thru my notes, this did start at 1.4.0, but only on my laptop, a Lenovo G585, with AMD/ATI, and Mint Linux 17, my desktop with Mint 17 has no problems. I added "-gl2 -noshadows " to get around it, though what is life without shadows? My notes also say that you need to add "-lqshadows -tq 1" on an RPI to make it run and not hang with V 1.4.

-------------------------

bukkits | 2017-01-02 01:06:21 UTC | #11

Okay interesting.

I am using the latest version of Urho, cloned from the github repo. That may be my issue. I'll try stepping down a version and see if I get different results. I also dug up an old laptop that only has integrated graphics, and I'll see if I get different results. That might be able to rule out hardware or drivers.

-------------------------

thebluefish | 2017-01-02 01:06:21 UTC | #12

Try the stable 1.4 release.

-------------------------

