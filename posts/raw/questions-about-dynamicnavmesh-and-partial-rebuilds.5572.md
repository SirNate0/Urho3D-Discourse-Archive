Leith | 2019-09-13 05:35:25 UTC | #1

Hey guys :slight_smile:

I've just implemented an orientation tool in my ingame editor project.
The current test scene includes a dynamic navmesh.

I have two questions.

#1 - how could I programatically deternine if a Drawable is Navigable, without specifically adding Navigable components everywhere? 

#2 - When I rotate some Navigable in my scene, I perform a partial rebuild of the navmesh, using the boundingbox of the subject. This works as expected..
Should I assume that any nearby Offmesh Links are NOT re-evaluated once that local region of the navmesh has been re-established?

-------------------------

