Vincentwx | 2017-01-02 01:11:39 UTC | #1

Today, at Build 2016 , Microsoft announced Xamarin is now free for every edition of Visual Studio, including the free community edition. For everyone who are using Urho3D through UrhoSharp with C#, now you can use it at NO extra cost.

-------------------------

hdunderscore | 2017-01-02 01:11:39 UTC | #2

That's really good news ! Microsoft really stepping up their game the last few years.

-------------------------

rku | 2017-01-02 01:11:39 UTC | #3

I am not convinced. Their wrapper is a hack. Especially overriding inherited members. Not sure why they didnt use CppSharp which mono guys develop. It already is used to wrap large and complex libs like Qt. Oh and it produces wrappers that work on linux.

-------------------------

Egorbo | 2017-01-02 01:11:39 UTC | #4

[quote="rku"]I am not convinced. Their wrapper is a hack. Especially overriding inherited members. Not sure why they didnt use CppSharp which mono guys develop. It already is used to wrap large and complex libs like Qt. Oh and it produces wrappers that work on linux.[/quote]
What virtual methods do you need in Urho3d? Urho has a lot of events and they all are surfaced in C#. I don't see any "override" usages in Samples.
PS: Urho was mentioned during Build 2016  :smiley:

-------------------------

rku | 2017-01-02 01:11:40 UTC | #5

[quote="Egorbo"][quote="rku"]I am not convinced. Their wrapper is a hack. Especially overriding inherited members. Not sure why they didnt use CppSharp which mono guys develop. It already is used to wrap large and complex libs like Qt. Oh and it produces wrappers that work on linux.[/quote]
What virtual methods do you need in Urho3d? Urho has a lot of events and they all are surfaced in C#. I don't see any "override" usages in Samples.
PS: Urho was mentioned during Build 2016  :smiley:[/quote]

Component::OnNodeSet() for example. I dont see it firing events. I bet there are more.

Got a video link mentioning urho? Would be interesting to see!

-------------------------

Egorbo | 2017-01-02 01:11:40 UTC | #6

[quote="rku"][quote="Egorbo"][quote="rku"]I am not convinced. Their wrapper is a hack. Especially overriding inherited members. Not sure why they didnt use CppSharp which mono guys develop. It already is used to wrap large and complex libs like Qt. Oh and it produces wrappers that work on linux.[/quote]
What virtual methods do you need in Urho3d? Urho has a lot of events and they all are surfaced in C#. I don't see any "override" usages in Samples.
PS: Urho was mentioned during Build 2016  :smiley:[/quote]

Component::OnNodeSet() for example. I dont see it firing events. I bet there are more.

Got a video link mentioning urho? Would be interesting to see![/quote]

Actually OnNodeSet works in UrhoSharp  :smiley: as well as methods needed for (de)serialization.

-------------------------

rku | 2017-01-02 01:11:41 UTC | #7

Cool i guess, wrapper generator still a hack. Wrapper still not working on linux either.  :unamused:

-------------------------

