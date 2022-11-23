Askhento | 2021-11-01 10:46:27 UTC | #1

I am looking for a way to append shader defines for all commands. 

What i am currently doing : 
1) Creating empty RenderPath()
2) Looping through all commands and appending to vertexShaderDefines and pixelShaderDefines.
3) Append commands to new RenderPath, add all renderTargets
4) Set new RenderPath to viewport.

I see all the object in viewport, but define does not seem to pass inside the shader.

My question is related to other already asked [Update RenderPath and/or RenderPathCommand](https://discourse.urho3d.io/t/update-renderpath-and-or-renderpathcommand/1611), but I don't want to resurrect it. @cadaver?

-------------------------

Bananaft | 2021-11-07 08:33:19 UTC | #2

Why do you create empty path instead of just updating commands in your existing one?
Some suggestions:
-Check if it works on quad command before scene command.
-Edit XML file and see if it works.

-------------------------

Askhento | 2021-11-07 11:26:59 UTC | #3

I only need to update shader defines from angelscript.

-------------------------

JSandusky | 2021-11-08 08:47:13 UTC | #4

Steps 2 and 3 are backwards. 

Steps 1 and 2 in that order make absolutely no sense, that can do absolutely nothing.

... I want to kick a puppy now in frustration from reading that.

-------------------------

Askhento | 2021-11-12 16:22:35 UTC | #5

Well, at least I know that you are angry...

-------------------------

Eugene | 2021-11-12 17:18:37 UTC | #6

@Askhento, don't get bothered too much about it, I think @JSandusky is the most angry person on this server. Also, one of the few people who really know the insides of Urho.

-------------------------

JSandusky | 2022-03-10 06:41:40 UTC | #7

But don't worry, it's usually figuratively angry. It's rarely angry angry. Take it as poorly phrased snark.

In this case I was upset because I delved through code thinking something could be wrong, and delved into it for about an hour before I realized, "*no, it's the user*." Hence, I wanted to kick a puppy (not something I'd ever do, I only eliminate feral dogs).

Don't worry, I'm more snark than bite

-------------------------

