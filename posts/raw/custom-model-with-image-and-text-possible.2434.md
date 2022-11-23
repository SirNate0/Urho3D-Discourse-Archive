Jimmy78 | 2017-01-02 01:15:23 UTC | #1

Hey guys , 

this is the first time i'm using urho and i had a question .

Is it possible to create a model that takes an image (local or url) with some text . 

E.g - instead of the ragdolls or boxes - i want something like a billboard 

like this : [imgur.com/a/TJ62e](http://imgur.com/a/TJ62e)

I have a scene and a plane - this will be on the plane .

Thank you , i would be very grateful if anyone can tell me how to do this - i have zero experience with graphics.
If i can use a web url for the image - even better - else local.

-------------------------

ghidra | 2017-01-02 01:15:23 UTC | #2

yes, you can.

There are a few concepts that you should get familiar with to get started.
First, Urho uses "nodes" to "hold" information. In this case, a grid.

Step 1: In the editor, create a local node.

Second, a lot of game logic, or logic that can be attached to nodes, are done with "components".
So far, you have a node in the scene. Which is nothing more than a invisible point in a scene that has transformation information. Or simply information on where in the 3d scene the node is, and the rotation and scale.

Step 2: If you want a simple grid to put on an image, with the node selected. add a "static mesh" component.
This static mesh component will allow you to load in any static mdl. Urho has a few general ones. 
You should see a paramaters pane in the editor for your static mesh component, that you can choose to load the mdl onto. Select the Grid.mdl.

Step3:
Finally to get a image on this grid.
Within the same static mesh component, after you have loaded the grid mdl, there is another paramater further down, that you can choose a material. (Im not infront of a working urho build, so the instructions might be a little incorrect). I would just try a simple material, Lit maybe, or DefaultLit.
You should be able to inspect the material, and load a local image into the diffuse parameter.

Step 4: You might need to add a light to the scene as well.
Make a node, make a light component, and change the light to directional. and rotate it so it lights up your grid.

This should get you a very very basic set up.
(when I am infront of a proper urho build, I can save out a scene.xml that you can load, if you havent managed to get this far)

-------------------------

Jimmy78 | 2017-01-02 01:15:24 UTC | #3

Thanks a lot ghida , Highly appreciated .

I'm very unfamiliar with the urho editor - i tried it last night and was completely lost 

I have been coding directly in c# so far based on the samples

-------------------------

