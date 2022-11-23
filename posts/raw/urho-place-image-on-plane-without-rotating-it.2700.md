Jimmy781 | 2017-01-13 21:46:41 UTC | #1

Hey guys , 

I've just upgraded urhosharp and since then i have been facing an issue.

plane.SetMaterial(Material.FromImage("image.png"));

It is placing the image on the plane sideways , I tried the new plane.mdl from the urho repo but the issue persists . 

Is there any way to fix that ?

-------------------------

artgolf1000 | 2017-01-14 01:02:33 UTC | #2

Just checked the latest Plane.mdl, it is alright.
You may rotate the node 90 degrees around Y axes to fix the issue.

-------------------------

George1 | 2017-01-14 02:33:06 UTC | #3

[quote="artgolf1000, post:2, topic:2700"]
e node 90 degrees around
[/quote]


I think it would be great if there is a function to change the orientation and translation of the origin coordinate or the Mesh in Urho3D.  E.g. Change and save permanently. This would be a time saver.

-------------------------

SirNate0 | 2017-01-14 04:31:33 UTC | #4

It would be a nice feature for the editor, at least, though I'm not sure how useful it would be elsewhere, as most models are imported from a proper modelling software that can do more than simply adjust orientation and translation...

-------------------------

Eugene | 2017-01-14 08:11:25 UTC | #5

Transfromation hierarchy is now implemented through nodes. So it would be duplicate functionality if additionally put the same logic in StaticModel. 

There is such logic for collision shapes... But collision shapes need it much stronger than graphical components.

-------------------------

