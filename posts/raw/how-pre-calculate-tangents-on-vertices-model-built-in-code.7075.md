ToolmakerSteve | 2021-12-01 18:59:56 UTC | #1

I'm making an MIT-licensed tool for "drawing" shapes (think "walls") on a terrain.

When the shape is done being drawn (pen lifted), I'd like to have an option to calculate tangent values (for normal map) and store in vertices.

I was thinking of doing this all in memory - not necessarily saving to a model file and reloading via asset loader. So can instantly see the rendering with normal map applied.

I have not yet done anything in urho with model saving/loading, other than load the sample models. So assume I know nothing about what urho has available.

If I do save it as a model, does urho's asset loader have an option to calculate those tangents at load time?

If so, is there a way I can call that on my model in memory?

------------------------------------

(If anyone knows of existing MIT-licensed code related to this topic, I'm interested in that also. Vaguely similar to google's Sketch Up. Blender is GPL, so I can't use any source from it. "permissive licensed" code only.)

Without normal map:
![crazy wall|690x388](upload://25fAd8mCvFurVVlETuEO1dRZMpP.jpeg)

-------------------------

Eugene | 2021-12-01 20:22:35 UTC | #2

[quote="ToolmakerSteve, post:1, topic:7075"]
If I do save it as a model, does urho’s asset loader have an option to calculate those tangents at load time?
[/quote]
There is no built-in preprocessing on Model load, it's always loaded as is. However, you _can_ generate tangents at the same time you generate Model and vertex buffers, see `Tangent.cpp`

-------------------------

ToolmakerSteve | 2021-12-02 04:20:25 UTC | #3

Having trouble getting model to display with tangents.

Material.xml:

	<material>
		<technique name="Techniques/DiffNormal.xml" quality="0" />
		<texture unit="diffuse" name="Textures/StoneWall4/white.jpg" />
		<texture unit="normal" name="Textures/StoneWall4/Wall Stone 004_NRM.jpg" />
	</material>

Note the diffuse map is white, to clearly see effect of normal map.

First, WITHOUT tangents on element - Position | Normal | TexCoord1 here is that material, used on standard Box model, and on one of my walls:

![no tangent|400x374](upload://xBp5xebw5NlwH5TF9WsWu23IVry.jpeg)

It is correct on Box. On wall, it is having effect, but of course normals are not right - as rotate around the object, at certain positions lighting effect changes dramatically.

------------------------------------------

When add tangent to element - Position | Normal | TexCoord1 | Tangent, it is good on top, but not on sides (the box can be seen behind it, still good.). [I assume that what the Box shows, on facing side, is what it should match.]

![with tangent - too gray|400x302](upload://949ujyIbGaudcScWEn5nwwxgfpX.jpeg)



This is the vertex data for the top quad and side quads:

||// TOP|
|---|---|
||(-31, 8.65625, -60), (0.0622449, 0.995919, 0.0653572), (0, 0), (0, -0.0654841, 0.997854, 1)|
||(-31, 8, -50), (0.0622449, 0.995919, 0.0653572), (2.50744, 0), (-0.00038677, -0.0654601, 0.997855, 1)|
||(-29, 8, -50), (0.0622449, 0.995919, 0.0653572), (2.50744, 0.50178), (-0.000773855, -0.065436, 0.997856, 1)|
||(-29, 8.53125, -60), (0.0622449, 0.995919, 0.0653572), (0, 0.50178), (-0.00038677, -0.0654601, 0.997855, 1)|
||// SIDE 1|
||(-29, 8.53125, -60), (1, -0, -0), (0, 0), (0, -0.0530502, 0.998592, 1)|
||(-29, 8, -50), (1, -0, -0), (2.50744, 0), (0, -0.0530502, 0.998592, 1)|
||(-29, -0.5, -50), (1, -0, -0), (2.50744, 2.12519), (0, -0.0530501, 0.998592, 1)|
||(-29, 0.03125, -60), (1, -0, -0), (0, 2.12519), (0, -0.0530502, 0.998592, 1)|
||// SIDE2|
||(-31, 8, -50), (1, -0, -0), (-2.5093, 0), (0, 0.0654841, -0.997854, -1)|
||(-31, 8.65625, -60), (1, -0, -0), (0, 0), (0, 0.0654842, -0.997854, -1)|
||(-31, 0.15625, -60), (1, -0, -0), (0, 2.12519), (0, 0.0654842, -0.997854, -1)|
||(-31, -0.5, -50), (1, -0, -0), (-2.5093, 2.12519), (0, 0.0654842, -0.997854, -1)|

(I don't show the "end" quad - it is correctly solid gray because its in shadow and texture is solid white. This can be seen on Box as well.)

I've verified that position, normal, and UV (texcoord) are all same as in the previous image - only tangent values are new.

Are there any unit tests that show correct Tangent output? I rewrote the code in C#: https://github.com/ToolmakerSteve/Avalonia_4/blob/Main/Urho_AvaloniaSample/ModelFrom2DShape/Tangent1.cs

I don't know how to determine if those tangent values are good.

------------------------------------------------

**UPDATE**

If I swap endpoints so that wall is drawn right-to-left instead of left-to-right, the lighting is correct - looks just the same on wall as on box. The relevant (good) data:

||// TOP|
|---|---|
||(-29, 8, -50), (0, 0.998592, 0.0530502), (0, 0), (0, 0.0530502, -0.998592, 1)|
||(-29, 8.53125, -60), (0, 0.998592, 0.0530502), (2.5093, 0), (0, 0.0530502, -0.998592, 1)|
||(-31, 8.65625, -60), (0, 0.998592, 0.0530502), (2.5093, 0.500847), (0, 0.0530502, -0.998592, 1)|
||(-31, 8, -50), (0, 0.998592, 0.0530502), (0, 0.500847), (0, 0.0530502, -0.998592, 1)|
||// SIDE1|
||(-31, 8, -50), (-1, -0, -0), (0, 0), (0, 0.0654841, -0.997854, 1)|
||(-31, 8.65625, -60), (-1, -0, -0), (2.5093, 0), (0, 0.0654842, -0.997854, 1)|
||(-31, 0.15625, -60), (-1, -0, -0), (2.5093, 2.12519), (0, 0.0654842, -0.997854, 1)|
||(-31, -0.5, -50), (-1, -0, -0), (0, 2.12519), (0, 0.0654842, -0.997854, 1)|
||// SIDE2|
||(-29, 8.53125, -60), (-1, -0, -0), (-2.50744, 0), (0, -0.0530502, 0.998592, -1)|
||(-29, 8, -50), (-1, -0, -0), (0, 0), (0, -0.0530502, 0.998592, -1)|
||(-29, -0.5, -50), (-1, -0, -0), (0, 2.12519), (0, -0.0530501, 0.998592, -1)|
||(-29, 0.03125, -60), (-1, -0, -0), (-2.50744, 2.12519), (0, -0.0530502, 0.998592, -1)|

I think I have some issue in my calculation of normals. Both sides have normal pointing same direction, which can't be right.

I'll debug that tomorrow.

-------------------------

ToolmakerSteve | 2021-12-02 04:50:34 UTC | #4

Fixed.
![wall - good normals and tangents|622x500](upload://tGwKSvWLBoQqAIYAg48Ui7Fg7ip.jpeg)

-------------------------

