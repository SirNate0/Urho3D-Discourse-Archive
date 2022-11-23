Cpl.Bator | 2018-03-20 10:18:16 UTC | #1

Hi, i have a problem with transparent block in my voxel test code. i dont understand why, it's work sometime... , look the gif for the problem description : 

[https://media.giphy.com/media/5nselJ1uWNglqIdYkJ/giphy.gif](https://media.giphy.com/media/5nselJ1uWNglqIdYkJ/giphy.gif) 


i have read this topic : https://discourse.urho3d.io/t/transparent-material-with-using-diffvcol-technique/3962 , but didnt help me. i need transparent material with unlight/unshadowed & vertex color support, like DiffVColAlpha, but didnt exist in my Technique folder, i the gif, i use BasicVColUnlitAlpha.xml.

i'm efraid to create my transparent block in separate geometry and add it at last into the engine. in my code , each chunck is represented by fixed array ( unsigned char ) , i apply a simple culling test for display only visible surface for each block. Anyone have simple solution for thats ? Thank.

-------------------------

Eugene | 2018-03-20 16:17:54 UTC | #2

If you don't need semi-transparent things, you should use `ALPHAMASK` material instead of `*Alpha` tehniques.

Semi-transparent things should be rendered last, on the other hand.

-------------------------

Cpl.Bator | 2018-03-20 16:18:52 UTC | #3

Ok, i need to separate my geometry in two part. thanks for your help.

-------------------------

Eugene | 2018-03-20 16:31:37 UTC | #4

It seems for me that you don't need semi-transparent geometry for the scene shown in gif. Am I wrong?

-------------------------

Cpl.Bator | 2018-03-20 16:53:10 UTC | #5

For now, i dont have semi transparent block, but after, i need it for water, or other liquid block. for glass is not necessary. with two std::map i can divide my geometry in two part, transparent and non transparent block.

-------------------------

Eugene | 2018-03-20 18:23:09 UTC | #6

Just in case: separate all _three_ kinds of geometry (opaque, cutout transparent, semitransparent), rendering of the first two could be intermixed.

-------------------------

Cpl.Bator | 2018-03-20 19:25:40 UTC | #7

Ok, i take into account your topic

-------------------------

