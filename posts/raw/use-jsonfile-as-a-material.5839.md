Askhento | 2020-01-25 15:30:55 UTC | #1

I know that materials use .xml files, but I don't like them)) 
Is it possible to use JSON instead?

-------------------------

1vanK | 2020-01-25 20:00:42 UTC | #2

Urho3D Editor > View > Material Editor > Save As > *.json

-------------------------

Askhento | 2020-01-25 22:04:21 UTC | #3

Thnx for response)
Do you have an example file? Sounds stupid but I don't have editor haha

-------------------------

1vanK | 2020-01-25 23:22:51 UTC | #4

```
{
	"techniques": [
		{
			"name": "Techniques/NoTextureUnlit.xml",
			"quality": 0,
			"loddistance": 0.0
		}
	],
	"textures": null,
	"shaderParameters": {
		"UOffset": "1 0 0 0",
		"VOffset": "0 1 0 0",
		"MatDiffColor": "1 1 1 1",
		"MatEmissiveColor": "0 0 0",
		"MatEnvMapColor": "1 1 1",
		"MatSpecColor": "0 0 0 1",
		"Roughness": "0.5",
		"Metallic": "0"
	},
	"shaderParameterAnimations": null,
	"cull": "ccw",
	"shadowcull": "ccw",
	"fill": "solid",
	"depthbias": {
		"constant": 0.0,
		"slopescaled": 0.0
	},
	"alphatocoverage": false,
	"lineantialias": false,
	"renderorder": 128,
	"occlusion": true
}
```

-------------------------

Askhento | 2020-01-25 23:22:40 UTC | #5

It works! 
Thank you)

-------------------------

Askhento | 2020-02-17 22:28:39 UTC | #6

By the way what if I want to use EnvCube.xml Technique? Do you an example of a environment texture field in this case?

-------------------------

1vanK | 2020-02-17 22:42:44 UTC | #7

```
{
	"techniques": [
		{
			"name": "Techniques/DiffEnvCube.xml",
			"quality": 0,
			"loddistance": 0.0
		}
	],
	"textures": {
		"diffuse": "Textures/Mushroom.dds",
		"environment": "Textures/Skybox.xml"
	},
	"shaderParameters": {
		"UOffset": "1 0 0 0",
		"VOffset": "0 1 0 0",
		"MatDiffColor": "1 1 1 1",
		"MatEmissiveColor": "0 0 0",
		"MatEnvMapColor": "0.2 0.2 0.2",
		"MatSpecColor": "0.1 0.1 0.1 16",
		"Roughness": "0.5",
		"Metallic": "0"
	},
	"shaderParameterAnimations": null,
	"cull": "ccw",
	"shadowcull": "ccw",
	"fill": "solid",
	"depthbias": {
		"constant": 0.0,
		"slopescaled": 0.0
	},
	"alphatocoverage": false,
	"lineantialias": false,
	"renderorder": 128,
	"occlusion": true
}
```

-------------------------

Askhento | 2020-02-17 22:45:17 UTC | #8

Thank you! It seems that eventually I need the xml file "Textures/Skybox.xml"? Is there any way to set it as json also?

-------------------------

1vanK | 2020-02-17 22:52:47 UTC | #9

I found only `ParseTextureTypeXml` function in sources

-------------------------

