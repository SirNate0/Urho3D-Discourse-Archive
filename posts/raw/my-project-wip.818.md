setzer22 | 2017-01-02 01:03:07 UTC | #1

I finally have a video that I can show of my project. 

I've been working on this since I came here (most of the time has been learning the engine while porting from Unity). I've not been working on this full time so it's advancing at a pretty slow pace, but still here it is!

[video]https://www.youtube.com/watch?v=K-tuIG203qY[/video]

In particular in the video I'm experimenting with the effect of going from an schematic strategy view to a more detailed combat view.

Let me know what you think :smiley:

-------------------------

hdunderscore | 2017-01-02 01:03:07 UTC | #2

Nice !

The transition in scale from strategy to third person looks almost seamless, I didn't notice it at first.

How has your experience porting been? I need to get around to porting something I did a while back.

-------------------------

codingmonkey | 2017-01-02 01:03:08 UTC | #3

i'm think that you need to set textures for palms )
and two palma's leafs for Jack's for both side  )

-------------------------

setzer22 | 2017-01-02 01:03:10 UTC | #4

[quote="hd_"]How has your experience porting been? I need to get around to porting something I did a while back.[/quote]

Porting from unity has actually been quite easy. Theres a 1:1 equivalent in Urho to most Unity concepts. Most of my problems have been with C++ (I really wasn't used to pointers) and learning the more obscure parts of the engine API, like creating and registering your own components to mix script and C++. I'd say for anyone knowing both engines porting is going to be easy.

-------------------------

Stinkfist | 2017-01-02 01:03:11 UTC | #5

Looking good! It would be interesting to see also material from your original Unity-based game in order to see what the end product is going to look like.

-------------------------

setzer22 | 2017-01-02 01:03:12 UTC | #6

[quote="Stinkfist"]Looking good! It would be interesting to see also material from your original Unity-based game in order to see what the end product is going to look like.[/quote]

There's no such final product yet. I've already ported all the code I had. I actually decided to switch very early in the development because I couldn't stand Unity anymore with its restrictive licenses and their anti-Linux business model.

I really like Urho by the way! :smiley:

-------------------------

devrich | 2017-01-02 01:03:18 UTC | #7

Awesome work, setzer22 !! Reminds me of BattleChess ( I love the queen in that game from way waay back in the day on the pc )  :smiley:  

I have been trying to get a good working weather system going for these past few weeks but most of my time has been focused on getting to know my way around Urho3D.  I'm used to JavaScript for over a decade but I've been using Lua scripting with Urho3D in order to get up and running fast without worrying too much about pointers until I get a handle on how Urho3D's inner workings function. ( life and work has been taking most of my time these days -_- )

However; at times I find myself wanting to go with C++11 and smart pointers -- I am curious why you chose C++ / ActionScript over using Lua?  Is there a distinct benefit over Lua, or ?

-------------------------

cadaver | 2017-01-02 01:03:18 UTC | #8

If you have the choice, ie. you don't require Lua because of higher familiarity with it, you will have better bindings performance, safer programming, and more complete API bindings using AngelScript. This is mostly due to tolua++ being a poor bindings library, though exposing classes with it is quite pleasant (pkg files are mostly copied direct from C++ header files)

-------------------------

devrich | 2017-01-02 01:03:21 UTC | #9

[quote="cadaver"]If you have the choice, ie. you don't require Lua because of higher familiarity with it, you will have better bindings performance, safer programming, and more complete API bindings using AngelScript. This is mostly due to tolua++ being a poor bindings library, though exposing classes with it is quite pleasant (pkg files are mostly copied direct from C++ header files)[/quote]

My only issue with AngelScript is that it confuses me the 3 times i tried to learn it  :blush: .....  Is there a good place/tutorial I can go to try and learn AngelScript from? ( i would muuuch preferably something that teaches AngelScript using any version of Urho3D if at all available? )

-------------------------

setzer22 | 2017-01-02 01:03:24 UTC | #10

[quote="devrich"]Awesome work, setzer22 !! Reminds me of BattleChess ( I love the queen in that game from way waay back in the day on the pc )  :smiley:  

I have been trying to get a good working weather system going for these past few weeks but most of my time has been focused on getting to know my way around Urho3D.  I'm used to JavaScript for over a decade but I've been using Lua scripting with Urho3D in order to get up and running fast without worrying too much about pointers until I get a handle on how Urho3D's inner workings function. ( life and work has been taking most of my time these days -_- )

However; at times I find myself wanting to go with C++11 and smart pointers -- I am curious why you chose C++ / ActionScript over using Lua?  Is there a distinct benefit over Lua, or ?[/quote]

Thank you :smiley:

I use AngelScript because I already knew C++ beforehand and AngelScript is much more similar to it. Also I have never used Lua before, so my choice was quite clear.

And I started using C++ for my game's core because it performs better than scripting. But also because I wanted some practise with C++ and pointers (which I'm quickly becoming used to). After seeing the script performance in Urho it's basically the latter, because I don't really need the extra performance and the overhead seems to be minimal.

Also, with C++ you can use an IDE that provides autocompletion, which makes my life a bit easier while learning the API.

[quote="devrich"]My only issue with AngelScript is that it confuses me the 3 times i tried to learn it  :blush: ..... Is there a good place/tutorial I can go to try and learn AngelScript from? ( i would muuuch preferably something that teaches AngelScript using any version of Urho3D if at all available? )[/quote]

There's no Urho3D AngelScript tutorial I know of. But if you know any C-like language there's not much new stuff to learn. What did you struggle with when learning it?

-------------------------

devrich | 2017-01-02 01:03:25 UTC | #11

Thanks setzer22 :slight_smile:

I am basically at an intermediate level with c++11 and haven't done any c++ in many months now.  I know that pointers are important but I am all about smart pointers after watching youtube lectures from the c++ creator Bjarne Stroup, he rocks!

For over a decade now I have been extremely good at JavaScript ( not json nor node nore any other js librarys, just good ol JavaScript ) and as a kid I was heavily into BASICA, GW-BASIC, and QuickBasic so Lua was much easier for me to pick up.

AngelScript I had trouble understanding the "proper" use of the symbols and also the ways to get to class properties and methods. ( also how to properly use pointers in AngelScript ).  I know it's just my brain trying to learn that's the problem but if you could help me understand how these basic things work in AngelScript as compared to how they work the same way in C++11 with some Urho3D examples then I think I can use that to get me a really big jumpstart into properly understanding how AngelScript and Urho3D go together. 

Then I'd be more than glad to switch to AngelScript and see how far I can take it ( especially for my weathering system I am building ) and I'd owe you one for any help you can give me on this ( plus we'd get a good place on the forums to send newbies to AngelScript like me ) :smiley:

-------------------------

