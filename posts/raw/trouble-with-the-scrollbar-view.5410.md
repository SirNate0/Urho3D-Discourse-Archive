codexhound | 2019-08-05 06:53:11 UTC | #1

So I have a snippet with the following code. Can't figure out why the loop elements always decide to put themselves at the bottom half of the window no matter what I have tried so far.

Here is how it looks in game. I want the part in the loop to start from the top but instead there is a big piece of the layout with nothing in it.
![window|388x437](upload://nnojzhTmluNaHPdzjZiuOM8vmr3.png) 

indent preformatted text by 4 spaces

                m_Window->SetMinWidth(384);
		m_Window->SetMinHeight(500);
		m_Window->SetMaxHeight(700);
		m_Window->SetLayoutSpacing(15);
		m_Window->SetLayout(LM_VERTICAL);
		m_Window->SetAlignment(HA_LEFT, VA_TOP);
		m_Window->SetResizable(true);
		m_Window->SetName("Window");

		// Create Window 'titlebar' container
		UIElement* titleBar = new UIElement(context_);
		titleBar->SetAlignment(HA_CENTER, VA_CENTER);
		titleBar->SetLayoutSpacing(3);
		titleBar->SetLayoutMode(LM_HORIZONTAL);

		// Create the Window title Text
		Text* windowTitle = new Text(context_);
		windowTitle->SetName("WindowTitle");
		windowTitle->SetText(String((m_sType + " " + m_sName).toStdString().c_str()));
		windowTitle->SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"), 30);
		windowTitle->SetColor(Color(.3, 0, .3));

		// Create the Window's close button
		Button* buttonClose = new Button(context_);
		buttonClose->SetName("CloseButton");

		// Add the controls to the title bar
		titleBar->AddChild(windowTitle);
		titleBar->AddChild(buttonClose);

		// Add the title bar to the Window
		m_Window->AddChild(titleBar);

		buttonClose->SetStyle("CloseButton");

		ScrollView* scrollArea = new ScrollView(context_);
		scrollArea->SetScrollBarsVisible(false, true);
		scrollArea->SetStyleAuto();
		m_Window->AddChild(scrollArea);

		UIElement* scrollContent = new UIElement(context_);
		scrollContent->SetLayoutMode(LM_VERTICAL);
		scrollContent->SetLayoutSpacing(10);
		scrollContent->SetAlignment(HA_CENTER, VA_TOP);
		scrollContent->SetStyleAuto();

		scrollArea->SetContentElement(scrollContent);

		float sliderValue = 1.0f / (float)m_InfrastructureMap.size();
		auto it = m_InfrastructureMap.begin();
		while (it != m_InfrastructureMap.end()) {
			UIElement* currentI = new UIElement(context_);
			currentI->SetLayoutMode(LM_HORIZONTAL);
			currentI->SetLayoutSpacing(10);
                        currentI->SetAlignment(HA_CENTER, VA_CENTER);
			scrollContent->AddChild(currentI);
                        .................
                        currentI->AddChild(text);
                        it++
                }
    indent preformatted text by 4 spaces

-------------------------

codexhound | 2019-08-05 21:18:19 UTC | #2

Finally saw that child added to the window previously had grown to a  weirdly large size so it was placing the next element way down in the window. Just had to set a max height on the child ui elements.

-------------------------

Sinoid | 2019-08-06 01:02:47 UTC | #3

Expect headaches when you first start using ComboBox UI elements. They're the trickest UI element to use (though I believe Weitjong added warning messages a year or more ago since people kept getting tripped up by combo-boxes).

-------------------------

