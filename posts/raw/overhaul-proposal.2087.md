dragonCASTjosh | 2017-01-02 01:12:55 UTC | #1

Due to the a talk on the issue tracker ([url]https://github.com/urho3d/Urho3D/issues/1397[/url]) i decided to write a small proposal on a Overhaul of Urho3D. All the concepts suggeted within the proposal are open to debate and changes, i am also open to adding new changes suggested by the community. I will also keep a close eye on the suggestions thread for any new addition.

You can find the proposal at the following link:
[url]https://drive.google.com/open?id=0B7EwsKWU8ATkVmhEbkh1ejB1aDA[/url]

-------------------------

Enhex | 2017-01-02 01:12:55 UTC | #2

First of all I'd like to criticize the motivation.
Overhauling the whole engine is a bad idea. It would take a lot of time and effort, and there won't be any benefit in doing so.
It would only benefit projects that have the highest possible demands for performance, mostly graphics, and only projects with a budget of at least ~$10,000,000 would have the kind of assets and demands that would benefit from it, and I don't think Urho users have such projects thus there's no value in doing so.
I'd argue that work spent on adding new features to expand the possibility space of what can be made with Urho has much more value than overhauling the engine for what would be to virtually all Urho projects a premature optimization.


Rendering

? Unified shader language
- I'm for it, it would reduce work and maintainence.


? Modern Rendering pipeline targeted at a DirectX11 and DirectX12 work flow
without removing DirectX9 support for older systems.
- Against, a lot of work and users won't benefit from it.

? Geometry shaders for tessellation
- Not sure what you mean

? Pre-Filtered PBR (filtered within the engine)
- For it.

? Swappable render paths at either runtime or though a method at compile time
- Already possible to set render path at runtime, tho not sure if only before engine initialization. Even if it's only before, having some sort of graphic settings menu and changing the render path would only require a game restart, which isn't a big deal.

? Support for modern render API such as Vulkan and DirectX12
- Against. I heard they're barebone and require a lot of work, and no Urho user won't benefit from it. Even if it isn't barebone it still isn't beneficial.

? A low end and high end render path to enable maximum quality without losing
compatibility
- You can already have several paths, don't know what compitability would be lost.

? Multi-threaded rendering
- Isn't it the same as Vulkan/DX12?

? Material Prototypes
- Don't know what that means.


Core

? Support for Code Plug-ins
- Not sure what you mean by plug-ins, but you can already use Urho as a C++ library and add whatever you want. And there's scripting.

? Multi-threading using fibbers
- If it would offer sagnificant improvement, for.

? Hand written documentation on the engine
- Already exists, unless you mean documenting implementation details for engine developers and if so, for.

? A data driven engine design
- You already have event system, and node-component system.


Scripting

? Hand written documentation
- Already exists

? Auto generated script bindings
- Not sure if it's worth it. Valve had a paper about how they made a very complicated special tool that can generate bindings (doesn't work for all cases) and they spent a year making it instead of few days doing the bindings, and now you need specialized programmers to be able to even maintain it.
So you got partial solution that you'll have very hard time to be able to find replacement developers for and spent orders of magnitude more time making than just writing the bindings.
In general against, unless it can be kept almost as simple is writing the bindings.

? Syntax Highlighting for major IDE
- For Lua you won't have problems finding syntax highlighting for text editors.
For AS there are some efforts by community members, like [atom.io/packages/language-angelscript](https://atom.io/packages/language-angelscript).
There was also IDE stuff [post12251.html](http://discourse.urho3d.io/t/angelscript-editor-with-autocompletion/1956/8)
In general I wouldn't consider it in the scope of Urho.

? Support for users to add there own languages with minimal effort
- Already exists, use Urho as a C++ library and use whatever you want.


Urho2D

? 2D Lighting
? 2D Shadows
? Normal mapped 2D sprites
- Technically you can have those with regualr 3D rendering, not sure if they can be used with Urho2D, never looked into it.
Performance shouldn't be a problem if it's a 2D game.
If it isn't possible, then for.

? Spline based level creation
- Specialized content creation tool, not part of the engine level.

? Standard 2D movement in the editor with 2D mode enabled
- Never used Urho2D, don't know if the urho editor supports it.

? Layers for producing parallax or other layer based effects
- For, increases possibility space. Is it really not possible already?


UI

? Easy to change editor themes
- You can already have default style file (usually XML). The only thing I can think of which will make it easier is a visual style editor, which I'm for.

? Sliders
- already exist (tho I'd like to have an option for fixed size bar)

? Animated widgets
- Use attribute animation


Editor

? Changeable color themes
- Same as my visual style editor suggestion

? Updated UI textures
- What updating means? Better default ones?

? Integrated terrain editor
- Againt, specialized content creation tool, outside of engine scope. Urho just uses a heightmap image, and you can make the hieghtmaps with external tools.
Urho also has hot resource reloading, so it should be possible for the terrain to update as the image updates.

? Integrated IDE for AS and LUA
- Against, there are plenty of good editors out there, this would be a waste of time.




Also note that when I'm saying I'm against I don't mean they should never be done, I mean they have very little value and thus should have very little priority.

-------------------------

yushli | 2017-01-02 01:12:56 UTC | #3

I don't think overhauling Urho3D 3D part is a good idea. Don't fix what isn't broken at the first place. Urho3D 3D part is actually the most valuable part of this project. I don't believe anyone except the original authors can make big changes to the underlying architecture. 
If you really want to make big changes, please consider taking Urho3D 2D part to the next level first. Urho3D 2D part has a lot of places that can be improved. You can exam the design and architecture, improve the performance, add missing features, support new functions etc. That part would be easier to get integrated into main branch, and can benefit other users immediately.

-------------------------

franck22000 | 2017-01-02 01:12:56 UTC | #4

I tend to be agree, i am more for improving the existing engine architecture with new features (missing DX11 features for examples like geometry shaders, compute shaders...) and localized improvements / optimizations with github pull requests. I think that a lot of users (including me) have began to do some serious projects with this engine and such a big overhaul would add a lot of work for us to maintain our projects. However some ideas exposed here would be nice to have of course.

-------------------------

cadaver | 2017-01-02 01:12:56 UTC | #5

I believe this is not at sufficient detail level to inspire confidence. It's easy to write "data driven engine design" but harder to elaborate what that actually means in practice. However, like I said in the issue tracker, you can let the code speak for itself instead :slight_smile:

Aiming for a modern rendering architecture while keeping D3D9 level compatibility sounds contradictory, or at least something that would increase the difficulty. However I'd agree that given current compatibility and platforms that Urho can run on this is necessary (not D3D9 in itself, but mobile GLES2.0), because otherwise too much currently working platforms would be ruled out.

Vulkan and D3D12 are not at all certain to bring performance improvement. Instead you have to do low-level management of resources that the driver used to do for you, and it'd be rather easy to shoot yourself in the foot, on multiple levels from outright crashes to just inefficiency.

Having one shader language only is a well-defined goal and would benefit all use cases of Urho. Though one would still need to be careful of the implementation. For example, if this was done by runtime-translating HLSL into GLSL, then mobiles could suffer in longer startup time. An offline process would be a better approach, but remember that Urho does not have a "project asset build/preparation step" at least at the moment, but just expects to load ready-to-go resources (like models, dds textures and API's native shader code). For practical purposes I'd personally be fine with a manual approach like "when you have changed shaders, run this tool or batch file to translate into API-native shaders"

-------------------------

hdunderscore | 2017-01-02 01:12:56 UTC | #6

Whether or not it's a good idea is one thing, but the real challenge is in making any of the feature requests a reality (although as mentioned some of the features already exist or are already being worked on). I think many Urho users have shared interests in seeing some parts of the engine move forward, eg improved editor, improved UI, improved shaders and lighting. Due to limited time and lack of motivation, even though large progress might be made individually there have probably been a lot of features that have been left incomplete, never to see the light of a pull request.

The first questions should be: Who is willing to work on what? 

There are many talented and enthusiastic contributors to the Urho project, I think it might be possible to gather a small group (2 or 3 people) to at least attempt one feature request together.

It's easy to underestimate the effort or skill needed to knock out some of these features, so aiming for something at your own level is best. For someone with as much experience and enthusiasm in graphics programming and intimacy with the Urho source as cadaver, a graphics overhaul might be achievable but for 2 or 3 people without that same experience, it could be an unrealistic goal.

-------------------------

cadaver | 2017-01-02 01:12:56 UTC | #7

I would like to think that for someone who is knowledgeable of graphics APIs and how rendering engines work, Urho's codebase would be comparably easy to get into, even if you're not the original author :slight_smile: However if you change something fundamentally in the low-level rendering core, you could end up with a large amount of broken functionality (considering all the Drawable subclasses) which will take a lot of effort to fix.

Slightly more pessimistically, persons at the sufficient proficiency level are likely to be working on their own engines instead, so it's unlikely that someone appears out of the blue. From the issue tracker talk I understood that dragonCASTJosh would be offering to be the driving force or major implementor for the changes he has proposed.

For estimating what actually happens and how much functionality may break when you decide to overhaul an engine Ogre 2.x is a nice example. However they had a real pressing need for the overhaul (the engine was practically unusably slow for any larger real-world projects) while Urho has less so.

-------------------------

dragonCASTjosh | 2017-01-02 01:12:57 UTC | #8

I think allot of the feedback here is good and there seams to be some conflict on view and direction. but overall i see there is a want for some advancements on the Urho side that are larger then the standard PR. I will defensively begin work on some of the features that people are agreeing on. 

[quote="hd_"]The first questions should be: Who is willing to work on what? 

There are many talented and enthusiastic contributors to the Urho project, I think it might be possible to gather a small group (2 or 3 people) to at least attempt one feature request together.[/quote]
Im willing to work on anything but anything outside of graphics may take a little learning on my part. A small team of people who are willing to work on at least some of these features as part of a group would be awesome.

[quote="cadaver"]Aiming for a modern rendering architecture while keeping D3D9 level compatibility sounds contradictory, or at least something that would increase the difficulty. However I'd agree that given current compatibility and platforms that Urho can run on this is necessary (not D3D9 in itself, but mobile GLES2.0), because otherwise too much currently working platforms would be ruled out.[/quote]
I was thinking having a mobile and desktop pipeline, this possibly be done through the render paths by listing the passes you wish to perform, for example run something like tessellation on desktop but not mobile. D3D9 would run the mobile feature set as its main reason for being would be legacy support.

[quote="cadaver"]
Vulkan and D3D12 are not at all certain to bring performance improvement. Instead you have to do low-level management of resources that the driver used to do for you, and it'd be rather easy to shoot yourself in the foot, on multiple levels from outright crashes to just inefficiency.[/quote]
I think they will bring benefits but not in the short term. Like with the D3D11 release it  will take time before developers become comfortable with it and learn its new features, once developers get to this level then the overall performance on these API will be allot better. Because of that i felt it would be better to implement it toward the end of the Overhaul rather then doing it at a later date.

[quote="cadaver"]
Having one shader language only is a well-defined goal and would benefit all use cases of Urho. Though one would still need to be careful of the implementation. For example, if this was done by runtime-translating HLSL into GLSL, then mobiles could suffer in longer startup time. An offline process would be a better approach, but remember that Urho does not have a "project asset build/preparation step" at least at the moment, but just expects to load ready-to-go resources (like models, dds textures and API's native shader code). For practical purposes I'd personally be fine with a manual approach like "when you have changed shaders, run this tool or batch file to translate into API-native shaders"[/quote]
My plan for this was to compile the shader to its target format upon saving the shader file.

[quote="franck22000"]DX11 features for examples like geometry shaders, compute shaders[/quote]
That is the reason i was looking to separate D3D9 into a mobile render pipeline, that way we would be able to use DX11 features without worrying about legacy support because mobile handles that.

[quote="yushli"]I don't think overhauling Urho3D 3D part is a good idea. Don't fix what isn't broken at the first place.[/quote]
The problem i see is not that it is broken but more that the engine is aging, and starting to fall behind.

[quote="Enhex"]? Multi-threaded rendering
- Isn't it the same as Vulkan/DX12?[/quote]
No on D3D11 you can allow the renderer to run on multiple threads, D3D12 and Vulkan handle this automatically but older API's like GL3 and D3D11 do support the feature, its one of the reason that current performance results are only a 10 frame benefit to D3D12

[quote="Enhex"]? Auto generated script bindings
- Not sure if it's worth it. Valve had a paper about how they made a very complicated special tool that can generate bindings (doesn't work for all cases) and they spent a year making it instead of few days doing the bindings, and now you need specialized programmers to be able to even maintain it.
So you got partial solution that you'll have very hard time to be able to find replacement developers for and spent orders of magnitude more time making than just writing the bindings.
In general against, unless it can be kept almost as simple is writing the bindings.[/quote]
Once the system is done it wouldnt require much to maintain, the idea is that the community wouldn't need worry about manually writing script binding witch is more often then not forgotten on the initial PR

[quote="Enhex"]? Material Prototypes
- Don't know what that means.[/quote]
it is essentially inheritance for materials, for example a child material that just changes the diffuse color 

[quote="Enhex"]? Support for Code Plug-ins
- Not sure what you mean by plug-ins, but you can already use Urho as a C++ library and add whatever you want. And there's scripting.[/quote]
I way for the community to write features that are not suitable for the main repo, yes you can make your own fork but that often means that the branch if behind. With plugins features like a new scripting language or new editor features could just be a small download the you can load into the engine or editor to get that feature.

[quote="Enhex"]? Hand written documentation
- Already exists[/quote]
Most of the current documentation is generated from comments in the source, my idea was to go through and create documentation for everything by hand including code examples (look at unity and unreal for reference). i know this would take allot of time and would be an ongoing project but it feel it would be beneficial

[quote="Enhex"]? Updated UI textures
- What updating means? Better default ones?[/quote]
I mean a fresh coat of paint to make the editor look higher quality, higher resolution with effects like highlights and shadow in the texture.

-------------------------

cadaver | 2017-01-02 01:12:57 UTC | #9

[quote="dragonCASTjosh"]
My plan for this was to compile the shader to its target format upon saving the shader file.
[/quote]
Don't get this outright. Do you propose only working on shaders in an integrated editor? I would be likely editing/saving shader source in a text editor between program runs.

-------------------------

namic | 2017-01-02 01:12:57 UTC | #10

About the unified shading language: there's no need to reinvent the wheel with [github.com/bkaradzic/bgfx](https://github.com/bkaradzic/bgfx) around.

-------------------------

yushli | 2017-01-02 01:12:58 UTC | #11

@dragonCASTjosh, If you really have time and energy to begin the overhaul, please bring the newly added PBR feature to the next level first. Compare it to Unity's level of performance and feature richness. Then make a real world sample game using this PBR feature. It is hard to convince other people to use this feature if it is left half way to the product level of quality.

-------------------------

Enhex | 2017-01-02 01:12:58 UTC | #12

[quote="dragonCASTjosh"]
[quote="Enhex"]? Material Prototypes
- Don't know what that means.[/quote]
it is essentially inheritance for materials, for example a child material that just changes the diffuse color 
[/quote]
Resource wise I'm not sure if it's a good idea - it will save some writing and will require less maintenance but will be more complex and inspecting materials will be harder because you'll have to track down base material files.
Programmatically it's possible to clone a material and do changes, that's what I do now when I have a base material with some variable parameter like color, which is easier to manage because there are no extra files to maintain, which also means faster loading.

[quote="dragonCASTjosh"]
[quote="Enhex"]? Support for Code Plug-ins
- Not sure what you mean by plug-ins, but you can already use Urho as a C++ library and add whatever you want. And there's scripting.[/quote]
I way for the community to write features that are not suitable for the main repo, yes you can make your own fork but that often means that the branch if behind. With plugins features like a new scripting language or new editor features could just be a small download the you can load into the engine or editor to get that feature.
[/quote]
You can write a C++ library on top of Urho without modifying it, so other users just need to include it. Personally I've wrote several libs that way even for internal use to avoid forking and allow reuse.
For example [topic1895.html](http://discourse.urho3d.io/t/external-imgui-integration/1815/1)

[quote="dragonCASTjosh"]
[quote="Enhex"]? Hand written documentation
- Already exists[/quote]
Most of the current documentation is generated from comments in the source, my idea was to go through and create documentation for everything by hand including code examples (look at unity and unreal for reference). i know this would take allot of time and would be an ongoing project but it feel it would be beneficial
[/quote]
You have [urho3d.github.io/documentation/HEAD/pages.html](http://urho3d.github.io/documentation/HEAD/pages.html))
The comments are hand written, and you got the samples for code examples.
I don't see where the problem is, did you run into specific cases where the documentation wasn't enough? If so those specific cases should be fixed.

[quote="dragonCASTjosh"]
[quote="Enhex"]? Updated UI textures
- What updating means? Better default ones?[/quote]
I mean a fresh coat of paint to make the editor look higher quality, higher resolution with effects like highlights and shadow in the texture.[/quote]
So better default. I'm for, but I'm not sure if it should have high priority.

-------------------------

Bluemoon | 2017-01-02 01:12:58 UTC | #13

If its for UI makeover then I'm 100%  in support. I feel the UI needs a bit of work to be done on it. 
Was even starting up a lightweight pet project to uses HTML/CSS/JS for UI  so I can integrate it into Urho3D. If the project gains much traction I will definitely forward it as a UI proposal

-------------------------

cadaver | 2017-01-02 01:12:58 UTC | #14

[quote="namic"]About the unified shading language: there's no need to reinvent the wheel with [github.com/bkaradzic/bgfx](https://github.com/bkaradzic/bgfx) around.[/quote]
It is a working solution yes, but not something I'd call particularly elegant, or necessarily a "final" solution. It's based on macro / preprocessor transformations, and though it's based on GLSL it forces you to use non-idiomatic expressions, like doing matrix multiplication with a mul() function so it translates easily to HLSL. That's not necessarily bad, as long as the rules are clearly known, but there's room to search for even better solutions.

-------------------------

Enhex | 2017-01-02 01:12:58 UTC | #15

Regarding unified shading language:
There's a C++ library for OpenCL called [url=http://vexcl.readthedocs.io/en/latest/]VexCL[/url] which uses expression templates (with Boost.Proto) to compile C++ code to OpenCL/CUDA code.
I believe a similar thing can be done with GLSL & HLSL.

-------------------------

hdunderscore | 2017-01-02 01:12:58 UTC | #16

[quote="Enhex"][quote="dragonCASTjosh"]
[quote="Enhex"]? Material Prototypes
- Don't know what that means.[/quote]
it is essentially inheritance for materials, for example a child material that just changes the diffuse color 
[/quote]
Resource wise I'm not sure if it's a good idea - it will save some writing and will require less maintenance but will be more complex and inspecting materials will be harder because you'll have to track down base material files.
Programmatically it's possible to clone a material and do changes, that's what I do now when I have a base material with some variable parameter like color, which is easier to manage because there are no extra files to maintain, which also means faster loading.
[/quote]

Material inheritance is a pretty cool feature well demonstrated in UE4 (although in UE4 it's a must considering how long shader recompilation takes).

In this issue, weitjong mentions that it should be possible to use material inheritance already: [github.com/urho3d/Urho3D/issues ... t-86881286](https://github.com/urho3d/Urho3D/issues/684#issuecomment-86881286)

Exposing this to the editor would be the ideal scenario.

-------------------------

dragonCASTjosh | 2017-01-02 01:12:58 UTC | #17

[quote="yushli"]@dragonCASTjosh, If you really have time and energy to begin the overhaul, please bring the newly added PBR feature to the next level first. Compare it to Unity's level of performance and feature richness. Then make a real world sample game using this PBR feature. It is hard to convince other people to use this feature if it is left half way to the product level of quality.[/quote]

I actually have this finished for D3D11 although you will need to filter the cubemap outside the engine for the best results. all i need is to port it to OpenGL before i merge it. you can download a D3D11 demo here [url]https://drive.google.com/file/d/0B7EwsKWU8ATkclZnM0NhUEIyU1E/view[/url]

[quote="hd_"]Material inheritance is a pretty cool feature well demonstrated in UE4 (although in UE4 it's a must considering how long shader recompilation takes).In this issue, weitjong mentions that it should be possible to use material inheritance already: [github.com/urho3d/Urho3D/issues](https://github.com/urho3d/Urho3D/issues) ... t-86881286Exposing this to the editor would be the ideal scenario.[/quote]
I shall look into weitjong's suggestion and see how well it performs.

[quote="cadaver"]namic wrote:About the unified shading language: there's no need to reinvent the wheel with [github.com/bkaradzic/bgfx](https://github.com/bkaradzic/bgfx) around.It is a working solution yes, but not something I'd call particularly elegant, or necessarily a "final" solution. It's based on macro / preprocessor transformations, and though it's based on GLSL it forces you to use non-idiomatic expressions, like doing matrix multiplication with a mul() function so it translates easily to HLSL. That's not necessarily bad, as long as the rules are clearly known, but there's room to search for even better solutions.[/quote]
I did consider BGFX for more then just the shaders, it has a strong rendering abstraction but I'm not sure if its the best approach.

[quote="Enhex"]You can write a C++ library on top of Urho without modifying it, so other users just need to include it. Personally I've wrote several libs that way even for internal use to avoid forking and allow reuse. For example topic1895.html[/quote]
My issue with it is that it wont doesn't integrate with the editor, for example the terrain editor that the community made requires a separate executable rather then integrating with the existing editor


[quote="Enhex"]You have [urho3d.github.io/documentation/HEAD/pages.html](http://urho3d.github.io/documentation/HEAD/pages.html))The comments are hand written, and you got the samples for code examples.I don't see where the problem is, did you run into specific cases where the documentation wasn't enough? If so those specific cases should be fixed.[/quote]
My issue with it is when you go to learn the Scripting API you only have comments to work from for the most part, if there was a group effort to go through and remove all dependency on comments by hand writing it in detail including examples for everything, this would be an on going effort.

-------------------------

cadaver | 2017-01-02 01:12:59 UTC | #18

Plugins by themselves don't solve integration to the (current) editor. As it's a self-standing AngelScript application which cannot be accessed well from the outside (either C++ or Lua), the terrain editor would still need to be AngelScript too to integrate well, and to use the same UI / view system as the rest of the editor.

It's a different story if you are going to do a full C++ editor overhaul, and define an API for how plugins attach to the editor.

Plugins would be immediately beneficial if the only thing you need to do is to define extra components that you want to appear editable. Currently you'd need to construct a custom Urho3DPlayer that integrates your custom code (which adds things) and then runs the editor script.

-------------------------

dragonCASTjosh | 2017-01-02 01:12:59 UTC | #19

[quote="cadaver"]Plugins by themselves don't solve integration to the (current) editor. As it's a self-standing AngelScript application which cannot be accessed well from the outside (either C++ or Lua), the terrain editor would still need to be AngelScript too to integrate well, and to use the same UI / view system as the rest of the editor.

It's a different story if you are going to do a full C++ editor overhaul, and define an API for how plugins attach to the editor.

Plugins would be immediately beneficial if the only thing you need to do is to define extra components that you want to appear editable. Currently you'd need to construct a custom Urho3DPlayer that integrates your custom code (which adds things) and then runs the editor script.[/quote]
I would likely move the editor over to C++, that way the editor and the player are separate programs and the editor can launch the game for testing.

-------------------------

cadaver | 2017-01-02 01:12:59 UTC | #20

You don't need different executables for that really. You could just as well launch Urho3DPlayer from the editor again, with a parameter that runs the game script.

However I've spoken of this before, Urho is defined to be just a library, so there is not really a universal concept of how you "launch the game", as that can vary from project to project, or may not even make sense in some projects.

-------------------------

dragonCASTjosh | 2017-01-02 01:13:00 UTC | #21

Apparently glslang can now convert hlsl into glsl or spirv, both can be loaded with opengl

-------------------------

rku | 2017-01-02 01:13:03 UTC | #22

Editor really is a mess and thus extensibility or integrability of editor suffers. A clean (like rest of engine code) implementation of editor in c++ would be great addition. I think script editors are really out of scope for game engine, this is job for IDEs. Editor could be integrating with IDE (remote) debuggers instead to provide better experience for developer. I also think terrain editor can be great component. Argument that it is for specific game type thus should not be included makes no sense to me as long as using terrain component is totally optional.

-------------------------

cadaver | 2017-01-02 01:13:03 UTC | #23

A new C++ editor is a good idea and often repeated, but it would need a dedicated person or several. In the past I've suggested to make a separate editor project, which would be good for keeping the responsibility separate, but may not be good for adoption. Having the editor come with the engine codebase would make it clear that it's "official". However what I really don't want to see happening is a one-time contribution and dump of a C++ editor into the main codebase, after which the contributor becomes inactive, and the workload for existing maintainers grows. This is a development antipattern which has repeated quite many times in Urho history, and why I'd like to keep my personal maintenance responsibility strictly in the "runtime" part of the engine.

-------------------------

