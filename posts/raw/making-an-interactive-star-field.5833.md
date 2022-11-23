pldeschamps | 2020-02-13 14:29:00 UTC | #1

Hello,
I succeeded:
- in exporting many circles from blender in one .mdl file
![geometries.PNG|677x500, 75%](upload://hW4KqVISNhkEkrPIp4olDhqX2XT.jpeg) 
- in rendering the .mdl file in my urho3D project.

**How can I access each geometry from my urho3D project?**

I would like:
- first to detect when the user click on one circle and get the circle name
- second to attach a material

Regards,

-------------------------

Bananaft | 2020-01-23 09:21:32 UTC | #2

You should probably make this stars separate objects.
Are you planning to only 500 stars, or you want to add more in the future?
Do you want it on mobile or PC?

-------------------------

Modanung | 2020-02-13 18:17:17 UTC | #3

Thread concerning a similar project:
https://discourse.urho3d.io/t/sphere-as-light-source/5000/19

To detect clicks you could either cast rays in the Octree, or apply trigonometry.

Welcome to the forums, btw! :confetti_ball: :slightly_smiling_face:

-------------------------

pldeschamps | 2020-01-23 16:04:54 UTC | #4

@Bananaft, thank you for your answer. 500 is far enough. But as the human eye can see until the 5000 brighest stars, I may add that ones too.
If I make 500 separate objects, I need to add 500 files to my project which is not easy to manage...
I want it on mobile and PC (using C#, Xamarin, UWP and Android but keep that secret please :laughing: )

-------------------------

pldeschamps | 2020-01-23 16:12:09 UTC | #5

@Modanung
Thank you for your welcome and than you so much for the link to the thread: @lheller is doing the same work than me! :smiley:

-------------------------

pldeschamps | 2020-02-12 16:02:36 UTC | #6

Hi @Modanung ,

Finally, I made one StaticModel for each star.
Each star is facing the center of the scene (I struggled few days for that!):
![demisphere|586x500](upload://pUuVK5viB2yr36WDJsLfKE5AWsF.png) 
But, as you told me, billboard would be easier (in fact, the stars would be facing the camera the whole time!).
But does ray cast works on billboard?
It seems tha @cadaver tells it is possible:
https://discourse.urho3d.io/t/picking-billboards/76/3
Is there any sample for ray cast on a billboard?

Regards,

-------------------------

Modanung | 2020-02-12 19:11:12 UTC | #7

Did you manage to get it working with static models?

-------------------------

lezak | 2020-02-12 19:52:42 UTC | #8

[quote="pldeschamps, post:6, topic:5833"]
Is there any sample for ray cast on a billboard?
[/quote]

Should be exactly the same as raycast against any other drawable (for sure navigation, crowd navigation and decals samples use raycast).
And if You'd prefer to use static model instead of billboard, why use circles and not spheres with LOD (and maybe static model group)?

-------------------------

Modanung | 2020-02-12 21:12:59 UTC | #9

[quote="lezak, post:8, topic:5833"]
...why use circles and not spheres with LOD...
[/quote]

About that...

https://discourse.urho3d.io/t/information-source-how-to-exporting-lods-with-blender/2083

-------------------------

pldeschamps | 2020-02-13 11:19:29 UTC | #10

[quote="lezak, post:8, topic:5833"]
why use circles and not spheres
[/quote]

Because I have in mind that a sphere is more CPU-consuming than a 12 edges trifan circle but I may be wrong...
I may draw thousands of stars (maybe 1,600 or up to 5,000, even 120,000 if I can) on a mobile phone. I really want to optimize my code.
This is why I made one .mdl with the whole stars in it at the begining.
This is why I prefer a circle to a sphere (but is it the right choice?).
The questions are:
- are thousands of billboard items less CPU-consuming than thousands of StaticObject as @Modanung said: "you might as well use billboards instead of spheres for maximum performance"
- is a circle less CPU-consuming than a sphere?
- is a circle facing the center less CPU-consuming than a circle facing the camera (when the camera rotate)?
- is a sphere less CPU-consuming than a circle facing the camere when the camera rotate?

[quote="lezak, post:8, topic:5833"]
and not spheres with LOD
[/quote]
I don't really need LOD as all the stars are on a sphere at equal distance to the camera (Is LOD only for choosing an object depending on distance?).
The camera is in the center of the Scene and all the stars are at the same distance. To simulate the magnitude, I can use either the diameter of the circle (or the sphere) and the brightness of the color.
I was thinking about using a 18 edges trifan circle for Sirius (which is the brightest star), 12 edges for the 60 brightest stars and 8 edges for the others...

[quote="Modanung, post:7, topic:5833, full:true"]
Did you manage to get it working with static models?
[/quote]
I could draw the stars, I haven't tried Raycast already...

-------------------------

dertom | 2020-02-13 09:59:45 UTC | #13

[quote="pldeschamps, post:10, topic:5833"]
I could draw the stars, I haven’t tried Raycast already…
[/quote]

I actually wonder why you not just give it a try and fire a ray through you scene and see if it works ;)

....looking at the code, BillboardSet implements its own ProcessRayQuery and it should work as intended,....(never used it though)

Use something **like** this:
https://github.com/dertom95/urho3d-minimal-new-project/blob/master/src/GameLogic.cpp#L385

and call it **like** this:
```
     auto* ui = GetSubsystem<UI>();
     IntVector2 pos = ui->GetCursorPosition();
    Vector3 hitpos; 
    Drawable* hitObj;
    if (RayCast(pos,1000000.0f,hitpos,hitObj)) {
      // do something with hitobj 
   }
```

-------------------------

lezak | 2020-02-13 10:10:30 UTC | #14

I don't know how well would billboards perform with this numbers. 
Assuming that camera is not static, spheres may be a better choice then circles, because You will have to rotate every circle to face the camera and probably You'll loose performance gained from lower number of polys.
As for Your questions, the best way to find out which setup works best would be to simply compare them, especially that there is not so many options and it would take only few lines of code to switch between billboards, circles and spheres (keep in mind that there is static model group component).

-------------------------

Eugene | 2020-02-13 10:32:57 UTC | #15

[quote="pldeschamps, post:10, topic:5833"]
This is why I prefer a circle to a sphere (but is it the right choice?).
[/quote]

Ever thought about quad with custom shader? You can do a lot of interesting things there.

-------------------------

pldeschamps | 2020-02-13 11:14:55 UTC | #16

Well, I tried a BillboardSet using this png image:
https://discourse.urho3d.io/t/sphere-as-light-source/5000/43
This is the result:
![transparency|594x500](upload://dD64QLuJ0p66xH6V2LzizklMjKw.png) 
I guess (or I hope) the BillboradSet will offer a good performance.
But: how I use the transparency of the .png image?
Is it possible to get the billboard item at same size whatever the distance?
This is my code (sorry, C#):
```
        private void CreateBillboardSet(Scene scene)
        {
            var img = ResourceCache.GetImage("Images/glowingstar.png");
            var material = Material.FromImage(img);
            Node nodeBBS = scene.CreateChild();
            var bbs = nodeBBS.GetOrCreateComponent<BillboardSet>();
            bbs.NumBillboards = (uint)200;
            bbs.Sorted = true;
            bbs.Material = material;
            uint i = 0;
            i++; AddStarItem(bbs,i, -0.126f, 0.473f, -1.939f, -75.824f, 104.961f, 0.155f);
            i++; AddStarItem(bbs,i, -1.568f, -0.706f, 1.022f, 30.736f, 204.234f, 0.138f);
            i++; AddStarItem(bbs,i, -0.748f, -1.268f, -1.354f, -42.594f, 239.479f, 0.137f);
            i++; AddStarItem(bbs,i, 0.250f, -0.914f, 1.761f, 61.733f, 285.316f, 0.135f);
            i++; AddStarItem(bbs,i, 0.261f, 1.824f, 0.777f, 22.864f, 81.858f, 0.134f);
            //etc
            bbs.Commit();
        }
```

-------------------------

pldeschamps | 2020-02-13 11:28:49 UTC | #17

[quote="pldeschamps, post:16, topic:5833"]
But: how I use the transparency of the .png image?
[/quote]

nearly done with that:
```
material.AlphaToCoverage= true;
```
stars are not glowing though...
![alphatocoverage|594x500](upload://qWMmAWjvKPNH8NOC3oZLDKK15ft.png)

-------------------------

Modanung | 2020-02-13 12:13:28 UTC | #18

Did you know you can browse the source of the engine? To find out the capabilities of a `BillboardSet` have a look at `BillboardSet.h`. There you will find:
```
void SetFixedScreenSize(bool enable);
```
To make your stars glow simply use an image of a glowing star, or add a bloom post-processing effect.

-------------------------

pldeschamps | 2020-02-13 15:03:29 UTC | #19

I am currently using a image of a glowing star.

I added useAlpha:true to the Material.FromImage(img, useAlpha:true) but it did not change the result. I wonder if the ResourceCache.GetImage() loads the alpha :thinking:

I tried bbs.FixedScreenSize = true; but that made all the stars disappear.

```
        private void CreateBillboardSet(Scene scene)
        {
      
            var img = ResourceCache.GetImage("Images/glowingstar.png"); //is alpha loaded?
            var material = Material.FromImage(img, useAlpha: true); // not enough :-(
                
            material.AlphaToCoverage= true;
            Node nodeBBS = scene.CreateChild();
            var bbs = nodeBBS.GetOrCreateComponent<BillboardSet>();
            
            bbs.NumBillboards = (uint)200;
            bbs.Sorted = true;
            bbs.Material = material;
            bbs.FixedScreenSize = true;
            uint i = 0;
            i++; AddStarItem(bbs,i, -0.126f, 0.473f, -1.939f, -75.824f, 104.961f, 0.155f);
            i++; AddStarItem(bbs,i, -1.568f, -0.706f, 1.022f, 30.736f, 204.234f, 0.138f);
            i++; AddStarItem(bbs,i, -0.748f, -1.268f, -1.354f, -42.594f, 239.479f, 0.137f);
            i++; AddStarItem(bbs,i, 0.250f, -0.914f, 1.761f, 61.733f, 285.316f, 0.135f);
            i++; AddStarItem(bbs,i, 0.261f, 1.824f, 0.777f, 22.864f, 81.858f, 0.134f);
            //I will write better code...
            bbs.Commit();
        }
        private void AddStarItem(BillboardSet bbs, uint i, Single x, Single y, Single z, Single r1, Single r2, Single radius)
        {
            var bbi = bbs.GetBillboardSafe(i-1);
            bbi.Position = new Vector3(x, y, -z);
            bbi.Size = 0.1f * Vector2.One;
            //bbi.Color = Color.White;
            bbi.Enabled = true;
        }
```

-------------------------

Modanung | 2020-02-13 16:11:22 UTC | #20

Have you tried a material that uses an _alpha_ technique?

-------------------------

pldeschamps | 2020-02-13 16:31:25 UTC | #21

Well, I use a png image with alpha:
![GlowingStarCapture|447x500](upload://vKdDjfLZaTYfFvv1RXbAHHvsudr.png) 
I use alpha when making the material from image and I set AlphaToCoverage to true.
What else should I do?
```
            var img = ResourceCache.GetImage("Images/glowingstar.png");
            var material = Material.FromImage(img, useAlpha: true);
            material.AlphaToCoverage= true;
```

-------------------------

SirNate0 | 2020-02-13 16:59:45 UTC | #22

If you save the image when you load it and then open that that should help you determine if it loaded the transparency. You could also print the material's techniques to ensure it is actually one with alpha.

-------------------------

pldeschamps | 2020-02-13 17:35:53 UTC | #23

I looked at some pixels of the image img. It seems that Alpha is loaded:
(40,40) A=0 R=0 G=0 B=0
(120,120) A=0.302 R=1 G=1 B=1
(256,256) A=1 R=1 G=1 B=1
so the issue seems to be there:
```
var material = Material.FromImage(img, useAlpha: true);
```

-------------------------

Modanung | 2020-02-13 17:41:44 UTC | #24

Indeed the issue seems to be that you are not using Urho3D but UrhoSharp.

-------------------------

pldeschamps | 2020-02-13 17:50:56 UTC | #25

you are maybe right.
I have tried to set the ClearColor to blue:
```
viewPort.SetClearColor(Color.Blue);
```
and I added a green box inside my billboardset and here is the result:
![alpha|607x500](upload://aD7fEoIi2scbEU6YuSyh4ezxW6a.png) 

Around the glowing stars, the alpha is zero and we can see the green box, but as soon the alpha is different from zero, the light does not come through...

-------------------------

Modanung | 2020-02-13 17:57:46 UTC | #26

I expect this is because `FromImage` with `useAlpha` set to `true` outputs a material using an alpha *mask*.

-------------------------

pldeschamps | 2020-02-13 18:16:50 UTC | #27

[quote="Modanung, post:26, topic:5833, full:true"]
I expect this is because `FromImage` with `useAlpha` set to `true` outputs a material using an alpha *mask* .
[/quote]

Well, this gives the same result:
```
            var material = Material.FromImage(img);//, useAlpha: true);
            material.AlphaToCoverage= true;
```
Anyway, I give up, the glowing effect will be for the next version.
@Modanung, @SirNate0, Thank you for your help.

[quote="Eugene, post:15, topic:5833"]
Ever thought about quad with custom shader? You can do a lot of interesting things there.
[/quote]
That maybe a solution I will try later. Thank you.

[quote="dertom, post:13, topic:5833"]
I actually wonder why you not just give it a try and fire a ray through you scene and see if it works :wink:
[/quote]
I will try that next week, thank you.

-------------------------

pldeschamps | 2020-03-22 15:24:57 UTC | #28

[quote="Modanung, post:20, topic:5833, full:true"]
Have you tried a material that uses an *alpha* technique?
[/quote]

That sloved the problem:
```
material.SetTechnique(0, ResourceCache.GetTechnique("Techniques/DiffAlpha.xml"));
```

-------------------------

