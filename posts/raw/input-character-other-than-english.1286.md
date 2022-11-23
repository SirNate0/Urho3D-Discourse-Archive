yushli | 2017-01-02 01:06:36 UTC | #1

Is it possible to input characters other than english in Urho3D's UI element?

-------------------------

weitjong | 2017-01-02 01:06:36 UTC | #2

Currently I think the answer is no. Although we have String class that supports UTF8 characters, the Input subsystem does not has any interfaces to input method framework or IME. Naturally the API is not platform-agnostic. On Linux side, we have ibus and older scim. Both are LGPL, so I don't think Lasse would allow any direct interface with them within Urho3D library. Not sure what they have on Windows platform. Still, I think it is ok to interface with a chosen IME in your own project.

-------------------------

1vanK | 2017-01-02 01:06:37 UTC | #3

[url=http://savepic.su/6032521.htm][img]http://savepic.su/6032521m.jpg[/img][/url]

-------------------------

cadaver | 2017-01-02 01:06:37 UTC | #4

SDL may have some level of IME support, so one answer would be to investigate that.

-------------------------

1vanK | 2017-01-02 01:06:37 UTC | #5

On my screenshot I input the path manually, so it works :)

-------------------------

weitjong | 2017-01-02 01:06:38 UTC | #6

[quote="1vanK"]On my screenshot I input the path manually, so it works :slight_smile:[/quote]
I don't know how many alphabets or glyphs you have in Russian language and what kind of keyboard you use there, but if it works then I can imagine they are limited and the keyboard that you use can generate the UTF8 character directly. In Chinese language, we have more glyphs than our qwerty keyboard can hope for to map directly. The term "input method" is usually only relevant for such language where it imploys an indirect mean to input those glyphs via a normal qwerty keyboard. I am assuming OP is referring to this.

-------------------------

aster2013 | 2017-01-02 01:06:39 UTC | #7

I have add IME support code in Urho3D for windows. I can enter Chinese character in UI element.

???????????

-------------------------

yushli | 2017-01-02 01:06:39 UTC | #8

Is that support code already in Urho3D master branch? Or where can I find it?

-------------------------

thebluefish | 2017-01-02 01:06:39 UTC | #9

I would be interested to know as well. Urho3D 1.4 does not seem to support my Windows Japanese IME.

-------------------------

weitjong | 2017-01-02 01:06:40 UTC | #10

I just did a quick regex search on our SDL library code base in our master branch. It seems that the version we currently have only has IME-related code for Windows platform. I wonder if the latest version of SDL has made any progress in this area. The input method support is in the SDL 2.0 roadmap according to their Wiki here: [wiki.libsdl.org/Roadmap#Keyboard_Input](https://wiki.libsdl.org/Roadmap#Keyboard_Input).

-------------------------

