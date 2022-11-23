rasteron | 2017-01-02 01:08:32 UTC | #1

This is still a WIP..

[url=http://i.imgur.com/JCAkehi.png][img]http://i.imgur.com/JCAkehil.png[/img][/url]

..and don't ask about the mushroom headgear on the AIs, I know it's weird. Just testing node attachments there  :laughing:

-------------------------

codingmonkey | 2017-01-02 01:08:33 UTC | #2

nice, even shadow have a lines border )
did you use screen normal buffer for this freestyle lines effect ?

-------------------------

1vanK | 2017-01-02 01:08:33 UTC | #3

Maybe it will be useful
[wiki.unity3d.com/index.php/TeamFortress2Shader](http://wiki.unity3d.com/index.php/TeamFortress2Shader)

-------------------------

codingmonkey | 2017-01-02 01:08:36 UTC | #4

>Maybe it will be useful
it's very interesting)
I try to figure out with this little bit, a made some simplest test with toon.
actually in this picture below I use only diffuse texture (diff + ao) + ramp ramp texture from wiki TF topic. And rim color falls (from world pos) from - sky as emissive color

[url=http://savepic.su/6769984.htm][img]http://savepic.su/6769984m.png[/img][/url]

crappy shader (only for testing purpose) litSolidToon.glsl [pastebin.com/gbMLBacG](http://pastebin.com/gbMLBacG)

-------------------------

rasteron | 2017-01-02 01:08:40 UTC | #5

[quote="codingmonkey"]nice, even shadow have a lines border )
did you use screen normal buffer for this freestyle lines effect ?[/quote]

Thanks. :slight_smile: This was some older code that I was talking about on previous posts. It uses Sobel filters for edge detection.

-------------------------

rasteron | 2017-01-02 01:08:40 UTC | #6

[quote="codingmonkey"]>Maybe it will be useful
it's very interesting)
I try to figure out with this little bit, a made some simplest test with toon.
actually in this picture below I use only diffuse texture (diff + ao) + ramp ramp texture from wiki TF topic. And rim color falls (from world pos) from - sky as emissive color

[url=http://savepic.su/6769984.htm][img]http://savepic.su/6769984m.png[/img][/url]

crappy shader (only for testing purpose) litSolidToon.glsl [pastebin.com/gbMLBacG](http://pastebin.com/gbMLBacG)[/quote]

Nice, still looks close from reference though.

-------------------------

1vanK | 2017-01-02 01:09:24 UTC | #7

[quote="codingmonkey"]>
crappy shader (only for testing purpose) litSolidToon.glsl [pastebin.com/gbMLBacG](http://pastebin.com/gbMLBacG)[/quote]

It uses default lighting
[code]
float diff = GetDiffuse(normal, vWorldPos.xyz, lightDir);
[/code]

-------------------------

1vanK | 2017-01-02 01:09:24 UTC | #8

Urho used notnormalized directions ? It is correct?

[code]
float GetDiffuse(vec3 normal, vec3 worldPos, out vec3 lightDir)
{
        ...
        lightDir = cLightDirPS;
            ....
            return abs(dot(normal, lightDir));
[/code]

[code]
void PS()
{
    ...
    gl_FragColor = vec4(finalColor.rgb, 1.0);
    if (cLightDirPS != normalize(cLightDirPS))
        gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);
}
[/code]

[url=http://savepic.ru/8278727.htm][img]http://savepic.ru/8278727m.jpg[/img][/url]

-------------------------

1vanK | 2017-01-02 01:09:24 UTC | #9

[url=http://savepic.ru/8318699.htm][img]http://savepic.ru/8318699m.png[/img][/url]

Without self-shadowing and fog, only perpixel light sources and forward rendering

[code]void PS()
{
    // DIFF
    vec4 diffInput = texture2D(sDiffMap, vTexCoord.xy);
    vec3 normal = normalize(vNormal);
    float NdotL = dot(normal, normalize(cLightDirPS)) * 0.5 + 0.5;
    NdotL = clamp(NdotL, 0.01, 0.99);
    vec3 ramp = texture2D(sNormalMap, vec2(NdotL, 0.5)).rgb;
    vec3 finalColor = diffInput.rgb * ramp;
    
    // SPEC
    vec3 cameraDir = cCameraPosPS - vWorldPos.xyz;
    vec3 h = normalize(normalize(cLightDirPS) + normalize(cameraDir));
    float nh = max(0, dot(normal, h));
    float spec = pow(nh, 64);
    finalColor += cLightColor.rgb * spec;

    // RIM
    vec3 rimDir = normalize(cameraDir);
    float rimContribution = 1.0 - dot(normal, rimDir);
    rimContribution = clamp(rimContribution, 0.0, 1.0);
    rimContribution = pow(rimContribution, cRimPower);
    rimContribution = clamp(rimContribution, 0.0, 1.0);
    vec3 rimColor = rimContribution* cRimColor.rgb * cRimColor.a;
    finalColor += rimColor;
    
    gl_FragColor = vec4(finalColor.rgb, 1.0);
}
[/code]

Also i use ramp texture
[img]http://savepic.ru/8295145.png[/img]

-------------------------

1vanK | 2017-01-02 01:09:24 UTC | #10

Add selfshadowing and fog

[url=http://savepic.ru/8322801.htm][img]http://savepic.ru/8322801m.png[/img][/url]

[code]
void PS()
{
    // DIFF
    vec4 diffInput = texture2D(sDiffMap, vTexCoord.xy);
    vec3 normal = normalize(vNormal);
    float NdotL = dot(normal, normalize(cLightDirPS)) * 0.5 + 0.5;
    NdotL = clamp(NdotL, 0.01, 0.99);
    vec3 ramp = texture2D(sNormalMap, vec2(NdotL, 0.5)).rgb;
    #ifdef SHADOW
       ramp *= GetShadow(vShadowPos, vWorldPos.w);
    #endif
    ramp += cAmbientColor;
    ramp = clamp(ramp, 0.0, 1.0);
    vec3 finalColor = diffInput.rgb * ramp;
    
    // SPEC
    vec3 cameraDir = cCameraPosPS - vWorldPos.xyz;
    vec3 h = normalize(normalize(cLightDirPS) + normalize(cameraDir));
    float nh = max(0, dot(normal, h));
    float spec = pow(nh, 64);
    finalColor += cLightColor.rgb * spec;

    // RIM
    vec3 rimDir = normalize(cameraDir);
    float rimContribution = 1.0 - dot(normal, rimDir);
    rimContribution = clamp(rimContribution, 0.0, 1.0);
    rimContribution = pow(rimContribution, cRimPower);
    rimContribution = clamp(rimContribution, 0.0, 1.0);
    vec3 rimColor = rimContribution* cRimColor.rgb * cRimColor.a;
    finalColor += rimColor;
    
    // FOG
    #ifdef HEIGHTFOG
        float fogFactor = GetHeightFogFactor(vWorldPos.w, vWorldPos.y);
    #else
        float fogFactor = GetFogFactor(vWorldPos.w);
    #endif
    finalColor = GetFog(finalColor, fogFactor);
    
    gl_FragColor = vec4(finalColor.rgb, 1.0);
}
[/code]

For correct working it is needed to move the center of gradient to the bright side

[img]http://savepic.ru/8267505.png[/img]

-------------------------

1vanK | 2017-01-02 01:09:25 UTC | #11

Rim to outline (not perfect)

[url=http://savepic.ru/8317441.htm][img]http://savepic.ru/8317441m.png[/img][/url]

[code]
void PS()
{
    // DIFF
    vec4 diffInput = texture2D(sDiffMap, vTexCoord.xy);
    vec3 normal = normalize(vNormal);
    float NdotL = dot(normal, normalize(cLightDirPS)) * 0.5 + 0.5;
    NdotL = clamp(NdotL, 0.01, 0.99);
    vec3 ramp = texture2D(sNormalMap, vec2(NdotL, 0.5)).rgb;
    #ifdef SHADOW
       ramp *= GetShadow(vShadowPos, vWorldPos.w);
    #endif
    ramp += cAmbientColor;
    ramp = clamp(ramp, 0.0, 1.0);
    vec3 finalColor = diffInput.rgb * ramp;
    
    // SPEC
    vec3 cameraDir = cCameraPosPS - vWorldPos.xyz;
    vec3 h = normalize(normalize(cLightDirPS) + normalize(cameraDir));
    float nh = max(0, dot(normal, h));
    float spec = pow(nh, 64);
    finalColor += cLightColor.rgb * spec;

    // BLACK RIM
    vec3 rimDir = normalize(cameraDir);
    float rimContribution = dot(normal, rimDir);
    rimContribution = clamp(rimContribution * 1.5, 0.0, 1.0);
    finalColor *= rimContribution;
    
    // FOG
    #ifdef HEIGHTFOG
        float fogFactor = GetHeightFogFactor(vWorldPos.w, vWorldPos.y);
    #else
        float fogFactor = GetFogFactor(vWorldPos.w);
    #endif
    finalColor = GetFog(finalColor, fogFactor);
    
    gl_FragColor = vec4(finalColor.rgb, 1.0);
}
[/code]

-------------------------

thebluefish | 2017-01-02 01:09:25 UTC | #12

I'm totally going to grab that rim shader, I've always wanted rim lighting :p

-------------------------

