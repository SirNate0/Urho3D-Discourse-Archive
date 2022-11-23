vivienneanthony | 2017-01-02 01:08:04 UTC | #1

Hello 

Is this correct? I tried removing the file location and directory but it still loading a document or the first IF statement is not failing.

I'm wonder if it's a platform specific thing or problem. I'm using linux.

Vivienne


[code]bool GameOptions::Init(const char* xmlFilePath)
{

    //// read the XML file
    //// if needed, override the XML file with options passed in on the command line.
    m_FileName = String(xmlFilePath);

    m_pFile = new Urho3D::XMLFile(g_pApp->GetContext());

    pugi::xml_document* document = m_pFile->GetDocument();

    document->load_file(xmlFilePath);

    if (!document)
    {
        return false;
    }

    pugi::xml_node root = document->root();
    if (!root)
    {
        return false;
    }

    // Loop through each child element and load the component
    pugi::xml_node node;
    node = root.first_child();
    if (String(node.attribute("name").as_string()).Compare("options") == 0)
    {
        node = node.child("Graphics");
        if (node)
        {
            String attribute = node.attribute("renderer").as_string();
            int comp = attribute.Compare("OpenGL", false);

            if (attribute.Compare("OpenGL", false) == 0 || attribute.Compare("DirectX11", false) == 0 || attribute.Compare("DirectX9", false) == 0)
            {
                m_Renderer = attribute;
            }
            else
            {
                return false;
            }[/code]

-------------------------

thebluefish | 2017-01-02 01:08:04 UTC | #2

Technically, that shouldn't fail. You are checking against an object which should exist. Maybe you're looking to check if the document is opened instead?

[url=https://github.com/thebluefish/IndiesvsGamers/blob/master/IndiesvsGamers/IndiesvsGamers/src/SettingsData.cpp#L89]Here's an example of loading an XML file and parsing it.[/url]

-------------------------

