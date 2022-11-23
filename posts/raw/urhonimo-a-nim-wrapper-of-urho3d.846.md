gokr | 2017-01-02 01:03:28 UTC | #1

Hey guys!

Just wanted to mention that there now is a full automatically generated Nim wrapper of Urho3D. See original announcement here on the Nim forum:

[url]http://forum.nim-lang.org/t/870[/url]

Much can be said about Nim. Many of us think it's much easier to use than C++ while offering the same performance (it compiles via C++) and many powerful features like advanced AST based macros for example.

If you are curious about Nim and Urhonimo, don't hesitate to talk with us on IRC, #nim on freenode.

regards, G?ran

-------------------------

GoogleBot42 | 2017-01-02 01:03:28 UTC | #2

I have never heard of Nim before... It seems like a promising language.  I will definally look at it and its Urho3D wrapper.   :slight_smile:

-------------------------

jmiller | 2017-01-02 01:03:32 UTC | #3

I am just getting acquainted with [b]Nim[/b] and so far, I'm thoroughly impressed. :slight_smile:

Thanks for the info!

-------------------------

boberfly | 2017-01-02 01:03:32 UTC | #4

Wow this is impressive gokr!

I've looked up Nimrod (well, now it's Nim) last year which looked like it had the power of C++ but the syntax akin to Python (which I'm all about). This could be an incredible productivity solution for developing games or tools on top of Urho3D without compromise from interpreter speed! 

I noticed Nim can compile to javascript, would Urho3D's recent emscripten support be compatible with this? I'm not too sure how they would be pieced together per-se.

Also can it be run interpreter-style in Urho3D itself or would it make sense to combine this with the runtime-compiled patches and encapsulate the Nim code in a library?

-------------------------

gokr | 2017-01-02 01:03:33 UTC | #5

Hi!

Regarding javascript, I have no idea. :slight_smile: But... Nim compiles via C++ soo... if a C++ Urho3D app can be "emscriptified" - then I can't see why a Nim Urho3D app couldn't. After all, it ends up as C++.

Also, after the announcement we have ported the particle demo (25) and the huge object count demo (20). I also added the F1 (ehm, console doesn't do much yet I think), F2 and 1-8 keys split out in a separate module sample.nim.

Huge.nim shows from my feeble testing that it seems to clock in almost 2x faster than Angelscript (update avg time) and that its basically the same speed as the original C++ demos (guesstimate a few % slower).

NOTE: For the moment you will not be able to compile huge.nim without a trivial hack in the Nim compiler, Araq will fix.

So... yes, Nim should offer basically the same speed as C++ but with a much nicer language (IMHO).

Can it run interpreted? No, but we intend to explore dynamic reloading of Nim modules. Also, it seems quite doable to make Nim put selected subsets of procs/methods in separate modules that then can be dynamically reloaded on their own. This means, as long as you only modfiy behavior - then all data should persist just fine.

regards, G?ran

-------------------------

GoogleBot42 | 2017-01-02 01:03:33 UTC | #6

I think it would probably be best to comile Nim to c++ and then convert that to javascript.  I kind of doubt that Nim's nim-to-javascript compiler will be able to output faster code in the end.  This is because at lot of optimazations are done by the c++ compiler and many are also done by the asm to javascript compiler... I doubt that the small development team of Nim could make anything faster but I might be wrong... Although, it is possible that Nim's javascript compiler actually coverts to C++ then javascript.  If that were the case I don't think there would be much difference in speed...

But, again, I don't know much about Nim...

-------------------------

