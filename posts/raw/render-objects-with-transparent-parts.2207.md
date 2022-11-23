zedraken | 2017-01-02 01:13:55 UTC | #1

Hi all,

I keep discovering Urho3D (a really wonderful 3D engine) and now I try to render an object (a space ship) with some transparent parts (cockpit window pane), and I come here for an advice.
I have modelled the object in Blender made of a hull and a window pane (two different objects in Blender) which have different materials. For the window pane, I set the transparency factor to something close to 0. It renders fine within Blender.
On first approach, I exported both objects in one single "mdl" file.
Then, to render it in Urho3D, I create one single node under my main scene. To that node, I attach a static model, set the model file along with a "xml" material file. However, the material file applies to the entire object, the hull and the window pane.
The result is that the window pane is not transparent !

I change the way to address the problem. 

From Blender, I exported the hull to one object, and the window pane to another one. 
In Urho3D, I then create a single node under the scene. Then, under that node, I create two other nodes, first one is assigned the hull object, and the second node is assigned the window pane. 
By doing that, I am able to assign different "xml" material files, and for the window pane, I use something like that:

[code]
<material>
	<technique name="Techniques/DiffUnlitAlpha.xml" quality="0" />
	<parameter name="MatDiffColor" value="0.5 0.5 0.5 0.45" />
	<parameter name="MatSpecColor" value="0.5 0.1 0.1 40" />
	<parameter name="MatEmissiveColor" value="0.5 0.5 0.5 0.1" />
</material>
[/code]

The material file assigned to the hull object is rendered using a simple "diff.xml" technique.

The result is what I expected. The hull is opaque and the window pane is transparent with an alpha value of 0.45. This works fine.

However, I was wondering if there is another method which could avoid splitting a complete object into several smaller "mdl" objects with different materials ? Is it possible, under Urho3D, to load one single "mdl" file, and load several material files and have some materials assigned to some sub-objects by using their names for example ?

I hope my request is clear enough, but if you need more information, I would be very pleased to provide you with some code if it can help.

All my best regards !

Charles

-------------------------

1vanK | 2017-01-02 01:13:55 UTC | #2

Enable "Materials text list" in blender. Will be created file Models/MODEL_NAME.txt with materials list. In game you can use [i] object->ApplyMaterialList();[/i] for use this file. In editor this file loaded automatically (as long as I remember)

-------------------------

zedraken | 2017-01-02 01:13:56 UTC | #3

Hello 1vank, thanks for your advice.
I followed your instructions and it works fine !
Here is what I did in details?

From Blender, I exported all my meshes into a single [i]model.x[/i] file. It includes the hull and the window pane.

Using the [i]AssetImporter[/i], I convert the [i]model.x[/i] file into a [i]model.mdl[/i] file but I added the "-l" option. 

[code]
$ AssetImporter model model.x model.mdl -l
[/code]

This also creates a [i]model.txt[/i] file that looks like this :

[code]Materials/Fuselage.xml
Materials/Nickel.xml
Materials/Vitre.xml[/code]

In the [i]bin/Data/Materials[/i], the XML files shown above have been created. Then, I can modify the file called [i]Vitre.xml[/i] (sorry, file name is in french but it is the file that defines transparency for the window pane) to use the [i]DiffUnlitAlpha.xml[/i] technique for rendering window pane material (transparent).

In my source code, I create the static model with the following lines:

[code]
?
shipModel = shipNode->CreateComponent<StaticModel>();
shipModel->SetModel(cache->GetResource<Model>("Models/model.mdl"));
shipModel->ApplyMaterialList();
?
[/code]

The call to method [i]ApplyMaterialList()[/i] without parameter tells Urho3D to read materials definition from a file called [i]model.txt[/i] (it only replaces the [i].mdl[/i] extension by [i].txt[/i]), the one for which the content is displayed above.

And it works fine !

Thanks !

-------------------------

