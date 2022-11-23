darkirk | 2017-06-09 19:37:17 UTC | #1

I've seen the DynamicGeometry demo and i'm trying to build on top of it to create something like this:

https://www.youtube.com/watch?v=EUN-SNaccbE

Is there an additional example of DynamicGeometry that places a gizmo on the vertices and allow mouse input somehow?

-------------------------

hdunderscore | 2017-06-07 20:47:35 UTC | #2

With something like this you will have a better time looking at it from a different perspective. If you try to work with Urho3D's representation of geometry and try manipulating it like in the video, you're going to have a hard time digging up the vertex data. On the other hand if you maintain your own simpler data representation of geometry, then only render the result in Urho (ie, using Geometry/DynamicGeometry) you'll have an easier time.

Having your own handy data representation can be useful when you need to use third party libraries such as to assist with booleans or to speed up picking in a dense scene.

You can look at the editor code for example of manipulating a gizmo with the mouse.

-------------------------

darkirk | 2017-06-08 02:00:37 UTC | #3

What do you mean by my own data representation? Like, having my own class of a Cube and sending the changes to its vectors to a custom geometry entity? What's the benefit in that? Also, doesn't that make the scene serialization even more difficult?

-------------------------

