Spongeloaf | 2019-08-30 22:24:40 UTC | #1

This is my first game project, coming from a world of scripting and microcontroller programming. This is reasonably different than anything I've done before. I need a sanity check, please.

My game is all in 2d. It has a few basic types of objects. Planets, space rocks, missiles, and explosions. I'm using a custom component called "Actor" to store information and set basic behaviors.

For example, if a missile collides with a planet, it should simply be destroyed. If a missile collides with a space rock, it detonates and pushes the rock with a physics force. If a missile collides with a detonation, it should also be pushed, but not detonated. There are a few more basic behaviors but that's enough for now.

I'm concerned that the way I'm handling these different cases is clunky and over-thought. I'm handling collision events by subscribing to `E_PHYSICSBEGINCONTACT2D`, `E_PHYSICSUPDATECONTACT2D`, and `E_PHYSICSENDCONTACT2D`. 

I call a function and pass in eventtype & eventdata, and unpack the roles as follows:

```
Node* na = static_cast<Node*>(eventData[P_NODEA].GetPtr());
Node* nb = static_cast<Node*>(eventData[P_NODEB].GetPtr());

Actor* aa = na->GetComponent<Actor>();
Actor* ab = nb->GetComponent<Actor>();
	
Roles ra = aa->get_role();
Roles rb = ab->get_role();
```

Then I pass them through a matrix of if-statements. This is the part I fear is clunky and over thought. The following example is just two cases, but there are at least 25 of them, and it goes up exponentially if I add more roles. Because in any collision between two different nodes, either one may be A or B, I need two cases for a missile colliding with a rock. (NODEA == missle && NODEB == rock) or (NODEA == rock && NODEB == missile).

Here's what that looks like:

```
// Roles are enums. 
// There are currently 25 of these if statements to cover all cases 

if ((ra == Roles::ROCK) && (rb == Roles::MISSILE))
{
	// detonate missile
}

if ((ra == Roles::MISSILE) && (rb == Roles::ROCK))
{
	// detonate missile
}

if ((ra == Roles::ROCK) && (rb == Roles::ROCK))
{
	// do nothing. The physics engine will handle bouncing.
        // There's only a few "Do nothing" cases. I could get rid of them, but it would not trim a lot of fat
}
```
Of course that could be condensed to only one if statement with a few extra parentheses thrown in there, but I'm just not sure I like this solution. The problem is I can't see any other effective method. If I add another role, that makes the number of if statements skyrocket because I have N^2 cases. It works, but it seems very.............derpy. 

Is this a reasonable solution? Would you question my sanity if you saw this in production? Do you have some other ideas? Is there some feature of the engine to facilitate this procedure that I'm not aware of? Should I just shutup and get back to work?

-------------------------

throwawayerino | 2019-08-30 21:08:08 UTC | #2

What I do is have them all inherit from a common parent (Actor in your case) and call a virtual function *in the collision event\* that takes a role as parameter `virtual void Actor::OnCollide(Roles ColliderRole)`. Having an if else chain isn't a bad choice if you don't plan to add more roles, but if you do plan then having virtual functions is easier

-------------------------

glitch-method | 2019-08-30 23:20:07 UTC | #3

too new to give a good code example, but it seems fairly sane considering all roles are being treated as an Actor. you can't get away from some kind of elaborate matrix where you list out how roleA should behave with roleXYZ, but you may be able to make it "neater"... I may do something like what @throwawayerino mentioned, and/or maintain an array, couple options there... an Nx3 array (role, role, result), so your if block becomes something like 
[code]
    for n in array:
        arrayA = array[n,1]
        arrayB = array[n,2]
        if (roleA = arrayA & roleB = arrayB]) or (roleB = arrayA & roleA = arrayB) then
            return array[n,3]
    next
[/code]
then you'd have to maintain the array by adding an array[n+1, (new role, arrayA, new result)] for each unique arrayA.
or -
an XxX array containing only results, like
[code]return = array[roleA, roleB][/code]
then maintain by adding array[new role, roleB] for each unique roleB,
and adding array[roleA, new role] for each unique roleA.

i'm not sure which would end up messier or bloated if you're going to add a lot of roles, though. and like I said, i'm new... so someone else could probably give you a neater solution. just seemed worth mentioning.

edit: formatting, iguess my phone doesn't like me.

-------------------------

Sinoid | 2019-08-30 23:52:43 UTC | #4

Are you just ignoring sequencing? You can deal with Rock vs Missle and Missle vs Rock in one go by ordering your sides.

```
// sort keys so tests are invariant to parameter sequence
if (roleB < roleA)
{
    swap(roleA, roleB);
    swap(actorA, actorB);
}
```

It's generally easier to just use a table of function pointers with a *key* object for this sort of callback lookup. Using a proper key instead of some if statements makes it easier to deal with the `leftSide = min(roleA, roleB), rightSide = max(roleA, roleB)` you'll need to do if you want to be invariant to sequence, you deal with it once and never deal with it again - instead of every `if` statement needing to be in the correct order.

-------------------------

Spongeloaf | 2019-08-31 17:51:28 UTC | #5

Damn, I like this. 

I hadn't thought of sorting them by comparison, but that should work implicitly if I'm using an enum class right? If so, I'll definitely keep the role matrix, as @glitch-method agrees it's necessary in some capacity, but this will drastically cut down on the umber of cases. Thanks!

-------------------------

Modanung | 2019-08-31 22:35:58 UTC | #6

In [heXon](https://gitlab.com/luckeyproductions/heXon) I just used things like `if (otherNode->HasComponent<T>())` and `GetDerivedComponent<Enemy>()` inside `NodeCollisionStart` event handlers. It worked for me, and keeps the logic where it happens. I don't know about the computational difference, the game *is* aptly named _hack zone_.
Since there's a constant race for the pickups in the case of multi-player, it may happen two ships hit a pickup during the same frame. Distances are therefor also taken into account to assure fairness.

-------------------------

Spongeloaf | 2019-09-03 14:42:23 UTC | #7

@Modanung 
The only reason I haven't done the same is that most of my components are re-used among actors, and certain combinations of components need to be handled differently. 

I could also make more bespoke components, but I think this is less work for a similar result, in my case anyway.

-------------------------

George1 | 2019-09-04 03:25:16 UTC | #8

Similar to navigation problem.
Add index to all your component role types.

Add a 2D matrix as lookup table for your role index components.  Then label 0,1, 2 etc.

This should reduce your combinations of if.

Then just return the lookup value and call the respected function.

e.g.

NORMAL = 0
DETONATE = 1
OTHER = 2

collisionType = LookUpCollisionType( ra.index, rb.index);

switch(collisionType )
case NORMAL:
    DoNormalThing()
case DETONATE:
    ExplodeThing()
case OTHER:
   DoOtherThing()

-------------------------

extobias | 2019-09-05 10:52:13 UTC | #9

I think this maybe is related to what I've working. It's not finished yet, but the idea is to store different collision info in the same model. Maybe it should use a different model file with only the collision info per-vertex (tips are welcome), but this is not decided. For now just use the color vertex.

![output|320x166](upload://eJKMX8ReOvSqhoDPLUdnskxVjt9.gif)

-------------------------

Modanung | 2019-09-05 13:57:48 UTC | #10

That seems more like a way to vary friction. An interesting concept nonetheless.

-------------------------

extobias | 2019-09-05 21:56:21 UTC | #11

I've never think it that way :thinking:. Found some interesting wiki about mario kart collision (http://wiki.tockdom.com/wiki/KCL_(File_Format)) and tried to replicate with Urho3D. Maybe could create a special file format for collision. I like the idea of having one model with different collision flags.

-------------------------

Modanung | 2019-09-06 10:18:35 UTC | #12

I guess this method makes most sense in gastropodic settings. :snail: 
Note that in Mario Kart there are cases where you can land off-track and be return by Lakitu. In these cases there is no wall collision, only invalid areas. Also karts don't roll. I'd say it's quite a specialized approach: Powerful (fast and watertight), but with limited applicability. Although I guess you _could_ equip any model with vertex colors...

Maybe you could make a repository for this experiment to inspire people to be creative with vertex colors?

-------------------------

glitch-method | 2019-09-06 10:47:40 UTC | #13

I like the possibilities of this approach.

-------------------------

Leith | 2019-09-20 07:38:37 UTC | #14

@ karts don't roll - in these kinds of action games, roll is clamped to a limited range, this is also true of games like Tony Hawk variants, we can't flip upside down, but things can get exciting. Limiting the range of roll helps us reduce our workload as game devs, because we don't need to consider what happens if we land on our roof, which adds to the sense of continuity and ease of use, and reduces side effects associated with inertial frames of reference

-------------------------

