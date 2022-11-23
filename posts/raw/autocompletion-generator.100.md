silverkorn | 2017-01-02 00:57:59 UTC | #1

Hi,

Inspired by the "ToDoxHook.lua" file, I've prepared generator for an auto-completion list of Lua functions/properties for the MIT licensed Zerobrane IDE and maybe eventually other IDEs.

Before sending/committing to you, I had few question about the logic and possibilities:

[ul][li]Should I exclude the 1st level of auto-completion for classes available in the Global Properties? (ex.: "audio" only would be available in the list and "Audio" would not be visible but will be used as reference for this class auto-completion)[/li]
[li]Does the Lua function reflect new object creations via Object:new() or only Object() directly?[/li]
[li]Along with the constructors, is there destruction functions in Lua? (does ~Object() is possible in Lua? If not, does Object:destroy() exists? Else-wise, returning an object as "nil" will be garbage collected?)[/li][/ul]

I also plan later to give a try (unless aster goes ahead  :smiley: ) to fetch description comments (///) from the C++ equivalent functions using the header includes from the packages and match them with the Lua function for the tool-tip description from the auto-completion in Zerobrane.

Thanks!

-------------------------

cadaver | 2017-01-02 00:57:59 UTC | #2

Welcome aboard!

The construction / destruction mechanisms in Lua scripting are documented here: (look at the end of the page) [urho3d.github.io/documentation/a00017.html](http://urho3d.github.io/documentation/a00017.html)

-------------------------

silverkorn | 2017-01-02 00:58:04 UTC | #3

Pull request sent!

I've discussed with the author from Zerobrane Studio for helping me fix/confirm some issues and he seemed to find Urho3D project quite interesting, so it might help for publicity.  :wink: 

I also suggested to send him a pre-generated Lua API once the next release from Urho3D will be launched.

Let me know if you see something wrong, thanks!

[size=85][color=#FF0000]*[/color] Please note that Zerobrane Studio 0.40 doesn't work properly with Object() constructor but will be fixed in next release ("master" worked properly)[/size]

-------------------------

Mike | 2017-01-02 00:58:04 UTC | #4

Great job silverkorn  :wink:

Do we need to setup a Zerobrane config file to be able to launch lua files with Urho3DPlayer from within the IDE?
Thanks

-------------------------

silverkorn | 2017-01-02 00:58:04 UTC | #5

Yes, we currently need to setup an interpreter in Zerobrane.

Here's how it could be done (Based on Zerobrane Studio in "master" branch [size=85][[url]https://github.com/pkulchenko/ZeroBraneStudio/tree/master[/url]][/size]):
[ul]
[li]For the moment since it's not directly implemented yet, copy the "love2d.lua" within the "interpreter" folder;[/li]
[li]Rename this file to "urho3d.lua";[/li]
[li]In the file, rename all "love2d" to "urho3d", "Love2d" to "Urho3D" and finally "love" to "urho3d" (some case-sensitivity may vary);[/li]
[li]On line #26, replace the 2 last executable names to "Urho3DPlayer.exe" and "Urho3DPlayer";[/li]
[li]Add where your Urho3DPlayer resides in the default variables on lines #16 to #19 (or simply add this path in your PATH environment if you're familiar with it);[/li]
[li]Remove/Comment the condition from line #36 to #39;[/li]
[li]Change line #46 and #47 to [i]local cmd = ('"%s" "%s" %s'):format(urho3d, wfilename:GetFullName(), params and " "..params or "")[/i];[/li]
[li]Open Zerobrane Studio and setup a project directory by clicking on the "..." button on the left panel (Urho3D's "./Bin/Data/LuaScripts" for exemple);[/li]
[li]Change the the interpreter to Urho3D in "Project" -> "Lua Interpreter" -> "Urho3D";[/li]
[li]Open a Lua file then launch it "Project" -> "Run" (or F6) or with Scratchpad (*not tried yet, should run directly modifications without restarting the player) "Project" -> "Run as Scratchpad" (or Ctrl-F6).[/li][/ul]

These steps are not final neither 100% guaranteed to work so keep in mind that I'm planning to send an API and interpreter setup to Zerobrane Studio's repository once the next Urho3D release will be out. You will be able after to replace the API file with one generated manually from a future version and/or the master branch.

Until the next release, I'll work on a better interpreter configuration setup and probably setting a reflection of the C++ Doxygen description into the "ToZerobraneStudioHook.lua" generator. :slight_smile:

-------------------------

Mike | 2017-01-02 00:58:05 UTC | #6

Many thanks silverkorn :smiley:

For now it seems that Scratchpad doesn't work as is.

-------------------------

weitjong | 2017-01-02 00:58:05 UTC | #7

Thanks for sharing this, silverkorn. Just try it with the ToZerobraneStudioHook.lua and I am loving it already. BTW, while reviewing the hook, I notice the printFunction() does not include any constructors. Is that intentional? Otherwise, the ToDox hook and ToZero hook could share a large chunk of codes and only differs in outputting logic in the end. Probably could use 'require' statement to include the shared chunk to avoid code repetition? Also, saw your TODO comment. Do you plan to put those doxygen comment to ToDox hook as well when it happens?

-------------------------

silverkorn | 2017-01-02 00:58:06 UTC | #8

[quote]BTW, while reviewing the hook, I notice the printFunction() does not include any constructors. Is that intentional? [/quote]
Yes, Zerobrane Studio doesn't support it properly and, as I understood from the document sent by cadaver, we should not call "Object:Object()" in Lua for construction, so the latest Zerobrane Studio (currently on "master" branch) supports "Object()" as an object/class reference.
Otherwise, "new" and "delete" methods are used as alternative, but these needs to be managed manually, they will not be garbage collected by Lua, only the "Object()" constrcutor will be.

[quote]Otherwise, the ToDox hook and ToZero hook could share a large chunk of codes and only differs in outputting logic in the end. Probably could use 'require' statement to include the shared chunk to avoid code repetition?[/quote]
Why not? To be honest, I've copied the 1st "ToDoxHook.lua" that was created to have the freedom to modify it without feeling restricted... Was it by you or Aster? 
Feel free to edit it if needed.

[quote]Also, saw your TODO comment. Do you plan to put those doxygen comment to ToDox hook as well when it happens?[/quote]
Sure. I'll start with the Zerobrane hook then I could fit and adjust it in the ToDox hook.

-------------------------

aster2013 | 2017-01-02 00:58:06 UTC | #9

Good job!

You can require ToDoxHook in your lua, then rewrite  classPackage:print and these writeXXX funtions,  I think it will work well.

-------------------------

silverkorn | 2017-01-02 00:58:06 UTC | #10

Ok, I've applied it. I just needed to set first variables as global in "ToDoxHook.lua" and it seems to work.
I guess I'll create the description's fetch/map in the "ToDoxHook.lua" to consider it as the default/master script.

Btw, I've noticed that I was added in the credits list, thanks for that!
You can change it to my full name, I realized that you took the one from my profile and I just updated it! :wink:
Thanks!

-------------------------

weitjong | 2017-01-02 00:58:06 UTC | #11

Nice! Your PR has been merged now.

-------------------------

silverkorn | 2017-01-02 00:58:11 UTC | #12

Hi guys, little update.

I had time to play with the description extractor recently.

The general results seems good but it's a bit clunky since it's like I had to rewrite the Classes/Functions/Properties generator (ie, many regular expressions and cross-platform (to test) currently working directory workaround).

It needs some adjustments to fit in both "Dox" and "Zerobrane" output but I guess the hardest part is now behind.  :smiley:

I'll probably need a confirmation when done on it's operation on Unix/BSD platforms.

Thanks!

-------------------------

gotusso | 2017-01-02 00:58:15 UTC | #13

Hi!
I started a similar project a few weeks ago to provide autocompletion in Eclipse LDT (github.com/Gotusso/UrhoLDT)
Too bad I didn't saw this before, I wouldn't have started that project :stuck_out_tongue: I should check your code and try to merge as much code as possible.
On the other hand, I would like to debug the Lua code on the IDE, so I'm modifing the player to accept an '-e' parameter, as Eclipse LDT and Zerobrane uses it to wire-up some code for debugging. Have you looked something about that?
Cheers

-------------------------

silverkorn | 2017-01-02 00:58:19 UTC | #14

Sorry gotusso :wink:

No, I didn't have time to look at this, this month is unfortunately quite charged on my side and I'm having headaches with the description fetching. (The funny thing is, in the end if it works well, it could maybe replace the entire parsing mechanism from "tolua++" on package and header files with a standalone script) :confused: 

Otherwise, got on with it! I guess this is the missing piece to inject code for live coding (scratchpad) and debugging with Zerobrane Studio.
I would maybe suggest to make it possible by default on the debug build (with Lua/LuaJIT) to avoid code injection on a final product for security purpose.

-------------------------

silverkorn | 2017-01-02 00:58:26 UTC | #15

Hey guys,

I'm in running some questionable situations.

I want to map the description depending on the [b]Class -> Function/Property name -> Parameters[/b] for splitting overloading function.
Here's some example of what my debug print returns:

[code]Current Params: const String& name, unsigned char layer, bool looped, float fadeInTime = 0.0f
Name: Play
ok (name = "Play", type = "functions", className = "AnimationController")
Class: AnimationController = AnimationController
Element: Play = Play
Func1 Param: "const String", "&", "name", ""
Func1 Param: "unsigned", "", "char", ""
Func1 Param: "bool", "", "looped", ""
Func1 Param: "float", "", "fadeInTime", "0.0f"
Func2 Param: "const String", "", "name", ""
Func2 Param: "char", "", "layer", ""
Func2 Param: "bool", "", "looped", ""
Func2 Param: "float", "", "fadeInTime", "0.0f"
Is same element? False

Current Params: const String& fileName = String::EMPTY
Name: ApplyMaterialList
ok (name = "ApplyMaterialList", type = "functions", className = "StaticModel")
Class: StaticModel = StaticModel
Element: ApplyMaterialList = ApplyMaterialList
Func1 Param: "const String", "&", "fileName", "String::EMPTY"
Func2 Param: "const String", "", "fileName", "String::EMPTY"
Is same element? False[/code]
[size=85](Func1 Param = Header function's parameter, Func2 = Package function's parameter)[/size]

It says that the function is not the same due to the pointer/reference and it definitively is the case from what's I've seen in the package file VS the header file.

Similarly, I have a missing but "defaulted" argument like this:
[code]Current Params: Model* model, bool createBones = true
Name: SetModel
ok (name = "SetModel", type = "functions", className = "AnimatedModel")
Class: AnimatedModel = AnimatedModel
Element: SetModel = SetModel
Func1 Param: "Model", "*", "model", ""
Func1 Param: "bool", "", "createBones", "true"
Func2 Param: "Model", "*", "model", ""
Is same element? False[/code]

Is it intentional? 
Should I ignore those cases as they are quite specific or make an additional possibility if it's a "const String" against "const String&"?

Thanks!

-------------------------

cadaver | 2017-01-02 00:58:26 UTC | #16

Both of these are intentional. Passing strings as const String instead of const String& is an artifact of the Lua bindings mechanism. Aster will know this better. And sometimes "advanced" default-valued parameters that only make sense in internal engine use are left out from the script bindings, like the createBones parameter. In that case it's also to allow turning the SetModel function into a property setter.

-------------------------

aster2013 | 2017-01-02 00:58:26 UTC | #17

Hi, 

Because String is a custom class, if we binding it to Lua, all string operate are very difficult. Lua's string functions are very strength. So we directly mapping String to Lua string. These are same mapping between Vector<T> and Lua table.

I think you can ignore constant, reference and default value, just compare argument types.

-------------------------

silverkorn | 2017-01-02 00:58:28 UTC | #18

Noted!

What about this? 
StringHash == const String? [size=85]
(I've changed the "Func" printing name to be more relevant)[/size]

[code]Current Params: StringHash eventType, VariantMap& eventData
Name: SendEvent
ok (name = "SendEvent", type = "functions", className = "Object")
Class: Object = Object
Element: SendEvent = SendEvent
FuncHeader  Param: "StringHash", "", "eventType", ""
FuncHeader  Param: "VariantMap", "&", "eventData", ""
FuncPackage Param: "const String", "", "eventName", ""
FuncPackage Param: "VariantMap", "*", "eventData", "0"
Is same element? False[/code]

Also, shall I embed "unsigned" with next word as a type (or simply ignore it) and guess that "unsigned char" == "char"?

[code]Current Params: const String& name, unsigned char layer, bool looped, float fadeTime = 0.0f
Name: PlayExclusive
ok (name = "PlayExclusive", type = "functions", className = "AnimationController")
Class: AnimationController = AnimationController
Element: PlayExclusive = PlayExclusive
FuncHeader  Param: "const String", "&", "name", ""
FuncHeader  Param: "unsigned", "", "char", ""
FuncHeader  Param: "bool", "", "looped", ""
FuncHeader  Param: "float", "", "fadeTime", "0.0f"
FuncPackage Param: "const String", "", "name", ""
FuncPackage Param: "char", "", "layer", ""
FuncPackage Param: "bool", "", "looped", ""
FuncPackage Param: "float", "", "fadeTime", "0.0f"
Is same element? False[/code]

Sorry for those questions, unfortunately I'm not an usual C/C++ programmer  :confused:

-------------------------

friesencr | 2017-01-02 00:58:28 UTC | #19

signed vs unsigned denotes whether there is a bit reserved for the negative or positiveness of a number.  Unsigned has no negative value so it can use that extra bit for getting bigger numbers or limiting the domain of a number to only positive ones.  I am guessing we are using an unsigned char for cheesing an 8 bit number.  Integers are 32bit.  I can't get much further into detail since alas I am no c++ programmer myself.

-------------------------

aster2013 | 2017-01-02 00:58:28 UTC | #20

@silverkorn If you like, you can put your project to github. So other people can contribute to it.

-------------------------

silverkorn | 2017-01-02 00:58:28 UTC | #21

Thanks!

Indeed, I'll wrap up what I've done and clean up a little bit as this doesn't affect anything important at all, there might just be few "undescripted" functions to the output.

But before, I guess it would be great to prepare a table for equivalent types, so for special issues, we could map them there.

-------------------------

silverkorn | 2017-01-02 00:58:30 UTC | #22

Ok, I've sent the Pull Request.

Feel free to adjust missing/wrong stuff (or bad coding convection, sorry if so :wink:).
I've commented the previously shown debug prints, so you can reactivate them and output it in files to compare with a "Diff" application.
Please, try it if possible on a Unix OS to confirm that the current working directory workaround is running properly.

BTW, I haven't touched the Doxygen output because I'm not exactly sure how to print it, but everything should be there to implement it. ([u]classes[i].functions/properties[j].descriptions[k][/u]) :slight_smile:

Let me know if there's anything,
Thanks!

-------------------------

weitjong | 2017-01-02 00:58:30 UTC | #23

I have tested the PR in my Linux system. The get current working directory seems to work. It returns something like this for my case: [i]/path/to/urho3d/root[/i]/Source/Engine/LuaScript/pkgs and the separator character is '/'. However, I have encountered an issue further down the road. It hits an error on the printDescriptionsFromPackageFile recursive function. Here is the error and stack trace.
[code]
***curr code for error is tolua_property__get_set float dampingRatio;

stack traceback:
	[string "tolua embedded: lua/basic.lua"]:57: in function 'tolua_error'
	[string "tolua: embedded Lua code 23"]:5: in main chunk

: No such file or directory).ing "ToDoxHook.lua"]:293: bad argument #1 to 'lines' (/path/to/urho3d/root/Source/Engine/LuaScript/pkgs/Audio/Audio.pkg[/code]

I have not spent much time to figure out why it happens.

-------------------------

silverkorn | 2017-01-02 00:58:30 UTC | #24

Hmm... I'll try it on my VirtualBox Linux, it seems to work properly on my Windows 7 (with LuaJIT).
Did you used Lua or LuaJIT building?

-------------------------

weitjong | 2017-01-02 00:58:31 UTC | #25

with LuaJIT.

-------------------------

gotusso | 2017-01-02 00:58:31 UTC | #26

[quote="silverkorn"]Sorry gotusso :wink:

No, I didn't have time to look at this, this month is unfortunately quite charged on my side and I'm having headaches with the description fetching. (The funny thing is, in the end if it works well, it could maybe replace the entire parsing mechanism from "tolua++" on package and header files with a standalone script) :confused: 

Otherwise, got on with it! I guess this is the missing piece to inject code for live coding (scratchpad) and debugging with Zerobrane Studio.
I would maybe suggest to make it possible by default on the debug build (with Lua/LuaJIT) to avoid code injection on a final product for security purpose.[/quote]

Hi Silverkorn, sorry I'm also quite busy.

I've made a fork to recive the '-e' parameter in the player and now I can debug lua scripts in Eclipse LDT. I think I will make a guide in the next days. It would be great if you can try it and check if it's also useful for you at zerobrane. The code is at ([github.com/Gotusso/Urho3D/tree/lua-debug](https://github.com/Gotusso/Urho3D/tree/lua-debug)). Please, note I needed to change the order of the player parameters from "Urho3DPlayer <scriptfile> [options]" to "Urho3DPlayer [options] <scriptfile>" to be able to launch it from eclipse. 

Cheers

-------------------------

silverkorn | 2017-01-02 00:58:31 UTC | #27

[quote="gotusso"]Hi Silverkorn, sorry I'm also quite busy.[/quote]
Don't worry, me too! :stuck_out_tongue:

I'll check it out soon, I'll try to fix the previous issue identified by weitjong, it seems to happen because of the "directory" variable in some functions.
At least it motivated me to install a Linux distro on my system, which I shall have done way earlier.  :smiley:

Thanks!

-------------------------

silverkorn | 2017-01-02 00:58:32 UTC | #28

Well, that's cryptic!
It is able to load files from the directory of the executable and the current working directory but once we're out of this scope, Lua(JIT) seems to not see the file...

With the full path using the file handling "io.open" (end of output example):
[code]filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/Scene/Serializable.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/Scene/Component.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/Scene/Node.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/Scene/Scene.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/Scene/SplinePath.pkg
filename done :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/SceneLuaAPI.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/UI/UIElement.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/UI/BorderImage.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/UI/Button.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/UI/CheckBox.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/UI/Cursor.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/UI/FileSelector.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/UI/Font.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/UI/LineEdit.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/UI/Menu.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/UI/MessageBox.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/UI/DropDownList.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/UI/Slider.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/UI/ScrollBar.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/UI/ScrollView.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/UI/ListView.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/UI/Sprite.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/UI/Text.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/UI/Text3D.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/UI/ToolTip.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/UI/UI.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/UI/Window.pkg
filename MISSED :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/UI/View3D.pkg
filename done :/path/to/Urho3D/Source/Engine/LuaScript/pkgs/UILuaAPI.pkg
filename done :/path/to/Urho3D/Bin/LuaPkgToDox.txt[/code]

With current working directory scope using the file handling io.open (end of output exemple):
[code]filename MISSED :Scene/Serializable.pkg
filename MISSED :Scene/Component.pkg
filename MISSED :Scene/Node.pkg
filename MISSED :Scene/Scene.pkg
filename MISSED :Scene/SplinePath.pkg
filename done :SceneLuaAPI.pkg
filename MISSED :UI/UIElement.pkg
filename MISSED :UI/BorderImage.pkg
filename MISSED :UI/Button.pkg
filename MISSED :UI/CheckBox.pkg
filename MISSED :UI/Cursor.pkg
filename MISSED :UI/FileSelector.pkg
filename MISSED :UI/Font.pkg
filename MISSED :UI/LineEdit.pkg
filename MISSED :UI/Menu.pkg
filename MISSED :UI/MessageBox.pkg
filename MISSED :UI/DropDownList.pkg
filename MISSED :UI/Slider.pkg
filename MISSED :UI/ScrollBar.pkg
filename MISSED :UI/ScrollView.pkg
filename MISSED :UI/ListView.pkg
filename MISSED :UI/Sprite.pkg
filename MISSED :UI/Text.pkg
filename MISSED :UI/Text3D.pkg
filename MISSED :UI/ToolTip.pkg
filename MISSED :UI/UI.pkg
filename MISSED :UI/Window.pkg
filename MISSED :UI/View3D.pkg
filename done :UILuaAPI.pkg
filename done :/path/to/Urho3D/Bin/LuaPkgToDox.txt[/code]

Anyone has a clue? 

It worked with Windows MinGW compiled as :
"cmake_mingw.bat -DENABLE_64BIT=1 -DENABLE_LUAJIT=1 -DENABLE_DOCS=1" (Windows 7 64-bits).

This problematic one is built as :
"./cmake_gcc.sh -DENABLE_LUAJIT=1 -DENABLE_DOCS=1" (Linux Mint 14 32-bit).

Could it be a missing building flag to permit out of those scopes?

Thanks!

-------------------------

silverkorn | 2017-01-02 00:58:33 UTC | #29

I think I found it... Well I hope so, otherwise this thread will become my personal diary!  :laughing: 

I'll need to adjust my code to add some ':gsub("%c", "")' because line breaks seemed to cause this problem, which make sense because of Linux and Windows different line breaks philosophies (CR vs CRLF vs LF).

-------------------------

silverkorn | 2017-01-02 00:58:33 UTC | #30

You can test it out!

I haven't created a pull request for now to avoid a potential error and creating one every time...
([url]https://github.com/silverkorn/Urho3D[/url])

Does it matter if I send a pull request containing a "Merge remote-tracking branch 'upstream/master'"?

Thanks!

-------------------------

weitjong | 2017-01-02 00:58:34 UTC | #31

You may have nailed down the problem. The ToDoxHook.lua now works as expected in *nix build environment. I have also just fixed a small issue with LuaJIT search path which was broken since LuaJIT v2.0.3 upgrade. With that fix, I could also confirm that ToZerobraneStudioHook.lua produces output without throwing out any error. I have no time yet to compare the new output with the old output from previous hook though.

If I know Lasse better, I don't think he would mind the "Merge...." commit message in the history.

-------------------------

silverkorn | 2017-01-02 00:58:35 UTC | #32

I've remade the fork, it should be good.
The PR has been resent with the fix.

If everything is good, I'll start to prepare the ZerobraneStudio's configuration file + generating and sending an Urho3D API file for the latest "stable" version.
I'll probably look with gotusso (and you if you wish) to permit live coding for IDEs at least with the debug version. 
Otherwise, it's possible for ZerobraneStudio that "Mobdebug" can do all the trick... To see...

Thanks!

-------------------------

cadaver | 2017-01-02 00:58:36 UTC | #33

Occasional merge commits are fine; there are already several in the history anyway.

-------------------------

silverkorn | 2017-01-02 00:59:03 UTC | #34

Sorry for the delay...  :unamused: 
I've sent a Pull Request on their side for a simple "ready to go" support for Urho3D 1.31+.
I've included the process in the commit to generate a new API file, so you can make one on your own with the current "Master" branch.

So you can give it a try! :smiley:

[size=85]Edit: Link to their repository ([url]https://github.com/pkulchenko/ZeroBraneStudio[/url])[/size]

-------------------------

silverkorn | 2017-01-02 01:01:47 UTC | #35

Just for info, I've updated the API in the ZeroBranePackage repository to auto-complete Urho3D 1.32 Lua functions.
[github.com/pkulchenko/ZeroBranePackage](https://github.com/pkulchenko/ZeroBranePackage)

-------------------------

silverkorn | 2017-01-02 01:05:31 UTC | #36

Now updated to Urho3D 1.4

-------------------------

dertom | 2021-10-23 08:45:22 UTC | #37

I know this thread is quite old, but I just wanted to share that I updated the LUA Eclipse LDT-Autocompletion, Debugging-Version from @gotusso to work with the current urho3d-version. 
I actually don't use it actively but thought it would be nice to share and might help someone... :D 

https://github.com/dertom95/UrhoLDT

95ole,Tom

-------------------------

