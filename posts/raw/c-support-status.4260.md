Sehlit | 2018-05-23 15:27:38 UTC | #1

Hello.

I see there are 3 (independent?) C# projects for Urho:

* UrhoSharp by Microsoft/Xamarin
(generator is a hack: https://discourse.urho3d.io/t/its-getting-easier-to-use-urho3d-with-c/1933/7?u=sehlit, and only works on Mac: https://discourse.urho3d.io/t/net-bindings-for-urho3d/4119/12?u=sehlit (C# Microsoft stuff only for Mac ROFL))

* Net Bindings
(no visual studio: git hub. com/rokups/Urho3D/wiki/C%23-support :( )

* C# Script support like the other scripts
(almost no information on this)

Is any of these production ready? It seems to me UrhoSharp is the most mature but support does not seem very good and I don't have Mac or Win10 (WSL) so I'm stuck with the releases.

I'm likely going to use C++ but it would be good to have C# as an option and I just want to know the current status and if anyone have tried them and want to share experiences.

Thank you

-------------------------

Omid | 2018-05-24 06:27:27 UTC | #2

You don't need to have a Mac for using UrhoSharp. !!!!
https://www.nuget.org/packages/UrhoSharp

By the way if you want to compile it by yourself on windows you can clone the repo from github and compile it.
Only generator is working on mac because they using old version of MonoCLang. And you don't need to generate the code because it's already generated and pushed to github.

-------------------------

rku | 2018-05-24 07:50:39 UTC | #3

[quote="Sehlit, post:1, topic:4260"]
Is any of these production ready?
[/quote]
Define "production ready". All of them have missing pieces and dark corners. If you want to use that stuff be prepared to put in some work.

[quote="Omid, post:2, topic:4260"]
Only generator is working on mac because they using old version of MonoCLang. And you don’t need to generate the code because it’s already generated and pushed to github.
[/quote]
Do not fool yourself. UrhoSharp (or any other solution for that matter) is far from complete. If you start working on a non-trivial project using this technology you will definitely run into problems. You will find yourself dealing with unexposed APIs. You also may want to expose your own c++ code to managed runtime. Ability to generate bindings is not optional. It is a necessity.

-------------------------

Omid | 2018-05-24 10:00:35 UTC | #4

Already we had dissolution about it.! What i said and what you reply it's something else.

-------------------------

esakylli | 2018-05-28 16:30:10 UTC | #5

I have used UrhoSharp for 2 years now. For my use-case it has worked very well.
I have only encountered one unexposed API (Bullet Physics specific API that you could call if you had access to the underlying C++ pointer).

-------------------------

rku | 2018-06-01 08:24:09 UTC | #6

What is the size of your project?

-------------------------

esakylli | 2018-06-07 11:42:09 UTC | #7

@rku I'm sitting in Visual Studio for Mac and don't have the fancy code metrics option... but my project is between 7000 and 10000 lines of code (depending on how you count).
I have mainly used 3D graphics, bullet physics and 2D UI in Urho.

-------------------------

