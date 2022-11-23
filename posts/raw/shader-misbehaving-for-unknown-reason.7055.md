Batch | 2021-11-14 02:06:31 UTC | #1

I'm playing around with an Underwater sample, and the shader for submersion draws incorrectly sometimes. When I tell the render path to enable the "Underwater" tag there's a good chance based on what's currently being rendered that the shader wont draw properly. If the "Underwater" tag is enabled as soon as possible, then it works 90% of the time. I have no idea what could be going wrong.

https://imgur.com/a/l33PksD shows the failure (top image) and the success (bottom image). To generate these images, I simply ran the test app (the shader failed), hit print screen, closed the app, ran it again (the shader worked this second time with no changes on my part), hit print screen, and closed the app.

Seems like some kind of initialization problem. I can append the shader code and xml files if it'll help.

-------------------------

GodMan | 2021-11-14 18:34:34 UTC | #2

So going to be honest on this. This may be hard to track down. Are you getting any error messages in the console window?

-------------------------

JTippetts1 | 2021-11-14 20:22:52 UTC | #3

One thing to look into is to make sure your shaders are getting all the vertex and texture inputs they need. If a shader needs, ie, tangent coords, make sure it is getting proper tangent coords or it will just use whatever random bullshit is left in there. Same thing with textures. If a texture slot is used, make sure a texture is being bound to that slot or it'll just get random bullshit. Sometimes the random BS is okay-ish and the shader might seem to work, but then something in a frame is different and it doesn't work anymore. It all depends on chance and whatever order things happen, and what data gets written to where and it can seem pretty weird.

-------------------------

GodMan | 2021-11-14 20:54:48 UTC | #4

Sometimes in my cases my issues was that I forgot to use a parameter in the material file that the shader needs. So at certain camera angles the shader appeared to be working, but with other angles the shader had strange results.

-------------------------

