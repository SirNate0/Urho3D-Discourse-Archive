glebedev | 2020-10-11 13:45:05 UTC | #1

I've put together working unity script to convert Unity assets into Urho assets. 
https://github.com/gleblebedev/Unity2Urho

Here is how result looks like at the moment:
![image|690x372](upload://qbpgvB69NNohqH21HJlCrmypdQu.jpeg) 
![image|690x393](upload://zXhSqE1R47jIVzOjsvgp3CXZh9k.jpeg)

Just open a package manager in unity and add the package from git URL:
![image|306x118](upload://kM0zoO50Q9OF95NMc9SjjBRD8Ef.png) 

The URL is: [https://github.com/gleblebedev/Unity2Urho.git](https://github.com/gleblebedev/Unity2Urho.git)

Video instructions:

How add it to Unity project:
https://www.youtube.com/watch?v=McsQiEYu_5Y

How to create MDL file with LODs:
https://youtu.be/J21mRrnfkig

Exporting animation:
https://youtu.be/GyZyO6KM8NQ

Skyboxes and reflection probes:
https://youtu.be/rfZ1aU2Xa70

-------------------------

johnnycable | 2017-06-22 10:32:48 UTC | #2

Interesting. Can I ask you why are you changing for Urho from Unity? Urho is lightweight in respect to Unity, and no plugins...

-------------------------

glebedev | 2017-06-22 10:51:55 UTC | #3

I don't like Unity. Every time I've joined a Unity-centric team on a game jam it ended up being a disaster.

On other hand I love UrhoSharp - this is exactly what I need in my pet projects. Urho seems to be a small and efficient, not bloated with unnecessary features and very extendable.

So I would say it's a personal preference.

-------------------------

johnnycable | 2017-06-22 12:30:24 UTC | #4

Think the same, some tools are unnecessary heavy...

-------------------------

coldev | 2017-06-24 22:08:07 UTC | #5

thanks for this usefull script..

-------------------------

glebedev | 2017-06-25 23:10:01 UTC | #6

Transparency fixed + technique selection improved:

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/f7485db0ad16f951036a2d52ebb5bf8ef521f088.png'>

-------------------------

glebedev | 2017-08-01 21:48:48 UTC | #7

Now with heightmaps for terrain
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/b92cf85b17ef8267f66c0e82bc5942f450ba47fc.jpg'>

-------------------------

glebedev | 2017-08-01 21:44:22 UTC | #8

https://cdn.discordapp.com/attachments/235391394548547584/342033114845020170/unknown.png

-------------------------

smellymumbler | 2017-08-03 19:56:01 UTC | #9

Can you post the originals for comparison? Lighting sucks in Urho. :(

-------------------------

smellymumbler | 2019-05-23 13:20:01 UTC | #10

Also, what's with the artifacts? 

![sample|690x279](upload://n51inP8vLTeN84Cqv16mAAywDRI.jpg)
![sample2|690x280](upload://qOl64GFzaG1jBYkc11Ju4DFuEoQ.jpg)

-------------------------

glebedev | 2017-08-03 20:40:56 UTC | #11

I think these artifacts appear due to dynamic lighting. Unity use lightmaps and I don't know yet how to export them correctly.  Vanila Urho doesn't support lightmaps as they should be shared among multiple meshes.

Original assets utilize PBR rendering. I failed to extract cubemaps - Unity doesn't allow to read them in editor :frowning:

The latest source is available by the original link. You can try it on any other unity asset you have and report any issues you found.

The same asset in Unity and Unreal:
https://www.youtube.com/watch?v=Q3KUoWiTBbU

https://www.youtube.com/watch?v=WuGBwd3DyM4

-------------------------

glebedev | 2017-08-03 20:46:19 UTC | #12

I'm looking for someone who would help me to make the best Urho can deliver from the assets. The very first question people ask me about Urho3D - what level of graphics it could deliver. I believe that with right assets and shaders it could be quite good.

-------------------------

rasteron | 2017-08-03 21:02:52 UTC | #13

[quote="glebedev, post:11, topic:3274"]
Vanila Urho doesn’t support lightmaps as they should be shared among multiple meshes.
[/quote]

It does, but diffuse only and with alpha.

CoreData/Techniques/DiffLightMap.xml
CoreData/Techniques/DiffLightMapAlpha.xml

-------------------------

glebedev | 2017-08-03 21:18:31 UTC | #14

I mean: It does but not in a practical way. I can't create a unique material for each mesh in the scene. I should be able to keep original material + pass a second stream of UVs and lightmap texture for each static model.

The easiest way from my perspective at the moment - to merge all static geometry during the export and then put it in the scene as a single static model with generated materials based on original + lightmap. It's 100% doable... But I just don't have much time to do it. I want to make a small game first and as a result I'm updating the export script only when I need to add something that my game needs.

-------------------------

rasteron | 2017-08-03 21:25:30 UTC | #15

You can use different materials and share one lightmap texture on 2nd UV. Merging objects or a single mesh is of course great for mobiles or optimization.

-------------------------

smellymumbler | 2017-08-03 22:27:33 UTC | #16

Yeah, it definitely doesn't look as good as it could be. But it's not just the lightmap, IMO. The materials all look like plastic. Are they using the same specular configuration? Or do they have specular maps? Is Urho configured to read the speculars? 

As for artifacts, they shouldn't happen. Unity also has dynamic lighting and that does not occur. Same for other engines, like Ogre. Maybe it's the shadowmapping configuration needing some tweaks?

-------------------------

monkeyface | 2017-11-09 14:19:18 UTC | #17

I gave this a try with the Unity viking demo scene but my results weren't so successful :frowning:

![image|690x491](upload://oljoOrJUSvaaVu824oI1mJUpma8.jpg)

-------------------------

glebedev | 2018-12-10 12:47:53 UTC | #18

And a year later I've made some improvements to the script:
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/a/a07bf2949efe4a962ee988d8b0bee4025f3dda01.jpeg'>

I'll publish the fixed version later

-------------------------

glebedev | 2018-12-26 16:38:47 UTC | #20

Source code and unity asset are now available on github:
https://github.com/gleblebedev/Unity2Urho/

-------------------------

smellymumbler | 2018-12-26 16:48:12 UTC | #21

That's super useful. Thanks a lot for the hard work!

-------------------------

glebedev | 2020-06-01 23:16:40 UTC | #22

... And couple years later I've made few fixes for PBR compatibility:

https://i.gyazo.com/dbb37a48c1e43557a2d5908dba0676ff.jpg

-------------------------

glebedev | 2020-06-25 08:22:50 UTC | #23

I know 3 years passed... May I ask you to try again? I've fixed a lot of small issues and now it should be way better.

-------------------------

glebedev | 2020-08-10 09:06:47 UTC | #24

Now it converts all textures to compressed DDS format. it makes project loading times shorter.

-------------------------

HeadClot | 2020-08-17 06:54:16 UTC | #25

Hey is there a specific version of unity that I should use? Just curious :slight_smile:

-------------------------

glebedev | 2020-08-17 07:52:45 UTC | #26

I would guess any 2017+ version should work. If you have any troubles - open a ticket on GitHub.

-------------------------

HeadClot | 2020-08-17 07:59:13 UTC | #27

Noted and will do :slight_smile:

-------------------------

glebedev | 2020-09-18 08:05:47 UTC | #28

New feature: now it exports terrain trees. Also custom geometry naming is kinda fixed so you can export rivers and roads generated with R.A.M.

-------------------------

coldev | 2020-09-20 14:32:05 UTC | #29

 
thank you very very very very much :grinning:

-------------------------

glebedev | 2020-09-20 15:36:56 UTC | #30

![image|690x372](upload://qbpgvB69NNohqH21HJlCrmypdQu.jpeg)

-------------------------

glebedev | 2020-10-09 10:13:26 UTC | #31

Now exporter support LODgroup. Only works with static geometry at the moment.

-------------------------

elix22 | 2020-11-25 13:25:29 UTC | #32

I played with this tool a little bit.
Amazing stuff !!
Found some issue  ,
Disabled components in Unity are not disabled in Urho3D .
For example  disabled "Mesh Renderer"  in Unity , Static model is shown in Urho3D.
The exported components are missing the "Is Enabled" attribute
Every disabled component should have the following attribute. 
> attribute name="Is Enabled" value="false"

Thanks for sharing this amazing tool

-------------------------

glebedev | 2020-11-25 13:56:55 UTC | #33

May I ask you to open an issue on GitHub? I may forget to fix it otherwise.

-------------------------

elix22 | 2020-11-25 16:01:42 UTC | #34

Sure
Done
------------------------------------------

-------------------------

