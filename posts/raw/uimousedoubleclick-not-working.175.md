GIMB4L | 2017-01-02 00:58:38 UTC | #1

I have some text in the scene that I would like to have a UIMouseDoubleClick event on. I'm following the straightforward event setup structure, but it's still not working. Can UIMouseDoubleClicks be registered as events on Text elements?

-------------------------

friesencr | 2017-01-02 00:58:38 UTC | #2

I think the event is too dumb to care about what you are clicking on.  The procedure uses get element at(x,y) so make sure there is nothing in front of what you are double clicking on.  The event is sent from the element that was clicked on.  The buttons have to be the same as the last click within a period of time.

I did notice that I could not get a subscriber to get an event when they were subscribed to the control.

    SubscribeToEvent(window, "UIMouseDoubleClick", "HandleControlDoubleClicked");  <- doesn't work
    SubscribeToEvent("UIMouseDoubleClick", "HandleControlDoubleClicked"); <- works

-------------------------

weitjong | 2017-01-02 00:58:39 UTC | #3

I just check the code quickly, the "UIMouseDoubleClick" event is *only* being sent by UI subsystem, so that explains why below would never work. The sender of the event is not one of the UI-element derived classes' instance.
[code]SubscribeToEvent(window, "UIMouseDoubleClick", "HandleControlDoubleClicked"); <- doesn't work[/code]

-------------------------

friesencr | 2017-01-02 00:58:40 UTC | #4

I think it would make sense to have the element being clicked on also send the event.  Any opinions?

-------------------------

weitjong | 2017-01-02 00:58:40 UTC | #5

IMHO, it may be more intuitive in some cases to have the mouse click/doubleclick events to be sent by the element itself. Perhaps, we need another set of events defined for this, e.g.: E_CLICKED and E_DOUBLECLICKED. It is quite trivial to do this.

I think the existing E_UIMOUSECLICK and E_UIMOUSEDOUBLECLICK events should be left as they are because they are still useful for cases when one wants to have only a single handler to handle all the click events.

-------------------------

Azalrion | 2017-01-02 00:58:40 UTC | #6

Node events which were node specific but rethown by the scene had listeners added to them to replace being able to subscribe to things like E_NODECHANGED on a single node.

-------------------------

sirop | 2017-10-18 06:11:22 UTC | #7

Hallo.

I setup 3 events when creating an element of ListView:

    SubscribeToEvent(childList_.At(index).removeButton_,E_RELEASED, URHO3D_HANDLER(SplineEditor, HandleRemoveItemClicked));
    SubscribeToEvent(childList_.At(index).bodyElement_,E_ITEMCLICKED, URHO3D_HANDLER(SplineEditor, HandleItemMouseClicked));
    SubscribeToEvent(childList_.At(index).bodyElement_,E_ITEMDOUBLECLICKED, URHO3D_HANDLER(SplineEditor, HandleItemDoubleMouseClicked));

Only removeButton_ with E_RELEASED works, the other two events do not seem to trigger.

Code for HandleItemMouseClicked:

    void SplineEditor::HandleItemMouseClicked(StringHash eventType, VariantMap& eventData)
    {
        // Get control that was clicked
       Window* bodyElement = static_cast<Window*>(eventData[ItemClicked::P_ITEM].GetPtr());
       int index = listView_->FindItem(bodyElement);
       if (index!=M_MAX_UNSIGNED)
       {
          childList_[index].titleText_->SetColor(Color::MAGENTA);
          childList_[index].titleText_->SetText("SELECTED");
          childList_[index].bodyElement_->SetOpacity(0.9);
        
        // deselect the previous selection
          childList_[selectedIndex].titleText_->SetColor(Color::WHITE);
          childList_[selectedIndex].bodyElement_->SetOpacity(0.4);
        
          selectedIndex = index;
      }
    
    // Just for debugging
      listView_->RemoveItem(8);
      childList_.Erase(8);
      for (int i= 8; i<listView_->GetNumItems(); i++)
      {
          childList_[i].titleText_->SetText(childList_[i].titleText_->GetText().Split(' ')[0] + String(' ') + String(i+1));
      }
    }
![listview2|244x333](upload://lq057m4Lk2mmp4L8AUGvoCjDrvS.png)

Is there anything I misunderstood?
Thanks.

-------------------------

Eugene | 2017-10-18 08:15:00 UTC | #8

Always re-check event sender before writing code.

-------------------------

sirop | 2017-10-18 08:52:46 UTC | #9

Thanks for your answer, but what do you mean exactly?

I just looked at https://github.com/urho3d/Urho3D/blob/1.7/Source/Urho3D/UI/ListView.cpp#L994 ?

Shoudl the ListView be explicitly set to be editable? Just did that, but it did not help.

-------------------------

Eugene | 2017-10-18 08:57:19 UTC | #10

[quote="sirop, post:9, topic:175"]
what do you mean exactly?
[/quote]

I mean that E_ITEMCLICKED is send from ListView
It's not obvious from your code what's the list.

-------------------------

sirop | 2017-10-18 09:28:15 UTC | #11

You are right. Now with the sender changed to ListView  everything works.

-------------------------

