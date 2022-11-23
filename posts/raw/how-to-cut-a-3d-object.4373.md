luvain | 2018-07-04 06:28:31 UTC | #1

Hello everyone, I'm new to urho.
Could anyone pls help me with question about how to clipping a 3d object, I just want to do the same like here by urho.
https://stackoverflow.com/questions/43916002/three-js-how-to-cut-a-3d-object-with-y-plane

-------------------------

jmiller | 2018-07-04 16:54:23 UTC | #2

Hello, and welcome to the forum!

There have been a number of [url=https://en.wikipedia.org/wiki/Constructive_solid_geometry]CSG[/url]-related threads that may be helpful.
https://discourse.urho3d.io/search?q=CSG

-------------------------

luvain | 2018-07-05 01:19:17 UTC | #3

Thanks a lot, but is there any easy solution?
I just want let a model which assigned material disappear slowly from left to right.

-------------------------

jmiller | 2018-07-05 04:47:34 UTC | #4

..now I think a better approach could be material-based, like heXon used; discussion and shaders:
https://discourse.urho3d.io/t/models-dissolving-like-doom-3/1625/12

-------------------------

luvain | 2018-07-05 06:51:41 UTC | #5

Thanks your quick answer, is there any more easy way?
In three.js just set a clipping plan for material is enough:sweat_smile:
I do some research on urho, it just can set the clipping plane in camera.
could we do it by set animation or mask ?:scream:

-------------------------

luvain | 2018-07-08 22:15:18 UTC | #6

I'm new to urho3d, want to make a effect about box disappear from top to buttom slowly.
After do some research I find that need to implement it by custom shader. I known how to do it by Unity3d, like below, but have no idea in Urho3d's shader. especially how to clip in the ps() method.
Pass
        {
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag

            #include "UnityCG.cginc"

            struct appdata
            {
                float4 vertex : POSITION;
                float2 uv : TEXCOORD0;

            };

            struct v2f
            {
                float3 uv : TEXCOORD0;

                float4 vertex : SV_POSITION;
            };

            sampler2D _MainTex;
            float4 _MainTex_ST;
            float _DisappearOffset;

            v2f vert (appdata v)
            {
                v2f o;
                o.vertex = UnityObjectToClipPos(v.vertex);
                o.uv.xy = TRANSFORM_TEX(v.uv, _MainTex);
                o.uv.z = _DisappearOffset - v.vertex.y;
                return o;
            }

            xed4 frag (v2f i) : SV_Target
            {
                clip(i.uv.z);
                fixed4 col = tex2D(_MainTex, i.uv.xy);
                return col;
            }
            ENDCG
        }




![20171017154441749|690x373](upload://aIp7cVG7gOJVPNdhbj8BvyUOCsW.png)

-------------------------

jmiller | 2018-07-08 22:37:51 UTC | #7

Basically it's GLSL/HLSL.. Pages on Shaders, Rendering, etc. at [url=https://urho3d.github.io/documentation/HEAD/pages.html]Related pages[/url] go into detail.
Dunno if Modanung's shader is worth a look for this...

*or maybe a graphics programming Q&A site ..

-------------------------

Modanung | 2018-07-12 14:50:58 UTC | #8

[quote="jmiller, post:7, topic:4373"]
Dunno if Modanung’s shader is worth a look for this…
[/quote]

1vanK created the dissolve shader, if that's the shader you mean.

My first try for this would be to set alpha to 0 when y > 0 in the fragment shader.

-------------------------

