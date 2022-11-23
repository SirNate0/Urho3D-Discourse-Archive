HappyWeasel | 2021-04-22 22:00:27 UTC | #1

Hi, 

I have a .fbx file with simple transform/scale animation, no bones.. 

I can see that AssetImporter wrote an .ani file, and I can see that it's mostly linked to the Animation.cpp/h class, which says "Skeletal animation resource". 

So I guess Node Animation mostly refers to the creation of ValueAnimations within ObjectAnimations in code or from xml/json (as seen in the 30_LightAnimation demo)..

Any chance I can use that .ani file .. with an AnimationController maybe ? I searched the forum but did not find an answer..  (https://discourse.urho3d.io/t/animatedmodel-without-skeleton/4001, https://discourse.urho3d.io/t/export-animated-node-transforms-to-urho3d/1067)

Thanks!

(btw I was able to import and use an animated model in my c++ code with skeltal animation/bones, so that's really cool.. I just do not want to create a dummy bone and riggend animation or something if it can be solved differently.)...

-------------------------

Dave82 | 2021-04-22 23:04:25 UTC | #2

Just create an AnimationController to your root node and load the animation exactly the same way as you do with skeletal animations. Please note : 
- The nodes must have the same hierarchy as in the ani file.
- the nodes must have the same names as in the ani file.

-------------------------

HappyWeasel | 2021-04-23 16:27:09 UTC | #3

Works like a charm, thank you very much..  :+1:

-------------------------

