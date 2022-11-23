rogerdv | 2017-01-02 01:01:34 UTC | #1

Another basic question. I have been looking through the editor scripts, but cant find anything similar to what I want to do. I need to parse some xml files containing game configuration, from simple stuff like entity definition to more complex ones like dialogs (still not designed). 
So, my typical xml looks like this: 
[code]
<entities>
 <entity id="one" name="wahatever" description="WTF"/>
 <entity id="another" name="wahatever 2" description="No idea"/>
 *
 *
</entities>
[/code]

A more complex one could be:

[code]<item id="hunt-knife"  name="Knife" > 
  <property name="speed" value="1.0" type="speed"></property>
  <property name="range" value="1" type="range"></property>
 </item>[/code]

Can somebody give me a brief guide to iterate through several childs and parse nested xml?

-------------------------

OvermindDL1 | 2017-01-02 01:01:35 UTC | #2

UIElement and its base classes in the LoadXML function should be a good example.

-------------------------

rogerdv | 2017-01-02 01:01:35 UTC | #3

Yep, but the code is C++, Im using AS and some things are different, for example, you cant do while (childElem) {}, because AS while requires a boolean.

-------------------------

weitjong | 2017-01-02 01:01:35 UTC | #4

You can check how the Editor itself saves and load its configuration file. It is written in AngelScript.

-------------------------

Azalrion | 2017-01-02 01:01:35 UTC | #5

Look at editorimport.as as well.

[code]
        XMLElement compElem = entityElem.GetChild("component");
        while (!compElem.isNull)
        {
            ...

            compElem = compElem.GetNext("component");
        }
[/code]

-------------------------

