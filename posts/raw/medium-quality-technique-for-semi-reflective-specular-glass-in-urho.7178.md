najak3d | 2022-01-31 22:58:28 UTC | #1

We're wanting to emulate mostly reflective glass in our App.   Are there any existing examples in Urho that accomplish this?    Here's a crude sample of the effect we're wanting (this one is overdone and in Blender now):

![image|490x500](upload://bAMZUHxbXx7q4kAXDfthhEVkzjg.jpeg)

-------------------------

Lys0gen | 2022-02-01 00:14:34 UTC | #2

Sample 23 (Water) has a reflective (**not** air-)plane.

-------------------------

najak3d | 2022-02-01 04:32:37 UTC | #3

I'm thinking we'll setup Environment map of a Sky image for the reflection colors (not true reflections).  And then introduce some specularity and transparency.    That's my general idea for this.

-------------------------

