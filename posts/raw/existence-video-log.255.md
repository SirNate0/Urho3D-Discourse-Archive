vivienneanthony | 2017-01-17 18:46:13 UTC | #1

Hey

I decided to create a video log of my attempt to use Urho3D to development a game at least walk through. I'm not sure how to do the menu system but  I have to learn.

The video is [youtube.com/watch?v=2SHZwar ... e=youtu.be](https://www.youtube.com/watch?v=2SHZwar9cmA&feature=youtu.be)

http://www.youtube.com/watch?v=2SHZwar9cmA

My page is [youtube.com/cgprojectsfx](http://youtube.com/cgprojectsfx)

If anyone sees any problems, or better ways of doing something please write or comment. I will like to convert the following [youtube.com/watch?v=UWaMXP5 ... 1400182326](https://www.youtube.com/watch?v=UWaMXP5pGak&list=HL1400182326) to a more massive and robust setup.

Vivienne

-------------------------

Stinkfist | 2017-01-02 00:59:19 UTC | #2

Great, keep 'em coming! You might want to process the audio a bit to get rid of the static noise in the future.

-------------------------

vivienneanthony | 2017-06-10 19:56:55 UTC | #3

Hello All

This is the third video. I managed to get a compiled executable with your help and the documentation. 

1. I'm a little confused how the engine work. I read it was task driven so basically throught events/event handlers. I coded a login window function then added a event specific for that function. Then a second window function. When the first event handler is called. It starts the second window function.

Is that correct?

2. A progress bar. Still looking at how to do that.

Do I have to use a sprite to create that.

3. I want to add a basic character after the progress and update. There a console can be open (small) to execute a scene.

I was thinking of loading a xml temporarily but then update to a SQLITE load meaning I would have to create a importer from xml into a format for a database.

Anyway, sorry about noise. Don't know how to process the audio in Kdenlive fully yet.

Vivienne


https://www.youtube.com/watch?v=DGn_-fkuVYo

-------------------------

vivienneanthony | 2017-01-02 00:59:23 UTC | #4

Hello,

Is there a page showing what can be set with in the .xml?

    <element type="CloseButton" style="Button" auto="false">    <!-- non-auto style is shown explicitly in the Editor's style drop down list for user selection -->
        <attribute name="Min Size" value="16 16" />
        <attribute name="Max Size" value="16 16" />
        <attribute name="Image Rect" value="144 0 160 16" />
        <attribute name="Focus Mode" value="NotFocusable" />
    </element>

Vivienne

-------------------------

vivienneanthony | 2017-01-02 00:59:24 UTC | #5

Hello

I'm trying to remove a node but I'm not sure if it's correct. I think there is a problem with the bolded part but not sure where to look.

This is more a coding question not a bug.

Vivienne


[quote]void ExistenceClient::LoginScreenHandleClosePressed(StringHash eventType, VariantMap& eventData)
{

      Node *ExistenceLogo = scene_->GetChild("ExistenceLogo");

      scene_->RemoveChild(ExistenceLogo);

      ProgressScreen();

}[/quote]

-------------------------

vivienneanthony | 2017-01-02 00:59:24 UTC | #6

Hmmmm

I tried ...

[quote]void ExistenceClient::LoginScreen()
{

    Node* existencelogoNode = scene_->CreateChild("ExistenceLogo");
    //existencelogoNode ->SetScale(Vector3(1.0f,1.0f,1.0f));
    existencelogoNode ->SetPosition(Vector3(0.0,2.0,0.0));
    existencelogoNode ->SetRotation(Quaternion(270.0, 270.0,90.0));
    existencelogoNode ->SetName("ExistenceLogo");


}

void ExistenceClient::LoginScreenHandleClosePressed(StringHash eventType, VariantMap& eventData)
{

    // remove child node
    scene_->RemoveChild(scene_->GetChild("Existencelogo"));

    ProgressScreen();

}[/quote]

-------------------------

friesencr | 2017-01-02 00:59:24 UTC | #7

You may have a strong reference to the object still.  I believe the Node is only removed if there are no outstanding strong pointers.  If another object is holding a pointer you can swap it out with a weak pointer.  I also think there is a Remove() method on the Node itself.

-------------------------

vivienneanthony | 2017-01-02 00:59:24 UTC | #8

[quote="friesencr"]You may have a strong reference to the object still.  I believe the Node is only removed if there are no outstanding strong pointers.  If another object is holding a pointer you can swap it out with a weak pointer.  I also think there is a Remove() method on the Node itself.[/quote]

Hmm.  I will look at it again. I attempted to swap the Node with a blank node which did not work with a removechild.

I also attempted these lines but no response with that. I figure take out any components for that node which was a no go.

[quote]   // remove child node
    scene_->GetChild("ExistenceLogo",true)->RemoveAllComponents();
    scene_->GetChild("ExistenceLogo",true)->Remove();[/quote]

-------------------------

vivienneanthony | 2017-06-10 20:08:10 UTC | #9

[quote="friesencr"]You may have a strong reference to the object still.  I believe the Node is only removed if there are no outstanding strong pointers.  If another object is holding a pointer you can swap it out with a weak pointer.  I also think there is a Remove() method on the Node itself.[/quote]

THe second method mentioned seemed to work. I added a simple code to test if a account file exist and it sets up a variable accountexist to true or false. Oddly, without the file i/o it works but with it it doesn't. Basically a way to change the wine button options. So, I'm lost why. 

The only thing is becuase accountfile.open is dynamic Urho might not work that way and might require me to use the XML thirdparty option  included.

[quote]  // check account file
    ifstream accountfile;

    accountfile.open("CoreData/account.xml");

    if(accountfile.is_open())
    {
        accountexist=true;

        accountfile.close();
    }

    if(accountexist)
    {
        SubscribeToEvent(loginButton, E_RELEASED, HANDLER(ExistenceClient, LoginScreenHandleClosePressed));
    }else
    {

        SubscribeToEvent(newaccountButton, E_RELEASED, HANDLER(ExistenceClient, NewAccountHandleClosePressed));
    }
[/quote]

-------------------------

vivienneanthony | 2017-06-10 20:08:27 UTC | #10

Hello All

This is the fourth video in.  I am showing more of the code so maybe someone have a suggestion or can see a error.
https://www.youtube.com/watch?v=hvZuzmM-o1A&feature=youtu.be

Vivienne

-------------------------

vivienneanthony | 2017-06-10 20:08:43 UTC | #11

Hello

This is a update. Any feedback other then sound of the video is helpful? Tips or Ideas.

https://www.youtube.com/watch?v=7VI2__XXGlA

Complete Playlist 
[youtube.com/playlist?list=P ... re=mh_lolz](https://www.youtube.com/playlist?list=PLg3Q9upEQvPRAYaIqhImkUu1RBgSZA_N7&feature=mh_lolz)

Vivienne

-------------------------

jorbuedo | 2017-01-02 00:59:32 UTC | #12

If you want ideas you could have a look at makehuman, or any other rpg game with a character creation tool.

-------------------------

vivienneanthony | 2017-01-02 00:59:33 UTC | #13

[quote="jorbuedo"]If you want ideas you could have a look at makehuman, or any other rpg game with a character creation tool.[/quote]

I used makehuman to make the base meshes then imported it into blender then export to Urho3d.  Lot's of exporting.

I'm going research how to make some meshes but I don't think there is a option in makehuman to make non human characters.

-------------------------

vivienneanthony | 2017-06-10 20:08:58 UTC | #14

Hey,

Here is a update. So, I made the main screens UI. So I'm off to coding functionality.

I'll update a video showing the code in addition because I have some questions.

When done I was thinking at the main screen to make a hidden console that I can enter a command to load and start a scene

Vivienne

https://www.youtube.com/watch?v=n9EEWegmBSA

-------------------------

vivienneanthony | 2017-06-10 20:09:15 UTC | #15

Hi,

(Quick update)

I'm not sure if I'm at the point of setting up a scene load with a character allowing movement. If anyone have any suggestions feel free to write or contact me.

I can make some of the source available to anyone people who like to collaborate and into Starr Trek of scifi genre games(etc). I am considering using the standard scene xml load used in the demos so a scene can be made in the editor and/or a scene generator.

Vivienne

https://www.youtube.com/watch?v=wD3F01rWQSY&feature=youtu.be

-------------------------

vivienneanthony | 2017-06-10 20:09:26 UTC | #16

Thanks for all the help.

This is what I have already raw. So technically with some more work I can import the scene I made.

https://www.youtube.com/watch?v=LMTZN8DM3lg

-------------------------

vivienneanthony | 2017-06-10 20:09:34 UTC | #17

I will work on texture and code next. Probably working on the pipeline and a character integration.

https://www.youtube.com/watch?v=cBzGPRjmOvQ

-------------------------

vivienneanthony | 2017-06-10 20:09:49 UTC | #18

https://www.youtube.com/watch?v=vcFBM_5I_C4

Updates
1. Added physhics of Urho3D(Bullet) including collisions
2. Refined some textures and better utilized the Blender to Urho3D exporter
3. Added jump, turn left and right, back and forward movement
4. Added two camera modes first person and fly mode.
5. Cleaned up some code

To-Do
1. Add dynamic UI HUD interface in player mode.
2. Save input from the user
3. Improve terrain texture
4. Optimize better character movement. 
5. Impove character collision bounds - WIP - Created functional code and testing.
6. Add Debug hud - WIP Added and testing
7. Perlin generated terrain with save ability - WIP - Developing with others.

If anyone wants to help with this engine, contact me at [cgprojectsfx@gmail.com](mailto:cgprojectsfx@gmail.com).

-------------------------

vivienneanthony | 2017-06-10 20:10:22 UTC | #19

Testing Urho3d procedural generated heightmap option to save.

https://www.youtube.com/watch?v=bKRzQbz6FUM&list=UUTObP1VzcIglm7uTgUBQjaw

Function creating the scene.

[code] 
    //Terrain
    Node* terrainNode = scene_->CreateChild("Terrain");

    Terrain* terrain = terrainNode->CreateComponent<Terrain>();
    terrain->SetPatchSize(64);
    terrain->SetSpacing(Vector3(2.0f, 0.8f, 2.0f)); // Spacing between vertices and vertical resolution of the height map
    terrain->SetSmoothing(true);

    terrain->GenerateHeightMap();

    terrain->SetMaterial(cache->GetResource<Material>("Materials/Terrain.xml"));

    RigidBody* terrainbody = terrainNode->CreateComponent<RigidBody>();
   CollisionShape* terrainshape = terrainNode->CreateComponent<CollisionShape>();
    // Set a box shape of size 1 x 1 x 1 for collision. The shape will be scaled with the scene node scale, so the
    // rendering and physics representation sizes should match (the box model is also 1 x 1 x 1.)
    terrainbody->SetCollisionLayer(1);
    terrainshape->SetTerrain();


    // Create a scene node for the camera, which we will move around
    // The camera will use default settings (1000 far clip distance, 45 degrees FOV, set aspect ratio automatically)
    cameraNode_ = new Node(context_);

    cameraNode_ = scene_->CreateChild("Camera");
    cameraNode_->CreateComponent<Camera>();

    Camera* camera = cameraNode_->CreateComponent<Camera>();
    camera->SetFarClip(1500.0f);
    // Set an initial position for the camera scene node above the ground
    cameraNode_->SetPosition(Vector3(0.0f, 0.0f, 0.0f));

    SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
    renderer->SetViewport(0, viewport);

    // /create character
    Node * characternode_ = scene_->CreateChild("Character");
    characternode_->SetPosition(Vector3(0.0f, 0.0f, 0.0f));

    CreateCharacter();

    loadSceneUI();
[/code]

-------------------------

vivienneanthony | 2017-06-10 21:16:07 UTC | #20

https://www.youtube.com/watch?v=5qLcYEfoI4Q

Updates
1. Added physhics of Urho3D(Bullet) including collisions
2. Refined some textures and better utilized the Blender to Urho3D exporter - Completed
3. Added jump, turn left and right, back and forward movement - Completed
4. Added two camera modes first person and fly mode. - Completed
5. Cleaned up some code

To-Do
1. Add dynamic UI HUD interface in player mode. (Done)
2. Save input from the user
3. Improve terrain texture
4. Optimize better character movement. 
5. Impove character collision bounds - WIP - Created functional code and testing.
6. Create procedual terrain system - WIP -  - Currently working on.
7. Add UI interface with full funcionality - WIP - Added UI graphics adding functionality.

Contact me at [cgprojectsfx@gmail.com](mailto:cgprojectsfx@gmail.com)

-------------------------

vivienneanthony | 2017-06-10 21:16:24 UTC | #21

This is the new video.  I'm going through some of the steps of the terrain creation.

https://www.youtube.com/watch?v=uMYwy7CSLdo

-------------------------

vivienneanthony | 2017-06-10 21:16:36 UTC | #22

This is the newest update.

https://www.youtube.com/watch?v=6HhQGufSFjQ

1. Character creation screen actually creates information for a character

(Sorry. I said the alliances wrong)

Do anyone know how to use github on sourceforge?

-------------------------

gwald | 2017-01-02 01:00:31 UTC | #23

Hey,
I've watched a few of your videos of your project progressing.
Good work!

Re github, there's a lot on it:
[help.github.com/articles/fork-a-repo](https://help.github.com/articles/fork-a-repo)
[wiki.archlinux.org/index.php/Su ... _Git_Guide](https://wiki.archlinux.org/index.php/Super_Quick_Git_Guide)
[stackoverflow.com/questions/3159 ... ical-guide](http://stackoverflow.com/questions/315911/git-for-beginners-the-definitive-practical-guide)

-------------------------

vivienneanthony | 2017-06-10 21:16:51 UTC | #24

Thanks. I'm trying to use sourceforge more in addition to the github.

I placed a lot of code I did online so whoever wants to help can.  My main focus is cleaning up code and polishing what I have already while adding the procedual stuff. (Maybe some mechanics for exploration and object interaction.)

I think a lot of the code can be cleaned up including cutting down memory and unscribing inactive events to increase speed.

https://www.youtube.com/watch?v=xdCw1vyYAT8

-------------------------

gwald | 2017-01-02 01:00:32 UTC | #25

ha SF.net, old school, yeah I would look at migrating to github to get more follows.
I think sf.net is like myspace and github is the facebook  :laughing: 
I'll check it out one day tho.. just stepping through the samples learning urho3D basics.

-------------------------

vivienneanthony | 2017-06-10 21:17:03 UTC | #26

This is the new runtime after a day of serious crashing and adding a GNU debugger GDB to the mix of things.

https://www.youtube.com/watch?v=vL5SZPwUTxM

[b]Additions[/b]
1. Added XML load for the character creation. (Completed)
2. Turned on debugging for the application. (Completed)
3. Added three point lighting to character creation and main screen UI.

[b]Testing[/b]
1. New character and main menu switching.
2. Rotate camera orientation doing character creation.
3. File, procedul generation, and built-in scene loading.
4. Debughud testing.
5. Physics testing.

[b]Additional To-Do[/b]
1. Procedural terrain system update.
2. Gameobject addition and initialization to all game object.
3. Loop through scene objects.
4. Add lifetime to game objects.

[b]Gameplay[/b]
Thinking exploration.

-------------------------

thebluefish | 2017-01-02 01:00:43 UTC | #27

I've been watching some of your videos every now and then, great work so far!

-------------------------

sabotage3d | 2017-01-02 01:00:54 UTC | #28

Keep up the good work :slight_smile:

-------------------------

vivienneanthony | 2017-01-02 01:02:03 UTC | #29

Hello All,

I placed the code at the SF git I think is proteusgameengine. I'm new to Git so if anyone can help me figure it out. It will be appreciated.

[sourceforge.net/u/vivienneantho ... ster/tree/](https://sourceforge.net/u/vivienneanthony/proteusgameengine/ci/master/tree/)

I also placed the code in the SF at [sourceforge.net/projects/proteusgameengine/](https://sourceforge.net/projects/proteusgameengine/) unders the file.

Any help appreciated... The file has the .xmls and .mdl(models).

Vivienne

-------------------------

vivienneanthony | 2017-06-10 21:17:21 UTC | #30

I created a ad hoc lifetime system with some help. A little tweak. Thanks Jtippet and HD.

I've also uploaded the code and models as mentioned. If anyone has a idea of how I can further improve any of it. Feel free to write. This is the code in the video working.
I haven't figure out how to get the projectile to shoot in the direction of the figure.

Something causing the keys to loop because I just tap fire once and dozens of mushrooms shoot!!!!

https://www.youtube.com/watch?v=szPNdDEJdj4

[code]/// Create a object
void Character::MagicBox(void)
{
    /// Get Needed SubSystems
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    Renderer* renderer = GetSubsystem<Renderer>();
    Graphics* graphics = GetSubsystem<Graphics>();
    UI* ui = GetSubsystem<UI>();

    Scene * scene_;

    scene_ = this -> GetScene();

    /// Create Node
    Node * mushroomNode = scene_ -> CreateChild("MushroomNode");
    Node * characterNode = scene_ -> GetChild("Character");

    Vector3 characterPosition = characterNode -> GetPosition();

    /// Get Node position
    mushroomNode->SetPosition(characterPosition+Vector3(0.0f,1.0f,3.0f));

    /// Load mushroom
    StaticModel* mushroomObject = mushroomNode->CreateComponent<StaticModel>();
    mushroomObject->SetModel(cache->GetResource<Model>("Models/Mushroom.mdl"));
    mushroomObject->SetMaterial(cache->GetResource<Material>("Materials/Mushroom.xml"));

    /// Create physics
    CollisionShape* mushroomShape = mushroomNode->CreateComponent<CollisionShape>();
    mushroomShape->SetBox(Vector3::ONE);
    mushroomShape ->SetLodLevel(1);

    RigidBody* mushroomBody= mushroomNode ->CreateComponent<RigidBody>();
    mushroomBody->SetCollisionLayer(1);
    mushroomBody->SetCollisionEventMode(COLLISION_ALWAYS);

    /// Set Lifetime
    GameObject * Lifetime = mushroomNode->CreateComponent<GameObject>();
    Lifetime->SetLifetime(20);

    mushroomBody->	SetMass (.5);
    mushroomBody-> SetLinearVelocity(Vector3(0.0f,0.0f,2.0f));

    return;
}
[/code]

-------------------------

vivienneanthony | 2017-06-10 21:17:34 UTC | #31

Hello All

So I have been cranking away at the client during my free time. I've added several key features:

1) Upgraded to Urho 1.32 
2) Implemented rendering post process effects
3) Revamped the console command system
  a) Added environmental controls such as zones and lighting in /environmental
  b) Created a /debug and /character chain

The reason is I can test environments in game. I  will link the environment building to the same terrain seed generation. I know I will have to do some code removing, rewriting, and adding. I'm hoping to add more environmental controls, ability to place objects in game, save and load generated worlds, and refining everything mentioned before. It's going be a long road.

I still have to create four worlds. I isolated to making rules for 5 worlds, dessert, terrain, ice, water, rock based worlds. Then later I will make some quick assets to define human, alien, or ancient world.

https://www.youtube.com/watch?v=LTE51RvieW4

Still need help but a exploration game would be based.

-------------------------

vivienneanthony | 2017-01-02 01:02:46 UTC | #32

I placed it on Github.

-------------------------

vivienneanthony | 2017-01-02 01:03:01 UTC | #33

This is one third of the assets I made.

[imgur.com/a/AV9mz](http://imgur.com/a/AV9mz)

I'm just trying to figure terrain steepness with texture blend and more detailed displacement of specific terrainpatches.  :neutral_face: The last difficulty in making this to some game.

-------------------------

friesencr | 2017-01-02 01:03:02 UTC | #34

[quote="vivienneanthony"]This is one third of the assets I made.

[imgur.com/a/AV9mz](http://imgur.com/a/AV9mz)

I'm just trying to figure terrain steepness with texture blend and more detailed displacement of specific terrainpatches.  :neutral_face: The last difficulty in making this to some game.[/quote]

I really like the larger trees.  It sits well between having a painterly/artistic style and would work well in a photo realistic setting.

-------------------------

vivienneanthony | 2017-06-10 21:17:49 UTC | #35

This is a tidy video of whats new. Feel free to contact me, although it looks simple there is a lot of things happening so the game can grow.

https://www.youtube.com/watch?v=m48OTA5qtRM

-------------------------

vivienneanthony | 2017-01-02 01:03:47 UTC | #36

I got a seed based system to work. To see go here [imgur.com/a/FdWXC](http://imgur.com/a/FdWXC)

Bonus is a proceduralterrain logiccomponent so saving, loading, and massive multiterrain implementation procedural.

The first two pictures was generated a half hour apart and the last two days later using the same seed number.

The seed is 18556, world 50, subtype 0, and sealevel 0. Thats all needed. Im going terrain size detection to the component.

The grass uses the standard c# random implementation thats why the size different.

-------------------------

