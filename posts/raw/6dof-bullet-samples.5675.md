Lumak | 2019-10-19 23:24:16 UTC | #1

6Dof samples can be found here [https://github.com/Lumak/Urho3D-Constraint6DoF](https://github.com/Lumak/Urho3D-Constraint6DoF)

1 - ship on a rail example
2 - hoverbike

-------------------------

Lumak | 2019-10-20 14:48:36 UTC | #2

It's been a while since I made a video and thought it might be worth making one for this.
https://youtu.be/jsGpg6I-UH8

-------------------------

johnnycable | 2019-10-20 15:24:40 UTC | #3

Eh eh, it reminds me of good 'ol Battlezone

-------------------------

elix22 | 2019-10-21 05:41:29 UTC | #4

As usual , very nice demo :slightly_smiling_face:

-------------------------

Modanung | 2019-10-22 14:49:13 UTC | #5

Seems like this would make a great PR.

Could this constraint also be used to prevent raycast vehicles from toppling over, btw?

-------------------------

Lumak | 2019-10-23 01:11:51 UTC | #6

Yes, you can configure a vehicle to not turn over, and you can use it to assist in turning because bullet's raycastvehicle has a hard time doing that at high speeds.  Also, you can put wheels on that hoverbike and make it a motorcycle, although, you'll probably have to tweak the dynamics to behave more like a motorcycle.

-------------------------

QBkGames | 2019-10-23 01:21:57 UTC | #7

Would definitely be nice to have this as part of the Engine (version 1.8 ?) and the hover demo as a sample.

-------------------------

QBkGames | 2019-10-23 01:24:41 UTC | #8

Would you also be able to add the Fixed constraint, where 2 objects are stuck together, to Urho3D physics system? I think it can have its uses.

-------------------------

Lumak | 2019-10-24 12:54:23 UTC | #9

There are other Constraints that's already implemented in Urho3D where you can stick objects together. Understanding about ERP and CFM and how they work might be helpful. I know I keep referring back to this page, http://www.ode.org/ode-latest-userguide.html#sec_3_7_0 , just to refresh my memory.

-------------------------

coldev | 2019-11-04 00:54:14 UTC | #10

thanks lumak AAA examples, unity3d quality . ... 

thanks

-------------------------

Lumak | 2019-11-06 04:43:46 UTC | #11

Update hoverbike: added softpitch limit, corrected reverse direction, and changed camera functionality.

-------------------------

extobias | 2020-05-25 18:31:22 UTC | #12

hi @Lumak
This is great stuff. I've tried this but it seems there is some kind of problem. Sooner I press any key, the hoverbike is overturned. And the rail sample is not showing correctly. 
I've use a clean build from master repo. And comment some lines in Constraint6Dof.cpp:166, because AttributeInfo dont have offset_ property. Maybe that is failing.

![constraint-6dof|540x304](upload://6uZGHd2KP7CP3s0MBm9BpE47qh1.gif)

-------------------------

extobias | 2020-05-26 16:03:15 UTC | #13

Nevermind, some virtuals where missing in Constraint.h :sweat_smile:

-------------------------

Lumak | 2020-05-26 23:39:45 UTC | #14

Oh, good to hear it's working for you. I was concerned that version 1.7 was somehow not backward compatible with the latest.

-------------------------

