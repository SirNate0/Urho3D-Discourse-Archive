Ray_Koopa | 2017-01-02 01:13:43 UTC | #1

I'm a little puzzled understanding how to export a UI layout from the editor.

I have a simple hierarchy just to test some things, like this:
[ul][li]UI (Root)
[list][*]TestText (Text at top center)[/li]
[li]CloseButton (Button at top right)[/li]
[li]HelloText (Text at bottom center)[/li][/ul][/*:m][/list:u]

Now I want to export all these 3 UI elements into an XML file to load it in my game. But when I choose the root UI node, clicking on "UI-layout > Save UI-Layout (as...)" does nothing. I can only export single items which are children of the root.

Is this expected behavior? Do I always need to define a custom container stretching over the whole root which I then export and put children in?

-------------------------

cadaver | 2017-01-02 01:13:43 UTC | #2

Yes, it's expected. When loading a layout, we don't allow to load into / overwrite the actual UI root (it will contain the cursor element, if done in software), on the other hand legal XML must have a single root element.

I recommend thinking of the UI in modular terms, for example if game has a bottom HUD, it could be its own container.

-------------------------

Ray_Koopa | 2017-01-02 01:13:43 UTC | #3

I see, yeah that makes sense. Just for some tests it wasn't obvious at first, where I just place these typical "Hello World" labels  :slight_smile:

-------------------------

