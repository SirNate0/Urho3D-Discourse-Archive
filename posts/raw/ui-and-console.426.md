zakk | 2017-01-02 01:00:19 UTC | #1

Hello,

This time, it's about UI. And console. As the two subjects are nested, i make one post.
(ohh noooo, another post long like a month of sundays!)

Here is my code for a basic console display, with Lua and Urho3DPlayer:


[code]

require "scripts/common/keys"

function console_traitement()
  print("traitement")
end


function console_create()
  local style="UI/DefaultStyle.xml"
  local uiStyle = cache:GetResource("XMLFile", style)
  engine:CreateConsole()
  console.background.opacity = 0.8
  console.defaultStyle = uiStyle
  console:SetVisible(true)

end

Start = function()
  SubscribeToEvent("KeyDown", "handle_keys") --for handling ESCaping
  console_create()
end

[/code]

Now, i've some questions.

[b]About UI itself[/b]
Defining an UI seems rather complex.
For getting the console window to display, i need to include:

 - UI/DefaultStyle.xml [i]define the window displayed, i guess.[/i]
 - Fonts/Anonymous Pro.ttf [i]included by DefaultStyle.xml.[/i]
 - Textures/UI.png [i]included by DefaultStyle.xml.[/i]
 - Textures/UI.xml [i]i put it in the path, perhaps optional[/i]

And the shaders.
 - Shaders/GLSL : Basic.glsl [i]console won't work without this one.[/i]
 ([i]Basic.glsl[/i] needs [i]Samplers.glsl, Transform.glsl, Uniforms.glsl[/i])

1) I didn't find which part of [i]UI/DefaultStyle.xml[/i] ask for [i]Basic.glsl[/i]. Is the glsl file always needed, whatever Urho display subsystem we will use ?

2) I guess that UI parts won't be defined with a text editor. So I've launched Urho Editor, and try to load .xml files from UI directory.
I can see on screen some of them (for example, [i]UI/MessageBox.xml[/i] , i can open it with with ?open UI layout? submenu). But i cannot ?open UI layout? the file [i]UI/DefaultStyle.xml[/i] (i can only ?open? it, does it means it has no ?viewable? format ? Only definitions of elements, may be ?).


[b]About the console[/b]
Excepting for displaying errors messages and output on stdout, what is the interest of [i]console[/i] ?

I thought i could use my own functions for dealing with console keyboard input.
I mean, it would be nice to define a function in the script as a callback of console. For debugging, changing variables on the fly, choosing a level...

It seems that we can only choose our shell interpreter. And even this, i couldn't do:

I tried to change at least interpreter:
  console:SetCommandInterpreter("/usr/bin/zsh")
If i type in console [i]echo $SHELL[/i], i still get [i]/bin/bash[/i]


Another last question, just for the sake of curiosity:

  print(console.commandInterpreter) -- returns: ?FileSystem?
  print(console:GetCommandInterpreter()) -- returns: ?FileSystem?

What does ?FileSystem? means ? Ok i know what a FS is, but here ?



Thank you for reading all this.

-------------------------

friesencr | 2017-01-02 01:00:20 UTC | #2

UI:

Defining the ui is somewhat verbose.  However the alternative is to hide things from the user which has negative side effects too.  Someone could build an api on top of the ui system.  I myself have considered emulating an immediate mode ui.

1) Much of what people want out an engine is a certain amount of boilerplate.  It is arguably better to reduced code complexity then lots of configuration.  That is arguable.  The dependency on Basic.glsl can actually beneficial in that it shows you how to wire things up and replace it.  around line 700 in the ui.cpp is the code to change the shader.

2) If you are going to write uis by hand the api is probably a better route.  You can write xml properties by hand but it requires knowing the attribute names, the type, and how it serializes.  About DefaultStyle.xml, there is no style editor which is unfortunate.  I wrote the right click menus I assume you are talking about and the integrations.  They are not comprehensive of what the editor can do.  They were about as much as I could figure out without implementing submenus or having data dependencies.  There are probably some easy ones that are missing.

Console:

The interpreter is not the shell.  It is either Filesystem which will execute system commands, Script which is AngelScript, and LuaScript which are lua commands.  The console does send an event ConsoleCommand.  Subscribing to that will give you what you are looking for.

-------------------------

weitjong | 2017-01-02 01:00:20 UTC | #3

[b]About the UI[/b]

I don't think it is fair to list out what are necessary in that way. Those that you have listed (with the exception of Basic.glsl shader) are just relevant to the UI "skin". Although it is not being stated as one of the feature but Urho3D UI subsystem is fully skinnable. The "DefaultStyle.xml" is but just one of the default skin or style. There is in fact another old skin "OldStyle.xml" in the UI subdirectory. You can create your own skin that matches your game's theme, use your own font, use your own UI.png texture file, etc. So, those that you have listed would probably be customized for your own project anyway. You should, however, always create a file similar to UI.xml in the same location of where you put UI.png resource file. For more detail see: [urho3d.github.io/documentation/H ... s_Textures](http://urho3d.github.io/documentation/HEAD/_materials.html#Materials_Textures).

Currently our rudimentary UI layout editor can only load and edit the UI layout file. It does not load and edit the UI skin/style file as already pointed out. However, it does support applying the UI styles. By default the Editor will load the "DefaultStyle.xml" skin, but if you do have your own style file then you can set the Editor to use it by choosing Editor's UI-layout | Set default style... menu item. In the Editor's attribute inspector window, you can inspect what is the current style an UI-element has and change it too. The styles available in the drop down list is data driven based on the number of actual styles available in your skin/style file. Like it or not, the current default style is more geared toward the need of Editor itself. The point is, your game doesn't even have to use the default. You don't even have to limit yourself to have only one UI style file in your game.

[b]About the console[/b]

IMHO, the console tries to mimics terminal console which has the standard input, standard output, and standard error streams. I think you have already figured out the output/error part, it just displays them without caring from where those output/error come from. Similarly for the input part, the console is just responsible to accept an input "command string", it does not itself know what to do with the command string so it just simply dispatches the command string to any classes that subscribed to the console command event. So far we have three subsystem classes that are able to handle this event: filesystem, (Angel)Script, and LuaScript. The filesystem redirects the command string to SystemCommand() call (in Linux platform, this will most likely end up in bash shell trying to interpret it). The Script and LuaScript, on the other hand, will try to "execute" the command string. What important to note here is that the command execution is done using the same AngelScript context and Lua context, respectively, that your application is currently using. In other words, you can use it as your original intuition like modifying the variable values on the fly, changing the game state, or what have you, without even have to writing any callback. If you don't use any scripting, however, then you will probably have to create a new class that handles the E_CONSOLECOMMAND event and makes it interpret the command string anyway you like it.

-------------------------

zakk | 2017-01-02 01:00:22 UTC | #4

Hello,

First, thanks for your replies.

I must clarify something: as i'm not an english native speaker, some of my posts could be misinterpreted.

I'm not criticizing Urho3D when i'm doing a list of what is needed for seeing on screen an UI. It's just what i did with trials/errors for displaying the console: i included a lot of files which seemed required, and removed them one by one, just keeping the absoluted needed ones.

For the moment, i still have troubles with the understanding of the workflow of Urho3D. But i think the effort worth it.
Now, i understand what is the purpose of [i]Basic.glsl[/i], for example. Two days ago, it was someting cloudy for me. Ok, it's needed by UrhoPlayer for the display, as it's using modern OpenGL shaders. That's nice to have something so user-adjustable, and not buried deep into some obscure C++ class. But i had to understand it before admire it :wink:

With your explainations, i did succeed with having a working Lua console (_very_ handy for developping Lua script for Urho!). And i've climbed a step in the global comprehension of the API.

I've troubles with the documentation. Maybe it's me, but i've the feeling that for understanding Urho3D, you have to fully understand Urho3D. I explain: i mean, you must read and understand the whole (and a bit sparse) documentation available. That's why i try to make very precise posts when i ask a question, with the hope that it will be useful for someone next. It's not for criticizing, but just for setting a precise case, which puzzled me at a time.

That said, i'd be curious to know where is the documentation of the methods availables in an event callback. I mean:

[code]

function HandleConsoleCommand(eventType, eventData)
    if eventData:GetString("Id") == "LuaScript" then
        eventData:GetString("Command")
    end
end

[/code]

Ok, we handle the console commands with two users values.
[b]eventType[/b] : i don't know what is it, the type for sure. But why testing the type with ?eventData:GetSrting("Id")?, then ?
[b]eventData[/b] : seems to contains a lot of things, even the type.

I use a [i]GetString("Command")[/i] for executing arbitrary Lua code typed in the console (dangerous, i know, but it's for debugging only). I found the ?Command? paramater when reading the samples provided with Urho. Where can i find the complete list of methods and associated parameters of [i]eventData[/i] userdata ?
I've searched the documentation, even the console cpp sources, but found nothing.

What is the purpose of [i]eventType[/i] ? I've grepped (grep -i eventtype *.lua) the whole Lua sample directory, but it's not used.

Thank you for reading this, and for helping me to understand Urho3D, which is by far the best OpenSource game engine i've tested so far :wink:

-------------------------

Mike | 2017-01-02 01:00:22 UTC | #5

Events are documented at [url]http://urho3d.github.io/documentation/HEAD/_event_list.html[/url].
For example, ConsoleCommand is the type of event you are listening to, and its available data is 'Command' and 'Id'.

-------------------------

weitjong | 2017-01-02 01:00:22 UTC | #6

[quote="zakk"]I must clarify something: as i'm not an english native speaker, some of my posts could be misinterpreted.

I'm not criticizing Urho3D when i'm doing a list of what is needed for seeing on screen an UI. It's just what i did with trials/errors for displaying the console: i included a lot of files which seemed required, and removed them one by one, just keeping the absoluted needed ones.[/quote]

In case you have not noticed, I am also not a native English speaker. Chinese and Indonesian are my primary and secondary languages, English is the third. When I first read your post I did not perceive it as you attacking (criticizing) Urho3D, so it is not my original intention if you some how perceive my reply as me trying to defending Urho3D. So, sorry for my bad English too :slight_smile:.

Now with that settled, let's go back to the topic. About the documentation, I could not agree more with you that it is rather sparse and hard to understand in some of the sections. Having said that, it actually amazes me that Lasse (the main author of Urho3D) has the time to single-handedly author almost all of those documentation pages. Furthermore, his code is not just clean but also well commented throughout. It is easy to forget that the source code itself is the best documentation to understand Urho3D. Good luck with that with other game engines, especially those closed ones.

About the event handling, you may want to read this section [urho3d.github.io/documentation/H ... _list.html](http://urho3d.github.io/documentation/HEAD/_event_list.html) to know what event data are available for each event type before attempting to access them in the VariantMap. Again, I agree the documentation is rather sparse on this area. Using your example, it is hard to understand what is the purpose of id string and command string of the console command event without actually peeking at the C++ code. The purpose of the id string is to prevent the command string from being interpreted multiple times by classes that handle console command event. The Console's UI has a drop down list (when it detects there are more than one handler available the app) to let user choose which class is supposed to interpret the command and pass the chosen class id as one of the event data. So, I hope it is clearer to you now why the event handler has to first check the id to see whether the command string is meant for its consumption before actually attempting to consume it.

-------------------------

