SteveU3D | 2017-05-05 09:40:53 UTC | #1

Hi,
I try to apply alpha technique to an object but I don't get the expected result.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/a8e5fabc8c69564e77eb03a96c1aaf37aab23475.png" width="690" height="418">

On the image, on the left, I use NoTextureVCol.xml as technique 

    <technique vs="LitSolid" ps="LitSolid" vsdefines="NOUV VERTEXCOLOR" psdefines="VERTEXCOLOR" >
        <pass name="base" />
        <pass name="litbase" psdefines="AMBIENT" />
        <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
        <pass name="prepass" psdefines="PREPASS" />
        <pass name="material" psdefines="MATERIAL" depthtest="equal" depthwrite="false" />
        <pass name="deferred" psdefines="DEFERRED" />
        <pass name="depth" vs="Depth" ps="Depth" />
        <pass name="shadow" vs="Shadow" ps="Shadow" />
    </technique>

and on the right I use NoTextureVColAddAlpha.xml

    <technique vs="Unlit" ps="Unlit" vsdefines="VERTEXCOLOR NOUV" psdefines="VERTEXCOLOR">
        <pass name="alpha" depthwrite="false" blend="addalpha" />
    </technique>

I put a box behind the face and it can be seen when I use NoTextureVColAddAlpha.xml. It's ok but the problem is that the different triangles on the face are not visible anymore. So how to combine those two techniques to have the left model but with transparency?
Thanks.

-------------------------

Enhex | 2017-05-05 12:09:05 UTC | #2

I think you don't want to use additive blending. You need something like "NoTextureVColAlpha".

-------------------------

SteveU3D | 2017-05-12 09:18:20 UTC | #3

Hi,
Sorry but I don't get it. It tried with : 

    <technique vs="Unlit" ps="Unlit" vsdefines="VERTEXCOLOR NOUV" psdefines="VERTEXCOLOR">
    <pass name="alpha" depthwrite="false" blend="alpha" />
</technique>

but it gives the same result as the right image. I have transparency but the edges are not visible.

-------------------------

SirNate0 | 2017-05-12 12:50:45 UTC | #4

Based off of the DiffAlpha.xml technique, I think you need to add the litalpha pass:
```
<pass name="litalpha" depthwrite="false" blend="addalpha" />
```

-------------------------

