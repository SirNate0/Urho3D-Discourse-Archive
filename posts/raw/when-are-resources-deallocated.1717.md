TheComet | 2017-01-02 01:09:40 UTC | #1

I can't quite wrap my head around the way memory is managed.

When is sceneFile deleted in this case? Should I be doing something to free that resource after I use it?
[code]XMLFile* sceneFile = cache->GetResource<XMLFile>("Scenes/Ramps.xml");
// use sceneFile for something here[/code]

Should I be doing this?
[code]Node* cameraNode = scene_->CreateChild("Camera");[/code]

...or this?
[code]SharedPtr<Node> cameraNode = scene_->CreateChild("Camera");[/code]

and why?

-------------------------

Dave82 | 2017-01-02 01:09:40 UTC | #2

Resources are deallocated when their ref count reaches 0.

[quote]When is sceneFile deleted in this case? Should I be doing something to free that resource after I use it?
[code]XMLFile* sceneFile = cache->GetResource<XMLFile>("Scenes/Ramps.xml");
// use sceneFile for something here[/code][/quote]

Yes you should ! You have to call either
[code]cache->ReleaseAllResources();[/code]
To delete ALL unused resources
or call :
[code]sceneFile->ReleaseRef();[/code]
or 
[code]cache->GetResource<XMLFile>("Scenes/Ramps.xml")->ReleaseRef();[/code]

This is because once you load a resource the resourceCache will automatically increase the refCount by 1.If you use this resource anywhere in the scene , the ref count increses.
the "ReleaseAllResources" function simply releases all unused resources.(all resources where refCount == 1 will be deleted)

Urho has also a smart pointer system.This ensures automatic destruction of a resource / Node / Component , if they go out of their scope.
If you call :

[code]SharedPtr<XMLFile> sceneFile = cache->GetTempResource<XMLFile>("Scenes/Ramps.xml");[/code]
In this case the resource cahce won't increase the ref count on the resource (returns the sceneFile with reCount == 0) and constructs a smart pointer from it
(which increases the refCount of sceneFile)

In short : in this case the sceneFile will be deleted automatically once it goes out of it's scope :

[code]
{
      SharedPtr<XMLFile> sceneFile = cache->GetTempResource<XMLFile>("Scenes/Ramps.xml");
}
// sceneFile deleted... you don't need to worry about the memory anymore.

{
    XMLFile* sceneFile = cache->GetResource<XMLFile>("Scenes/Ramps.xml");
}
// sceneFile pointer destructed hovewer resourceCache still keeps a refCount to it.To delete it call :
cache->GetResource<XMLFile>("Scenes/Ramps.xml")->ReleaseRef();

// or perform a globa cleanup:
cache->ReleaseAllResources();

[/code]


[quote]Should I be doing this?
[code]Node* cameraNode = scene_->CreateChild("Camera");[/code]

...or this?
[code]SharedPtr<Node> cameraNode = scene_->CreateChild("Camera");[/code]

and why?[/quote]

The first example CreateChild() simply returns a pointer to the object with refCount == 1 (only scene holds it's reference) so while your scene "is alive" your cameraNode is going to be a live.
The second example CreateChild() returns a pointer , but constructs a shared pointer from it (which increases the cameraNode's ref coint to 2... 1 ref by scene 2nd ref by the SharedPtr.
Once your sharedPtr goes out of scope , it wiil automatically decrease the cameraNode's refCount to 1 (scene still keeps a reference to it)
Once you delete your scene the cameraNode will be deleted too.

To delete your camera node , you have to call cameraNode->Remove();

-------------------------

TheComet | 2017-01-02 01:09:40 UTC | #3

Thanks, that was very informative.

I tested the things you said and it all makes sense to me now.

[code]	Node* n1 = scene->CreateChild("n1");
	SharedPtr<Node> n2(scene->CreateChild("n2"));

	std::cout << n1->Refs() << std::endl;
	std::cout << n2->Refs() << std::endl;
	std::cout << n2.Refs() << std::endl;  // this delegates to n2->Refs()[/code]

The output is:
[code]1
2
2[/code]

-------------------------

