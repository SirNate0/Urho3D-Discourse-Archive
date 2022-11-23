Modanung | 2017-01-17 17:35:54 UTC | #1

# heXon

#### FOSS TWIN-STICK-SHOOTER
https://vimeo.com/162301414
**Binaries:**
[heXon on itch.io](https://luckeyproductions.itch.io/hexon)

**Source:**
[heXon on GitHub](https://github.com/LucKeyProductions/heXon)

**Pickups:**
_Golden apple_ / Provides 23 points. Collect 5 apples in a row to get weapon upgrades. Picking up a Heart breaks the count.
_Heart_ / Heals half of your max life. Collect 5 hearts in a row to get a shield upgrade. Picking up an Apple breaks the count.

_MultiX_ / Increases your score multiplier.
_ChaoBall_ / Turns enemies into useful ChaoMines and disrupts Seekers

**Enemies:**
_Razors_ / Mostly harmless in small numbers. Don't fly into them though. 5 points on destruction.
_Spires_ / These sturdy towers launch Seekers; player seeking foo fighters that should be evaded. 10 points when obliterated.

**Noteworthy:**
Explosions repel most objects.
Reaching the end of the net will send most objects to the opposite side.

**Controls:**
heXon is best played using a dual stick controller and was developed and tested with Sony PS3 SIXAXIS controllers on Xubuntu and Linux Mint.

Keyboard controls are as such:
Movement / WASD
Firing / IJKL or the numpad
Pause / P

-----

**Tools:**
Urho3D, QtCreator, Blender, Inkscape, GIMP, SuperCollider, Audacity and more (All FOSS)

**Soundtrack:**
Alien Chaos - Disorder
from [Discovering the Code](http://www.ektoplazm.com/free-music/alien-chaos-discovering-the-code)

-------------------------

sabotage3d | 2017-01-02 01:05:45 UTC | #2

Awesome work ! Looks really cool I will try it tonight.

-------------------------

Modanung | 2017-01-02 01:05:45 UTC | #3

It did just occur to me I made some engine modifications that are yet unpushed. Will try to fix that.

-------------------------

sabotage3d | 2017-01-02 01:05:45 UTC | #4

Yeah I am having some problems building it. Is there anything special I need to do in order to build it ?

-------------------------

Modanung | 2017-01-02 01:05:45 UTC | #5

Are you using QtCreator for the build process?
Did you SymLink/Copy the Data, CoreData and Resources folders?

Are you getting any [i]undefined method[/i] errors?

-------------------------

sabotage3d | 2017-01-02 01:05:45 UTC | #6

The errors are not related to the resources. I think you have added modifications to the engine.
These are the errors:

[code]mastercontrol.h:119:59: No member named 'Length' in 'Urho3D::Vector<double>'
mastercontrol.h:119:70: Use of undeclared identifier 'Cycle'
mastercontrol.h:120:57: No member named 'Length' in 'Urho3D::Vector<double>'
mastercontrol.h:120:68: Use of undeclared identifier 'Cycle'
arenaedge.cpp:43:16: No matching member function for call to 'SetScale'
arenaedge.cpp:44:34: Too many arguments to function call, expected single argument 'position', have 3 arguments
arenaedge.cpp:79:9: No member named 'Distance' in 'Urho3D::Vector3';
arenaedge.cpp:79:27: No viable conversion from 'Urho3D::Vector3' to 'const btVector3'[/code]

-------------------------

Modanung | 2017-01-02 01:05:46 UTC | #7

[quote="sabotage3d"]The errors are not related to the resources. I think you have added modifications to the engine.[/quote]
Correct.

[code]mastercontrol.h:119:59: No member named 'Length' in 'Urho3D::Vector<double>'[/code]
Is fixed by adding the following to VectorBase.h:
[code]unsigned Length() {return size_;}[/code]
[code]mastercontrol.h:119:70: Use of undeclared identifier 'Cycle'[/code]
Is fixed by adding the following to MathDefs.h:
[code]/// Return the cycled value of a float
inline float Cycle(float value, float min, float max)
{
    float cycled = value;
    float range = max - min;
    if (cycled < min) {
        cycled += range * abs(ceil((min - cycled) / range));
    }
    else if (cycled > max) {
        cycled -= range * abs(ceil((cycled - max) / range));
    }
    return cycled;
}
/// Return the cycled value of a double
inline double Cycle(double value, double min, double max)
{
    double cycled = value;
    double range = max - min;
    if (cycled < min) {
        cycled += range * abs(ceil((min - cycled) / range));
    }
    else if (cycled > max) {
        cycled -= range * abs(ceil((cycled - max) / range));
    }
    return cycled;
}
/// Return the cycled value of an int
inline int Cycle(int value, int min, int max)
{
    int cycled = value;
    int range = max - min;
    if (cycled < min) {
        cycled += range * abs(ceil((min - cycled) / range));
    }
    else if (cycled > max) {
        cycled -= range * abs(ceil((cycled - max) / range));
    }
    return cycled;
}[/code]

[code]arenaedge.cpp:79:9: No member named 'Distance' in 'Urho3D::Vector3';
arenaedge.cpp:79:27: No viable conversion from 'Urho3D::Vector3' to 'const btVector3'[/code]
Should both be fixed by adding the following to Vector3.h:
[code]/// Return length of difference vector
    static float Distance(const Vector3& lhs, const Vector3& rhs) { return (lhs-rhs).Length(); }[/code]

[code]arenaedge.cpp:43:16: No matching member function for call to 'SetScale'
arenaedge.cpp:44:34: Too many arguments to function call, expected single argument 'position', have 3 arguments[/code]
Should be fixed with latest heXon commit.

I know this is not the way to do things. I'm still finding out what is.

-------------------------

sabotage3d | 2017-01-02 01:05:46 UTC | #8

There are still a lot of issues.
There are a lot of 3 floats where they should be Vector3 . Some of the function calls are ambigious as there are mixes of floats and doubles. 
There is a missing define for M_TAU . After fixing a lot of these I tried to compile but I started getting. A lot of incomplete return types to 'Urho3D::URHO3D_API' .
This is the complet error list after fixing the small things: [codepad.org/Pusn3B6Y](http://codepad.org/Pusn3B6Y)
At the end I gave up, as I am not sure what is causing the issue.

-------------------------

thebluefish | 2017-01-02 01:05:47 UTC | #9

[quote="sabotage3d"]There are still a lot of issues.
There are a lot of 3 floats where they should be Vector3 . Some of the function calls are ambigious as there are mixes of floats and doubles. 
There is a missing define for M_TAU . After fixing a lot of these I tried to compile but I started getting. A lot of incomplete return types to 'Urho3D::URHO3D_API' .
This is the complet error list after fixing the small things: [codepad.org/Pusn3B6Y](http://codepad.org/Pusn3B6Y)
At the end I gave up, as I am not sure what is causing the issue.[/quote]

That's usually caused by a missing #include <Urho3D/Urho3D.h>, but that seems to be included in the headers already. There may be some non-standard stuff going on, and at the very least I'd recommend throwing in some header guards instead of solely relying on #pragma once.

-------------------------

Modanung | 2017-01-02 01:05:47 UTC | #10

[quote="sabotage3d"]There are a lot of 3 floats where they should be Vector3 . Some of the function calls are ambigious as there are mixes of floats and doubles.[/quote]
Most of this should be fixed a few commits ago.
[quote]There is a missing define for M_TAU.[/quote]
Stopped using that as well with the latest commit.
[quote]At the end I gave up, as I am not sure what is causing the issue.[/quote]
Thanks for the effort.

Fixed the header guards.

-------------------------

sabotage3d | 2017-01-02 01:05:47 UTC | #11

In you latest commits these are still errors which are easy to fix. After fixing those there are still the previous issue with the incomplete type. It is super weird because If I call Rand() in a clean project everything works fine.
[codepad.org/0kvVf6df](http://codepad.org/0kvVf6df)

[code]arenaedge.cpp:44:34: Too many arguments to function call, expected single argument 'position', have 3 arguments
enemy.cpp:49:84: Call to 'Max' is ambiguous
explosion.cpp:37:18: Non-constant-expression cannot be narrowed from type 'double' to 'float' in initializer list
explosion.cpp:82:25: Call to 'Max' is ambiguous
explosion.cpp:83:27: Call to 'Max' is ambiguous
flash.cpp:51:27: Call to 'Max' is ambiguous
player.cpp:108:39: Too many arguments to function call, expected single argument 'position', have 3 arguments
player.cpp:109:21: No matching member function for call to 'SetScale'
player.cpp:115:39: Too many arguments to function call, expected single argument 'position', have 3 arguments
player.cpp:116:21: No matching member function for call to 'SetScale'
player.cpp:122:44: Too many arguments to function call, expected single argument 'position', have 3 arguments
player.cpp:131:59: Too many arguments to function call, expected single argument 'position', have 3 arguments
player.cpp:142:56: Too many arguments to function call, expected single argument 'position', have 3 arguments
player.cpp:181:52: Call to member function 'Sine' is ambiguous
player.cpp:183:52: Call to member function 'Sine' is ambiguous
player.cpp:331:37: Call to 'Clamp' is ambiguous[/code]

-------------------------

sabotage3d | 2017-01-02 01:05:48 UTC | #12

The problem was with the multiple includes in your source files to the Urho3d headers. I fixed it in a working states there is only one thing I can't figure out
There is a problem here:
[code]tileMap_[IntVector2(i, j)] = new Tile(context_, this, tilePos);[/code]
Which gives this error:
[code]/DEV/libs/Urho3d-1.40mod/Source/Urho3D/Container/Hash.h:45:18: No member named 'ToHash' in 'Urho3D::IntVector2'[/code]
I made temporary fix which is wrong but atleast it compiles. 

These are my changes: [github.com/sabotage3d/heXon/com ... feb45f7197](https://github.com/sabotage3d/heXon/commit/a488c3854f804fab86e810567df9e2feb45f7197)

-------------------------

att | 2017-01-02 01:05:49 UTC | #13

[quote="sabotage3d"]The problem was with the multiple includes in your source files to the Urho3d headers. I fixed it in a working states there is only one thing I can't figure out
There is a problem here:
[code]tileMap_[IntVector2(i, j)] = new Tile(context_, this, tilePos);[/code]
Which gives this error:
[code]/DEV/libs/Urho3d-1.40mod/Source/Urho3D/Container/Hash.h:45:18: No member named 'ToHash' in 'Urho3D::IntVector2'[/code]
I made temporary fix which is wrong but atleast it compiles. 

These are my changes: [github.com/sabotage3d/heXon/com ... feb45f7197](https://github.com/sabotage3d/heXon/commit/a488c3854f804fab86e810567df9e2feb45f7197)[/quote]


Try adding following in IntVector2.h
unsigned ToHash()
{
      return ToString().ToHash();
}

I think it will work. :smiley:

-------------------------

sabotage3d | 2017-01-02 01:05:49 UTC | #14

Thanks it works but it needs const.
[code]
    unsigned ToHash() const
    {
        return ToString().ToHash();
    }[/code]

-------------------------

Modanung | 2017-01-02 01:05:54 UTC | #15

[quote="att"]Try adding following in IntVector2.h
unsigned ToHash()
{
      return ToString().ToHash();
}[/quote]

I only have a Vector2.h (no IntVector2.h) and within the class definition of Intvector2 it has this line:
[code]/// Return hash value for HashSet & HashMap.
unsigned ToHash() const { return (MakeHash(x_) & 0xffff) | (MakeHash(y_) << 16); }[/code]
...which I somehow expect to do a better job.

@Sabotage3D: The tileMap_ HashMap uses IntVector2 keys for checking neighbouring tiletypes when semi-auto mapping. This doesn't happen in heXon yet, but it does in another LucKey Production called [url=https://github.com/LucKeyProductions/MastersOfOneiron]Masters of Oneiron[/url] from where I reused the code. At the moment heXon only uses the values of the HashMap to pick a random tile as a spawn point. Using only one of the iterators instead of the hashed IntVector2 as key will, I expect, make all enemies and pickups (re)spawn below the left edge of the arena.

-------------------------

Modanung | 2017-01-02 01:06:00 UTC | #16

The code has been changed so that it should compile with default Urho3D.

-------------------------

sabotage3d | 2017-01-02 01:06:00 UTC | #17

I think your chages would be a nice addition to the engine. Maybe you can try and push some of them to the main branch.

-------------------------

Modanung | 2017-01-02 01:06:02 UTC | #18

The Length() method turned out to be useless. It was the more aptly named Size() I was looking for. But indeed I intend to submit the other changes as pull requests to the Engine. I'm still learning git as well, requesting pulls requires steps I didn't take before.
Did you get heXon to compile btw? There is no in-game settings screen as of yet; the resolution is set in mastercontrol.cpp.

-------------------------

att | 2017-01-02 01:06:02 UTC | #19

I had compiled it for mobile, but it always crash sometimes.

-------------------------

Lumak | 2017-01-02 01:06:24 UTC | #20

I built this game in Windows and played it a bit.

I did have a crash issue whenever I fired a bullet, but it was an easy fix.  Just add a distance check in:
[code]
bool MasterControl::PhysicsRayCast(PODVector<PhysicsRaycastResult> &hitResults, Ray ray, float distance, unsigned collisionMask = M_MAX_UNSIGNED)
{
    if ( distance > 1e-9f )
    {
        physicsWorld_->Raycast(hitResults, ray, distance, collisionMask);
    }

    return ( hitResults.Size() > 0 );
}

[/code]

fix the issue and I was able to play it.

I really like the feel of this game.  Good luck finishing it.

Edit: There are a couple of optimization issues that you might want to address: 1) there's often a frame rate lag whenever, I guess, objects spawn in the world.  If all objects were pre-cached, this problem would go away. 2) the ray cast, or any collision for that matter, could be limited to run at 32 msec interval and it'll still be okay. Urho3D's tick is 10msec interval so, it might bog your game down a bit.

Edit2: Just stepped through bt ::stepSimulation() and the timeStep is actually 0.039 secs, so it looks like Urho3D processes collision at a good interval.

-------------------------

Lumak | 2017-01-02 01:06:25 UTC | #21

There was another crash issue that always occur during bt collision process after you kill an enemy.

Not sure if you guys already fixed it, but that one was an easy fix as well.

-------------------------

Lumak | 2017-01-02 01:06:26 UTC | #22

Here is the fix for a crash that happens in bt collision manifold creation process.  Crash caused by negative [b]NaN[/b] (-1#IND).
Changes in explosion.cpp (not in its entirety, just the key part):
[code]
void Explosion::UpdateExplosion(StringHash eventType, VariantMap& eventData)
{
. . .

                if (!hitResults[i]->IsTrigger())
                {
                    Vector3 v3DeltaPos = hitResults[i]->GetNode()->GetWorldPosition() - rootNode_->GetWorldPosition();
                    float fDist = radius - v3DeltaPos.Length();
					     Vector3 v3Force = v3DeltaPos * sqrt( fabs(fDist) ) * timeStep * 500.0f * rigidBody_->GetMass();
                    hitResults[i]->ApplyForce( v3Force );

                    //Deal damage
                    unsigned hitID = hitResults[i]->GetNode()->GetID();
                    float damage = rigidBody_->GetMass()*timeStep;
                    if(masterControl_->spawnMaster_->spires_.Keys().Contains(hitID)){
                        masterControl_->spawnMaster_->spires_[hitID]->Hit(damage, 1);
                    }
                    else if(masterControl_->spawnMaster_->razors_.Keys().Contains(hitID)){
                        masterControl_->spawnMaster_->razors_[hitID]->Hit(damage, 1);
                    }
                }
. . .
}
[/code]

[b]the square root of a negative number causes negative NaN[/b].  While [b]fabs()[/b] insures positive value, I'm not sure if you meant to do this:
[code]
Vector3 v3Force = v3DeltaPos * sqrt(  fDist * fDist ) * timeStep * 500.0f * rigidBody_->GetMass();
[/code]
taking the square root of distance squared.

Anyways, I really like the game.  I hope to see it on Steam and other platforms!

-------------------------

Modanung | 2017-01-02 01:06:27 UTC | #23

Thanks for the informative improvements. Any contribution is highly appreciated.
Steam is not one of my targets, but if they allow GPL software to be distributed at no charge feel free to make your wish come true.

-------------------------

sabotage3d | 2017-01-02 01:06:31 UTC | #24

Thanks for updating the game, I am really enjoying it. The only thing I had to change was FXAA3 to FXAA3 as it doesn't work properly on my machine. 
One small thing at the moment there is no way to exit the game, apart from that I haven't ran into any issues. 
I saw you have some other games as well is there anything playbale at the moment ?

-------------------------

rasteron | 2017-01-02 01:06:31 UTC | #25

I remember playing a similar game but with pc viruses and bots (forgot the title)

Looks awesome so far! :slight_smile:

-------------------------

Modanung | 2017-01-02 01:06:40 UTC | #26

[quote="sabotage3d"]Thanks for updating the game, I am really enjoying it. One small thing at the moment there is no way to exit the game[/quote]
Cool! :mrgreen:
Walking out into the darkness exits the game. This will probably be more clearly hinted at in the future.
[quote="sabotage3d"]I saw you have some other games as well is there anything playable at the moment ?[/quote]
h?X?n is is the only project with significant functional gameplay. Masters of Oneiron, KO and OG Tatt might narrowly count as primitive sandboxes but maybe "proof of name" is a more fitting term for their current stage of development. :confused:
Since a few days KO loads [url=http://www.mapeditor.org]Tiled[/url] TMX maps and turns them into a 3D level, which I think is pretty neat. It's a method I'll definitely use more often. Dungeon::InitializeFromMap does the TMX parsing.
The next three weeks I'll be diving into a [url=https://github.com/Modanung/Finchy]scientific model visualization project utilizing Urho3D[/url].

-------------------------

