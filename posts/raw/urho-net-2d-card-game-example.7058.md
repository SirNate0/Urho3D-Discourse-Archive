bayganik | 2021-11-19 17:02:47 UTC | #1

I've created a 2D solitaire game using Urho.Net.  This is in C# using a "kind of " ECS framework.  You'll find it here (https://github.com/bayganik/Urho.Net_CardGame_Example)

![image|668x499](upload://rIXtJRzFg6ttIPWgCUlHJf8dICq.png)

-------------------------

vmost | 2021-11-19 17:12:52 UTC | #2

Visual hack: replace red text with orange text, much easier to see on a dark background :).

-------------------------

elix22 | 2021-11-19 19:38:20 UTC | #3

Small comment you will have to rename the root folder

> **Urho.Net_CardGame_Example** to **CardGameExample** 
Otherwise it will fail compilation (at least for me)

-------------------------

bayganik | 2021-11-19 23:13:08 UTC | #4

Thank you so much for the comments :slight_smile:

-------------------------

bayganik | 2021-11-23 17:24:06 UTC | #5

elix22 are you referring to URHONET_HOME_ROOT ?  if so, how do I change that?  I see if being referenced during compilation.

-------------------------

elix22 | 2021-11-23 20:45:19 UTC | #6


[quote="bayganik, post:5, topic:7058"]
are you referring to URHONET_HOME_ROOT ?
[/quote]

No , I am referring to the repo name **Urho.Net_CardGame_Example**

When you git clone the repo the root folder is **Urho.Net_CardGame_Example** but it should be **CardGameExample**

So the folder structure would be **CardGameExample/CardGameExample.csproj**

When you created the project it was **CardGameExample/CardGameExample.csproj**
I guess you changed it prior of uploading your project to github

-------------------------

