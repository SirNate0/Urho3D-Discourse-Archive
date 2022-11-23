NiteLordz | 2017-01-02 01:02:47 UTC | #1

I am trying to dynamically load a script, and execute a method within the dynamically loaded script.

Script A launches.

Script B contains a custom defined function that needs to be executed. 

The file name of Script B is read from a customization file that is read in Script A. When Script A completes, it then needs to execute the next script file (Script B).

I can load the script file dynamically and it is stored in a ScriptFile@ object.  

Note, this script is not attached to any node or component.

-------------------------

cadaver | 2017-01-02 01:02:48 UTC | #2

Should work like this. Note that the second script file is left in memory, but you could purge it explicitly from the resource cache with ReleaseResource(). Also note that ability to create arbitrary class instances via AngelScript API doesn't exist, as there's the difficulty of how to return an arbitrary object back to the calling script, so for now you're limited to calling free functions. I suppose it could work if it would be required to inherit from a known class, like ScriptInstance requires.

First script file:

[code]
void Start()
{
    ScriptFile@ newScript = cache.GetResource("ScriptFile", "Scripts/NewScript.as");
    Array<Variant> params;
    newScript.Execute("void MyFunction()", params);
    engine.Exit();
}
[/code]

Second script file: (NewScript.as)

[code]
void MyFunction()
{
    Print("MyFunction was executed");
}
[/code]

Finally, if you pull latest master, you'll have the option of omitting the Variant array if your function has no parameters.

-------------------------

NiteLordz | 2017-01-02 01:02:48 UTC | #3

yea, i got it figured out, i wasn't passing in the parameters.  i was actually in the process of making that method not need the parameter lol.  

thanks for the update

-------------------------

