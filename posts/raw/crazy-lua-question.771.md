devrich | 2017-01-02 01:02:47 UTC | #1

Hi everyone,

( [u][i]Our Lua Game Code's Source Code Protecting Idea[/i][/u] )

I was wondering if there was a way to "embed" a Lua script into the Urho3D player prior to distributing to keep our Lua script code private from customers?

Here is what I mean:

1: Create a great video game using Lua script and the pre-existing Urho3DPlayer application during development

2-A: Development is complete and time to send to GooglePlay, Amazon MarketPlace, Ouya, etc etc

2-B: ( how to do this step ) Embed our .Lua script file(s) directly into the Urho3DPlayer -- I assume we'd have to do this into directly the Urho3D Player source code

2-C: Compile for our target platform

2-D: Send the compiled Urho3DPlayer ( which now contains our Lua script file(s) ) to the GooglePlay, etc

If this is possible then how to do this? ( or would we "have" to give our our game code as the .Lua files ? )

-------------------------

cadaver | 2017-01-02 01:02:47 UTC | #2

For store submission, the application already exists as a form of package (for example .apk on android). 

Whether the script is embedded into the executable or as a resource file within the package should not have great difference on how "hackable" it is. By all means you can cook up whatever protection mechanisms you want, but you'd be basically on your own; it shouldn't (IMO) be Urho3D's responsibility in any way. Also consider that the Urho3DPlayer is a very minimal executable (basically: instantiate engine, load script, let it run) and at the point when you have a finished game ready for submission, you could (should?) easily replace it with your own customized executable.

-------------------------

devrich | 2017-01-02 01:02:48 UTC | #3

I think I understand what you're explaining. *sigh* I was hoping it'd be easier than converting Lua scripts to C++ ....

Do you know of an easy way or method to go about converting Lua scripts to c++ ?

-------------------------

weitjong | 2017-01-02 01:02:48 UTC | #4

Just a thought. For simple obfuscation, you can "pre-compile" the Lua script into Lua bytecode. This can be done for both Lua or LuaJIT libraries. We have built the standalone tool for that. The precompiled bytecode does not actually perform any faster but just a layer of obfuscation. You can add another layer by packaging all your assets (including the Lua bytecodes) into *.pak. The PackageTool is provided by Urho3D project too. It uses LZ4 library. If that is still not sufficient for you, I suppose you can add another encryption layer. But like Lasse has pointed out, all these defense layers are useless against the technically-inclined hackers. Your shipped app after all has to reveal the "key" to access those assets. So we are better of just concentrating on our game development. :slight_smile:

-------------------------

devrich | 2017-01-02 01:02:49 UTC | #5

[quote="weitjong"] If that is still not sufficient for you, I suppose you can add another encryption layer. But like Lasse has pointed out, all these defense layers are useless against the technically-inclined hackers. Your shipped app after all has to reveal the "key" to access those assets. So we are better of just concentrating on our game development. :slight_smile:[/quote]

You both bring up excellent points and I understand about the idea that if someone really wants to hack your game then they'll find a way.  I just wanted to try and minimize the opportunity as if some 10 year old kid gets the idea to do a google search for how to hack a program then just follows the instructions like their parents would do when they make them frozen fish sticks in the oven lol ( ohh now i miss fish sticks  :frowning:  )

course when i was 10 the internet didn't exactly exist lol xD


[quote="weitjong"]Just a thought. For simple obfuscation, you can "pre-compile" the Lua script into Lua bytecode. This can be done for both Lua or LuaJIT libraries. We have built the standalone tool for that. The precompiled bytecode does not actually perform any faster but just a layer of obfuscation. You can add another layer by packaging all your assets (including the Lua bytecodes) into *.pak. The PackageTool is provided by Urho3D project too. It uses LZ4 library.[/quote]

I agree that obfuscating my lua scripts and then add them to a *.pak file should be good enough for the most part, thanks for that  :slight_smile:

I have a few questions on that please   :slight_smile: 

on the tools documentation page:  [url]http://urho3d.github.io/documentation/1.32/_tools.html[/url] it talks about compiling AngelScript but do i use the same ScriptCompiler to compile .lua's to bytecode as well?  are there any Lua specific things/instructions i must do/follow?

For the PackageTool the documentation page says: [i][u]"The package file can be added to the ResourceCache and used as if the files were on a (read-only) filesystem."[/u][/i]  How do I load the .pak file from .Lua script? I am assuming I'd use the "cache:" to do it but not sure of the right syntax for it? ( and let's say I just put all my assets and scripts in the /Data/ sub-folder and just package that as Data.pak like the documentation example did because I think that would be easist )

-------------------------

weitjong | 2017-01-02 01:02:49 UTC | #6

[quote="devrich"]I have a few questions on that please   :slight_smile: 

on the tools documentation page:  [url]http://urho3d.github.io/documentation/1.32/_tools.html[/url] it talks about compiling AngelScript but do i use the same ScriptCompiler to compile .lua's to bytecode as well?  are there any Lua specific things/instructions i must do/follow?

For the PackageTool the documentation page says: [i][u]"The package file can be added to the ResourceCache and used as if the files were on a (read-only) filesystem."[/u][/i]  How do I load the .pak file from .Lua script? I am assuming I'd use the "cache:" to do it but not sure of the right syntax for it? ( and let's say I just put all my assets and scripts in the /Data/ sub-folder and just package that as Data.pak like the documentation example did because I think that would be easist )[/quote]
We don't have specific instruction for Lua/LuaJIT standalone tools because they are not tool unique to Urho3D. Our build system simply builds those tools along with Lua/LuaJIT library. You can check the documentation on respective Lua or LuaJIT project on how to invoke their standalone tool.

One thing to take note, however, is that the tool is being built using target toolchain instead of host toolchain. That is, for Android platform, this standalone tool can only be run in the target system. In other words, you need to know how to use "adb" command to transfer the tool to the device, shell into the device, and do your business there.

-------------------------

devrich | 2017-01-02 01:02:51 UTC | #7

Thanks weitjong!  Looks like the android is going to be a bit of a pain  :wink:

-------------------------

