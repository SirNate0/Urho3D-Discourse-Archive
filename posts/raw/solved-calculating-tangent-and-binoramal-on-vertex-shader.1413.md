Bananaft | 2017-01-02 01:07:34 UTC | #1

I'm writing my own billboards, and i want them to use normal maps for lighting. I'm having hard time figuring out how to calculate tangent and binormal vectors.

I assumed, I can take direction towards the camera as normal, and then calculate right and up vectors as tangent and binormal. All in world space.

I've got pretty close to wanted result with this GLSL code:
VS:
[code]
  vec3 camUp = vec3(cCameraRot[0][1],cCameraRot[1][1],cCameraRot[2][1]);
  vec3 Dir = normalize(cCameraPos-worldPos);
  vec3 Right = normalize( cross( Dir , camUp));
  vec3 Up = normalize( cross( Right, Dir ) );
  vNormal = Dir;
  vBinormal = Up * -1;
  vTangent = Right;
[/code]
PS:
[code]
vec4 nmMap = texture2D(sDiffMap, vTexCoord.xy);
  if (nmMap.a < 0.5)
      discard;
  mat3 tbn = mat3(vTangent, vBinormal, vNormal);
  vec3 normal = DecodeNormal(nmMap) * tbn;[/code]

It looks alright, from all directions, but only as long as camera stays in parallel with horison. Looking top-down or changing camera rool will break proper orientation.

I've tried many other things, my brain is boiling up from all this vectors and matrices, and result is always crooked.

So, what am I missing here? What else can I try?

-------------------------

codingmonkey | 2017-01-02 01:07:34 UTC | #2

Did you read this topic ? code from Mahagam also not working correctly ?
[gamedev.ru/code/forum/?id=205849](http://www.gamedev.ru/code/forum/?id=205849)

-------------------------

Bananaft | 2017-01-02 01:07:34 UTC | #3

[quote="Sinoid"]Just add the normals and tangents to the vertex stream. So much easier.[/quote]
1)then I still need to calculate them
2)I can't with my solution. My mesh is bunch of quads, each shrinked to the point. The final vertex positions is calculated on vertex shader. It's pretty cool, because there is no need to change buffers in every frame. But storing normals and tangents won't make much sense.

full shader code, just in case:
[spoiler][code]
#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"


varying vec4 vTexCoord;
varying vec4 vWorldPos;
varying vec3 vNormal;
varying vec3 vBinormal;
varying vec3 vTangent;


void VS()
{
  mat4 modelMatrix = iModelMatrix;
  vec3 worldPos = GetWorldPos(modelMatrix) +  vec3(6*iTexCoord.x, 6*iTexCoord.y,0) * cCameraRot;
  gl_Position = GetClipPos(worldPos);
  vWorldPos = vec4(worldPos, GetDepth(gl_Position));
  //vec4 worldnorm = GetNearRay(gl_Position);
  vec3 camUp = vec3(cCameraRot[0][1],cCameraRot[1][1],cCameraRot[2][1]);
  vec3 Dir = normalize(cCameraPos-worldPos);
  vec3 Right = normalize( cross( Dir , camUp));
  vec3 Up = normalize( cross( Right, Dir ) );
  vNormal = Dir;
  vBinormal = Up * -1;
  vTangent = Right;

  vTexCoord = vec4(0.5 * iTexCoord + vec2(0.5,0.5),0,0);

}

void PS()
{
  vec4 nmMap = texture2D(sDiffMap, vTexCoord.xy);
  if (nmMap.a < 0.5)
      discard;
  mat3 tbn = mat3(vTangent, vBinormal, vNormal);
  vec3 normal = DecodeNormal(nmMap) * tbn;

  vec3 diffColor = vec3(1.0,1.0,1.0);
  vec3 ambient = diffColor.rgb * cAmbientColor * ( 0.5 * (normal.y + 1.0));



  #if defined(PREPASS)
      // Fill light pre-pass G-Buffer
      gl_FragData[0] = vec4(0.5, 0.9, 0.5, 1.0);
      gl_FragData[1] = vec4(EncodeDepth(vWorldPos.w), 0.0);
  #elif defined(DEFERRED)
      gl_FragData[0] = vec4(ambient , 1.0);
      gl_FragData[1] = vec4(diffColor.rgb, 0.0);
      gl_FragData[2] = vec4(normal * 0.5 + 0.5, 1.0);
      gl_FragData[3] = vec4(EncodeDepth(vWorldPos.w), 0.0);
  #else
      gl_FragColor = vec4(diffColor.rgb, diffColor.a);
  #endif
}
[/code][/spoiler]

-------------------------

Bananaft | 2017-01-02 01:07:35 UTC | #4

[quote="codingmonkey"]Did you read this topic ? code from Mahagam also not working correctly ?
[gamedev.ru/code/forum/?id=205849](http://www.gamedev.ru/code/forum/?id=205849)[/quote]
Will check that out, thank you.

-------------------------

Bananaft | 2017-01-02 01:07:36 UTC | #5

Well, turns out, my method was right. I only had to transpose final matrix (switch rows and columns). No Idea why it needed to be transposed. At this point I was desperately shuffling everything in the code.

-------------------------

