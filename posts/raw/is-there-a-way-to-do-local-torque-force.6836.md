evolgames | 2021-05-08 04:35:14 UTC | #1

I have a helicopter with a rigidbody that I hover with upward force and steer and pitch with torque. However, the problem I get is that once you have turned, if you adjust the pitch it becomes a roll. I prefer torque forces here because it gives nice realistic motion. But is there any way I can make the Torque's vector direction local to itself? Or do I need more nodes or something?
It's weird because ApplyForce works fine if I multiply the rotation of the body by my up vector, resulting in it "lifting" wherever its top is. This allows you to lean forward to travel forward, like a real helicopter. Is there an Urho function for what I need to do?

-------------------------

Modanung | 2021-05-08 08:49:54 UTC | #2

Could you show the code where you apply the torque and forces?

-------------------------

evolgames | 2021-05-08 15:31:46 UTC | #3

Yeah sure, it's simply:
```
self.hullBody:ApplyTorque(Vector3(self.curAccel, 0, 0) * self.tiltForce)
self.hullBody:ApplyTorque(Vector3(0, self.steering, 0) * self.turnForce)
```

-------------------------

Modanung | 2021-05-08 16:23:02 UTC | #4

Try using something like:
```
self:GetNode():GetRight() * self.curAccel * self.tiltForce
self:GetNode():GetUp()    * self.steering * self.turnForce
```
...as arguments.

-------------------------

evolgames | 2021-05-08 16:29:06 UTC | #5

Hm no, that looks like it does the same thing

-------------------------

Modanung | 2021-05-08 21:04:46 UTC | #6

*Exactly* the same? :confused:

Is  `self:GetNode()` the same as `self.hullBody:GetNode()`?

-------------------------

evolgames | 2021-05-09 01:57:48 UTC | #7

Yeah the hullbody rigidbody is a component of self.node. Switching to self.hullBody:GetNode() produces the same result

-------------------------

Modanung | 2021-05-11 19:03:52 UTC | #8

Got repo?<super></super>

-------------------------

evolgames | 2021-05-11 19:18:36 UTC | #9

Oh no it's all local in my project folder

-------------------------

