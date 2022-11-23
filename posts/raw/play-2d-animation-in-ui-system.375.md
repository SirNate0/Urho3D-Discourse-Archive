hualin | 2017-01-02 00:59:57 UTC | #1

Hi, 
Currently there is no way to play 2d animated sprite in UI system. Will the engine add this feature recently?

-------------------------

aster2013 | 2017-01-02 00:59:57 UTC | #2

No, engine will not add this feature, but you can render 2D sprite to a render target, then use it in UI.

???????QQ??171718390?Urho3D????QQ?????????????????????????

-------------------------

cadaver | 2017-01-02 00:59:57 UTC | #3

It's not worth implementing UI/scene cross-over features such as this in an isolated manner. What would possibly make sense would be a complete merging of the UI and scene system, meaning that the UI elements would be part of a scene node graph and be rendered with a camera. But doing this would naturally break every Urho program using the existing UI, so the old and new (scene-based) UI's would need to exist side by side.

This would be a very large undertaking and I can't promise to have time for it myself, but if this gives someone ideas / inspiration, I'm glad to answer questions.

-------------------------

friesencr | 2017-01-02 00:59:57 UTC | #4

How would having uis while scenes are loading work, and in general sceneless operations.  It's too bad the sceneless mode had that wierd bug on android.  If it is any lift off your shoulders I would be happy to rewrite any of the ui code in the samples and the editor, this would require the code to sit in a branch and it would likely happen over a weekend when my vitamin pizza levels are high.

-------------------------

cadaver | 2017-01-02 00:59:58 UTC | #5

As different cameras can render different scenes, one scene could be loading while another renders the UI. In fact that would probably be recommended anyway so that you don't have to worry of having to place the UI in an inaccessible spot in your world :slight_smile:

Thanks for the offer! In such undertaking it would make sense to solve the UI element float positioning and scaling features at the same time (ie. you don't have to use integer coordinates and absolute pixel sizes if you don't want to) so it'd be hard to know exactly how well things would map into the "old" UI. For example, layouting would happen by actually moving and scaling child scene nodes.

-------------------------

