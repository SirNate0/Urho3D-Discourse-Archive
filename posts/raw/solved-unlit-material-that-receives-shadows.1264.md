rasteron | 2017-01-02 01:06:29 UTC | #1

Is there a way for an object or material to be unlit and at the same time still receive shadows?

I found a similar issue and a possible solution to this at polycount forums, but it's a unity shader code:

[polycount.com/forum/showthread.php?p=2325341](http://www.polycount.com/forum/showthread.php?p=2325341)

[code]
Shader "Unlit With Shadows" {
	Properties {
		_Color ("Main Color", Color) = (1,1,1,1)
		_MainTex ("Base (RGB)", 2D) = "white" {}
	}
	SubShader {
		Tags {"Queue" = "Geometry" "RenderType" = "Opaque"}

		Pass {
			Tags {"LightMode" = "ForwardBase"}
			CGPROGRAM
				#pragma vertex vert
				#pragma fragment frag
				#pragma multi_compile_fwdbase
				#pragma fragmentoption ARB_fog_exp2
				#pragma fragmentoption ARB_precision_hint_fastest
				
				#include "UnityCG.cginc"
				#include "AutoLight.cginc"
				
				struct v2f
				{
					float4	pos			: SV_POSITION;
					float2	uv			: TEXCOORD0;
					LIGHTING_COORDS(1,2)
				};

				float4 _MainTex_ST;

				v2f vert (appdata_tan v)
				{
					v2f o;
					
					o.pos = mul( UNITY_MATRIX_MVP, v.vertex);
					o.uv = TRANSFORM_TEX (v.texcoord, _MainTex).xy;
					TRANSFER_VERTEX_TO_FRAGMENT(o);
					return o;
				}

				sampler2D _MainTex;

				fixed4 frag(v2f i) : COLOR
				{
					fixed atten = LIGHT_ATTENUATION(i);	// Light attenuation + shadows.
					//fixed atten = SHADOW_ATTENUATION(i); // Shadows ONLY.
					return tex2D(_MainTex, i.uv) * atten;
				}
			ENDCG
		}

		Pass {
			Tags {"LightMode" = "ForwardAdd"}
			Blend One One
			CGPROGRAM
				#pragma vertex vert
				#pragma fragment frag
				#pragma multi_compile_fwdadd_fullshadows
				#pragma fragmentoption ARB_fog_exp2
				#pragma fragmentoption ARB_precision_hint_fastest
				
				#include "UnityCG.cginc"
				#include "AutoLight.cginc"
				
				struct v2f
				{
					float4	pos			: SV_POSITION;
					float2	uv			: TEXCOORD0;
					LIGHTING_COORDS(1,2)
				};

				float4 _MainTex_ST;

				v2f vert (appdata_tan v)
				{
					v2f o;
					
					o.pos = mul( UNITY_MATRIX_MVP, v.vertex);
					o.uv = TRANSFORM_TEX (v.texcoord, _MainTex).xy;
					TRANSFER_VERTEX_TO_FRAGMENT(o);
					return o;
				}

				sampler2D _MainTex;

				fixed4 frag(v2f i) : COLOR
				{
					fixed atten = LIGHT_ATTENUATION(i);	// Light attenuation + shadows.
					//fixed atten = SHADOW_ATTENUATION(i); // Shadows ONLY.
					return tex2D(_MainTex, i.uv) * atten;
				}
			ENDCG
		}
	}
	FallBack "VertexLit"
}
[/code]

Maybe a possible conversion and added to the materials section? thanks in advance..

-------------------------

codingmonkey | 2017-01-02 01:06:29 UTC | #2

add shadow pass into your unlit material tech

DiffUnlit.xml (with shadows)

[code]<technique vs="Unlit" ps="Unlit" psdefines="DIFFMAP" >
    <pass name="base" />
    <pass name="prepass" psdefines="PREPASS" />
    <pass name="material" />
    <pass name="deferred" psdefines="DEFERRED" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
</technique>[/code]

[url=http://savepic.net/7121451.htm][img]http://savepic.net/7121451m.png[/img][/url]

-------------------------

rasteron | 2017-01-02 01:06:29 UTC | #3

Thanks CodingMonkey, :slight_smile: but sorry for not being specific. I was aiming for something like grass types such as vegetation with Alpha mask, whereas the grass objects or billboards are unlit (double sided) and still receive shadows.

Another example problem like this one on Unreal Forums:

[answers.unrealengine.com/questi ... adows.html](https://answers.unrealengine.com/questions/53579/possible-for-unlit-material-to-receive-shadows.html)

[img]http://i.imgur.com/Nowy9tV.png[/img]

With the current 'lit' shader, it does receive shadows but has this weird toasted effect when it is not on the lighted side.

-------------------------

codingmonkey | 2017-01-02 01:06:29 UTC | #4

In this case you need take some basic tech based on LitSolid shader like Diff.xml and delete all thing about lightning in shader for this new tech.
but you need keep the things about shadows in shader.
actually I'm try this, with this

create tech
[code]
<technique vs="UnlitWithShadows" ps="UnlitWithShadows" vsdefines = "DIFFMAP PERPIXEL" psdefines="DIFFMAP PERPIXEL" >
    <pass name="base" />
    <pass name="light" vsdefines="NORMALMAP" psdefines="NORMALMAP PACKEDNORMAL" depthtest="equal" depthwrite="false" blend="add" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
</technique>
[/code]

and shader for tech - UnlitWithShadows
[spoiler][pastebin]5bzW51Rf[/pastebin][/spoiler]

[url=http://savepic.net/7118390.htm][img]http://savepic.net/7118390m.png[/img][/url]

node: unlit object what receive shadows must do not cast shadows. if it will be cast shadows - they will lay on it own (self shadowing effect)

but there is have a strange bug if light count are more then 1 near the unlited object - overbright, I think it's because light pass are "add" all light what placed around on object's surface.
I do not know how to fix this. There is need somebody more competent in this.

-------------------------

rasteron | 2017-01-02 01:06:29 UTC | #5

Hey thanks, works like a charm. :slight_smile: BUT my main concern really is I do intend it to use it with [b]AlphaMask[/b] and [b]Vegetation[/b] Technique and not just solid textured objects. Do I just add the passes below?

..and maybe a GLSL version of the shader if it's not a bit of a stretch?  :wink:

-------------------------

rasteron | 2017-01-02 01:06:31 UTC | #6

Somehow, I just got a simple workaround in adjusting the ambient settings on my lighting setup. It would still be a good addition if something like this can be done with Alpha Mask and GLSL.

Appreciate all the help on this CodingMonkey! :smiley:

-------------------------

rasteron | 2017-01-02 01:06:32 UTC | #7

[quote="Sinoid"][quote]It would still be a good addition if something like this can be done with Alpha Mask and GLSL.[/quote]

Discarding the fragment in shadowmap rendering based on alpha is probably the best you can do (barring changes). The shadowmaps are R16 or R32 formats so there's nothing for an actual alpha value.[/quote]

Thanks Sinoid, maybe an example code to test out?

-------------------------

rasteron | 2017-01-02 01:06:35 UTC | #8

[quote="Sinoid"]It's actually all already there in the existing shadow shaders:
[code]
void PS()
{
    #ifdef ALPHAMASK
        float alpha = texture2D(sDiffMap, vTexCoord).a;
        if (alpha < 0.5)
            discard;
    #endif

    gl_FragColor = vec4(1.0);
}
[/code]

So you probably haven't added the ALPHAMASK define to your shadow pass in the technique.[/quote]

Thanks, will try that one next time.

-------------------------

