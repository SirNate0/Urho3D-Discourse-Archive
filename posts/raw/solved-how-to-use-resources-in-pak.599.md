codingmonkey | 2017-01-02 01:01:36 UTC | #1

hi [size=50]world[/size] folks!)
i found some interesting section on urho.io and read this info about packages:
[urho3d.github.io/documentation/H ... urces.html](http://urho3d.github.io/documentation/HEAD/_resources.html)

I was especialy interested in this:
[quote]By default, the engine registers the resource directories Data and CoreData, or the packages Data.pak and CoreData.pak if they exist.[/quote]

then i go to test this:
i copy my bin directory with worked testscene.exe and create *.bat file:

[code]PackageTool.exe CoreData\ CoreData.pak -c
PackageTool.exe Data\ Data.pak -c[/code]

after packages compile two *.pak file i delete old dirs Data\ and CoreData\

Then i try to run testscene.exe and it not runnning( 
why? i forgot something, to do ?

-------------------------

Pellucas | 2017-01-02 01:01:36 UTC | #2

No problem on OSX

-------------------------

codingmonkey | 2017-01-02 01:01:36 UTC | #3

how do you make the packages ?

in the program anything needed to rewrite or add some code? for use *.pak's 
or it just if there are no folders ResourceCache will search for packages ?

i try to debug my app with only pakages and it handle error on getting "cameraNode" of Scene. 
this getNode it's first get in program, and it ended with err. 
I think that the scene is not loaded as needed, but why  :question:

-------------------------

codingmonkey | 2017-01-02 01:01:36 UTC | #4

i rewrite scene loading proc
and now it's work
[code]
void GameMain::LoadScene(Urho3D::String sceneFileName) 
{
	scene_ = new Scene(context_);
	
	//File sceneFile(context_, 
	//				GetSubsystem<FileSystem>()->GetProgramDir() + "Data/Scenes/" + sceneFileName,
	//				FILE_READ);
	
	File sceneFile (context_, 
					new PackageFile(context_,GetSubsystem<FileSystem>()->GetProgramDir() +"/Data.pak"), 
					"Scenes/" + sceneFileName);

	scene_->LoadXML(sceneFile);
}
[/code]

-------------------------

