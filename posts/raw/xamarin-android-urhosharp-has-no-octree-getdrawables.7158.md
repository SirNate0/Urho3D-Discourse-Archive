tianlv777 | 2022-01-27 15:03:52 UTC | #1

xamarin android urhosharp has no octree.getdrawables
how to solve

-------------------------

Eugene | 2022-01-27 15:09:30 UTC | #2

I say you poke @elix22, they are the closest thing to UrhoSharp "maintainer" out there.

-------------------------

tianlv777 | 2022-01-27 15:12:19 UTC | #3

please help me,I don't know how to poke elix22

-------------------------

George1 | 2022-01-28 00:23:01 UTC | #4

Here is the .net version.

https://discourse.urho3d.io/t/urho-net-c-cross-platform-game-development-framework/6674

https://github.com/Urho-Net

-------------------------

tianlv777 | 2022-01-30 05:02:20 UTC | #5

I saw the Urho.Net，And try use.But Urho.Net scene.GetComponent<Octree>().getdrawables is alos not finded.
So what is right way.I could using octree.getdrawables function.

-------------------------

tianlv777 | 2022-01-30 05:10:58 UTC | #6

![Y237$H0RIRN0E3EUAWS41F4|626x500](upload://dhuxN4a4T6oItUDr8owjzjd92Xq.png)

-------------------------

elix22 | 2022-01-30 07:53:38 UTC | #7

Create an issue on Github .
I am not promising anything , I will see what I can do.

Please note  that on mobile devices (unlike UrhoSharp) Urho.Net  is not linked to 
Xamarin Android/iOS  , it's running directly on top of Mono runtime.

-------------------------

tianlv777 | 2022-01-30 10:55:19 UTC | #8

0 0,I mean if there are no has other easy way to do octreee.getdrawables.It means we can not get Nodes within a rectangle by octree of urho3d.So I want add my logic to do this function.Just like War3 Game,I just want to get units by rectangle.

-------------------------

tianlv777 | 2022-02-02 05:42:31 UTC | #9

Now I could use Urho.Net to run  "android-deploy-debug".But I can't debug with breakpoint.I use Win10.And .net core debug is ok,I could use breakpoint.But in "android-deploy-debug" ,breakpoint is invalid.Just Samples.

-------------------------

tianlv777 | 2022-02-02 05:47:34 UTC | #10

![无标题|690x388](upload://6ClAE49zNCOgdV6CIL02OY76wWL.png)

-------------------------

elix22 | 2022-02-02 07:17:04 UTC | #11

Currently Debugger is available only on Desktop (Windows , Linux, MacOS)
You can use Logs , it's working on all platforms .
```
using Urho.IO;

Log.LogLevel = LogLevel.Info;

Log.Info("Some test log with a number " + 10.ToString() + " and a nother number" + 456.ToString());
```

-------------------------

