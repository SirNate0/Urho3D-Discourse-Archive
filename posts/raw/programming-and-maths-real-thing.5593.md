kapsloki | 2019-09-18 07:56:32 UTC | #1

So many languages: C, C++, Java, Javascript, C#... Most based on another!

What is the real thing about programming? Operating systems written in C, why not in C ++?

What language does one say "true programmer", is there that?

Mathematics as implemented in code? That looks very different from writing on paper.

Should mathematics be learned or just used as a library?

Does a real and good programmer have time to always make a new math library when creating new software that will use it?

How is OpenGL studied and how do I know what it is and when to use #define for the graphic or whatever?

**I would like to know opinions to increase my knowledge, thanks!**

-------------------------

jmiller | 2019-09-18 19:48:32 UTC | #2

Hello!
Programming languages share similar concepts, but are born from different requirements or tastes.
https://wikipedia.org/wiki/Ada_Lovelace is considered a real programmer ...*having written programming algorithms before computers were invented*. :brain: :) 

OSs written in C: They were once written in assembly or machine language. C has dominated for various reasons -- Unix, interoperability, popularity, momentum -- and it is like a portable assembly language: as close to the machine as possible while almost universally available for existing architectures. More on this: https://softwareengineering.stackexchange.com/questions/281882/why-does-c-provide-language-bindings-where-c-falls-short

Math: It is my impression that most programmers (and I include myself) have never made a math library outside of academics ... something about reinventing wheels. :)

OpenGL: I learned basics by studying Urho's GLSL shaders and web searching. https://opengl.org/

Web search/books should also be informative on much of this. And perhaps our C++ thread:
  https://discourse.urho3d.io/t/learning-c-to-use-urho3d/5316

-------------------------

Modanung | 2019-09-18 18:02:05 UTC | #3

Most of the math you should be familiar with will not ask more of you than secondary school. The main exception to that, I think, are the dot product and cross product. Understanding these can be very helpful, but is not common knowledge to the average person who just starts programming.
Dot Product|Cross Product
---|---
![Image](https://upload.wikimedia.org/wikipedia/commons/3/3e/Dot_Product.svg)|![Image](https://upload.wikimedia.org/wikipedia/commons/b/b0/Cross_product_vector.svg)

-------------------------

kapsloki | 2019-09-18 20:15:27 UTC | #4

@jmiller Thank you for the info and for the links, specially C++ link, I already downloaded some pdfs there :smiley:

@Modanung Thank you :smiley: talking about this image and what you said, you got more "math learn" resources for graphics?

-------------------------

Modanung | 2019-09-18 20:29:50 UTC | #5

Something like this?  

https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces

Or more like this?

https://github.com/lettier/3d-game-shaders-for-beginners

-------------------------

urnenfeld | 2019-09-18 21:05:13 UTC | #6

[quote="jmiller, post:2, topic:5593"]
OSs written in C: They were once written in assembly or machine language.
[/quote]

Lowest parts are still written in ASM. Context switching, MMU/MPU handling, Interrupts... Some OSs call it the ASP (Architecture Support Package). Typical code you will find in /arch...

[quote="kapsloki, post:1, topic:5593"]
Operating systems written in C, why not in C ++?
[/quote]

Despite there is no C++ in Linux or BSD, you still can find C++ inside newer kernels like Haiku-OS(BeOS successor) or Fuchsia(Google's).

-------------------------

Leith | 2019-09-19 04:33:00 UTC | #7

Dot and cross products can be explained fairly easily, when given contextual examples of their use in games, for me the complex math is more complex - we have things like Set Theory, skew symmetrics, hamiltonians, dual quaternions, barycentrics, not to mention complex equations that we end up learning once, implementing, and totally forgetting... I would absolutely agree that basic knowledge of vector mathematics (and yes, some trigonometry) will take you a long way, and would add that most of the rules for 3D vectors also work for 2D vectors, so it's definitely advisable to start with 2D vector math and then simply adding the third dimension...

-------------------------

suppagam | 2019-09-19 21:04:03 UTC | #8

The books from Lengyel are helping me a lot: http://www.terathon.com/lengyel/
And this one too: https://www.mcshaffry.com/GameCode/

Read those, and you're good.

-------------------------

Leith | 2019-09-20 07:07:30 UTC | #9

I'm certainly happy to share what I know, if there is anything specific that you (or anyone else) struggles to understand, or can't appreciate the value or purpose of, with respect to the mathematics of game development. I'm qualified in that stuff, and working on becoming qualified to teach it, so it would be good for me too.

-------------------------

