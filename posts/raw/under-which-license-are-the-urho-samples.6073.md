elix22 | 2020-04-10 11:59:08 UTC | #1

@migueldeicaza ,
I was curious  , under which license are the urho-samples .
Specifically I wanted to port SamplyGame  into Urho3D (as open source )
The urho-samples repository doesn't contain any license file.
https://github.com/xamarin/urho-samples .

Please advice.

-------------------------

Modanung | 2020-04-10 14:47:29 UTC | #3

As you may be well aware, those are not "our" Urho samples you linked to: As such you will need to get somebody from the Xamarin team to answer your question. As no license is included, it seems these samples would default to "all rights reserved", at first glance.
But since they abandoned UrhoSharp, one email might be able to change that.

-------------------------

elix22 | 2020-04-10 15:22:55 UTC | #4

@Modanung
@migueldeicaza is Xamarin and Xamarin is @migueldeicaza   
I deliberately provided  the link to the UrhoSharp samples , the idea is to port SamplyGame into Urho3D (AngelScript and C++ under open source license ).
You are right ,since there is no license , the default is "all rights reserved " which means I am not allowed to port it without prior written permission from the authors .
Another solvavble option , If the author would have added a permission file into the Github repository ,

-------------------------

Modanung | 2020-04-10 15:45:56 UTC | #5

Right, @migueldeicaza *would* be the one to ask. Note that he hasn't visited these forums since July.

-------------------------

1vanK | 2020-04-10 21:43:07 UTC | #6

I think no one will sue you for violating the license.

-------------------------

QBkGames | 2020-04-11 02:50:27 UTC | #7

... unless you sell it and make $1000000 :slight_smile:.

-------------------------

migueldeicaza | 2020-04-13 21:08:36 UTC | #8

Well, that is an oversight, it should be MIT, I will add the license now.

(Edit: I incorrectly said MIT/X11, I meant MIT).

-------------------------

migueldeicaza | 2020-04-13 21:08:43 UTC | #9

Fixed - it is MIT licensed.

-------------------------

elix22 | 2020-04-14 13:53:32 UTC | #11

Great , thanks 
I plan to port a customized version of SamplyGame into Urho3D , initially using Angelscript .
I will release the source code once it's ready.

-------------------------

SirNate0 | 2020-04-14 14:05:16 UTC | #12

It's your choice obviously, but since there's already an AngelScript game example (Ninja Snow War), why not a game using c++?

-------------------------

throwawayerino | 2020-04-15 15:13:57 UTC | #13

I hope not because I want my game to be the C++ sample game!

-------------------------

elix22 | 2020-04-20 18:22:26 UTC | #14

I completed it , I wrote it in Angelscript
C++ is my comfort zone ,  doing it 24/7.
I wanted to try Angelscript and see if it's suitable for prototyping small games.
The outcome looks really nice and it runs really well on mobile   .
You can read more about it below (source code included).

https://discourse.urho3d.io/t/development-branch-with-apples-metal-support-and-more-samples/6032/5

-------------------------

