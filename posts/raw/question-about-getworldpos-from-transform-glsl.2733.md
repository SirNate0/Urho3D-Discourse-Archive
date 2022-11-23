KonstantTom | 2019-05-23 13:20:00 UTC | #1

Hello, I need to calculate vertex position in world coordinates in my shader. For example, I want to flood fill all points, which X is greater than 10.0, with plain color .
My shader code:
```glsl
#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"

varying vec2 vScreenPos;
varying vec3 vWorldPos;

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos (modelMatrix);
    gl_Position = GetClipPos (worldPos);
    vScreenPos = GetScreenPosPreDiv (gl_Position);
    vWorldPos = worldPos + cCameraPos;
}

void PS()
{
    vec3 diffRGB = texture2D (sDiffMap, vScreenPos).rgb;
    if (vWorldPos.x > 10.0)
    {
        gl_FragColor = vec4 (0.023, 0.341, 0.756, 1.0);
    }
    else
    {
        gl_FragColor = vec4 (diffRGB.x, diffRGB.y, diffRGB.z, 1.0);
    }
}
```
But result don't match what I expected.
Camera Y is 100:
![Image1](upload://273mIlt9dVJ5gawuDNQ7tQ336Wf.png)
Camera Y is 200:
![Image2](upload://eH3LkcwI95kxlEcDBwX0WUXXfiA.png)
In first case it fills points which X is greater that 2, in second case -- greater than 4. And If I change camera Y, result changes too.
What is it? How I can get world coordinates of point/vertex?

P.S. Replacing `vWorldPos = worldPos + cCameraPos;` with `vWorldPos = worldPos;` doesn't changes anything. And sorry for bad quality of pictures.

-------------------------

Eugene | 2017-01-22 15:46:24 UTC | #2

What is your geometry? What camera do you have?

-------------------------

KonstantTom | 2017-01-22 16:43:00 UTC | #3

I have camera with standart configuration (same as camera on editor startup, camera position is (0.0f, 100.0f, 0.0f) ). I use Urho3D Editor for testing. In test scene there is only 1 geometry -- grid. But nothing changes if I add terrain or other models to scene.

-------------------------

Eugene | 2017-01-22 19:07:30 UTC | #4

If you have no geometry, I can't understand what do you render with your shader.

-------------------------

KonstantTom | 2017-01-22 19:53:00 UTC | #5

I use shader for postprocessing (see `GrayScale.glsl` and `Data/PostProcess/GreyScale.xml` for example). In my game I want to render fog of war using "quad" render step. For this purpose, I need position in world space to read information about this point from my fog of war mask. Did I choose wrong way for this task?

-------------------------

Eugene | 2017-01-22 20:16:11 UTC | #6

You have to compute world position on your own because `worldPos` contain something absolutely unrelated to your scene.

-------------------------

1vanK | 2017-01-23 13:41:37 UTC | #7

You need render scene depth to texture. For it use renderpathes with "depth" suffix. Thus you can get a world coordinate post-processing step. For example see:

https://github.com/1vanK/Urho3DMotionBlur/blob/master/Final/RenderPaths/MyForwardHWDepth.xml
https://github.com/1vanK/Urho3DMotionBlur/blob/master/Final/Shaders/GLSL/MotionBlur.glsl

-------------------------

KonstantTom | 2017-01-23 13:42:38 UTC | #8

Thank you very much! All works now! :)

-------------------------

