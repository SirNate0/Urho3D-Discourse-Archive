slapin | 2017-01-02 01:15:39 UTC | #1

Hi, all!

For some months I was trying to make Urho physics constraints work. I was using ragdoll demo and trying to port it to my model
(basically makehuman export). I was not able make even single joint work. It looks like ragdoll demo was specially crafted
together the model to work. Is there any limitations in constraints?

As experiment I was trying to make spine work, so I added rigidbody to root bone and another one to spine05,
then I added conetwist constraint to spine05. I added bruteforce sequence which selected from a set of axis-aligned data
for axis and parentAxis and looped through all of them to see if any pair will produce at least remotely feasible
result - it did not. So I conclude there are some undocumented modelling requirements which I need to comply to make
constraints work.
basically I have the following questions unresolved by heavy digging.

1. what are axis and parentAxis exactly? They are somehow related to actual rotation, but I could not figure-out
the way they affect it. I could not predict any consequence of changing axes. First I expected them to be rotation axis set in
local coordinates of body the constraint is attached to. This happens to be not true, hten I tried if it was constraint body and other body local coordinates, but that also seems to be not true, as the result is always not right. Also, with conetwost constraint, brute forcing coordinates I was not able to make it look up or down - only left, right, front, back. So it looks
like some degree of freedom is lost.

2. Why Urho constraint binding doesn't use full Bullet settings, like conetwist have 3 separate limits and Urho uses only 2,
but duplicates one? There's on reason for that as there are unused API parameters left which could be used for that.
Also there are a few interesting things in Bulled which deserve having Urho API as raytrace vehicle, etc. Any plans for expansion?

3. Is there any reasonable bullet documentation or tutorial? I can't find anything useful, which would help me with
understanding. While it looks extremely stupid, at this stage it looks much easier to write own (much worse) implementation of constraints (or use some other library) than use Bullet (de-facto standard library for physics, I wonder how they have managed to understand it). So it looks like it is not ready for general use and/or not accessible enough to be useful.

-------------------------

Dave82 | 2017-01-02 01:15:39 UTC | #2

[quote="slapin"]Hi, all!

For some months I was trying to make Urho physics constraints work. I was using ragdoll demo and trying to port it to my model
(basically makehuman export). I was not able make even single joint work. It looks like ragdoll demo was specially crafted
together the model to work. Is there any limitations in constraints?

As experiment I was trying to make spine work, so I added rigidbody to root bone and another one to spine05,
then I added conetwist constraint to spine05. I added bruteforce sequence which selected from a set of axis-aligned data
for axis and parentAxis and looped through all of them to see if any pair will produce at least remotely feasible
result - it did not. So I conclude there are some undocumented modelling requirements which I need to comply to make
constraints work.
basically I have the following questions unresolved by heavy digging.

1. what are axis and parentAxis exactly? They are somehow related to actual rotation, but I could not figure-out
the way they affect it. I could not predict any consequence of changing axes. First I expected them to be rotation axis set in
local coordinates of body the constraint is attached to. This happens to be not true, hten I tried if it was constraint body and other body local coordinates, but that also seems to be not true, as the result is always not right. Also, with conetwost constraint, brute forcing coordinates I was not able to make it look up or down - only left, right, front, back. So it looks
like some degree of freedom is lost.

2. Why Urho constraint binding doesn't use full Bullet settings, like conetwist have 3 separate limits and Urho uses only 2,
but duplicates one? There's on reason for that as there are unused API parameters left which could be used for that.
Also there are a few interesting things in Bulled which deserve having Urho API as raytrace vehicle, etc. Any plans for expansion?

3. Is there any reasonable bullet documentation or tutorial? I can't find anything useful, which would help me with
understanding. While it looks extremely stupid, at this stage it looks much easier to write own (much worse) implementation of constraints (or use some other library) than use Bullet (de-facto standard library for physics, I wonder how they have managed to understand it). So it looks like it is not ready for general use and/or not accessible enough to be useful.[/quote]


I know exacly how you feel about this... I went through this headache and came to the 2 major conclusions >
1.Don't ever try to adjust the axes via code...It's impossible to make it to work.Since all these axes are local to the joints and some joints are even local to other joints it's impssible to see what are you doing by changing some values by code.
2.I'm not deeply familiar with Blender but your best bet is to find some ragdoll generator script for blender and write an exporter that exports the data for urho.I have my own ragdoll generator and exporter for 3ds max , which uses a one-click solution.It calculates the axes , limits and rigidbody sizes then i export it to a *.ragdoll file and read it in urho. Unfortunately this works only with max Biped so you have to find your own solution for blender...

-------------------------

slapin | 2017-01-02 01:15:40 UTC | #3

Well, Blender rigidbody setup for a ragdoll is very diffrent from what it is in Urho, so the tools for ragdolls
need to be implemented as Urho tool.
As for your script for Max - could you explain theory behind it? How do you convert 3DSMax data
to Urho data, and what is source setup? That will quite probably give me some idea.

-------------------------

Dave82 | 2017-01-02 02:11:20 UTC | #4

[quote="slapin"]Well, Blender rigidbody setup for a ragdoll is very diffrent from what it is in Urho, so the tools for ragdolls
need to be implemented as Urho tool.
As for your script for Max - could you explain theory behind it? How do you convert 3DSMax data
to Urho data, and what is source setup? That will quite probably give me some idea.[/quote]

3ds max comes with a built in ragdoll script that works strictly with max's biped system.Basically the UI is one "Create Ragdoll" button.If you press the button the script will loop through the biped and assign constraints to specific biped bones.All limits , axes , parent / chilren hierarchy is automatically set up.The script uses two type of constraints : Hinge (which is the same as in Urho) and a constraint called "Ragdoll" which is more or less equal to Urho's Conetwist.
After the script builds the ragdoll , it looks like this (Note the arrows that show the axes and the blue mesh shows the limits of the constraint.) :

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/7bc3f78843126bbf91c01d5bc83211245b198148.jpg[/img]

Nearly without any modifications it is ready to export.I wrote an exporter that loops through the scene and writes the constraints data to a *.ragdoll file. (BoneCount , boneSize , contrainttype , parent , child , etc) 
And i wrote a Ragdoll component which is basically the same as Urho's ragdoll component except it reads and builds the ragdoll from my *.ragdoll script instead from static code.
I had to make some adjustments before i export : Some axes must be rotated 90 degs in some direction to match Urho's space.(Note the "Urho fix" checkbox on the upper image)

So basically thats all.


here's the constraint export function :

[code]
-- 1 string child name
-- 1 string parent name
-- 1 int constraint type (0 hinge , 1 = conetwist)
-- 1 2dvector min rotation 
-- 1 2dvector max rotation
-- 1 quaternion child rotation
-- 1 quaternion parent rotation

fn exportConstraints theFile childName parentName =
(
	noConstraint = true
	
	for c = 1 to objects.count do
	(
		if classof objects[c] == Hinge or classof objects[c] == Ragdoll then
		(
			noConstraint = false
			if objects[c].parentBody.name == parentName and objects[c].childBody.name == childName then
			(
				pName = generateStandardName parentName
				cName = generateStandardName childName
				
				writeString theFile cName 
				writeString theFile pName
				
				if classof objects[c] == Hinge then
				(	
					writeLong theFile 0
					writeFloat theFile objects[c].limitMinAngle
					writeFloat theFile 0
					writeFloat theFile objects[c].limitMaxAngle
					writeFloat theFile 0
				)
				else -- It's a Conetwist (called Ragdoll in 3ds max)
				(
					writeLong theFile 1
					writeFloat theFile objects[c].coneLimitMinAngle
					writeFloat theFile objects[c].coneLimitMaxAngle
					writeFloat theFile objects[c].coneLimitMinAngle
					writeFloat theFile objects[c].coneLimitMaxAngle
				)

				childRotation = objects[c].childTransform.rotation
				parentRotation = objects[c].parentTransform.rotation
				
				writeFloat theFile childRotation.w 
				writeFloat theFile childRotation.x 
				writeFloat theFile childRotation.z 
				writeFloat theFile childRotation.y 
				
				writeFloat theFile parentRotation.w 
				writeFloat theFile parentRotation.x 
				writeFloat theFile parentRotation.z 
				writeFloat theFile parentRotation.y
				
				Print ("Export Constraint with parent : " + parentName + " -- and child : " + childName)
			)
			else
			(
				MessageBox ("Constraint with parent : " + parentName + " and child : " + childName + " does not exist")
			)
		)
	)
	if noConstraint then MessageBox ("No constraint found in the scene")
)[/code]

And here's the rigidBody export function 


[code]
-- 1 int collision type (0 = box 1= capsule)
-- 1 string bone name
-- 1 vector3 
fn writeRagdollBoneData theFile theName collisionType =
(
	writeLong theFile collisionType 
	
	body = findObjectByName theName
	bb = nodeGetboundingBox body body.transform	
	size = bb[2] - bb[1]
	size.x = abs(size.x)
	size.y = abs(size.y)
	size.z = abs(size.z)
	
	st = generateStandardName body.name
	writeString theFile st
        -- Special case to these bones.A little correction to make the collision jitterles.
	if st == "Bip01_L_Calf" or st == "Bip01_R_Calf" or st == "Bip01_L_Forearm" or st == "Bip01_R_Forearm" then  size.x *= 1.2

	writeFloat theFile size.x
	writeFloat theFile size.z
	writeFloat theFile size.y
)[/code]

and finally here's the ragdoll data exporter , using these two functions :

[code]

-- 1 int num affected bones
-- 1 int collision type (0 box , 1 = capsule)
-- 1 string = bone name
-- 1 vector = size

fn exportRagdoll theFile =
(
	writeLong theFile 11

	writeRagdollBoneData theFile "Bip01 Pelvis" 0
    writeRagdollBoneData theFile "Bip01 Spine1" 0
    writeRagdollBoneData theFile "Bip01 L Thigh" 1
    writeRagdollBoneData theFile "Bip01 R Thigh" 1
    writeRagdollBoneData theFile "Bip01 L Calf" 1
    writeRagdollBoneData theFile "Bip01 R Calf" 1
    writeRagdollBoneData theFile "Bip01 Head" 0
    writeRagdollBoneData theFile "Bip01 L UpperArm" 1
    writeRagdollBoneData theFile "Bip01 R UpperArm" 1
    writeRagdollBoneData theFile "Bip01 L Forearm" 1
    writeRagdollBoneData theFile "Bip01 R Forearm" 1
	
	-- export constraints :
	
	-- num constraints
	writeLong theFile 10
	
	exportConstraints theFile "Bip01 L Thigh" "Bip01 Pelvis" 
	exportConstraints theFile "Bip01 R Thigh" "Bip01 Pelvis" 
	
	exportConstraints theFile "Bip01 L Calf" "Bip01 L Thigh" 
	exportConstraints theFile "Bip01 R Calf" "Bip01 R Thigh" 
	
	exportConstraints theFile "Bip01 Spine1" "Bip01 Pelvis" 
	exportConstraints theFile "Bip01 Head" "Bip01 Spine1" 
	
	exportConstraints theFile "Bip01 L UpperArm" "Bip01 Spine1" 
	exportConstraints theFile "Bip01 R UpperArm" "Bip01 Spine1" 
	
	exportConstraints theFile "Bip01 L Forearm" "Bip01 L UpperArm" 
	exportConstraints theFile "Bip01 R Forearm" "Bip01 R UpperArm"
)
[/code]

-------------------------

slapin | 2017-03-08 12:06:17 UTC | #5

Sorry for late thanks, but this helped me a lot, so I made some ad-hoc scripts to create ragdoll
for Makehuman character. Thanks a lot for your help. The most complex problem is to find proper transform
from model space to bone space to setup constraints.

-------------------------

