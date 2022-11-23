Avagrande | 2019-07-18 08:31:28 UTC | #1

I am having some trouble with LUA errors, I have compiled urho3d with the URHO3D_SAFE_LUA at ver 1.7.1 with luajit and I keep getting strange type errors.

I am creating render surfaces so I need to use GetRGBAFormat but I can't use it since it reports back to me: 

"GetRGBAFormat argument #1 is 'Graphics'; 'Graphics' expected"

I assume this has something to do with the function being static? It worked when I disabled the safe lua flag.

Has anyone had this error before?

-------------------------

Leith | 2019-07-18 09:47:38 UTC | #2

I don't know about this one, but I am having troubles on the angelscript side. I don't use the standard application model, but then again I don't do anything weird... we're in the same boat.
I actually do have experience in lua - which is why I chose not to use it.

-------------------------

Avagrande | 2019-07-18 10:12:00 UTC | #3

I think having wrappers in tolua++ is probably not ideal... its kind of old. 
I had been writing wrappers for lua before and opted for sol2 which made wrappers a breeze. I think overall the lua side could be improved substantially considering the way it handles resources. 

Yesterday I worked on 2d stuff and in lua its impossible to create a Sprite2D on its own since its a resource so I had to copy code from the cpp source and process the rectangles myself and push em to the StaticSprite2D, its a shame really. urho3d is a pretty good engine tho it just needs a good clean up.  

Although to be fair I am doing some strange things, currently I am stuck on a crash when I try to render the character sprite as I have a billboard with a render target and within that render target I am using another one and that always crashes which prompted me to get safe lua so I have a chance at debugging it.

-------------------------

Leith | 2019-07-18 10:16:18 UTC | #4

I do strange things too - I start my own application, I load my own scenes, I run my own scripts, and I get odd results, and no responses from the wings of this academy. Apparently, we're all meant to live under the mantle.

-------------------------

