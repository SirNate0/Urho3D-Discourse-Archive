tni711 | 2018-06-27 21:06:21 UTC | #1

Hi,
I am new to game development and want to learn building 3D game as a hobby. I have years of C++ programming experiences but with only academic understanding of 3D graphics. Can anyone advise if Urho is a good place to start as compared to Godot? Godot seems to have a better Editor and better coverage on mobile platforms.

-------------------------

smellymumbler | 2018-06-27 21:06:21 UTC | #2

You should create a new thread with your questions. You should try to be more specific. But if you're new, go with Godot. Don't use Urho if you think that tinkering with engines isn't fun.

-------------------------

johnnycable | 2018-06-27 21:06:21 UTC | #3

Godot has an art-inclined workflow, 2d is mature, 3d is ongoing. Editor is good. 
Urho has programmer-inclined workflow. 3d is mature, 2d is ok. Editor is ok.

Mobile Warning, after Apple opengl deprecation: none of them support Metal on Ios.

-------------------------

tni711 | 2018-06-27 21:06:21 UTC | #4

Thanks for the key points. I agree Urho has programmer-inclined workflow and that is why I kind of like it even though Godot has a lot more publicity.

-------------------------

Alan | 2018-06-28 04:08:01 UTC | #5

[quote="johnnycable, post:3, topic:4359"]
Editor is ok.
[/quote]
Overstatement of the century :laughing:
[quote="tni711, post:4, topic:4359, full:true"]
Thanks for the key points. I agree Urho has programmer-inclined workflow and that is why I kind of like it even though Godot has a lot more publicity.
[/quote]
Since you said you have years of C++ experience Urho is probably going to be a great choice, however depending on what you're planning to do and also if you want to see results quickly it might not be the best option for you. I personally don't like Godot but sure give it a try and take your own conclusions. You might want to consider Unity too especially if you want to support mobiles.
That being said in my opinion Urho >>>>>>>>>>>> Godot :trollface:

-------------------------

tni711 | 2018-06-28 15:00:52 UTC | #6

Yes, Urho3D fits what I am looking for, a c++ open source 3D game engine that supports development in Linux platform. I am not looking for quick result. I don't mind investing a couple of months to get in-depth understanding of the engine and learn how to build some simple 3D games (thinking of building some 3D sport games of table tennis or tennis) with it. I like Urho3D a lot so far just by browsing the source models and playing with the sample programs. I hope I can get a better handle of it in a month or two.

I also like Godot. It is an excellent product with a lot of momentum recently. I spent a couple of weeks playing with it but want to explore other option which allows me to build the 3D game directly in c++. I think it is easier way to build up expertise on a product by reading the native source code. In Godot, you build the game using its GDScript language and it is not easy to navigate from GDScript script function to the actual c++ modules behind the scene.  The documentation which is already pretty good can only help you to get some basic concept.

-------------------------

slapin | 2018-06-29 01:18:22 UTC | #7

Godot allows C++ too, and it is quite nice. You can interop with editor in much nicer way than Urho does though.

-------------------------

tni711 | 2018-06-29 02:51:54 UTC | #8

As per the documentation, writing c++ via the gdnative plugin framework in Godot is really considered an exception rather than the normal workflow. The integration process is quite tedious, as least for me. The framework is still evolving to support dynamic linking rather than static link with the recent release. I would rather wait a little bit before spending time with this path.

-------------------------

slapin | 2018-06-29 04:49:17 UTC | #9

I just generally hacked the engine code for that. GDNative is immature and will be like this for a long time.

-------------------------

pSupaNova | 2018-07-24 10:40:00 UTC | #10

First into 3D games learn Unreal, that's a must this engine is not just for games and you can see the source, contribute to it too, make plugins and it's C++. 

Pick a few game engines and graphic libraries do your  research and play with them. 

I have tried a lot of engines concepts do cross on to other engines so the knowledge you gain is not wasted.

-------------------------

tni711 | 2018-07-27 03:12:36 UTC | #11

Yes, Urho3D is a better engine for starter like myself to learn about how game engine works. Unreal is a bit too much for me :slight_smile:

-------------------------

simonsch | 2018-07-27 13:23:55 UTC | #12

The choice if urho3d as an engine has not to be caused by the experience level of the developer. For me it was caused by an evaluation of my use case, alternative products and so on.
In short, if you develop native mobile applications with a lot of performance critical code written in c++ and you want to play the 'cross-platform' game you have not that many alternatives. Especially if you want to stay in your common IDE, urho can be used as a simple prebuilt c++ plug'n play library on mobile devices, while unity or others bother you to move all your development to the complete blown up editor. For apps like games this is good, but if you want only to fill a 3D view in your app as a surface view, this is totally an overkill.

Of course there are maybe other engines which fit into these requirements (feel free to mention them), but urho does a very good job in giving me the necessary abstraction from pure opengl + gpu implementations of performance critical parts.

-------------------------

