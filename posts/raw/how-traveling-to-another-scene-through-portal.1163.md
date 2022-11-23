codingmonkey | 2017-06-29 09:39:58 UTC | #1

Hi, folks!
i'm curious how to may be created this effect ?
[url=http://savepic.su/5782786.htm][img]http://savepic.su/5782786m.png[/img][/url]

two world and Character may going into another world through this portal.

how this may be created in urho3d ? 
do you think is this needs some working around stencil buffer things or just place rendered texture from another camera from background scene ?

-------------------------

cadaver | 2017-01-02 01:05:48 UTC | #2

Urho doesn't so far expose stencil buffer for user customizable rendering, rather it uses it for internal rendering optimizations. But you can use render-to-texture. Look at the example 10_RenderToTexture.

-------------------------

codingmonkey | 2017-01-02 01:05:49 UTC | #3

>But you can use render-to-texture
yes, but it's will be look weird I guess in some angles, because spectator may change it own position in world ( point of view ) then he looked on this portal effect.

Is it possible to render portal mesh into mask texture like this:
[url=http://savepic.su/5819687.htm][img]http://savepic.su/5819687m.png[/img][/url]
then use this mask to combine two render-textures from both world into one final image ?

how render path may be looked for this technique ?
and I guess that we need special post fx shader to combine (this two render-textures by mask) at last stage

-------------------------

setzer22 | 2017-01-02 01:05:49 UTC | #4

[quote="codingmonkey"]Is it possible to render portal mesh into mask texture like this:
[url=http://savepic.su/5819687.htm][img]http://savepic.su/5819687m.png[/img][/url]
then use this mask to combine two render-textures from both world into one final image ?

how render path may be looked for this technique ?
and I guess that we need special post fx shader to combine (this two render-textures by mask) at last stage[/quote]

What you describe is exactly what the stencil buffer does, too bad it's already being used for other stuff. As far as I know this technique can't be easily achieved in any other way.

-------------------------

cadaver | 2017-01-02 01:05:49 UTC | #5

Your realistic best bet is probably just to dig in and modify Urho's scene rendering code to do what you want, then see if it can be contributed as a pull request that doesn't breaking existing functionality.

-------------------------

Bananaft | 2017-01-02 01:05:50 UTC | #6

[quote="codingmonkey"]>But you can use render-to-texture
yes, but it's will be look weird I guess in some angles, because spectator may change it own position in world ( point of view ) then he looked on this portal effect.
[/quote]

1) Update position of a camera that renders to texture, making it the same as spectators position relative to the camera in each frame.
2) Change portal,s shader so it will apply rendered texture in screen coordinates (instead of UVs).

That's should do this exact effect with render to texture.

-------------------------

codingmonkey | 2017-06-29 08:10:31 UTC | #7

[quote]1) Update position of a camera that renders to texture, making it the same as spectators position relative to the camera in each frame.
2) Change portal,s shader so it will apply rendered texture in screen coordinates (instead of UVs).[/quote]

Yeah, i'm almost  execute this todo list :slight_smile: but with last position I have a some problems. 
Do you mean  (in screen coordinates (instead of UVs) - use screen position of rectangle(portal) as texCoords or you mean something else ?

today i'm trying to set oTexCoord like that:
UnlitSS shader
[code]
   #ifdef NOUV
    float2 iTexCoord = float2(0.0, 0.0);
    #endif

    float4x3 modelMatrix = iModelMatrix;
    float3 worldPos = GetWorldPos(modelMatrix);
    oPos = GetClipPos(worldPos);
    //oTexCoord = GetTexCoord(iTexCoord);
	oTexCoord = GetScreenPosPreDiv(oPos);
	//oTexCoord = GetQuadTexCoord(oPos);

	oWorldPos = float4(worldPos, GetDepth(oPos));
	//oPos = GetScreenPos(worldPos);
[/code]

but it's still far from expected effect

https://www.youtube.com/watch?v=79fcu-mO0GQ

there is I gotten some portal (diagonal) issue

-------------------------

codingmonkey | 2017-01-02 01:05:54 UTC | #8

ok, how i'm want to try another method
based on RenderPath commands with custom quad shader who join x3 RT-textures(cam1, mask, cam2) in to one final image
but i'm don't know how to setup these 3x RenderTargets into <command type="quad" as parameters for shader ? any ideas ?

-------------------------

cadaver | 2017-01-02 01:05:54 UTC | #9

[code]
<command type="quad" vs="MyShader" ps="MyShader">
        <texture unit="0" name="cam1" />
        <texture unit="1" name="mask" />
        <texture unit="2" name="cam2" />
</command>
[/code]

Note: to have access to the RT textures from several different renderpaths, you must create them manually, name them (e.g. tex->SetName("cam1")) and store into ResourceCache with ResourceCache::AddManualResource(tex). If you create them with the RT definition elements inside a renderpath xml, the access is restricted to the same renderpath only.

-------------------------

codingmonkey | 2017-01-02 01:05:56 UTC | #10

for debug viewing (that i got in RT) i needed to save several renderTargets into image files, how I may do this ? 

I trying to save like this, but not found any saved file in dir
[code]
void World::SaveFrame(String fileName)
{
	if (renderTexture) 
	{
		File fileImage(context, context->GetSubsystem<FileSystem>()->GetProgramDir() + "Data/Textures/" + fileName, FILE_WRITE);
		renderTexture->Save(fileImage);
	}

}
[/code]

i'm also find a Graphic->TakeScreenShot(image destination) but it save only actual viewport I guess.

-------------------------

codingmonkey | 2017-01-02 01:05:56 UTC | #11

ok I solve previous problem like this.

[code]
void World::SaveFrame(String fileName)
{
	
	if (renderTexture) 
	{
		Renderer* renderer = context->GetSubsystem<Renderer>();
		Viewport* prevVp = renderer->GetViewport(0);
		renderer->SetViewport(0, camera.vp);
		Graphics* graphic = context->GetSubsystem<Graphics>();
		
		SharedPtr<Image> img = SharedPtr<Image>(new Image(context));
		img->SetSize(graphic->GetWidth(), graphic->GetHeight(), 3);
		
		
		Engine* eng = context->GetSubsystem<Engine>();
		eng->RunFrame();
		eng->Render();

		graphic->TakeScreenShot((*img));

	
		img->SavePNG(context->GetSubsystem<FileSystem>()->GetProgramDir() + fileName);

		renderer->SetViewport(0, prevVp);

	}


}

[/code]


and there is next strange thing that I got.
this is world of portals(it used only as RT-mask texture, it copy transform of camera from another worlds), and it must look similar in RT
[url=http://savepic.su/5832446.htm][img]http://savepic.su/5832446m.png[/img][/url]

but in RT it looks like this

[url=http://savepic.ru/7557981.htm][img]http://savepic.ru/7557981m.png[/img][/url]

why ? i'm use for spheres noTextureUnlit render tech with full white diffuse color

-------------------------

codingmonkey | 2017-01-02 01:05:56 UTC | #12

ok last problem also has been solved. I don't know why but editor does not update in last time saved material (his render tech). 
now I guess all is ok

[url=http://savepic.su/5814003.htm][img]http://savepic.su/5814003m.png[/img][/url]

-------------------------

codingmonkey | 2017-01-02 01:05:56 UTC | #13

now i'm have some problems with black screen instead mixed frame

I create for each world namedRT texture and add it to cache manualy
[code]
void World::CreateNamedRT(String worldName) 
{
	Graphics* g = context->GetSubsystem<Graphics>();
	int w = g->GetWidth();
	int h = g->GetHeight();

	renderTexture = SharedPtr<Texture2D>(new Texture2D(context));

	if (renderTexture) 
	{
		renderTexture->SetSize(w, h, Graphics::GetRGBFormat(), TEXTURE_RENDERTARGET);
		renderTexture->SetFilterMode(FILTER_BILINEAR);
		renderTexture->SetName(worldName);

		RenderSurface* surface = renderTexture->GetRenderSurface();
		surface->SetViewport(0, camera.vp);

		ResourceCache* cache = context->GetSubsystem<ResourceCache>();
		cache->AddManualResource(renderTexture);
	}
}
[/code]

[code]

		// usial worlds
		worlds[WORLD_A].InitScene(context_, "WorldA.xml", WORLD_A);
		worlds[WORLD_A].SetupPlayer();
		worlds[WORLD_A].CreateNamedRT("WorldA");

		worlds[WORLD_B].InitScene(context_, "WorldB.xml", WORLD_B);
		worlds[WORLD_B].SetupPlayer();
		worlds[WORLD_B].CreateNamedRT("WorldB");

		// world with portal mesh
		worlds[WORLD_P].InitScene(context_, "WorldP.xml", WORLD_P);
		worlds[WORLD_P].SetupPlayer();
		worlds[WORLD_P].CreateNamedRT("WorldP");
[/code]

only for test i'm append to active visible viewport a part with new RenderPath
[code]
		worlds[WORLD_A].SetCurrent();
		// add PrenderPath

		rp = SharedPtr<RenderPath>((worlds[WORLD_A].camera.vp->GetRenderPath()->Clone()));
		rp->Append(cache->GetResource<XMLFile>("PostProcess/Portal.xml"));
		worlds[WORLD_A].camera.vp->SetRenderPath(rp);

[/code]

where is portal.xml
[code]
<renderpath>
    <command type="quad" vs="Portal" ps="Portal" output="viewport" >
        <texture unit="0" name="WorldA" />
        <texture unit="1" name="WorldP" />
        <texture unit="2" name="WorldB" />
    </command>
</renderpath>
[/code]

and his shader portal.hlsl

[code]
#include "Uniforms.hlsl"
#include "Samplers.hlsl"
#include "Transform.hlsl"
#include "ScreenPos.hlsl"
#include "Lighting.hlsl"

void VS(float4 iPos : POSITION,
    out float2 oScreenPos : TEXCOORD0,
    out float4 oPos : OUTPOSITION)
{
    float4x3 modelMatrix = iModelMatrix;
    float3 worldPos = GetWorldPos(modelMatrix);
    oPos = GetClipPos(worldPos);
    oScreenPos = GetScreenPosPreDiv(oPos);
}

void PS(float2 iScreenPos : TEXCOORD0,
    out float4 oColor : OUTCOLOR0)
{
	// DiffMap - WorldA = tex unit 0
	// NormalMap - WorldP = tex unit 1
	// SpecMap - WorldB = tex unit 2

	float3 MaskRgb = Sample2D(NormalMap, iScreenPos).rgb;
	
	float MaskIntensity = GetIntensity(MaskRgb);
	
	float3 Wa = Sample2D(DiffMap, iScreenPos).rgb;
	float3 Wb = Sample2D(SpecMap, iScreenPos).rgb;

	oColor = float4(lerp(Wa, Wb, MaskIntensity), 1.0);
}
[/code]

in the log i'm don't see any of shaders error, i mean that all loading is ok
also I checkout for all worlds RT (make screenshots) and only one - first have a fully black color

but why is black? any ideas ?

ps. if I change shader with output line like this 
oColor = float4(1.0, 1.0, 1.0, 1.0); the screen will be - white. 
but if I make changes like: 
oColor = float4(MaskRgb, 1.0); or oColor = float4(Wa, 1.0); or oColor = float4(Wb, 1.0); 
it still will be fully black

-------------------------

codingmonkey | 2017-06-29 08:39:03 UTC | #14

May I ask? Is this first tree commands to create three RT or no ?

https://pastebin.com/5kHsBzSL

if this command to create three RT why I couldn't access to each of them from Resource Cache ?

https://pastebin.com/y7Kx9KXT

-------------------------

cadaver | 2017-01-02 01:05:57 UTC | #15

The rendertargets you define with rendertarget elements in the renderpath are allocated internally without going into the resource cache, and therefore you can't access them from your code or from other renderpaths. (This is to allow reuse of renderpaths in different viewports without having resource conflicts.) Thought I explained that before in the thread. Rather you need to create the textures yourself, name them, store them. And don't include the rendertarget definitions at all in the renderpath.

-------------------------

codingmonkey | 2017-01-02 01:05:58 UTC | #16

>Rather you need to create the textures yourself, name them, store them
I do exactly as you say. I create 3x RT and add these RT manually to cache but screen is black.  
Shader fill screen with manual established colors, but do not mix these RTs and i guessing what it do not see these RTs. 
And that why a decide create RT by another path.

-------------------------

cadaver | 2017-01-02 01:05:58 UTC | #17

You could debug into the function View::FindNamedTexture() which is used to find both rendertargets and textures when the renderpath gets executed, and see if you can spot what is going wrong.

-------------------------

codingmonkey | 2017-01-02 01:05:58 UTC | #18

there is one another question:
Is it possible to use exact same one RT as for output(for viewport) and as one of RTs for reading in shader ?
in my trying(example) I use worldA-RT as output and in same time use this worldA-RT as RT for reading in shader as unit0(diffuse)

-------------------------

cadaver | 2017-01-02 01:05:58 UTC | #19

Using the same texture both for rendering and sampling at the same time is illegal. The "viewport" output is a bit special as the View class handles automatic pingponging of it to 2 RT textures as necessary.

With custom defined RT's other than "viewport", you have to manage the pingponging manually.

-------------------------

codingmonkey | 2017-01-02 01:05:58 UTC | #20

i suppose that i need create a fourth RT for main screen (view) and set to only it (renderer.SetViewport(0, mainVp))
other 3x RT will be offscreen with standart RenderPath (Forward.xml)
and only main RT will be use my custom RenderPath (Portal.xml with quad commands) and mix these 3x offscreened RTs. 
i will try do this...

-------------------------

codingmonkey | 2017-01-02 01:05:58 UTC | #21

i'm just curious if i bind the main view to index=0 in Renderer->SetViewport(0, mainViewport)

which index i should use to other RTs ? 1,2,3 ?
 
or maybe i should use inverted indexes because last rendered viewport are visible on screen

maybe i should use  0,1,2 index for worlds and mask and last index = 3 for mainViewport ?

in my logic: render do rendering each of them into worlds and mask RTs and finally do rendering  index = 3 with mainViewport (quad mix RTs shader) 
is this rendering method are possible or I something missed ?

-------------------------

cadaver | 2017-01-02 01:05:58 UTC | #22

The Renderer viewports always render to the backbuffer (window), so don't try to use them for the RT textures. Instead, from a RT texture you can get the RenderSurface object, where you configure the viewport/scene/renderpath, and how it should update.

The RT viewports will update before the backbuffer, so when you perform the final compositing in the backbuffer's viewport/renderpath, the RT's should be up to date.

-------------------------

codingmonkey | 2017-06-29 08:40:20 UTC | #23

Thanks, [b]cadaver[/b] now I found this %... error that blowing my mind in last two days :slight_smile:

there is
[code]surface->SetUpdateMode(RenderSurfaceUpdateMode::SURFACE_UPDATEVISIBLE); [/code]
by default parameter it update offscreen RTs only if they are visible (RenderSurfaceUpdateMode::SURFACE_UPDATEVISIBLE) 
and guess what? yes - they are invisible because they placed in other scenes )

i'm change this to
[code]surface->SetUpdateMode(RenderSurfaceUpdateMode::SURFACE_UPDATEALWAYS); [/code]
and now I see portal to another scene(world), cool! 

https://pastebin.com/YR7AWKAv

I guessing that now time to polish and do some optimization...

http://www.youtube.com/watch?v=Ejtlz5hoOVE

-------------------------

cadaver | 2017-01-02 01:05:59 UTC | #24

Congrats for getting it working!

-------------------------

codingmonkey | 2017-06-29 09:39:41 UTC | #25

add visible obstacles what close portals. just clone all static object from player's world to portal's world with full black material


https://pastebin.com/mQ1Yw7XG

https://youtu.be/47DRfr1QJ9o

but now on the contours of object I got a strange white tail in 1pix, and it visible only where skybox rendered

just for curious in this
link to repo: [github.com/MonkeyFirst/Urho3DPo ... ssFXPortal](https://github.com/MonkeyFirst/Urho3DPostProcessFXPortal)

-------------------------

