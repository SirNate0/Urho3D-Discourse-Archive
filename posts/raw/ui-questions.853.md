TikariSakari | 2017-01-02 01:03:31 UTC | #1

Hello, I have tried using the examples on urho on my android phone. It uses 1080p resolution. Now the problem is that the samples have relatively small buttons when trying the samples on my phone, meaning they are almost practically unpressable. So I was trying to modify the 02 sample to use some sort of screenheight/value to make the components act as normalized size.

I ran into a problem with line edits. I just couldn't figure out how you could change font size for line-edit on the fly. How can I change the line-edits font after declaring the ui-components?

Another question is: If I pass -s to the engine, it can become resizable, and I feel like that is basically how I would really want my application to work. I was wondering if there is a way to pass this resizable parameter to engine codewise without having to modify the engine.cpp or launching the exe-file with -s parameter? Like if I could just pass a parameter from the sample that is inheritated from application to lets say for example make resizable etc? I guess open source is good for being able to modify, but maybe there is a way already in there, which I just happened to miss.

Edit: Found my answer, when I was looking how to disable the mouse lock into the screen (which I haven't yet found an answer), but from urhoplayer, if I inherit the Setup-function from sample, I can overwrite the engineParameters_["WindowResizable"] -variable to true.
Edit2: GetSubsystem<Input>()->SetMouseVisible(true); seems to do the trick to not lock the mouse cursor onto the screen.

Third thing: 
I noticed that the sample 10 has some issues with the view on my android. I think this is same as spamming decals on top of each other, they might start to compete against each other which one to draw on top.

Picture of sample10 on my android phone:
[url]http://i.imgur.com/WBDOyOX.png[/url]
Those lines change direction/width depending from where I am watching the screen.

-------------------------

setzer22 | 2017-01-02 01:03:34 UTC | #2

For the line edit thing, have you tried using GetTextElement? 

The Text class can have its font set to it. I haven't tried this but I think it should work.

Documentation for GetTextElement: [url]http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_line_edit.html#a94333c8740270937ebad32721c463bb5[/url]

-------------------------

TikariSakari | 2017-01-02 01:03:35 UTC | #3

Ty, dang I completely missed it. I was just using the getText, but somehow was too blind to notice there was such method. It seems I was able to change font size with this, so thank you.

-------------------------

