shifttab | 2022-10-09 12:17:04 UTC | #1

Hello, I'm trying to follow a shader tutorial and do it in urho. The shader is a simple water shader where I need to know the depth of the water relative to objects behind it.

![WaterDepth|690x363, 75%](upload://26mHuX9tLqfPJd8VTLUUCCipMTG.png)

*Scene Depth* node's description:
> Provides access to the current **Camera**'s depth buffer using input **UV**, which is expected to be normalized screen coordinates.
> 
> Eye - Depth converted to eye space units

So in urho, is this equivalent to viewport's depth buffer which is rendered to a texture?

*Screen Position* node:
> Provides access to the mesh vertex or fragment's **Screen Position**
> Raw - This mode does not divide **Screen Position** by the clip space position W component. This is useful for projection.

I don't know what to do for Screen Position.

-------------------------

1vanK | 2022-10-09 16:17:06 UTC | #2

<https://github.com/1vanK/Urho3DDeepWater>

-------------------------

