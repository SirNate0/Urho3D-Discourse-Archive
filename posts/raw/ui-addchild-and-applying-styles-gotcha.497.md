LouisCyphre | 2017-01-02 01:00:53 UTC | #1

Hi everybody,

I just wanted to create a simple Messagebox in C++ (similar to the MessageBox.xml)...

First, I created everything, and added every child to its parent after initialization. But unfortunately, I got a Problem with styles... (Could not see the Ok-Text in my OK button)... The only style explicitely set was the "DialogWindow" @ the Window object, everything else was set to SetStyleAuto()

My code was like this:
[quote]
      simpleButton->AddChild(buttonTitle); // Text* added to Button*
      buttonContainer->AddChild(simpleButton); // Button* added to UIElement* 
      window->AddChild(buttonContainer); // UIElement* added to Window*
[/quote]

NO text was visible (the buttonTitle element)... This way around,everything is fine. 

[quote]
  window->AddChild(buttonContainer); // UIElement* added to Window*
  buttonContainer->AddChild(simpleButton); // Button* added to UIElement* 
  simpleButton->AddChild(buttonTitle); // Text* added to Button*
[/quote]

This way around, the text was visible... obviously, calling AddChild too early was "the Problem" (Parent did not know its intended style at that time). Maybe this should be pointed out somewhere for newbies like me :wink: ..  Or maybe I am still doing s.th. wrong.. ???

-------------------------

hdunderscore | 2017-01-02 01:01:08 UTC | #2

I agree that there are some gotcha's in the UI code like this, I personally want to remove them to make it more friendly.

Did you try setting the default style on the UI root element?

-------------------------

cadaver | 2017-01-02 01:01:08 UTC | #3

It might be possible to apply the style (which basically amounts to SetStyleAuto() if no manual style defined) at some point automatically, like when adding a child element to parent, but I'm not 100% sure of it, as setting the UI element style can be destructive (may overwrite some attributes that should be "per-element", like size). 

Another improvement could be to have the default style defined in the UI subsystem, from which even non-parented elements could fetch it, if they don't have a style file defined on their own.

-------------------------

