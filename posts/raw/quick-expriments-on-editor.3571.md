WangKai | 2017-09-18 02:16:36 UTC | #1

![editor|690x260](upload://lZWOv0lc8pnToBLFJrHEMijknDa.png)

There are many doubts and arguments about Urho's editor. I think everyone can modify the editor and make it suitable for small game development. The only problem to meet that is some time and energy invested. It makes sense for the core dev team to save them for the engine code base. Though lacking of a script debugger it's really a pain in the neck and you will find yourself waving a wood in the stone age :joy:

-------------------------

WangKai | 2017-09-18 02:19:51 UTC | #2

Also color picker needs some more work.

![editor_test_screenshot2|329x500](upload://iWdieWJtWbVdexpydkJ6cQo5tzM.png)

-------------------------

WangKai | 2017-09-19 16:05:20 UTC | #3

Very time consuming without script debugger

![ss|690x239](upload://hnl6VwKqrfiZI0dhtg4UevpuSIx.png)

-------------------------

WangKai | 2017-09-19 16:09:11 UTC | #4

Is there a way to extend C++ object in script? Here I need to extend the widgets and add more function to them. Otherwise I have to hack here and there.

Edit: I found the scripting is very slow to develop to me. It seems that the AngelScript is not efficient enough to work with in real world.

-------------------------

George1 | 2017-09-19 17:10:13 UTC | #5

It would be nice to have a script debugger.

Compile and load/reload and append script code at run time.

-------------------------

WangKai | 2017-09-20 02:44:01 UTC | #6

[quote="George1, post:5, topic:3571, full:true"]
It would be nice to have a script debugger.

Compile and load/reload and append script code at run time.
[/quote]

I tried to implement a debugger for AS by extending Visual Studio Code, but it turns out there is still a lot of work.

-------------------------

