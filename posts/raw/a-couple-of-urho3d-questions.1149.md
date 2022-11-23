mejon | 2017-01-02 01:05:43 UTC | #1

Hello,

I have a couple of questions to determine whether I?ll use Urho3D.

1. Can you use ads in the apps you create? e.g admob

2. Is it free to make and publish with no royalties?

3. How long does it take to learn Urho3D for a beginner?

4. What language does Urho3D use, or how are games in Urho3D created?

5. How long does it take to make your first game?

6. To create games with Urho3D do you have the option of just coding it, 
or can you create visually without needing to enter lines of code? 

7. What are some popular Ios/Android apps made with Urho3D?

8. Can you make the same type of games using Urho3D as you would using Corona SDK, Unity, or Construct2?

-------------------------

setzer22 | 2017-01-02 01:05:43 UTC | #2

I'll answer what I can:

2. Urho is released under the MIT license so you're completely free to develop anything with it and publish it without any kind of royalty.

3. Depends on many factors, like other engines you've used and your programming skills. But I would say it takes longer than similar engines like Unity due to lack of tutorials and learning material. The documentation is very well written but for a begginer it can feel lacking sometimes. Also you have lots of examples that illustrate most common functionalities.

4. You can code in C++, AngelScript, Lua. You can also mix them, although mixing C++ and scripting is not trivial nor very documented, so it's not recommended for begginers. Usually it's easier to start off using one of the scripting languages. 

6. You can make a game totally in code (just like it's done in the examples) or you can use the visual editor to arrange your scenes and add components. But there's no way to do a game in Urho without some programming.

8. You can make any game in Urho, it's not restricted in any way nor designed specially for any game genre.

-------------------------

thebluefish | 2017-01-02 01:05:43 UTC | #3

[quote="mejon"]
1. Can you use ads in the apps you create? e.g admob
[/quote]

Of course you can. It's entirely open-source, and just depends on how much effort it takes for that specific platform to be integrated.

[quote="mejon"]
2. Is it free to make and publish with no royalties?
[/quote]

[url=https://github.com/urho3d/Urho3D/blob/master/License.txt]MIT license[/url]. No royalties, very little restriction on what you can do.

[quote="mejon"]
3. How long does it take to learn Urho3D for a beginner?
[/quote]

It depends on the beginner. Someone could have a new concept down for a game jam in just a couple days. Other people may take months before their first project comes to life. It's all based on that individual's skill level, just like any other engine. Though I have to say it's certainly much more readable that some other engines I've seen.

[quote="mejon"]
4. What language does Urho3D use, or how are games in Urho3D created?
[/quote]

The entire engine is written in C++, and largely C++ is the main language used. Angelscript and LUA are both available as scripting languages, and can both serve as a full game with a minimal C++ wrapper.

[quote="mejon"]
5. How long does it take to make your first game?
[/quote]

Again, it depends on many factors. Depending on skill level, how quickly you learn, complexity of the game, any issues you run across, etc... it could take anywhere from a day to several months.

[quote="mejon"]
6. To create games with Urho3D do you have the option of just coding it, 
or can you create visually without needing to enter lines of code? 
[/quote]

To create a scene with Urho3D, there is a full WYSIWYG editor. However you will still need to make the game logic to actually do something with it.

[quote="mejon"]
7. What are some popular Ios/Android apps made with Urho3D?
[/quote]

Popular? None that I know if. There are mobile projects in the [url=http://urho3d.prophpbb.com/forum11.html]Showcase[/url] forum. Though do keep in mind that Urho3D has a small community and so it hasn't attracted any big developers.... yet.

[quote="mejon"]
8. Can you make the same type of games using Urho3D as you would using Corona SDK, Unity, or Construct2?
[/quote]

Yes.

-------------------------

