ghidra | 2017-01-02 01:01:29 UTC | #1

okay, so I am using the ninjasnowwar method of instantiatin a xml node. It has a script instance on it. Called "Character"
I spawn it:

[code]
Node@ spawn_player(){
  XMLFile@ xml = cache.GetResource("XMLFile", "Scripts/character.xml");
  return scene_.InstantiateXML(xml, Vector3(0.0f,0.0f,0.0f), Quaternion());
}
[/code]

Then when I try to grab the scripobject:

[code]
void Start(){
  Node@ player_ = spawn_player();
  //Character@ c_ = cast<Character>(player_.GetScriptObject("Character"));
  Character@ c_ = cast<Character>(player_.scriptObject);
  Print(c_.temp);
}
[/code]

the character script looks like this:

[code]
class Character:ScriptObject{
  int temp;
  Character(){
    temp = 9999;
  }
}
[/code]


The print function gives me an error:
Exception 'Null pointer access' in 'void Start()' with either method (the non commented and the commented).
Am i going at this wrong? Am i trying to access it before it is instantiated?
Thanks

-------------------------

hdunderscore | 2017-01-02 01:01:29 UTC | #2

Not 100% sure if this is your issue, but something that tripped me up when working with Angelscript is the module resolution. 

Here is a link that explains the issue: [topic52.html](http://discourse.urho3d.io/t/how-exactly-do-scripts-in-the-editor-work/74/1)

But in summary, if you want to talk to the 'scriptX.as' module from the 'scriptY.as' module, you need to #include 'scriptX.as' into 'scriptY.as' so that it's one big module, and point both of the ScriptFile components to the 'scriptY.as' module. If you don't do this, Angelscript will see the 'Character' class in 'scriptX.as' module as different from the 'Character' class in 'scriptY.as' module.

Other methods were also described in the link, but this one is simplest.

-------------------------

ghidra | 2017-01-02 01:01:29 UTC | #3

yep, that was it.
I just changed the path that my xml was refereceing, to not just reference the character.as file. but my main.as file, that I was calling it from.
Thanks for pointing that out.

-------------------------

