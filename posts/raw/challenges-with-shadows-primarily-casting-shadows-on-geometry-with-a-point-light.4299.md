mustacheemperor | 2018-06-08 20:23:22 UTC | #1

I'm cross-posting this from the UrhoSharp forum at the Xamarin discussion board. 

I'm trying to get shadow casting working and I must be doing something wrong because regardless of what I try I cannot get shadows to draw. I've found a couple other threads without much help.

I'm using a point light configured as 
    cursorLight = LightNode.CreateComponent<Light>();  cursorLight.LightType = LightType.Point;  
    cursorLight.Color = Color.White;  cursorLight.Range = (.02f);  cursorLight.ShadowIntensity = .5f;  
    cursorLight.Brightness = 3f;  cursorLight.CastShadows = true;  cursorLight.ShadowBias = new 
    BiasParameters(0.00025f, 0.5f);  cursorLight.ShadowCascade = new CascadeParameters(10.0f, 50.0f, 200.0f, 0.0f, 0.8f);  cursorLight.SpecularIntensity = 2f; 

I'm testing with two box primitives.
    var testBox = Scene.CreateChild(); testBox.SetWorldPosition(new Vector3(0, 0, 1f)); 
    testBox.SetScale(.04f); var testBoxModel = testBox.CreateComponent<StaticModel>(); 
    testBoxModel.CastShadows = true;

Additionally, I configured my renderer based on some of what I saw on GitHub and around Google results for this problem.
    Renderer.ShadowMapSize *= 4;
    Renderer.DrawShadows = true;

I can see the specular highlight of the light on the boxes, so I know it the light is working. But I cannot see a shadow. I expect the smaller box in front to cast a shadow on the box behind it. The front of the box lights properly, and the sides are darker, as I'd expect. But it does not project a shadow onto the geometry behind it. I've tried cranking the range on the light up much higher and that has no effect other than increasing the size of the specular highlight.

This is a HoloLens project. Are there known issues casting shadows using UrhoSharp in the HoloLens? I haven't encountered a problem like that yet. Something unusual I've noticed is that my lit textures appear illuminated from the front as if the scene has a directional light, but there are no other lights in my project. You can see in the screenshot that the front faces of the cubes appear more illuminated the other faces. Moving around the cubes etc doesn't alter this illumination. I experimented with placing my test shadow caster on one of the sides that is less illuminated, but that had no effect on the problem. I'm at my wit's end with this one - both the mysterious front illumination and the shadow problem. I'll be extremely grateful if anyone has an idea! I found one thread that says only directional and spot light shadows are supported on Urho Mobile - did the HoloLens inherit that limitation? That would be unusual, because it certainly has the horsepower to support that.

Edit: I just tested with a spotlight instead, and I still do not see shadows. 

I can only include one image in a post as a new user, the other imgur url's ending is E8fAG08.png. 

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/9/95e7082c41c0e937db61dfbb28c71665944a3ee3.jpg'>

-------------------------

mustacheemperor | 2018-06-12 15:37:49 UTC | #2

@Egorbo could you please confirm if there are known issues with lighting and shadows in the HoloLens StereoApplication implementation for UrhoSharp? I understand the project's developer community is probably too busy to address my specific problem but a nudge in the right direction would be really appreciated, at least whether or not I'm on a wild goose chase. 

I noticed StereoApplication.cs creates a directional light in the scene by default, which explains the front lighting that's constantly visible. Could that be preventing shadows from drawing altogether?

Edit: I've tried intercepting and removing the directional light right after calling base.Start() which removes the lighting effect but doesn't help this problem. Additionally, enabling shadows on that directional light doesn't do anything either.

-------------------------

