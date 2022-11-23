extobias | 2019-05-26 06:47:00 UTC | #1

Hi there, 
I'm trying to visualize the depth buffer
in a texture created in a example application
and writing it through a quad command in the renderpath.

// texture creation
[code]
SharedPtr<Texture2D> renderTexture(new Texture2D(context_));
float div = 2.0f;
renderTexture->SetSize(graphics->GetWidth() / div, graphics->GetHeight() / div, Graphics::GetRGBFormat(), TEXTURE_RENDERTARGET);
renderTexture->SetName("DepthBuffer");
[/code]

// command added to the renderpath Deferred.xml
[code]
<command type="quad" vs="CopyFramebufferDepth" ps="CopyFramebufferDepth" blend="replace" output="DepthBuffer">
    <texture unit="depth" name="depth" />
</command>
[/code]

// PS  CopyFramebufferDepth.glsl
[code]
float x = vScreenPos.x;
float y = 1.0f - vScreenPos.y;
float depth = DecodeDepth(texture2D(sDepthBuffer, vec2(x, y)).rgb);
vec3 color = vec3(depth, depth, depth);
gl_FragColor = vec4(color, 1.0);
[/code]

What I get is the following. the depths should not be on a grayscale?
should I define a readable depth texture, like docs says?

![depth|690x316,75%](upload://vIcDaXTBsWZ58JNzDYozqk88LsY.jpeg)

-------------------------

Leith | 2019-05-26 07:12:31 UTC | #2

the depth buffer is a grey scale texture, so your visualization is horribly wrong

-------------------------

UNDEFINED-BEHAVIOR | 2019-05-26 11:09:02 UTC | #3

Have you tried this? https://renderdoc.org/ maybe it works with urho.

-------------------------

extobias | 2019-05-26 15:08:24 UTC | #4

Apparently the depth buffer was read correctly
for what you see in the texture is the content of sDepthBuffer.
Use the Deferred.xml renderpath and add the command at the end, could it affect something?

![renderdoc-capture|690x351](upload://3Lujzgyv0sFTNWzsNyUcIZxuEUB.png)

-------------------------

extobias | 2019-05-27 03:29:22 UTC | #5

I thought that the rt depth was a direct reference to the opengl depth buffer. but as the documentation says "define a readable hardware depth texture, and instruct the render path to use it instead" was the solution.
@UNDEFINED-BEHAVIOR thanks, renderdoc really helped me.  

![renderdoc-capture2|690x314,75%](upload://q2u9YKHyL0ZeaRl5NBORRldKf7w.jpeg)

-------------------------

guk_alex | 2019-05-27 08:48:41 UTC | #6

Btw, if you want to visualise it right you might know that depth buffer contains non-linear values, and if you render the raw values then you won't be able to distinguish depth of the far objects, only the ones that are close to the camera.
You can convert it to linear values like that (with 'near' and 'far' being your clip values) :
    
    float LinearizeDepth(float depth) 
    {
        float z = depth * 2.0 - 1.0; // back to NDC 
        return (2.0 * near * far) / (far + near - z * (far - near));	
    }

-------------------------

Leith | 2019-05-27 08:57:25 UTC | #7

Multiply by W :) This is not well covered in most literature, most people do not understand homogenous vec4

-------------------------

jmiller | 2019-05-27 16:55:22 UTC | #8

Considering the docs section on reading scene depth..
  https://urho3d.github.io/documentation/HEAD/_render_paths.html#RenderPaths_Depth

`ReconstructDepth()`, defined in our `Samplers.glsl` shader functions include, is to reconstruct linear 0-1 depth from hardware. Also there is `DecodeDepth()`..

These are used in e.g. DeferredLight.glsl, and I find some posts in the forum and insights by @cadaver   https://discourse.urho3d.io/t/way-to-getting-depth-texture-in-forward-render-path/1459

-------------------------

