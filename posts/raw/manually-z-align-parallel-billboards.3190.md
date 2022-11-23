Pencheff | 2017-06-02 09:35:55 UTC | #1

I have couple of billboard sets that lay on the same plane, say their nodes all have Z = 0 and are parallel.
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/34d8f36607700192a0013bef068d9eeed1cce086.png" width="690" height="403">
I need the green plane on top right to be rendered over the white plane. One way is to change the green plane's Z axis closer to the camera with very small value, but I don't like the results (I really need them to be parallel). The other way I can think of is to use materials with different z-bias, I used that with Ogre3D, but the problem is I need to use different materials for every plane. 
Any other ways I can do this ?

-------------------------

Modanung | 2017-06-02 11:31:25 UTC | #2

Maybe you could couple the z-bias to the vertex colours using a custom shader? Or can it only be set per material?

-------------------------

Pencheff | 2017-06-02 15:28:46 UTC | #3

Hmm yes that sounds logical. Thanks, I'll try that.

-------------------------

sabotage3d | 2017-06-02 15:38:29 UTC | #4

This looks really similar to my problem here: https://discourse.urho3d.io/t/alpha-sorting-issue/3172/11.
It works if there is no transparency if there is between two batches one is opaque not sure why.

-------------------------

Modanung | 2017-06-02 15:39:21 UTC | #5

If you use the vertex alpha channel you can still _colour_ the vertices as you like.

-------------------------

Pencheff | 2017-06-02 17:02:26 UTC | #6

I could but I will lose alpha, I still need to control every quad's transparency.
In Ogre3D I had an option to control the rendering order of every entity by using setRenderQueueGroupAndPriority(), which solved most of the problems when having transparency.

What I'm trying to achieve is 2D functionality inside 3D, by having a "screen" component as master and "media" component as child nodes, then those get placed on a plane with common Z, camera moved back and adjusted so it captures the whole "screen" plane. Every child plane must have color/transparency and Z order.

-------------------------

Modanung | 2017-06-02 17:04:00 UTC | #7

Could you add an extra channel?

-------------------------

Pencheff | 2017-06-02 17:24:32 UTC | #8

Sorry I edited my post after your response.

I can add an extra channel to pass z-order, I'm still not sure how to control which item renders over another with vertex shader, unless I touch the vertexes to get closer to the camera and that breaks things. I'm not a shader expert, maybe there's a legit way of doing it.

-------------------------

Modanung | 2017-06-02 17:34:33 UTC | #9

[quote="Pencheff, post:8, topic:3190"]
I'm not a shader expert
[/quote]
Neither am I. I couldn't tell you the exact implemention as of now. Just connecting blurs here. ;)

-------------------------

sabotage3d | 2017-06-09 13:01:52 UTC | #10

This is what worked for me in the same batch. For example in the Unlit shader you can add:

    int index = int(iObjectIndex);
    gl_Position.z = -index * 0.001;

Where `ObjectIndex` is an attribute per billboard or you can add shader override in two different materials to override the `gl_Position.z`. The advantage over modifying the position is won't get closer to the camera.

-------------------------

Pencheff | 2017-06-02 18:27:20 UTC | #11

Isn't gl_Position modifying the vertex position ? What happens if you choose a bigger multiplier than 0.001, doesn't this move the vertex closer ?
There's a Drawable::sortValue_ and accessor methods, but it only seems to be used for input raycasting, if only it was used for sorting rendering order ...

-------------------------

sabotage3d | 2017-06-02 20:03:42 UTC | #12

I don't think it modifies the vertex position. It is used in the depth directly:
`vWorldPos = vec4(worldPos, GetDepth(gl_Position));`
Where `worldPos` is the actual vertex position.

-------------------------

Pencheff | 2017-06-02 20:15:06 UTC | #13

OK then, that sounds like a solution, it still limits me to use special material (with that shader), but it's something.

-------------------------

Pencheff | 2017-06-04 10:12:38 UTC | #14

Either I'm doing something wrong, or gl_Position doesn't do what I desire. Here's my VS, copied from Unlit:

[code]
#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"
#include "Fog.glsl"

varying vec2 vTexCoord;
varying vec4 vWorldPos;
#ifdef VERTEXCOLOR
    varying vec4 vColor;
#endif
uniform float cZorder;

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    gl_Position.z = -cZorder;
    vTexCoord = GetTexCoord(iTexCoord);
    vWorldPos = vec4(worldPos, GetDepth(gl_Position));

    #ifdef VERTEXCOLOR
        vColor = iColor;
    #endif
}
[/code]

When I change the cZorder, the billboard only flickers, no matter the values.

-------------------------

Pencheff | 2017-06-04 10:18:06 UTC | #15

Oh, my bad, my material is same for both planes I'm testing this on, I need to clone materials so every component gets its own cloned instance.

-------------------------

Pencheff | 2017-06-04 11:38:13 UTC | #16

@sabotage3d, it works fine thanks. Any other ideas how to do this without having to use special material for the purpose ?

-------------------------

sabotage3d | 2017-06-09 13:01:52 UTC | #17

You can try `Material::SetRenderOrder` it might work in your case.

-------------------------

Pencheff | 2017-06-04 12:38:36 UTC | #18

That is exactly what would I was looking for. Now the element on top still bugs like in the screenshot, but if I set an appropriate BiasParameters that should do the trick.

-------------------------

Pencheff | 2017-06-09 13:01:40 UTC | #19

I can't seem to find a way to do this with BiasParameters, so the best technique so far is the one with gl_Position.z adjustment.

-------------------------

