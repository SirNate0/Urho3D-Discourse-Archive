AntiLoxy | 2019-01-20 22:00:31 UTC | #1

Hello, I encounter a problem when creating a ScrollView in the constructor of a window subclass.
My code works fine if I create the ScrollView elsewhere than in the constructor.

    NodeWindow::NodeWindow(Context* context) : Window(context), node_(nullptr)
    {
        SetStyleAuto();

        ScrollView* scroll = CreateChild<ScrollView>();
        scroll->SetFixedSize(300, 100);
        scroll->SetStyleAuto();

        UIElement* sections = new UIElement(context_);
        sections->SetFixedWidth(300);
        sections->SetLayoutMode(LayoutMode::LM_VERTICAL);
        sections->SetStyleAuto();

        for (unsigned int i = 0; i < 10; i++)
        {
            ButtonText* btn = sections->CreateChild<ButtonText>("g");
            btn->SetLabel("Button");
        }

        scroll->SetContentElement(sections);
    }

With this version, the scrollview is empty.
When i move this code to a method called after construction, everything work fine.

    nodeWindow_ = uiRoot_->CreateChild<NodeWindow>("NodeWindow");
    nodeWindow_->Init();

This work, but it's not a valid solution, so i need help :) thanks.

-------------------------

weitjong | 2019-01-21 00:56:58 UTC | #2

https://discourse.urho3d.io/t/hotkey-control-based-on-lineedit/4501/12?u=weitjong

This should give you a clue why it did not work in your constructor. Your parent window was still “detached” at the time you tried to apply the style, so the UI subsystem did not know which style sheet to use. Thus, you ended up with “naked” UI elements.

-------------------------

Leith | 2019-01-21 08:29:38 UTC | #3

That's very useful information!

I have not run into this problem myself, since I tend to initialize outside of my constructors, but I am sure I would eventually have run into this one ;)

-------------------------

AntiLoxy | 2019-01-21 17:05:51 UTC | #4

Okay, after your explanation i try to review the code:

    NodeWindow::NodeWindow(Context* context) : Window(context), node_(nullptr)
    {
        titleBar_ = CreateChild<UIElement>("NW_TitleBar");
        titleText_ = titleBar_->CreateChild<Text>("NW_TitleText");
        closeButton_ = titleBar_->CreateChild<Button>("NW_CloseButton");
        scroll_ = CreateChild<ScrollView>();
        scroll_->SetFixedSize(300, 100);

        sections_ = new UIElement(context_);
        sections_->SetFixedWidth(300);
        sections_->SetLayoutMode(LayoutMode::LM_VERTICAL);

        for (unsigned int i = 0; i < 10; i++)
        {
            ButtonText* btn = sections_->CreateChild<ButtonText>("g");
            btn->SetLabel("Button");
        }

        scroll_->SetContentElement(sections_);
    }

    void NodeWindow::Init()
    {
        SetStyle("NodeWindow");
        titleBar_->SetStyle("WindowTitleBar");
        titleText_->SetStyle("NodeWindowTitleText");
        sections_->SetStyleAuto();
        closeButton_->SetStyle("CloseButton");
        scroll_->SetStyleAuto();
    }

    uiRoot_->SetDefaultStyle(GetSubsystem<ResourceCache>()->GetResource<XMLFile>("UI/DefaultStyle.xml"));
    nodeWindow_ = uiRoot_->CreateChild<NodeWindow>("NodeWindow");
    nodeWindow_->Init();

TitleBar work fine, but ScrollView still empty :transpiration:
However, NodeWindow know the correct XML file style when i call Init();

-------------------------

weitjong | 2019-01-22 03:46:05 UTC | #5

You still missing the point.

-------------------------

AntiLoxy | 2019-01-22 17:06:44 UTC | #6

Ok, can you tell me more please? I think it can also be useful for other people. I specify that my problem only concerns the scrollbar, the other elements are loaded correctly (their styles too),

Note: My custom UIElement is also registered.

-------------------------

weitjong | 2019-01-23 13:39:11 UTC | #7

I was quite busy in office yesterday, so I am sorry that my short message was not useful.

Remember that all the descendant of `UIElement` inherits the `SetDefaultStyle()` method. So, you can call this method as early as possible in your parent window's constructor (just like you do for UI root) before adding its children. That should fix most of the issue with styling.

There is actually also nothing wrong with your revised code too. You can skip the styling during the object construction, and only applying the style later after adding the parent to the UI hierarchy. Why it did not work for `ScrollView` can be considered as a bug, IMHO. This UI-element class contains a few internal sub UI-elements, but it does not override the `SetStyle()` method to take care of those sub UI-elements. In other words, I suspect the code `scroll_->SetStyleAuto();` might not do what it supposes to do.

-------------------------

weitjong | 2019-01-23 16:05:00 UTC | #8

Come to think about it. The problem is analogous to someone else uses your `NodeWindow` class and just calls `NodeWindow::SetStyleAuto()` and expects that call would do what your `Init()` method does.

-------------------------

AntiLoxy | 2019-01-23 22:19:19 UTC | #9

Thank you for your complete answer :)
I found solution that seems to me to be flexible and practical for the declaration of styles.

    NodeWindow::NodeWindow(Context* context) : Window(context)
    {
        titleBar_ = CreateChild<UIElement>("NW_TitleBar");
        titleText_ = titleBar_->CreateChild<Text>("NW_TitleText");
        closeButton_ = titleBar_->CreateChild<Button>("NW_CloseButton");

        scroll_ = CreateChild<ScrollView>();
        scroll_->SetScrollBarsVisible(false, true);
    }

    void NodeWindow::SetStyle(const String& styleName)
    {
        Window::SetStyle(styleName);
        titleBar_->SetStyle(styleName + "TitleBar");
        titleText_->SetStyle(styleName + "Title");
        closeButton_->SetStyle("CloseButton");
        scroll_->SetStyle(styleName + "Scroll");

        styleName_ = styleName;
    }

    void NodeWindow::SetStyleAuto()
    {
        SetStyle(GetTypeName());
    }

    UIElement* NodeWindow::CreateComponentSection(Component* component)
    {
        UIElement* section = new UIElement(context_);
        section->SetStyle(styleName_ + "Section"); // can be useful to set style to dynamic loaded ui element.
    }

Sample of my DefaultStyle.xml

    <element type="NodeWindow" style="Window">
        <attribute name="Min Size" value="400 300" />
        <attribute name="Is Movable" value="true" />
        <attribute name="Layout Mode" value="Vertical" />
        <attribute name="Layout Spacing" value="6" />
        <attribute name="Layout Border" value="6 6 6 6" />
    </element>
    <element type="NodeWindowTitleBar">
        <attribute name="Min Size" value="400 20" />
        <attribute name="Max Size" value="400 20" />
        <attribute name="Layout Mode" value="Horizontal" />
    </element>
    <element type="NodeWindowTitle" style="Text">
        <attribute name="Text" value="Node Window" />
    </element>
    <element type="NodeWindowScroll" style="ScrollView">
        <attribute name="Max Size" value="400 300" />
    </element>

The thing a bit unfortunate with this method is that the dynamic elements will not be affected by possible later changes of styles.

If this solution seems to be in agreement with the engine then it would be nice:
- Set SetStyle as virtual function
- Add GetStyleName () to UIElement to avoid styleName_ member.

-------------------------

weitjong | 2019-01-26 15:01:46 UTC | #10

I am afraid your approach at best can only be considered as a workaround, when you insist to create the UI-element by code and also by doing styling at later time instead of at the time the UI-element is being added as child. If you look carefully how the "ScrollView" default style is being defined in the Editor's style sheet file then you should realize that its definition has nested XML elements, i.e. each sub UI-element has its own nested element section. The problem is, I believe, the current implementation of UIElement::SetStyle() (when being called at later time) does not do the right thing to use those nested definition. It only uses those correctly when the child insertion/addition and styling are done together at the same time.

This is not a big problem, at least to me, because given chance to choose then I would prefer to use the Editor to design the UI layout than to design the UI by code. Add the UI-elements, apply the style, adjust the attributes further more all in the editor,  and when it looks great then save the layout as another XML file which I can then load in the code with a single line of code. Most the windows, if not all, in the Editor itself are loaded using XML layout files in this manner.

-------------------------

Leith | 2019-01-25 03:43:39 UTC | #11

Editor on Linux is quite unstable, and prone to crashing, with no errors reported.
In particular, this happens when I have loaded a scene from xml file I saved in my application, which contains components unknown to the editor - my scene loads, I can see it, and moving the mouse around shows the bounding boxes and so on, but if I left click on something in the scene, the editor crashes.
For this reason, I find the editor completely useless, have avoided and will avoid using it, damn it would be faster for me to recreate enough of it in a language I can debug.

-------------------------

weitjong | 2019-01-25 08:33:24 UTC | #12

The editor crashing issue is off-topic here, but it is already being tracked in our issue tracker.

https://github.com/urho3d/Urho3D/issues/2384

-------------------------

