lexx | 2017-06-13 06:34:33 UTC | #1

I might be use AssetImporter wrong but there is
> -p <path>   Set path for scene resources. Default is output file path

so I write
> AssetImporter scene myscene1.fbx  myscene.scene -p Scene1

Ok, there will be myscene.scene,  Scene1/Materials/,  Scene1/Models/ and Scene1/Textures/.
Good.
But in myscene.scene, there are "links" to Materials/, Models/ and Textures/  (not Scene1/Marerials, Scene1/Models, Scene1/Textures), so scene loading failed.
.

-------------------------

lexx | 2017-06-13 12:02:31 UTC | #2

Well, modified AssetImporter.cpp a little, seems to work.
.material files doesnt point to Scene1/Textures/ (only Textures/  but thats fine).

Line 1701 (added resourcePath_ +  ):
`String modelName = resourcePath_ + (useSubdirs_ ? "Models/" : "") + GetFileNameAndExtension(model.outName_);`

Line 2357 (added resourcePath_ +  ):
`return resourcePath_ + (useSubdirs_ ? "Materials/" : "") + matName + ".xml";`

-------------------------

