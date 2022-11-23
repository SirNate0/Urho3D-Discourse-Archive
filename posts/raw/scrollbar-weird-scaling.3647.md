sirop | 2017-10-10 20:49:34 UTC | #1

Hello.

There are some themes already discussed about ListView or ScrollView. And I looked them through.
However I do not understand my case where the scrollbar of a ListView element is scaled to occupy the whole size of its parent.
My snippets:

Creating ListView:

    listView_ = CreateChild<ListView>();
    listView_->SetLayout(LM_VERTICAL, 6, IntRect(6, 6, 6, 6));
    listView_->SetAlignment(HA_LEFT, VA_TOP);
    listView_->SetMinSize(100, listView_->GetParent()->GetHeight());
    listView_->SetMaxWidth(listView_->GetParent()->GetHeight()*0.7f);
    listView_->SetMultiselect (false);
    listView_->SetHighlightMode(HighlightMode::HM_ALWAYS);
    listView_->SetStyle("ListView", cache->GetResource<XMLFile>("UI/DefaultStyle.xml"));
    listView_->SetStyleAuto();


Adding elements to ListView:
   
    ListElement listElem;
    
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    
    Window *element = new Window(GetContext()); //content_->CreateChild<Window>(); //// new UIElement(this->GetContext());
    listElem.bodyElement_ = element;
    element->SetLayoutBorder(IntRect(5,5,5,5));
    element->SetLayoutMode(LM_VERTICAL);
    element->SetLayoutSpacing(2);
    element->SetMaxHeight(80);
    element->SetWidth(listView_->GetWidth()*0.8f);
    element->SetStyleAuto();
    // listView_->InsertItem(index, element);
      
    
    // Create the Window title Text
    listElem.titleBar_ = element->CreateChild<UIElement>();
    ...    
    listElem.titleText_ = listElem.titleBar_->CreateChild<Text>();
    ...    
    listElem.removeButton_ = listElem.titleBar_->CreateChild<Button>()
    ...    
    listElem.textVector3_ = element->CreateChild<Text>(); 

    listElem.titleBar_->SetStyleAuto();
    listElem.titleText_->SetStyleAuto();
    listElem.removeButton_->SetStyle("CloseButton");
    listElem.textVector3_->SetStyleAuto();
    
    //listView_->InsertItem(index, element);
    listView_->AddItem(element);
    

![listview|241x340](upload://dIq2MBO2XZ33me8EfdqySvcouUG.jpg)

-------------------------

Eugene | 2017-10-11 03:03:34 UTC | #2

I faced exactly the same issue with `ScrollView`.
Do **not** call `AddChild`, `SetLayout` or other behavior-important `UIElement` methods for compound UI elements like `ListView`, `ScrollView` and so on.

-------------------------

sirop | 2017-10-11 03:06:55 UTC | #3

Indeed commenting out the second line

          listView_ = CreateChild<ListView>();
          // listView_->SetLayout(LM_VERTICAL, 6, IntRect(6, 6, 6, 6));
          listView_->SetAlignment(HA_LEFT, VA_TOP);
          listView_->SetMinSize(100, listView_->GetParent()->GetHeight());
          listView_->SetMaxWidth(listView_->GetParent()->GetHeight()*0.7f);
          listView_->SetMultiselect (false);
          listView_->SetHighlightMode(HighlightMode::HM_ALWAYS);
          listView_->SetStyle("ListView", cache->GetResource<XMLFile>("UI/DefaultStyle.xml"));
          listView_->SetStyleAuto();

solved it:

![listview2|244x335](upload://9XuKuqyL0kjgFOIwMlmbAuVgPDT.png)

-------------------------

