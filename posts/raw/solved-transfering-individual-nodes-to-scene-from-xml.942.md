vivienneanthony | 2017-01-02 01:04:17 UTC | #1

Hi

I'm trying to transfer a xml with nodes into the scene. I have to parse through each element because I have to add each node invidiually.

I created the following code but I think I'm doing something wrong. Most definitely.

Vivienne

[code]/// Load account information from a account file
int Manager::LoadManagedNodes(const char *filename)
{

    /// Grab resources
    ResourceCache * cache = GetSubsystem<ResourceCache>();
    FileSystem * filesystem = GetSubsystem<FileSystem>();

    /// Check if scene exist
    if(scene_==NULL)
    {
        return 1;
    }

    /// Force .xml on Load
    if(!string(filename).find(".xml"))
    {
        return 0;
    }

    /// Create String
    String Loadsceneexport;

    /// Set directory
    Loadsceneexport.Append(filesystem->GetProgramDir().CString());
    Loadsceneexport.Append("/");
    Loadsceneexport.Append(filename);

    XMLFile * loadingfile = new XMLFile(context_);

    /// Create a file in current context
    File LoadFile(context_, Loadsceneexport.CString(), FILE_READ);

    loadingfile->Load(LoadFile);

    XMLElement nextElement = loadingfile -> GetRoot().GetChild("node");

    do
    {
        if(nextElement==0)
        {
            break;

        }

        /// Create pointer
        Node * newNode;

        newNode ->	LoadXML (nextElement, false);

        scene_->AddChild(newNode);


        /// push
        ManagedNodes.Push(newNode);

        cout << newNode -> GetID() <<endl;

        nextElement=nextElement.GetNext("node");

    } while(nextElement!=NULL);

    return 1;
}

[/code]

-------------------------

vivienneanthony | 2017-01-02 01:04:17 UTC | #2

I think the problem lays in these lines.
[code]
 /// Create pointer
        Node * newNode;

        newNode ->   LoadXML (nextElement, false);

        scene_->AddChild(newNode);[/code]

-------------------------

vivienneanthony | 2017-01-02 01:04:17 UTC | #3

The format I'm trying to read is
[code]
<?xml version="1.0"?>
<node id="211">
	<attribute name="Is Enabled" value="true" />
	<attribute name="Name" value="oddbox" />
	<attribute name="Position" value="0 0 0" />
	<attribute name="Rotation" value="1 0 0 0" />
	<attribute name="Scale" value="1 1 1" />
	<attribute name="Variables" />
	<component type="StaticModel" id="431">
		<attribute name="Model" value="Model;Models/oddbox.mdl" />
		<attribute name="Material" value="Material;Materials/oddbox.xml" />
	</component>
	<component type="GameObject" id="432" />
</node>
[/code]

I tried the following with no luck either
[code]
/// Create a file in current context
    File LoadFile(context_, Loadsceneexport.CString(), FILE_READ);

    loadingfile->Load(LoadFile);

    XMLElement nextElement = loadingfile -> GetRoot();

    nextElement=nextElement.GetNext("node");

    do
    {
        if(nextElement.IsNull())
        {
            break;

        }

        /// Create pointer
        Node * newNode;

        newNode ->	LoadXML (nextElement, false);

        scene_->AddChild(newNode);

        cout << nextElement.GetName().CString() << endl;


        /// push
        ManagedNodes.Push(newNode);

        nextElement=nextElement.GetNext("node");

    } while(nextElement.NotNull());
[/code]

-------------------------

