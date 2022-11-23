Eugene | 2017-07-04 20:12:02 UTC | #1

I want to 'chain' several logical components inside the node.
I construct component and store it in the host component, then I set the node of component via SetNode to keep component fully functional.

Are there any side effects or pitfalls of this approach?

-------------------------

cadaver | 2017-07-05 08:57:04 UTC | #2

I would say that if it breaks, you get to keep both parts. The recommended way would be for the component to create the other component it needs using node_->CreateComponent(), that way it's sure all bookkeeping happens as intended. For performance, it can of course store a direct reference.

-------------------------

Eugene | 2017-07-05 09:31:46 UTC | #3

[quote="cadaver, post:2, topic:3322"]
The recommended way would be for the component to create the other component it needs using node_-&gt;CreateComponent()
[/quote]

The problem here is that added component will automatically receive events. However, I usually want to call event handlers in the specific order when I use multiple logic components.

I've just thought that I can use CreateComponent and disable the component or reset event mask to block all callbacks. This one looks like a perfect solution.

-------------------------

