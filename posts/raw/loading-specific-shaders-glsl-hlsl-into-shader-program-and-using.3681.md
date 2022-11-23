vivienneanthony | 2017-10-24 18:26:51 UTC | #1

Hello,

I'm trying to implement some code. How can you directly load a glsl or hlsl into Urho3D that can be used by the shader program? I have to pass information into it utilizing the GPU. The code is the following.

Any input will help.. I can provide a sample of the code it's being used in at least the calls to the shader.

Vivienne

Planet.GLSL

    #include "Uniforms.glsl"
    #include "Samplers.glsl"

    uniform vec3      lightDir;
    uniform sampler2D colormap;
    uniform sampler2D heightmap;
    uniform sampler2D normalmap;
    uniform vec3      atmosphereColor;
    varying vec3      planetNormal;
    varying vec2      texCoord;
    varying float     dist;
    varying vec3  	  planetNormal;
    varying vec2  	  texCoord;
    varying float 	  dist;

    void PS()

    {
      gl_FragColor = vec4(0.0, 1.0, 0.0, 1.0);
    }

&nbsp;

PositionHeightMap.glsl
&nbsp;

    void VS()
    {
      planetNormal = normalize(gl_Vertex.xyz);
      texCoord = gl_MultiTexCoord0.st;
      gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
      dist = gl_Position.z;
    }

    #include "Uniforms.glsl"
    #include "Samplers.glsl"

    uniform sampler2D positionmap;
    uniform float texelSize;

    void VS()
    {
      gl_TexCoord[0].st = gl_MultiTexCoord0.st;
    	gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
    }

    NormalHeightMap.glsl
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




&nbsp;

PositionMap.glsl
  
    #include "Uniforms.glsl"
    #include "Samplers.glsl"
    uniform sampler2D permTex;
    uniform float heightScale;
    uniform unsigned int octaves;
    uniform float gain;
    uniform float lacunarity;
    uniform float offset;
    uniform float h;
    uniform float radius;
    varying vec3  cubePosition;

    #define TEXEL_FULL 0.003906250
    #define TEXEL_HALF 0.001953125
    #define FADE(t) ((t) * (t) * (t) * ((t) * ((t) * 6.0 - 15.0) + 10.0))

    float perlin(vec3 p)
    {
      vec3 p0i = TEXEL_FULL * floor(p) + TEXEL_HALF;
      vec3 p1i = p0i + TEXEL_FULL;
      vec3 p0f = fract(p);
      vec3 p1f = p0f - 1.0;
      
      vec3 u = FADE(p0f);
      
      // Could using a single RGBA texture for the four permutation table lookups increase performance?
      float perm00 = texture2D(permTex, vec2(p0i.y, p0i.z)).a;
      float perm10 = texture2D(permTex, vec2(p1i.y, p0i.z)).a;
      float perm01 = texture2D(permTex, vec2(p0i.y, p1i.z)).a;
      float perm11 = texture2D(permTex, vec2(p1i.y, p1i.z)).a;
      
      float a = dot(texture2D(permTex, vec2(p0i.x, perm00)).rgb * 4.0 - 1.0, vec3(p0f.x, p0f.y, p0f.z));
      float b = dot(texture2D(permTex, vec2(p1i.x, perm00)).rgb * 4.0 - 1.0, vec3(p1f.x, p0f.y, p0f.z));
      float c = dot(texture2D(permTex, vec2(p0i.x, perm10)).rgb * 4.0 - 1.0, vec3(p0f.x, p1f.y, p0f.z));
      float d = dot(texture2D(permTex, vec2(p1i.x, perm10)).rgb * 4.0 - 1.0, vec3(p1f.x, p1f.y, p0f.z));
      float e = dot(texture2D(permTex, vec2(p0i.x, perm01)).rgb * 4.0 - 1.0, vec3(p0f.x, p0f.y, p1f.z));
      float f = dot(texture2D(permTex, vec2(p1i.x, perm01)).rgb * 4.0 - 1.0, vec3(p1f.x, p0f.y, p1f.z));
      float g = dot(texture2D(permTex, vec2(p0i.x, perm11)).rgb * 4.0 - 1.0, vec3(p0f.x, p1f.y, p1f.z));
      float h = dot(texture2D(permTex, vec2(p1i.x, perm11)).rgb * 4.0 - 1.0, vec3(p1f.x, p1f.y, p1f.z));
      
      vec4 lerpZ = mix(vec4(a, c, b, d), vec4(e, g, f, h), u.z);
      vec2 lerpY = mix(lerpZ.xz, lerpZ.yw, u.y);
      return mix(lerpY.x, lerpY.y, u.x);
    }

    // http://mathproofs.blogspot.com/2005/07/mapping-cube-to-sphere.html
    vec3 cubeToSphere(vec3 pt)
    {
      vec3 ptSq = pt * pt;
      return pt.xyz * sqrt(max(1.0 - (ptSq.yzx + ptSq.zxy) * 0.5 + ptSq.yzx * ptSq.zxy * 0.3333333, 0.0));
    }

    float ridgedMultifractal(vec3 dir)
    {
      float frequency = lacunarity, signal, weight;
      
      // Get the base signal (absolute value to create the ridges; square for sharper ridges)
      signal = offset - abs(perlin(dir));
      signal *= signal;
      float result = signal;
      
      float exponentArraySum = 1.0;
      for (int i = 1; i < octaves; i++)
      {
        // This could be precalculated
        float exponentValue = pow(frequency, -h);
        exponentArraySum += exponentValue;
        frequency *= lacunarity;
        
        dir *= lacunarity;
        weight = clamp(signal * gain, 0.0, 1.0);
        
        // Get the next "octave" (only true octave if lacunarity = 2.0, right?)
        signal = offset - abs(perlin(dir));
        signal *= signal;
        signal *= weight;
        
        result += signal * exponentValue;
      }
      
      // Scale result to [0,1] (not true when offset != 1.0)
      result /= exponentArraySum;
      
      return result;
    }

    void VS()
    {
    	varying vec3 cubePosition;

    	// Vertex position on the cube [-1,1] is passed as texture coordinates
     	cubePosition = gl_MultiTexCoord0.xyz;
      
    	gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
    }

    void PS()
    {
      // Transform from cube [-1,1] to unit sphere
      vec3 spherePosition = cubeToSphere(cubePosition);
      
      // Calculate height value
      float rmf0 = ridgedMultifractal(spherePosition);
      
      // Scale and bias to match CPU implementation [-1,1]
      float rmf1 = rmf0 * 2.0 - 1.0;
      float height = 1.0 + rmf1 * heightScale;
      //height *= radius;
      
      // RGBA with surface position (RGB) and RMF value (A)
      gl_FragColor = vec4(spherePosition * height, rmf0);
    }

-------------------------

vivienneanthony | 2017-10-24 21:47:41 UTC | #2

I'm thinking that ShadeProgram should initalize and load a resource that adds then compile some source.

-------------------------

Eugene | 2017-10-24 21:57:24 UTC | #3

[quote="vivienneanthony, post:1, topic:3681"]
How can you directly load a glsl or hlsl into Urho3D that can be used by the shader program?
[/quote]

`ShaderProgram` constructor explicitly consumes `ShaderVariation`s that are generated by `Shader`.
So, you load `Shader`, make `ShaderVariation` and finally got a `ShaderProgram`

-------------------------

vivienneanthony | 2017-10-24 23:26:40 UTC | #4

After a compile I'm looking at that currently.  I'm checking would for the purpose I'm doing creating a global shader then telling a Graphics subsystem to use a shader at a particular time.

-------------------------

