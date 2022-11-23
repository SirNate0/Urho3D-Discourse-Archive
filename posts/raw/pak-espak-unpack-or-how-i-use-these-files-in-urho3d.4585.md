donbruno | 2018-10-09 18:23:38 UTC | #1

Hello,

I have some file:

Studio_1_Widescreen.jpg
Studio_1_Materials_33_0.pak
Studio_1.jpg
Studio_1.espak
info.json

and now my questions:

1.) can I decompress/unpack the .pak and the .espak?
2.) how I use these files in UrHo3D?

greetings and many thx
doniom

-------------------------

S.L.C | 2018-10-09 20:25:42 UTC | #2

There are a few ways to interpret the question.

1) the (an?) editor exported those files to generate your app (?) in which case you'd run the player to launch your app.

2) you expect the engine to provide IO functionality for those formats. in which case you must know that these might not be a standard or something common like a .zip file.

3) you want to implement your own custom package file. in which case the engine does not allow such thing by default. you'd have to break outside the engine scope and make a few modifications to the engine itself.

You'd have to be a bit more specific.

-------------------------

donbruno | 2018-10-10 08:51:34 UTC | #3

mmhh I have these files and I must unpack/pack these files... or I can used it in Urho3D

pak has a format like ULZ4
espak has a format like ELZ4

my info.json shows:
```
{
	"DistributionInfo": {
		"DistributionName": "Studio_1",
		"PackageFile": "Studio_1.espak",
		"Custom": false,
		"DistributeDate": "Thu Nov 30 09:20:20 2017",
		"CoverInfosCount": 0,
		"CoverInfos": [],
		"StudioInfosCount": 2,
		"StudioInfos": [
			{
				"Name": "Studio_1.xml",
				"ScenePath": "Scenes/Studio_1.xml",
				"ImagePath": "Studio_1.jpg"
			},
			{
				"Name": "Studio_1_Widescreen.xml",
				"ScenePath": "Scenes/Studio_1_Widescreen.xml",
				"ImagePath": "Studio_1_Widescreen.jpg"
			}
		]
	}
```

-------------------------

JTippetts | 2018-10-09 23:22:56 UTC | #4

Where did these package files come from? The file extension .espak leads me to believe it is some sort of package file for a different engine or game. Knowing where the thing came from, and what engine it was built for, would certainly help in determining if and how it could be converted to be used with Urho3D.

-------------------------

