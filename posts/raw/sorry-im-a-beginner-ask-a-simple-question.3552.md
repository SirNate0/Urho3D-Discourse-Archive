spwork | 2017-09-10 14:58:34 UTC | #1

I use code create a button,and the button is not a button,it's a white square,so,how to create a button correctly or other UI element?

-------------------------

1vanK | 2017-09-10 14:58:58 UTC | #2

 example 02_HelloGUI

```
    // Load XML file containing default UI style sheet
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    XMLFile* style = cache->GetResource<XMLFile>("UI/DefaultStyle.xml");

    // Set the loaded style as default style
    uiRoot_->SetDefaultStyle(style);
```

```
button->SetStyleAuto();
```

-------------------------

spwork | 2017-09-10 12:14:42 UTC | #3

Thank you, master, I forget SetStyleAuto()

-------------------------

