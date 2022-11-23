Lichi | 2017-01-02 01:01:44 UTC | #1

Hi, i'm making the menu of my project, the idea is that when i press the button, the scene is loaded and then i can play. But, when i press the button the scene loads but i cant play, the character wont move.
If i remove the button the game works perfectly.
Here's my button code:
[pastebin.com/8MkN6ZtM](http://pastebin.com/8MkN6ZtM)
Someone helps me?
Thanks.

-------------------------

GGibson | 2017-01-02 01:01:45 UTC | #2

Hi lichi,

If you haven't looked at the angelscript source for the example demos then try that. Usually in the examples there is a function called SubscribeToEvents() wherein the 'update' event is given a handler, within which the camera and/or character responds to input. I don't see such a function being called in your code so maybe that is it? Again, I suggest really looking through the demo code to see why the demo code works and how it's working.

-------------------------

Lichi | 2017-01-02 01:01:45 UTC | #3

[quote="GGibson"]Hi lichi,

If you haven't looked at the angelscript source for the example demos then try that. Usually in the examples there is a function called SubscribeToEvents() wherein the 'update' event is given a handler, within which the camera and/or character responds to input. I don't see such a function being called in your code so maybe that is it? Again, I suggest really looking through the demo code to see why the demo code works and how it's working.[/quote]

Thanks for reply :slight_smile:
I looked at the angelscrit samples, the code that i use is a copy from the gui sample :/
The function SubscribeToEvents() is called in other part of the code.

In the examples dont't appear who remove a button, that may be what i'm doing wrong.

-------------------------

