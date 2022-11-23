Kanfor | 2017-01-02 01:10:01 UTC | #1

Hi, urhofans!

I have a plane with a material with transprencies and DiffNormalAlpha technique.

The GREAT problem is when I put other similar plane in front, some times I can't see the plane more near ??????

If I use DiffNormalAlphaMask I solve the problem, but the texture looks ugly in the borders :frowning: 

Somebody can help me, please?

I read something about alpha test, but I don't know how it works.

Thansk!

-------------------------

rasteron | 2017-01-02 01:10:02 UTC | #2

Hey Kanfor, I think you are somehow referring to mipmapping. You could try and play around with those values by setting up the texture paramaters with an additional texture xml file that is the same name has the texture file name.

[code]
<texture>
   <address coord="u|v" mode="wrap|mirror|clamp|border" />
   <border color="r g b a" />
   <filter mode="nearest|bilinear|trilinear|anisotropic" />
   <mipmap enable="true|false" />
   <quality low="x" medium="x" high="x" />
 </texture>
[/code]

As for the alpha test, you can manage it in the editor or manually in your material xml file:

[code]
<material>
   <base name="BaseMaterial.xml" />
   <technique quality="q" loddistance="d" sm3="true|false" />
       <texture unit="diffuse|normal|specular|emissive|detail|environment" name="Texture.dds" />
       <parameter name="ShaderParameterName" value="x y z w" />
       <pass name="deferred|emissive|prepass|material|ambient|negative|light|postopaque|shadow"
           vs="VertexShaderName" ps="PixelShaderName" alphamask="true|false" 
           alphatest="true|false" blend="replace|add|multiply|alpha|addalpha|premulalpha|invdestalpha" 
           cull="none|ccw|cw" depthtest="always|equal|less|lessequal|greater|greaterequal" 
           depthwrite="true|false" /> 
   </technique>
</material>
[/code]

Are we talking about leaves/branches when you mentioned ugly borders on your alpha textures? :wink:

Then again if it is just an art pipeline problem then I guess you should compare other existing textures that you have tested without any problems. There are techniques and tools in creating alpha textures with good borders or edges.

More reference:
[urho3d.github.io/documentation/1 ... rials.html](http://urho3d.github.io/documentation/1.5/_materials.html) (materials and textures page)
[urho3d.wikia.com/wiki/Texture](http://urho3d.wikia.com/wiki/Texture)
[urho3d.wikia.com/wiki/Material](http://urho3d.wikia.com/wiki/Material)

-------------------------

Kanfor | 2017-01-02 01:10:05 UTC | #3

Thank you, master!  :smiley: 

 I will keep trying  :wink:

-------------------------

