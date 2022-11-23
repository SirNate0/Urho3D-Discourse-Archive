vivienneanthony | 2017-01-02 01:02:30 UTC | #1

Hey

Did anyone get any player to shoot a bullet or object? I'm looking over the Ninja code for a example but the  obvious answer I'm not seeing.

This is the code I'm tryiing. No matter what direction or rotation. It seems not to set and shoots in he same direction even if the character is turned around. 

I would like some flying mushrooms. Kidding.

Vivienne



[code]    /// Create Node
    Node * mushroomNode = scene_ -> CreateChild("MushroomNode");
    Node * characterNode = scene_ -> GetChild("Character");

    Vector3 characterPosition = characterNode -> GetPosition();
    Quaternion characterRotation = characterNode-> GetRotation();

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
    mushroomNode-> SetRotation(characterRotation);
    mushroomNode-> Translate(Vector3::FORWARD*2.0f);[/code]

-------------------------

rasteron | 2017-01-02 01:02:31 UTC | #2

I have tried this before and honestly it is quite easy if you examine carefully the NSW Demo. You can change physics variables like respawn time, velocity, bounce etc. to simulate bullets instead of snowballs. Try also checking for direction and node points where the projectile is coming from.

-------------------------

setzer22 | 2017-01-02 01:02:34 UTC | #3

Also, this might be a bit offtopic, but bear in mind that (fast-traveling)bullets are not usually made using RigidBodies in videogames. Raycasting is used instead. 

It's very difficult to have an object moving as fast as a real bullet and not cause any physics-related bug.

-------------------------

vivienneanthony | 2017-01-02 01:02:35 UTC | #4

[quote="setzer22"]Also, this might be a bit offtopic, but bear in mind that (fast-traveling)bullets are not usually made using RigidBodies in videogames. Raycasting is used instead. 

It's very difficult to have an object moving as fast as a real bullet and not cause any physics-related bug.[/quote]
Oh. Hmmm.

-------------------------

rasteron | 2017-01-02 01:02:36 UTC | #5

[quote]Also, this might be a bit offtopic, but bear in mind that (fast-traveling)bullets are not usually made using RigidBodies in videogames. Raycasting is used instead.

It's very difficult to have an object moving as fast as a real bullet and not cause any physics-related bug.[/quote]

I have tried Urho with the Ninja Demo and spawning 60-80 entities at one time. 20 of them are firing at my character on different intervals and I have setup to have my projectile fire at a very rapid rate and the performance is still good :slight_smile:

I wish I recorded a video of that mod but I could try and replicate it again when I have the time..  :bulb:

-------------------------

devrich | 2017-01-02 01:02:37 UTC | #6

How I have done bullets or other projectiles before is use a stretched out invisible box to approximate the size and shape of the bullet/projectile.  Enable physics on that invisible box and disable physics on the mesh of the bullet/projectile while ensureing that they share the same pos/rot/scale either by attachment or by manually changing their pos/rot/scale.

Then I just calculate the distance per frame that the bullet/projectile will be travel during that frame and do a raycast call for from the front of the bullet/projectile to that distance +/- ( usually + ) 0.01meters in the vector direction of the bullet/projectile's flight path.

By enabling physics on the stretched out invisible box -- we allow other bullets/projectiles and other raycast calls to be able to "hit" the bullet/projectile and then send to the bullet/projectile to destroy it because it got hit by something _instead_ of it hitting it's target.  This allows for nice effects such as players in a multi-player setting to destroy incoming missles or in a flight simulator setting to fly close to the bullet/projectile as a means to "intercept" it and save the day.

just my 2 cents of experience :slight_smile:

-------------------------

