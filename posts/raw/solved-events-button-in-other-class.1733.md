Kanfor | 2017-01-02 01:09:47 UTC | #1

Hi, Urhofans.

I have my Application class where I can check the events, but I would like make other class
and check new events there like buttons.

Can somebody help me?  :unamused: 

[color=#FF0000]Suscribetoevent was not declared in this scope[/color]

-------------------------

jmiller | 2017-01-02 01:09:47 UTC | #2

Hi,

You probably want to make your class a subclass of Object, which has the SubscribeToEvent method.

For example, the Character class from CharacterDemo subclasses LogicComponent, so it's also an Object.
[github.com/urho3d/Urho3D/tree/m ... racterDemo](https://github.com/urho3d/Urho3D/tree/master/Source/Samples/18_CharacterDemo)

[urho3d.github.io/documentation/H ... types.html](http://urho3d.github.io/documentation/HEAD/_object_types.html)

HTH

-------------------------

Kanfor | 2017-01-02 01:09:48 UTC | #3

Thank you very much!

 :smiley: 

Urho3D has a great community.
-------------------------
But... not work in my case  :cry: 

I only want create a 

[color=#4040BF]SubscribeToEvent(button, E_RELEASED, URHO3D_HANDLER(MyNewClass, MyButtonFunction));[/color]

in the new class.
----------------------
Ok. Now works, but I need set the new class as LogicComponent  :stuck_out_tongue: I'm not sure if this is the best solution  :unamused:

-------------------------

Kanfor | 2017-01-02 01:09:48 UTC | #4

No, not work  :question: 

[code]void MyNewClass::Press_Switch(StringHash eventType, VariantMap& eventData)
{
    text_password->SetText("HELLO");
    cout << "SWITCH WORKS!" << endl;
}[/code]

When I press my switch button, the app crash. If I put the setText in othe function works fine, but if i add this
in a handler the app crash.

-------------------------

jmiller | 2017-01-02 01:09:48 UTC | #5

It is only a small bit of code, but I can say you probably have some bad C++ somewhere in that class. :stuck_out_tongue: 
The documentation and [url=http://urho3d.wikia.com/wiki/Unofficial_Urho3D_Wiki]wiki[/url] can help, as well as a debugger.

To forget to register new Component classes can cause crashes.
[github.com/urho3d/Urho3D/blob/m ... mo.cpp#L59](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/18_CharacterDemo/CharacterDemo.cpp#L59)

Assuming the demo does not crash, you might study it for something else missed.

-------------------------

Kanfor | 2017-01-02 01:09:49 UTC | #6

Thanks again!  :wink: 
I'll keep trying

-----------------------

WORKS!!!  :smiley:

-------------------------

