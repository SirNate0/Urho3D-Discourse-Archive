Hans | 2020-05-25 08:26:37 UTC | #1

Hi, 

I am a novice hobbyist C++ programmer and I would like to try Urho. 
However, it's unclear to me if Urho can / is aimed to be used with only C++. 
Is it possible and, in the affirmative, is it convenient? Does it work out of the box?

Thanks a lot, and sorry for the newbie question.

-------------------------

Eugene | 2020-05-25 08:46:46 UTC | #2

Urho is C++ library first and foremost.
So the question doesn't really make much sense for me.
I mean... C++ libraries are made to be used from C++.

-------------------------

Hans | 2020-05-25 08:46:12 UTC | #3

Thank you Eugene! 

I was troubled by the mention, in the presentation page, of the following limitation: "C++ for performance-critical code", so I wondered if the engine was not aimed to be used with Lua in the general case. 

Thanks for your answer :slight_smile:

-------------------------

jmiller | 2020-05-26 22:15:49 UTC | #4

An understandable query. :slight_smile: 

What Eugene said.
To illustrate (edit: exact procedure will vary) a configuration step in [building](https://urho3d.github.io/documentation/HEAD/_building.html) without scripting support:
`script/cmake_generic.sh <build-dir> -D URHO3D_ANGELSCRIPT:bool=0 -D URHO3D_LUA:bool=0`

-------------------------

Hans | 2020-05-26 18:56:10 UTC | #5

Thanks for the tip jmiller, I will definitely try that :slight_smile:

-------------------------

