GodMan | 2020-03-14 22:22:49 UTC | #1

So I have a Character class that has a private variable` int health` in my Projectile class I have this:
```
if (resultNode->HasComponent<Character>())
{
    _Node = resultNode->GetComponent<Character>();
    _Node->setHealth(_Node->getHealth() - damage);
}
```
It works fine I just feel like my code is not efficient.

-------------------------

SirNate0 | 2020-03-14 19:48:32 UTC | #2

If it's about writing it with less text:
```
auto character = resultNode->GetComponent<Character>();
if (character)
{
    _Node = character;
    _Node->setHealth(_Node->getHealth() - damage);
}
```

-------------------------

GodMan | 2020-03-14 19:50:58 UTC | #3

@SirNate0 Looks a lot cleaner, and easier to read.

-------------------------

SirNate0 | 2020-03-14 19:53:14 UTC | #4

If you don't need to keep the last Character you can shorten it even more, though at the cost of some readability
```
if (_Node = resultNode->GetComponent<Character>())
    _Node->setHealth(_Node->getHealth() - damage);
```

-------------------------

GodMan | 2020-03-14 21:23:51 UTC | #5

I need to come up with a good method for and AI that has died. If the AI health hits zero play the death animation then remove the CrowdAgent from that node. 

Is there a way to remove everything from the node, but not delete the model just yet. My ideas have not worked very well. I can get the AI to die then play the death animation, but the CrowdAgent keeps affecting the node.

-------------------------

Modanung | 2020-03-14 22:26:08 UTC | #6

A more generalized approach would be to use `GetDerivedComponent<Character>()`. This way components that derive from `Character` would also receive damage.

-------------------------

JTippetts | 2020-03-15 20:09:07 UTC | #7

The way I usually handle this is to have the dying AI object spawn a separate object to play the death animation, then mark itself for deletion. That way the death animation object has no residual components that are no longer relevant, such as crowd agents or physics objects. If you need to track anything from the AI (corpse data, ie for spells that consume corpses Diablo-clone-style) just pass that through a special component attached to the death object.

-------------------------

GodMan | 2020-03-16 02:26:24 UTC | #8

Won't this have a strange affect though? Like a random spawning character model that plays the death animation, but the previous model instantly disappearing. Wouldn't that be really noticeable though?

-------------------------

SirNate0 | 2020-03-16 02:33:51 UTC | #9

Not if they start from the same point in the animation. Both approaches are effectively the same, it's just different based on the actual setup you have for your game - with your idea you remove some components and leave others, with JTippetts' you create a new node and copy a few essentials (models/poses/etc) as needed (which could be nothing depending).

Regarding your request, can I ask why you want to leave the CrowdAgent until after death?

-------------------------

GodMan | 2020-03-16 02:46:55 UTC | #10

I don't want to keep it after death. Problem I was having when my npc dies the crowd agent was still active.

-------------------------

SirNate0 | 2020-03-16 03:27:14 UTC | #11

Can you just remove or disable that component?

-------------------------

GodMan | 2020-03-16 03:28:47 UTC | #12

I tried disabling the agent, but that did not work.

-------------------------

GodMan | 2020-03-18 03:51:57 UTC | #13

Like to post I fix this. I have it were my AI class templates fix this issue.

-------------------------

