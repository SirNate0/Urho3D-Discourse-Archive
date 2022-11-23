Dave82 | 2017-01-02 01:05:14 UTC | #1

Hi everyone i've just finished my biped exporter for my game and i thought there may be other 3ds max users who will probably found this tool useful.
So basically what it does is searches the scene and exports the FIRST biped found in the scene hierarchy.

It was tested with 3ds max 9 but should work with any version... let me know if you found some issues...

NOTE : Make sure your biped and the skined mesh's biped have the axact same size otherwise the exported data will be invalid (but the result should be pretty funny :smiley: long hands , legs etc)

I had the same issue with irrlicht as the bone positions changing in different biped sizes.I solved this by exporting the distance between the root node and the first spine bone.
and calculate the scale between mesh and biped

[code]float scale = character.root.pos.distanceTo(character.spine1.pos) / biped.root.distanceTo(biped.spine)[/code]

and by multiplying the positions with this value corrected the issue , although i don't know how this should be done in Urho3D...

There's no option to add attachments so i just paste it here... copy , create new script, and run it

[code]

-- counts all (maximum) frames in the biped.

fn countFramesInBiped theBiped =
(
	retFrames = 0
	
	for c = 1 to 22 do
	(
		for l = 1 to 4 do
		(
			bod = biped.getNode theBiped c link:l
			if bod != undefined then
			(
				if bod.controller.keys.count > 0 then
				(
					lastKey = bod.controller.keys[bod.controller.keys.count]
						if lastKey.time > retFrames then retFrames = lastKey.time
				)
			)
		)
	)
	retFrames
)

-- returns bone count
fn countBonesInBiped theBiped =
(
	retBones = 0
	
	for c = 1 to 22 do
	(
		-- these are the com object so ignore it... we don't want to export them 3x times
		if c == 14 or c == 15 or c == 16 then continue

		for l = 1 to 4 do
		(
			bod = biped.getNode theBiped c link:l
			if bod != undefined then
			(
				retBones += 1
			)
		)
	)
	retBones
)


-- Generates standard names for bones.Replaces spaces with _ (Bip01 Head = Bip01_Head)
fn generateStandardName theString =
(
	nArr = filterString theString " "
	finString = ""
	for z = 1 to nArr.count do
	(
		finString += (nArr[z] + "_")
	)
	
	f = (substring finString 1 (finString.count-1))
	f
)


/*
byte[4]    Identifier "UANI"
cstring    Animation name
float      Length in seconds
uint       Number of tracks

  For each track:
  cstring    Track name (practically same as the bone name that should be driven)
  byte       Mask of included animation data. 1 = bone positions 2 = bone rotations 4 = bone scaling
  uint       Number of keyframes

    For each keyframe:
    float      Time position in seconds
    Vector3    Position (if included in data)
    Quaternion Rotation (if included in data)
    Vector3    Scale (if included in data)
*/


fn inf_ExportBipedAnim theFile animName=
(
	
	-- find biped in the scene
	for z = 1 to objects.count do
	(
		if objects[z].parent == undefined and classof objects[z] == Biped_Object then
		(
			-- We have our Biped COM object
			theBiped = objects[z] -- points to com object
			
			-- calculate frame count
			frameCount = countFramesInBiped theBiped

			magic = "UANI"
	
			for x = 1 to magic.count do
			(
				writeByte theFile (bit.charAsInt magic[x])
			)
					
			writeString theFile animName -- animation name
			
			-- Only keyframe per frame is supported... so the length is equal to keyframes
			-- keysframes starting from 0 and not 1  
			writeFloat theFile (frameCount + 1)
			
			
			boneCount = countBonesInBiped theBiped
			writeLong theFile boneCount	-- number of tracks
			
			print	
			print ("           Number of frames = " + frameCount as string)
			print ("           Number of bones = " + boneCount as string)
 
			-- export frames :
			for a = 1 to 22 do
			(
				-- these are all the com object so ignore them
				if a == 14 or a == 15 or a == 16 then continue
				
				for b = 1 to 4 do
				(
					bod = biped.getNode theBiped a link:b
					if bod != undefined then
					(
						-- we have a valid bone , so export its data
						-- write bone name 
						st = generateStandardName bod.name
						writeString theFile st
								
						print ("Exporting Bone : " + st) 
						
						writeByte theFile 3 -- mask : pos and rotate scale is ignored

						writeLong theFile (frameCount+1)	-- keyframes count
						
						for fr = 0 to frameCount do
						(
							at time (fr)
							(
								-- claculate local transform for each body
								transf = bod.transform
								if bod.parent != undefined then transf = bod.transform * (inverse bod.parent.transform)
								
								writeFloat theFile fr
								
								writeFloat theFile transf.pos.x
								writeFloat theFile transf.pos.z
								writeFloat theFile transf.pos.y
																
								writeFloat theFile transf.rotation.w
								writeFloat theFile transf.rotation.x
								writeFloat theFile transf.rotation.z
								writeFloat theFile transf.rotation.y

							)-- endof at time()
							
						)-- endof frame count loop
					
					) -- body != undefined

				)-- for b = 1 to 4	

			) -- for a = 1 to 22
			
		) -- if objects[z].parent == undefined and classof objects[z] == Biped_Object
		
	) -- scene objects loop
	
)



rollout unnamedRollout "Urho3D Biped anim exporter 0.1" width:482 height:160
(
	label lbl1 "Urho3D Biped animation exporter." pos:[155,9] width:166 height:19
	label lbl2 "The script will automatically export the FIRST biped found in the scene ! Make sure your animated biped and the skined mesh's biped are the exact same size !" pos:[11,44] width:426 height:34
	button btn_Export "Export" pos:[363,121] width:80 height:23
	on btn_Export pressed do
	(
		fname = getSaveFileName caption:"Save As.." types:"*.ani|*.ani"
		if fname != undefined then
		(
			fr = fopen fname "wb"
			inf_ExportBipedAnim fr (getFilenameFile fname)
			fclose fr
		)
	)
)

createDialog unnamedRollout 
[/code]

-------------------------

