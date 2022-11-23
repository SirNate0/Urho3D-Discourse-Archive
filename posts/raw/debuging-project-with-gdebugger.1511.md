codingmonkey | 2017-01-02 01:08:12 UTC | #1

hi folks
I try figure out with debugging though gDEBugger.
I find strange biggest texture in my project 2048x3072 (12mb) 
Actually i do not create this texture.
What's is this?
[url=http://savepic.su/6541290.htm][img]http://savepic.su/6541290m.png[/img][/url]

and others expected textures
[url=http://savepic.su/6543338.htm][img]http://savepic.su/6543338m.png[/img][/url]

-------------------------

cadaver | 2017-01-02 01:08:12 UTC | #2

That's a point light shadow map with 6 sides unrolled. Probably you could lower the shadow quality for any point lights you use.

-------------------------

codingmonkey | 2017-01-02 01:08:12 UTC | #3

Now i understood, thanks
I guessing this value set ratio for this kind maps
[url=http://savepic.su/6521600.htm][img]http://savepic.su/6521600m.png[/img][/url]
after changing this from 1 to 0.5 it become twice smaller

And other question:
Am I right? What application in most time spent in calling this two function again and again ?
[url=http://savepic.su/6494976.htm][img]http://savepic.su/6494976m.png[/img][/url]

-------------------------

