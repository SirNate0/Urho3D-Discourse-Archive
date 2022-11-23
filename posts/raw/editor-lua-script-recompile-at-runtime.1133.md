setzer22 | 2017-01-02 01:05:37 UTC | #1

Hi all! 

I'm starting a new project with Urho3D, and after having developed a taste for LUA I thought It'd be a good idea to adopt LUA as the main scripting language of the project. But when I started making some tests I realised  there's no reload feature for LUA scripts, so I have to restart the whole editor for script changes to take effect.

As ChrisMAN_mk2 pointed out on the IRC channel, there's really no such feature in the Editor's code, and I was just wondering why. Is there any kind of added difficulty in recompiling Lua scripts at runtime? Or is the feature just not implemented yet?

For now I'm gonna take a look myself in the editor code and see if I can add this. If anyone wants to point out the relevant code sections to look at, or wants to provide some help it will be more than welcome.  :smiley: 

Thank you!

-------------------------

GoogleBot42 | 2017-01-02 01:05:37 UTC | #2

Hmmm maybe you could create a small lua program that detects if a loaded lua file has changed and then reload it.

-------------------------

cadaver | 2017-01-02 01:05:37 UTC | #3

I'm not the Lua scripting system maintainer so I don't precisely know how it works.

However, the Lua script is just a "blob" of functions / tables / objects in the Lua VM's memory. If I understand right when you reload a script, you would just re-execute it. What happens to the already created objects? Likely they stay. (I see the LuaFile class has a hasExecuted_ member variable to prevent multiple execution, probably because of exactly this.)

The AngelScript system is more organized, each script file is a module, and the module is destroyed & recreated when the script is reloaded. The in-scene script objects (held by ScriptInstance C++ objects) created from that module are also destroyed, then recreated.

-------------------------

setzer22 | 2017-01-02 01:05:37 UTC | #4

[quote="cadaver"]I'm not the Lua scripting system maintainer so I don't precisely know how it works.

However, the Lua script is just a "blob" of functions / tables / objects in the Lua VM's memory. If I understand right when you reload a script, you would just re-execute it. What happens to the already created objects? Likely they stay. (I see the LuaFile class has a hasExecuted_ member variable to prevent multiple execution, probably because of exactly this.)

The AngelScript system is more organized, each script file is a module, and the module is destroyed & recreated when the script is reloaded. The in-scene script objects (held by ScriptInstance C++ objects) created from that module are also destroyed, then recreated.[/quote]

So basically the problem is that there's no easy way to delete everything a lua script might create without having to track it all object by object, right?

Thanks for the feedback, I'll have a look!

-------------------------

GoogleBot42 | 2017-01-02 01:05:39 UTC | #5

Hmmm the problem of components is more complicated...  I would create a wrapper function for every function that is called for the component (or maybe I would do some metatable magic).  That wrapper function then calls the real function which is stored in a table somewhere.  Then there is code that will automatically reload the component functions.  This would be a little tricky to write maybe I will try to do that when I have more time...  :unamused:  Furthermore, this would not be good to keep in the released version because it will slow down the program a lot due to two functions being called rather than just one for components. :\

-------------------------

setzer22 | 2017-01-02 01:05:45 UTC | #6

I think as long as all the data alocated by the script is released, re-running the script will just reload the component successfully. The defined functions of a ScriptObject are just attributes in a table AFAIK.

Also, as long as Urho is not disabling garbage collection, setting the global symbols the script allocated to null will make the garbage collector delete them. After that, defining those symbols again will achieve reloading.

It's certainly not an efficient approach but it allows for quick prototyping in the editor.

Any ideas on how could I track the allocated global symbols of a lua script without parsing the source? I could check for new additions in the global symbols table, but maybe there's a better way to do it.

-------------------------

GoogleBot42 | 2017-01-02 01:05:45 UTC | #7

[quote="setzer22"]I think as long as all the data alocated by the script is released, re-running the script will just reload the component successfully. The defined functions of a ScriptObject are just attributes in a table AFAIK.

Also, as long as Urho is not disabling garbage collection, setting the global symbols the script allocated to null will make the garbage collector delete them. After that, defining those symbols again will achieve reloading.

It's certainly not an efficient approach but it allows for quick prototyping in the editor.

Any ideas on how could I track the allocated global symbols of a lua script without parsing the source? I could check for new additions in the global symbols table, but maybe there's a better way to do it.[/quote]

Unfortunately, that cannot work with components.  This is because functions are directly attached to the lua component.  Thus, the old functions (which are stored completely independent of the file from which it was generated) are not garbage collected because lua sees that they are being kept alive by the lua component.

But if the lua functions are not stored per component and instead as a template for the component it should be possible (but the urho3d source might need to be modified...

I will look into how urho3d implements lua and see if it is possible.

-------------------------

setzer22 | 2017-01-02 01:05:45 UTC | #8

[quote="GoogleBot42"]
Unfortunately, that cannot work with components.  This is because functions are directly attached to the lua component.  Thus, the old functions (which are stored completely independent of the file from which it was generated) are not garbage collected because lua sees that they are being kept alive by the lua component.

But if the lua functions are not stored per component and instead as a template for the component it should be possible (but the urho3d source might need to be modified...

I will look into how urho3d implements lua and see if it is possible.[/quote]

Lua ScriptObjects usually start like:
[code]
Rotator = ScriptObject()

function Rotator:Start 
   ...
end
[/code]

From that code I just assumed Rotator was a global table, wouldn't re-execute the script re-declare the table and its methods? I'm a bit lost with the inner implementation right now. 

Also, when the symbol for Rotator points somewhere else, won't the garbage collector free that memory?

I don't get why functions in a table would persist, but I'm not very familiar with Lua's inner workings so maybe I'm missing something here.

-------------------------

GoogleBot42 | 2017-01-02 01:05:48 UTC | #9

Rotator is a reference to a lua table with functions that is created when the lua file is loaded and run.  Urho3D will keep a reference to the that very same table internally.  If the file is loaded again, the table that Urho3D keeps internally doesn't change.


Think about it like this.  I create a urho3d component in lua.  This is done by using a custom function that urho3d passes to lua scripts for creating components.  Every time "ScriptObject()" is called in lua the result is guaranteed to be a new empty component.  Lua allocates the table that holds the functions and then lua passes a pointer to urho3d that represents the table (I think it is a bit different than a pointer but here we can think of it as just a pointer).  Then the lua script sets the lua functions inside that table.  And the app is run.

Then the script is reloaded... "ScriptObject()" is called again.  But a different table returned not the original.  This is because it is impossible for urho3d to know that the component already exists (without extra parameters added to ScriptObject() ).  This is much because lua doesn't have builtin classes.  So what ends up happening is that the initial "pointer" to the table help by urho3d is not deleted and urho3d doesn't know that the programmer wants to reload the script.

But don't worry too much :wink:  A wrapper should easily be able to be written that just wraps around ""ScriptObject()" and adds a parameter to uniquely identify a component.  That function would remember every table for every class and overwrite every function automatically.  (But this way might not work depending on if urho3d access the lua functions directly or if it gets them indirectly from the table.)

-------------------------

setzer22 | 2017-01-02 01:05:52 UTC | #10

@Sinoid 

So basically, there's no big issue preventing Lua reloading at runtime? 

When I checked the source I could see the LuaScriptInstance implementing no reload events (as AngelScript does), and as @cadaver pointed out, the reload is avoided on purpose in the code. All that make it seem like in Lua it's not as easy to reload the script. 

Anyway, I'm curious. Is it only me that finds this such an essential thing to have? How do you guys work without script reloading?

-------------------------

