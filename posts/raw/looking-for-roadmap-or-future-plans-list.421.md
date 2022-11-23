JeriX | 2017-01-02 01:00:17 UTC | #1

Is there any document describing plans of official development?
Or maybe list of contributor's intentions to add something?
I didn't find anything on forums or github...

-------------------------

cadaver | 2017-01-02 01:00:17 UTC | #2

There isn't one, really. The best to do is to follow discussion here, as well as the github issues and github feature branches.

-------------------------

JeriX | 2017-01-02 01:00:17 UTC | #3

I see...
So, is there anybody right now who trying to rethink urho ui?
I started to think about how implement fully adaptive ui style/layouts. But the simplest idea I can implement was just some wrapper about current Urho3D::UIElement. Still with own xml scheme...
Any thoughts or suggestions?
Or maybe precautions?

-------------------------

cadaver | 2017-01-02 01:00:17 UTC | #4

There is currently an issue open on the subject of percentage-based UI element positioning / sizing. [github.com/urho3d/Urho3D/issues/443](https://github.com/urho3d/Urho3D/issues/443)

I believe at some point it is inevitable that the UI must be revamped. Perhaps sort of a "NewUI" written alongside the old to preserve compatibility for a transition period. Contributions to this direction are very welcome!

IMO the UI should be components in scene nodes to allow full mixing with other scene content. You'd likely have another scene for the UI so that it doesn't disturb the game scene. Other use cases to consider are interactive "screen displays" like in Doom 3. There shouldn't be a "singleton" -like one UI hierarchy like there is now. Also, the skinnability / UI style mechanism is flaky, as there is mixing between the UI element's "content" attributes and skin/style attributes, meaning that applying a style to UI elements can be destructive or irreversible, as it possibly overwrites some of the UI element's content attributes.

Btw. there has been suggestions of integrating 3rd party UI libraries in the past, I personally don't believe in that, not for the reason that Urho should implement everything itself (it shouldn't, where it makes sense to use 3rd party solutions) but because it's doubtful that a 3rd party solution can achieve as seamless and usable integration into the rest of the system as an "in-house" solution, also considering the needs of eg. scripting.

-------------------------

friesencr | 2017-01-02 01:00:18 UTC | #5

I haven?t done a lot with ui stuff since the topic came up last but here are some of my thoughts.

You can't really beat urho3d ui in terms of speed.  The way the ui batches images and draws is fast.  If you are close to shipping a game and want a millisecond back a bulky ui will make you sadface.  Generally games don't require full blown uis.  Most games uis are mostly sprites.  Having full scene integration and a bulkier api is ok because it needs to be perfect.

However the tooling for making games often requires more advanced uis.  More robust components are required.  However I and probably most devs would rather spoon our own eyeballs then write tons of ui code.  I mostly write uis for a living as a web programmer so my wife had me install spoon guards.  IMGui style the best choice for tooling as it is a very concise api.

It's possible that having two ui systems would be a better solution.

-------------------------

JeriX | 2017-01-02 01:00:18 UTC | #6

[quote="cadaver"]it's doubtful that a 3rd party solution can achieve as seamless and usable integration into the rest of the system as an "in-house" solution, also considering the needs of eg. scripting.[/quote]
I will definitely agree with that!

[quote="cadaver"]IMO the UI should be components in scene nodes to allow full mixing with other scene content. You'd likely have another scene for the UI so that it doesn't disturb the game scene. Other use cases to consider are interactive "screen displays" like in Doom 3. There shouldn't be a "singleton" -like one UI hierarchy like there is now.[/quote]
For now I'm not so familiar with Urho, but I want to be :slight_smile: 

My intention was to fix this:
[quote="cadaver"]Also, the skinnability / UI style mechanism is flaky, as there is mixing between the UI element's "content" attributes and skin/style attributes, meaning that applying a style to UI elements can be destructive or irreversible, as it possibly overwrites some of the UI element's content attributes.[/quote]

I was thinking about wrapping existent UI classes like UIElement and BorderImage to separate layout from style by providing new Serializables...
I like the way urho uses Serialazable with attributes. It's seems simple when engine uses this mechanism, but when I go deeply it's very frustrating :confused:


// and I think we should create new thread about ui :wink:

-------------------------

weitjong | 2017-01-02 01:00:18 UTC | #7

[quote="cadaver"]IMO the UI should be components in scene nodes to allow full mixing with other scene content. You'd likely have another scene for the UI so that it doesn't disturb the game scene. Other use cases to consider are interactive "screen displays" like in Doom 3. There shouldn't be a "singleton" -like one UI hierarchy like there is now. Also, the skinnability / UI style mechanism is flaky, as there is mixing between the UI element's "content" attributes and skin/style attributes, meaning that applying a style to UI elements can be destructive or irreversible, as it possibly overwrites some of the UI element's content attributes.[/quote]

Totally agree with the last statement. Currently a significant part of the UI-layout serialization logic is there just to filter out those UI styling attributes from being "saved" again in the layout file. It was one of the challenge I faced then when I tried to enhance the existing Editor to support UI-layout editing. Those XPath filtering logic could be thrown out when the proposed UI skin/style and content separation is being implemented.

I also agree with removing the 'singleton'-ness of the UI root hierarchy. It should again make implementation of UI editor simpler than currently. Currently it is kind of a hack to make the new UI layout being edited and modified  in the editor view does not actually mess up with the Editor's own UI and vice versa, as if there were more than one UI root while in fact there is actually only one.

Additionally I want to add one more point. It has been awhile since I last look deeper into UI subsystem so correct me if I am wrong. Currently the UI subsystem only renders at the very last and it is outside of the Renderer subsystem. In other words, it is kind of "fixed" in the pipeline. IMHO, the UI rendering could be treated as one of the available post-processing step in a normal render path pipeline. By default it should still be the last command in the pipeline. But now, since it is not "fixed" anymore, one could change the render path commands to achieve other effects *after* the UI has been rendered, such as lens distortion correction post-processing for Oculus Rift or Google Cardboard. I think it should also make the rendering UI in a rendertarget possible.

-------------------------

friesencr | 2017-01-02 01:00:18 UTC | #8

Another problem we will have with the ui is when 4k displays come out they will not scale well or look good.  I have wondered if using a vector based ui to author the ui parts and then use rtt to save images for runtime speed.

-------------------------

cadaver | 2017-01-02 01:00:18 UTC | #9

[quote="weitjong"]
Additionally I want to add one more point. It has been awhile since I last look deeper into UI subsystem so correct me if I am wrong. Currently the UI subsystem only renders at the very last and it is outside of the Renderer subsystem. In other words, it is kind of "fixed" in the pipeline. IMHO, the UI rendering could be treated as one of the available post-processing step in a normal render path pipeline. By default it should still be the last command in the pipeline. But now, since it is not "fixed" anymore, one could change the render path commands to achieve other effects *after* the UI has been rendered, such as lens distortion correction post-processing for Oculus Rift or Google Cardboard. I think it should also make the rendering UI in a rendertarget possible.[/quote]
This is true. Having the UI render as a renderpath command would quite easy and straightforward, however it could not be fully described with renderpath xml data, as it would need to refer to a live root UI element. So you'd need to setup the UI render command programmatically, which is not a big problem of course.

For a complete change of how the UI rendering works, and which would allow full mixing with eg. 3D models, there could be a root component like UIPanel which would be a Drawable. It would collect the vertex data from all underlying UI elements (in child nodes) and render normally through a Camera. (*) You would just render the UI on top of the scene content using another camera and viewport that doesn't clear the depth & color buffers, then finally apply any distortion post-processes. Of course if you wanted, you could even have UIPanel's as a part of your main scene, for example some holographic display. Done this way, you could also transform the UI elements in 3D space as you wanted, for example look at them at an angle.

(*) There are some concepts in UI rendering which are alien to normal scene rendering, such as scissor clipping. But this could be emulated by rather clipping the actual vertices.

Injecting input to the UI would be another matter. There could be manual and automatic injection, in automatic mode (normal) the UI would keep track of to what screen coordinates it has been rendered last, and scale eg. mouse input accordingly. The simplest case is when the UI just fills the whole screen.

-------------------------

thebluefish | 2017-01-02 01:00:19 UTC | #10

[quote="cadaver"]I believe at some point it is inevitable that the UI must be revamped. Perhaps sort of a "NewUI" written alongside the old to preserve compatibility for a transition period. Contributions to this direction are very welcome!

IMO the UI should be components in scene nodes to allow full mixing with other scene content. You'd likely have another scene for the UI so that it doesn't disturb the game scene. Other use cases to consider are interactive "screen displays" like in Doom 3. There shouldn't be a "singleton" -like one UI hierarchy like there is now. Also, the skinnability / UI style mechanism is flaky, as there is mixing between the UI element's "content" attributes and skin/style attributes, meaning that applying a style to UI elements can be destructive or irreversible, as it possibly overwrites some of the UI element's content attributes.
[/quote]

Interesting. I have actually been working on a UI replacement for my game, as I needed a bit more flexibility with rendering text within the game work. So far I have a rough working of a system that's based off Components, so that UI elements can be attached to nodes. Consequently I removed the whole UI subsystem and instead it's all handled by the UI components and an additional RenderPath. I haven't had much time to work on it lately as I recently transitioned jobs, but I have a bit done already. I may look to uploading it separately so that I can get additional help on it what I already have.

-------------------------

boberfly | 2017-01-02 01:00:20 UTC | #11

May I suggest:
[github.com/memononen/nanovg](https://github.com/memononen/nanovg)

For vector drawing.

There's quite a thin GUI abstraction to this that uses blender widgets as well, I stumbled on this when looking at bgfx.
[bitbucket.org/duangle/blendish/src](https://bitbucket.org/duangle/blendish/src)

There could be some nice references for the next-gen UI in there. The thin UI 'oui.h' currently doesn't scale based on DPI but nanovg is vector-based so it shouldn't be too hard to extend I'd imagine.

-------------------------

friesencr | 2017-01-02 01:00:20 UTC | #12

I looked into nanovg as well.  It doesn't have a dx9 renderer.  The nanovg bgfx port does support dx9 rendering through bgfx.  I was thinking about writing a desiner that used bgfx and nanovg to dump bitmaps.  Our font sdf trick could also apply to ui bitmaps making them scalable and super sharp.  There are performance issues with nanovg too.  The IMgui api that oui uses is attractive too.

-------------------------

