QBkGames | 2019-06-04 05:17:02 UTC | #1

I'm having trouble understanding how all the Node SetEnabled variants work.

First problem is:
>     /// Set enabled state on self and child nodes. Nodes' own enabled state is remembered (IsEnabledSelf) and can be restored.
>     void Node::SetDeepEnabled(bool enable)
>     {
>         SetEnabled(enable, true, false);
>     }
The comment says the node remembers is current state which can be restored later, however the 3rd parameter to the SetEnabled function which flags whether to remember its state or not, is actually false.

Second problem:
> void Node::SetEnabled(bool enable, bool recursive, bool storeSelf)
> {
>     ...
>
>     if (storeSelf)
>         enabledPrev_ = enable;
> 
>     if (enable != enabled_)
>     {
The function is not storing its current state, but the new state which is passed on as a parameter. Shouldn't it be:
>     if (storeSelf)
>         enabledPrev_ = enabled_;
So, either I don't understand how this code works or there are some serious bugs! Can someone clarify? Thanks.

-------------------------

Leith | 2019-06-03 10:47:05 UTC | #2

SetEnabled does what it says - it enables, or disables, a node, for update purposes. Its children may still receive updates! SetEnabled applies to exactly one node, and not to its children, or their children.
SetDeepEnabled does something slightly different, it enables, or disables, a node, and all its children, and their children!, and remembers what it did, so it can be undone for some entire scene subtree. I use this to pause stuff.
I am implying some things that are not clear about Urho - object updates don't stop when we hit a disabled object, its children can still fire unless explicitly disabled. Urho, like all game engines, has some quirks.
The strategy of having a master thing live outside of game scenes, was something I had already applied to a commercial game in Unity - they had the hindsight to implement support for "things that are immortal"

When I began using Urho, I decided to create a unique scene - not the game scene, but a manager scene, that would live outside of all game scenes, with components to represent my major game states, and one ring to rule them all. I had no idea what I was doing, but it turned out to be a good plan, to separate my game state management

-------------------------

weitjong | 2019-06-03 12:34:59 UTC | #3

Urho3D is an open source project. When in doubt, you can always use the `git blame` to find out which commit introduced the code in question. It did not take me more than a minute to find the commit. 

https://github.com/urho3d/Urho3D/commit/3e4882bfa551584e003c272964d98848bc82adbb

And with the whole commit message and the whole changes in the context, it does not seem to me that there is any bug in the code.

I have helped Lasse to migrate from SVN to GitHub and I can confirm that we have never lost any commit history since the day this project was his pet project till today. The code itself is the ultimate document of the project. Read from source to get the truth yourself instead of from other personal opinion.

-------------------------

QBkGames | 2019-06-04 00:20:19 UTC | #4

Your argument seems to be based on the Appeal to Authority fallacy: This piece of code is the perfect original creation of the project god, which has never been corrupted by other influences throughout its history, so how dare you doubt it!?
With all due respect to Lasse, who created an awesome project, I'll commit the blasphemy of suggesting that the original code written by him is logically wrong, and I'm guessing that no one has picked it up because no one really tried to use it to its potential.
Can someone prove wrong my critique of the code using logic?

-------------------------

weitjong | 2019-06-04 02:11:55 UTC | #5

That’s not exactly what I meant. I don’t care who was the author of that commit. I have looked at that code when it was first committed and again yesterday. My logic says it is correct. As I recall, the `SetDeepEnabled()` is something added much later and it is intended to let user temporarily toggle the state to one way or another. So, it is intentional that it does not alter the `enablePrev_`. For the permanent toggle, use the `SetEnabledRecursive()`. If you have actually looked at the commit I linked then you should have understood why I said it appears there is no bug to me.

I guess one has to get accustomed to Lasse ‘s code style to understand his logic better. Don’t get me wrong, I am not saying he is or we are always right.

-------------------------

QBkGames | 2019-06-04 02:54:38 UTC | #6

I did look at the commit and read all the replies, however, what I don't get is:
* If  SetDeepEnabled() is intended to temporarily toggle the state, then how does it store the current state so it can be restored it back if it's not using the enablePrev_ field? RestoreDeepEnabled() is relying on this variable!
* If SetEnabledRecursive() does a permanent toggle, then what does it need the enablePrev_ for? It shouldn't care about the previous state if it's a permanent action.

I appreciate your reply, but I'm sorry, neither the code nor your explanation make sense to me.

-------------------------

weitjong | 2019-06-04 03:26:47 UTC | #7

If the enabledPrev_ is unaltered then it contains the value of the last permanent state. So the reset method can revert to whatever as it was.

-------------------------

QBkGames | 2019-06-04 05:24:54 UTC | #8

I finally get it! I think the name of RestoreDeepEnabled got me confused about what the Set... functions are supposed to do. I was thinking of a different mechanism all along while looking at the code.
Thanks for clarifying and apologies about the bother.

-------------------------

weitjong | 2019-06-04 05:35:55 UTC | #9

No problem. The name of the method could have been better.

-------------------------

