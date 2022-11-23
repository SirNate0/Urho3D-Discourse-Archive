slapin | 2017-06-01 00:27:18 UTC | #1

Hi, all!

Could please somebody suggest an engine or something with the following abilities:

1. Node system
2. Detour/Detour crowd integrated with node system
3. Bullet integrated with node system.

I'm mostly interested in Ogre now, but I'd like to find some already made library integrations,
so to not do all the engine work myself.
Please no commercial engines, I know about UE4, looking at it. I'm more interested in open source stuff now.
And no Godot please (I know about it).

-------------------------

smellymumbler | 2017-06-01 01:09:55 UTC | #2

* http://www.banshee3d.com/
* http://torque3d.org/
* Panda with https://github.com/consultit/p3recastnavigation and https://github.com/tobspr/RenderPipeline

-------------------------

slapin | 2017-06-01 02:18:12 UTC | #3

Ah, thank you so much for links!
I will look at these. torque still doesn't support Linux, but Panda is great
can't get to understand what Banshee is.but looks window-only too.
will go for Panda then.

-------------------------

smellymumbler | 2017-06-01 02:44:55 UTC | #4

Torque 3.9 works fine in Linux.

-------------------------

slapin | 2017-06-01 02:56:51 UTC | #5

Does it allow developing in Linux?

-------------------------

slapin | 2017-06-01 04:59:48 UTC | #6

Thanks, Torque3D works fine in Linux including editors.
It is very nice thing to play with. The only limitation it doesn't support Android and other OSes.
But I really need to spend time with it, as its editor is a dream!

-------------------------

slapin | 2017-06-01 05:00:10 UTC | #7

And asset pipeline is great too.

-------------------------

slapin | 2017-06-01 20:53:04 UTC | #8

Well, Torque3D seems in the same league with Urho, but a bit less flexible.
1. It doesn't have IK support
2. It doesn't have ragdoll support.

But the tools are nice. But no Android support...
Torque3D also consumes my character models very easily, unlike Urho, it supports many bones.
But tools.. I think something like Montague mount could be implemented in Torque3D easily.
But it is not possible to export whole house to Torque3D and control things individually and have separate collision objects... one have to export piece by piece and recombine in editor which sucks... Urho blender exporter fails to
set node coordinates, but there is collada and AssetImporter...

Strange... I will probably try to do something small with Torque, but will struggle with Urho for bigger project.
Also will look at Panda from time to time, and openmw...

-------------------------

smellymumbler | 2017-06-03 15:08:56 UTC | #9

Sadly, you won't find everything you are looking for in a single solution. Even using proprietary ones, you would have to buy content from third-party providers on stores. The best way to approach this is to find the engine that has the best documentation and the most maintainable code. 

I stopped using Torque 3D because the code was terrible. Too hard to do everything, because it was a huge mess. Banshee is getting there, has good docs and excellent code. Panda and Urho are very similar, but i chose Urho because the C++ SDK is vastly superior. 

Also, the Urho community rocks. :slight_smile:

-------------------------

slapin | 2017-06-03 21:04:35 UTC | #10

Well, I think I will try to look over some other engines. The good thing about Urho is that you can do everything yourself
the extensibility is great. Torque doesn't look too complicated, but misses features I won't be able to do myself.
But one can make simple adventure game with dialogue system and primitive AI in a few days with Torque, which is great. So for small isolated projects which do not need features Torque misses, Torque really makes development super fast, as it completely separates logic from content and have powerful conten pipeline.
Panda3D does have somewhat bigger community than Urho and somewhat more documented. Also entry
is easier. But on feature level it is basically the same. But I see some projects using it which do features I need so I could copy-paste. So I will definitely look at panda and try something with it to see how it scales.

For me currently Urho is the best as long as I don't stumble to some fundamental problems nobody
can help me with. At that times I want a bit of mouse programming, Unity style (or Torque style).
Something which Urho do not have.

-------------------------

smellymumbler | 2017-06-04 00:29:17 UTC | #11

Did you really like the content pipeline? I felt that the support for animated meshes in the default Character class was abysmal. Everything was hardcoded, in a bad way, so either i used the original skeleton, or GTFO. I ended up creating my own stuff, which defeated the purpose of using the engine in the first place. Same for weapons and vehicles. That's when i moved to Urho. (at the cost of losing those really good looking terrains :( )

I've always been curious about the performance impact of Python in Panda vs. AngelScript/Lua in Urho. Their SDK in C++ is very bad so it kind of forces you to use Python. Compiling the engine is also an issue and it's hard to integrate with your flow (unlike Urho, which is just a CMake submodule).

BTW: what's the problem with Godot?

-------------------------

slapin | 2017-06-04 01:25:57 UTC | #12

Well, I did not get to the problem part with characters in Torque. It looks like you have to create animations
for your character in individual collada files, this is where I stopped. This works, but not what I used for, and tedious.
But I'm not an artist, probably they like the workflow. What I like is predictability and solidness, so everything is well designed. Landscapes are created in no time. Did not go for vehicles, will look at these. Hardcoding is not bad when everything is solid... I did not have much  time to look at details too much yet.

The wrong thing about godot was when I played with it one could not get answers, and nothing basically worked.
Also many adverticed features had unadverticed limitation (i.e. worked only exactly like in examples from assets
from examples), and no way to make use in your own game. After lots of hard attempts like this (for about 2 years) I dropped entire thing and got to Urho. Implemented the same level of game in 2 weeks. Fell very sad about wasted time. I do not say Godot can't be used for something. I just could not find that something. Probably things have changed a lot after this, I don't know. Will give it another try after I finish my current projects and see.

-------------------------

slapin | 2017-06-04 05:20:56 UTC | #13

Also what I like about Torque is automatic generation of impostors. And it is hard to impossible to do in Urho.
I was not able to do this.

-------------------------

Eugene | 2017-06-04 07:47:53 UTC | #14

What do you mean by "generation of impostors"?

-------------------------

slapin | 2017-06-04 07:56:04 UTC | #15

Well, impostors are 2d textures on quad or 2 tris which replace actual mesh at average-large distances.
Like doom-style characters. So they are done from 9 directions, for example and displayed instead of 3D mesh.
Torque generates them automagically for all 3D models if requested. Nice feature.

-------------------------

Eugene | 2017-06-04 08:33:45 UTC | #16

Ok, I understood. When I needed this stuff, I wrote it with few lines of code. Render-to-texture several times, that's all. Actually, the main complexity is that impostors have different algorithms of generation and you have to use the most appropriate one if you want nice picture.

However, it'd be nice to have integration with Editor for such tasks. I haven't implemented that.

-------------------------

