OMID-313 | 2017-01-02 01:14:39 UTC | #1

Hi everyone.

I just successfully installed Urho3D on Ubuntu 14.04 (on VMware on Win 7).

But when I run 
[code]. NinjaSnowWar.sh[/code]
it gives a blue screen like this:

[img]http://uploads.im/Z6mdS.jpg[/img]

[url]http://uploads.im/Z6mdS.jpg[/url]

and nothing else appears. The controls also don't work.

How can I solve this problem !!?

-------------------------

cadaver | 2017-01-02 01:14:39 UTC | #2

This looks like something is off in the OpenGL / GPU driver. You could try the -gl2 switch on the command line to force Urho3D to use OpenGL 2.

-------------------------

OMID-313 | 2017-01-02 01:14:39 UTC | #3

[quote="cadaver"]This looks like something is off in the OpenGL / GPU driver. You could try the -gl2 switch on the command line to force Urho3D to use OpenGL 2.[/quote]

Thanks @cadaver for your reply.

I tried the following command:
[code]root@ubuntu:/home/omid/Urho3D/bin# . NinjaSnowWar.sh -gl2[/code]
But nothing changes.

Is there any other command I can combine with -gl2 !?

-------------------------

cadaver | 2017-01-02 01:14:39 UTC | #4

If -gl2 doesn't work then there's nothing more Urho can do to make itself work on a broken OpenGL implementation, so you need to fix your environment. Unfortunately I can't help you in more detail.

-------------------------

OMID-313 | 2017-01-02 01:14:39 UTC | #5

When trying different keys, I realized that after pressing F3 key, the screen changes to wireframe mode, and I was ablo to play the game.
Here is a picture:

[img]http://uploads.im/Mdokr.jpg[/img]

[url]http://uploads.im/Mdokr.jpg[/url]

Ok. Now what should I do to solve the OpenGL/Graphics-Card/GPU problem?

-------------------------

OMID-313 | 2017-01-02 01:14:39 UTC | #6

Any suggestions please !!!!?!

-------------------------

Sir_Nate | 2017-01-02 01:14:42 UTC | #7

Try updating the driver (try the proprietary one if it exists and you are not using it). Consider also googling for problems associated with your graphics card and/or the VMware with a graphics card and solutions people have found for them.
My personal guess is that it is a problem with VMware or your configuration of VMware. Consider changing the Accelerate 3d graphics setting under Virtual Machine > Settings > Display.

If you are able, I would actually go with a dual-boot setup for Ubuntu and Windows (which is what I use). I've never used Ubuntu through VMware, so I can only speculate as to what may be the cause of your problem...

-------------------------

rasteron | 2017-01-02 01:14:43 UTC | #8

I have almost the same setup as yours but only I'm using Virtual Box. You should first sort out your driver setup and check if it is running. 

Were you able to run glxgears?

-------------------------

