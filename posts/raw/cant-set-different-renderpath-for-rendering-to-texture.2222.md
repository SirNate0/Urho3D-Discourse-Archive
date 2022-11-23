krstefan42 | 2017-01-02 01:14:01 UTC | #1

I'm trying to render to a texture using a RenderPath with just a fullscreen quad command (to generate a procedural heightmap for a terrain vertex shader). However, it doesn't seem to matter what I set the RenderPath to for the RTT viewport, it always uses the same RenderPath as the backbuffer. The code is like this(mostly copied from the renderToTexture lua sample code):
[code]
	scene_ = Scene()
	scene_:CreateComponent("Octree")
	
	local rttCameraNode =  scene_:CreateChild("Camera2")
	local rttCam = rttCameraNode:CreateComponent("Camera")
	
	local renderTexture = Texture2D:new()
	renderTexture:SetSize(2048, 2048, Graphics:	GetRGBA16Format(), TEXTURE_RENDERTARGET)
	
	
	local surface = renderTexture.renderSurface
	local rttViewport = Viewport:new( scene_, rttCameraNode:GetComponent("Camera"))
	surface:SetViewport(0, rttViewport)
	rttViewport.renderPath:Load(cache:GetResource("XMLFile", "RenderPaths/RenderTerrainHeightMap.xml"));	 
	
	local screenNode = scene_:CreateChild("Screen")
	local screenObject = screenNode:CreateComponent("StaticModel")
	screenObject.model = cache:GetResource("Model", "Models/Plane.mdl")
	
	local renderMaterial = Material:new()
	renderMaterial:SetTechnique(0, cache:GetResource("Technique", "Techniques/DiffUnlit.xml"))
	renderMaterial:SetTexture(TU_DIFFUSE, renderTexture)
	screenObject.material = renderMaterial

	cameraNode = scene_:CreateChild("Camera")
	local camera = cameraNode:CreateComponent("Camera")

	local viewport = Viewport:new(scene_, camera)
	viewport.renderPath:Load(cache:GetResource("XMLFile", "RenderPaths/SSAO.xml"));	 
	renderer:SetViewport(0,viewport)
[/code]
I don't think the problem is with the RenderPath file, because even setting the RTT viewport RenderPath to one of the built-in ones doesn't seem to work (the rendered texture still has the SSAO effect applied from my SSAO RenderPath that I'm using for the backbuffer).

-------------------------

cadaver | 2017-01-02 01:14:01 UTC | #2

When you create a viewport without specifying a renderpath object, it gets the default renderpath from Renderer. So you're essentially editing the same renderpath object in 2 places.
You can either first create the new renderpath, then create the viewport specifying it, or assign it later.

-------------------------

krstefan42 | 2017-01-02 01:14:01 UTC | #3

Thanks. How do you call the constructor for RenderPath in lua? RenderPath:new(), RenderPath(), etc, don't seem to work. 

I tried renderer.DefaultRenderPath:Clone() as a workaround, but it doesn't seem to actually create a unique Renderpath; I still get the same problem as before.

EDIT: I figured out I can use Viewport:SetRenderPath. So everything's good now.

-------------------------

