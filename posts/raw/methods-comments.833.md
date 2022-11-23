lexx | 2017-01-02 01:03:18 UTC | #1

Im wondering why I cant see methods' comments when I hover mouse over them?
I see them when I press ctrl+space but not with mouse. I have tried VS2010 express and VS2013 community edition.
Some option which isnt setted by cmake? I can see comments on other engines I have used.

-------------------------

OvermindDL1 | 2017-01-02 01:03:18 UTC | #2

[quote="lexx"]Im wondering why I cant see methods' comments when I hover mouse over them?
I see them when I press ctrl+space but not with mouse. I have tried VS2010 express and VS2013 community edition.
Some option which isnt setted by cmake? I can see comments on other engines I have used.[/quote]
If you are talking about the doxygen comments, unsure about VS but in KDevelop it works fine:
[spoiler][img]http://overminddl1.com/overassault/screenshots/KDevelop_Intellisense_Showing_Comment.png[/img][/spoiler]
Do you have to rebuild the VS intellisense database or did they finally fix having to do that yet (had to do it all the time on older VS's or intellisense would just occasionally stop showing some types of data...).

-------------------------

lexx | 2017-01-02 01:03:19 UTC | #3

Yeah, doxygen comments. I did Project->Rescan solution, didnt help. Seems it does it automatically, if I delete *.sdf files.  I have Urho3D.sdf which is 124MB, it is some intellisense information file.

-------------------------

hdunderscore | 2017-01-02 01:03:19 UTC | #4

After a quick look I see that vanilla-VS doesn't seem to like doxygen-style comments too much, which is what Urho uses. There's also an option to use xml formatting in comments for VS. More: [msdn.microsoft.com/en-us/library/s0we08bk.aspx](https://msdn.microsoft.com/en-us/library/s0we08bk.aspx)

Simple solution you find-replace /// with // in the header files.

VS 2013 Community let's you install extensions, so you could try to find an extension that works for you.

-------------------------

GoogleBot42 | 2017-01-02 01:03:19 UTC | #5

If you still can't get it working maybe you could try qt creator.  qt creator is available for windows and offers code completion as well.

-------------------------

lexx | 2017-01-02 01:03:23 UTC | #6

I tried qt, and tried extensions, no success. Maybe if I use // instead of /// helps but havent replaced text yet, I have something else to do.

-------------------------

hdunderscore | 2017-01-02 01:03:25 UTC | #7

Well I know of at least one extension that works, although it's not free (it has a trial) -- it's called Visual Assist. I use it myself as it improves a few things in VS2013 (such as auto-completion).

-------------------------

thebluefish | 2017-01-02 01:03:40 UTC | #8

[quote="hd_"]Well I know of at least one extension that works, although it's not free (it has a trial) -- it's called Visual Assist. I use it myself as it improves a few things in VS2013 (such as auto-completion).[/quote]

$99 isn't bad. I'll have to check this out, thanks!

-------------------------

