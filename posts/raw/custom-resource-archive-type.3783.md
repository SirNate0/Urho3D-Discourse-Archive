Naros | 2017-11-25 11:51:52 UTC | #1

Is there a way to extend Urho3D's resource system with custom archive types?  

    ResourceCache* cache = GetSubsystem<ResourceCache>();
    cache->BackgroundLoadResource<MapFile>( "Maps/ArticWonderland.map" );

The .map file is located inside a proprietary bundle format and I had hoped there was a way I could have wrapped our library using some Urho3D Bundle-like interface that we could register with the ResourceCache system.  Other engines expose similar solutions but I haven't yet seen how to do with Urho3D.

-------------------------

Eugene | 2017-11-25 12:41:35 UTC | #2

[quote="Naros, post:1, topic:3783"]
Is there a way to extend Urho3D’s resource system with custom archive types?
[/quote]

Do you want to load Urho resources from this archive?
Or it's enough for you to load the archive into `MapFile` itself?
Code snippet that you posted here should work fine if MapFile is derived from Resource.

-------------------------

Naros | 2017-11-25 19:25:44 UTC | #3

> Do you want to load Urho resources from this archive?

Yes.  

For example, there are _XMLFile_ resources in this bundle that I would have liked to have been able to simply load by using the standard API as follows

    XMLFile xml = GetSubsystem<ResourceCache>()->LoadResource<XMLFile>( "UI/Constants.xml" );

My hope was that I would be able to supply the _ResourceCache_ with a variety of _container_ implementations and it simply asks these _containers_ if a resource by the name exists and if so, the _container_ would then know how to stream the contents into the _Resource_ object.

> Or it's enough for you to load the archive into `MapFile` itself?

I'm not sure I understand this.

> Code snippet that you posted here should work fine if MapFile is derived from Resource.

Actually, it doesn't and reports that the resource cannot be loaded.  

This is because `ResourceCache` calls `GetFile` that leads to trying to create ` File` object that refers to that path; however it cannot create the `File` because internally its all based on looking in packages and the file system.  Since that file exists inside a custom bundle file, Urho3D doesn't seem to have a way to extend the resource subsystem with custom archive format types.

-------------------------

Eugene | 2017-11-25 20:29:45 UTC | #4

Oh, I see now.
It's not supported now.
However, it's not hard to add support of this feature.
This may require some tweaking of `PackageFile` and `ResourceCache`, but it's definetely doable.

- Virtualize `PackageFile` or extract some interface;
- Extract file creation from `ResourceCache::SearchPackages` to `PackageFile` virtual function;
- Somehow replace `File` with `AbstractFile` across `ResourceCache` because it would be almost impossible to make your custom package return true `File`. May require some interface changes.
- Then just add your package to resource cache and load resources.

Don't see any obstacles for now, except some design questions in (3)

-------------------------

Naros | 2017-11-25 20:54:24 UTC | #5

Awesome, I think this could go a long way for Urho3D users who would like to plug-in a custom resource provider solution that doesn't necessarily fit the compressed archive or file-system paradigm.

-------------------------

Eugene | 2017-11-25 23:27:24 UTC | #6

If you want maintainer(s?) to work on this feature request, please report it on GitHub.
If you are going to do it on your own, good luck and I'm waiting for PR.

-------------------------

