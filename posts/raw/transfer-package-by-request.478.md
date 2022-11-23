cin | 2017-01-02 01:00:45 UTC | #1

I want to allow user upload package file on runtime, with [UserNodeFile].xml and all resources used in xml file, to server, create node and load content to this node from xml file.
All stes here:
1. User upload package file to server
2. Server call ResourceCache->AddPackageFile(user_package_file); and add package file to autoload.
3. Client send command to create node and load node content form xml file from package file.
4. Server create node and load its content from xml file.
5. Now network must send package file to clients to allow see created model by user.
6. Server send node ID to client to allow user manipulate it.

-------------------------

cin | 2017-01-02 01:00:45 UTC | #2

Now I make experiment and I see what package file sending when client connect to server.
My test code here.

[code]Node* NetServer::CreateTestObject(Vector3 pos = Vector3::ZERO)
{
	Node* pn = scene->CreateChild("Test");
	pn->SetPosition(pos);
	ResourceCache* cache = GetSubsystem<ResourceCache>();
	SharedPtr<PackageFile> pkgfile(new PackageFile(context_, "Packages\\Teapot.pkg"));
	cache->AddPackageFile(pkgfile);
	scene->AddRequiredPackageFile(pkgfile);
	XMLFile* xf = (cache->GetResource<XMLFile>("Teapot.xml"));
	XMLElement xr = xf->GetRoot("node");
	pn->LoadXML(xr);
	return pn;
}[/code]

How i can to force clients to download added package when they already connected and have loaded scene?

-------------------------

cadaver | 2017-01-02 01:00:45 UTC | #3

Presently you can't (without modifying the engine).

Urho does not work well as an engine using network streamed resources/packages, because everything is based on the assumption of immediately available resources (ie. you instantiate a model, you expect the model/material/textures to already be there.)

If resources were loaded from packages in the middle of a client being connected to a scene, either the server would have to delay sending objects depending on those packages, or the client would need the intelligence to wait before trying to instantiate them.

You are welcome to improve the engine to work in this direction, but it may be a large and hard overhaul. Btw. this is exactly the situation we are dealing a lot in the realXtend Tundra project ([github.com/realxtend/tundra.git](https://github.com/realxtend/tundra.git)), and that's also why its network & asset code are at least 2x more complex than Urho :slight_smile:

-------------------------

cin | 2017-01-02 01:00:45 UTC | #4

cadaver,  are you (or who now work with realXtend/tundra) plan to add this feature to engine? 
Today I try to understand engine internals and may be write here about how to implement this.
My preliminary thoughts on the matter:

[ul][li]Client receive that what it must create replicated node with component.[/li]
[li]If it fail, client get list of packages on server and check they on cache. If needed then client download (sync) missing packages from server, and try again to load resource into cache.
OR[/li]
[li]If it fail, client ask server "In which package this resource?" . Server send package filename and client download (sync) only this missing package from server, and try again  to load resource.[/li][/ul]

-------------------------

cadaver | 2017-01-02 01:00:45 UTC | #5

My plan is to not work on this kind of functionality, at least for now. The Tundra codebase is practically full of assumptions "what if this asset is not yet downloaded" and the increased complexity that results from it, so in Urho I was glad to be free from that :wink:

I assume that with "fail" you mean that some of the needed resources is missing. Your flow looks basically OK. You possibly may get away with instantiating the node and component instantly, but leaving for example the model empty (null) as it hasn't been downloaded yet. Then you start the download and once it's completed, assign the model. You'll run into difficulties and special cases, though, for example a bone hierarchy can not be instantiated before the model exists, so if the object has bone attachments, those can not practically be instantiated before the model.

Another way would be to store objects received from server, that have missing resources, into a kind of "buffer" while waiting for the resources to load. Then, after all needed resources are loaded, instantiate the object based on the buffered data. The server will of course keep sending updates (as eg. the object moves), in which case you must keep updating the buffered data. And in worst case the object might get deleted before the downloads finish, which you also need to take into account.

-------------------------

cadaver | 2017-01-02 01:00:46 UTC | #6

It looks to be on the right track at least in theory. One thing you didn't have there yet would be to sync the updated package list to other connected clients, right?

-------------------------

cin | 2017-01-02 01:00:46 UTC | #7

Some update.
indent is 4 spaces.
Added parameter all_clients, if it true then all clients sync packages. Default it true.
SyncPackages registered in NetworkAPI.cpp.
Pull request created.

-------------------------

