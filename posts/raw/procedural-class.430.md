vivienneanthony | 2017-01-02 01:00:21 UTC | #1

Hello

I have been playing with the procuderal code which now works in a class not as a hack image class modification. So,  it can be applied to anything that uses a image. The code is at the below link. Any addition or help would be appeciated.

[sourceforge.net/projects/proteu ... rocedural/](https://sourceforge.net/projects/proteusgameengine/files/Existence/Source/Engine/Procedural/)

I generated some images and most of it is self explanatory although ad-hoc. The cmakelists.txt have to be modified to have the directory Procedural as source code. I did not update my client game login but the code works. 

So my goal is to play around with a generate scene code utilizing the terrain and planet rules, make the code faster, also add offsetx/y, scalexy/y to the diamond displacement method.

Testing Code

[code]/// Initilalize procedural
    proceduralMap -> Initialize(1024,1024);
    proceduralMap -> SetOffSets(0,0);
    proceduralImage -> SetSize(1024,1024, 1, 4);

    /// Test procedual generation
    proceduralMap -> SetOctaves(4,0.25f,true,0.9f,0.5f,0.5f,0.5f,0.5f,0.5f,0.5f,0.5f);
    //proceduralMap -> GenerateProceduralTerrain(terrainRule);
    proceduralMap -> GenerateProceduralDiamond(.8);

    /// Copy Procedual to Image Data
    proceduralImage -> SetData(proceduralMap -> GetImage());

    /// Save Procedual to a file
    proceduralImage -> SavePNG(String("/media/home2/vivienne/Existence/Bin/testclass.png"));
[/code]

-------------------------

