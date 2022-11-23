sirop | 2018-08-08 11:26:20 UTC | #1

Hello.

I have 3 widgets in my application which always yield smth. like
```
WARNING: Forcing top alignment because parent element has vertical layout
```
or 
```
WARNING: Forcing left alignment because parent element has horizontal layout
```

What shall I do to get rid of these warnings? 

Or is there a general way to just suppress this debug level/ warnings ?

Thanks.

-------------------------

sirop | 2018-08-08 12:20:20 UTC | #2

Setting   `engineParameters_[EP_LOG_LEVEL] = 0; `   let me get rid of warnings, however DEBUG level log messages are still there.

How can that be?

-------------------------

Miegamicis | 2018-08-08 12:35:18 UTC | #3

Log level 0 means that all the messages that comes in should be outputted to console.
There are multiple log levels
0 - output everything
1 - output debug messages and everything > 1
2 - output info messages and everything > 2
3 - output warning messages and everything > 3
4 - output error message and everything > 4
5 - output nothing

See source here: https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/IO/Log.h#L33-L46

-------------------------

Miegamicis | 2018-08-08 12:34:10 UTC | #4

Do you have sample code where you create parent with vertical/horizontal layout and add a child to it?

-------------------------

sirop | 2018-08-08 12:40:31 UTC | #5

yes, I have some: https://pastebin.com/zJzCFMS0

-------------------------

Miegamicis | 2018-08-08 13:02:01 UTC | #6

[quote="sirop, post:1, topic:4442"]
Forcing top alignment because parent element has vertical layout
[/quote]

This warning message is generated when you create a parent with vertical layout mode and add child to it, and after that try to change it's vertical layout to something other than `VA_TOP`
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/UI/UIElement.cpp#L713

Same thing with horizontal layout, only `HA_LEFT` alignment is allowed for added child elements.

-------------------------

