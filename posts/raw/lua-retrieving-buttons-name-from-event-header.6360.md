SuperVehicle-001 | 2020-08-31 23:12:59 UTC | #1

To cut right to the chase, I have these two snippets of Lua code. One of which generates three buttons to put in a menu window:
```
for i=1,3,1 do
	local button = Button:new()
	button.minHeight = 24
	button.name = i
	local buttonText = Text:new()
	buttonText.text = "Stage "..i
	buttonText:SetAlignment(HA_CENTER, VA_CENTER)
	window:AddChild(button)
	button:SetStyleAuto()
	button:AddChild(buttonText)
	buttonText:SetStyleAuto()
	SubscribeToEvent(button, "Released", "LoadStage")
end
```
and later on I have that event:
```
function LoadStage(object, eventType, eventData)
	log:Write(LOG_INFO, "Loaded stage "..object.name)
end
```
In theory, this should result in the log mentioning "*Loaded stage 1*", "*Loaded stage 2*" and "*Loaded stage 3*" when I press the appropiate button. However, it doesn't work properly and pressing the buttons results in an "*Execute Lua function failed: [string "init"]:61: attempt to concatenate field 'name' (a nil value)*" error in the log. Any help?

-------------------------

JTippetts1 | 2020-09-01 01:30:49 UTC | #2

An event handler has the signature of `HandleThingy(eventType, eventData)` so in your example, LoadStage is being passed a StringHash, then a VariantMap, and finally the one you call eventData is passed as nil. Inside, you are essentially trying to concatentate a field that resolves to StringHash::name, which there is no such thing.

In order to get the object sending the event, inside LoadStage you need to do something like:

`    function LoadStage(eventType, eventData)
        local e=eventData["Element"]:GetPtr("UIElement")
        local name=e:GetName()
        log:Write(LOG_INFO, "Loaded stage "..name)
    end
`

This will obtain the name of the UIElement sending the event.

-------------------------

SuperVehicle-001 | 2020-09-01 01:30:46 UTC | #3

Ah, I had misunderstood a few things then. Your solution works and also thanks for the explanation.

-------------------------

