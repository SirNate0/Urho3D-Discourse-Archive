Tinimini | 2017-01-02 01:04:55 UTC | #1

I'm having some trouble wrapping my head around how to make custom meshes in Urho. I took the DynamicGeometry sample as the base and I'm trying to do just a simple quad using a custom mesh. So two triangles. Shouldn't be too hard, now should it... But for some reason I end up getting very strange results.
What I currently have is one triangle on one side and then on the other side I have one line (see screenshots).
[dropbox.com/s/9q13rmo7bj6v1 ... 4.png?dl=0](https://www.dropbox.com/s/9q13rmo7bj6v11c/Screen%20Shot%202015-04-30%20at%2014.13.54.png?dl=0)
[dropbox.com/s/xlattnpzc2h6o ... 9.png?dl=0](https://www.dropbox.com/s/xlattnpzc2h6o1q/Screen%20Shot%202015-04-30%20at%2014.14.09.png?dl=0)

And this is my vertex data and indices:
[code]
    float vertexData_[] {
        // Position             Normal
        -0.5f, -0.5f,  0.5f,     0.0f,  0.0f,  1.0f,
        -0.5f,  0.5f,  0.5f,     0.0f,  0.0f,  1.0f,
         0.5f, -0.5f,  0.5f,     0.0f,  0.0f,  1.0f,
         0.5f,  0.5f,  0.5f,     0.0f,  0.0f,  1.0f
    }

    unsigned short indexData_[] {
        0, 1, 2,
        2, 1, 3
    }
[/code]

And finally the geometry is created like this:

[code]
geom->SetVertexBuffer(0, vb);
geom->SetIndexBuffer(ib);
geom->SetDrawRange(TRIANGLE_STRIP, 0, 4);
[/code]

The initialization of vb and ib is pretty much exactly as in the sample.

I know there's probably some really really simple explanation for this, but I keep tripping up with these vertex/index definitions with custom meshes, no matter what engine or language I'm using.

-------------------------

Tinimini | 2017-01-02 01:04:55 UTC | #2

Ugh.. Stupid me. When I changed the type from TRIANGLE_LIST to TRIANGLE_STRIP I didn't realize that I naturally have to adjust the sizes to compensate the different type. So geom->SetDrawRange(TRIANGLE_STRIP, 0, 6) is correct as I have 6 indices... Stupid, stupid, stupid.. It works now...

-------------------------

