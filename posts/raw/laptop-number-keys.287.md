Bluemoon | 2017-01-02 00:59:24 UTC | #1

I seem to have a slight issue with number keys on laptop. I have a test app that I'm developing and I would like to handle number key presses using KEY_NUMPADX (X = 0-9) but when I press the number keys on the laptop they are not recognized. Something like the following code when testing for the "1" key pressed on a laptop in the app's Key down handler

[code]
   int key = eventData[P_KEY].GetInt();
   if(key == Urho3D::KEY_NUMPAD1)
    {
        //Do something
    }
[/code]

Even though "1" is pressed, the if(...) statement evaluates to false.
I will like to know what exactly I'm doing wrong and how to correct it

--------------------------------

My bad!!! I was doing it the wrong way, it should have been something like this
[code]
  if(key == '1')
  {
     //Do something
  }
[/code]

Problem Solved

-------------------------

