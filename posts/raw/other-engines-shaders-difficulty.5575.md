brojonisbro | 2019-09-15 22:40:46 UTC | #1

hey again!

Its a generic question and i know, probably everyone here is tired of this but
using any engine extract and getting shader code base, its easy to convert to urho3d pure c++ glsl?

anyone got experience on this? i already see on jmonkeyengine(2 times), ppls literally cloned a unity shader just seeing the .CS/.shader code to jmonkeycode(.java)

OK! Java and CSharp are "next to" each other but....

for real? im interested on this:

https://github.com/LuggLD/SmearFrame

(overwatch and 3D-JRPG like moves)

(ue4 is c++, but isnt hlsl based?)

thx again

-------------------------

SirNate0 | 2019-09-13 20:01:30 UTC | #2

Disclaimer: I've only tried this one or twice, so I'm not at all an expert.

The basic idea is to reverse engineer the shader and recreate it in Urho. If most of the work is completed calculations in the shader using fairly standard inputs this may mean just copying the code and changing some function/variable names to match the new engine's, and then just creating a Technique that uses that shader. Alternatively, this could mean more extensive work writing some extra code in c++ to collect and pass on additional shader parameters (like the LastPosition from the unity (?) example).

How much experience do you have with this sort of thing?

-------------------------

GoldenThumbs | 2019-09-14 02:54:56 UTC | #3

Not sure I really understand your question, but what I am getting is that you want to convert shaders meant for other engines to work with Urho? If so, that's totally possible and actually pretty easy. I do it a lot. Just message me if you need some explanations on how to do it.

-------------------------

brojonisbro | 2019-09-15 22:44:13 UTC | #4

i forgoted this thread, sry

@SirNate0 
reverse engineer u say for example... "convert lto" languages? i already tried convert my tic tac toe python game to c#, but when i was on the half i stopped;
experience? being sincere... not too much, i'm still studying yet, graphics, graphic maths, maths, etc
**i'm on the "phase": discovering** yet

@GoldenThumbs 
yeah, i'm curious about this cause, for example: a engine or framework using c# and hlsl
is possible to convert to glsl? i know, possible can be but
literally calling... a CODE CLONE?
is for example... opengl version a problem comparing to hlsl?

**if anyone here have a great,easy and free pdf book about glsl i'll be grateful**

I usually visit a lot of Japanese game development sites and there's alot of resources but they normally are using hlsl
for example, this japanese guy released on github a Guilty Gear / Zelda Breath of the Wild, will be awesome use this on urho3d and not on that "fake/not 100% open source" unreal engine 4

(source on description)
https://www.youtube.com/watch?v=5u-pyWSpoxw

-------------------------

Teknologicus | 2019-09-16 08:33:21 UTC | #5

You may find this helpful:  https://thebookofshaders.com/

-------------------------

brojonisbro | 2019-09-16 10:19:26 UTC | #6

Hey, thanks, i'll take a look on that

-------------------------

