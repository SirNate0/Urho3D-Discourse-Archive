smellymumbler | 2017-12-09 15:24:54 UTC | #1

So, I'm playing around with Urho's geometry capabilities and i'm curious about how to do some transformations on primitives. I did a small tool to create arbitrary boxes and now I want to allow users to extrude the faces of those boxes. Unfortunately, I have no idea how to do this or where to start. Any tips?

Also, how do you guys handle texture mapping on CustomGeometry nodes? What I'm doing is similar to the old HL1 map editor.

-------------------------

SirNate0 | 2017-12-07 04:53:56 UTC | #2

Fine the boundary ring the selection (so the four edges if its just a square), duplicate the vertices on it, change the triangles outside the selection to use the new vertices, and move the selected faces along the normal, bridging the hole with new triangles.

I can't help with the texture mapping - all of my geometry is exported from Blender.

-------------------------

smellymumbler | 2017-12-08 17:56:35 UTC | #3

Hi, and thanks for the help. I'm now able to see the process as a whole, but i still don't understand two things:

* How can i find the boundary from a face?
* How can i create new triangles? If i understand correctly, the only thing i have are the old position of the points and the new one, after the extrusion.

-------------------------

Modanung | 2017-12-08 19:27:00 UTC | #4

I'm thinking you could pick all sides that are not shared between (selected) triangles to get the edge of your selection.
Then you could build triangle strips from weaved lists of sets from these vertices. [spoiler](Those are not type suggestions)[/spoiler]

-------------------------

