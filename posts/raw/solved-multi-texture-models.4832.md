sandsound | 2019-01-29 12:48:18 UTC | #1

Sorry if this have been answered elsewhere, but I haven't been able to find any examples of using multiple textures on a model, is this at all possible?

I wanted to use one of the Mixamo-models (Erika-archer) for my game, but are having a lot of problems. One of them is that her body apparently uses another texture than her clothes.

Would be awesome if someone had the model game-ready for download, but I'd also be happy if someone could just point me in the right direction.

-------------------------

Leith | 2019-01-17 12:05:15 UTC | #2

Yes it is possible. Models can have multiple materials and meshes, and each mesh can use a different material.
You can make a car with four wheels that use a rubber tyre material, and not need four wheel meshes, as well.
The windscreen and other windows can be made of another material, this is fine, within a single model.

-------------------------

sandsound | 2019-01-17 13:06:03 UTC | #3

Do you know of any examples of this?
just a basic one would be great since I have a hard time learning something without seeing it in action.

-------------------------

Dave82 | 2019-01-17 13:31:22 UTC | #4

You can set a material per geometry by calling animatedModel->SetMaterial(geometryId , material);
The number of geometries can be checked by calling model->GetNumGeometries();

-------------------------

Modanung | 2019-01-17 14:06:13 UTC | #5

If you create a ModelName.txt file in the same directory as the model you can call `ApplyMaterialList()` on the model component. This file would simply contain a list of the names of the materials.
```
Materials/Mat0.xml
Materials/Mat1.xml
Materials/Mat2.xml
```

-------------------------

I3DB | 2019-01-17 17:59:09 UTC | #6

How about for this [model for Jack](https://github.com/xamarin/urho-samples/blob/master/FeatureSamples/Assets/Data/Models/Jack.mdl)?

I've been trying to get [the Jack.mdl model here](https://github.com/xamarin/urho-samples/blob/master/FeatureSamples/Assets/Data/Models/Jack.mdl) to use the face and body textures.

It [has an associated material](https://github.com/xamarin/urho-samples/blob/master/FeatureSamples/Assets/Data/Materials/Jack.xml), but it's been edited to use no texture.

However, there are two textures, [here](https://github.com/xamarin/urho-samples/blob/master/FeatureSamples/Assets/Data/Textures/Jack_body_color.jpg) and [here](https://github.com/xamarin/urho-samples/blob/master/FeatureSamples/Assets/Data/Textures/Jack_face.jpg) that seem like the right ones.

How would the Material/Jack file need to be edited to include those two textures for this one model?

-------------------------

sandsound | 2019-01-17 18:03:54 UTC | #7

Thanks for all the tips, I think I have an idea of how to do this now.

It would still be nice if there was an example in the samples, perhaps just a change in one of the existing samples?

-------------------------

Dave82 | 2019-01-17 18:52:40 UTC | #8

[quote="I3DB, post:6, topic:4832"]
How about for this [model for Jack](https://github.com/xamarin/urho-samples/blob/master/FeatureSamples/Assets/Data/Models/Jack.mdl)?
[/quote]

Create two materials JackBody.xml and JackHead.xml set technique , and diffuse texture unit to your corresponding texture files. And finally create a Jack.txt file and set to point to your materials.(as Modanung suggested)

-------------------------

I3DB | 2019-01-17 23:03:25 UTC | #9

@Dave82
1. Created the two files, JackBody/JackHead.xml in materials folder.
2. Copied the existing Jack.xml contents to each, and modified the texture of each
3. Created the Jack.txt file where Jack.mdl exists and added paths to the jack materials.
4. Made code change to ApplyMaterialList and removed to previous call to setmaterial to jack.xml. 

Tested ... couldn't find Materials/JackHead.xml
```
ERROR: Could not find resource ﻿Materials/JackHead.xml
````

Tried putting in path in Jack.txt as  ../Materials/JackHead.xml ... same error.
Created a new folder Materials inside the models folder and put materials there .... same error.
Put materials in models folder as same level as Jack.mdl and edited paths in Jack.txt to just file names ...  same error.

If I load the JackHead.xml material just by itself or JackBody.xml, both load fine.

If I set the material directly using either the head or body, nothing paints but default material, but no error messages.

```
modelObject.Material = Application.ResourceCache.GetMaterial("Materials/JackBody.xml");
```

But this will give Jack a colored body:
```
modelObject.Material = Material.FromColor(Randoms.NextColor());
```

Seems simple enough, what am I missing?

Here is the JackHead.xml file after edit:
```
<material>
  <technique name="Techniques/NoTexture.xml" />
  <parameter name="MatSpecColor" value="0.5 0.5 0.5 16" />
  <texture unit="diffuse" name="Materials/Jack_face.jpg" />
</material>
```

And the Jack.txt file contents:
```
JackHead.xml
JackBody.xml
```

-------------------------

I3DB | 2019-01-17 22:56:57 UTC | #10

As @sandsound pointed out, a working sample really is useful. When I try this simple case, the error messages aren't helpful enough to figure out the problem.

-------------------------

Modanung | 2019-01-17 23:15:45 UTC | #11

[quote="I3DB, post:9, topic:4832"]
&lt;technique name="Techniques/**NoTexture**.xml" /&gt;
&lt;**texture** unit="diffuse" name="Materials/Jack_face.jpg" /&gt;
[/quote]
The `NoTexture` technique does not support textures.

-------------------------

I3DB | 2019-01-17 23:23:50 UTC | #12

[quote="Modanung, post:11, topic:4832"]
> &lt;technique name=“Techniques/ **NoTexture** .xml” /&gt;
> &lt; **texture** unit=“diffuse” name=“Materials/Jack_face.jpg” /&gt;

The `NoTexture` technique does not support textures.
[/quote]

And ... is there a technique which does? Could you give a clue?

-------------------------

Eugene | 2019-01-17 23:26:43 UTC | #13

[quote="I3DB, post:12, topic:4832"]
And … is there a technique which does? Could you give a clue?
[/quote]

Any technique with the word `Diff`, depending on your final goal.

-------------------------

I3DB | 2019-01-17 23:28:21 UTC | #14

I'd really just like to see a working example where more than one material is added to one model.

That is my goal.

-------------------------

Eugene | 2019-01-17 23:32:15 UTC | #15

I'm not 100% sure for Urho#, but there shall be someting like `Materials`, or some other plural property or function to setup materials for model. Or use text file, but all resource names still have to be "absolute" (relative to base resource folders)

[quote="I3DB, post:9, topic:4832"]
And the Jack.txt file contents:

```
JackHead.xml
JackBody.xml
```
[/quote]

-------------------------

I3DB | 2019-01-18 00:32:20 UTC | #16

I got it working, but it's not working ...

```
modelObject.ApplyMaterialList();
modelObject.Material = Application.ResourceCache.GetMaterial("Materials/JackBody.xml");
```
ApplyMaterialList() throws this error::
```
ERROR: Could not find resource ﻿Materials/JackBody.xml
```
But does paint Jack's head.
The next line paints Jack's body. No problems finding the material I guess.

JackHead.xml contents
```
<material>
  <technique name="Techniques/Diff.xml" />
  <parameter name="MatSpecColor" value="0.5 0.5 0.5 16" />
  <texture unit="diffuse" name="Jack_face.jpg" />
</material>
```

JackBody.xml contents
```
<material>
  <technique name="Techniques/Diff.xml" />
  <parameter name="MatSpecColor" value="0.5 0.5 0.5 16" />
  <texture unit="diffuse" name="Jack_body_color.jpg" />
</material>
```

Jack.txt contents
```
Materials/JackBody.xml
Materials/JackHead.xml
```

If the two lines are swapped in Jack.txt, then Jack's head gets the body material.
modelObject.Material = always sets the body's material, never the head.

Also, changing the path on texture of either file, for instance to:
```
  <texture unit="diffuse" name="Textures/Jack_body_color.jpg" />
```
makes no difference. There is a single Jack_body_color.jpg and setting material directly finds it regardless of the path set differently, and has no effect on the errors thrown by ApplyMaterialList().

-------------------------

I3DB | 2019-01-18 00:52:19 UTC | #17

The issue is whichever resource is listed first in Jack.txt is never found. If it's the second line, it works fine.

Created the file in visual studio by adding a new file. Edited the contents also in visual studio. Probably something to do with encoding or line endings.

But there is a workaround, and this is then to set the material using whatever was on the first line of the .txt file. That setting overrides the first line of the .txt, which isn't set due to some issue reading the file.

Tried adding a space and a blank line to that first line. If a blank first line, both of the resources are found, but the body will be default material. In fact, no matter what I did with the Jack.txt file, never could get the body to paint through using ApplyMaterialsList(). This very well could be due to something in the SharpReality binding, or a bug in the reading of the .txt file contents in Urho.dll.

Finally, also tried @Dave82 's suggestion for .SetMaterial, though in my exerience, the sharpreality binding tends to throw a lot of exceptions with .SetMaterial, so I don't like to use it.

But, this works with no exceptions or errors noted in my case:
```
modelObject.SetMaterial(0, Application.ResourceCache.GetMaterial("Materials/JackBody.xml"));
modelObject.SetMaterial(1, Application.ResourceCache.GetMaterial("Materials/JackHead.xml"));
``` 

And if creating a lot of models, for instance for the skeletal animation model, there the errors add quite a bit of delay lessening the user experience.

Also, @Egorbo could have made a Materials field rather than a Material field. That's a purely SharpReality issue though, unrelated.

```
namespace Urho
{
	partial class StaticModel
	{
		public Material Material
		{
			get { return GetMaterial(0); }
			set { SetMaterial(0, value); }
		}
	}

	partial class AnimatedModel
	{
		public Model Model
		{
			get { return base.Model; }
			set { this.SetModel(value, true); }
		}
	}
}
```

-------------------------

sandsound | 2019-01-18 12:35:29 UTC | #18

[quote="I3DB, post:17, topic:4832"]
Created the file in visual studio by adding a new file. Edited the contents also in visual studio. Probably something to do with encoding or line endings.
[/quote]

I remember having similar problems with Borlands Delphi back in the day, that's why I use a simple text-editor today.

Regarding an example, I threw something together, but haven't found a place to host it yet, besides... I'm almost certain that one of the actual devs can make something better :slight_smile:

-------------------------

Leith | 2019-01-19 05:21:35 UTC | #19

Ugh line endings!

I'm fairly new to Linux - porting my old Windows code to Linux is painful enough without having to deal with line endings.
I feel for you.

Surely we can find a common encoding that just works? Sigh.

-------------------------

Modanung | 2019-01-19 08:46:04 UTC | #20

[quote="Leith, post:19, topic:4832"]
Surely we can find a common encoding that just works? Sigh.
[/quote]
We did, Microsoft is just keeping up a tradition of ignoring standards.  

Best ignore _that_ for the sake of sanity. ;)

-------------------------

I3DB | 2019-01-19 12:03:28 UTC | #21

Ran this on a different platform with the file, and the error message is:
```
Could not find resource ï»¿Materials/JackBody.xml. 
```

Then recreated the file Jack.txt with vscode and all works perfectly. 

modelObject.ApplyMaterialList(); worked fine.

-------------------------

sandsound | 2019-01-19 13:52:09 UTC | #22

@I3DB
You should be able to disable [BOM](https://en.wikipedia.org/wiki/Byte_order_mark) in your editor

-------------------------

I3DB | 2019-01-19 14:08:18 UTC | #23

[quote="sandsound, post:22, topic:4832"]
You should be able to disable [BOM ](https://en.wikipedia.org/wiki/Byte_order_mark) in your editor
[/quote]

Found this https://vlasovstudio.com/fix-file-encoding/

But didn't see a way to do it directly in options in VS, but that's why vscode is handy.

-------------------------

Modanung | 2019-10-03 13:14:56 UTC | #24

2 posts were split to a new topic: [Problem applying textures to Jack](/t/problem-applying-textures-to-jack/5645)

-------------------------

