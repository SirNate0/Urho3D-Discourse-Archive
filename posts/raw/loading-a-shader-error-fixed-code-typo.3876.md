vivienneanthony | 2017-12-24 03:42:28 UTC | #1

I'm trying to load a shader following into the Shader class. One shader work but this one fails. Do anyone know what could be the cause

[code]
#include "Uniforms.glsl"
#include "Samplers.glsl"

uniform sampler2D positionmap;
uniform float texelSize;

void VS()
{
	gl_TexCoord[0].st = gl_MultiTexCoord0.st;
	gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
}

void PS()
{
 // Sample positions
  vec3 posX0Y0 = texture2D(positionmap, gl_TexCoord[0].st).rgb;
  vec3 posXMY0 = texture2D(positionmap, gl_TexCoord[0].st - vec2(texelSize, 0.0)).rgb;
  vec3 posXPY0 = texture2D(positionmap, gl_TexCoord[0].st + vec2(texelSize, 0.0)).rgb;
  vec3 posX0YM = texture2D(positionmap, gl_TexCoord[0].st - vec2(0.0, texelSize)).rgb;
  vec3 posX0YP = texture2D(positionmap, gl_TexCoord[0].st + vec2(0.0, texelSize)).rgb;
  
  // Edges connecting the samples
  vec3 edgeXM = posXMY0 - posX0Y0;
  vec3 edgeXP = posXPY0 - posX0Y0;
  vec3 edgeYM = posX0YM - posX0Y0;
  vec3 edgeYP = posX0YP - posX0Y0;
  
  // Using only one of these normals is faster but not as accurate
  vec3 normalM = cross(edgeXM, edgeYM);
  vec3 normalP = cross(edgeXP, edgeYP);
 
  // Normalize the sum of both normals (averaging happens automatically)
  vec3 normal = normalize(normalM + normalP);
  gl_FragData[0] = 0.5 + 0.5 * vec4(normal, 1.0);
  gl_FragData[1] = vec4(texture2D(positionmap, gl_TexCoord[0].st).a);
}
[/code]

The code to load is the following 

[code]
// Load resource cache
	ResourceCache * cache = g_pApp->GetConstantResCache();

	// Get Position Map
	shaderQuadNormalHeightMap = (Shader *) cache->GetResource("Shader",
			"CoreData/Shaders/GLSL/QuadTreeNormalHeightMap.glsl");

	if (!shaderQuadTreePositionMap) {
		URHO3D_LOGINFO("Loading Shader shaderprogQuadNormalHeightMap failed");
	} else {
		URHO3D_LOGINFO(
				"Loading Shader shaderprogQuadNormalHeightMap successful");

		String Defines1;
		String Defines2;

		ShaderVariation * vs0 = shaderQuadTreePositionMap->GetVariation(VS,
				Defines1);
		ShaderVariation * ps0 = shaderQuadTreePositionMap->GetVariation(PS,
				Defines2);

		shaderprogQuadNormalHeightMap = new ShaderProgram(g_pApp->GetGraphics(),
				vs0, ps0);
	}

	// Get Position Map
	shaderQuadTreePositionMap = (Shader *) cache->GetResource("Shader",
			"CoreData/Shaders/GLSL/QuadTreePositionMap.glsl");

	if (!shaderQuadTreePositionMap) {
		URHO3D_LOGINFO("Loading Shader shaderprogQuadTreePositionMap failed");
	} else {
		URHO3D_LOGINFO(
				"Loading Shader shaderprogQuadTreePositionMap successful");

		String Defines3;
		String Defines4;

		ShaderVariation * vs1 = shaderQuadTreePositionMap->GetVariation(VS,
				Defines3);
		ShaderVariation * ps1 = shaderQuadTreePositionMap->GetVariation(PS,
				Defines4);

		shaderprogQuadTreePositionMap = new ShaderProgram(g_pApp->GetGraphics(),
				vs1, ps1);
	}
[/code]

-------------------------

