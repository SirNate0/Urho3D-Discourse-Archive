vivienneanthony | 2017-01-02 01:04:12 UTC | #1

Hi

Is this valid ? In the Manager class headerI created a SharedPtr <Scene). I attempted clearing it then directly pointing the pointer to the pass pointer but I don't think that is working.

Viv


[code]/// Set Scene
int Manager::SetScene(SharedPtr<Scene> scene)
{

    /// point
    scene_ = new Scene(context_);
    
    scene_ = scene;

    /// Node
    Node * parentnode = scene_ -> GetParent();

    String  nodename = parentnode ->GetName();
    
    cout << nodename.CString() <<endl;
}
[/code]

-------------------------

JTippetts | 2017-01-02 01:04:12 UTC | #2

[quote="vivienneanthony"]
int Manager::SetScene(SharedPtr<Scene> scene)
{

    /// point
    scene_ = new Scene(context_);
[/quote]
The above creates a new scene and stores it in the pointer scene_
[quote]
    
    scene_ = scene;
[/quote]
The above overwrites the newly created pointer above with the value of whatever is in scene, passed to the method. If scene is an empty pointer, scene_ is now empty. If scene is an existing Scene, then scene_ is now pointing to that existing scene. The newly created scene_ allocated above is gone.
[quote]

    /// Node
    Node * parentnode = scene_ -> GetParent();
[/quote]

The above tries to get the parent of scene_, but a Scene is a root-level Node be default. A newly constructed scene is going to have a null parent.

[quote]
    String  nodename = parentnode ->GetName();
[/quote]
The above tries to dereference the null parent of the scene to obtain its name. Dereferencing a null pointer is, of course, an error.

I honestly can't even begin to imagine what it is you are trying to accomplish here, but I suspect that 24+ hours without sleep might be a part of the reason for that.

-------------------------

vivienneanthony | 2017-01-02 01:04:12 UTC | #3

Lol. yea. It's late and I'm tired.

After making that note. It works. I think it's bed time for me.

Ultimately.  I want to recursively look through the Scene and save all nodes not generated including the components(Manual(Editor or in-client addition) or Automatic (NPC'S, spawn points, etc)). Then also be able to do the opposite like load.

-------------------------

cadaver | 2017-01-02 01:04:12 UTC | #4

[quote="JTippetts"]A newly constructed scene is going to have a null parent.[/quote]
I would add that in normal use a scene is always going to have a null parent. Or, Urho will not specifically stop you from adding a scene as a child to another scene or another node, but it does not make sense and you can expect errors (eg. node/component ID allocation clashes) or even outright crashes to result from that.

-------------------------

vivienneanthony | 2017-01-02 01:04:14 UTC | #5

The new code is this. Any recommendations??
[code]

/// Main Save scene
int Manager::SaveScene(int mode)
{

    /// Check if scene exist

    if(scene_==NULL)
    {
        return 1;
    }

    /// point
    unsigned int childrencount=scene_->GetNumChildren();
    cout <<  childrencount << endl;

    children_ = scene_->GetChildren();

    /// loop each child
    for (Vector<SharedPtr<Node> >::Iterator i = children_.Begin(); i != children_.End(); ++i)
    {
        /// Create a new child instance
        Node* childnode = *i;

        /// Get node infomration, check for children, and check components
        if(childnode->GetName().Find("Generated",0,false)==String::NPOS)
        {
            cout << "Node :" << childnode->GetName().CString() <<endl;

            /// GET ALL NODE INFORMATION

            if(childnode->GetNumChildren())
            {
                SaveSceneNode(childnode);
            }
            else
            {
                SaveSceneNodeComponents(childnode);
            }

        }

    }
}

/// Recursive
int Manager::SaveSceneNode(Node * node)
{
    /// Define a temporary pointer
    Vector<SharedPtr<Node> > subchildren_;

    /// Get children node
    subchildren_ = node->GetChildren();

    ///IF no child exist get all components
    ///ELSE
    for (Vector<SharedPtr<Node> >::Iterator i = subchildren_.Begin(); i != subchildren_.End(); ++i)
    {
        /// Create a new child instance
        Node* childnode = *i;

        /// Get node infomration, check for children, and check components
        if(childnode->GetName().Find("Generated",0,false)==String::NPOS)
        {
            cout << "Node :" << childnode->GetName().CString() <<endl;

            // set virtual const
            const Vector<AttributeInfo>* attributes = childnode->GetAttributes();

            /// loop through attributes
            for (Vector<AttributeInfo>::ConstIterator i = attributes->Begin(); i != attributes->End(); ++i)
            {
                /// output info
                cout << i -> name_.CString() << " type " << i -> defaultValue_. GetTypeName ().CString() <<" value" << i -> defaultValue_.ToString().CString()<< endl;
            }


            if(childnode->GetNumChildren())
            {
                SaveSceneNode(childnode);
            }
            else
            {
                SaveSceneNodeComponents(childnode);
            }
        }
    }
}
int Manager::SaveSceneNodeComponents(Node *node)
{
    /// Define temporary pointer for components
    Vector< SharedPtr< Component > > 	subcomponents_;

    /// If node has no components
    if(node->	GetNumComponents ()==0)
    {
        cout << " Node has no components" << endl;

        return 1;
    }

    /// Get children node
    subcomponents_ = node->GetComponents();

    /// Loop through components
    for (Vector<SharedPtr<Component> >::Iterator i = subcomponents_.Begin(); i != subcomponents_.End(); ++i)
    {
        Component * subcomponent = *i;

        cout << subcomponent->GetTypeName().CString() <<endl;


        /// READ EACH COMPONENT AND GET ATTRIBUTES
        if(subcomponent->GetNumAttributes ())
        {
            /// set virtual const
            const Vector<AttributeInfo>* attributes = subcomponent->GetAttributes();

            /// loop through attributes
            for (Vector<AttributeInfo>::ConstIterator i = attributes->Begin(); i != attributes->End(); ++i)
            {
                /// output info
                cout << i -> name_.CString() << " type " << i -> defaultValue_. GetTypeName ().CString() <<" value" << i -> defaultValue_.ToString().CString()<< endl;
            }

        }
    }


    return 1;
}[/code]

The result is okay but I think I have to differentiate a subchild because the output looks like one long list
[code]
Node :Mushroom
Is Enabled type Bool valuetrue
Name type String value
Position type Vector3 value0 0 0
Rotation type Quaternion value1 0 0 0
Scale type Vector3 value1 1 1
Variables type VariantMap value
Network Position type Vector3 value0 0 0
Network Rotation type Buffer value
Network Parent Node type Buffer value
StaticModel
Is Enabled type Bool valuetrue
Model type ResourceRef value
Material type ResourceRefList value
Is Occluder type Bool valuefalse
Can Be Occluded type Bool valuetrue
Cast Shadows type Bool valuefalse
Draw Distance type Float value0
Shadow Distance type Float value0
LOD Bias type Float value1
Max Lights type Int value0
View Mask type Int value-1
Light Mask type Int value-1
Shadow Mask type Int value-1
Zone Mask type Int value-1
Occlusion LOD Level type Int value-1
GameObject
Game Lifetime type Float value-1


Node :Character
Is Enabled type Bool valuetrue
Name type String value
Position type Vector3 value0 0 0
Rotation type Quaternion value1 0 0 0
Scale type Vector3 value1 1 1
Variables type VariantMap value
Network Position type Vector3 value0 0 0
Network Rotation type Buffer value
Network Parent Node type Buffer value
SubNode :hips
SubNode :thigh.L
SubNode :shin.L
SubNode :foot.L
SubNode :toe.L
 Node has no components
SubNode :thigh.R
SubNode :shin.R
SubNode :foot.R
SubNode :toe.R
 Node has no components
SubNode :spine
SubNode :chest
SubNode :clavicle.R
SubNode :upper_arm.R
SubNode :forearm.R
SubNode :hand.R
SubNode :thumb.02.R
SubNode :thumb.03.R
 Node has no components
SubNode :f_ring.01.R
 Node has no components
SubNode :f_index.01.R
 Node has no components
SubNode :clavicle.L
SubNode :upper_arm.L
SubNode :forearm.L
SubNode :hand.L
SubNode :thumb.02.L
SubNode :thumb.03.L
 Node has no components
SubNode :f_ring.01.L
 Node has no components
SubNode :f_index.01.L
 Node has no components
SubNode :neck
SubNode :head
SubNode :jaw
 Node has no components
SubNode :eye.R
 Node has no components
SubNode :eye.L
 Node has no components
SubNode :CameraFirstPerson
Camera
Is Enabled type Bool valuetrue
Near Clip type Float value0.1
Far Clip type Float value1000
FOV type Float value45
Aspect Ratio type Float value1
Fill Mode type Int value0
Auto Aspect Ratio type Bool valuetrue
Orthographic type Bool valuefalse
Orthographic Size type Float value20
Zoom type Float value1
LOD Bias type Float value1
View Mask type Int value-1
View Override Flags type Int value0
Projection Offset type Vector2 value0 0
Reflection Plane type Vector4 value0 1 0 0
Clip Plane type Vector4 value0 1 0 0
Use Reflection type Bool valuefalse
Use Clipping type Bool valuefalse
SubNode :CrossBox
StaticModel
Is Enabled type Bool valuetrue
Model type ResourceRef value
Material type ResourceRefList value
Is Occluder type Bool valuefalse
Can Be Occluded type Bool valuetrue
Cast Shadows type Bool valuefalse
Draw Distance type Float value0
Shadow Distance type Float value0
LOD Bias type Float value1
Max Lights type Int value0
View Mask type Int value-1
Light Mask type Int value-1
Shadow Mask type Int value-1
Zone Mask type Int value-1
Occlusion LOD Level type Int value-1


Node :Camera
Is Enabled type Bool valuetrue
Name type String value
Position type Vector3 value0 0 0
Rotation type Quaternion value1 0 0 0
Scale type Vector3 value1 1 1
Variables type VariantMap value
Network Position type Vector3 value0 0 0
Network Rotation type Buffer value
Network Parent Node type Buffer value
Camera
Is Enabled type Bool valuetrue
Near Clip type Float value0.1
Far Clip type Float value1000
FOV type Float value45
Aspect Ratio type Float value1
Fill Mode type Int value0
Auto Aspect Ratio type Bool valuetrue
Orthographic type Bool valuefalse
Orthographic Size type Float value20
Zoom type Float value1
LOD Bias type Float value1
View Mask type Int value-1
View Override Flags type Int value0
Projection Offset type Vector2 value0 0
Reflection Plane type Vector4 value0 1 0 0
Clip Plane type Vector4 value0 1 0 0
Use Reflection type Bool valuefalse
Use Clipping type Bool valuefalse
GameObject
Game Lifetime type Float value-1
[/code]

-------------------------

JTippetts | 2017-01-02 01:04:14 UTC | #6

What is wring with using Scene::SaveXML()?

-------------------------

vivienneanthony | 2017-01-02 01:04:15 UTC | #7

[quote="JTippetts"]What is wring with using Scene::SaveXML()?[/quote]

I have to manually go through the node structure and not save Generated and a few other types of components(like camera and others that will throw off everything). I really don't want to modify the base Scene.cpp code to do so.

I want output that can be imported into the Editor.as or another Editor. I put the latest semi-close code on github.

-------------------------

vivienneanthony | 2017-01-02 01:04:15 UTC | #8

I made some code to try to replace the Export Node or SaveXML parsing through a scene. So far the output is as follows.

Any help is appreciated? I should be able to loadXML with the output since Editor.as is written in Angelscript directly linking the Save XML(Differiental) will not happen soon unless a c/c++ editor becomes available.

Source code in [github.com/vivienneanthony/Exis ... enceClient](https://github.com/vivienneanthony/Existence/tree/development/Source/ExistenceApps/ExistenceClient) as manager.cpp and manager.cpp

[code]/// Main Save scene
int Manager::SaveScene(int mode)
{

    /// Check if scene exist

    if(scene_==NULL)
    {
        return 1;
    }


    String savesceneexport;

    ResourceCache * cache = GetSubsystem<ResourceCache>();
    FileSystem * filesystem = GetSubsystem<FileSystem>();

    savesceneexport.Append(filesystem->GetProgramDir().CString());
    savesceneexport.Append("CoreData/");
    savesceneexport.Append("testing.xml");

    File saveFile(context_, savesceneexport.CString(), FILE_WRITE);

    /// Check if the account file information exist
    if(!filesystem->FileExists(savesceneexport.CString()))
    {
        //cout << "\r\nAccount file ("<< savesceneexport.CString() << ") does not exist.";
    }

    XMLFile * savesceneexportxml= new XMLFile(context_);

    XMLElement configElem = savesceneexportxml-> CreateRoot("node");

    /// point
    unsigned int childrencount=scene_->GetNumChildren();
    cout <<  childrencount << endl;

    children_ = scene_->GetChildren();

    /// loop each child
    for (Vector<SharedPtr<Node> >::Iterator i = children_.Begin(); i != children_.End(); ++i)
    {
        /// Create a new child instance
        Node* childnode = *i;

        /// Get node infomration, check for children, and check components
        if((childnode->GetName().Find("Generated",0,false)==String::NPOS)
            &&(childnode->GetName().Find("Character",0,false)==String::NPOS)
            &&(childnode->GetName().Find("Camera",0,false)==String::NPOS))
        {
            XMLElement NodeElement = configElem. CreateChild ("node");

            // set virtual const
            const Vector<AttributeInfo>* attributes = childnode->GetAttributes();

            /// loop through attributes
            for (Vector<AttributeInfo>::ConstIterator i = attributes->Begin(); i != attributes->End(); ++i)
            {
                XMLElement AttributeElement = NodeElement. CreateChild ("attribute");
                AttributeElement.SetAttribute ("name", i -> name_);
                AttributeElement.SetAttribute ("value", i -> defaultValue_.ToString());

            }

            if(childnode->GetNumChildren())
            {
                SaveSceneNode(childnode);
            }
            else
            {
                SaveSceneNodeComponents(childnode);
            }

        }
    }
      savesceneexportxml->Save(saveFile);

}

/// Recursive
int Manager::SaveSceneNode(Node * node)
{
    /// Define a temporary pointer
    Vector<SharedPtr<Node> > subchildren_;

    /// Get children node
    subchildren_ = node->GetChildren();

    for (Vector<SharedPtr<Node> >::Iterator i = subchildren_.Begin(); i != subchildren_.End(); ++i)
    {
        /// Create a new child instance
        Node* childnode = *i;

        /// Get node infomration, check for children, and check components
        if(childnode->GetName().Find("Generated",0,false)==String::NPOS)
        {
            ///cout << "SubNode :" << childnode->GetName().CString() <<endl;
            XMLElement NodeElement = configElem. CreateChild ("node");

            if(childnode->GetNumChildren())
            {
                SaveSceneNode(childnode);
            }
            else
            {
                SaveSceneNodeComponents(childnode);
            }
        }
    }
}
int Manager::SaveSceneNodeComponents(Node *node)
{
    /// Define temporary pointer for components
    Vector< SharedPtr< Component > > 	subcomponents_;

    /// If node has no components
    if(node->	GetNumComponents ()==0)
    {
        cout << " Node has no components" << endl;

        return 1;
    }

    /// Get children node
    subcomponents_ = node->GetComponents();

    /// Loop through components
    for (Vector<SharedPtr<Component> >::Iterator i = subcomponents_.Begin(); i != subcomponents_.End(); ++i)
    {
        Component * subcomponent = *i;

      	XMLElement componentElement = configElem.CreateChild ("component");
      	componentElement.SetAttribute("Type", subcomponent->GetTypeName());

        /// READ EACH COMPONENT AND GET ATTRIBUTES
        if(subcomponent->GetNumAttributes ())
        {
            /// set virtual const
            const Vector<AttributeInfo>* attributes = subcomponent->GetAttributes();

            /// loop through attributes
            for (Vector<AttributeInfo>::ConstIterator i = attributes->Begin(); i != attributes->End(); ++i)
            {
                /// output info
                ///cout << i -> name_.CString() << " type " << i -> defaultValue_. GetTypeName ().CString() <<" value " << i -> defaultValue_.ToString().CString()<< endl;
                XMLElement AttributeElement = configElem. CreateChild ("attribute");
                AttributeElement.SetAttribute ("name", i -> name_);
                AttributeElement.SetAttribute ("value", i -> defaultValue_.ToString());
            }

        }
    }

    return 1;
}[/code]

The output is 

[code]<?xml version="1.0"?>
<node>
	<node>
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="" />
		<attribute name="Position" value="0 0 0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" value="" />
		<attribute name="Network Position" value="0 0 0" />
		<attribute name="Network Rotation" value="" />
		<attribute name="Network Parent Node" value="" />
	</node>
	<node>
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="" />
		<attribute name="Position" value="0 0 0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" value="" />
		<attribute name="Network Position" value="0 0 0" />
		<attribute name="Network Rotation" value="" />
		<attribute name="Network Parent Node" value="" />
	</node>
</node>[/code]

I'm trying to get output similiar to  

[code]<?xml version="1.0"?>
<node id="16777249">
	<attribute name="Is Enabled" value="true" />
	<attribute name="Name" value="" />
	<attribute name="Position" value="-0.012422 0.460372 0.00271687" />
	<attribute name="Rotation" value="1 1.30976e-06 0.000361086 6.60281e-07" />
	<attribute name="Scale" value="1 1 1" />
	<attribute name="Variables" />
	<component type="RigidBody" id="16777277">
		<attribute name="Physics Rotation" value="1 1.30991e-06 0.000361086 6.34012e-07" />
		<attribute name="Physics Position" value="-0.012422 0.460372 0.00271687" />
	</component>
	<component type="CollisionShape" id="16777278">
		<attribute name="Size" value="1.1 1.3 3.95" />
		<attribute name="Offset Position" value="0 0.13 0.3" />
	</component>
	<node id="16777236">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="" />
		<attribute name="Position" value="0 0 0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
		<component type="StaticModel" id="16777257">
			<attribute name="Model" value="Model;Models/airbikefoils.mdl" />
			<attribute name="Material" value="Material;Materials/airbike.colorbase.xml" />
			<attribute name="Cast Shadows" value="true" />
		</component>
	</node>
</node>
[/code]

-------------------------

vivienneanthony | 2017-01-02 01:04:15 UTC | #9

The new code produces results about 50% there. I have not figure out why the first node don't get the right attributes. I also not sure how to get the texture information and id's so it's clearer.

[code]
/// Main Save scene
int Manager::SaveScene(int mode)
{

    /// Check if scene exist

    if(scene_==NULL)
    {
        return 1;
    }


    String savesceneexport;

    ResourceCache * cache = GetSubsystem<ResourceCache>();
    FileSystem * filesystem = GetSubsystem<FileSystem>();

    savesceneexport.Append(filesystem->GetProgramDir().CString());
    savesceneexport.Append("CoreData/");
    savesceneexport.Append("testing.xml");

    File saveFile(context_, savesceneexport.CString(), FILE_WRITE);

    /// Check if the account file information exist
    if(!filesystem->FileExists(savesceneexport.CString()))
    {
        //cout << "\r\nAccount file ("<< savesceneexport.CString() << ") does not exist.";
    }

    XMLFile * savesceneexportxml= new XMLFile(context_);

    XMLElement configElem = savesceneexportxml-> CreateRoot("node");

    /// point
    unsigned int childrencount=scene_->GetNumChildren();

    /// Weak Pointer children
    Vector<SharedPtr<Node> > children_;

    children_ = scene_->GetChildren();

    /// loop each child
    for (Vector<SharedPtr<Node> >::Iterator i = children_.Begin(); i != children_.End(); ++i)
    {
        /// Create a new child instance
        Node* childnode = *i;

        /// Get node infomration, check for children, and check components
         if(childnode->GetName().Find("Generated",0,false)==String::NPOS)
         {
        XMLElement NodeElement = configElem. CreateChild ("node");

        const Vector<AttributeInfo>* attributes = childnode->GetAttributes();

        /// loop through attributes
        for (Vector<AttributeInfo>::ConstIterator j = attributes->Begin(); j != attributes->End(); ++j)
        {
            XMLElement AttributeElement;

            AttributeElement = NodeElement. CreateChild ("attribute");
            AttributeElement.SetAttribute ("name", j -> name_);
            AttributeElement.SetAttribute ("value", j -> defaultValue_.ToString());

        }

        if(childnode->GetNumChildren())
        {
            SaveSceneNode(childnode, NodeElement);
        }
        else
        {
            SaveSceneNodeComponents(childnode,NodeElement);
        }

        }
    }
    savesceneexportxml->Save(saveFile);

}

/// Recursive
int Manager::SaveSceneNode(Node * node, XMLElement parentelement)
{
    /// Define a temporary pointer
    Vector<SharedPtr<Node> > subchildren_;

    /// Get children node
    subchildren_ = node->GetChildren();

    for (Vector<SharedPtr<Node> >::Iterator i = subchildren_.Begin(); i != subchildren_.End(); ++i)
    {
        /// Create a new child instance
        Node* childnode = *i;

        /// Get node infomration, check for children, and check components
        if(childnode->GetName().Find("Generated",0,false)==String::NPOS)
        {
            ///cout << "SubNode :" << childnode->GetName().CString() <<endl;
            XMLElement NodeElement = parentelement. CreateChild ("node");

            if(childnode->GetNumChildren())
            {
                SaveSceneNode(childnode, parentelement);
            }
            else
            {
                SaveSceneNodeComponents(childnode,parentelement);
            }
        }
    }
}
int Manager::SaveSceneNodeComponents(Node *node, XMLElement parentelement)
{
    /// Define temporary pointer for components
    Vector< SharedPtr< Component > > 	subcomponents_;

    /// If node has no components
    if(node->	GetNumComponents ()==0)
    {
        cout << " Node has no components" << endl;

        return 1;
    }

    /// Get children node
    subcomponents_ = node->GetComponents();

    /// Loop through components
    for (Vector<SharedPtr<Component> >::Iterator i = subcomponents_.Begin(); i != subcomponents_.End(); ++i)
    {
        Component * subcomponent = *i;

        XMLElement componentElement = parentelement.CreateChild ("component");
        componentElement.SetAttribute("Type", subcomponent->GetTypeName());

        /// READ EACH COMPONENT AND GET ATTRIBUTES
        if(subcomponent->GetNumAttributes ())
        {
            /// set virtual const
            const Vector<AttributeInfo>* attributes = subcomponent->GetAttributes();

            /// loop through attributes
            for (Vector<AttributeInfo>::ConstIterator i = attributes->Begin(); i != attributes->End(); ++i)
            {
                /// output info
                ///cout << i -> name_.CString() << " type " << i -> defaultValue_. GetTypeName ().CString() <<" value " << i -> defaultValue_.ToString().CString()<< endl;
                XMLElement AttributeElement =  componentElement. CreateChild ("attribute");
                AttributeElement.SetAttribute ("name", i -> name_);
                AttributeElement.SetAttribute ("value", i -> defaultValue_.ToString());
            }

        }
    }

    return 1;
}
[/code]


Current Results using F12 - Console (/scene file dummy /build setscene /build savescene) 
[pastebin.com/xrgGWxFR](http://pastebin.com/xrgGWxFR)

-------------------------

vivienneanthony | 2017-01-02 01:04:16 UTC | #10

I basically  dumped the method I was using.  Changing the code to the below. I need to add more functionality from the console line and maybe a load.

[code]int Manager::SaveManagedNodes(const char *filename)
{
    /// Grab resources
    ResourceCache * cache = GetSubsystem<ResourceCache>();
    FileSystem * filesystem = GetSubsystem<FileSystem>();

    /// Check if scene exist
    if(scene_==NULL)
    {
        return 1;
    }

    /// Check if Node is empty
    if (ManagedNodes.Empty())
    {
        return 1;
    }

    /// Create String
    String savesceneexport;

    /// Set directory
    savesceneexport.Append(filesystem->GetProgramDir().CString());
    savesceneexport.Append("/");
    savesceneexport.Append(filename);

    File saveFile(context_, savesceneexport.CString(), FILE_WRITE);

    XMLFile * savesceneexportxml= new XMLFile(context_);

    XMLElement xmfileelement = savesceneexportxml-> CreateRoot("scene");

    /// Loop through components
    for(Vector<Node *>:: Iterator it = ManagedNodes.Begin(); it != ManagedNodes.End(); ++it)
    {
        (*it) -> SaveXML(xmfileelement);
    }

    savesceneexportxml->Save(saveFile);

    return 1;
}
[/code]

-------------------------

