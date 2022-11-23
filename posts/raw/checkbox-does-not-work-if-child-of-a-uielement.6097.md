pldeschamps | 2020-04-19 10:43:49 UTC | #1

I need to organize my UI:
a checkbox on top left, the description on the right next to it
2 texts under
a button at the bottom
few texts over from left to right.

So I had the idea of creating UIElements:
a top canvas on top left, layoutmode vertical
a bottom canvas, at bottom of the screen, layout mode vertical
etc

If I add the checkbox to the UI.Root it works, but if I add it to the topCanvas UIElement, it does not work anymore...

C# code:
```
        private void CreateUI()
        {
            var topCanvas = new UIElement();
            topCanvas.LayoutMode = LayoutMode.Vertical;
            topCanvas.VerticalAlignment = VerticalAlignment.Top;
            topCanvas.HorizontalAlignment = HorizontalAlignment.Left;
            topCanvas.Name = "topCanvas";
            //topCanvas.SetStyleAuto(null);
            UI.Root.AddChild(topCanvas);

            showNamesCheckbox = new Urho.Gui.CheckBox();
            showNamesCheckbox.Name = "CheckBoxNames";
            showNamesCheckbox.Checked = true;
            showNamesCheckbox.VerticalAlignment = VerticalAlignment.Bottom;
            showNamesCheckbox.HorizontalAlignment = HorizontalAlignment.Right;
            showNamesCheckbox.SetDefaultStyle(style);
            showNamesCheckbox.SetColor(Urho.Color.Cyan);

            topCanvas.AddChild(showNamesCheckbox);
        }
```

-------------------------

throwawayerino | 2020-04-19 13:18:53 UTC | #2

You're not really supposed to directly use UIElement. Try using a Window instead to organise your screen elements

-------------------------

Lumak | 2020-04-19 16:46:57 UTC | #3

That looks like it should work, but I'm not sure about c# and not certain if it functions the same as c++.  What you might try is to create the checkbox as a child to topCanvas. I don't know the syntax in c# but c++ code would look something like:
```
CheckBox *mycb  = topCanvas->CreateChild<CheckBox>();
```
And no guarantee that'd work.  I created an UI repo a few years back with similar feature and then some.

-------------------------

