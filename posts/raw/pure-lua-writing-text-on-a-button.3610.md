zakk | 2017-09-27 15:03:17 UTC | #1

Hello,

This time, i'm trying to put text on a button, in **UI** hierarchy.

I tried to start from the second sample (``02_HelloGUI.lua``).

I can see and click the button, but there is no text on it. I've browsed the Lua doc for finding method for writing text on a button (i guess it's ``.text`` property, but i'm not sure).


Can you help me ?

Here is the code of my modified sample:

<code>
function Start()

  graphics.windowTitle = "hello world"
  input.mouseVisible = true
  SubscribeToEvent("KeyUp",exit_test)

  local style = cache:GetResource("XMLFile", "UI/DefaultStyle.xml")
  ui.root.defaultStyle = style
  init_window()
  init_button()
end

function init_window()
  window = Window:new()
  ui.root:AddChild(window)
  window.minWidth = 384;
  window:SetLayout(LM_VERTICAL, 6, IntRect(66, 66, 66, 66))
  window:SetAlignment(HA_CENTER, VA_CENTER)
  window:SetName("Window")
end

function init_button()
  local button = Button:new()
  button:SetName("Button")
  button.minHeight = 44

---
  -- doesn't work
  local button_text = Text:new()
  button_text.text = "push me"
  button.text=button_text
-
  window:AddChild(button)
  button:SetStyleAuto()
end


function exit_test(eventType,eventData)
    local key = eventData["Key"]:GetInt()
    if key == KEY_ESCAPE then
      engine:Exit();
    end
end
</code>

Thank you for reading,
Zakk.

-------------------------

zakk | 2017-09-27 17:41:16 UTC | #2

Reading another sample (``40_Localization.lua``), i've found the solution :)

The trick is the text has to be a child of the button.

And the ``Text`` style must be applied to the text child.

>    \<element type="Text">                                                                                                                                                                                                         
>         \<attribute name="Font" value="Font;Fonts/Anonymous Pro.ttf" />                                                                                                                                                            
>         \<attribute name="Font Size" value="11" />                                                                                                                                                                                 
>         \<attribute name="Color" value="0.85 0.85 0.85" />                                                                                                                                                                         
>     \</element>

For the moment, i have not understood how to creaty the UI xml text file. Don't tell me everything must be done **by hand** ! :/ Because i can understand this for declarations like ``Text`` above, but what about that:

> \<element type="ProgressBar" style="BorderImage">                                                                                                                                                                              
>     \<attribute name="Size" value="16 16" />                                                                                                                                                                                   
>     \<attribute name="Image Rect" value="48 0 64 16" />                                                                                                                                                                        
>     \<attribute name="Border" value="4 4 4 4" />      
> (etc…)


Anyway , here is the correct code:

<code>

  local button = Button:new()
--  local button_text = Text:new()
  local button_text = button:CreateChild("Text", "text_for_button")
  button_text.text = "push me"
  button:SetName("Button")
  button.minHeight = 44
  button.text=button_text
  window:AddChild(button)
  button:SetStyleAuto()
  button_text:SetStyle("Text")
</code>

-------------------------

weitjong | 2017-09-27 23:36:57 UTC | #3

The provided editor has a rudimentary support for editing UI-layout.

-------------------------

