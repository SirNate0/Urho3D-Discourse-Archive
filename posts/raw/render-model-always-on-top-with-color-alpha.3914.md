esakylli | 2018-01-05 13:51:52 UTC | #1

I want to render a model always on top of all other models, specifying a color with alpha value for it.
Is it possible?

The technique NoTextureOverlay seems to do it, but I cannot use alpha value with the color...
(I want my model to look somewhat transparent.)

-------------------------

esakylli | 2018-01-07 16:14:39 UTC | #3

In my material I tried using technique NoTexture with a color (+ alpha), together with renderorder but no luck.
I'm not sure how renderorder works, but shouldn't I be able to adjust the rendering order with it?
But maybe it just works with some specific technique?

-------------------------

Dave82 | 2018-01-07 16:20:06 UTC | #4

Perhaps this helps.The same idea should work for your case

https://discourse.urho3d.io/t/show-ui-element-behind-3d-model/3185

-------------------------

esakylli | 2018-01-07 17:00:01 UTC | #5

Thanks for the reply, it got me a little further.
With it I can get my model on top of all, but I'm still facing two issues with it:
- The model is rendered on top of my cursor, how can I get it rendered between the UI and all other models?
- I can't get any alpha (transparency) along with my color, is it possible?

-------------------------

Dave82 | 2018-01-07 22:54:57 UTC | #6

[quote="esakylli, post:5, topic:3914"]
The model is rendered on top of my cursor, how can I get it rendered between the UI and all other models?
[/quote]

Try it like this 

[code]
<renderpath>
    <command type="clear" depth="1.0" />
    <command type="scenepass" pass="TopObjects"/>
    <command type="renderui"/>
</renderpath> 
[/code]

[quote="esakylli, post:5, topic:3914"]
I can’t get any alpha (transparency) along with my color, is it possible?
[/quote]
Create a copy of your DiffAlpha.xml technique and try to change the "alpha" pass to TopObjects.

-------------------------

esakylli | 2018-01-08 16:05:54 UTC | #7

Thanks @Dave82! It works like a charm :smiley:

One last question about this, is it right adding the render path like this (after I have created the Viewport)?

			var rp = Viewport.RenderPath.Clone();
			rp.Append(ResourceCache.GetXmlFile("RenderPaths/TopObjects.xml"));
			Viewport.RenderPath = rp;

-------------------------

Dave82 | 2018-01-08 16:14:54 UTC | #8

[quote="esakylli, post:7, topic:3914"]
One last question about this, is it right adding the render path like this (after I have created the Viewport)?

		var rp = Viewport.RenderPath.Clone();
		rp.Append(ResourceCache.GetXmlFile("RenderPaths/TopObjects.xml"));
		Viewport.RenderPath = rp;
[/quote]

Probably the Clone() is unneccessary so you could simply write : 
 [code]
Viewport.RenderPath.Append(ResourceCache.GetXmlFile("RenderPaths/TopObjects.xml"));
[/code]

-------------------------

