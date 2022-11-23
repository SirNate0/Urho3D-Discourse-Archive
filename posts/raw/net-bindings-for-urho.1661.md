migueldeicaza | 2017-01-02 01:09:20 UTC | #1

Hello,

We recently did some bindings for .NET for Urho and they support C# and F#.   

Since this is my first post on the forum, I was Our bindings to Urho are available here:

[github.com/xamarin/urho](http://github.com/xamarin/urho)

And we have ported the Urho samples to C# as well to test the binding, and added a few of our own:

[github.com/xamarin/urho-samples](https://github.com/xamarin/urho-samples)

In the .NET world it is common to publish the code in the form of a NuGet package, it ships with binaries for Windows, Mac, Android, iOS and tvOS and we have nade it available here:

[nuget.org/packages/UrhoSharp/](https://www.nuget.org/packages/UrhoSharp/)

We also wrote some introductory documents for people in the .NET world to Urho:

[developer.xamarin.com/guides/cro ... roduction/](http://developer.xamarin.com/guides/cross-platform/urho/introduction/)

We published some C# API documentation based on Urho's documentation and our own writing and it is available here:

[developer.xamarin.com/api/root/Urho/](http://developer.xamarin.com/api/root/Urho/)

Our community is usually on the Xamarin forums, so we opened a dedicated forum here:

[forums.xamarin.com/categories/urhosharp](https://forums.xamarin.com/categories/urhosharp)

Happy new year!
Miguel.

-------------------------

1vanK | 2017-01-02 01:09:20 UTC | #2

Nice to see such a famous person on the our forum :)

-------------------------

Bluemoon | 2017-01-02 01:09:21 UTC | #3

This is a wonderful development and a great news... Urho3D is now accessible to a host of .NET developers

-------------------------

sabotage3d | 2017-01-02 01:09:21 UTC | #4

It is really nice with cool additional features. I am trying to backport the actions to Urho3D C++ do I have to obey any license restrictions?

-------------------------

boberfly | 2017-01-02 01:09:22 UTC | #5

Hi Miguel,

It's great to see .Net support for Urho3D, thank you for the contribution.

I'll have to experiment with Python.NET inside of Maya to see if I can access Urho from there, this could be great for tools development!

Kind regards

-------------------------

migueldeicaza | 2017-01-02 01:09:23 UTC | #6

[quote="sabotage3d"]It is really nice with cool additional features. I am trying to backport the actions to Urho3D C++ do I have to obey any license restrictions?[/quote]

The code is MIT, so you can just copy/paste/translate the code, you only need to keep the credit about the original code (Xamarin Inc)

-------------------------

rku | 2017-01-02 01:09:37 UTC | #7

No linux support?

-------------------------

HeadClot | 2017-01-02 01:10:57 UTC | #8

[quote="rku"]No linux support?[/quote]

There is linux support for Xamerian Studio if you are developing on linux.

Just do not expect to be able to deploy to Linux.

Details in this report. [url=https://bugzilla.xamarin.com/show_bug.cgi?id=142#c40]Link[/url]

-------------------------

Jacob_Christ | 2017-01-02 01:12:10 UTC | #9

I made a really bare bone WinForms project for VS2015 for Urhosharp here:

[github.com/JacobChrist/UrhosharpWinFormTest](https://github.com/JacobChrist/UrhosharpWinFormTest)

Jacob

-------------------------

namic | 2017-01-02 01:12:10 UTC | #10

This is much more useful now that Xamarin is open-source. :slight_smile:

-------------------------

migueldeicaza | 2017-01-02 01:12:33 UTC | #11

Hello,

We have released an update to UrhoSharp, it tracks Urho up to the version from May 21st, with this hash:

591171202a5c5829a3338c9643ce4b98747a0590

The release notes are here:

[forums.xamarin.com/discussion/67 ... sed#latest](http://forums.xamarin.com/discussion/67610/urhosharp-1-0-557-released#latest)

Someone had asked previously about support for Urho on UWP, it now also works there.

-------------------------

DavTom | 2017-01-02 01:12:46 UTC | #12

For users here interested to use .NET c# Urho3d for e.g. windows 10 mobile (UWP through D3D11), do share your interest in this thread so we could see that happens soon. Great job for bring .NET to urho3D
[github.com/xamarin/urho/issues/119](https://github.com/xamarin/urho/issues/119)

-------------------------

