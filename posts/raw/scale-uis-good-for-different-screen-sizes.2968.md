miz | 2017-03-29 10:14:19 UTC | #1

Thought something like this would be good to be built into urho until then you can use this :)

only thing is you lose some sharpness for not whole number values of scale but I guess that's unavoidable

If you enter a Window and set recursive to true and set the scale to size of screen / size of screen it was designed for - it works really nicely

    void ScaleUIElement(UIElement * uiElement, float scale, bool recursive) 
    {
    	IntVector2 Size = uiElement->GetSize();
    	Size = IntVector2(Size.x_ * scale, Size.y_ * scale);
    	uiElement->SetSize(Size);
    	IntVector2 Position = uiElement->GetPosition();
    	Position = IntVector2(Position.x_* scale, Position.y_ * scale);
    	uiElement->SetPosition(Position);
    	if (dynamic_cast<TextEdit*>(uiElement) != NULL)
    	{
    		int fontSize = (dynamic_cast<TextEdit*>(uiElement))->GetFontSize();
    		dynamic_cast<TextEdit*>(uiElement)->SetFontSize(fontSize * scale);
    	}
    	if (dynamic_cast<Text*>(uiElement) != NULL)
    	{
    		int fontSize = (dynamic_cast<Text*>(uiElement))->GetFontSize();
    		Font *font = (dynamic_cast<Text*>(uiElement))->GetFont();
    		dynamic_cast<Text*>(uiElement)->SetFont(font, fontSize * scale);
    	}
    	if (dynamic_cast<Sprite*>(uiElement) != NULL)
    	{
    		IntVector2 hotspot = (dynamic_cast<Sprite*>(uiElement))->GetHotSpot();
    		hotspot = IntVector2(hotspot.x_ * scale, hotspot.y_ * scale);
    		dynamic_cast<Sprite*>(uiElement)->SetHotSpot(hotspot);
    	}
    	if (recursive)
    	{
    		Vector<SharedPtr<UIElement> > allChildren = uiElement->GetChildren();
    		for (int i = 0; i < allChildren.Size(); i++)
    		{
    			ScaleUIElement(allChildren[i], scale, true);
    			
    		}
    	}
    }

-------------------------

Enhex | 2017-03-29 17:21:18 UTC | #2

I did some related work in the past:
http://discourse.urho3d.io/t/ui-aspect-ratio-and-relative-font-size/1946

Still didn't reach adding it to Urho3D in my to do list.

-------------------------

artgolf1000 | 2017-04-03 03:57:39 UTC | #3

Thank you for sharing the code, I like it.

-------------------------

vivienneanthony | 2017-05-07 20:38:27 UTC | #4

There is a little hack. It should work basically, it accounts for X, Y. I'm not sure about fonts so I used the scaling of the screen height.


    void ScaleUIElement(UIElement * uiElement, float scaleX, float scaleY, bool recursive) 
    {
        // using Y since usually changes the most with text higher then longer
        float basefontScale = scaleY;
        
    	IntVector2 Size = uiElement->GetSize();
    	Size = IntVector2(Size.x_ * scaleX, Size.y_ * scaleY);
    	uiElement->SetSize(Size);
    	IntVector2 Position = uiElement->GetPosition();
    	Position = IntVector2(Position.x_* scaleX, Position.y_ * scaleY);
    	uiElement->SetPosition(Position);
    	if (dynamic_cast<TextEdit*>(uiElement) != NULL)
    	{
    		int fontSize = (dynamic_cast<TextEdit*>(uiElement))->GetFontSize();
    		dynamic_cast<TextEdit*>(uiElement)->SetFontSize(fontSize * basefontScale );
    	}
    	if (dynamic_cast<Text*>(uiElement) != NULL)
    	{
    		int fontSize = (dynamic_cast<Text*>(uiElement))->GetFontSize();
    		Font *font = (dynamic_cast<Text*>(uiElement))->GetFont();
    		dynamic_cast<Text*>(uiElement)->SetFont(font, fontSize * basefontScale );
    	}
    	if (dynamic_cast<Sprite*>(uiElement) != NULL)
    	{
    		IntVector2 hotspot = (dynamic_cast<Sprite*>(uiElement))->GetHotSpot();
    		hotspot = IntVector2(hotspot.x_ * scale, hotspot.y_ * scaleY);
    		dynamic_cast<Sprite*>(uiElement)->SetHotSpot(hotspot);
    	}
    	if (recursive)
    	{
    		Vector<SharedPtr<UIElement> > allChildren = uiElement->GetChildren();
    		for (int i = 0; i < allChildren.Size(); i++)
    		{
    			ScaleUIElement(allChildren[i], scale, true);
    			
    		}
    	}
    }

If I'm correct 


    // Base WIdth
    float baseWidth = 480.0f;
    float baseHeight = 853.0f;

    // Scaling Variables
    float scaleWidth = 1.0f;
    float scaleHeight = 1.0f;

    // Calculate scaling
    scaleWidth =  ScreenWidth /  BaseWidth < 1.0f ? scaleWidth = 1.0f : scaleWidth = scaleWidth;
    scaleHeight = ScreenHeight / BaseHeight < 1.0f ? scaleHeight = 1.0f : scaleHeight = scaleHeight;

Should pass the values you need

Vivienne

-------------------------

