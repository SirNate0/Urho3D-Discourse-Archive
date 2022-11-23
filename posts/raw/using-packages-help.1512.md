vivienneanthony | 2017-01-02 01:08:12 UTC | #1

Hello,

How do you use packages? This is what I'm doing I have a file GameAssetData.xml and putting it in for example GameData.pak package file.

I have a function the search a Package or list with adidtional search criterias. It returns a a Vector <string>.

On the first find of GameAssetData.xml located there.

The question next is how do I load it properly.

Vivienne

-------------------------

thebluefish | 2017-01-02 01:08:12 UTC | #2

[url=https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/IO/File.h#L91]File::Open seems to be what you want.[/url]

Alternatively you can use ResourceCache to open it.

-------------------------

vivienneanthony | 2017-01-02 01:08:13 UTC | #3

[quote="thebluefish"][url=https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/IO/File.h#L91]File::Open seems to be what you want.[/url]

Alternatively you can use ResourceCache to open it.[/quote]

I'm looking at resource cache documentation but just not sure how to open it. I have something like


[code]// load game assets
bool GameAssetData::LoadGameAssets(Vector<GameAsset*>* AllData)
{
    // Get Resource
    ResourceCache* resCache = g_pApp->GetConstantResCache();

    // create a empty file
    Vector<String> m_datafiles;
    String m_UsePackage;

    // search files
    for(unsigned i=0; i<=m_pDataFiles->Size(); ++i)
    {
        // temporary clear data
        m_datafiles.Clear();

        m_datafiles = SWResourceCache::Match(g_pApp->GetConstantResCache(), m_pDataFiles->At(i), m_pDataPath->CString());

        // if file is found
        if(m_datafiles.Size()>0)
        {
            // Use this package
            UsePackage.Append(m_pDataFiles->at(i));

            break;
        }
    }

    // If datafiles is 0 or empty return - meaning nothing was found
    if(UsePackage.Empty())
    {
        return false;
    }


    // Set File Pointer to file
    SharedPtr<File> m_DataFile = rescache->GetFile("GameAssetOption.xml");


    return true;
}[/code]

-------------------------

thebluefish | 2017-01-02 01:08:13 UTC | #4

ResourceCache can use Package Files the exact same way as directories. For example, /Data/ and Data.pak are interchangeable, and retrieving "scripts/editor.as" will pull from either one.

If you're not trying to use ResourceCache the way it's meant to be used (ie, you are trying to directly work with the package file), then you have to use File::Open.

-------------------------

vivienneanthony | 2017-01-02 01:08:13 UTC | #5

[quote="thebluefish"]ResourceCache can use Package Files the exact same way as directories. For example, /Data/ and Data.pak are interchangeable, and retrieving "scripts/editor.as" will pull from either one.

If you're not trying to use ResourceCache the way it's meant to be used (ie, you are trying to directly work with the package file), then you have to use File::Open.[/quote]

Like the above code I posted?

-------------------------

thebluefish | 2017-01-02 01:08:13 UTC | #6

AFAIK as long as you aren't doing something strange, the code *should* work in the sense that:

[code]
SharedPtr<File> m_DataFile = rescache->GetFile("GameAssetOption.xml");
[/code]

Should pull a File from a Package assuming the Package is used by ResourceCache. However I am not sure what the rest of the code is useful for.

-------------------------

vivienneanthony | 2017-01-02 01:08:13 UTC | #7

[quote="thebluefish"]AFAIK as long as you aren't doing something strange, the code *should* work in the sense that:

[code]
SharedPtr<File> m_DataFile = rescache->GetFile("GameAssetOption.xml");
[/code]

Should pull a File from a Package assuming the Package is used by ResourceCache. However I am not sure what the rest of the code is useful for.[/quote]

I boiled down a error to this

[pastebin.com/xXVD96xU](http://pastebin.com/xXVD96xU)

I checked the size of which is correct to the filename but I tried muiltiple ways. I think those lines load up garbage. So, either I'm not allocating the memory correctly or something else.

-------------------------

