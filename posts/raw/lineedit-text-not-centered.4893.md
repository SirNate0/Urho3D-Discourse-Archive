AntiLoxy | 2019-02-03 21:31:00 UTC | #1

Hello, i have a problem with LineEdit.

At start, i want to create a set of classes to simply handle ui controls.

Here is the list of classes I'm going to implement (all inherit directly from UIElement):
- CheckboxControl
- StringControl (1x LineEdit)
- NumberControl (1x LineEdit, 2x Button up / down)
- FileControl (1x LineEdit, 1x Button, 1x FileSelector)
- Vector3Control (3x NumberControl)
- ResourceRefControl

For all these classes, only one event: E_CONTROL_VALUE_CHANGED

That's the idea, what do you think of this design?
For my part I do not see any problem but I prefer to have your opinion in passing.

Now, let's come to my problem.
The LineEdit element does not center the text correctly when this element is created in the constructor of another element (element not yet attached).

StringControl constructor:

    StringControl::StringControl(Context* context) : UIElement(context)
    {
        lineEdit_ = CreateChild<LineEdit>("LineEdit");
        lineEdit_->SetInternal(true);
    }

DefaultStyle.xml :

    <element type="StringControl" auto="true">
        <attribute name="Layout Mode" value="Horizontal" />
        <element type="LineEdit" internal="true">
            <attribute name="Min Size" value="50 24" />
            <attribute name="Vert Alignment" value="Center" />
        </element>
    </element>


    StringControl* control = uiGroup->CreateChild<StringControl>("RF_StringControl");
    control->SetStyleAuto();
    control->SetText("DefaultValueTextEdit");

Everything works pretty well apart from the text LineEdit that is hidden by default, you have to take the mouse to move the cursor position and finally see the text.

Is there a solution to solve this problem?

Apart from inheriting the StringControl class from LineEdit because this solution is not possible for FileControl for example.

NOTE : The origin of problem comes from this line not work : 
`<attribute name="Layout Mode" value="Horizontal" />`
So i understand why EditLine haven't width but why the SetLayoutMode is ignored ?

-------------------------

Leith | 2019-02-04 03:15:20 UTC | #2

I believe [SetTextAlignment](https://urho3d.github.io/documentation/1.4/class_urho3_d_1_1_text.html#a1582bfb8d06d3c7675681ed2475b8756) (HorizontalAlignment align) is what you are looking for in code - not sure what it looks like in xml but you can dump your UI to xml at runtime and find out.

-------------------------

AntiLoxy | 2019-02-04 12:19:30 UTC | #3

After some research I saw that it is LayoutMode which is not supported during the loading xml style in reality but I do not know why.

-------------------------

Leith | 2019-02-04 12:27:19 UTC | #4

LayoutMode tells how child elements will be aligned inside a parent, but there is also horizontal and vertical alignment per element - its not presented in the DefaultStyle.xml, but you can do it in code, and dump it to xml - and yes its a strange workflow, to write code that makes things, then dump it to disk just so you can load it again without that code in play. I am still without a working editor, and lazy, but I am wrapping my mind around the idea of dumping things to disk and loading them back in.

-------------------------

weitjong | 2019-02-04 13:07:05 UTC | #5

To avoid repeating myself again, search the forum for recent thread regarding UI. It should give some clues why styling does not work as expected in the constructor.

-------------------------

Modanung | 2019-02-04 14:59:46 UTC | #6

> Your search term is too short.

"ui style" _is_ long enough, but...
@weitjong Maybe bookmark that answer? :thinking:
...or append the docs?

-------------------------

weitjong | 2019-02-05 08:41:37 UTC | #7

https://urho3d.github.io/documentation/HEAD/_u_i.html

The docs explains the UI layout should be designed in XML and loaded. Using code to construct although is supported, it is cumbersome and prone for error, unless you study the inner working of UI subsystem. I believe what I have posted a few days ago in the other thread are more or less the same as the doc.

Edit: I agree to add a warning on the section when doing it programmatically, after I am back from my holiday.

-------------------------

AntiLoxy | 2019-02-05 17:36:15 UTC | #8

I'm sorry, this engine is awesome but i'm hurt with GUI system.
In my case, the style is set in xml, not loaded in constructor.
Style are loaded when i call SetStyleAuto() like any other UIElement subclass;

    <element type="StringControl" auto="true">
        <attribute name="Layout Mode" value="Horizontal" />
        <element type="LineEdit" internal="true">
        </element>
    </element>

StringControl :

    StringControl::StringControl(Context* context) : UIElement(context)
    {
    //    SetLayoutMode(LayoutMode::LM_HORIZONTAL);   WORK WITH THIS LINE !
        lineEdit_ = CreateChild<LineEdit>("LineEdit");
        lineEdit_->SetInternal(true);
    }

    void StringControl::RegisterObject(Context* context)
    {
        context->RegisterFactory<StringControl>();
        URHO3D_COPY_BASE_ATTRIBUTES(UIElement);
    }

I read some post but nothing helping to me.
When i watch some Urho3D UIElement source code i can see SetLayoutMode defined in c++ side.

-------------------------

Leith | 2019-02-08 06:15:08 UTC | #9

There is a way to dump a UI created at runtime (c++ or script) to xml file, and a way to set the layout mode - to find the proper xml we can manually set the layout mode on the element, dump the entire ui to xml file, and then look at the xml - sorry I have not done it because ui is the least of my current concerns, but this is the path to understanding

-------------------------

weitjong | 2019-02-23 05:06:31 UTC | #10

As promise I have added the warning in the doc and also x-ref it in the `SetStyle()` and `SetStyleAuto()` methods.

-------------------------

Leith | 2019-02-24 04:48:14 UTC | #11

Thanks man, it was one of the first silly bugs I had with UI, so I appreciate it being documented ;)

-------------------------

