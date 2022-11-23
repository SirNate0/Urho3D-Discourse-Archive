arpo | 2018-07-02 12:29:23 UTC | #1

My code looks like this. 

	SubscribeToEvent(E_ITEMSELECTED, URHO3D_HANDLER(HelloGUI, HandleControlSelected));

----

	void HelloGUI::HandleControlSelected(StringHash eventType, VariantMap &eventData)
	{

			auto *el = static_cast<DropDownList *>(eventData[UIMouseClick::P_ELEMENT].GetPtr());
			
			if (el) {
					
					
					TypeInfo info = *el->GetTypeInfo();
					String type = info.GetTypeName();
					Log::Write(LOG_INFO, type);
					
			}
	}

Where do I go from here?

-------------------------

arpo | 2018-07-02 14:33:22 UTC | #2

I did solve it. For anyone else looking for the same answer. Here’s my solution to watch UI elements and how to fetch their info.

First setup some event listeners

    SubscribeToEvent(E_UIMOUSECLICK, URHO3D_HANDLER(HelloGUI, eventManager));
    SubscribeToEvent(E_SLIDERCHANGED, URHO3D_HANDLER(HelloGUI, eventManager));
    SubscribeToEvent(E_ITEMSELECTED, URHO3D_HANDLER(HelloGUI, eventManager));
    SubscribeToEvent(E_FOCUSED, URHO3D_HANDLER(HelloGUI, eventManager));
    SubscribeToEvent(E_DEFOCUSED, URHO3D_HANDLER(HelloGUI, eventManager));

Then add the eventManager

	void HelloGUI::eventManager(StringHash eventType, VariantMap &eventData)
	{
			auto *el = static_cast<UIElement *>(eventData[UIMouseClick::P_ELEMENT].GetPtr());
			

			if (el) {
					
					String name = el->GetName();
					String evName = "";
					String value = "";
					TypeInfo info = *el->GetTypeInfo();
					String type = info.GetTypeName();
					bool fireEvent = false;
					
					if(E_FOCUSED == eventType) {
							evName = "FOCUS";
					} else if(E_DEFOCUSED == eventType) {
							evName = "BLUR";
					} else if(E_UIMOUSECLICK == eventType) {
							evName = "CLICK";
					} else if(E_SLIDERCHANGED == eventType) {
							evName = "SLIDE";
					} else if(E_ITEMSELECTED == eventType) {
							evName = "ITEMSELECTED";
					}
					
					if(type == "LineEdit" && (evName == "BLUR" || evName == "FOCUS")) {
							LineEdit *lineEl = static_cast<LineEdit *>(el);
							value = lineEl->GetText();
							fireEvent = true;
					} else if(type == "Slider" && evName == "SLIDE") {
							using namespace SliderChanged;
							float valueFloat = eventData[P_VALUE].GetFloat();
							value = String(valueFloat);
							fireEvent = true;
					} else if(type == "Button" && evName == "CLICK") {
							fireEvent = true;
					} else if(type == "DropDownList" && evName == "ITEMSELECTED") {
							
							DropDownList *ddEl = static_cast<DropDownList *>(el);
							unsigned ddIndex = ddEl->GetSelection();
							value = String(ddIndex);
							fireEvent = true;
							
					} else if(type == "CheckBox" && evName == "CLICK") {
							auto* box = static_cast<CheckBox*>(eventData[Toggled::P_ELEMENT].GetPtr());
							bool checked = box->IsChecked();
							value = String(checked);
							fireEvent = true;
					}
					
					if(fireEvent) {
							Log::Write(LOG_INFO, evName + ": " + name + " " + type + " " + value);
					}

					
			}
			
	}

-------------------------

