claudeHasler | 2020-03-15 13:43:16 UTC | #1

Hi, im using urhosharp ( the c# bindings of Urho3d) and im trying to get a material to move acros the surface of the model im applying it to. I've tried to use an animation of the uvoffset but it hasnt worked, all that happened is that my texture was stretched, no animation occurs.

Does anyone have a c++ code example for this? I can translate it to c# by myself.

This is what ive tried:
[Code]
Material mushroomMat = ResourceCache.GetMaterial("Materials/StoneTiled.xml");

ValueAnimation uvShiftAnimation = new ValueAnimation();
uvShiftAnimation.SetKeyFrame(0.0f, new Vector2(0.0f, 0.0f));
uvShiftAnimation.SetKeyFrame(1.0f, new Vector2(0.0f, 1.0f));

mushroomMat.Scene=scene;
mushroomMat.SetShaderParameterAnimation("VOffset", uvShiftAnimation/*, WrapMode.Loop, 1.0f*/);
[/Code]

-------------------------

1vanK | 2020-03-14 16:28:44 UTC | #2

 https://discourse.urho3d.io/t/basic-material-effects-for-rendering/2953

-------------------------

claudeHasler | 2020-03-14 22:27:53 UTC | #3

Thanks alot!

This worked for me (adapted from the UvSequencer class in the link)

[Code]
ValueAnimation uvShiftAnimation = new ValueAnimation();
uvShiftAnimation.SetKeyFrame(0.0f, new Vector4(1.0f,0.0f, 0.0f,0.0f));  
uvShiftAnimation.SetKeyFrame(1.0f, new Vector4(1.0f, 0.0f, 0.0f, 1.0f));

material.SetShaderParameterAnimation("UOffset", uvShiftAnimation, WrapMode.Loop, 1.0f);
[/Code]


Is there any documentation as to what i can control with SetShaderParameter? For example what paramer names exist, and what parameters can be passed to them? I passed float, Vector2, and Vector4 objects all with varying results, but without errors.

https://urho3d.github.io/documentation/1.6/_shaders.html

I've read this page but couldnt find any other information

-------------------------

