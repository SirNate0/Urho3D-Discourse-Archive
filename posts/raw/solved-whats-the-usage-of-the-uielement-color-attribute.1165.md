victorfence | 2017-01-02 01:05:49 UTC | #1

Hello everyone
I found the UIElement have a attribute named Color. This seems the setting of background color.

 [code]
 <element>
    <attribute name="Is Enabled" value="true" />
    <attribute name="Color" value="0.3 0.4 0.9 1" />
    <attribute name="Opacity" value="1" />
    <attribute name="Size" value="300 100" />
</element>
[/code]

I saw no background, just a placeholder, Can anyone give me some introduce about this?

-------------------------

victorfence | 2017-01-02 01:05:50 UTC | #2

[quote="Sinoid"]
Plain elements don't render. They're just layout / rational groupings. The element needs to be of some other type, such as BorderImage, in which case color is shorthand for setting all 4 corners. There are attributes for the individual corners if desired.[/quote]

I think you are right, BorderImage is the thing what I want, thank you so mush.

-------------------------

