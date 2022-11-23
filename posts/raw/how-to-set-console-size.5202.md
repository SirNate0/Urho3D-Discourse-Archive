Dave82 | 2019-05-30 13:35:26 UTC | #1

It seems that for some reason the console subsytem always runs in fullscreen. How can i set it's height for let's say 200 so it appears on top of the screen like in most games ? It seems that it is possible since the editor limits the height of the console but there's no SetSize() method in Urho3D::Console class...

-------------------------

Leith | 2019-05-30 14:25:42 UTC | #2

I wish my console ran in fullscreen. I want to know how to make it bigger.

-------------------------

Dave82 | 2019-05-30 14:40:06 UTC | #3

How's that pissible ? Which version you use ? I tried the 1.7 Console input demo and tried to create a console in my game and both have fullscreen consoles...

-------------------------

Dave82 | 2019-05-30 18:09:15 UTC | #4

It seems the magic is happening in void Console::UpdateElements()
where the elements get their final size. The  rowContainer_->SetFixedHeight(); uses some overcomplicated calculations to get the final height. For anyone who want to change the height of the console just use a constant height value and that's it. 
 rowContainer_->SetFixedHeight(someHeight);

-------------------------

Leith | 2019-05-31 04:16:40 UTC | #5

I thought you meant the system console :P

-------------------------

