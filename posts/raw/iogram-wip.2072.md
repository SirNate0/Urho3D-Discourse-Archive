godan | 2017-01-02 01:12:49 UTC | #1

Hi all,

Despite being very very early in the development process, I'm quite excited to share Iogram. The idea with Iogram is to bring computational design to game engines (via nice friendly node inteface), and also to bring game engine tech to computational designers! So far, it's been a fun project. 

[video]https://youtu.be/8o6tA72nvrw[/video]

All feedback is welcome! And big big thank you to all devs and community members behind Urho. It is an amazing platform - let's keep pushing it :slight_smile:

UPDATE 1:

Icons, update Listener, moving boxes....starting to come together :slight_smile:

[video]https://youtu.be/syt1Vtv_-ds[/video]

-------------------------

Victor | 2017-01-02 01:12:49 UTC | #2

This is really awesome work! :slight_smile: I bet this could be a really good shader editor as well (there really needs to be something like ShaderForge for making/testing small tedious shaders heh).

-------------------------

sabotage3d | 2017-01-02 01:12:49 UTC | #3

This is quite cool. If I understand correctly you can make procedural levels using a blueprint.

-------------------------

godan | 2017-01-02 01:12:50 UTC | #4

Yep, procedural content is one of the main goals. However, this workflow is also very useful for prepping a scene prior to runtime. For example, say you needed to place a bunch of trees on a terrain. You could create a little graph that 1) References a terrain mesh, 2) distributes some points on it 3) clones a tree model and places it in the scene. You save the scene, and away you go. No need to maintain a "Tree Placement" add on or something. Of course, there are benefits to the custom add on workflow, especially as the task grows in complexity.

As Victor suggests, the same workflow could be applied to Material and other Resource creation.

-------------------------

ghidra | 2017-01-02 01:12:52 UTC | #5

This is really awesome.
[quote]The idea with Iogram is to bring computational design to game engines[/quote]
Does this mean this is something that you are willing to share?

-------------------------

godan | 2017-01-02 01:12:53 UTC | #6

In principle, absolutely!

I make a living writing algorithms/geometry stuff, so at some point, I would very much like Iogram to be a source of income. However, I am totally open to the possibility of making it open source, but with paid updates or something. In fact, I think it would be so much better if there was strong community involvement. In the short term, I will be posting a WIP release of Iogram for anyone who is interested.

-------------------------

godan | 2017-01-02 01:13:01 UTC | #7

Getting dangerously close to an early WIP release!

[img]https://dl.dropboxusercontent.com/u/69779082/Iogram_VariedColor.PNG[/img]

-------------------------

godan | 2017-01-02 01:13:01 UTC | #8

Also, getting some pretty fun looking failures....:slight_smile:

[img]https://dl.dropboxusercontent.com/u/69779082/MeshChaos.PNG[/img]

-------------------------

Modanung | 2017-01-02 01:13:02 UTC | #9

[quote="godan"]Also, getting some pretty fun looking failures....:slight_smile:[/quote]
Which makes me wonder: Are you planning audio analysis inputs? Would make it a nice VJ tool as well. :slight_smile:

-------------------------

godan | 2017-01-02 01:13:03 UTC | #10

Very pleased to see that it works with Emscripten!

[img]https://dl.dropboxusercontent.com/u/69779082/Iogram_Chrome.PNG[/img]

-------------------------

sabotage3d | 2017-01-02 01:13:03 UTC | #11

Looks great. I have noticed some functions like fill polygons and smooth polygons, how are these implemented? Are you planning on contributing them as part of the Urho3D API? It would be great if we could use them directly with C++.

-------------------------

rasteron | 2017-01-02 01:13:05 UTC | #12

Looks interesting :slight_smile: keep it up!

-------------------------

godan | 2017-01-02 01:13:18 UTC | #13

Preliminary OpenStreetMaps reader:

[img]https://dl.dropboxusercontent.com/u/69779082/Screenshot%202016-07-17%2020.55.03.png[/img]

-------------------------

godan | 2017-07-05 13:54:30 UTC | #14

Hi all, there is a new release of IOGRAM out! [Get it here](https://github.com/MeshGeometry/Iogram/releases/tag/v0.0.8-wip).  Among other features, we've got some fancy mesh editor tools:

https://youtu.be/9g0BT_mRC5E?list=PL_1hCYCSHdNRwoXreVBLGx11dOALMUZbQ

https://youtu.be/rslUOOswrxk?list=PL_1hCYCSHdNRwoXreVBLGx11dOALMUZbQ


Also, I have just updated the [core repo](https://github.com/MeshGeometry/IogramSource) - there is a ton of Urho goodness in there (including some native components for [mesh editing](https://github.com/MeshGeometry/IogramSource/blob/master/Components/ModelEditLinear.cpp)) [[1]](https://discourse.urho3d.io/t/manipulating-vertices-and-faces-with-urho/3179). 

IOGRAM was Greenlit by the Steam community. Very exciting.

As always, I would love to your hear your thoughts on how I can make this a better tool for this community. Linux users in particular!

-------------------------

