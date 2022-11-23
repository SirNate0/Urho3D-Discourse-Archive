practicing01 | 2017-01-02 01:05:48 UTC | #1

Edit: If ListView->SetSelection() takes an unsigned index then why does E_ITEMSELECTED return an int according to UIEvents.h?
SetSelection() is crashing for me btw, index returned from E_ITEMSELECTED is correct.

Edit: I gave up and split the lists.  Items are not being highlighted when I click them though:
[img]http://img.ctrlv.in/img/15/07/04/55985a03e740d.png[/img]

Hello, I can add multiple Text* to a ListView but when I try to add multiple UIElement*, it only adds one entry.  Thanks for any help.

[code]
...
		SharedPtr<UIElement> serverInfo = ui_->LoadLayout(cache_->GetResource<XMLFile>("UI/serverInfo.xml"));
		((Text*)serverInfo->GetChild("serverName", true))->SetText(serverName);
		((Text*)serverInfo->GetChild("gameMode", true))->SetText(gameMode);
		((Text*)serverInfo->GetChild("address", true))->SetText(address);
		servers_.Push(serverInfo);

		((ListView*)gameMenu_->GetChild("serverList", true))->AddItem(serverInfo);
...
[/code]

-------------------------

