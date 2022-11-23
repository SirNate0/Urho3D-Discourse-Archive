Leith | 2019-06-18 09:43:34 UTC | #1

I created a massive headache for myself recently - I had smashed out a bunch of classes deriving from Serializable, created a tree of specialized nodes (a custom set of derived node classes, nothing to do with Urho3D::Node), and during destruction, I was landing in Context::RemoveEventReceiver, on my deepest node (initially), with pthis=nullptr
As my project pulls in the (release) Urho lib, I could not easily investigate the cause of the crash, but I do know my way around ASM, and I was able to inspect the disassembled code and the CPU registers to figure out that one of my objects had not correctly initialized the context_ member.

The issue was caused as follows:
[code]
MyClass::MyClass(Context* context):ItsAncestor(context_) { }
[/code]

Can you see the problem?
It's such a subtle bug, but it's super-nasty.

The input argument "context" is valid on entry - but that's not what we handed to the ancestor!

Just a friendly heads-up incase someone else is wondering why their code crashes silently!

-------------------------

Leith | 2019-06-18 09:48:25 UTC | #2

Curse of intellisense strikes again

-------------------------

guk_alex | 2019-06-18 09:49:00 UTC | #3

Should the compiler warn you for unused input argument?

-------------------------

Leith | 2019-06-19 12:48:26 UTC | #4

I handed in the placeholder member, which we inherited from serializable (actually from Object, deeper again), I did not pass the input argument as intended

I had a train ticket to pass to the conductor, but i showed him my empty pocket before he had handed me the ticket back to put in my pocket

the input argument was called context
the thing i handed the ancestor was the ultimate holder of context, called context_

at the time i did so, context_ was still empty

yes, the compiler should warn you, about unused inputs, if they have no defaults specified

it never ceases to amuse me, as a programmer, how one character out of place can crash the entire machine

in my days as an industrial robotics coder, once i put the decimal point in the wrong place in one number in a huge program, and quite some time later, a 50 tonne robot attempted to tear itself apart, at full speed - 30 meters per minute back then (I happened to be nearby, but I was also running other machines too)

-------------------------

Leith | 2019-06-18 10:07:00 UTC | #5

Yes, for arguments which have no default value specified, for sure - maybe not if there is a default, because it could be a throw-away value depending on the whim of the caller

-------------------------

