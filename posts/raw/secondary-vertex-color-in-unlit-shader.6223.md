Teknologicus | 2020-06-24 20:41:31 UTC | #1

In my cubic voxel surfaces project I want to make sunlight transition (day to night and vice versa) work via a sunlight level scalar shader uniform.  Each vertex will also have a secondary color for the sunlight (in addition to the torchlight (first) vertex color already working).

My understanding of techniques and shaders is rudimentary and I'm looking for some helpful/insightful direction on how to go about this.  If someone has relevant code in an open source Urho3D project accessible online, please point me to it so I can study the relevant code.

This is the "DiffUnlitVCol.xml" technique (credit @Tinimini) I'm using:

>\<technique vs="Unlit" ps="Unlit" vsdefines="VERTEXCOLOR" psdefines="DIFFMAP VERTEXCOLOR">
    \<pass name="base" />
    \<pass name="prepass" psdefines="PREPASS" />
    \<pass name="material" />
    \<pass name="deferred" psdefines="DEFERRED" />
\</technique>

Do I need to change/add anything in this technique for it to be able to pass the secondary color from the vertex buffer object to the shader as well as expose the sunlight scalar shader uniform?  Furthermore, do I need to make modifications to a copy of the "Unlit.glsl" shader?  It looks to me like "Unlit.glsl" only makes use of one vertex color (VERTEXCOLOR) and I'm unclear how I would make it access the uniform for scaling the secondary vertex color (sunlight).

Kind regards,
Teknologicus

-------------------------

Teknologicus | 2020-10-05 01:23:50 UTC | #2

I've made some progress on this in that I understand Urho3D only supports one color per vertex, whereas I need three colors per vertex (sun, torch and anti-light).  I decided to make some experimental changes to a copy of Urho3D source code to see if I could get it to support multiple colors per vertex with vertex buffers.

What I'm looking for is feedback as to whether I'm going down the right path or not.

Here's what I changed in a copy of Urho3D source code:

    diff -r -U3 /tmp/Urho3D-master/Source/Urho3D/Graphics/GraphicsDefs.cpp ./Source/Urho3D/Graphics/GraphicsDefs.cpp
    --- /tmp/Urho3D-master/Source/Urho3D/Graphics/GraphicsDefs.cpp	2020-07-27 06:31:27.000000000 -0700
    +++ ./Source/Urho3D/Graphics/GraphicsDefs.cpp	2020-10-04 16:01:29.154308332 -0700
    @@ -97,6 +97,8 @@
        VertexElement(TYPE_VECTOR3, SEM_POSITION, 0, false),     // Position
        VertexElement(TYPE_VECTOR3, SEM_NORMAL, 0, false),       // Normal
        VertexElement(TYPE_UBYTE4_NORM, SEM_COLOR, 0, false),    // Color
    +    VertexElement(TYPE_UBYTE4_NORM, SEM_COLOR, 0, false),    // Color2
    +    VertexElement(TYPE_UBYTE4_NORM, SEM_COLOR, 0, false),    // Color3
        VertexElement(TYPE_VECTOR2, SEM_TEXCOORD, 0, false),     // Texcoord1
        VertexElement(TYPE_VECTOR2, SEM_TEXCOORD, 1, false),     // Texcoord2
        VertexElement(TYPE_VECTOR3, SEM_TEXCOORD, 0, false),     // Cubetexcoord1
    diff -r -U3 /tmp/Urho3D-master/Source/Urho3D/Graphics/GraphicsDefs.h ./Source/Urho3D/Graphics/GraphicsDefs.h
    --- /tmp/Urho3D-master/Source/Urho3D/Graphics/GraphicsDefs.h	2020-07-27 06:31:27.000000000 -0700
    +++ ./Source/Urho3D/Graphics/GraphicsDefs.h	2020-10-04 14:23:35.474301914 -0700
    @@ -136,6 +136,8 @@
        ELEMENT_POSITION = 0,
        ELEMENT_NORMAL,
        ELEMENT_COLOR,
    +    ELEMENT_COLOR2,
    +    ELEMENT_COLOR3,
        ELEMENT_TEXCOORD1,
        ELEMENT_TEXCOORD2,
        ELEMENT_CUBETEXCOORD1,
    @@ -452,21 +454,23 @@
    // Legacy vertex element bitmasks.
    enum VertexMask : unsigned
    {
    -    MASK_NONE = 0x0,
    -    MASK_POSITION = 0x1,
    -    MASK_NORMAL = 0x2,
    -    MASK_COLOR = 0x4,
    -    MASK_TEXCOORD1 = 0x8,
    -    MASK_TEXCOORD2 = 0x10,
    -    MASK_CUBETEXCOORD1 = 0x20,
    -    MASK_CUBETEXCOORD2 = 0x40,
    -    MASK_TANGENT = 0x80,
    -    MASK_BLENDWEIGHTS = 0x100,
    -    MASK_BLENDINDICES = 0x200,
    -    MASK_INSTANCEMATRIX1 = 0x400,
    -    MASK_INSTANCEMATRIX2 = 0x800,
    -    MASK_INSTANCEMATRIX3 = 0x1000,
    -    MASK_OBJECTINDEX = 0x2000,
    +    MASK_NONE            = 0x0000,
    +    MASK_POSITION        = 0x0001,
    +    MASK_NORMAL          = 0x0002,
    +    MASK_COLOR           = 0x0004,
    +    MASK_COLOR2          = 0x0008,
    +    MASK_COLOR3          = 0x0010,
    +    MASK_TEXCOORD1       = 0x0020,
    +    MASK_TEXCOORD2       = 0x0040,
    +    MASK_CUBETEXCOORD1   = 0x0080,
    +    MASK_CUBETEXCOORD2   = 0x0100,
    +    MASK_TANGENT         = 0x0200,
    +    MASK_BLENDWEIGHTS    = 0x0400,
    +    MASK_BLENDINDICES    = 0x0800,
    +    MASK_INSTANCEMATRIX1 = 0x1000,
    +    MASK_INSTANCEMATRIX2 = 0x2000,
    +    MASK_INSTANCEMATRIX3 = 0x4000,
    +    MASK_OBJECTINDEX     = 0x8000
    };
    URHO3D_FLAGSET(VertexMask, VertexMaskFlags);
    


In a copy of bin/CoreData/Shaders/GLSL/Transform.glsl called TransformC3.glsl, I've done this:

    --- bin/CoreData/Shaders/GLSL/Transform.glsl    2018-10-28 08:20:42.000000000 -0700
    +++ bin/CoreData/Shaders/GLSL/TransformC3.glsl  2020-10-04 14:28:03.170968864 -0700
    @@ -9,6 +9,8 @@
    attribute vec4 iPos;
    attribute vec3 iNormal;
    attribute vec4 iColor;
    +attribute vec4 iColor2;
    +attribute vec4 iColor3;
    attribute vec2 iTexCoord;
    attribute vec2 iTexCoord1;
    attribute vec4 iTangent;


In a copy of bin/CoreData/Shaders/GLSL/Unlit.glsl called UnlitC3.glsl, I've done this:

    --- bin/CoreData/Shaders/GLSL/Unlit.glsl        2018-10-28 08:20:42.000000000 -0700
    +++ bin/CoreData/Shaders/GLSL/UnlitC3.glsl      2020-10-04 17:24:30.407646913 -0700
    @@ -1,6 +1,6 @@
    #include "Uniforms.glsl"
    #include "Samplers.glsl"
    -#include "Transform.glsl"
    +#include "TransformC3.glsl"
    #include "ScreenPos.glsl"
    #include "Fog.glsl"
    
    @@ -8,6 +8,8 @@
    varying vec4 vWorldPos;
    #ifdef VERTEXCOLOR
        varying vec4 vColor;
    +    varying vec4 vColor2;
    +    varying vec4 vColor3;
    #endif
    
    void VS()
    @@ -20,8 +22,9 @@
    
        #ifdef VERTEXCOLOR
            vColor = iColor;
    +        vColor2 = iColor2;
    +        vColor3 = iColor3;
        #endif
    -
    }
    
    void PS()
    @@ -38,6 +41,7 @@
        #endif
    
        #ifdef VERTEXCOLOR
    +        // mix together multiple colors here
            diffColor *= vColor;
        #endif


I've defined a technique called DiffUnlitVCol3.xml as follows which utilizes the shader:

    <technique vs="UnlitC3" ps="UnlitC3" vsdefines="VERTEXCOLOR" psdefines="DIFFMAP VERTEXCOLOR">
        <pass name="base" />
    </technique>


And a material called VoxelsAtlas.xml which utilizes the technique:

    <material>
        <technique name="Techniques/DiffUnlitVCol3.xml" />
        <texture unit="diffuse" name="Textures/VoxelsAtlas.dds" />
    </material>


In my C++ application code I create a model using a vertex buffer with three colors per vertex and add it as a node to the scene.  In the PS function, in the shader UnlitC3.glsl, if I code "diffColor *= vColor;" I get what I would expect, but if I instead use "diffColor *= vColor2;" I get results which look like vec4 colors that are uninitialized (mainly the color black with some weird colors here and there).  I've verified the vertex buffer data is being filled in correctly on the application side, so I'm unsure what I'm most likely doing wrong in the Urho3D code changes.

-------------------------

Eugene | 2020-10-06 06:55:48 UTC | #3

[quote="Teknologicus, post:2, topic:6223"]
```
    VertexElement(TYPE_UBYTE4_NORM, SEM_COLOR, 0, false),    // Color
+    VertexElement(TYPE_UBYTE4_NORM, SEM_COLOR, 0, false),    // Color2
+    VertexElement(TYPE_UBYTE4_NORM, SEM_COLOR, 0, false),    // Color3
```
[/quote]

My best bet is on these lines. You don't have 3 color attributes, you have 3 declarations of the same color attribute.

-------------------------

Teknologicus | 2020-10-05 19:55:37 UTC | #4

Thank you.  Yes, indeed!  It should be:

        VertexElement(TYPE_UBYTE4_NORM, SEM_COLOR, 0, false),    // Color
    +    VertexElement(TYPE_UBYTE4_NORM, SEM_COLOR, 1, false),    // Color2
    +    VertexElement(TYPE_UBYTE4_NORM, SEM_COLOR, 2, false),    // Color3

-------------------------

Teknologicus | 2020-10-06 20:58:52 UTC | #5

Update:  It turned out I only needed two colors per vertex to achieve day/night sunlight transitions.  Here's what I had to change in the Urho3D source code and GLSL shaders:

    diff -r -U3 Urho3D-orig/Source/Urho3D/Graphics/GraphicsDefs.cpp Urho3D/Source/Urho3D/Graphics/GraphicsDefs.cpp
    --- Urho3D-orig/Source/Urho3D/Graphics/GraphicsDefs.cpp	2020-07-27 06:31:27.000000000 -0700
    +++ Urho3D/Source/Urho3D/Graphics/GraphicsDefs.cpp	2020-10-06 10:50:39.864288705 -0700
    @@ -97,6 +97,7 @@
        VertexElement(TYPE_VECTOR3, SEM_POSITION, 0, false),     // Position
        VertexElement(TYPE_VECTOR3, SEM_NORMAL, 0, false),       // Normal
        VertexElement(TYPE_UBYTE4_NORM, SEM_COLOR, 0, false),    // Color
    +    VertexElement(TYPE_UBYTE4_NORM, SEM_COLOR, 1, false),    // Color2
        VertexElement(TYPE_VECTOR2, SEM_TEXCOORD, 0, false),     // Texcoord1
        VertexElement(TYPE_VECTOR2, SEM_TEXCOORD, 1, false),     // Texcoord2
        VertexElement(TYPE_VECTOR3, SEM_TEXCOORD, 0, false),     // Cubetexcoord1
    diff -r -U3 Urho3D-orig/Source/Urho3D/Graphics/GraphicsDefs.h Urho3D/Source/Urho3D/Graphics/GraphicsDefs.h
    --- Urho3D-orig/Source/Urho3D/Graphics/GraphicsDefs.h	2020-07-27 06:31:27.000000000 -0700
    +++ Urho3D/Source/Urho3D/Graphics/GraphicsDefs.h	2020-10-06 10:50:28.364288693 -0700
    @@ -136,6 +136,7 @@
        ELEMENT_POSITION = 0,
        ELEMENT_NORMAL,
        ELEMENT_COLOR,
    +    ELEMENT_COLOR2,
        ELEMENT_TEXCOORD1,
        ELEMENT_TEXCOORD2,
        ELEMENT_CUBETEXCOORD1,
    @@ -452,21 +453,22 @@
    // Legacy vertex element bitmasks.
    enum VertexMask : unsigned
    {
    -    MASK_NONE = 0x0,
    -    MASK_POSITION = 0x1,
    -    MASK_NORMAL = 0x2,
    -    MASK_COLOR = 0x4,
    -    MASK_TEXCOORD1 = 0x8,
    -    MASK_TEXCOORD2 = 0x10,
    -    MASK_CUBETEXCOORD1 = 0x20,
    -    MASK_CUBETEXCOORD2 = 0x40,
    -    MASK_TANGENT = 0x80,
    -    MASK_BLENDWEIGHTS = 0x100,
    -    MASK_BLENDINDICES = 0x200,
    -    MASK_INSTANCEMATRIX1 = 0x400,
    -    MASK_INSTANCEMATRIX2 = 0x800,
    -    MASK_INSTANCEMATRIX3 = 0x1000,
    -    MASK_OBJECTINDEX = 0x2000,
    +    MASK_NONE            = 0x0000,
    +    MASK_POSITION        = 0x0001,
    +    MASK_NORMAL          = 0x0002,
    +    MASK_COLOR           = 0x0004,
    +    MASK_COLOR2          = 0x0008,
    +    MASK_TEXCOORD1       = 0x0010,
    +    MASK_TEXCOORD2       = 0x0020,
    +    MASK_CUBETEXCOORD1   = 0x0040,
    +    MASK_CUBETEXCOORD2   = 0x0080,
    +    MASK_TANGENT         = 0x0100,
    +    MASK_BLENDWEIGHTS    = 0x0200,
    +    MASK_BLENDINDICES    = 0x0400,
    +    MASK_INSTANCEMATRIX1 = 0x0800,
    +    MASK_INSTANCEMATRIX2 = 0x1000,
    +    MASK_INSTANCEMATRIX3 = 0x2000,
    +    MASK_OBJECTINDEX     = 0x4000
    };
    URHO3D_FLAGSET(VertexMask, VertexMaskFlags);
   

Transform.glsl:

    --- bin/CoreData/Shaders/GLSL/Transform~.glsl	2020-10-06 13:05:07.610963219 -0700
    +++ bin/CoreData/Shaders/GLSL/Transform.glsl	2020-10-06 10:44:42.510955016 -0700
    @@ -9,6 +9,7 @@
    attribute vec4 iPos;
    attribute vec3 iNormal;
    attribute vec4 iColor;
    +attribute vec4 iColor1;
    attribute vec2 iTexCoord;
    attribute vec2 iTexCoord1;
    attribute vec4 iTangent;


Unlit.glsl copied to UnlitC2.glsl with added uniform for sunlight level:

    --- bin/CoreData/Shaders/GLSL/Unlit.glsl	2018-10-28 08:20:42.000000000 -0700
    +++ bin/CoreData/Shaders/GLSL/UnlitC2.glsl	2020-10-06 12:33:46.287628103 -0700
    @@ -4,10 +4,13 @@
    #include "ScreenPos.glsl"
    #include "Fog.glsl"
    
    +uniform vec3 cSunlightLevel;
    +
    varying vec2 vTexCoord;
    varying vec4 vWorldPos;
    #ifdef VERTEXCOLOR
        varying vec4 vColor;
    +    varying vec4 vColor1;
    #endif
    
    void VS()
    @@ -20,8 +23,8 @@
    
        #ifdef VERTEXCOLOR
            vColor = iColor;
    +        vColor1 = iColor1;
        #endif
    -
    }
    
    void PS()
    @@ -38,7 +41,17 @@
        #endif
    
        #ifdef VERTEXCOLOR
    -        diffColor *= vColor;
    +        vec4 sun   = vColor,
    +             torch = vColor1,
    +             color;
    +        sun.r *= cSunlightLevel.r;
    +        sun.g *= cSunlightLevel.g;
    +        sun.b *= cSunlightLevel.b;
    +        color.r = sun.r > torch.r ? sun.r : torch.r;
    +        color.g = sun.g > torch.g ? sun.g : torch.g;
    +        color.b = sun.b > torch.b ? sun.b : torch.b;
    +        color.a = 1.0;
    +        diffColor *= color;
        #endif
    
        // Get fog factor

https://youtu.be/6y3sRwfXQv0

-------------------------

Modanung | 2020-10-07 07:15:29 UTC | #6

Wow, it's like the Efteling.

[details=""]
![](https://static.thousandwonders.net/Efteling.original.4346.jpg)
[/details]

-------------------------

