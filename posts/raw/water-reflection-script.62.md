szamq | 2017-01-02 00:57:42 UTC | #1

I implemented some handy water reflection scriptinstance class which can be added in the editor. Mostly it's copied from 23_Water with some tweaks.

Features:
- Create water reflection just by adding one component to the node
- Multiple water reflection surfaces supported
- Reflection will work after saving and loading

Usage:
add it as ScriptInstance component to a node with StaticModel

Hierarchy:
-node
--StaticModel
--ScriptInstance (WaterReflection)

Edit: Changed Start to DelayedStart. Does anyone know why Start creates null pointer exception after loading scene? It should work because components are created at creation time, but it says that reflectionCamera is null.

[code]
class WaterReflection : ScriptObject
{
	Node@ reflectionCameraNode;
	Camera@ reflectionCamera;
    WaterReflection(){}
	
    void DelayedStart()
	{
		StaticModel@ water = node.GetComponent("StaticModel");
		Material@ waterMaterial = cache.GetResource("Material", "Materials/Water.xml");
		water.material=waterMaterial.Clone();
		// Set a different viewmask on the water plane to be able to hide it from the reflection camera
		water.viewMask = 0x80000000;

		reflectionCameraNode = renderer.viewports[0].camera.node.CreateChild();
		reflectionCameraNode.temporary=true;
		reflectionCamera = reflectionCameraNode.CreateComponent("Camera");
		
		TransformChanged();
		
		reflectionCamera.farClip = 750.0;
		reflectionCamera.viewMask = 0x7fffffff; // Hide objects with only bit 31 in the viewmask (the water plane)
		reflectionCamera.autoAspectRatio = false;
		reflectionCamera.useReflection = true;
		reflectionCamera.useClipping = true; 
		reflectionCamera.aspectRatio = float(graphics.width) / float(graphics.height);
		reflectionCamera.viewOverrideFlags = VO_DISABLE_SHADOWS;
		
		int texSize = 1024;
		Texture2D@ renderTexture = Texture2D();
		renderTexture.SetSize(texSize, texSize, GetRGBFormat(), TEXTURE_RENDERTARGET);
		renderTexture.filterMode = FILTER_BILINEAR;
		RenderSurface@ surface = renderTexture.renderSurface;
		Viewport@ rttViewport = Viewport(renderer.viewports[0].scene, reflectionCamera);
		surface.viewports[0] = rttViewport;
		water.materials[0].textures[TU_DIFFUSE] = renderTexture;
	}
	
	void Update(float timestep)
	{
		reflectionCamera.aspectRatio = float(graphics.width) / float(graphics.height);
	}
	
	void TransformChanged()
	{
		StaticModel@ water = node.GetComponent("StaticModel");
		float delta=(water.worldBoundingBox.max.y - water.worldBoundingBox.min.y)/2.f;
		Plane waterPlane = Plane(node.worldRotation * Vector3(0.0f, 1.0f, 0.0f), node.worldPosition+Vector3(0.0f, delta, 0.0f));
		Plane waterClipPlane = Plane(node.worldRotation * Vector3(0.0f, 1.0f, 0.0f), node.worldPosition +	Vector3(0.0f,delta- 0.1f, 0.0f));
		reflectionCamera.reflectionPlane = waterPlane;
		reflectionCamera.clipPlane = waterClipPlane;
	}
}
[/code]

-------------------------

