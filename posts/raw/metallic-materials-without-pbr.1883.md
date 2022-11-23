1vanK | 2017-01-02 01:11:04 UTC | #1

It used spec map as reflection map

[url=http://savepic.ru/8996896.htm][img]http://savepic.ru/8996896m.png[/img][/url]
[url=http://savepic.ru/9005088.htm][img]http://savepic.ru/9005088m.png[/img][/url]

In litsolid.glsl replace all

[code]        #ifdef ENVCUBEMAP
            finalColor += cMatEnvMapColor * textureCube(sEnvCubeMap, reflect(vReflectionVec, normal)).rgb;
        #endif[/code]
to
[code]
        #ifdef ENVCUBEMAP
            finalColor += cMatEnvMapColor * textureCube(sEnvCubeMap, reflect(vReflectionVec, normal)).rgb * specColor * cAmbientColor;
        #endif
[/code]

Example technique (just add ENVCUBEMAP and SPECMAP everywhere, also technique should be without litbase pass)
[code]<technique vs="LitSolid" ps="LitSolid" psdefines="DIFFMAP">
    <pass name="base"  vsdefines="NORMALMAP ENVCUBEMAP SPECMAP" psdefines="ENVCUBEMAP AMBIENT NORMALMAP SPECMAP"/>
    <pass name="light" vsdefines="NORMALMAP ENVCUBEMAP SPECMAP" psdefines="ENVCUBEMAP NORMALMAP SPECMAP" depthtest="equal" depthwrite="false" blend="add" />
    <pass name="depth" vs="Depth" ps="Depth" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
</technique>
[/code]

Example material:
[code]<?xml version="1.0"?>
<material>
	<technique name="Techniques/MyDiffNormalSpecEnvCube.xml" />
	<texture unit="diffuse" name="Textures/Cerberus_A.tga" />
	<texture unit="normal" name="Textures/Cerberus_N.tga" />
	<texture unit="environment" name="Textures/Skybox.xml" />
	<texture unit="specular" name="Textures/Cerberus_A.tga" />
	<parameter name="MatDiffColor" value="1 1 1 1" />
	<parameter name="MatSpecColor" value="1 1 1 100" />
	<parameter name="MatEnvMapColor" value="1 1 1 1" />
</material> [/code]

-------------------------

dragonCASTjosh | 2017-01-02 01:11:04 UTC | #2

Nice work, i will not that the IBL looks to have the same problem PBR had when i picked it up from sinoid where the reflections look greasy, to solve this you have to change the way reflections are rendered. In addition to this Metallic in a real work senario do you accept diffuse, the more metallic the less diffuse. I believe your results are what developers did before the mainstream of PBR within modern engines.

-------------------------

