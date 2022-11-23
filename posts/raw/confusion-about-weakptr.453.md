thebluefish | 2017-01-02 01:00:32 UTC | #1

This is really a two-part issue, but I'm more-so focused on the "why" versus the end result at this point.

Originally what I was trying to do is modify Node.h to change the owner_ from a Connection* to a WeakPtr<Connection> to make it follow the standards presented throughout Urho3D. This will also prevent issues from attempting to use the Connection retrieved from GetOwner() when someone disconnects (Unless I'm mistaken here?).

When I made the appropriate changes, I can no longer compile. Instead I get the following errors:
[code]
error C2027: use of undefined type 'Urho3D::Connection'
error C2227: left of '->RefCountPtr' must point to class/struct/union/generic type	
[/code]

I've spent roughly 2 hours checking similar headers and making sure I'm not making any mistakes, but I can't seem to figure out what I'm doing wrong here. Other headers similarly forward-declare class names and successfully wrap them with a WeakPtr, so why am I having this problem?

-------------------------

cadaver | 2017-01-02 01:00:32 UTC | #2

The reason why Connection was originally a raw pointer is maintaining a strict top-down hierarchy of libraries: Network was supposed to depend on Scene and not the other way around. This is also necessary if we want to be able to optionally remove the networking functionality from the library build (similarly like Physics & Navigation can be removed.)

Look at Scene::CleanupConnection(Connection* connection); it does the owner cleanup from the scene's all replicated nodes and components on disconnect. So unless you're assigning an owner to local nodes / components (which should not make sense) you're already safe.

I've spent substantial time going through similar errors with forward-declared classes. You will need to make sure that the WeakPtr is not manipulated in any way from the header, not even .Get(), or from other files that don't actually include Connection.h. Compiler-generated functions like destructor, assignment etc. may also cause trouble in this regard.

-------------------------

thebluefish | 2017-01-02 01:00:32 UTC | #3

I suppose that makes sense. It just seems weird to me that we're relying on manual assignment instead of reference counting like the rest of the engine. IMO it would be preferably that there isn't a hierarchy of libraries, that Network and Scene both work completely independently of each-other and maintain their own internal state. If one needs access to the other, it would use WeakPtrs and Events to communicate available information. Just a pipe dream I suppose, the engine's great either way.

I think I've figured out what I need to change in my code to get it working reliably. I was using SetOwner and GetOwner to maintain user-based Nodes instead of SetScene on the Connection, silly me.

Still haven't figured out why making the Connection a WeakPtr wasn't working for me, but I suppose it's a moot point anyways.

-------------------------

