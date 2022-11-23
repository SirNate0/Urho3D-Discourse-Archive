hiddenworlds225 | 2017-08-09 23:05:34 UTC | #1

Hi im new to Urho3D and I just want to know two things:  How Do I start Urho3D and why isnt the mouse connected to the game? Going into more detail for the mouse, I searched the forums and found this Thread:  https://discourse.urho3d.io/t/keyboard-keys-not-working-on-rpi-platform/2335/8

It  talked about the keyboard at first, but then to the mouse. I saw that the keyboard was fixed but not the mouse.. 

That caught my attention for a moment, but not enough until i tried the demos, then my screen was screwed in the background.

If you know a way to fix this please tell me, and also @weitjong if you are reading this, I know you are extremely busy and you were the one that fixed the keyboard problem, when can you fix this if possible?

-------------------------

hiddenworlds225 | 2017-08-09 23:18:59 UTC | #2

Ok I figured out the first question but it is UNRESPONSIVE.

Why is that?

-------------------------

weitjong | 2017-08-10 13:06:45 UTC | #3

Welcome to the forum. As you know Urho3D project is cross platform, so you need to tell us which platform are you targeting. Assuming you are targeting RPI platform, the keyboard/mouse handling problem on RPI has been fixed quite a while already and it was actually a bug from upstream SDL library. The last time I booted into my RPI to check, all is good, except for a known caveat on RPI where its graphics driver has limited amount of uniforms and thus we can only make RPI supports half of number of bones compared to other platforms. So certain demos produce rendering artifact. Is that what you saw? The demos (and the assets) are not designed specifically for RPI in mind. As for the responsiveness, have you killed the X and GNOME/KDE desktop environment? We need all the computing resource to be allocated to Urho game engine.

-------------------------

