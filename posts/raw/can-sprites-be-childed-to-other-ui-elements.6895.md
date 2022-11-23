evolgames | 2021-06-15 01:47:29 UTC | #1

I've been trying to figure out how to get sprites on windows and other ui elements. If I child a sprite image texture to some ui element, it simply doesn't show up. Am I missing something or is this not possible? I can get them to appear by making them children of the ui.root but only with that. In my case, I need sprites in a scrolling content window, and so they can't be arbitrarily placed on the screen but must be within that content.

-------------------------

Lys0gen | 2021-06-15 03:40:48 UTC | #2

It is possible, I have a ScrollView that I add sprites to and it works fine. Got some code to look at?

-------------------------

evolgames | 2021-06-15 03:56:22 UTC | #3

Well that's good news.

Here's the main part. Kind of a mess but you should get the idea. I add text from a table of "blocks" and I'd like to generate a sprite there too that will scroll with that text and other content. Currently I have the sprites spaced out to *fit*, though this won't let me scroll since the sprites will just stay in place.

![Screenshot_2021-06-14_23-54-34|690x388](upload://nfhRlQAQHXTfrb04cECPT2kddGH.png)


```
function MakeBuildMenu()

	CreateHoverDialog()
	CreateColorMenu()

	partwindowmenu=true
	partwindowtext=nil
	partwindowtext={}
	_scrollV = ScrollView:new()
    _scrollV:SetStyleAuto(hudStyleNoWindowBacking);
    _scrollV:SetSize(menuSize,graphics.height)
    _scrollV:SetPriority(10)
    _scrollV:SetEnabled(true)
    _scrollV:SetScrollBarsVisible(false, true)  

    partwindow = UIElement:new()
    partwindow.minWidth = menuSize
    partwindow:SetLayout(LM_VERTICAL, 6, IntRect(6, 6, 6, 6))
    partwindow:SetName("bWindow")
    partwindow:SetStyleAuto(hudStyleNoWindowBacking)
    partwindow:SetVisible(true)
    partwindow:SetPriority(2)
    partwindow:SetAlignment(HA_LEFT, VA_TOP)

    ui.root:AddChild(_scrollV)
    _scrollV:AddChild(partwindow)
    ui.root:AddChild(partwindow)
   
    local box = UIElement:new()
    box:SetMinSize(0, 24)
    box.layoutMode = LM_HORIZONTAL
    box:SetAlignment(HA_CENTER,VA_TOP)
    partwindow:AddChild(box)
    partwindow:SetOpacity(pl.opacity)
    partwindowtext[#partwindowtext+1] = Text:new()
    partwindowtext[#partwindowtext].text = "\n     Parts"
    partwindowtext[#partwindowtext]:SetFont(cache:GetResource("Font", "Fonts/LeagueSpartan-Bold.otf"), 15)
    box:AddChild(partwindowtext[#partwindowtext])
		local spacer = UIElement:new()
		spacer:SetMinSize(400, 80)
		spacer.layoutMode = LM_HORIZONTAL
		spacer:SetAlignment(HA_CENTER,VA_TOP)
		partwindow:AddChild(spacer)

	for i=1,#blocks do
		local lbox = UIElement:new()
		lbox:SetMinSize(400, 77*i)
		lbox.layoutMode = LM_HORIZONTAL
		lbox:SetAlignment(HA_CENTER,VA_TOP)
		partwindow:AddChild(lbox)

		partwindowtext[#partwindowtext+1] = lbox:CreateChild("Text")
		partwindowtext[#partwindowtext].name = 1
		partwindowtext[#partwindowtext]:SetStyleAuto(uiStyle)
		partwindowtext[#partwindowtext]:SetEnabled(true)
		partwindowtext[#partwindowtext]:SetVerticalAlignment(VA_CENTER)
		partwindowtext[#partwindowtext]:SetFontSize(15)
		partwindowtext[#partwindowtext].text = blocks[i].name
		SubscribeToEvent(partwindowtext[#partwindowtext], "Click",
			function (eventType, eventData)
				--ConfirmBlock()
				AddBlock(i,pl.buildPosition)
			end)
		SubscribeToEvent(partwindowtext[#partwindowtext], "HoverBegin",
			function (eventType, eventData)
				--PlaySound("hover","cut")
			end)

		local logoTexture = blocks[i].texture
		logoTexture:SetFilterMode(FILTER_BILINEAR)
		local testSprite = ui.root:CreateChild("Sprite")
		testSprite:SetTexture(logoTexture)
		testSprite:SetPosition(100,60 + 120*i)
		testSprite:SetStyleAuto()
		testSprite:SetVisible(true)
		testSprite:SetEnabled(true)
		testSprite:SetPriority(105)
		local textureWidth = logoTexture.width
		local textureHeight = logoTexture.height
		testSprite:SetScale(80 / textureWidth)
		testSprite:SetSize(textureWidth, textureHeight)
		testSprite.hotSpot = IntVector2(textureWidth, textureHeight)
				SubscribeToEvent(testSprite, "Click",
			function (eventType, eventData)
				--ConfirmBlock()
				AddBlock(i,pl.buildPosition)
			end)
	end
	
	 SubscribeToEvent(_scrollV, "ViewChanged",
        function (eventType, eventData)
			local y = eventData["Y"]:GetInt()
			ui.focusElement=_scrollV
			testSprite:SetPosition(testSprite:GetPosition().x,testSprite:GetPosition().y+y) 
        end)

   
 
	_scrollV:SetContentElement(partwindow)
	_scrollV:SetViewPosition(0,0)
```

-------------------------

Lys0gen | 2021-06-15 04:12:30 UTC | #4

Ok, couple of things that might help:

1. Try using SetFixedSize(..) instead of SetSize(..). I don't know exactly why but for me it was necessary (now that I think about it I think I also spent more than an hour playing with defines to get my sprite to show up. The UI system has a lot of quirks that I still don't understand after a year of using it.)
2. If that isn't enough, try defining SetImageRect(..) and perhaps do SetStyleAuto() directly after creating the object
3. You don't seem to need to rotate the image? In that case you could just make it a BorderImage element instead?

-------------------------

evolgames | 2021-06-15 04:23:50 UTC | #5

Thanks for the ideas. None of them seem to work, though. I agree about the UI system. Took me a while to figure out I had to do SetEnabled(true) to be able to subscribe to click events on sprites.

-------------------------

Lys0gen | 2021-06-15 11:30:59 UTC | #6

Strange. Maybe also try setting a fixed size on the content/list element?

Anyway, here is everything I am doing to the element, maybe I overlooked something important that is missing on your side. You did change it from adding to the root to the content element, yes?


                    spriteItem->SetStyleAuto();
                    spriteItem->SetPriority(contentElement->GetPriority()+1);
                    spriteItem->SetImageRect(textureDimensions);
                    spriteItem->SetPosition(pX, pY);
                    spriteItem->SetFixedSize(itemWidth, itemHeight);
                    spriteItem->SetHotSpot(spriteItem->GetWidth()*0.5, spriteItem->GetHeight()*0.5);
                    spriteItem->SetRotation(atan2(endPosition.y_-startPosition.y_, endPosition.x_-startPosition.x_) * RAD_TO_DEG);
                    spriteItem->SetColor(itemColor);
                    spriteItem->SetOpacity(1.0);

                    contentElement->AddChild(spriteItem);

-------------------------

evolgames | 2021-06-16 03:53:09 UTC | #7

Oh man I really thought this would work but I'm still not getting it

-------------------------

SirNate0 | 2021-06-16 18:31:07 UTC | #8

What happens if you make the box larger, maybe 500x500 fixed size? I.e. instead of this:

> `box:SetMinSize(0, 24)`

-------------------------

