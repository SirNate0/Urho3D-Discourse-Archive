ghidra | 2017-01-02 01:01:30 UTC | #1

I write my urho app on 2 different devices 3 different OSs.
Mainly on ubuntu 14.10. on my tower with windows 7 dual boot. second most on my laptop ubuntu 14.04.

So, I was having some issues last night with the scriptObject, that was fixed by setting the instance to reference my main.as class instead of just the class file itself.
Everything works, both on 14.10 and windows7. I did some extra work after getting it to do what I wanted, all still works.

This morning on the train, on the laptop, tried the same code, and the same urho and it wasnt working. It didnt error, but what I had working was not working.
I redownloaded urho, re downloaded my repo, and nothing was working still.

The code is actually here:
[github.com/ghidra/urho_shmup](https://github.com/ghidra/urho_shmup)
at the  Nov 23, 2014  "faster projctile" commit.
forgive me it's messy.

In a nut shell:
--------
main.as inits an inputplayer.as class to handle controls.
it also instantiates my character.xml, that has a character.as script object.
character.as extends pawn.as extends actor.as

playerinput is given the node that is spawned that has the character scriptobject.
it then uses that to pass functions to it for controls.

And that is where it doesnt work on the laptop, but does on my desktop.
at this function:

[code]
void set_controlnode(Node@ control_node){
   Pawn@ pawn = cast<Pawn>(control_node.scriptObject);
   //Character@ pawn = cast<Character>(control_node.scriptObject);
   //Pawn@ pawn = cast<Pawn>(control_node.GetScriptObject("Character"));
   if (pawn !is null){
      //Print("we have something to control");
      node_ = control_node;
   }
}
[/code]

It doesnt error, because i am doing the null check.
And if I Print numComponents it sees them all, or if I grab the components[1], it knows it's a scriptObject. But it isnt getting passed the null check.

So, is this a bug, or am i doing someting wrong here? Since it works in 2 different places, but not in 1.

Thanks

EDIT:

I'm also not sure that it isnt some other garbage that is in my code that is causing conflicts, but I'm throwing it out there.

-------------------------

friesencr | 2017-01-02 01:01:30 UTC | #2

Could it be a load order issue?  Or events running in different orders?

-------------------------

cadaver | 2017-01-02 01:01:30 UTC | #3

Unless you're using background loading of resources (it doesn't happen automatically, so if you don't know then you aren't) the load order should be the same on every platform & computer, as it's all main thread logic.

What possibly can trip it up if the script file(s) get loaded multiple times. I imagine this can be theoretically possible due to Windows being not case-sensitive, and Ubuntu is. Though I don't have an idea of the specifics in this case. If you make a debug build it will print to the log whenever a resource gets loaded.

To save trouble, in small to medium-small games I'd recommend the approach used in NinjaSnowWar: the main script file includes all other script files. All script objects are instantiated by referring to the main scriptfile. This ensures there are no gotchas of script classes in one script file not being visible to other files, which would manifest as casts returning null pointers.

The "classes not being visible to another script file" is an AngelScript mechanic. For another solution, see the "shared script entities" approach. [angelcode.com/angelscript/sdk/do ... hared.html](http://angelcode.com/angelscript/sdk/docs/manual/doc_script_shared.html)

-------------------------

ghidra | 2017-01-02 01:01:31 UTC | #4

Using the Shared Entities did the trick on my laptop, I'll test it tonight on my desktop to make sure it all still works.
Thank you.
EDIT: all works!

-------------------------

