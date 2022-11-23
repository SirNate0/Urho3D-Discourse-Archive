anako126n | 2017-01-02 01:04:03 UTC | #1

Any idea why whenever I use AssetImporter to export a model from *.dae file the whole model is getting scaled down?

A simple test case:

Cube 10.0 x 10.0 x 10.0 created in Maya, geometry in *.dae file looks as following:
-5.000000 -5.000000 5.000000
5.000000 -5.000000 5.000000
-5.000000 5.000000 5.000000
5.000000 5.000000 5.000000
-5.000000 5.000000 -5.000000
5.000000 5.000000 -5.000000
-5.000000 -5.000000 -5.000000
5.000000 -5.000000 -5.000000

After running the AssetImporter on this file and loading the output file, vertices are as follow:

-0.05 -0.05 0.05
0.05 -0.05 0.05
......
......

Everything loaded into the scene is seriously small. To get the original size I would have to set the scale to 100  :open_mouth:

EDIT: Hmm, this happens only if I use model command. Exporting the whole scene create models in its original size.

-------------------------

thebluefish | 2017-01-02 01:04:03 UTC | #2

Typically that means your model has a scale of 100. Scale the model down to 1, then scale all of the vertices by 100.

I do this way too much in 3DS max. I don't know about your modelling program, but my issues went away as soon as I set my coordinate sizes correctly (aka meters for everything).

-------------------------

