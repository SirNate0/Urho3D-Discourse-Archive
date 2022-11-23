Spongie | 2017-01-02 01:02:42 UTC | #1

Hi, I just pushed this to my playground repos on github. 

< there would have been a link here, but it's not allowed on my first post. LOL :slight_smile: >

It's meant to be a very clear, yet satisfying overview for anyone who (like me) wants to learn at a slow pace where nothing
is hidden and all the code (and build instructions) is revealed in one file. I don't like it when the file is split up or when extra
"helper code" is somewhere else. This is as plain as it gets in C++, I reckon.

Please give feedback, I'm hoping this would attract more people or somehow benefit Urho3D. I'm a C guy, so I'm really on thin ice here.

EDIT: the link, [github.com/spongebob/playground ... xample.cpp](https://github.com/spongebob/playground/blob/master/urho3d_simple_example.cpp)

-------------------------

lexx | 2017-01-02 01:02:43 UTC | #2

Hi. 
I too like to write methods inside class (maybe because I use java and c# too).
Doesn't compile with MSVC++, 
add 
[code]
#ifdef _MSC_VER
#include <cstdio>
#define snprintf _snprintf
#endif
[/code]
in the beginning.

-------------------------

Spongie | 2017-01-02 01:02:44 UTC | #3

Hello, thanks for the feedback! I will put that in there.

The only reason you want the entire translation unit in one file is simply for clarity when looking at it as a beginners example, it's not very good for maintaining code.
Hopefully it showcases what is needed for ppl to get started experimenting with Urho3D themselves.

Java and C# barely qualify as languages, I put them in the same category as GW Basic. :wink:

-------------------------

lexx | 2017-01-02 01:02:44 UTC | #4

Im using your code atm, fewer files the better.
But :smiley:
[quote]
Java and C# barely qualify as languages, I put them in the same category as GW Basic. 
[/quote]
Dont make me laugh :smiley: These are good too. (at least for scripting). My games (in my homepages)
are written with java or c#, still I use c++ time to time (I dont like templates).
..

-------------------------

Spongie | 2017-01-02 01:02:45 UTC | #5

Yes please. I would also accept script examples for any language that may be used with Urho3D. Maybe I should even create a repository just for Urho3D examples that we can share.

-------------------------

