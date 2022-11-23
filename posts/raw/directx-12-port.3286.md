theak472009 | 2017-06-28 04:45:06 UTC | #1

I am working on a DX12 port for Urho3D and I dont get the use of void pointers everywhere in the graphics framework. What do you achieve from this? Why dont we just put the actual API data types instead of void pointers? Sure it will increase the number of ifdefines but at least the framework will be a lot more clear and will help to add new APIs easily.
For example: In DX12, we need to store the CPU handle of a SRV. Now to follow the framework style, I need to add another void pointer to the texture class and then go around casting it everywhere as a CPU handle in the DX12Texture class implementation.

Urho3D is a developer's engine. What's the point of hiding everything from the user? I am pretty sure anyone using Urho won't misuse the API.

Anyways, I dont care if we use annoying opaque types (void*) or nice API types, I will soon push the DX12 port to a repo :smile:

-------------------------

cadaver | 2017-06-27 08:09:02 UTC | #2

If I remember right, the primary concern was to keep API header pollution from everywhere where the rendering classes are being used. If you're writing to a single API, and that is not a concern for you, then I agree that just referring to the real classes is preferable.

-------------------------

Eugene | 2017-06-27 14:19:59 UTC | #3

No 3rd-party garbage in public headers IMO is better than internal developer's convenience.

But forward-declarations shall be fine too.

-------------------------

slapin | 2017-06-27 14:10:34 UTC | #4

I think internal headers should solve case of developer unhappiness while public headers could contain only forward declarations (and void pointers if forward declarations are too cumbersome).

-------------------------

theak472009 | 2017-06-28 04:43:49 UTC | #5

Now after getting used to this, its better but I still prefer the old Urho style where we just changed the include header depending on the API. Anyways, are there any features you guys are most interested to see in Urho DX12 port?

Here are some features I plan to add depending on spare time:
- Bindless textures
- Indirect draw
- Most of the implementation will be targeted towards AMD hardware so you might not see root descriptors
- Maybe multi-threaded command list generation (but for this, need to change the actual Renderer code, not sure)

-------------------------

boberfly | 2017-06-30 17:54:04 UTC | #6

Hey @theak472009

Any reason why you went DX12 over Vulkan? The mutli-thread command list I was thinking that a struct handle that gets passed as the first argument to things could work so that graphics commands aren't in global state (the other APIs would need this too like an emulation of command lists/buffers).

-------------------------

theak472009 | 2017-07-01 19:20:02 UTC | #7

Vulkan like OpenGL is a poor man's DirectX. Its already an extension hell. Vulkan's ExecuteIndirect is very basic and cant do anything fancy. The fancy extension is only available on NVIDIA cards which is not our primary focus. In addition, it still does not allow us to use the GDS which becomes kind of annoying when using append consume buffers.
Yeah the multi-threaded command buffer generation requires changes to app level code so I am not really sure about that one.

-------------------------

coldev | 2017-07-02 02:17:47 UTC | #8

Is possible Use to render layer how bgfx 
https://github.com/bkaradzic/bgfx

-------------------------

slapin | 2017-07-02 06:21:33 UTC | #9

AFAIK usually OpenGL vs DirectX discussions are initiated by people who either never seen directX or OpenGL or both.
So I see the side you're on. In general, both APIs provide the same function set and both have huge chunks of ugliness.

-------------------------

theak472009 | 2017-07-02 07:59:09 UTC | #10

I dont intend to do any DX vs Vulkan. But unfortunately, the truth is that Vulkan lacks some key features right now on AMD hardware. The biggest one is ExecuteIndirect. I don't think AMD has any plans to add the ExecuteIndirect extension.
In addition, currently using Vulkan is pointless because you can use DX12 on PC and XBOX, Metal for OSX, iOS and GNM for PS4. Only valid reason for using Vulkan is if you want a really high performant Android game.
So I think choosing DX12 over Vulkan is reasonable right now.

-------------------------

