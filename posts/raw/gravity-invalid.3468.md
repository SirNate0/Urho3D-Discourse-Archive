ChunFengTsin | 2019-05-23 13:20:02 UTC | #1

Hello everyone , 

I make a demo , learn from a open game "KO".
After I import character to scene, it can be control to move , and the physics is well when collision happen.

But the confusion to me is : gravity invalid for the character.

My core code  here （Hero inherit from Controller）:
 
Hero->
![2017-08-21 00-27-01屏幕截图|690x423](upload://gwXqI2kPUcyexgVO8ciBK0OI4H7.png)




Controller->
![2017-08-21 00-26-31屏幕截图|690x196](upload://zbmBlM3yVNPonOS2G3dBa24L5GH.png)


And  load scene code:
![2017-08-21 00-30-13屏幕截图|690x328](upload://jJIguC8sTbdiETOAj3clMVNVp5e.png)



scene in editor:

![2017-08-21 00-30-41屏幕截图|690x388](upload://4YkMb2itfdswDhRueauhcNYbsfF.png)





when game running , character in sky ,do not drop to ground, everything else is normal


someone can help me ,thanks !

-------------------------

Eugene | 2020-02-12 05:07:47 UTC | #2

I see that you intentionally disabled rigid body movement along Y axis (linear factor)

-------------------------

ChunFengTsin | 2017-08-20 21:54:20 UTC | #3

oh oh,thanks very much, I am so sorry , I have not understand the LinearFactor before .

But now ,you see that  AngularFactor is UP , it is only rotation on Y axis?
 why my character will fall  when it walk on  ground not flat ?

-------------------------

Eugene | 2017-08-20 21:13:34 UTC | #4

I don't know. Try to set angular factor to zero. You probably don't need even yaw rotation for the collider.

-------------------------

Modanung | 2020-02-12 05:08:18 UTC | #5

[quote="ChunFengTsin, post:3, topic:3468"]
But now ,you see that  AngularFactor is UP , it is only rotation on Y axis?
[/quote]

Yes, that is correct.

-------------------------

