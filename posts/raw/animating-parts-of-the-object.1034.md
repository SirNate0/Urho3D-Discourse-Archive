v0van1981 | 2017-01-02 01:04:58 UTC | #1

How to animate multiple parts of the object together? For example  walking animation for legs and firing animation for hands.
p.s. Sorry For My Bad English.

-------------------------

cadaver | 2017-01-02 01:04:58 UTC | #2

You can blend animations partially using the following:

- You can set a StartBone for the AnimationState, which means the animation will only be applied from that bone onward in the hierarchy (easiest)
- You can control AnimationState blend weights per bone (harder, but more precise control)
- Finally using the AnimationState Layer setting you can control the order the animations get blended in. Higher layers = blended later, which means they will have higher priority in case of conflicts.

-------------------------

v0van1981 | 2017-01-02 01:04:59 UTC | #3

thank you

-------------------------

