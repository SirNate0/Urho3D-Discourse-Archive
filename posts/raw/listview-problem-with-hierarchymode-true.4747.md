AntiLoxy | 2018-12-15 01:47:55 UTC | #1

Hello, i have a problem with ListView only when SetHierarchy is set to true.
It display items on top of each other.

I set defaultstyle to root ui element, but problem still...

        auto* cache = GetSubsystem<ResourceCache>();
    auto* font = cache->GetResource<Font>("Fonts/Anonymous Pro.ttf");
    XMLFile* style = cache->GetResource<XMLFile>("UI/DefaultStyle.xml");

    auto title = SharedPtr<Text>(new Text(context_));
    title->SetText("File1");
    title->SetDefaultStyle(style);
    title->SetStyleAuto();
    title->SetInternal(true); // i tried without

    auto title2 = SharedPtr<Text>(new Text(context_));
    title2->SetText("File2");
    title2->SetDefaultStyle(style);
    title2->SetStyleAuto();
    title2->SetInternal(true); // i tried without

    auto* list = window->CreateChild<ListView>("WindowListView");
    list->SetHierarchyMode(true);
    list->SetFixedHeight(300);
    list->SetFixedWidth(300);
    list->SetDefaultStyle(style);
    list->SetStyleAuto();
    list->SetIndent(1);

    list->InsertItem(M_MAX_UNSIGNED, title);
    list->InsertItem(M_MAX_UNSIGNED, title2);

Thanks for any helps.

-------------------------

AntiLoxy | 2018-12-15 15:16:00 UTC | #3

Thank you, it works !
I did not realize that vertical positioning is manual.

-------------------------

AntiLoxy | 2018-12-18 00:57:02 UTC | #5

When item collapse, you need to reposition items... It's very strange, i think it's an issue

-------------------------

AntiLoxy | 2018-12-18 12:35:14 UTC | #7

No, look (a picture is more clear of words)
![Sans%20titre|301x187](upload://A3vqmHpD6tBy2xzMAQHzl0Vf3T1.png) 

When LayerBack is collapse, all next items must be repositioned.
I was try to call enableLayoutUpdate(); after each inserted item and avoid manual positionning but without success.

    void LocalWorldEditorState::updateListViewGraphScene(ListView* list, Node* node, 
     UIElement* parent)
    {
    if (parent == nullptr)
    {
        list->RemoveAllItems();
    }

    for (Node* child : node->GetChildren())
    {
        auto item = new Text(context_);
        item->SetText(child->GetName());
        item->SetName(child->GetName());
        item->SetFixedHeight(20);
        item->SetStyleAuto();
        item->SetPosition(0, list->GetNumItems() * 20);

        if (parent == nullptr)
        {
            list->InsertItem(M_MAX_UNSIGNED, item);
        }
        else
        {
            list->InsertItem(M_MAX_UNSIGNED, item, parent);
        }

        updateListViewGraphScene(list, child, item);
    }

    list->GetContentElement()->SetFixedHeight(list->GetNumItems() * 20);
    }

For my use-case, i need display nodes inside layers, like this :

LayerBack
 node01
 node02 
LayerMiddle
 node03
 node04
LayerTop
 node05
 node06

Maybe i will fallback to multiple listview without hierarchy mode.

-------------------------

AntiLoxy | 2018-12-18 22:14:31 UTC | #9

Ok, the SetLayout track is good in my opinion.
In the meantime, I import the XML layout bin/Data/UI/EditorHierarchyWindow.xml and then apply my update function as shown above, and it works.

    SharedPtr<UIElement> list = m_ui->LoadLayout(GetSubsystem<ResourceCache>()->GetResource<XMLFile>("UI/EditorHierarchyWindow.xml"));
    ListView* l = static_cast<ListView*>(list->GetChild("HierarchyList", true));

    l->SetFixedHeight(300);
    l->SetFixedWidth(300);

    updateListViewGraphScene(l, m_scene);

    m_ui->GetRoot()->AddChild(list);

I wonder if it is not better to create the interface from xml file only (make separation between visual & logic like HTML & JS.

![Sans%20titre|345x370](upload://hRAAnqAtMFkQ082uKa7BnVPN1YP.png)

Edit: for a complete solution with only C++ code add SetStyle("HierarchyListView"); to your element.

-------------------------

