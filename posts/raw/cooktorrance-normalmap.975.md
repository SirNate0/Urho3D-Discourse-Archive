codingmonkey | 2017-01-02 01:04:33 UTC | #1

Hi folks!
Today i'm figure out how to add the affect of the NormalMap to CookTorrance lightning tech.

my tech DiffCookTorrance.xml based on Diff.xml
[code]
<technique vs="LitSolidCookTorrance" ps="LitSolidCookTorrance" psdefines="DIFFMAP NORMALMAP COOKTORRANCE">
    <pass name="base" />
    <pass name="litbase" psdefines="AMBIENT" />
    <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
    <pass name="prepass" psdefines="PREPASS" />
    <pass name="material" psdefines="MATERIAL" depthtest="equal" depthwrite="false" />
    <pass name="deferred" psdefines="DEFERRED" />
    <pass name="depth" vs="Depth" ps="Depth" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
</technique>
[/code]

CT without normalmap I guess works fine, 
[pastebin]DtpbyyXB[/pastebin]

But then i'm add normalmap most of the models are have strange behavior.

vec3 l = normalize (  cLightPosPS.xyz - vWorldPos.xyz);
vec3 n = normal;
float NoL = dot(n, l);
finalColor = (max(0.0, NoL) * ((diffCt.xyz + specCt.xyz))); - very bright in some angles view and color affecting on camera position
[url=http://savepic.net/6603347.htm][img]http://savepic.net/6603347m.png[/img][/url]


finalColor = (max(0.0, NoL) * ( diff * (diffCt.xyz + specCt.xyz))); - very dark in most angles view and color mostly constants and not affecting on scene lights 
[url=http://savepic.net/6566483.htm][img]http://savepic.net/6566483m.png[/img][/url]

I'm don't understand how to doing right affecting the normal mapping with CT tech.
Any ideas how to marge CT with normal mapping ?

-------------------------

codingmonkey | 2017-01-02 01:04:33 UTC | #2

>Tough to say without the CookTorrance function, but I'd really expect your specular color to be an input into the fresnel function in your CookTorrance function.
actual full source version of shader

[pastebin]4dvKwg2h[/pastebin]


i'm rewrite fresnel with: 
float fresnel = F_Schlick(mix(0.004, 0.9, cFresnel), NoV);
before i'm put cFresnel directly from material settings into CT function ( float ct = CookTorrance(h, NoV, NoL, NoH, VoH, cRougness, fresnel); ) and this in wrong as for me talked on gd.ru

>Probably just:
>finalColor = (max(0.0, NoL) * (((diffCt.xyz + specColor.xyz) * cLightColor.a));
No, it still have a same strange behavior with normal map and without it the CT lightning is - ok, I guess.

the bug with normal: it like the light change own direction and lightning the opposite side of model and not front side what it must lightning. And also this is huges specs on model's 
contours )

-------------------------

sabotage3d | 2017-01-02 01:04:47 UTC | #3

Hey man thanks for sharing this it looks quite cool .

-------------------------

