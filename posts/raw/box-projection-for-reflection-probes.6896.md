cmd | 2021-06-16 11:29:19 UTC | #1

Related to discussion:
https://discourse.urho3d.io/t/use-skybox-material-as-reflection-source/3016

I had some success implementing the HLSL and GLSL shader code changes to use box projection for the reflection probe. I've not generalised it yet, and it probably needs to be made optional for Zone environment (or more generally on TextureCube mapping). It is also currently based on the assumption that the zone bounds matches the required bounds for the box projection, which may not always be the case. Also assumes Zone bounds is in world space. For these reasons I decided not to make a PR out of it yet, but can provide details of what I changed if anyone is interesting in taking it further.

Here is my test scene, prior to my shader changes: 
![image|653x499](upload://utummndsjADcq7YZ2ppOojv6Gdt.jpeg)

An here is the same scene with my box projection shader changes:
![image|650x499](upload://hTVFf57JloZpCTeLnDnQpTaA6mQ.jpeg)

-------------------------

