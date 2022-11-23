Andre_B | 2017-02-02 17:34:49 UTC | #1

Im making an app for IOS using urho. 

I have a simple shader that all it does is offset a texture according to a simple ratio(AnimRatio), see fragment shader below:

> . #include "Uniforms.glsl"
> . #include "Transform.glsl"
> . #include "ScreenPos.glsl"
> . #include "Effects.glsl"

> uniform vec4 cClip;

> uniform sampler2D sLayer0;

> uniform vec4 cColor0;
> uniform float cAnimRatio;

> varying vec2 vCoord0;

> void PS()
> {
> 	if(gl_FragCoord.x < cClip.x || gl_FragCoord.x > cClip.z || gl_FragCoord.y < cClip.y || gl_FragCoord.y > cClip.w) discard;

>     vec4 chosenColor = cColor0;

>     // Coordinate offset
> 	vec2 newVCoords = vCoord0 + vec2(mix(1.0, 0.0, cAnimRatio), 0.0);
> 	vec2 offsetCoord = vec2(newVCoords.x, vCoord0.y);
>     vec4 color = texture2D(sLayer0, offsetCoord);
> 	float intensity = GetIntensity(color.rgb);

> 	chosenColor = vec4(cColor0.x * intensity * cColor0.a, cColor0.y * intensity * cColor0.a, cColor0.z * intensity * cColor0.a, intensity * cColor0.a);

>     gl_FragColor = chosenColor;
> }

However im facing some pixelization issues if i don't use the "highp" tag in "newVCoords" this variable directly affects the offset i apply to the texture coordinates.

However highp is not available on every device, and ive tried mediump which is widely available and i still see pixelization occurring.

Anny ideas?

-------------------------

Andre_B | 2017-02-06 21:18:53 UTC | #2

I just decided to offset the vertices on a vertex shader rather than changing the texture coordinates themselves.

-------------------------

