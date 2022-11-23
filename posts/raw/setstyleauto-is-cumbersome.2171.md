rku | 2017-01-02 01:13:39 UTC | #1

So i use one style for ui elements. Having to call SetStyleAuto() after creating every UI element is really cumbersome. Is there a particular reason why this is not done automatically? I inserted call to it in UIElement::InsertChild() and i no longer have to call it manually all the time. Everything seems to work, though im not sure if i did not break anything by accident. So any chance we could make calling SetStyleAuto() optional or we really can not?

-------------------------

cadaver | 2017-01-02 01:13:39 UTC | #2

It's annoying, but the UI style implementation in Urho is destructive, meaning there is not a clear separation of UI style attributes and instance attributes. So if the typename indicated style is applied first no matter what, but user would want to change a custom style immediately after, the result can be different than expected. When I tested this in the editor, it went wrong, but surprisingly little: the editor's menu bar had imagery that shouldn't be there. Other elements appeared to work.

For now I recommend making a helper function that adds or creates a child and calls SetStyleAuto().

-------------------------

weitjong | 2017-01-02 01:13:39 UTC | #3

IMHO, it would only appear that way if you don't have alternative styles defined. If you do then you are more likely to use the SetStyle() method instead and passing in the actual style you want to use.

-------------------------

rku | 2017-01-02 01:13:39 UTC | #4

[quote="weitjong"]IMHO, it would only appear that way if you don't have alternative styles defined. If you do then you are more likely to use the SetStyle() method instead and passing in the actual style you want to use.[/quote]

It depends on usecase i guess. In my case i have one main style and only very rarely if ever i want to override that. That is why it would be quite nice to have elements styled by default while still being able to override that default style.

[quote="cadaver"]It's annoying, but the UI style implementation in Urho is destructive, meaning there is not a clear separation of UI style attributes and instance attributes. So if the typename indicated style is applied first no matter what, but user would want to change a custom style immediately after, the result can be different than expected. When I tested this in the editor, it went wrong, but surprisingly little: the editor's menu bar had imagery that shouldn't be there. Other elements appeared to work.

For now I recommend making a helper function that adds or creates a child and calls SetStyleAuto().[/quote]
I see, sounds like improving on this aspect would be quite some work. There certainly are better things to spend time on. Oh well :wink:

-------------------------

Ray_Koopa | 2017-01-02 01:13:41 UTC | #5

It took me 2 hours to figure out how to get my custom style to work, and I was just missing this SetStyleAuto() call. I couldn't find a good overview about UI Styles, did I miss something? =)

-------------------------

cadaver | 2017-01-02 01:13:42 UTC | #6

Welcome to the forums. The UI documentation page indeed lacks a separate section on UI style, it's touched upon in the section dealing with XML layout files. The samples (for example HelloGUI) demostrate applying a style, though.

-------------------------

Ray_Koopa | 2017-01-02 01:13:42 UTC | #7

Thanks! I used that one as a base, though it wasn't clear what that method is for at first. But I guess it's just something I need to know, no problem.
I guess you mean the [urho3d.github.io/documentation/1.5/_u_i.html](https://urho3d.github.io/documentation/1.5/_u_i.html) page?

-------------------------

cadaver | 2017-01-02 01:13:42 UTC | #8

Yes. Note the version selector in the top right corner; for the latest stable version you should choose 1.6. Also, if you choose HEAD (tracks the current master branch) you'll see a new section on programmatic UI creation which mentions the need to use SetStyle() / SetStyleAuto().

-------------------------

Ray_Koopa | 2017-01-02 01:13:42 UTC | #9

That's fantastic. Thanks! I'm using the Xamarin C# port, but the code is almost the same, so this is really helpful.
I'll probably write some tutorials for the C# port later on when I'm sure about my knowledge.

-------------------------

rku | 2017-01-02 01:13:59 UTC | #10

Was there any thought on using external UI library instead? After all it seems like what Urho3D does with every other aspect of engine but UI. I am pretty sure we could benefit from UI component that is constantly maintained and improved. UI library in itself is not a trivial project so having that off the shoulders of maintainers could only be a good thing right?

-------------------------

cadaver | 2017-01-02 01:13:59 UTC | #11

Sure there has been discussion on and off, but it appears there's no single "winner" solution as for example Bullet is for 3D open source physics.

For Urho itself the list of requirements for a replacement UI library is steep (including feasibility of scripting integration), and it has been discussed on these forums before. An individual user replacing the UI in their Urho application could naturally set the bar of requirements differently.

UI libraries (the kind of lightweight, engine-suitable ones, not talking of heavy institutions like Qt) also have a danger of dying off once the author's initial personal requirements have been satisfied, unless the library gathers a significant "critical mass".

-------------------------

