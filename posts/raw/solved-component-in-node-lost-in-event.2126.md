rbnpontes | 2017-01-02 01:13:18 UTC | #1

Hello Guys, i have a problem when i'm trying to get component in node with custom event.
The component is lost.
Sorry for my english

-------------------------

jmiller | 2017-01-02 01:13:18 UTC | #2

Hello,

Your english is fine, what I do not understand is the problem. :slight_smile: Can you provide a bit more information or code?

-------------------------

rbnpontes | 2017-01-02 01:13:19 UTC | #3

OK, this is a example of my code
[code]
//Part 1
VariantMap& eventHandler = GetEventMapHandler();
eventHandler[RP_MY_EVENT_NODE] = node; 
SendEvent(RP_MY_EVENT,eventHandler);
// This part working with success
[/code]
[code]
//Part 2
Node* _node = static_cast<Node*>(eventHandler[RP_MY_EVENT].GetVoidPtr());
// The casting is working, the Node not return empty but
// If i'm try this
StaticModel* model = _node->GetComponent<StaticModel>();
// The variable model is only null, if i'm trying to get component, The return value is only null
//I'm trying to diferents casts like, static_cast,dynamic & reinterpreter and not working
[/code]

-------------------------

jmiller | 2017-01-02 01:13:19 UTC | #4

I use static_cast in the same way with success. As you say, Node is saying it has no component of that type. It may help to see how you added it to the Node.
For reference, many samples do this (like 18_Characterdemo).

-------------------------

Modanung | 2017-01-02 01:13:19 UTC | #5

It seems to me RP_MY_EVENT could use an appended _NODE at the beginning of part 2.

-------------------------

rbnpontes | 2017-01-02 01:13:19 UTC | #6

My Node have a StaticModel component

-------------------------

rbnpontes | 2017-01-02 01:13:19 UTC | #8

No, The Component is not removed
I'm added component like this
[code]
Node* node = _scene->CreateChild("Test");
StaticModel* m = node->CreateComponent<StaticModel>();
[/code]

-------------------------

Lumak | 2017-01-02 01:13:19 UTC | #9

As Modanung mentioned, change:
//Part 2
Node* _node = static_cast<Node*>(eventHandler[ [b]RP_MY_EVENT[/b] ].GetVoidPtr());

[b]to:[/b]
//Part 2
Node* _node = static_cast<Node*>(eventHandler[ [b][color=#FF0000]RP_MY_EVENT_NODE[/color][/b] ].GetVoidPtr());

-------------------------

rbnpontes | 2017-01-02 01:13:20 UTC | #11

Sorry Guys for the error, i'm added node to Scene and not to Node  :laughing: 
i'm fixed, thank's for the help

-------------------------

