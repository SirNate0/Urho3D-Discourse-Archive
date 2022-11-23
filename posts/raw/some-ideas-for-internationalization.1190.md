1vanK | 2017-01-02 01:05:59 UTC | #1

1) There is an object that stores all the strings in all languages
2) This object has a property "current language"
3) This object has a method that returns a string with a certain identifier in the current language
4) When changed property "language" called a event
5) Any object can subscribe to this event and update their data when it occurs

Example:

[spoiler][img]http://s017.radikal.ru/i427/1507/f0/28fe743f84cc.jpg[/img] [img]http://s020.radikal.ru/i708/1507/84/40b18d1a5361.jpg[/img][/spoiler]

[drive.google.com/open?id=0B_XuF ... G5WbWRpdFk](https://drive.google.com/open?id=0B_XuF2wRVpw4RWRxTG5WbWRpdFk)

p.s. the source is very very dirty, it's only test

-------------------------

1vanK | 2017-01-02 01:05:59 UTC | #2

We need only one database for strings. Is it a good idea to implement it as a subsystem?

-------------------------

1vanK | 2017-01-02 01:05:59 UTC | #3

Updated version. Now loading strings from *.json.

[drive.google.com/open?id=0B_XuF ... HNYTi1RYW8](https://drive.google.com/open?id=0B_XuF2wRVpw4OENUMHNYTi1RYW8)

-------------------------

Bananaft | 2017-01-02 01:06:01 UTC | #4

?, ???????!

But i'm sure, it would be much better to store each language in separate file.

-------------------------

1vanK | 2017-01-02 01:06:02 UTC | #5

[quote="Bananaft"]?, ???????!

But i'm sure, it would be much better to store each language in separate file.[/quote]

I have not yet finished [github.com/urho3d/Urho3D/pull/783](https://github.com/urho3d/Urho3D/pull/783) , but it is already possible

-------------------------

thebluefish | 2017-01-02 01:06:08 UTC | #6

Simply amazing work dude!

-------------------------

rasteron | 2017-01-02 01:06:08 UTC | #7

Great work 1vank! looks like it officially came through. really curious in trying this one out.

-------------------------

jmiller | 2017-01-02 01:06:10 UTC | #8

Great work, 1vank!
An important feature (and great that Urho enjoys such a diverse user-base already).

-------------------------

