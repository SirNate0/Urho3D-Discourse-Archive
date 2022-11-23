simonsch | 2018-03-12 11:28:54 UTC | #1

Hi community it is me again,

after setting up everything on android i am working on get some things done in urho3d.

Does anyone know how to use blendmode in urho3d or sdl? To better describe what i mean, i have a scene where a i render a cube, the background is black. I want that this black becomes transparent. In OpenGL i simply can work with some enable blending like

  > glEnable(GL_BLEND);
  glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

Would be grateful for any suggestions, how and where to enable this feature.

-------------------------

simonsch | 2018-03-12 15:15:17 UTC | #3

Okay little update, i realized that the Android SurfaceView is not able to blend with its background. So in my case i had 2 SurfaceViews in a stack and wanted to display the background of the one in the back.

Now i did managed to integrate both into one SurfaceView, which leads to new problems. I have 2 JNI interfaces the one for a framework, the second for urho3d both need to work independently. The first one provides a camera image which i want to render via Urho3d.

-------------------------

simonsch | 2018-03-13 08:13:58 UTC | #4

Okay another update my framework binds a opengl texture now so far so good, what i want now is to realize the visualization of this texture via a separate RenderPath. 
So i added a second viewport and used some quad shaders, so far so good. But now i don't know how to use the already bound glTexture2D in the urho3d shader or render path. Any suggestions are welcome.

-------------------------

simonsch | 2018-03-14 12:26:12 UTC | #5

Hey there! :) so another update. After managing successfully to create 2 RenderPaths i think i can now blend those 2 together. One is the default render path and the other only contains a texture.

My viewport order now is,
 0 -> Texture RenderPath
 1 -> Default RenderPath

Does anyone know, how i can enable alpha blending for the default one in xml? I think the default render path is Forward.xml

    <renderpath>
    <command type="clear" color="fog" depth="1.0" stencil="0" />
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" />
    <command type="forwardlights" pass="light" />
    <command type="scenepass" pass="postopaque" />
    <command type="scenepass" pass="refract">
        <texture unit="environment" name="viewport" />
    </command>
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
    <command type="scenepass" pass="postalpha" sort="backtofront" />
</renderpath>

Maybe it is possible to enable the alpha blending that way, that the background of the default render path is transparent instead black.

-------------------------

