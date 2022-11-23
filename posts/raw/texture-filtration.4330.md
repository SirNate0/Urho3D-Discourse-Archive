Blackfox | 2018-06-19 08:09:21 UTC | #1

I`m just newbe in Urho3d. So please help me.
For example I have stone.xml
material
    technique name="Techniques/DiffNormal.xml" quality="1" /
    technique name="Techniques/Diff.xml" quality="0" /
    texture unit="diffuse" name="Textures/StoneDiffuse.dds" /
    texture unit="normal" name="Textures/StoneNormal.dds" /
    shader psdefines="PACKEDNORMAL" /
    parameter name="MatSpecColor" value="0.3 0.3 0.3 16" /
/material
"
Where can I put "filter mode="nearest" /" string?
question2: Can I simple add strings from difenvcube.xml to difnormspec.xml to get difnormspecenvcube.xml?

-------------------------

jmiller | 2018-06-22 17:12:33 UTC | #2

Hello, and welcome to the forums!

[quote="Blackfox, post:1, topic:4330"]
Where can I put “filter mode=“nearest” /” string?
[/quote]

A texture definition XML file will be used if placed in the same location as the texture:
  https://urho3d.github.io/documentation/HEAD/_materials.html#Materials_Textures

Question 2 
Generally, Urho code and shaders have good consistency and can be copied/extended with minor changes as many of us have done. 
  https://urho3d.github.io/documentation/HEAD/_shaders.html
I'm half awake yet.. "couldn't hurt to try?" ;)

-------------------------

Blackfox | 2018-06-19 11:38:57 UTC | #3

Great thanks... :blush:

-------------------------

