v0van1981 | 2017-01-02 01:05:35 UTC | #1

like selection in Diablo 3 and Dota 2

examples [forum.unity3d.com/threads/highli ... ed.143043/](http://forum.unity3d.com/threads/highlighting-system-released.143043/)
[i40.tinypic.com/a0yxaa.png](http://i40.tinypic.com/a0yxaa.png)
[hydra-media.cursecdn.com/dota2.g ... d30b982593](http://hydra-media.cursecdn.com/dota2.gamepedia.com/thumb/2/25/Unit_highlighting.gif/180px-Unit_highlighting.gif?version=9f55206c423a76b18280e3d30b982593)
[i.imgur.com/WVE3f.jpg](http://i.imgur.com/WVE3f.jpg)

algorithm from [habrahabr.ru/post/157447/](http://habrahabr.ru/post/157447/)
1) render model to texture [imageshack.us/a/img834/2183/highlights.jpg](http://imageshack.us/a/img834/2183/highlights.jpg)
2) blur
3) blurred image minus original texrure
4) out result over scene

i try realise it, but I do not know much engine and shader language

added:
also i find [stackoverflow.com/questions/2326 ... ngl-es-3-0](http://stackoverflow.com/questions/23260853/inner-and-outer-glow-implementation-using-opengl-es-3-0)

-------------------------

GoogleBot42 | 2017-01-02 01:05:35 UTC | #2

Here you go :wink:: [url]http://nervegass.blogspot.com/2014/12/urho-shaders-edge-detection.html[/url]

-------------------------

v0van1981 | 2017-01-02 01:05:35 UTC | #3

Thank you

-------------------------

1vanK | 2017-01-02 01:07:07 UTC | #4

[github.com/1vanK/Urho3DOutline](https://github.com/1vanK/Urho3DOutline)

[url=http://savepic.su/6098764.htm][img]http://savepic.su/6098764m.jpg[/img][/url]

-------------------------

rasteron | 2017-01-02 01:07:07 UTC | #5

Thanks for sharing 1vank :slight_smile: I'm looking for something like this as well. 

Some questions:

- how do you make the outline more of a solid color, like in toon effect?
- Can this be created with a pure material shader solution? I see you need to clone the object to produce the effect.

-------------------------

1vanK | 2017-01-02 01:07:08 UTC | #6

[quote="rasteron"]Thanks for sharing 1vank :) I'm looking for something like this as well. 

One question though, how do you make the outline more of a solid color, like in toon effect?[/quote]

This is not feature, this is bug xD A lot of blur
[code]
    vec4 blurredMask = GaussianBlur(3, vec2(0.0, 1.0), vec2(0.008, 0.008), 2.0, sNormalMap, vScreenPosInv);
    blurredMask = blurredMask + GaussianBlur(3, vec2(1.0, 0.0), vec2(0.008, 0.008), 2.0, sNormalMap, vScreenPosInv);
    blurredMask = blurredMask + GaussianBlur(3, vec2(0.0, 1.0), vec2(0.004, 0.004), 2.0, sNormalMap, vScreenPosInv);
    blurredMask = blurredMask + GaussianBlur(3, vec2(1.0, 0.0), vec2(0.004, 0.004), 2.0, sNormalMap, vScreenPosInv);
[/code]

If you want to fully solid color change shader

[code]
void PS()
{
    vec3 rgb = texture2D(sDiffMap, vScreenPos).rgb;
    vec3 mask = texture2D(sNormalMap, vScreenPosInv).rgb;      

    vec4 blurredMask = GaussianBlur(3, vec2(0.0, 1.0), vec2(0.008, 0.008), 2.0, sNormalMap, vScreenPosInv);
    blurredMask = blurredMask + GaussianBlur(3, vec2(1.0, 0.0), vec2(0.008, 0.008), 2.0, sNormalMap, vScreenPosInv);
    blurredMask = blurredMask + GaussianBlur(3, vec2(0.0, 1.0), vec2(0.004, 0.004), 2.0, sNormalMap, vScreenPosInv);
    blurredMask = blurredMask + GaussianBlur(3, vec2(1.0, 0.0), vec2(0.004, 0.004), 2.0, sNormalMap, vScreenPosInv);
        
    if (mask.rgb == vec3(1.0, 1.0, 1.0))
        gl_FragColor = vec4(rgb, 1.0);
    else if (GetIntensity(blurredMask.rgb) > 0.01)
        gl_FragColor = vec4(0.0, 1.0, 0.0, 1.0);
    else
        gl_FragColor = vec4(rgb, 1.0);
}
[/code]

[url=http://savepic.su/6104899.htm][img]http://savepic.su/6104899m.jpg[/img][/url]

Edit:The object is cloned to another scene to receive his mask may be exist a different method

-------------------------

jmiller | 2017-01-02 01:07:08 UTC | #7

Looks nice! Thanks for sharing.

Here's yet another approach using a stencil buffer, which may be too specific to their SDK but maybe another thing to search on.
[developer.valvesoftware.com/wik ... low_Effect](https://developer.valvesoftware.com/wiki/L4D_Glow_Effect)

[img]http://i.imgur.com/tbo6OW3.jpg[/img]

-------------------------

rasteron | 2017-01-02 01:07:08 UTC | #8

Thanks 1vanK, it works great  :smiley: 

One more small issue that I seem to notice is when you view the effect away, it looks uneven and weird.

[img]http://i.imgur.com/ntxmHEF.png[/img]

still a great share, appreciate this.


[b]@Carnalis[/b]

Yes that effect on those valve games seems really nice!

-------------------------

1vanK | 2017-01-02 01:07:08 UTC | #9

[quote="rasteron"]Thanks 1vanK, it works great  :D 

One more small issue that I seem to notice is when you view the effect away, it looks uneven and weird.
[/quote]

This question of tuning. Perhaps even need to use another method of blur. Try

[code]
void PS()
{
    vec3 rgb = texture2D(sDiffMap, vScreenPos).rgb;
    vec3 mask = texture2D(sNormalMap, vScreenPosInv).rgb;      

    vec4 blurredMask = GaussianBlur(3, vec2(0.0, 1.0), vec2(0.008, 0.008), 2.0, sNormalMap, vScreenPosInv);
    blurredMask = blurredMask + GaussianBlur(3, vec2(1.0, 0.0), vec2(0.008, 0.008), 2.0, sNormalMap, vScreenPosInv);
    blurredMask = blurredMask + GaussianBlur(3, vec2(1.0, 1.0), vec2(0.008, 0.008), 2.0, sNormalMap, vScreenPosInv);
    blurredMask = blurredMask + GaussianBlur(3, vec2(1.0, 0.0), vec2(0.004, 0.004), 2.0, sNormalMap, vScreenPosInv);
    blurredMask = blurredMask + GaussianBlur(3, vec2(0.0, 1.0), vec2(0.004, 0.004), 2.0, sNormalMap, vScreenPosInv);
    blurredMask = blurredMask + GaussianBlur(3, vec2(1.0, 1.0), vec2(0.004, 0.004), 2.0, sNormalMap, vScreenPosInv);
            
    if (mask.rgb == vec3(1.0, 1.0, 1.0))
        gl_FragColor = vec4(rgb, 1.0);
    else if (GetIntensity(blurredMask.rgb) > 0.0)
        gl_FragColor = vec4(0.0, 1.0, 0.0, 1.0);
    else
        gl_FragColor = vec4(rgb, 1.0);
}
[/code]

-------------------------

rasteron | 2017-01-02 01:07:08 UTC | #10

..I'm still getting a deformed outline when viewed from a distance but it looks much better than the first version. Can you make the outline stay the same thickness or at least proportioned?

[img]http://i.imgur.com/jxorBYA.jpg[/img]

-------------------------

rasteron | 2017-01-02 01:07:08 UTC | #11

Btw, I tried converting this to Angelscript and it does not seem to have an effect. Let me know what I am missing here:

[code]
#include "Scripts/Utilities/Sample.as"

RenderSurface@ surface;
Scene@ outlineScene_;
Node@ outlineCameraNode_;
Node@ outlineNode;
Viewport@ outlineViewport;
Texture2D@ renderTexture;

void Start() {
  // Execute the common startup for samples
  SampleStart();
  // Create the scene content
  CreateScene();
  // Create the UI content
  CreateUI();
  // Setup the viewport for displaying the scene
  SetupViewport();
  // Hook up to the frame update and render post-update events
  SubscribeToEvents();
}

void CreateScene() {

  scene_ = Scene();
  // Create octree, use default volume (-1000, -1000, -1000) to (1000, 1000, 1000)
  // Also create a DebugRenderer component so that we can draw debug geometry
  scene_.CreateComponent("Octree");
  scene_.CreateComponent("DebugRenderer");
  // Create scene node & StaticModel component for showing a static plane
  Node@ planeNode = scene_.CreateChild("Plane");
  planeNode.scale = Vector3(100.0f, 1.0f, 100.0f);
  StaticModel@ planeObject = planeNode.CreateComponent("StaticModel");
  planeObject.model = cache.GetResource("Model", "Models/Plane.mdl");
  planeObject.material = cache.GetResource("Material", "Materials/StoneTiled.xml");
  // Create a Zone component for ambient lighting & fog control
  Node@ zoneNode = scene_.CreateChild("Zone");
  Zone@ zone = zoneNode.CreateComponent("Zone");
  zone.boundingBox = BoundingBox(-1000.0f, 1000.0f);
  zone.ambientColor = Color(0.4f, 0.5f, 0.8f);
  zone.fogColor = Color(0.4f, 0.5f, 0.8f);
  zone.fogStart = 100.0f;
  zone.fogEnd = 300.0f;
  // Create a directional light to the world. Enable cascaded shadows on it
  Node@ lightNode = scene_.CreateChild("DirectionalLight");
  lightNode.direction = Vector3(0.6f, -1.0f, 0.8f);
  Light@ light = lightNode.CreateComponent("Light");
  light.lightType = LIGHT_DIRECTIONAL;
  light.color = Color(0.6f, 0.5f, 0.2f);
  light.castShadows = true;
  light.shadowBias = BiasParameters(0.00025f, 0.5f);
  // Set cascade splits at 10, 50 and 200 world units, fade shadows out at 80% of maximum shadow distance
  light.shadowCascade = CascadeParameters(10.0f, 50.0f, 200.0f, 0.0f, 0.8f);
  Node@ ouNode = scene_.CreateChild("Mushroom");
  ouNode.position = Vector3(0.0f, 0.0f, 20.0f);
  ouNode.SetScale(1.5f + Random(2.0f));
  ouNode.rotation = Quaternion(0.0f, 360.0f, 0.0f);
  StaticModel@ ouObject = ouNode.CreateComponent("StaticModel");
  ouObject.model = cache.GetResource("Model", "Models/Mushroom.mdl");
  ouObject.material = cache.GetResource("Material", "Materials/Mushroom.xml");
  // Create the camera. Limit far clip distance to match the fog
  cameraNode = scene_.CreateChild("Camera");
  Camera@ camera = cameraNode.CreateComponent("Camera");
  cameraNode.position = Vector3(0.0f, 5.0f, 0.0f);
  
  outlineScene_ = Scene();
  outlineScene_.CreateComponent("Octree");
  
  outlineCameraNode_ = cameraNode.Clone();
  outlineCameraNode_.parent = outlineScene_;
}

void CreateUI() {
  // Create a Cursor UI element because we want to be able to hide and show it at will. When hidden, the mouse cursor will
  // control the camera, and when visible, it will point the raycast target
  XMLFile@ style = cache.GetResource("XMLFile", "UI/DefaultStyle.xml");
  Cursor@ cursor = Cursor();
  cursor.SetStyleAuto(style);
  ui.cursor = cursor;
  // Set starting position of the cursor at the rendering window center
}

void SetupViewport() {
  // Set up a viewport to the Renderer subsystem so that the 3D scene can be seen
  Viewport@ viewport = Viewport(scene_, cameraNode.GetComponent("Camera"));
  
  renderer.viewports[0] = viewport;
  RenderPath@ effectRenderPath = renderer.viewports[0].renderPath.Clone();
  effectRenderPath.Append(cache.GetResource("XMLFile", "PostProcess/Outline.xml"));
  effectRenderPath.Append(cache.GetResource("XMLFile", "PostProcess/FXAA3.xml"));
  renderer.viewports[0].renderPath = effectRenderPath;
  Texture2D@ renderTexture = Texture2D();
  renderTexture.SetSize(graphics.width, graphics.height, GetRGBFormat(), TEXTURE_RENDERTARGET);
  renderTexture.filterMode = FILTER_NEAREST;
  renderTexture.name = "OutlineMask";
  cache.AddManualResource(renderTexture);
  RenderSurface@ surface = renderTexture.renderSurface;
  surface.updateMode = SURFACE_UPDATEALWAYS;
  outlineViewport = Viewport(outlineScene_, outlineCameraNode_.GetComponent("Camera"));
  surface.viewports[0] = outlineViewport;
}

void SubscribeToEvents() {
  // Subscribe HandleUpdate() function for processing update events
  SubscribeToEvent("Update", "HandleUpdate");
  // Subscribe HandlePostRenderUpdate() function for processing the post-render update event, during which we request
  // debug geometry
  SubscribeToEvent("PostRenderUpdate", "HandlePostRenderUpdate");
}

void MoveCamera(float timeStep) {
  // Right mouse button controls mouse cursor visibility: hide when pressed
  ui.cursor.visible = !input.mouseButtonDown[MOUSEB_RIGHT];
  // Do not move if the UI has a focused element (the console)
  if (ui.focusElement!is null) return;
  // Movement speed as world units per second
  const float MOVE_SPEED = 20.0f;
  // Mouse sensitivity as degrees per pixel
  const float MOUSE_SENSITIVITY = 0.1f;
  // Use this frame's mouse motion to adjust camera node yaw and pitch. Clamp the pitch between -90 and 90 degrees
  // Only move the camera when the cursor is hidden
  if (!ui.cursor.visible) {
    IntVector2 mouseMove = input.mouseMove;
    yaw += MOUSE_SENSITIVITY * mouseMove.x;
    pitch += MOUSE_SENSITIVITY * mouseMove.y;
    pitch = Clamp(pitch, -90.0f, 90.0f);
    // Construct new orientation for the camera scene node from yaw and pitch. Roll is fixed to zero
    cameraNode.rotation = Quaternion(pitch, yaw, 0.0f);
  }
  // Read WASD keys and move the camera scene node to the corresponding direction if they are pressed
  if (input.keyDown['W']) cameraNode.Translate(Vector3(0.0f, 0.0f, 1.0f) * MOVE_SPEED * timeStep);
  if (input.keyDown['S']) cameraNode.Translate(Vector3(0.0f, 0.0f, -1.0f) * MOVE_SPEED * timeStep);
  if (input.keyDown['A']) cameraNode.Translate(Vector3(-1.0f, 0.0f, 0.0f) * MOVE_SPEED * timeStep);
  if (input.keyDown['D']) cameraNode.Translate(Vector3(1.0f, 0.0f, 0.0f) * MOVE_SPEED * timeStep);
  // Toggle debug geometry with space
  if (input.keyPress[KEY_SPACE]) drawDebug = !drawDebug;
}

void HandleUpdate(StringHash eventType, VariantMap & eventData) {
  // Take the frame time step, which is stored as a float
  float timeStep = eventData["TimeStep"].GetFloat();
  // Move the camera, scale movement with time step
  MoveCamera(timeStep);
  outlineCameraNode_.position = cameraNode.position;
  outlineCameraNode_.rotation = cameraNode.rotation;
  
  if (outlineNode is null) {} else {
    outlineNode.Remove();
  }
  
  outlineNode = scene_.GetChild("Mushroom").Clone();
  StaticModel@ stModel = outlineNode.GetComponent("StaticModel");
  stModel.material = cache.GetResource("Material", "Materials/White.xml");
  outlineNode.parent = outlineScene_;
}

void HandlePostRenderUpdate(StringHash eventType, VariantMap & eventData) {
  // If draw debug mode is enabled, draw viewport debug geometry. Disable depth test so that we can see the effect of occlusion
  if (drawDebug) renderer.DrawDebugGeometry(false);
}

String patchInstructions = "";
[/code]

No console errors. I just modified some demo scripts and adapt your code.

Thanks again.

-------------------------

1vanK | 2017-01-02 01:07:08 UTC | #12

[quote="rasteron"]Btw, I tried converting this to Angelscript and it does not seem to have an effect. Let me know what I am missing here:

No console errors. I just modified some demo scripts and adapt your code.

Thanks again.[/quote]

I think you forgot to specify the folder with resources

[code]start "" Urho3DPlayer_d.exe Scripts/Outline.as -p "Data;CoreData;MyData" -w -x 800 -y 600
[/code]

It works.

Edit:
Also it implemented only OpengGL shader. May be your Player using DirectX?

-------------------------

codingmonkey | 2017-01-02 01:07:08 UTC | #13

[b]1vanK[/b], nice effect!)

I think for avoid this deformations on far distances need to turn-off blur. Create additional uniform for material maxBlurDistance and then compare distance between (in VS) vertex.pos and camPosVS if this distance > uniform value(maxBlurDistance) do not use bluring and if it less use blur.

also I think in some way it may rendered to internal RT (in RenderPath) and additional pass in material.

-------------------------

rasteron | 2017-01-02 01:07:08 UTC | #14

[quote="1vanK"]
I think you forgot to specify the folder with resources

[code]start "" Urho3DPlayer_d.exe Scripts/Outline.as -p "Data;CoreData;MyData" -w -x 800 -y 600
[/code]

It works.

Edit:
Also it implemented only OpengGL shader. May be your Player using DirectX?[/quote]

Yes, that's the problem. I'm now using OpenGL and copied all the files to their designated folders instead. I even tried with the same setup you got above.

-------------------------

1vanK | 2017-01-02 01:07:08 UTC | #15

Good settings:
[code]
void PS()
{
    vec3 rgb = texture2D(sDiffMap, vScreenPos).rgb;
    vec3 mask = texture2D(sNormalMap, vScreenPosInv).rgb;     

    vec4 blurredMask = GaussianBlur(3, vec2(0.3, 0.0), vec2(0.01, 0.01), 2.0, sNormalMap, vScreenPosInv);
    blurredMask = blurredMask + GaussianBlur(3, vec2(0.0, 0.2), vec2(0.01, 0.01), 2.0, sNormalMap, vScreenPosInv);
    blurredMask = blurredMask + GaussianBlur(3, vec2(0.3, 0.2), vec2(0.01, 0.01), 2.0, sNormalMap, vScreenPosInv);
    blurredMask = blurredMask + GaussianBlur(3, vec2(0.3, -0.2), vec2(0.01, 0.01), 2.0, sNormalMap, vScreenPosInv);
           
    if (mask.rgb == vec3(1.0, 1.0, 1.0))
        gl_FragColor = vec4(rgb, 1.0);
    else if (GetIntensity(blurredMask.rgb) > 0.0)
        gl_FragColor = vec4(0.0, 1.0, 0.0, 1.0);
    else
        gl_FragColor = vec4(rgb, 1.0);
}
[/code]

-------------------------

rasteron | 2017-01-02 01:07:08 UTC | #16

[quote="1vanK"]Good settings:
[code]
void PS()
{
    vec3 rgb = texture2D(sDiffMap, vScreenPos).rgb;
    vec3 mask = texture2D(sNormalMap, vScreenPosInv).rgb;     

    vec4 blurredMask = GaussianBlur(3, vec2(0.3, 0.0), vec2(0.01, 0.01), 2.0, sNormalMap, vScreenPosInv);
    blurredMask = blurredMask + GaussianBlur(3, vec2(0.0, 0.2), vec2(0.01, 0.01), 2.0, sNormalMap, vScreenPosInv);
    blurredMask = blurredMask + GaussianBlur(3, vec2(0.3, 0.2), vec2(0.01, 0.01), 2.0, sNormalMap, vScreenPosInv);
    blurredMask = blurredMask + GaussianBlur(3, vec2(0.3, -0.2), vec2(0.01, 0.01), 2.0, sNormalMap, vScreenPosInv);
           
    if (mask.rgb == vec3(1.0, 1.0, 1.0))
        gl_FragColor = vec4(rgb, 1.0);
    else if (GetIntensity(blurredMask.rgb) > 0.0)
        gl_FragColor = vec4(0.0, 1.0, 0.0, 1.0);
    else
        gl_FragColor = vec4(rgb, 1.0);
}
[/code][/quote]

Now that's perfect! :slight_smile: Though I'm still figuring out what is wrong with my angelscript version..

-------------------------

1vanK | 2017-01-02 01:07:08 UTC | #17

[quote="rasteron"]
Now that's perfect! :) Though I'm still figuring out what is wrong with my angelscript version..[/quote]

[drive.google.com/open?id=0B_XuF ... VZrUXV5Vk0](https://drive.google.com/open?id=0B_XuF2wRVpw4bERnSVZrUXV5Vk0)

-------------------------

rasteron | 2017-01-02 01:07:08 UTC | #18

[quote="1vanK"][quote="rasteron"]
Now that's perfect! :slight_smile: Though I'm still figuring out what is wrong with my angelscript version..[/quote]

[drive.google.com/open?id=0B_XuF ... VZrUXV5Vk0](https://drive.google.com/open?id=0B_XuF2wRVpw4bERnSVZrUXV5Vk0)[/quote]

Aha ok.. I double checked it with my player built and it looks like mine is outdated. Thanks for confirming this as well! :slight_smile:

-------------------------

tianlv777 | 2022-03-30 05:00:41 UTC | #19

![QQ图片20220330125711|690x310](upload://vykxoAFIJMK1J4NVuYXEXbJJqBW.jpeg)

-------------------------

tianlv777 | 2022-03-30 05:03:32 UTC | #20

![QQ图片20220330130129|690x493](upload://pdaCTlrUJ1QVXynID3sl1M8ukLV.jpeg)
Now I want to achieve this. What should I do?
I also want the front border of the box to be displayed, indicating that I have selected this character.

-------------------------

SirNate0 | 2022-03-30 15:54:06 UTC | #21

I think you'd need to either adjust your model to have holes at the edge of the box that would then be filled with the glow, or look at something like this.

https://discourse.urho3d.io/t/toon-and-line-shader/1517/3

-------------------------

