nevil2142 | 2020-02-03 19:15:35 UTC | #1

Hi everyone.
I develop 3D chart system with UrhoSharp and i stacked on why my object glows.
Cuz of it, there's pretty difficult to see on it.
Can someone help me, what am i doing wrong?
![1|502x499](upload://eCciLC0bUt8zYZqLk2uhwgwBHjN.jpeg)

-------------------------

GodMan | 2020-02-04 15:08:50 UTC | #2

Looks like from the image that you made everything glow. Like a bloom filter on the whole scene, and not really a glow to each object. Like a glow mask for the spheres and not the whole scene.

-------------------------

Bananaft | 2020-02-04 15:08:50 UTC | #3

Hi, welcome to the forum!

Please specify what renderpath you are using, and have you added any post-effects to it?

-------------------------

nevil2142 | 2020-02-04 15:09:46 UTC | #4

Thank you, from your message searched how to disable Bloom and find it as SetEnabled("BloomHDR", false)

-------------------------

