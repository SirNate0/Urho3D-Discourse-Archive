horvatha4 | 2017-01-02 01:13:24 UTC | #1

Hi!
I generate Node and Terrain from code and then save it as XML, I get this:
[code]
...
	<component type="Terrain" id="2">
		<attribute name="Is Enabled" value="false" />
		<attribute name="Vertex Spacing" value="90 256 90" />
		<attribute name="Patch Size" value="8" />
		<attribute name="Is Occluder" value="true" />
	</component>
</node>
[/code]

But if I reproduce a terrain in the Urho Editor I get this:
[code]
...
	<component type="Terrain" id="4">
		<attribute name="Height Map" value="Image;Terrain/N489E0210_geo.png" />
		<attribute name="Material" value="Material;Materials/Terrain.xml" />
		<attribute name="Vertex Spacing" value="90 256 90" />
		<attribute name="Patch Size" value="8" />
	</component>
</node>
[/code]

"Height Map" and "Material" attributes is not saved from C++ or they are not valid attributes?
Naturally, what I saved from C++, is appear as an empty Node in the Editor.

Arpi

-------------------------

cadaver | 2017-01-02 01:13:24 UTC | #2

How are you setting the height map & material resources in C++ code? Are they valid (and named) resources in the resource cache at the time of saving?

-------------------------

horvatha4 | 2017-01-02 01:13:24 UTC | #3

They are unnamed.
Here is my code:
[code]
			Node* terrainNode_ = scene_->CreateChild();
			Terrain *terrain_ = terrainNode_->CreateComponent<Terrain>();
			terrain_->SetOccluder(true);
			terrain_->SetSmoothing(false);
			terrain_->SetSpacing(Vector3(ONE_MAPCELL_LENGHT, 256.0f, ONE_MAPCELL_LENGHT));
			terrain_->SetPatchSize(TERRAIN_PATCH_SIZE);
			for (...
			{
				for (...
				{
					SharedPtr<Image> terrainGeoSubImg = context_->CreateObject<Image>(), 
						terrainTexSubImg = context_->CreateObject<Image>();
					terrainGeoSubImg->SetSize(121, 121, 3);
					terrainTexSubImg->SetSize(121, 121, 3);
					for (int j = 0; j <= 120; j++)
					{
						for (int i = 0; i <= 120; i++)
						{
							int16_t r = origSRTM3[k * 120 + i][l * 120 + j], g = r;
							r = r & 0x00ff; g = g >> 8 & 0x00ff;// STRM3 BigEndian
							terrainGeoSubImg->SetPixel(i, j, Color(r / 255.0f, g / 255.0f, 0));
...
									terrainTexSubImg->SetPixel(i, j, landTopographicColors_[z]);
...
									terrainTexSubImg->SetPixel(i, j, seaTopographicColors_[z]);
								}
							}
						}
					}
					terrain_->SetHeightMap(terrainGeoSubImg);
					SharedPtr<Material> mat = context_->CreateObject<Material>();
					mat->SetTechnique(0, cache->GetTempResource<Technique>("Techniques/Diff.xml"));
					SharedPtr<Texture2D> tex2d = context_->CreateObject<Texture2D>();
					tex2d->SetData(terrainTexSubImg);
					mat->SetTexture(TU_DIFFUSE, tex2d);
					terrain_->SetMaterial(mat);
...
					File *file = new File(context_, tmp_filename + ".xml", FILE_WRITE);
					terrainNode_->SaveXML(*file);
					file->Flush();
					file->Close();
					terrainGeoSubImg->SavePNG(tmp_filename + "_geo.png");
					terrainTexSubImg->SavePNG(tmp_filename + "_tex.png");
...
[/code]

What is wrong?

-------------------------

