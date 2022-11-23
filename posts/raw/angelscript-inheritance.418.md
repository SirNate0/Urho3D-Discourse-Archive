thebluefish | 2017-01-02 01:00:15 UTC | #1

I've been scratching my head over this one for a few days, thought you guys might have a better idea.

Essentially I want to define a standard interface that can be then inherited from in Angelscript classes. For example, say I have a card game like Magic The Gathering, my base class might look like:

[code]class Card
{
public:
    virtual void PreDrawPhase() = 0;
    virtual void PostDrawPhase() = 0;
    // etc....
};[/code]

Then I want to be able to define each card in Angelscript such that the cards can be called from C++, but the logic is handled by the script itself. How would I go about defining the behavior?

-------------------------

friesencr | 2017-01-02 01:00:15 UTC | #2

Do you need to pass data generated from c++?  Why does the c++ code call it?  There are lots of looser coupled options like subscribing to events and using node vars data bags.

-------------------------

thebluefish | 2017-01-02 01:00:15 UTC | #3

[quote="friesencr"]Do you need to pass data generated from c++?  Why does the c++ code call it?  There are lots of looser coupled options like subscribing to events and using node vars data bags.[/quote]

Think of my example from before. Say I have a hundred cards and each one does various effects. Instead of hard-coding the effect in C++, I can let the script define the effect that's done. So I could then call from C++:

[code]// in pseudo-code
foreach(card in player.cards)
{
    if(card->PreDrawPhase())
    {
        player->DrawCard();
    }
    card->PostDrawPhase();
}[/code]

and in my card's script:

[code]bool PreDrawPhase()
{
    if(player.cards.count > 7)
        return false; // Don't draw a card

    return true;
}

void PostDrawPhase()
{
    //Discard another player's card because we can
}[/code]

-------------------------

weitjong | 2017-01-02 01:00:15 UTC | #4

Have you checked the ScriptInstance documentation? I think it may fit your use case well. You should be able to define your base AngelScript class using empty interface ScriptObject then derived your Anglescript inherintance from this base class. I don't think you need C++ abstract base class for that. You can then invoke the ScriptInstance's method by using ScriptInstance::Execute() or ScriptInstance::DelayedExecute() methods from the C++ side.

-------------------------

thebluefish | 2017-01-02 01:00:15 UTC | #5

I never noticed ScriptInstance, I only saw ScriptFile when I was looking through before.

This seems promising, especially as it appears the ScriptInstance can register for events. I am confused about this bit:

[quote]Subscribing to events in script behaves differently depending on whether SubscribeToEvent() is called from a script object's method, or from a procedural script function. If called from an instantiated script object, the ScriptInstance becomes the event receiver on the C++ side, and calls the specified handler method when the event arrives. If called from a function, the ScriptFile will be the event receiver and the handler must be a free function in the same script file. The third case is if the event is subscribed to from a script object that does not belong to a ScriptInstance. In that case the ScriptFile will create a proxy C++ object on demand to be able to forward the event to the script object.[/quote]

Say I have the file testCard.as with the following:

bool HandlePreDraw()
{
    // Do something
}

void HandlePostDraw()
{
    // Do something
}

Would it still receive events properly if I called SubscribeToEvent() from the Start() function? Or would I need to set it up a different way? Also, event data is read in AngelScript the same way it is read in C++, correct?

-------------------------

weitjong | 2017-01-02 01:00:15 UTC | #6

As I understand it, you only use SubscribeToEvent() when you know there is *other* Object sending a particular event that your object is interested (and want to become the event receiver). For your case, I don't think you can easily find the preexisting events that are suitable for your two handlers to listen to. I believe it is easier to just invoke the PreDraw() and PostDraw() as normal Script Object's methods via the ScriptInstance::Execute() method as I pointed out earlier.

Regarding your confusion, You can observe the differences in the Samples by comparing SubscribeToEvent() call in Ninja.as and SubscribeToEvent() call in 01_HelloWorld.as. HTH.

-------------------------

friesencr | 2017-01-02 01:00:15 UTC | #7

Some events like some of the ui events don't have senders.  So using the syntax without a the sender is used.  It's contextual.

-------------------------

thebluefish | 2017-01-02 01:00:15 UTC | #8

[quote="weitjong"]As I understand it, you only use SubscribeToEvent() when you know there is *other* Object sending a particular event that your object is interested (and want to become the event receiver). For your case, I don't think you can easily find the preexisting events that are suitable for your two handlers to listen to. I believe it is easier to just invoke the PreDraw() and PostDraw() as normal Script Object's methods via the ScriptInstance::Execute() method as I pointed out earlier.[/quote]

Due to the way events work, it's trivial to add new events as needed. My game already has a few dozen custom events in use, same as the InputManager class that I released.

Completely forgot about the .as demos as I had previously deleted them from my build. I looked through them and found what I needed.

For a test, I created a Card class inherited from ScriptInstance. Luckily, it's easy to tell Angelscript that one class inherits another. Therefore instead of traversing nodes looking for an attached ScriptInstance components which might or might not be a Card (could be something else scripted), it's now easier to traverse the nodes looking for an attached Card component.

One thing I haven't yet figured out (remember I'm fairly new to scripting) is how to access the current node within the script. I know I can call my globally registered class from the script. Does ScriptInstance give global variables to the underlying script to do this?

-------------------------

friesencr | 2017-01-02 01:00:16 UTC | #9

if you are in a ScriptInstance and call "node" not this.node, it will give you the node that is attached to the scriptinstance.

-------------------------

weitjong | 2017-01-02 01:00:16 UTC | #10

ScriptInstance is a Component. So, it should have all the common methods and properties the base Component class gives, including the node property. See [urho3d.github.io/documentation/H ... ptInstance](http://urho3d.github.io/documentation/HEAD/_script_a_p_i.html#Class_ScriptInstance)

[quote="thebluefish"]Due to the way events work, it's trivial to add new events as needed.[/quote]
Yes, adding new events to suit your need works as well. I think it is all comes to the design decision whether you want to have loosely coupled or tightly coupled design. The Urho3D library cannot anticipate how all the components in the end application interacts with each other, so having the event subscription mechanism solves that problem by allowing the components to depend on each other loosely. While in your own application, you do have a choice between the two as you should already know how your components would interact with each other before hand.

-------------------------

thebluefish | 2017-01-02 01:00:18 UTC | #11

Awesome :smiley:

I was able to further work the ScriptInstance class to fit what I was trying to do. I find it's easy to simply inherit from this class, and expose additional script functions explicitly.

-------------------------

