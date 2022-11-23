McC1oud | 2019-11-09 07:13:57 UTC | #1

Hello, I have an application I'm building in Xamarin and was looking to try out this engine to build a game with it. I've run into a bit of an issue with my xaml page from following a few examples:

https://xamarinhelp.com/introduction-urhosharp-xamarin-forms/

It explains to implement the following in my page code:

```
<?xml version="1.0" encoding="utf-8" ?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:local="clr-namespace:UrhoSharp.Demo"
             xmlns:urho="clr-namespace:Urho.Forms;assembly=Urho.Forms"
             x:Class="UrhoSharp.Demo.MainPage">

    <urho:UrhoSurface x:Name="HelloWorldUrhoSurface" VerticalOptions="FillAndExpand" />

</ContentPage>
```

My implementation edits are just changing:

```
         xmlns:local="clr-namespace:ZorduGamma"
```

I'm running into an issue on:

```
xmlns:urho="clr-namespace:Urho.Forms;assembly=Urho.Forms"
```

Which is telling me that that Assembly Urho.Forms was not found.
My C# scripts aren't complaining about implementing:
using Urho;
using Urho.Forms;

I've installed UrhoSharp.Forms v1.9.67

-------------------------

Modanung | 2019-11-09 12:06:18 UTC | #2

First of all welcome to the **Urho3D** forums.

Xamarin [abandoned](https://forums.xamarin.com/discussion/141631/urhosharp-is-dead-should-we-fork-it) the UrhoSharp project some time ago which existed separately from Urho3D as a fork.  Please switch to Urho *proper* if you'd like to receive support here or try the [Xamarin forums](https://forums.xamarin.com/categories/xamarin-forms).

-------------------------

McC1oud | 2019-11-09 12:42:04 UTC | #3

Heh, I was sent to Urhosharp by a Xamarin Dev... well that's a pain in the butt.

-------------------------

throwawayerino | 2019-11-09 12:56:45 UTC | #4

Turning people away isn't polite, and it is true that UrhoSharp was abandoned
However your problem doesn't seem to be related to the library. Check your project settings and make sure you included the assembly in the dependencies

-------------------------

