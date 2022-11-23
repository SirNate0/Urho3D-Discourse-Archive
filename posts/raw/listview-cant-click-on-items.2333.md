TheComet | 2017-01-02 01:14:48 UTC | #1

I'm adding items to my ListView with the following code:

[code]void LobbyScreen::ScanForMaps()
{
    FileSystem* fs = GetSubsystem<FileSystem>();
    ResourceCache* cache = GetSubsystem<ResourceCache>();

    LineEdit* selectedMap = GetUIChild<LineEdit>(mapSelect_, "lineEdit_selectedMap");
    ListView* mapsList = GetUIChild<ListView>(mapSelect_, "listView_maps");
    if(selectedMap == NULL || mapsList == NULL)
        return;
    mapsList->RemoveAllItems();

    const StringVector& resourceDirs = cache->GetResourceDirs();
    for(StringVector::ConstIterator resourceDir = resourceDirs.Begin();
        resourceDir != resourceDirs.End();
        ++resourceDir)
    {
        const String scenePath = *resourceDir + "Scenes/";
        if(!fs->DirExists(scenePath))
            continue;

        URHO3D_LOGDEBUGF("Scanning for maps in %s", scenePath.CString());
        StringVector sceneList;
        fs->ScanDir(sceneList, scenePath, "*", SCAN_FILES, true);

        for(StringVector::ConstIterator sceneFile = sceneList.Begin();
            sceneFile != sceneList.End();
            ++sceneFile)
        {
            URHO3D_LOGDEBUGF("Found map %s", sceneFile->CString());
            StringVector split = sceneFile->Split('/');
            Text* text = new Text(context_);
            text->SetStyleAuto();
            text->SetText(*(split.End() - 1));
            mapsList->AddItem(text);
        }
    }
}[/code]

However, I can't select any of the items in the list view. They just don't react to the mouse at all. How can I enable selection? I'm using a ListView with default settings.

[img]http://i.imgur.com/hHRKEn1.png[/img]

-------------------------

cadaver | 2017-01-02 01:14:48 UTC | #2

There is no automatic mechanism to guarantee that text shows a highlight effect upon being selected, rather you need to use a style which enables that or set it yourself. For example "FileSelectorListText"

-------------------------

