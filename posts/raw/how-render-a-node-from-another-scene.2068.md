dakilla | 2017-01-02 01:12:47 UTC | #1

Is there a way to render a node (StaticComponent) that belong to another scene (without cloning it) ? (same node instance used in multiple rendertarget)
Because my node is only rendered in the last scene where I added it.

Thanks

-------------------------

cadaver | 2017-01-02 01:12:48 UTC | #2

This is a variation of the "layering scenes" question. If you want it to render it in multiple rendertargets or viewports, you could have a viewport + renderpath without clear command whose purpose is to render only this object. Otherwise a node can only exist in one scene at a time.

This will introduce some inefficiency because it triggers a whole another scene render processing, so in case you want to keep max. performance I'd just recommend cloning the node to different scenes. The memory overhead from this is very small (just the component's + node's attributes) since the large data (mesh) is held in memory only once.

-------------------------

dakilla | 2017-01-02 01:12:49 UTC | #3

[quote]This is a variation of the "layering scenes" question [/quote]
Yes i'm working on a cutscene player, where it is possible to layering multiple scenes to make special fx.

[quote]Otherwise a node can only exist in one scene at a time[/quote]
Ok, thanks. 
I was looking for a way to do not clone a node because I have a custom animation system for nodes, but finally I found a way to use it as a component and how to create custom attributes of ptr types, so I can now clone nodes that refer to a unique anim ptr instance using this component. That solve my problem.

-------------------------

