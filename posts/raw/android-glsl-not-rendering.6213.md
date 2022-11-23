najak3d | 2020-06-19 16:50:46 UTC | #1

I am creating a simple Plan geometry, so that I can control the Vertex definitions.  I only want Position and TEXCOORD1, no normals (unlike the built in plane.mdl).    So it's 5 floats per vertex (Vec3 for Position, plus Vec2 for UV coordinate).   I am using an Index Buffer, with 6 indices.

All works wonderfully on Windows, for HLSL.

But when I switch to Android with GLSL, it fails miserably.   My Vertex/Pixel Shaders for GLSL seem fine because they are butt simple and work just fine when applied to the Plane.Mdl.    However when I use my own manually generated Plane Geometry, it is NOT VISIBLE on Android.  No Errors, No Warnings in the log.  The Plane is simply just NOT THERE.   I've pared the GLSL vertex shader down to merely rendering RED, instead of even reading a DIFFUSE map....  still shows NOTHING.

I then simplified my Geometry to be Position-Only (no TEXCOORD), and still is shows NOTHING.  Other shaders work fine on Android, and so does the Plane if I use the Plane.MDL, but just not my manual geometry.

Here is the shader:
===
#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
}

void PS()
{
    gl_FragColor = vec4(1.0, 0.0, 1.0, 1.0);
}

===

and here is the code that sets up the Plane Geometry setup:
===
	private const int NUMVERTICES = 4;
	private const int NUMINDICES = 6;

	static private short[] _tileIndexData = new short[6] { 0, 2, 1, 0, 3, 2 }; // { 0, 1, 2, 0, 2, 3 };
...

	s_TileVertexData = new float[] {  -0.5f, 0, -0.5f,    0.5f, 0, -0.5f,     0.5f, 0, 0.5f,   -0.5f, 0, 0.5f  };

	_tileIndexBuffer = new IndexBuffer(UrhoApp.Context);
	_tileIndexBuffer.SetSize(NUMINDICES, false, false);
	_tileIndexBuffer.SetData(_tileIndexData);
	_tileBounds = new BoundingBox(-0.5f, 0.5f);

	VertexBuffer vb = new VertexBuffer(UrhoApp.Context);
	vb.SetSize(NUMVERTICES, ElementMask.Position); 
	vb.SetData(s_TileVertexData);

	Geometry g = new Geometry();
	g.SetVertexBuffer(0, vb);
	g.IndexBuffer = _tileIndexBuffer;
	g.SetDrawRange(PrimitiveType.TriangleList, 0, NUMINDICES, false);

	var model = new Model();
	model.NumGeometries = 1;
	model.SetGeometry(0, 0, g);
	model.BoundingBox = _tileBounds;

	_plane.Model = model;

	_material = _tileMaterial.Clone();
	_material.CullMode = CullMode.None;
	_plane.SetMaterial(_material);
===

Again -- all this works fine on Windows, but is NOT VISIBLE on Android and log shows no warnings or errors.

-------------------------

SirNate0 | 2020-06-19 23:17:53 UTC | #2

1. Does your plane model work with the built-in shaders? 
2. Does your shader work with other models? (You may have addressed that aspect, I'm not certain)

If 1 is tea and 2 is no (both on Android) then you probably have an error in your shader (OpenGL ES tends to be stricter than desktop OpenGL).
If 2 is yes and 1 is no then there's probably a problem with your model - my guess would be that the bounding box is incorrect and just happens to be initialized to a value that works on the desktop but on mobile you're not getting that lucky.

That said, that's just a guess, I could be completely wrong.

-------------------------

najak3d | 2020-06-20 00:21:06 UTC | #3

Thanks for the ideas SirNate0 -- that's what I was hoping for -- "Ideas" to get me unstuck and hints as to where the normal points of failure occur.  I'll post back after I finally resolve this.

-------------------------

najak3d | 2020-06-20 00:27:16 UTC | #4

Here's an interesting tidbit -- my shader and geometry both work fine on Android for a different scene sample.  It just doesn't work when I put it in the scene where I need it.  I'm in process of removing/deconstructing our application scene until we find out what aspect of this context is making the plane invisible.

-------------------------

najak3d | 2020-07-07 02:28:15 UTC | #5

FYI, the cause was Multi-sampling.  If enabled the base Multi-Sampling using "Graphics.SetMode()" (by setting it to 2), that's what caused wholesale failure of SOME shaders.   Setting it back to '1' fixed it.  Not sure why this was the case, but it's what seemed  to do the trick reliably.

-------------------------

