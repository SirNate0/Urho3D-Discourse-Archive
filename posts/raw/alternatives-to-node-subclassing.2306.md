vudugun | 2017-01-02 01:14:36 UTC | #1

Hello,
I know subclassing Node is not recommended, but I can't find a good way to store/link custom objects in a node:

1) using components:
    - adding component is ok
    - accessing components is slow (linear search, GetComponent() is in fact a "FindFirstComponent")
    - accessing derived components is slower (linear search + dynamic_cast)

2) using node vars: feels like javascript

3) creating a custom component system: HashSet<Node*, MyCustomObject*>: please no

Is full support for Node subclassing anywhere on the roadmap or even possible?

Thanks!

-------------------------

TheComet | 2017-01-02 01:14:36 UTC | #2

Maybe I don't understand the problem, but subclassing Node doesn't improve performance of GetComponent().

If it really turns out that GetComponent() is your bottleneck (which I doubt), then an option could be to just cache them. Listen to E_COMPONENTADDED and E_COMPONENTREMOVED and maintain your own data structure of components.

-------------------------

cadaver | 2017-01-02 01:14:36 UTC | #3

Subclassing nodes is not planned to be supported.

I would recommend holding cached links to your objects near to the place where you need them. If you use WeakPtr for this it should be safe against deletion happening at arbitrary time. For example a targeting script or logic component having the last assigned target node as a member variable.

For a generic storage solution 2) is valid.

For maximum performance, if you want to mass-process a high amount of objects and handle links between them then you could have a "subsystem-like" component that has its own data structures.

-------------------------

vudugun | 2017-01-02 01:14:36 UTC | #4

Thanks for the replies!

@TheComet:
GetComponent() is not my bottleneck yet, but calling it from a LogicComponent::Update() function shared by many nodes *might* become a problem. If I could derive from Node, the component would be a simple data member, with minimal access time.

@Cadaver
Too bad to hear subclassing nodes is not planned. I think I'll go for the WeakPtrs option, I am already caching from inside LogicComponent::Start() functions, but I could be more aggressive than that.

-------------------------

TheComet | 2017-01-02 01:14:36 UTC | #5

You say it's a linear search - which is true - however considering that in a typical game you won't ever have more than maybe 10 components on a node, it's not going to be "slow" like you say. It will be [i]slower[/i] than accessing a data member but it's still very, very fast.

-------------------------

vudugun | 2017-01-02 01:14:37 UTC | #6

I wouldn't bother for a rarely used function, but GetComponent() looks like a frequently used function in client code. After all, we are told to use components for custom logic, and its innocent-looking name is a bit misleading.

Anyway, I have come up with a solution for my problem (storing per-node custom objects in a fast-accessible way). It is actually pretty simple: by ensuring my custom component is always the last one, I can quickly access it via Node::GetComponents().Back().

-------------------------

