practicing01 | 2017-01-02 01:08:15 UTC | #1

I was having issues with it exporting scenes (it wasn't saving node position and convex hull wasn't working well).  After switching to MonkeyFirsts fork, those issues were solved.  I'm new to blender but if I understand correctly, you can use it to bake lighting and perhaps other optimization techniques.  This is important and even more so is that it can be used as an editor for placing nodes.

It seems the official Reattiva exporter is obsolete abandonware.  The link provided to it [url=http://urho3d.github.io/documentation/1.5/_external_links.html]here[/url] should be changed to MonkeyFirsts fork [url=https://github.com/MonkeyFirst/Urho3D-Blender]here[/url].  The reason being that MonkeyFirst has fixed the aforementioned issues.

Hopefully someday the official urho3d editor will have the needed features so that the exporter is not required.  Thanks for your time.

-------------------------

codingmonkey | 2017-01-02 01:08:15 UTC | #2

Earlier i wanted to do PR in the Reattiva's master brunch, but I have not completed yet the ability to store the position of the nodes (now it's working only from "front view" = back). 
Maybe later I will do PR to the official master, when solve this issue.

-------------------------

