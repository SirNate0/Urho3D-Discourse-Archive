sand2710 | 2019-06-30 17:38:12 UTC | #1

Hello,

I followed the discussion about the rendering order

https://discourse.urho3d.io/t/how-to-control-render-order/1240/20

but it is not clear to me how it was solved (enhex's hellbreaker is fantastic).

My first attempt was to replicate the code proposed by enhex (I used actionscript) but SetRenderOrder still doesn't work or I'm doing something wrong, in 18_CharacterDemo.as:CreateCharacter ()

        Node @ xNode = characterNode.CreateChild ("test");
        xNode.scale = Vector3 (0.25f, 0.25f, 1.0f);
        xNode.position = Vector3 (0.5f, 0.9f, 1.5f);
        StaticModel @ xobject = xNode.CreateComponent ("StaticModel");
        xobject.model = cache.GetResource ("Model", "Models / Box.mdl");
        xobject.castShadows = true;
        // (is there a way in actionscript to use clone () without declaring two variables?)
        Material @ mat = cache.GetResource ("Material", "Materials / Jack2.xml");
        Material @ mat2 = mat.Clone ();
        mat2.renderOrder = 200;
        Technique @ tec = mat2.techniqueEntries [0] .technique;
        Technique @ tec2 = tec.Clone ();
        Pass @ pass = tec2.GetPass (tec2.passNames [0]);
        pass.depthTestMode = CMP_ALWAYS;
        xobject.material = mat2;



As a second attempt I duplicated the Material and the Technique, but I am not yet confident with the urho render pipeline and materials, I enabled DumpResources on exit and I see that the updated material and technique are used:

    Materials / Jack2.xml
    Techniques / NoTexture2.xml

I see the shaders that are used:

    Shaders / GLSL / Shadow.glsl
    Shaders / GLSL / LitSolid.glsl
    Shaders / GLSL / Basic.glsl

it is not clear to me where to intervene to associate a custom shader to the Jack2 material (notexture has the attribute vs only for depth and shadow and depth is not even used ??)

I think the weapon is a fairly common requirement for a FPS, it would be nice to have a working example.

**edit**

Somehow I missed the fact that the notexture technique element has the vs attribute, I modified it and I see that the specified shader is loaded (Shaders / GLSL / LitSolid2.glsl)

I tried modifying VS with gl_Position.z * = 0.999 or gl_Position.z * = 0.01 but I don't see changes, do I have to change anything else?

-------------------------

Bananaft | 2019-07-01 10:16:37 UTC | #2

Hello, welcome to the forum!

Don't use box model. Take any concave model and you will see the effect of CMP_ALWAYS, and why it is bad idea for this case, because the different parts of gun model will have totally broken z order.

gl_Position hacking works surprisingly fine. But I would expect some problems down the line with z-precision, lighting or particle effects for example.

Make sure you change z value before this line in LitSolid.glsl:

    vWorldPos = vec4(worldPos, GetDepth(gl_Position));

Because that's the depth value that gets passed into pixel shader and then used for depth testing.

> I think the weapon is a fairly common requirement for a FPS, it would be nice to have a working example.

Best solution depends on exact renderpath and even post-effects you are using.

Good luck and have fun.

-------------------------

sand2710 | 2019-07-01 15:44:03 UTC | #3

Hi Bananaft, thanks!

I've been following Urho3D for some time, I think it's a fantastic engine and I finally found some free time to play with it. The documentation is good, I just wish there was a little more material about it (video tutorials, books?).

Back to the render order question, I didn't edit the post but I made some progress by following the directions of cadaver, adding basefps to renderpath, adding renderorder to the materials and CMP_ALWAYS in some pass. The box behaved quite well in the FP cam, the only oddity I noticed was some flicker in the shadow it receives, I imagined it depended on the fact that I resized the box.

Thank you very much for confirming that instead the shader is the way to go and for the valuable advice, I will try with a decent model with multiple parts, and a shader with z value parameterized as suggested by gawag.

> I think the weapon is a fairly common requirement for FPS, it would be nice to have a working example.
> 
> Best solution depends on exact renderingpath and even post-effects you are using.

To be honest, what I've been thinking about for some time and I'd like to see is a FPS multiplayer SDK made with Urho, simple to mod, I'm a Bad Company 2 fan, I often wonder if Urho can achieve a similar result (I think so ).

-------------------------

jmiller | 2019-07-01 21:31:31 UTC | #4

Hello and welcome!

I recall this depth hack by @1vank and more info from @cadaver.
https://discourse.urho3d.io/t/depthhack-for-weapon-rendering/2202

[quote="cadaver, post:2, topic:2202, full:true"]
Camera custom projection matrix should go in to master shortly, however this would require a per-object custom projection matrix (if we want to use shadows from the existing scene render) which can be somewhat unclean to get in. Ideas / PRs are welcome.
[/quote]

-------------------------

sand2710 | 2019-07-02 07:33:00 UTC | #5

Thanks @jmiller 

I had seen the DepthHack mentioned in the other thread but I hadn't seen this specific thread nor the video, very interesting, thanks again.

Incredibly I had never seen this video on youtube even though I often searched for Urho3D video and having already found some 1vank videos (some time ago I created a [Urho3D playlist](https://www.youtube.com/playlist?list=PLHl6zjcEAbLOGMbFb46-RZcWf-LOXXKii))

Today in the evening I should be able to proceed with my tests

-------------------------

Dave82 | 2019-07-04 19:06:46 UTC | #6

Just an idea. What would happen if we render the hands and weapon to a texture and then draw this texture on top of everything using a fullscreen shader ?

-------------------------

sand2710 | 2019-07-04 21:25:47 UTC | #7

@Dave82, some old FPS I saw used animated images, for the weapon in first person, but you still need a mask / alpha, at that point instead of a texture it would be enough to render it last. Personally at the moment I don't know enough about Urho3D's render pipeline for such an implementation, I don't know if the challenge is to get the mask/alpha together with the light and shadows of the main scene.

I had to push the test of the weapon in the stack but I expect to go back to it soon and post some results.

P.S. : I have a series of stupid questions like "how could I do this ..." or "would it be possible to do ...", what would be the best place to post them?

-------------------------

Modanung | 2019-07-05 21:50:33 UTC | #8

[quote="sand2710, post:7, topic:5267"]
P.S. : I have a series of stupid questions like “how could I do this …” or “would it be possible to do …”, what would be the best place to post them?
[/quote]

These forums will do, related followup questions can be asked in the same thread, but don't hesitate to start a new one either. There's also [Gitter](https://gitter.im/urho3d/Urho3D), and if you're question is _really_ stupid, just try formulating it more intelligently until it contains the answer (and then trim). Have you found your way into the [documentation](https://urho3d.github.io/documentation/HEAD/)?

-------------------------

