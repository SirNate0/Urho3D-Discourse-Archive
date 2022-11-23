microface | 2017-01-02 01:15:07 UTC | #1

Please forgive my poor English.
I have some problems with my skill system in my game. Actually, I just do not know how to realize my skill system(in RPG-like games).  
Unlike the inventory system, each skill is a class (which derives from LogicComponent) rather an object. So I need a container to store my character's skills. This container cannot be defined as something like 'Vector<Skill*>' as it should contain a bunch of classes rather than objects. So how can I just store a bunch of classes in a structure ?
What I really want to ask is that how do you guys(No offense. I have no idea is it a polite statement or not.) build your skill systems?
THANKS!

-------------------------

Sir_Nate | 2017-01-02 01:15:08 UTC | #2

I  would either go with not using a separate class for each, or use an instancer. Have another class that returns a logic component based on the type, and either use a switch statement to return the class needed, or have a templatized instancer driving from a common parent that stores returns the class, and store them in a hash map (the same way the context instances new classes once you've registered the factory).

As to your latter question, I have a single class for my skills, which then uses either a timeline for the effects (you can define your own events, and then just read them from the timeline and use the event data as needed), my own timeline format, out a script object with a few pre-defined methods. I want to keep my game mod-able, though, so I am willing to take the small performance hit from this as compared to native code.

If you want to keep using separate classes, you can try what I've described above, and there is also some class information stuff in the newer versions of CPP. I also did what you are trying in an earlier iteration, but I abandoned it. I can pull out that code and look at exactly what I did if you would like, though.

-------------------------

microface | 2017-01-02 01:15:08 UTC | #3

Um, is that to say what I need to do is to realize all the skills in only one class and trigger them according to specific input? Actually, I do not catch your meaning which using a timeline for the effects. Is not timeline just a tool for realizing animation? How can you realize the skill logic with it? 

Sorry that I may not follow you quite well. Could you please speak a little more clearly or maybe show me some of your codes ?

-------------------------

Sir_Nate | 2017-01-02 01:15:08 UTC | #4

It depends on what you are trying to do. 
1) Are these skills 'attacks' that are used at specific times (based on user input) and then are finished or are they passive things (you gain them, and then you get, e.g. an experience bonus whenever you kill something)?
2) Is your game a turn-based RPG (like Pokemon, Dragon Quest, etc.) or a real time one (think Zelda, perhaps the Tales of ____ games (I don't really remember the combat in them though))?

Attacks + Real time
--you will need something like a timeline, as the attacks will have to move in certain ways and initiate their effects at certain times
Attacks + Turn based
--you can probably do you system the same way you do items -- skill have float damage, chanceOfHitting, chanceOfStatusCondition; int numberOfHits; enum STATUS_CONDITION; enum TYPE; float sp/mp/mana/___Cost;
Passive + Real time
--you probably just need an Object or Component, not a LogicComponent, as most of them will probably just respond to specific events (E_ENEMY_KILLED, etc.) and not to the general Update, FixedUpdate, etc. events
Passive + Turn based
--these can probably be realized as 2 functions -- an applySkill(Character) that adjusts current stats and such and a removeSkill(Character) that un-does that change, but that is up to you.

My game falls in to the Attacks+Real time, hence the timeline, but I also have abilities that fall into passive+real time, for which I use a script object (so basically a logic component).

If you need a container just to store which skill you have, just use a Vector<String> or Vector<StringHash> to store the name(hash) of the class and instantiate from the context as needed. You'll just have to register each as a factory (context_->RegisterFactory<Attack>();//replace Attack with each of your skill classes in turn). If you need a pointer to the objects of each class, use a Vector<LogicComponent*> to store them (you should probably use WeakPtrs or SharedPtrs though).

If you provide more details, I can try to give more specific feedback.

-------------------------

microface | 2017-01-02 01:15:09 UTC | #5

It's a real-time shooting online-game which is something like [i]OverWatch[/i]. Each player can choose a character and choose skills(both active and passive) to carry before one round starts. So I need a interface with which I can change one's skills after a round.

Active ones are something that one can trigger by its input while passive ones are just something like a buff which always impacts the character during one round.

e.g. One of the skills is something like that launching a missile, then it will follow anyone else who else is within its tracking range. 

Also other ones like launching a rocket which can trigger a debuff on someone it hitted.

-------------------------

Sir_Nate | 2017-01-02 01:15:11 UTC | #6

I would go with just a vector of Strings then. Have all of your skills be logic components (or perhaps a class derived from logic component, which would allow you to have functions like GetDescription() and GetImage(), etc. for the skills (things you know most every one of them should have). You can then instantiate them with Context's CreateObject(StringHash), or, for that matter, just use Node's CreateComponent(StringHash type,...) and construct accordingly. Since you won't be doing this often, I would go with a Vector<String> over a Vector<StringHash>, as it makes it easier to print them out in logging and such. Active skill can then just use the regular events (input, update, etc.) to act, and the passive buffs can use OnNodeSet or (probably better, thought not necessarily) DelayedStart. For the buffs/debuffs, you can either just use Node variables, or you can create a Creature/Player/... component that stores all of the stat information and just use Node::GetComponent<> and Node::HasComponent<>.

-------------------------

microface | 2017-01-02 01:15:13 UTC | #7

What you suggested really did a great favor to me though I may not catch your idea very well sometimes. I'll try it then, and thanks a lot for your help!

-------------------------

