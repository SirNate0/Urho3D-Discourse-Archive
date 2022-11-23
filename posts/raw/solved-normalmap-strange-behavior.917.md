codingmonkey | 2017-01-02 01:04:05 UTC | #1

Hi!
I'm create material for floor-plane that contains diffmap and normalmap and in normal map within the alpha channel i'm also store AO for this floor-plane .
And the strange behavior it is because in material editor it's looks - ok but on the object it's look as simple diffmap only.

[url=http://savepic.su/5364982.htm][img]http://savepic.su/5364982m.png[/img][/url]

-------------------------

codingmonkey | 2017-01-02 01:04:07 UTC | #2

Well, I found my problem. Then i going to look into shader code for how is normalmapped-objects draw.

 #ifndef NORMALMAP
        out float2 oTexCoord : TEXCOORD0,
    #else
        out float4 oTexCoord : TEXCOORD0,
        [b]out float4 oTangent : TEXCOORD3,[/b]

then doing export object need to be "tangent" option to be - ON

[url=http://savepic.su/5372648.htm][img]http://savepic.su/5372648m.png[/img][/url]

-------------------------

