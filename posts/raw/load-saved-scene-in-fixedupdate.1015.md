szamq | 2017-01-02 01:04:50 UTC | #1

I'm doing simple scene loading in fixed update. I noticed I have random crashed with that.
When I move my loading scene code to Update event then the issue is not present.

[code]		
File loadFile(fileSystem.programDir + "Data/Scenes/CharacterDemo", FILE_READ);
scene_.Load(loadFile);
script.defaultScene=scene_;

characterNode = scene_.GetChild("Player", true);
if (characterNode is null)
	return;
HandleCameraToPlayer();
[/code]

Is there something obvious that load scene could cause troubles in FixedUpdate aka PhysicsPreStep?
Or should I find some access violations in my code? (Note I'm using AngelScript and it's not writing null usage in the console, just crash and generated dump)

-------------------------

cadaver | 2017-01-02 01:04:51 UTC | #2

FixedUpdate is implemented via a callback from Bullet physics update, so unfortunately it's not safe to load the scene during it, at least if it contains active physics objects.

I would recommend using the application-level update events for scene loading, to ensure nothing gets interrupted. Probably you're safe when using Update, but just for the sake of clean determinism.

-------------------------

szamq | 2017-01-02 01:04:51 UTC | #3

Thanks for the anwser

-------------------------

