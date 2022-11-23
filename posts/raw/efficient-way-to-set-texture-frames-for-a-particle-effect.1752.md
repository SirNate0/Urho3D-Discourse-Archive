Enhex | 2017-01-02 01:09:52 UTC | #1

Is there any efficient way to set texture frames?
Right now it requires manually normalizing the min and max points of a frame to type them in and typing in the time.

-------------------------

codingmonkey | 2017-01-02 01:09:57 UTC | #2

Hi, did you trying doing similar stuff ?
this is from unity example with some fixes.

let's say
you got this texture:
[url=http://savepic.net/7702466.htm][img]http://savepic.net/7702466m.png[/img][/url]

this shader UnlitAnim
[code]#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"
#include "Fog.glsl"

varying vec2 vTexCoord;
varying vec4 vWorldPos;
#ifdef VERTEXCOLOR
    varying vec4 vColor;
#endif

#ifdef COMPILEVS

uniform float cAnimTime;
uniform float cAnimTileX;
uniform float cAnimTileY;

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vTexCoord = GetTexCoord(iTexCoord);
    vWorldPos = vec4(worldPos, GetDepth(gl_Position));
    
    int index = int(cAnimTime);  
    index = index % int(cAnimTileX * cAnimTileY);
    
    vec2 size = vec2(1.0 / float(cAnimTileX), 1.0 / float(cAnimTileY));
    
    // split into horizontal and vertical index
	int uIndex = index % int((cAnimTileX));
	int vIndex = index / int((cAnimTileY));
    
    
    vec2 finalFrame = iTexCoord;
    finalFrame.x /= cAnimTileX;
    finalFrame.y /= cAnimTileY;
    
    finalFrame += vec2((uIndex) * size.x, (vIndex) * size.y);
     
    vTexCoord = GetTexCoord(finalFrame);
    

    #ifdef VERTEXCOLOR
        vColor = iColor;
    #endif
}

#endif

void PS()
{
    // Get material diffuse albedo
    #ifdef DIFFMAP
        vec4 diffColor = cMatDiffColor * texture2D(sDiffMap, vTexCoord);
        #ifdef ALPHAMASK
            if (diffColor.a < 0.5)
                discard;
        #endif
    #else
        vec4 diffColor = cMatDiffColor;
    #endif

    #ifdef VERTEXCOLOR
        diffColor *= vColor;
    #endif

    // Get fog factor
    #ifdef HEIGHTFOG
        float fogFactor = GetHeightFogFactor(vWorldPos.w, vWorldPos.y);
    #else
        float fogFactor = GetFogFactor(vWorldPos.w);
    #endif

    #if defined(PREPASS)
        // Fill light pre-pass G-Buffer
        gl_FragData[0] = vec4(0.5, 0.5, 0.5, 1.0);
        gl_FragData[1] = vec4(EncodeDepth(vWorldPos.w), 0.0);
    #elif defined(DEFERRED)
        gl_FragData[0] = vec4(GetFog(diffColor.rgb, fogFactor), diffColor.a);
        gl_FragData[1] = vec4(0.0, 0.0, 0.0, 0.0);
        gl_FragData[2] = vec4(0.5, 0.5, 0.5, 1.0);
        gl_FragData[3] = vec4(EncodeDepth(vWorldPos.w), 0.0);
    #else
        gl_FragColor = vec4(GetFog(diffColor.rgb, fogFactor), diffColor.a);
    #endif
}[/code]

and this tech for material
[code]<technique vs="UnlitAnim" ps="UnlitAnim" psdefines="DIFFMAP" >
    <pass name="base" />
    <pass name="prepass" psdefines="PREPASS" />
    <pass name="material" />
    <pass name="deferred" psdefines="DEFERRED" />
</technique>[/code]

create material with this tech and add few uniform for shader (as show on picture bellow)
then try change animTime 
[url=http://savepic.net/7670722.htm][img]http://savepic.net/7670722m.png[/img][/url]

Probably you may try use this anim technique for animate particles:
I guess you need put into shader the arrays of uniforms or TBO (with personal particles data - frame(or time)) and fetch it by particle index. 
Or just extends(or use free element masks) vertex structure with additional data for each particle(+float time), I guess particles system feed one common VBO for all particles(per emitter) on cpu side every frame.

-------------------------

Enhex | 2017-01-02 01:09:57 UTC | #3

I'm talking about Urho's ParticleEffect frames, and the particle editor.
[img]http://i.imgur.com/rIbqVJj.jpg[/img]

Perhaps a visual tool for defining frame sets for sprite sheets could improve the workflow. Such tool can be generic.
Urho's editor will need an option to load frames from such frame set file.

-------------------------

