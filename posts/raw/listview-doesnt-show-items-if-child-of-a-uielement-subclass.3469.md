TheComet | 2019-05-23 13:20:02 UTC | #1

This has been super frustrating for me and I hope someone can help.

Here is a minimal working example:

    void MyApplication::Start()
    {
        ResourceCache* cache = GetSubsystem<ResourceCache>();
        UI* ui = GetSubsystem<UI>();
        ui->GetRoot()->SetDefaultStyle(cache->GetResource<XMLFile>("UI/DefaultStyle.xml"));

        UIElement* container = new UIElement(context_);
        container->SetStyleAuto();
        container->SetLayoutMode(LM_VERTICAL);
        container->SetLayoutSpacing(5);
        ui->GetRoot()->AddChild(container);

        ListView* view = new ListView(context_);
        view->SetStyleAuto();
        container->AddChild(view);

        LineEdit* edit = new LineEdit(context_);
        edit->SetFixedHeight(20);
        edit->SetStyleAuto();
        edit->SetFocusMode(FM_FOCUSABLE);
        container->AddChild(edit);

        Text* text = new Text(context_);
        text->SetText("This is a test");
        text->SetStyleAuto();
        view->AddItem(text);
        view->UpdateLayout();

        container->SetSize(200, 200);
    }

Looks like this (as expected):

![1|225x209](upload://8Y1tpA1nX2AxibLeOgPK5SsvpPm.png)

Now, watch what happens when I refactor that stuff out into a subclass of UIElement:

    class DoesntWork : public UIElement
    {
    public:
        DoesntWork(Context* context) : UIElement(context) {
            SetLayoutMode(LM_VERTICAL);
            SetLayoutSpacing(5);

            ListView* view = new ListView(context_);
            view->SetStyleAuto();
            AddChild(view);

            LineEdit* edit = new LineEdit(context_);
            edit->SetFixedHeight(20);
            edit->SetStyleAuto();
            edit->SetFocusMode(FM_FOCUSABLE);
            AddChild(edit);

            Text* text = new Text(context_);
            text->SetText("This is a test");
            text->SetStyleAuto();
            view->AddItem(text);
            view->UpdateLayout();
        }
    };

    void MyApplication::Start()
    {
        ResourceCache* cache = GetSubsystem<ResourceCache>();
        UI* ui = GetSubsystem<UI>();
        ui->GetRoot()->SetDefaultStyle(cache->GetResource<XMLFile>("UI/DefaultStyle.xml"));

        UIElement* container = new DoesntWork(context_);
        container->SetStyleAuto();
        ui->GetRoot()->AddChild(container);
       container->SetSize(200, 200);
    }

It's practically the same code, yet:

![2|212x208](upload://pLu2MXJW3rJQRUFr7FwkEb82DST.png)

Where is the text?

No matter what I try, I cannot for the life of me get the items in the list view to appear. They're just gone.

-------------------------

Enhex | 2017-08-20 22:05:40 UTC | #2

I remember I had a problem when trying to derive from UIElement.
When working on a recent UI PR, I noticed I had to use `URHO3D_COPY_BASE_ATTRIBUTES(UIElement);` in the RegisterObject() function for the class that derives from UIElement for it to work properly (built in UI classes that derive from UIElement do it too, ex. Text and BorderImage).
You could try that and see if it helps, kinda makes sense since style uses properties (didn't test your code myself).

-------------------------

lezak | 2017-08-21 08:17:35 UTC | #3

I've tried Your code and it worked after manually setting style of Text - that means replacing:
`text->SetStyleAuto();` 
with 
`text->SetStyle("Text", GetSubsystem<ResourceCache>()->GetResource<XMLFile>("UI/DefaultStyle.xml"));`

One more thing, You should mark all created elements as internal.

-------------------------

Enhex | 2017-08-21 09:08:07 UTC | #4

[UIElement::SetStyleAuto()](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_u_i_element.html#a08c4fe55c45b8ef00abc7297ebdca382) uses whatever you set with [UIElement::SetDefaultStyle()](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_u_i_element.html#a387ce2e545031cc9e4d4cfa82772f38b).
You can set a default style for the [UI's root element](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_u_i_element.html#a696f2c9d35d4b2e262b2c666bceda61f) to have a global default.

-------------------------

slapin | 2017-08-21 12:18:25 UTC | #5

Interesting.

For me I was not able to make some more complex widgets like ListView or DropDownList work as intended
there are too many moving targets and simply bad design.
Each time I had to struggle and had to find out exact conditions for a widget to run - not a good way to spend my precious time.
So I found the solution - I can represent each list widget as UIElement of UIElements of simple widgets
like Text or Button. It is very simple and requirements are always the same, everything is stable and predictable. First - for all widgets, for each one, run SetStyle/SetStyleAuto. Widgets react differently
to no style setting and you will have hard time distinguishing what is going on.
For each UIElement set SetLayout() (e.g. SetLayout(LM_VERTICAL, 10, 10, 10, 10)).
Set your min/max height/width depending on parent layout for each widget.
Don't forget to set layout on your top-level widget too.

So for me I found the following basic rules when using Urho3D GUI most effectively:
1. Never consider Urho3D UI system as end-user widget system - that is a set of building blocks to
implement your widget system with, not more.
2. Don't use complex widgets - nobody can tell you what are they made of and how they work,
so you will be on your own here. Developers don't know, too.
3. The system is very flexible so you can implement your stable widgets very quickly,
but is also very verbose, so it is better to implement your own function blocks to reduce clutter
in your code
4. Never use XML UI layouts for something more complex than menu.

-------------------------

