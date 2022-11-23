shifttab | 2022-08-17 01:44:54 UTC | #1

I'm trying to show the depth. Am I doing this correctly?
```
SharedPtr<Viewport> viewport(new Viewport(context_, m_scene, camera));
viewport->SetRenderPath(cache->GetResource<XMLFile>("RenderPaths/DeferredHWDepth.xml"));
viewport->GetRenderPath()->Append(cache->GetResource<XMLFile>("Post/ShowDepth.xml"));

auto renderer = context_->GetSubsystem<Renderer>();
renderer->SetViewport(0, viewport);
```

ShowDepth.xml

```
<renderpath>
    <command type="quad" vs="MyDepthTexture" ps="MyDepthTexture" output="viewport">
        <texture unit="depth" name="depth" />
    </command>
</renderpath>
```

```
// MyDepthTexture.glsl
void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vScreenPos = GetScreenPosPreDiv(gl_Position);
}

void PS()
{
    float depth = ReconstructDepth(texture2D(sDepthBuffer, vScreenPos).r);
    vec3 color = vec3(depth, depth, depth);
    gl_FragColor = vec4(color, 1.0);
}
```
Result:
![urho|690x408, 50%](upload://9hKtk5lWXYsWaNM3Q7kjd4z1yTH.png)

-------------------------

1vanK | 2022-08-19 10:53:19 UTC | #2

This is correct depth texture with different depth values

![4115352ee634066092d24dcacacc24d2ec90206d|690x414](upload://eI0Gv9X3wSij0b067evESbrT4Z.png)

-------------------------

Eugene | 2022-08-19 11:07:07 UTC | #3

Yep, looks like depth after some curve tweaking
![image|690x271](upload://yLJ0hoZ5MU2j5lMSEfFQalpultH.png)

-------------------------

shifttab | 2022-08-19 11:32:37 UTC | #4

I just solved this a while ago. It was because the default camera far clip, at least in the editor where I created the scene, was 1000. It was too high for the different values to be visible.

I cant believe it took me days :angry:

-------------------------

