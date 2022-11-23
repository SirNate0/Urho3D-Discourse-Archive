NiteLordz | 2017-01-02 01:14:40 UTC | #1

Currently, i have an animated model walking around a room that has a marble floor. i would like to add reflection to the marble floor.  However, i am not good with the materials and techniques to know how to build this.  Can anyone point me in the correct direction?

-------------------------

cadaver | 2017-01-02 01:14:40 UTC | #2

See 23_Water example. Note that Urho doesn't support oldschool stencil buffer reflections, since stencil is used for light optimization instead, so you always need to render to texture and sample that appropriately in the material.

-------------------------

NiteLordz | 2017-01-02 01:14:40 UTC | #3

Can this be done within the Editor?

from what it appears, you would create a child node to main camera, enable reflection, clipping and set the clip plane.

set view mask on the floor (in my case).

The problem is, i don't know how to set a RenderTexture within the Editor.

-------------------------

cadaver | 2017-01-02 01:14:40 UTC | #4

I'd do that with an active script in some scene object that sets up the reflection rendering, and keeps updating the reflection camera. There's nothing in the editor itself that would setup rendertextures.

-------------------------

NiteLordz | 2017-01-02 01:14:43 UTC | #5

[quote="cadaver"]I'd do that with an active script in some scene object that sets up the reflection rendering, and keeps updating the reflection camera. There's nothing in the editor itself that would setup rendertextures.[/quote]

I setup a script, and i have reflections working.  When the scene is loaded from an external application, and runs, the reflections work properly. This works great for the compiled *.exe.  however, i am curious as to why the script doesn't display the reflection within the editor? 

Here is the script
[code]class Reflection : ScriptObject {
	Plane reflectionPlane;

	void Start() {
		reflectionPlane = Plane(Vector3(0.0f, 1.0f, 0.0f), Vector3(0.0f, 0.0f, 0.0f));

		int texSize = 1024;

		Texture2D@ renderTexture = Texture2D();
		renderTexture.SetSize(texSize, texSize, GetRGBFormat(), TEXTURE_RENDERTARGET);
		renderTexture.filterMode = FILTER_BILINEAR;

		RenderSurface@ surface = renderTexture.renderSurface;

		Camera@ reflectionCamera = node.GetComponent("Camera");
		reflectionCamera.reflectionPlane = reflectionPlane;
		reflectionCamera.aspectRatio = float(graphics.width) / float(graphics.height);

		Viewport@ rttViewport = Viewport(script.defaultScene, reflectionCamera);
		surface.viewports[0] = rttViewport;

		Material@ marbleTile = cache.GetResource("Material", "Materials/MarbleTile.material");
		marbleTile.textures[TU_ENVIRONMENT] = renderTexture;
	}

    void Update(float timeStep) {
        Camera@ reflectionCamera = node.GetComponent("Camera");
		reflectionCamera.aspectRatio = float(graphics.width) / float(graphics.height);
    }
}[/code]

-------------------------

cadaver | 2017-01-02 01:14:43 UTC | #6

Editor has its own cameras / viewports, do you take that into account when positioning the reflection camera? You could get to them via the Renderer subsystem.

To be honest, anytime you write scripts that should cooperate with the editor, it's going to get somewhat messy.

-------------------------

NiteLordz | 2017-01-02 01:14:43 UTC | #7

I have a reflection camera component assigned to a node, which is a child of "Main Camera" node, not the editor camera. When clicking on the Main Camera node, preview displays, showing the models on the marble floor, but the reflection is not there. The reflection script is assigned to the the reflection camera node.

-------------------------

cadaver | 2017-01-02 01:14:44 UTC | #8

Testing this simple script with a scene saved from the Water example didn't exhibit problems to view it in the editor's camera preview. Note that it's not perfect, the viewmasking / clipping doesn't go correctly, but I could see the reflection being rendered (or even preview the reflection camera in the editor)

[code]
class Reflection : ScriptObject
{

    private Node@ reflectionCameraNode;
    float height = 1.0f;

    void Start()
    {
        // Create a mathematical plane to represent the water in calculations
        Plane waterPlane(Vector3(0.0f, 1.0f, 0.0f), Vector3(0,height,0));
        // Create a downward biased plane for reflection view clipping. Biasing is necessary to avoid too aggressive clipping
        Plane waterClipPlane(Vector3(0.0f, 1.0f, 0.0f), Vector3(0.0f, height - 0.1f, 0.0f));

        // Create camera for water reflection
        // It will have the same farclip and position as the main viewport camera, but uses a reflection plane to modify
        // its position when rendering
        reflectionCameraNode = node.CreateChild();
        Camera@ reflectionCamera = reflectionCameraNode.CreateComponent("Camera");
        reflectionCamera.farClip = 750.0;
        reflectionCamera.viewMask = 0x7fffffff; // Hide objects with only bit 31 in the viewmask (the water plane)
        reflectionCamera.autoAspectRatio = false;
        reflectionCamera.useReflection = true;
        reflectionCamera.reflectionPlane = waterPlane;
        reflectionCamera.useClipping = true; // Enable clipping of geometry behind water plane
        reflectionCamera.clipPlane = waterClipPlane;
        // The water reflection texture is rectangular. Set reflection camera aspect ratio to match
        reflectionCamera.aspectRatio = float(graphics.width) / float(graphics.height);

        // Create a texture and setup viewport for water reflection. Assign the reflection texture to the diffuse
        // texture unit of the water material
        int texSize = 1024;
        Texture2D@ renderTexture = Texture2D();
        renderTexture.SetSize(texSize, texSize, GetRGBFormat(), TEXTURE_RENDERTARGET);
        renderTexture.filterMode = FILTER_BILINEAR;
        RenderSurface@ surface = renderTexture.renderSurface;
        Viewport@ rttViewport = Viewport(scene, reflectionCamera);
        surface.viewports[0] = rttViewport;
        Material@ waterMat = cache.GetResource("Material", "Materials/Water.xml");
        waterMat.textures[TU_DIFFUSE] = renderTexture;
    }
}
[/code]

-------------------------

NiteLordz | 2017-01-02 01:14:44 UTC | #9

Yea, i am able to see the reflection in the reflection camera, but not when viewing the main camera preview, which should have the character on top of the floor with reflection.  

back to drawing board :slight_smile:

-------------------------

NiteLordz | 2017-01-02 01:14:44 UTC | #10

I think i figured out my problem.  I am using script.defaultScene when i set the viewport (which is launching from a script), but if not launching from a script, defaultScene never gets set, so there is no viewport to be used for the reflection.

in this case, how can i get access to the scene?  i noticed in your example, you use "scene" which i expect is defined in another class somewhere.  

i only have one script file, the reflection class), which doesn't have access to a global scene object, unless i am missing something somewhere.

have confirmed that scene is null when creating the viewport, as the scene file loads, executes the script, before i can set the default scene.  i know there is a DelayedExecute method, but i am struggling to figure out how to make it work.

Figured out it was a lot simpler than i was doing.  called DelayedStart() instead of Start, allows me to set the default scene from the c++ side, and bobs your uncle, reflections showing properly!

-------------------------

cadaver | 2017-01-02 01:14:44 UTC | #11

For a script object located in a node, the global property "scene" is automatically filled to allow access to the scene the node resides in.

-------------------------

