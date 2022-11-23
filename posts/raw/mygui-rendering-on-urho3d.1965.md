ViteFalcon | 2017-01-02 01:11:53 UTC | #1

Hi All,

I am very new to Urho3D and I'm still learning my way around it. As part of porting some of my code into Urho3D, I wanted to get MyGUI rendering in Urho3D and I've managed to get it working. Here's a screenshot of it:

[img]http://i.imgur.com/VAXPCW1.png[/img]

The fonts are a bit messed up. My layout file was for smaller font-size and the current font I have is a bit large and gets culled.

-
Vite Falcon

-------------------------

S.L.C | 2017-01-02 01:12:02 UTC | #2

Is the source released or is it just a WIP for personal use? I'm also trying to create a subsystem for MyGUI and if this was already released then I'd be saving some time.

-------------------------

ViteFalcon | 2017-01-02 01:12:05 UTC | #3

[quote="S.L.C"]Is the source released or is it just a WIP for personal use? I'm also trying to create a subsystem for MyGUI and if this was already released then I'd be saving some time.[/quote]
I plan to release the source. It requires some changes to Urho3D, unfortunately. I'm trying to see if there's an easy way around that though. I also need to do some clean up so that it doesn't use my custom resource manager and uses Urho3D;:ResourceCache instead to retrieve resources.

-------------------------

