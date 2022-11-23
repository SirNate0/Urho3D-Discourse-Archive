Mike | 2017-01-02 00:58:17 UTC | #1

I have trouble accessing/modifying values from loaded layouts:

[code]
	-- Load layout
	window = ui:LoadLayout(cache:GetResource("XMLFile", "UI/Master_Layout.xml"))
	ui.root:AddChild(window)

	-- Get 'Slider1' from layout and print its range
	local slider = window:GetChild("Slider1", true)
	print(slider.range)
[/code]
slider.range returns nil and doesn't update itself.

If I create the same slider from scratch (from code), I can access its values and it updates itself.

-------------------------

cadaver | 2017-01-02 00:58:18 UTC | #2

It seems that the exposed UIElement::GetChild() function is missing the same magic as Node::GetComponent(). It would need to inspect the UIElement and get its correct type. Now when you query a child, it's always returned to you as UIElement, with none of the subclasses' properties or functions.

-------------------------

cadaver | 2017-01-02 00:58:18 UTC | #3

Should be fixed in the master branch.

-------------------------

aster2013 | 2017-01-02 00:58:18 UTC | #4

you can use tolua.cast to cast wanted type.

-------------------------

Mike | 2017-01-02 00:58:18 UTC | #5

Many thanks, works perfectly.

I'll check tolua.cast, I remember that there is an example that uses it, thanks Aster.

As we are dealing with layouts, I have a question regarding saving layouts.
For now I use this kind of code, which works as expected:
[code]
window:SaveXML(fileSystem:GetUserDocumentsDir() .. "Master_Layout.xml")
[/code]
But the lua API includes a function for this:
SaveLayout(Serializer& dest, UIElement* element)

Is this function still relevant and if so how to use it (especially the Serializer& dest parameter) ?

-------------------------

