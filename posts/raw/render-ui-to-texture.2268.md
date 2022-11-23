bluerriq | 2017-01-02 01:14:24 UTC | #1

Hi, i wanted to know is it possible to render ui to texture and pass input events to it? I'm aiming for something similar to how the in-game computers/panels etc looked in doom 3. Image for reference : 

[img]https://www.roguevector.com/wp-content/uploads/2013/03/doom3_console.jpg[/img]

I couldn't find anything after looking at the docs so i'm assuming  the UI currently only renders to the default backbuffer. If i wanted to modify urho's source and add this in how complicated would it be and which parts of the source code should i look into? I'm new to urho and so far i've only had a cursory glance at the source so any help would be really appreciated.

Thanks!

-------------------------

cadaver | 2017-01-02 01:14:24 UTC | #2

You can render the UI to texture via a renderpath command, however there isn't mapping of input from arbitrary 3D coordinates, or a possibility to have multiple UI hierarchies.

-------------------------

bluerriq | 2017-01-02 01:14:24 UTC | #3

Ah okay. So are there any plans to add more features to the default UI in a future release or are users expected to provide their own solution by plugging in another library?

-------------------------

cadaver | 2017-01-02 01:14:24 UTC | #4

In-world UI's would certainly make sense, and there shouldn't be anything impossible with it, it's just effort. Urho project operates with limited developers and development time, so the best option always is that if you want something to be implemented, go ahead and do it, and make a pull request when it's done. Quite a number of features have been implemented that way.

-------------------------

bluerriq | 2017-01-02 01:14:24 UTC | #5

I understand. I'll go look into the source and see how it works underneath. Who knows, maybe I'll be able to add something to it :stuck_out_tongue: 
Thanks for the help!

-------------------------

jmiller | 2017-01-02 01:14:24 UTC | #6

Related
[url=http://discourse.urho3d.io/t/how-to-best-generate-an-in-game-hud/1684/1]How to best generate an in-game HUD[/url]

-------------------------

bluerriq | 2017-01-02 01:14:24 UTC | #7

I looked at that thread before asking but thanks for posting. It seems rendering the UI to texture won't be that complicated(after i figure out how renderpaths, viewports, views, cameras and rendering tie together  :stuck_out_tongue: ). I'm still wondering about how i'd handle propagating input though!

-------------------------

bluerriq | 2017-01-02 01:14:24 UTC | #8

Progress!!  :smiley: 

[img]http://i.imgur.com/tnTN0PP.png[/img]

-------------------------

godan | 2017-01-02 01:14:25 UTC | #9

Looks good! Nice one.

What was your approach? This is sort of ui is something I have to tackle at some point as well, so I'd be happy to help out with the effort.

-------------------------

Lumak | 2017-01-02 01:14:25 UTC | #10

Oh wow, emacs for windows? That's pretty neat and looks great.

-------------------------

bluerriq | 2017-01-02 01:14:25 UTC | #11

[quote="godan"]Looks good! Nice one.

What was your approach? This is sort of ui is something I have to tackle at some point as well, so I'd be happy to help out with the effort.[/quote]

I used a simple renderpath on a viewport without a camera or scene. Here's the renderpath:
[code]
<renderpath>
	<command type="clear" color="0 0 0 1" depth="1.0" stencil="0" />
	<command type="renderui" output="ui_texture" />
</renderpath>
[/code]

The code is pretty simple as well, this is on a logic component with a plane attached to it

[code]
void Screen_Component::Start()
{
	ResourceCache* cache = GetSubsystem<ResourceCache>();
	Context* context = GetContext();
	
	SharedPtr<Texture2D> render_texture(new Texture2D(context));
	render_texture->SetSize(800, 600, Graphics::GetRGBAFormat(), TEXTURE_RENDERTARGET);
	render_texture->SetFilterMode(FILTER_BILINEAR);
	render_texture->SetName("ui_texture");
	cache->AddManualResource(render_texture);

	SharedPtr<Material> material(new Material(context));
	material->SetTechnique(0, cache->GetResource<Technique>("Techniques/DiffSpec.xml"));
	material->SetTexture(TU_DIFFUSE, render_texture);
	
	StaticModel* model = GetComponent<StaticModel>();
	model->SetMaterial(material);

	RenderSurface* surface = render_texture->GetRenderSurface();
	SharedPtr<Viewport> ui_viewport(new Viewport(context));
	XMLFile* ui_renderpath = cache->GetResource<XMLFile>("RenderPaths/UI_Render.xml");
	ui_viewport->SetRenderPath(ui_renderpath);
	ui_viewport->SetRect(IntRect(0, 0, 0, 0));
	surface->SetViewport(0, ui_viewport);

	UI* ui = GetSubsystem<UI>();
	Cursor* cursor = new Cursor(context);
	Image* image = cache->GetResource<Image>("Textures/UI.png");
	if (image)
	{
		cursor->DefineShape(CS_NORMAL, image, IntRect(0, 0, 12, 24), IntVector2(0, 0));
		cursor->DefineShape("Custom", image, IntRect(12, 0, 12, 36), IntVector2(0, 0));
	}
	cursor->SetVisible(false);
	ui->SetCursor(cursor);
}

[/code]

There's still a lot left to do however. If the plane goes out of the view the UI is drawn to the screen like normal. I have to come up with some way to disable the UI when the player is not looking. Since i plan on having most, if not all UI in world space, this won't be too complicated. There are probably other issues to resolve as well which i haven't encountered yet but this seems like a good enough start. It would've been really nice if there could've been multiple UI hierarchies though, it seems i'll either have to modify urho's source or i'll have to figure out some other hack and simulate it by having other empty UI nodes attached to the root node and turn them on and off when i need.

[quote="Lumak"]Oh wow, emacs for windows? That's pretty neat and looks great.[/quote]
Yeah, i have to basically use emacs everywhere after getting "emacs fingers", no other text editor feels right, and i'm not even that good with emacs! :laughing: That being said, the consolas font looks even better in emacs for some reason. Windows is no fun at all but i have to use it because performance on linux is not that great on my craptop(Intel HD 4000)  :stuck_out_tongue:

-------------------------

cadaver | 2017-01-02 01:14:25 UTC | #12

If you want to implement this properly I believe you have to tackle the multiple UI hierarchies issue, for example allow a scene component to store a UI root element, and have it separate from the existing UI root that would be rendered to the backbuffer. This probably includes more substantial code changes. For the existing UI there's a simple logic that if it's not rendered anywhere else by a renderpath command, then it will be rendered to the backbuffer, which you're seeing here.

-------------------------

bluerriq | 2017-01-02 01:14:25 UTC | #13

I'm still researching whether or not to go with world-space UI's everywhere though and so far i haven't seen a lot of games going with this approach and for good reason. For simple UI elements like large buttons etc this approach would be better but for more complicated UIs this approach could get annoying. I suppose i'll have to strike a balance between 3d and 2d UIs by using text3d/textures for worldspace elements and 2d UI for the rest to not affect the immersion and go for the same look as fallout's pipboy : 

[img]http://vignette3.wikia.nocookie.net/fallout/images/7/76/Pip-Boy_3000.jpg/revision/latest?cb=20110712154420[/img]

Food for thought!

Either way, personal musing on UIs aside, you're correct, there's no going around multiple hierarchies if this way of handling UIs is required.

-------------------------

godan | 2017-01-02 01:14:25 UTC | #14

Would having more control over the transform that's passed to the Batch class do anything? E.g.:

[code]
void UIBatch::AddQuad(const Matrix3x4& transform, int x, int y, int width, int height, int texOffsetX, int texOffsetY,
    int texWidth, int texHeight)
{
    unsigned topLeftColor, topRightColor, bottomLeftColor, bottomRightColor;

    if (!useGradient_)
    {
        // If alpha is 0, nothing will be rendered, so do not add the quad
        if (!(color_ & 0xff000000))
            return;

        topLeftColor = color_;
        topRightColor = color_;
        bottomLeftColor = color_;
        bottomRightColor = color_;
    }
    else
    {
        topLeftColor = GetInterpolatedColor(x, y);
        topRightColor = GetInterpolatedColor(x + width, y);
        bottomLeftColor = GetInterpolatedColor(x, y + height);
        bottomRightColor = GetInterpolatedColor(x + width, y + height);
    }

    Vector3 v1 = (transform * Vector3((float)x, (float)y, 0.0f)) - posAdjust;
    Vector3 v2 = (transform * Vector3((float)x + (float)width, (float)y, 0.0f)) - posAdjust;
    Vector3 v3 = (transform * Vector3((float)x, (float)y + (float)height, 0.0f)) - posAdjust;
    Vector3 v4 = (transform * Vector3((float)x + (float)width, (float)y + (float)height, 0.0f)) - posAdjust;

...
[/code]

If this could provide full 3d positioning of the quad, it seems like this would go a long way towards 3d camera space ui. Doesn't handle occluding geometry, though...

-------------------------

cadaver | 2017-01-02 01:14:25 UTC | #15

The problem with free form UI transform is that you can no longer use scissor, which means listviews etc. would not be able to mask the scrolling content properly. To keep things working right I'd rather recommend rendering to a texture first. 

Naturally that will cause a video RAM problem if you have for example a building with 100's of computer screens and each allocates its own unique texture, so in that case a more advanced allocation system is needed, that throws out the unneeded UI textures.

-------------------------

godan | 2017-01-02 01:14:25 UTC | #16

Just to pursue the UI transform a bit more: What about resizing the Scissor to the projected transform/quad size? Or even, just use whatever Scissor was calculated before transforming the quad. For sure, in the worst case, the quad while be positioned such that the scissor is not too effective. But on the other hand, the Scissor test should still catch conditions like the UI element being off screen, or lots and lots of text not being inside the UI size, etc...Basically, you just do the scissor test on the inverse of the transform.

-------------------------

cadaver | 2017-01-02 01:14:25 UTC | #17

It's a fixed hardware feature and only rectangular, so it wouldn't work for example with a ListView rotated 45 degrees, and you'd have items leaking out. I don't even care for optimization in that regard, but correctness.

-------------------------

