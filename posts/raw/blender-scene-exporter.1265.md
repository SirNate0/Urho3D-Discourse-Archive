gabdab | 2017-01-02 01:06:29 UTC | #1

..Looks like it is working now  :astonished: 
Apply Scale and Rotation before running the script.
Name your physics enabled models something+phys inside blender, as phys is the keyword matched for rigid bodies in xml file .
Convert .fbx models with assetimporter (using a batch comand perhaps) and move materials textures and models in relative folders inside Data .
[Current Blender version (2.76) has broken .fbx exporter , use 2.73 }
[code]
import bpy
import mathutils
import math
import time




path = bpy.path.abspath('//')  
filepath=str(path +"livello.xml")
testPath=''



out = open(filepath, 'w')
out.write("<?xml version=\"1.0\"?>\n<scene id=\"1\">\n	<attribute name=\"Name\" value=\"\" />\n	<attribute name=\"Time Scale\" value=\"1\" />\n	<attribute name=\"Smoothing Constant\" value=\"50\" />\n	<attribute name=\"Snap Threshold\" value=\"5\" />\n	<attribute name=\"Elapsed Time\" value=\"0\" />\n	<attribute name=\"Next Replicated Node ID\" value=\"1\" />\n	<attribute name=\"Next Replicated Component ID\" value=\"4\" />\n	<attribute name=\"Next Local Node ID\" value=\"1677723000000\" />\n	<attribute name=\"Next Local Component ID\" value=\"1677723900000\" />\n	<attribute name=\"Variables\" />\n	<attribute name=\"Variable Names\" value=\"\" />\n	<component type=\"Octree\" id=\"1\" />\n	<component type=\"DebugRenderer\" id=\"2\" />\n	<component type=\"PhysicsWorld\" id=\"3\" />\n")
# loop through all the objects in the scene
scene = bpy.context.scene

obs=[]
oldObDataName=[]
#xml export_scene
nodeid=16777216
componentid=16777218
NextLocalNodeID=nodeid+1
NextLocalComponentID=componentid+1
rad=180.00/3.1415
physObj=''#indicates if object is rigidbody




   	     	
for ob in bpy.context.selected_objects:
    obs.append(ob)
    ob.select = False
for ob in obs:
	if ob.type == 'MESH':
		ob.select = True
		itDataName = 0
		for it in oldObDataName:
			if(ob.data.name==it):
				itDataName = 1
				break
            		
		if itDataName == 0:
			wLoc = ob.location.copy()
			wRot = ob.rotation_euler.copy()
			wScal= ob.scale.copy()
			ob.rotation_euler=(0,0,0)
			ob.location=(0,0,0)
			ob.scale = (1,1,1)    
			bpy.ops.export_scene.fbx(use_selection=1,filepath=str(path) +ob.data.name + '.fbx')
			print (str(path) +str(testPath)+"/"+ob.data.name + '.fbx')
			oldObDataName.append(ob.data.name)
			ob.location = wLoc
			ob.rotation_euler=wRot
			ob.scale=wScal
		ob.select = False	
    

    
for ob in obs:

    scene.objects.active = ob
    ob.select = True
    

    bpy.context.scene.objects.active = ob 

    obName = ob.name.replace(".", "_")
    obDataName = ob.data.name 
    print (obName)		
    # make sure that we only export meshes
    if ob.type == 'MESH':
 
            rots=''
            locs=''
            scales=''
            wLoc = ob.location.copy()
            wRot = ob.rotation_euler.copy()
            wScal= ob.scale.copy()

            locs += "%.2f" %float(wLoc[0])+' '
            locs += "%.2f" %float(wLoc[2]) +' '
            locs += "%.2f" %float(wLoc[1])+' '  


            wRot[0]=float(-wRot[0])
            arrTmp=float(-wRot[1])
            wRot[1]=float(-wRot[2])
            wRot[2]=arrTmp
            wRot[2]=float(wRot[2])
            eArr=mathutils.Euler(wRot)
            print(eArr)
            qArr = eArr.to_quaternion()
            rots += str("%.2f" %(qArr[0]))+' '
            rots += str("%.2f" %(qArr[1]))+' '
            rots += str("%.2f" %(qArr[2]))+' '
            rots += str("%.2f" %(qArr[3])) 
            

            scales += "%.2f" %float(wScal[0])+' '
            scales += "%.2f" %float(wScal[2])+' '
            scales += "%.2f" %float(wScal[1])  


            if obName.find('phys')!=-1:
            	physObj = "<component type=\"CollisionShape\" id=\"" + str(nodeid)+"\">\n<attribute name=\"Shape Type\" value=\"TriangleMesh\" />\n<attribute name=\"Model\" value=\""+"Model;Models/"+str(testPath)+"/"+ob.data.name+".mdl\" />\n</component>\n<component type=\"RigidBody\" id=\"" + str(nodeid+1)+"\">\n<attribute name=\"Physics Position\" value=\"" + locs + "\" />\n</component>"
            	nodeid +=2
            else:
            	physObj=''
            	
            out.write(	"<node id=\""
	+str(nodeid)+
	"\">\n<attribute name=\"Is Enabled\" value=\"true\" />\n<attribute name=\"Name\" value=\""
	+obName+
	"\" />\n<attribute name=\"Position\" value=\""
+locs+
	"\" />\n<attribute name=\"Rotation\" value=\""
+rots+
	"\" />\n<attribute name=\"Scale\" value=\""
+scales+
	"\" />\n<attribute name=\"Variables\" />\n<component type=\"StaticModel\" id=\""
+str(componentid)+
	"\" >\n<attribute name=\"Model\" value=\"Model;Models"
+str(testPath)+"/"+ob.data.name+
	".mdl\" />\n")
            out.write(	"<attribute name=\"Material\" value=\"Material;Materials"+str(testPath)+"/")
            if(len(ob.material_slots)!=0):
            	i=0
            	for mt in range(len(ob.material_slots)-1,-1,-1):
            		out.write(	ob.material_slots[mt].name+
		".xml")
            		if(i==(len(ob.material_slots))-1):
            			out.write("\" />\n")
            		else:
            			out.write(";Materials/"+str(testPath))
            		i += 1
            else:
            	out.write("noMaterial.xml\" />\n")
            	
            out.write("</component>\n"+
		physObj+
	"</node>\n")
            componentid += 1
            nodeid += 1
            
            '''
            #as a reference for uv texture exporting as opposed to materials
            me = ob.data
            bool1=False
            if me.uv_textures.active is not None:
                for tf in me.uv_textures.active.data:
                    if tf.image:
                        img = tf.image.name
                        if(bool1==False):
                            print("uv texture: ",img)
                            ##out.write(obName+"->setTexture(\"test_env_6_4_1/textures/"+img+"\");\n")
                            bool1=True
                        
            print(obName)
            print(ob.material_slots[0].name)
            for mat_slot in ob.material_slots:
            	print("matslot %s" %mat_slot.name)
            	for mtex_slot in mat_slot.material.texture_slots:
                    if mtex_slot:
                        # dump(mtex_slot)
                        #print("\t%s" % mtex_slot)
                        if hasattr(mtex_slot.texture , 'image'):
                            print("\t\t%s" % mtex_slot.texture.image.filepath)
                            #out.write(obName+"->setTexture(\""+mtex_slot.texture.image.filepath[2:]+"\");\n")														          
            '''
            


            

    # deselect the object and move on to another if any more are left
    ob.select = False
for ob in obs:
	ob.select = True
	


out.write("</scene>")
NextLocalNodeID=nodeid+1
NextLocalComponentID=componentid+1

out.close()
[/code]
[i]Thou shalt not miss the video :[/i]
[url]https://www.youtube.com/watch?v=O3w0ALouv3E[/url]

-------------------------

Enhex | 2017-01-02 01:06:30 UTC | #2

Have you seen [github.com/reattiva/Urho3D-Blender](https://github.com/reattiva/Urho3D-Blender) ?

-------------------------

gabdab | 2017-01-02 01:06:30 UTC | #3

[quote="Enhex"]Have you seen [github.com/reattiva/Urho3D-Blender](https://github.com/reattiva/Urho3D-Blender) ?[/quote]
Yes thanks ..

-------------------------

rasteron | 2017-01-02 01:06:35 UTC | #4

Hey gabdab, 

I see that you have removed your original post and replaced it with a fail video compilation instead. I would recommend though, that you post your basic exporter code back again. There is nothing wrong and no shame with that as there is not a single solution to a problem, at least in coding.

Obviously you might have not seen reattiva's blender exporter before you came up with that code, so who cares? What you did is a positive thing there and it is good for an open source community. So, I would not mind leaving it there.  :slight_smile:

Although the blender exporter is the best one for the engine to date, everyone has a different pipeline and method of doing things. Heck, I'm using the AssetImporter commandline tool and it works great for me. :wink:

cheers.

-------------------------

gabdab | 2017-01-02 01:06:35 UTC | #5

[EDIT: Working full script is in first post ]
:astonished: 
I do appreciate your caring , very polite and friendly .
Thanks , makes me feel at home .
I gladly submit the 'failed' attempt to a blender scene exporter (wrong rotations, now commented) as a basic exporter for models but not linked duplicates ( objects that share same mesh , but have different rotations scale position values than original mesh ).
If someone can correct rotations error on the fly (quaternions) please do ..
[code]
import bpy
import mathutils
import math


path = bpy.path.abspath('//')  
filepath=str(path + "livello.xml")
out = open(filepath, 'w')
out.write("<?xml version=\"1.0\"?>\n<scene id=\"1\">\n	<attribute name=\"Name\" value=\"\" />\n	<attribute name=\"Time Scale\" value=\"1\" />\n	<attribute name=\"Smoothing Constant\" value=\"50\" />\n	<attribute name=\"Snap Threshold\" value=\"5\" />\n	<attribute name=\"Elapsed Time\" value=\"0\" />\n	<attribute name=\"Next Replicated Node ID\" value=\"1\" />\n	<attribute name=\"Next Replicated Component ID\" value=\"4\" />\n	<attribute name=\"Next Local Node ID\" value=\"1677723000000\" />\n	<attribute name=\"Next Local Component ID\" value=\"1677723900000\" />\n	<attribute name=\"Variables\" />\n	<attribute name=\"Variable Names\" value=\"\" />\n	<component type=\"Octree\" id=\"1\" />\n	<component type=\"DebugRenderer\" id=\"2\" />\n	<component type=\"PhysicsWorld\" id=\"3\" />\n")
# loop through all the objects in the scene
scene = bpy.context.scene

obs=[]
oldObDataName=[]
#xml export_scene
nodeid=16777216
componentid=16777218
NextLocalNodeID=nodeid+1
NextLocalComponentID=componentid+1
rad=180.00/3.1415
physObj=''#indicates if object is rigidbody
fileCont=[]#loadfile lines container
saveFilepath=str(path + "scene.txt")



   	     	
for ob in bpy.context.selected_objects:
    obs.append(ob)
    ob.select = False
for ob in obs:
	ob.select = True
	itDataName = 0
	for it in oldObDataName:
		if(ob.data.name==it):
			itDataName = 1
			break
            		
	if itDataName == 0:
		wLoc = ob.location.copy()
		wRot = ob.rotation_euler.copy()
		wScal= ob.scale.copy()
#		ob.rotation_euler=(0,0,0)
#		ob.location=(0,0,0)
#		ob.scale = (1,1,1)    
		bpy.ops.export_scene.fbx(use_selection=1,filepath=str(path +ob.data.name + '.fbx'))
		oldObDataName.append(ob.data.name)
		ob.location = wLoc
		ob.rotation_euler=wRot
		ob.scale=wScal
	ob.select = False	
    
    
for ob in obs:
#scene.objects:
    # make the current object active and select it
    scene.objects.active = ob
    ob.select = True
    
    bpy.context.scene.objects.active = ob # set object as active object


    obName = ob.name.replace(".", "_")
    obDataName = ob.data.name #.replace(".","_")
    print (obName)		
    # make sure that we only export meshes
    if ob.type == 'MESH':
 
            rots=''
            locs=''
            scales=''
            wLoc = ob.location.copy()
            wRot = ob.rotation_euler.copy()
            wScal= ob.scale.copy()

            locs += "%.2f" %float(wLoc[0])+' '
            locs += "%.2f" %float(wLoc[2]) +' '
            locs += "%.2f" %float(wLoc[1])+' '  


            wRot[0]=float(wRot[0])
            arrTmp=float(wRot[1])
            wRot[1]=float(wRot[2])
            wRot[2]=arrTmp
            wRot[2]=float(wRot[2])
            eArr=mathutils.Euler(wRot)
            print(eArr)
            qArr = eArr.to_quaternion()
            rots += str("%.2f" %(qArr[0]))+' '
            rots += str("%.2f" %(qArr[1]))+' '
            rots += str("%.2f" %(qArr[2]))+' '
            rots += str("%.2f" %(qArr[3])) 
            

            scales += "%.2f" %float(wScal[0])+' '
            scales += "%.2f" %float(wScal[2])+' '
            scales += "%.2f" %float(wScal[1])  


            if obName.find('phys')!=-1:
            	physObj = "<component type=\"CollisionShape\" id=\"" + str(nodeid)+"\">\n<attribute name=\"Shape Type\" value=\"TriangleMesh\" />\n<attribute name=\"Model\" value=\""+"Model;Models/"+ob.data.name+".mdl\" />\n</component>\n<component type=\"RigidBody\" id=\"" + str(nodeid+1)+"\">\n<attribute name=\"Physics Position\" value=\"" + locs + "\" />\n</component>"
            	nodeid +=2
            else:
            	physObj=''
            	
            out.write(	"<node id=\""
	+str(nodeid)+
	"\">\n<attribute name=\"Is Enabled\" value=\"true\" />\n<attribute name=\"Name\" value=\""
	+obName+
	"\" />\n<!--<attribute name=\"Position\" value=\""
+locs+
	"\" />-->\n<!--<attribute name=\"Rotation\" value=\""
+rots+
	"\" />-->\n<!--<attribute name=\"Scale\" value=\""
+scales+
	"\" />-->\n<attribute name=\"Variables\" />\n<component type=\"StaticModel\" id=\""
+str(componentid)+
	"\" >\n<attribute name=\"Model\" value=\"Model;Models/"
+ob.data.name+
	".mdl\" />\n<attribute name=\"Material\" value=\"Material;Materials/"
 +ob.material_slots[0].name+
	".xml\" />\n"
+
		"</component>\n"+
		physObj+
	"</node>\n")
            componentid += 1
            nodeid += 1

            '''
            #included as a reference
            me = ob.data
            bool1=False
            if me.uv_textures.active is not None:
                for tf in me.uv_textures.active.data:
                    if tf.image:
                        img = tf.image.name
                        if(bool1==False):
                            print("uv texture: ",img)
                            ##out.write(obName+"->setTexture(\"test_env_6_4_1/textures/"+img+"\");\n")
                            bool1=True
                        
            print(obName)
            print(ob.material_slots[0].name)
            for mat_slot in ob.material_slots:
            	print("matslot %s" %mat_slot.name)
            	for mtex_slot in mat_slot.material.texture_slots:
                    if mtex_slot:
                        # dump(mtex_slot)
                        #print("\t%s" % mtex_slot)
                        if hasattr(mtex_slot.texture , 'image'):
                            print("\t\t%s" % mtex_slot.texture.image.filepath)
                            #out.write(obName+"->setTexture(\""+mtex_slot.texture.image.filepath[2:]+"\");\n")														          
            '''

            



    ob.select = False
for ob in obs:
	ob.select = True
	

out.write("</scene>")
NextLocalNodeID=nodeid+1
NextLocalComponentID=componentid+1
out.close()
[/code]

-------------------------

rasteron | 2017-01-02 01:06:37 UTC | #6

That's great and hey, appreciate it. For me I feel it's the right thing to do and this encourages new members to learn and share their work or experience. :wink:

Btw, post it again as the first post and not as a reply. (you can remove the failed video compilation now  :smiley: )

-------------------------

