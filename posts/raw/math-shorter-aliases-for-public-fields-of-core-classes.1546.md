freegodsoul | 2017-01-02 01:08:23 UTC | #1

[b]Motivation[/b]: When I write a math-intensity code, I want to write it as fast as possible.
[b]Problem[/b]: Oftenly-used math classes such as Vector3, Rect, Color, etc, have underscore-postfixed public field names. Instead of writing just "x" or "min", in addition I have to press a key once or even twice. It's not big issue, but annoying thing. It slows me down and final code looks ugly little bit.

For example, the code
[code]closest_corner.x = dmin_abs.x < dmax_abs.x ? rect.min.x : rect.max.x;
closest_corner.y = dmin_abs.y < dmax_abs.y ? rect.min.y : rect.max.y;
closest_delta.x = dmin_abs.x < dmax_abs.x ? dmin_abs.x : dmax_abs.x;
closest_delta.y = dmin_abs.y < dmax_abs.y ? dmin_abs.y : dmax_abs.y;[/code]
looks mush better for me than
[code]closest_corner.x_ = dmin_abs.x_ < dmax_abs.x_ ? rect.min_.x_ : rect.max_.x_;
closest_corner.y_ = dmin_abs.y_ < dmax_abs.y_ ? rect.min_.y_ : rect.max_.y_;
closest_delta.x_ = dmin_abs.x_ < dmax_abs.x_ ? dmin_abs.x_ : dmax_abs.x_;
closest_delta.y_ = dmin_abs.y_ < dmax_abs.y_ ? dmin_abs.y_ : dmax_abs.y_;[/code]

There are many reasons to eliminate underscores in public field names of widely-used core math classes:
1) The code is [b]shorter[/b]
2) [b]Beautiful[/b]
3) [b]Faster[/b] writing and refactoring
4) [b]Conventional [/b]naming (Most of engines and libraries are using simple notation: lowercased without underscores. Examples: Unity, glm, glsl, hlsl)

So I found simple solution for me:
In Urho3D's class headers I've cover the public fields by [b]union[/b] statements, e.g. [b]Vector3[/b] member definitions look like this:
[code]/// X coordinate.
union
{
	float x_;
	float x;
};
/// Y coordinate.
union
{
	float y_;
	float y;
};
/// Z coordinate.
union
{
	float z_;
	float z;
};[/code]

[b]download[/b]: [url]http://gdurl.com/AamL[/url] (modified headers only)

Now I can write math code in Unity-style without using external library! Happy coding :smiley:

-------------------------

codingmonkey | 2017-01-02 01:08:23 UTC | #2

>but annoying thing
yep, this is pain for me too )
thanks for showing how this may be solved in elegant manner

-------------------------

franck22000 | 2017-01-02 01:08:24 UTC | #3

Yes :slight_smile: That change should be pushed in masterbranch !

-------------------------

1vanK | 2017-01-02 01:08:24 UTC | #4

[quote="franck22000"]Yes :) That change should be pushed in masterbranch ![/quote]

I think, various code style in one project is bad idea

-------------------------

freegodsoul | 2017-01-02 01:08:24 UTC | #5

[quote="codingmonkey"]thanks for showing how this may be solved in elegant manner[/quote]
[quote="franck22000"]Yes That change should be pushed in masterbranch !:)[/quote]
I'm glad to hear it =)

[quote="1vanK"]I think, various code style in one project is bad idea[/quote]
In [b]one[/b] project maybe. But there are two projects:
1) [i][Explicit][/i] Urho3D engine
2) [i][Implicit][/i] End-User's project, [b]using[/b] the engine

;D

-------------------------

1vanK | 2017-01-02 01:08:24 UTC | #6

> In [b]one[/b] project maybe. But there are two projects:
> 1) Urho3D engine
> 2) End-User's project, [b]using[/b] the engine

I just expressed my opinion about sending of PR :)

-------------------------

freegodsoul | 2017-01-02 01:08:24 UTC | #7

[quote="1vanK"]I just expressed my opinion about sending of PR :slight_smile:[/quote]
Ok, i get it)

-------------------------

Enhex | 2017-01-02 01:08:24 UTC | #8

I don't see what purpose suffixing every member with "_" serves.

-------------------------

codingmonkey | 2017-01-02 01:08:25 UTC | #9

>I don't see what purpose suffixing every member with "_" serves.

this is just rule for member variables
[urho3d.github.io/documentation/H ... tions.html](http://urho3d.github.io/documentation/HEAD/_coding_conventions.html)
[quote]?Variables are in lower-camelcase. Member variables have an underscore appended. For example numContacts, randomSeed_.[/quote]

then you looked into code you are know what of these variables are member for this class or struct and what not

-------------------------

Enhex | 2017-01-02 01:08:25 UTC | #10

[quote="codingmonkey"]this is just rule for member variables[/quote]
A rule isn't a valid reason.

[quote="codingmonkey"]then you looked into code you are know what of these variables are member for this class or struct and what not[/quote]
When you access member vars you have the class instance prefixing them, f.e. position.x.
When you look inside a member function it's obvious that it is member var if it isn't a parameter.
It carries no semantic value.

The only possible case  in which it makes "sense" is when you have failure you properly express parameter name in a member function, f.e.:
[code]
MyClass::setX(float x)
{
    x = x; // bad. "setting x to x" doesn't make sense.
    x_ = x; // hack
    x = x_; // hack (paramter is x_)
    mX = x; // hack
   [random prefix]x[random suffix] = x // same hack, different string
}
[/code]

In that example naming the parameter "x" is bad, it's unexpressive and collides with the class's x.
Instead it should be something like this:
[code]
MyClass::setX(float new_x)
{
    x = new_x; // Setting x to the new value of x. Much better semantics, makes perfect sense
}
[/code]

Instead of prefixing/suffixing every member var with something, which is a kludge and doesn't carry any semantic value.
Marking a member variable as a member variable is redundant because the information is already there.

-------------------------

freegodsoul | 2017-01-02 01:08:26 UTC | #11

[quote="Enhex"]
[code]
MyClass::setX(float x)
{
    x = x; // bad. "setting x to x" doesn't make sense.
[/code]
In that example naming the parameter "x" is bad, it's unexpressive and collides with the class's x.
[/quote]

What you think about using [b]this[/b] keyword?
Example:

[code]MyClass::setX(float x)
{
    this->x = x;
}[/code]

-------------------------

Enhex | 2017-01-02 01:08:26 UTC | #12

While using "this->" is only required inside member functions, it's still marking member var as a member var and kludging around proper semantics.

-------------------------

TikariSakari | 2017-01-02 01:08:26 UTC | #13

Aren't underscores used on member names mostly to avoid coding errors. Isn't that purpose of most coding conventions to write less buggy code.

Something like after doing tons of iterations to a function:
[code]
void classA::functionA()
{
   x = 0; // <--- after modifying code for several times, you might accidentally fiddle members value, because you used
            // to create new x-variable in here.
   for( int x = 0; x < WIDTH; ++x) // Do something
   {}
}

[/code]

edit: Altho this kind of error could be avoided by using const keyword on declaring functions

-------------------------

Enhex | 2017-01-02 01:08:26 UTC | #14

[quote="TikariSakari"]Aren't underscores used on member names mostly to avoid coding errors. Isn't that purpose of most coding conventions to write less buggy code.

Something like after doing tons of iterations to a function:
[code]
void classA::functionA()
{
   x = 0; // <--- after modifying code for several times, you might accidentally fiddle members value, because you used
            // to create new x-variable in here.
   for( int x = 0; x < WIDTH; ++x) // Do something
   {}
}

[/code]

edit: Altho this kind of error could be avoided by using const keyword on declaring functions[/quote]

How does it changes anything? If you forgot to delete test code, you forgot to delete test code. Having a suffix won't magically send you emails to remind you.

-------------------------

freegodsoul | 2017-01-02 01:08:29 UTC | #15

Good news! I have posted a proposal in "Developer Talk" section, which might to improve math library's usability: [url]http://discourse.urho3d.io/t/math-library-improvement-proposal/1558/1[/url]

-------------------------

Modanung | 2017-01-02 01:08:32 UTC | #16

[quote="Enhex"]
A rule isn't a valid reason.
[/quote]
There may be a valid reason for the rule.
[quote="Enhex"]
Instead of prefixing/suffixing every member var with something, which is a kludge and doesn't carry any semantic value.
Marking a member variable as a member variable is redundant because the information is already there.[/quote]
When you learn the underscore is a conventional way of marking member values it receives its semantic value. To me removing the underscore would remove the name's very semantics.
Also adding accessing member values without underscore postfix as an option makes them unavailable as parameter names.
[quote="Enhex"]
When you look inside a member function it's obvious that it is member var if it isn't a parameter.
[/quote]
I like that I can write:
[code]Class::Class(const int a, const int b):
a_{a},
b_{b}[/code]
...as the constructor's head.
[quote="Enhex"]
[code]
MyClass::setX(float new_x)
{
    x = new_x; // Setting x to the new value of x. Much better semantics, makes perfect sense
}
[/code]
[/quote]
This can make parameter lists longer than is required.
The way it is works perfect for me and I apply the same logic in my own code.

-------------------------

Enhex | 2017-01-02 01:08:33 UTC | #17

[quote="Modanung"]
When you learn the underscore is a conventional way of marking member values it receives its semantic value. To me removing the underscore would remove the name's very semantics.
Also adding accessing member values without underscore postfix as an option makes them unavailable as parameter names.
[/quote]
There's 0 semantic value. Does hgfdsaughdasX mean anything to you? It carries exactly the same semantic value as _x.
The fact you have meta information about the variable doesn't mean the information is there.

Initialization list works with using the same name, the following code is valid:
[code]
MyClass::MyClass(const int a, const int b) :
a(a),
b(b)
[/code]

[quote="Modanung"]
This can make parameter lists longer than is required.[/quote]
It doesn't make anything longer than it needs to be.

-------------------------

yushli | 2017-01-02 01:08:35 UTC | #18

Variable names has semantics. Definitely not 0 semantics with the underscore. Otherwise why not just name every variable a1, a2 ,a3...? underscore at the end means that (at least to me) this variable belongs to a class, not a temporary one. Here I agree with Modanung, it is good to be able write code like he mentions.

-------------------------

Modanung | 2017-01-02 01:08:35 UTC | #19

[quote="Enhex"]
Initialization list works with using the same name, the following code is valid:
[code]
MyClass::MyClass(const int a, const int b) :
a(a),
b(b)
[/code]
[/quote]
But ambiguity is maintained in the constructor?s body. Also at first glance this looks like some circular initialisation to me.

-------------------------

rikorin | 2017-01-02 01:08:35 UTC | #20

This code is perfectly normal, I always write it that way in my personal projects. The thing is, good IDE shows local variables in a different color, so there is no ambiguity.
To be honest, I really hate underscores, but sadly there is no better solution for public projects.

-------------------------

Enhex | 2017-01-02 01:08:36 UTC | #21

[quote="yushli"]Variable names has semantics. Definitely not 0 semantics with the underscore. Otherwise why not just name every variable a1, a2 ,a3...? underscore at the end means that (at least to me) this variable belongs to a class, not a temporary one. Here I agree with Modanung, it is good to be able write code like he mentions.[/quote]
"_" doesn't mean anything. You fail to realize that meta information isn't information.
And in your example I could say "a" means belongs to a class. Is the information there? No.

-------------------------

yushli | 2017-01-02 01:08:36 UTC | #22

As long as you are consistent with using a at the beginning of variables to mean they are members of a class, there is meanings there. That is why we need a coding rule to guide the coding style. As long as they are consistent, there is meanings. 
Coding style is very different from people to people, even the same person would prefer different style with time goes. So just pick what one likes most.

-------------------------

Enhex | 2017-01-02 01:08:36 UTC | #23

The information isn't there, it's external to the code thus meta.
Coding style isn't code.

-------------------------

Modanung | 2017-01-02 01:08:36 UTC | #24

[quote="Enhex"]You fail to realize that meta information isn't information.[/quote]
You appear to be stating metaphysical impossibilities. Or is it doublethink?
[quote="yushli"]Coding style is very different from people to people, even the same person would prefer different style with time goes. So just pick what one likes most.[/quote]
Exactly, but since we're dealing with shared code: here's a link to the [url=http://urho3d.github.io/documentation/1.5/_coding_conventions.html]Urho3D coding conventions[/url].
[quote="[url=https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md#S-naming]C++ Core Guidelines[/url]"]Consistent naming and layout are helpful. If for no other reason because it minimizes "my style is better than your style" arguments. However, there are many, many, different styles around and people are passionate about them (pro and con). Also, most real-world projects includes code from many sources, so standardizing on a single style for all code is often impossible.[/quote]
Also note that the C++ Core Guidelines are "...less concerned with low-level issues, such as naming conventions and indentation style." for exactly this reason.

-------------------------

yushli | 2017-01-02 01:08:37 UTC | #25

I am quite satisfied with Urho3D's coding convention. I will  stick with it.

-------------------------

