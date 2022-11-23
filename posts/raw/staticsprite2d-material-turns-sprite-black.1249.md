practicing01 | 2017-01-02 01:06:23 UTC | #1

Hello, I'm trying to set a material to a StaticSprite2D and it appears as a black square when I do.  Thanks for any help.

Edit: With DiffLitParticleAlpha and some other techniques, the sprite is visible.  However, I'm interested in normal maps.  Is there a technique without normal in its name, that applies the normal map?

Material:
[code]
<?xml version="1.0"?>
<material>
        <technique name="Techniques/DiffNormal.xml" />
        <texture unit="diffuse" name="Urho2D/cleric/cleric.png" />
        <texture unit="normal" name="Urho2D/cleric/clericN.png" />
        <parameter name="UOffset" value="1 0 0 0" />
        <parameter name="VOffset" value="0 1 0 0" />
        <parameter name="MatDiffColor" value="1 1 1 1" />
        <parameter name="MatEmissiveColor" value="0 0 0" />
        <parameter name="MatEnvMapColor" value="1 1 1" />
        <parameter name="MatSpecColor" value="1 1 1 16" />
        <cull value="none" />
        <shadowcull value="none" />
        <fill value="solid" />
</material>
[/code]

-------------------------

