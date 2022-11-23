Yatsomi | 2019-05-23 13:20:03 UTC | #1

Im developing a 2D game. How can i create some animations like this? Can it achieve it in the editor?
Im mean creating keyframes in a timeline for node attributes like position or location.

![](upload://zL1JHEMKwyl7pKpOo07mFDaC94v.gif)

-------------------------

Modanung | 2019-02-23 08:24:36 UTC | #2

I have not used this feature myself, but a SplinePath seems the way to go:
https://discourse.urho3d.io/t/possible-splinepath-speed-bug/3943/18

-------------------------

Yatsomi | 2019-02-23 11:32:22 UTC | #3

Tnx man. So there is no way to create some keyframes in a visual timeline? i think i should add it to editor myself though im not familiar with such a thing.

-------------------------

weitjong | 2019-02-23 12:20:54 UTC | #4

Have to checked out attribute animation?

https://urho3d.github.io/documentation/HEAD/_attribute_animation.html

-------------------------

Modanung | 2019-02-23 14:40:22 UTC | #5

Hm, indeed that may be alot simpler yet sufficient.

-------------------------

Yatsomi | 2019-02-23 17:04:08 UTC | #6

Yes i did, but some animations should be created visually. I mean consider making something like this using 3 sprite node: 
![Folding%20platform|690x101](upload://nhjDtVnOiRPcNJeCnv3XLdXhQTJ.jpeg) 
Each sprite needs to rotate and positioned by hand. Also a box collider that its size change while the platforms unfold. Im developing a 2D platformer game and i need mechanics like this a lot. Its so hard to do this in code. Any suggestion?

-------------------------

I3DB | 2019-02-23 17:59:50 UTC | #7

It's not hard to do in code.

You are rotating and translating.

Once you try a few to see what's going on, you'll see how easy it is.

Also, you can readily animate using Actions. [The urhosharp guys describe them](https://developer.xamarin.com/api/namespace/Urho.Actions/). And they may have been ported into C++ already.

You could just apply your custom action to the nodes and get much better result than animating in a framewise manner. Often your custom action can just be a couple few existing actions applied in sequence or parallel.

So from #1 to #2, you rotated round a point. To #3 you translated along an axis then rotated around a point. To #4 you rotated around a point as is #5-#7.

[Here's a discussion about them](https://discourse.urho3d.io/t/urhosharp-actions/1655), but don't know the end result. But once you understand the base code behind actions, to animate, you'll see how easy it all is.

-------------------------

weitjong | 2019-02-24 03:27:48 UTC | #8

You can either use SplinePath as originally proposed by Modanung if your animation path is organic in nature or just based on some artistic impression; Or use the attribute animation if your animation is more mechanical or clockwork in nature. The former approach allows you to use the Editor to visualize and modify the path interactively. The latter approach does not have Editor support at the moment, I believe. Having said that, I think the value/object animation keyframe definition XML file can be easily generated using a small external util program. It should not be only faster to get it done, but also should produce more accurate result, IMHO.

-------------------------

Modanung | 2019-02-24 07:04:26 UTC | #9

Depending on the situation you _could_ also use skeletal animation for this purpose.

-------------------------

Yatsomi | 2019-02-24 14:55:43 UTC | #10

Thanks for the answer sir. I'm familiar with the actions and have no problem implementing it, but after that, animations should be create in code. As i said my problem is lack of a visual tool to create animations.

-------------------------

Yatsomi | 2019-02-24 14:59:36 UTC | #11

Thanks sir. I think your latter approach to use XML file will solve my problem. Do you have any external program in mind to doing that? I will start searching for it.

-------------------------

Yatsomi | 2019-02-24 15:03:18 UTC | #12

Thanks sir. you mean using something like Spriter? I think @weitjong solution to use exported XML animation from an external software is more efficient. But Spriter could work too. I will test both solutions and share the results.

-------------------------

weitjong | 2019-02-24 16:35:57 UTC | #13

The related documentation is quite scarce, but you can always turns to C++ implementation source code for clue. You can actually choose between XML format or JSON format as the animation resource definition file.

For ValueAnimation:
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Scene/ValueAnimation.cpp#L89
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Scene/ValueAnimation.cpp#L151

For ObjectAnimation:
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Scene/ObjectAnimation.cpp#L78
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Scene/ObjectAnimation.cpp#L131

The documentation does show how to load such resource file, however. If done correctly, perhaps you can reuse the same animation file for the grouping node (containing two sprite node) and for the individual node.

I don't know any of the external tool out there that can readily generate the resource file in these formats. These are anyway very Urho-specific format, but who knows you will be lucky to find one in your search. If I were you though, I would probably just use Ruby/Perl/Python/JS script to generate the JSON file myself. Isn't it just simple rotation? So, a simple sine wave function can do the trick, no?

-------------------------

Yatsomi | 2019-02-24 17:56:58 UTC | #14

Maybe its a simple rotation yeah, but its just an example to explain what i need. I have multiple mechanics that some of them have location, rotation and scale changes over the time and creating that effect through the code is just not efficient and not the right way in my opinion. If there was a visual animator tool, they could be easily created. There is no such a thing in the urho editor so i think searching for a program to export animation with XML or JSON will be the best option though they need to be changed in a way that urho can read them.

-------------------------

weitjong | 2019-02-25 00:39:03 UTC | #15

I just have an idea. I haven’t tried it myself. It is plausible that you still can use our current Editor to visualize the animation, but using other tool to modify the animation resource file. The Editor uses a file watcher, so it auto reloads the resource when its content changes externally. The Editor has a minimalist quake-like console where you can enter AS or LUA command. So, in theory you could invoke the animation resource load/save scripting API from the console window. Once the scene is setup, use the play button in Editor to play the value/object animation. Use external file editor to alter the key frame or add new one, and our Editor should reflect the changes interactively. Again, this is just an idea before my morning coffee and untested yet. So I wish you good luck.

-------------------------

Yatsomi | 2019-02-27 21:06:24 UTC | #16

I just wanna say thank you for being so helpful and responsive. I'm searching for the external tool and will test your idea as soon as i can.

-------------------------

