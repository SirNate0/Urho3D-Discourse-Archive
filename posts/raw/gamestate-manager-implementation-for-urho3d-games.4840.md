Leith | 2019-01-20 04:37:30 UTC | #1

I've just finished implementing a gamestate manager, and I seek opinions, advice and comment from the gallery.
This is the third incarnation in as many days, however I'm pretty happy with the advantages that come with the design. 
Here's some quick notes I shoved into a ReadMe file that describe the key concepts:

[quote]
The gamestate manager resides in its own Scene, and can be fully serialized to remember user preferences.
It creates a toplevel node, with one child node (bearing one component) per gamestate.
I have implemented three example states: intro (splashscreen), main menu, and gameplay.

The gamestate components can disable and re-enable themselves on demand (see the Enter and Exit methods), and they remain resident at all times (but can unload/reload resources to reduce memory footprint).

This is not a stack based implementation, which means that any gamestate can in theory transition to any other,
and it also means that, in theory, multiple gamestates can be active simultaneously (although I did not provide an example).

The GamePlay gamestate creates and manages a secondary scene, which represents the game scene.
Since the game scene is separate to the manager scene, it can be serialized separately,
representing a snapshot of gameplay that can be saved and reloaded independently of the game manager / menu settings.
GamePlay has full access to the game scene at all times, and can manipulate it in any way.
The purpose of the GamePlay gamestate is not to implement game logic, but merely to provide
a means to manage the content of the game scene from outside of that scene.
[/quote]

What I forgot to mention? GameStates are not aware they are being managed, or that a manager class exists.
This is achieved by implementing a custom event handler in the manager:
[quote]
	/// Event Handler: Change of GameState
	void onStateChange(StringHash eventType, VariantMap& eventData );
[/quote]

-------------------------

Modanung | 2019-01-20 12:14:46 UTC | #2

Interesting use of `Node`s.

Have you considered having the game state manager inherit (directly) from `Serializable` instead and giving it some attributes?

EDIT: ...and to use it without a `Scene` (or any `Node`), instead registering it as a _subsystem_?

-------------------------

Leith | 2019-01-20 12:17:46 UTC | #3

It already inherits serializable, its component based!

The file uploads here are very restrictive, I cant attach the xml I dumped from the manager and game scenes, but you can imagine them.

Screw it.

Here is the Manager Scene, it gets dumped by the Main Menu State for no particular raison.
Quoting XML on this site is also a bad, and possibly a security issue, I can't post shit here, sad face :(

-------------------------

Leith | 2019-01-20 12:29:20 UTC | #4

The master object, the game state manager, which could be a singleton or not, is derived from Object, not Component - it is still Serializable (though there is nothing worth serializing), and can do Eventing (which I use), it is not part of the scene, or any scene, but there is a node in a scene named after it, for sanity.

The GameStateManager is NOT registered as a subsystem, just a regular Object.
It only subscribes for ONE event - a custom event, the change gamestate event.

Changing gamestate involves calling Exit on the current state, calling Enter on the new state, and updating a pointer to the current (most recently entered) state, the third step being a courtesy for the next Exit.

-------------------------

Modanung | 2019-01-20 12:40:47 UTC | #5

I guess there's many ways to approach this problem. :)
Also I must say I'm not at all familiar with design patterns. Using `Node`s just seems a bit unnecessary to me in this case.

[quote="Leith, post:3, topic:4840"]
I can’t post shit here
[/quote]

Would a [gist](https://gist.github.com/) provide what you're looking for?

-------------------------

Leith | 2019-01-20 12:38:43 UTC | #6

Probably, but I have not committed my stuff to github, and tend not to since it was bought out by m$
Force of habit I guess.

I'll set up a dump someplace.

-------------------------

Modanung | 2019-01-20 12:41:59 UTC | #7

[quote="Leith, post:6, topic:4840"]
Probably, but I have not committed my stuff to github, and tend not to since it was bought out by m$
Force of habit I guess.
[/quote]

You're right, I should've mentioned [GitLab snippets](https://gitlab.com/snippets/new) instead. :slight_smile:

-------------------------

Leith | 2019-01-20 13:04:37 UTC | #8

Alibaba (China) are a shareholder, still does not smell like the right place to dump.
I tend to think I can find something suitable, even if I have to host it myself.

I often think to myself that the Chinese using the name Alibaba is ironic - he was a prince of thieves.

If I host it myself, and publish it here, I at least have a poor mans copyright over my work, and evidence of prior art.
As I am familiar with the WAMP stack, it should be fairly easy to set up a LAMP stack, and find a reasonable or free domain name to point at it - for example, my earliest internet tombstone, is u.wants.it

-------------------------

Modanung | 2019-01-20 13:10:52 UTC | #9

[quote="Leith, post:8, topic:4840"]
Alibaba (China) are a shareholder
[/quote]

I did not know that, although I only find Alibaba being mentioned as a main customer. Not shareholder.
Ever read [Ali Baba and the Fourty Thieves](https://en.wikipedia.org/wiki/Ali_Baba), btw?
> In the story, Ali Baba is a poor woodcutter who discovers the secret of a thieves' den, entered with the phrase "Open Sesame". The thieves learn this and try to kill Ali Baba...

I guess the 40 thieves would represent the Western world if Ali Baba were China.

-------------------------

Leith | 2019-01-20 13:11:27 UTC | #10

[quote]
Ali Baba is then left as the only one knowing the secret of the treasure in the cave and how to access it. 
[/quote]

I had the thousand and one tales of the arabian nights as a child.
Ali Baba ended up with the treasure, and was the only one who could access it.

He had learned to rule by controlling the information.

I don't want to control information, but I do want to retain my rights as author.

-------------------------

Modanung | 2019-01-20 13:21:36 UTC | #11

He can keep his treasures, I'm more interested in spiritual gold.
It is more liberating, everlasting, harder to steal and easier to share. :slight_smile:

-------------------------

Leith | 2019-01-20 13:21:04 UTC | #12

What I contribute to Urho3D in terms of Pull Requests, and what I publish on the side, are separate.
I choose to contribute some things to the community, which is cool, right? But other things, like example code, I don't expect to publish in the community, but FOR the community nonetheless. The difference is who owns that IP.
Regardless, I need a place to do it, and there is no place like home.

-------------------------

Leith | 2019-01-21 08:52:21 UTC | #13

https://www.dropbox.com/s/nh8inz28wwyn1rl/UrhoTest.zip?dl=0

Here's the files for the state manager as of today.
There's not a whole lot to see, other than the implementation working as expected.

Press "space" on the "main menu state" (the one displaying FPS) to see the "game state".
Escape to quit.

I've partially implemented a Loading state, and am currently figuring out character controller and background loading.

Before I run headfirst into walls, I like to set up a safe space for my game. This invariably begins with some kind of state management, whether it be FSM, or like this one, ISM. I won't spend too much effort on anything until I have a solid foundation to build on.

With a suitable game state manager, we could do away with separate builds for the samples, and load them all in a single application, like bullet, like ogre. Not that I am complaining, just pointing out the obvious.

-------------------------

Leith | 2019-01-22 05:45:16 UTC | #14

I implemented asynch scene loading, and have a character in my game scene.
Now working on character controller, soon I'll have the character sample running under my state manager.

The key advantage of using a state manager, so far, is to separately serialize the content of the state manager, and the content of the game scene. 

The idea is that something is alive, above the game scene, that can unload and reload the game scene, and save its state, without needing to be told how.

-------------------------

Miegamicis | 2019-01-22 12:46:25 UTC | #15

Will check this out.

I also implemented my own game state manager in his project: https://discourse.urho3d.io/t/new-project-template/4428
It was a bit more complex, but maybe there's something that I could borrow from your implementation to further improve it. I basically had `LevelManager` class, which handler what sort of screen is visible to the user and the `SceneManager` which was responsible for the background scene loading.

-------------------------

Leith | 2019-01-22 12:49:37 UTC | #16

I deliberately went for less complexity - it started as a stack based thing, but I realized quickly that stack based stuff induces limits on the transitions, and that is not always a good thing - this implementation is ISM, infinite state machine, any state can transition to any other, and we don't need to deal with the overhead

-------------------------

Leith | 2019-01-23 08:19:59 UTC | #17

I have the guts of the character sample working under my state manager.
I'm 99 percent happy with the code structure.

The point is, I have a playable demo running under my state manager, which can save snapshots of gameplay and reload them, separately to the menu system / user options.

I will tidy it a bit and then post a link, I note that much of the code and assets are not mine, and don't expect to claim anything other than that my state manager works.

-------------------------

Leith | 2019-01-24 08:57:58 UTC | #18

I note that Urho has no method for serializing a subtree of a scene.
I offer to provide one, assuming that others agree this could be handy.

-------------------------

Leith | 2019-01-24 09:17:01 UTC | #19

If you see anything you like, please feel free to take it and use it as you wish.
I don't want to be credited for finding ways to use the engine, but any core changes I make, I would appreciate to see some credit.
I will update the codebase later today, which includes some some stuff for ragdoll extensions.
I also enabled physics debug drawing, and no way to disable it.
Life is for the living.

-------------------------

Leith | 2019-01-24 09:32:47 UTC | #20

https://www.dropbox.com/s/mhzyw7flc9d8ppa/UrhoTest.zip?dl=0 update

-------------------------

lezak | 2019-01-24 14:12:02 UTC | #21

You mean like serializing only selected node and its children? You can do that, You can even save single components.

-------------------------

Leith | 2019-01-25 03:19:33 UTC | #22

Yes I realized this pretty late, still I feel more comfortable with a proper state manager, than trying to kludge everything together somewhere else... and it makes a lot of sense to have a Loading state, that stays resident, and GUI elements (like menu items) that are not part of the game scene, not to be in the game scene.
Modularity has lots of advantages, including the ability to easily re-use the modules.

-------------------------

