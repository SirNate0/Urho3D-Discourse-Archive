alessandro | 2017-05-24 06:49:19 UTC | #1

HI all, as said some days ago, i am new in this environment.
I am using the c# version and so i am trying to understand some little tutorials i found on xamarin site.

Now i am able to create a simple scene, i am able to add simple models and so on.
Now i'd like to add some movements to my models but i cannot understand how to respond to user input.

i'd like to add four circular buttons to the screen but i cannot understand how to do. And so on, i cannot understand where to find a simple reference for this kind of scripting : 

<?xml version="1.0"?>
<element inherit="UI/ScreenJoystick.xml">
    <add sel="/element/element[./attribute[@name='Name' and @value='Button0']]">
        <attribute name="Is Visible" value="false" />
    </add>
    <add sel="/element/element[./attribute[@name='Name' and @value='Button1']]">
        <attribute name="Is Visible" value="true" />
    </add>
    <add sel="/element/element[./attribute[@name='Name' and @value='Button2']]">
        <element type="Text">
            <attribute name="Name" value="KeyBinding" />
            <attribute name="Text" value="SELECT" />
        </element>
    </add>
    <replace sel="/element/element[./attribute[@name='Name' and @value='Hat0']]/attribute[@name='Position']/@value">12 -76</replace>
    <add sel="/element/element[./attribute[@name='Name' and @value='Hat0']]">
        <element type="Text">
            <attribute name="Name" value="KeyBinding" />
            <attribute name="Text" value="WSAD" />
        </element>
    </add>
</element>

-------------------------

smellymumbler | 2017-05-24 18:35:32 UTC | #2

C# version? You mean UrhoSharp? I think you'll find better help here: https://github.com/xamarin/urho/issues

-------------------------

alessandro | 2017-05-25 06:50:27 UTC | #3

i'm not looking for issues but an help to start.
Can you explain me how to use screenjoistick?

thanks

-------------------------

rasteron | 2017-05-25 07:59:33 UTC | #4

Hey alessandro. You can just check out the utilities folder which has a touch and joystick implementation. It's in angelscript so just make the conversion to C#

https://github.com/urho3d/Urho3D/tree/master/bin/Data/Scripts/Utilities

Hope that helps.

-------------------------

