Hevedy | 2017-01-02 01:02:20 UTC | #1

I'm created a new package to test and make things in Urho3D & Unreal Engine 4 from the idea of the old "Stimulus Package" now from zero and with more content the "Purpleprint Kit".
In the repository have more info about the Purpleprint Kit and is under CC-BY 3.0 license.

[url]https://github.com/Hevedy/PurpleprintKit[/url]
*This a alpha version of the project and some content are missing.


[img]https://dl.dropboxusercontent.com/u/28070491/UE/Screenshots/PurpleprintKitMaterials.png[/img]
[img]https://dl.dropboxusercontent.com/u/28070491/UE/Screenshots/PurpleprintKit3DModels.png[/img]
[img]https://dl.dropboxusercontent.com/u/28070491/UE/Screenshots/LightMap.png[/img]

Happy development.
Thanks.

-------------------------

hdunderscore | 2017-01-02 01:02:20 UTC | #2

Pretty interesting, could be useful for testing the PBR shaders I am working on for a quick comparison with UE4.

Are there Urho ready scene xml's that I can load into the editor?

-------------------------

Hevedy | 2017-01-02 01:02:21 UTC | #3

[quote="hd_"]Pretty interesting, could be useful for testing the PBR shaders I am working on for a quick comparison with UE4.

Are there Urho ready scene xml's that I can load into the editor?[/quote]

The plan is add some more scenes, and add to Urho3D & UE4 over this month. That scene is more for light than PBR, and the materials are unlit and normal without more shaders than diffuse, but you can customize as you like that, in the Urho3D folder you have the same config basic metals from UE4, but only have a setup of diffuse color, and specular, because the Urho3D don't have that PBR (you can change the properties and compare that).

I need fix 2 3D models with a ligthmap problem, change some textures and add the Urho3D materials, models and scenes.

You can see the progress over here: [url]https://trello.com/b/vx7Ydo7I/public-projects[/url]
*Since scenes are created in the engines, are more o less similar but have some differences. (Location, Scale, Rotations)
*The 3D models are in m/cm = 2x2m.

You will merge the PBR shaders in Urho3D to public ?

-------------------------

Hevedy | 2017-01-02 01:03:01 UTC | #4

Purpleprint 1.0.0 out !

Happy Development.

-------------------------

cnccsk | 2017-01-02 01:03:02 UTC | #5

good job, Thanks.

-------------------------

devrich | 2017-01-02 01:03:02 UTC | #6

Hey thanks Hevedy!!  :smiley:

-------------------------

JulyForToday | 2017-01-02 01:03:05 UTC | #7

That's an interesting question, is there any plan at all for Urho when it comes to having a PBR setup available out of the box? I'm only just now in the process of learning about PBR, and still relatively new to shaders, so I have no idea how difficult it would be to get a PBR setup going with Urho.

-------------------------

cadaver | 2017-01-02 01:03:05 UTC | #8

Likely will happen only if someone outside is going to contribute PBR example shaders. I'm mainly interested in whether the engine needs to expose something it doesn't yet to support PBR. Possibly custom uniforms for lights?

-------------------------

hdunderscore | 2017-01-02 01:03:05 UTC | #9

[quote="cadaver"]Likely will happen only if someone outside is going to contribute PBR example shaders. I'm mainly interested in whether the engine needs to expose something it doesn't yet to support PBR. Possibly custom uniforms for lights?[/quote]

I will try to clean up and share my shaders in the next few days. There will be much work ahead, thanks for the offer  :smiling_imp:

-------------------------

OvermindDL1 | 2017-01-02 01:03:16 UTC | #10

As there is no "Graphics Exchange" like the "Code Exchange" subboard, perhaps this should be moved to Showcase for greater visibility as I keep fogetting about it in here?  :slight_smile:

-------------------------

Hevedy | 2017-01-02 01:03:16 UTC | #11

The kit have a new ground material/texture to test the PBR with multiple maps, if you like.

-------------------------

JulyForToday | 2017-01-02 01:05:18 UTC | #12

Thought I'd give this thread a bump. I'm curious where things are at with this.

-------------------------

