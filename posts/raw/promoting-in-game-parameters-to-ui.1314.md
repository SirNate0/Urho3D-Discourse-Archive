sabotage3d | 2017-01-02 01:06:45 UTC | #1

Hi guys,
What would be the fastest way to promote parameters from the C++ side to the in-game UI ? At the moment it looks a bit tedious. Does anyone have a macro or a quick factory class ?

-------------------------

weitjong | 2017-01-02 01:06:46 UTC | #2

How about by making your game parameters as "attributes"? Your in-game UI should be able to edit attribute value and apply the changes similar to how attribute-inspector works in the Editor.

-------------------------

sabotage3d | 2017-01-02 01:06:49 UTC | #3

Thank you weitjong. Do you have a simple snippet on how to do that ?

-------------------------

cadaver | 2017-01-02 01:06:49 UTC | #4

The AttributeEditor is 1600 lines of code, so it can hardly be called a snippet. Also it's AngelScript so if your project is C++ you'll have to adapt the code.

For something simpler and manual, which doesn't use attributes, you can look into the editor's Material Editor window (bin/Data/Scripts/Editor/AttributeEditor.as): it loads the predefined editor window layout, hooks up to the edit elements' value change events, and loads the elements' initial values from the material. The event handlers apply the element values back into the material. That is AngelScript as well, though. 

The downside of a predefined UI layout and manual code to edit the values is that you have to add UI elements and code for each new value that needs to be edited. So, pick your poison :slight_smile:

-------------------------

sabotage3d | 2017-01-02 01:06:49 UTC | #5

I am already using scorvi's InGameEditor. I am just not sure how to promote custom attributes . Is there a better way doing it with AngelScript ?

-------------------------

weitjong | 2017-01-02 01:06:49 UTC | #6

The sample code is already there, if you look for them carefully. Check out sample 14_SoundEffects. The comments in the sample do not say it out loud but it almost demonstrates what you want already. It binds a few of the object's states to UI elements and control those states through the UI. It does not go through Urho3D attribute manipulation mechanism though. You can also do it like this when you don't intend to serialize/persist your in-game parameters. If they need to be persisted then it is easier to make those parameters become attributes and naturally your game object must be derived from Serializables instead of Object class.

In my previous post I mentioned to use attribute-inspector style of editing and applying the changes. But that's only one way of doing it, i.e. if you want to have a generic in-game UI system to manipulate all your game attributes. However, if you would only want to bind a few specific game attributes that you want to control then the direct binding demonstrated by the above sample should work as well.

-------------------------

cadaver | 2017-01-02 01:06:49 UTC | #7

Ah, forgot that one, indeed a much better example of the "simple" way than the material edtor!

EDIT: the InGameEditor seems to already have adapted the attribute editor code from AngelScript to C++, so going that route (if it works right) should just require defining attributes for your components. For examples look to any of the Urho3D inbuilt component classes, for example the drawable components.

-------------------------

sabotage3d | 2017-01-02 01:06:49 UTC | #8

Thanks a lot cadaver, I will try that :slight_smile:

-------------------------

