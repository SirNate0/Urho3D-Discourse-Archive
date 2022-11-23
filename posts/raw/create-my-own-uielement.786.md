empirer64 | 2017-01-02 01:02:53 UTC | #1

Hello,
I would like to create my own UIElement inherited from Button, but when I try to do that I can not properly set the Style (XML style). It still remains white. I also tried to copy paste the whole Button code into my class (I just replaced the word Button with name MyElement) but it didnt work. Can someone please help me with this ?  :confused: 

BTW the code I used for testing MyElement should be correct because when I replace the word MyElement with the word Button, everything works ok.

-------------------------

weitjong | 2017-01-02 01:02:53 UTC | #2

Most probably that's because you have not created your own "stylesheet" that defines the auto style of your new UI-element class. Either that or you can just modify the existing "DefaultStyle.xml" stylesheet to define your new UI-element auto style. Alternatively, don't use SetStyleAuto() or any APIs that rely on it, instead set [b]ALL[/b] the attributes of your new UI-element instance explicitly from scratch. The latter is not recommended if you have many of such instances.

-------------------------

empirer64 | 2017-01-02 01:02:54 UTC | #3

[quote="weitjong"]Most probably that's because you have not created your own "stylesheet" that defines the auto style of your new UI-element class. Either that or you can just modify the existing "DefaultStyle.xml" stylesheet to define your new UI-element auto style. Alternatively, don't use SetStyleAuto() or any APIs that rely on it, instead set [b]ALL[/b] the attributes of your new UI-element instance explicitly from scratch. The latter is not recommended if you have many of such instances.[/quote]

I tried it using the first method by adding MyWidget to the DefaultStyle.xml but it does not work. I still get white widget. I also tried assigning working styles to it like widget->SetStyle("Button"). I really dont know whats wrong with it.

-------------------------

devrich | 2017-01-02 01:02:54 UTC | #4

[quote="empirer64"][quote="weitjong"]Most probably that's because you have not created your own "stylesheet" that defines the auto style of your new UI-element class. Either that or you can just modify the existing "DefaultStyle.xml" stylesheet to define your new UI-element auto style. Alternatively, don't use SetStyleAuto() or any APIs that rely on it, instead set [b]ALL[/b] the attributes of your new UI-element instance explicitly from scratch. The latter is not recommended if you have many of such instances.[/quote]

I tried it using the first method by adding MyWidget to the DefaultStyle.xml but it does not work. I still get white widget. I also tried assigning working styles to it like widget->SetStyle("Button"). I really dont know whats wrong with it.[/quote]


> [i]I would like to create my own UIElement inherited from Button, but when I try to do that I can not properly set the Style (XML style). It still remains white[/i]

( [u][i]disclaimer: this is all assumed on my part as I haven't worked with any uielements so far[/i][/u] ) I don't know if this helps as I haven't worked with uielements yet but just on initial looking around in the DefaultStyle.xml I noticed two parameters for every <element> "type" and "style".  It appears as though "type" is the custom name for your <element> and can be Any name you want it to be.  Whereas "style" if present represents the "type" of another <element> that you want 'your' <element> to inherit from.  if that <element> has it's own "style" parameter then that element will inherit from the other "style" parameter it has and so on..  if there is no "style" parameter then your <element> will not inherit from any other <element>

If that all holds true then I would assume you can fix your <element> by adding this to it's <element> tag

[code]style="Button"[/code]

or

[code]style="ButtonImage"[/code]

or you could just add this to the very begining of your DefaultStyle.xml file:

[code]<elements>
<element type="MyAwesomeImage">
<attribute name="Texture" value="Texture2D;Textures/MyAwesomeImageFileNameHere.png" />
</element>

<element type="empirer64CustomUIelement" style="MyAwesomeImage">
<attribute name="Size" value="16 16" />
<attribute name="Image Rect" value="16 0 32 16" />
<attribute name="Border" value="4 4 4 4" />
<attribute name="Pressed Image Offset" value="16 0" />
<attribute name="Hover Image Offset" value="0 16" />
<attribute name="Pressed Child Offset" value="-1 1" />
</element>
[/code]

Note that I just copied the attributes from the "Button" attributes like weitjong suggested for your new uielement "empirer64CustomUIelement".

Also note that I typed all that in by hand so hopefully there aren't any typos  :blush: 

Note that if you want to create a new uielement that would inherit from "empirer64CustomUIelement" then you would have that new <element>'s style attribute say:

[code]style="empirer64CustomUIelement"[/code]

to get somehting like this:

[code]<element type="MyNewUIelement" style="empirer64CustomUIelement">[/code]

@weitjong; did I get it right ?

-------------------------

weitjong | 2017-01-02 01:02:55 UTC | #5

Well, it is hard for me to say whether it is correct or not for the OP because I don't know the reason why he opts to subclass the Button class in the first place. We don't need to subclass the UI-Element if all we want is just a different styling. But otherwise, yes, I think you get the general idea.

-------------------------

empirer64 | 2017-01-02 01:02:55 UTC | #6

I want to create my own Button because I want to add text there. And yes I tried creating my own style in the defaultStyle.xml, I copied the Button Style and just renamed it to MyWidget, so I have there also the elements from which it should inherit the style. And MyWidget is just copied Button code with changed name from Button to MyWidget.

-------------------------

empirer64 | 2017-01-02 01:02:59 UTC | #7

Finaly I found out that it didnt work for me because I haven't Registered my new UIElement  :smiley: . Thank you guys for your help.

-------------------------

cadaver | 2017-01-02 01:02:59 UTC | #8

Using hierarchical composition would also be possible and actually used all over the Editor and other examples, ie. you create a Button and add a Text as a child element. When the child element has SetEnabled(false) (this is default for Text) it won't interfere with button press input.

-------------------------

