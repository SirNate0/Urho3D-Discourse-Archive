gawag | 2017-01-02 01:10:48 UTC | #1

Urho seems to be able to change the mouse cursor but my tries are just crashing. How does it work?
[urho3d.github.io/documentation/1 ... 1_u_i.html](http://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_u_i.html)
[urho3d.github.io/documentation/1 ... ursor.html](http://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_cursor.html)

[code]
        //Urho3D::Cursor* cursor=GetSubsystem<Urho3D::UI>()->GetCursor();   // cursor is 0 when trying this
        static Urho3D::Cursor* cursor=new Urho3D::Cursor(context_);         // doesn't work either, crashes in SetCursor
std::cout<<(size_t)cursor<<std::endl;

        if(c==mouse_cursor::beam)
            cursor->SetShape(Urho3D::CursorShape::CS_IBEAM);
        else
            cursor->SetShape(Urho3D::CursorShape::CS_NORMAL);

        GetSubsystem<Urho3D::UI>()->SetCursor(cursor);    // GetSubsystem<Urho3D::UI>() is non 0 and seems valid.
[/code]

Neither the samples nor the editor seem to change the cursor anywhere, it it currently possible? System default cursor shapes would be fine.

-------------------------

weitjong | 2017-01-02 01:10:48 UTC | #2

I think you still do not grasp that Urho3D's Input subsystem supports two kinds of mouse: operating-system mouse (the mouse cursor is rendered by OS) and software-rendered mouse (the mouse cursor is rendered by UI subsystem). You change which mouse mode to use with Input::SetMouseVisible(). The code that you posted only makes sense for the latter case. When using-software-rendered mouse, think of the cursor as "just another UI-element", in fact behind the scene it is a UI-element. So, it is easier to understand why the initial UI::GetCursor() return 0, i.e. you must first use UI::SetCursor() to set it to something initially before the UI::GetCursor() could return it back. You can actually see it in action in Editor but only when you have a very slow machine or you have a very CPU-intensive operation such as loading a very scene file, the editor switches the cursor shapes to CS_BUSY. The CursorShape enumeration that limits the number of cursor shape in software-rendered mouse is actually artificial. You can "register" as many custom shapes as you like. And more over the shape is just a skin deep, you can change whole UI looks by loading alternate UI-style file. Just for completeness sake, you can also change the cursor shape of the OS mouse, although the number of shapes to choose from is genuinely limited by the underlying OS could provide.

-------------------------

gawag | 2017-01-02 01:10:48 UTC | #3

The mouse is visible, I can see the normal arrow cursor.

[code]
        _context->GetSubsystem<Urho3D::Input>()->SetMouseVisible(true);
        static Urho3D::Cursor* cursor=new Urho3D::Cursor(context_);
std::cout<<(size_t)GetSubsystem<Urho3D::UI>()->GetCursor()<<std::endl;  // in the first function call this returns 0 in the second a valid value and crashes (I suppose at SetCursor)

           cursor->SetShape(Urho3D::CursorShape::CS_IBEAM);

        //if(!GetSubsystem<Urho3D::UI>()->GetCursor())    // If I uncomment this it doesn't crash but does also nothing
            GetSubsystem<Urho3D::UI>()->SetCursor(cursor);
[/code]
I'm never seeing a different cursor. (Windows 7 BTW)
Should it work like that?

Edit: In the editor code I found
[code]
ui.cursor.shape = CS_BUSY;
[/code]
Which could be equivalent to
[code]
GetSubsystem<Urho3D::UI>()->GetCursor()->SetShape(Urho3D::CursorShape::CS_IBEAM);
[/code]

I tried
[code]
GetSubsystem<Urho3D::Input>()->SetMouseVisible(true);
if(!GetSubsystem<Urho3D::UI>()->GetCursor())
    GetSubsystem<Urho3D::UI>()->SetCursor(new Urho3D::Cursor(context_));
GetSubsystem<Urho3D::UI>()->GetCursor()->SetShape(Urho3D::CursorShape::CS_BUSY);
[/code]
which didn't crash but also didn't change the cursor.

Only
[code]
GetSubsystem<Urho3D::Input>()->SetMouseVisible(true);
GetSubsystem<Urho3D::UI>()->GetCursor()->SetShape(Urho3D::CursorShape::CS_BUSY);
[/code]
crashes.

-------------------------

1vanK | 2017-01-02 01:10:49 UTC | #4

Pre-need to load the cursor image (for software-rendered cursor)

[code]    XMLFile* style = cache->GetResource<XMLFile>("UI/DefaultStyle.xml");
    SharedPtr<Cursor> cursor(new Cursor(context_));
    cursor->SetStyleAuto(style);
    ui->SetCursor(cursor);
    ui->GetCursor()->SetVisible(true);[/code]
Also, it makes no sense to use OS cursor at the same time

-------------------------

weitjong | 2017-01-02 01:10:50 UTC | #5

You can set the UI-style just once in the UI "root".

-------------------------

gawag | 2017-01-02 01:10:50 UTC | #6

Uhm I got something but it's weird. This is my GUI code now:
[code]
            XMLFile* style = cache->GetResource<XMLFile>("UI/DefaultStyle.xml");
            UI* ui=GetSubsystem<UI>();
            ui->GetRoot()->SetDefaultStyle(style);
            SharedPtr<Cursor> cursor(new Cursor(context_));
            cursor->SetStyleAuto(style);   // without this I can't see any cursor
            cursor->SetShape(Urho3D::CursorShape::CS_RESIZEHORIZONTAL);  // this is one of the defined default cursors
            ui->SetCursor(cursor);
            
            window=new Window(context_);
            ui->GetRoot()->AddChild(window);
            window->SetStyle("Window");
            window->SetSize(600,70);
            window->SetColor(Color(.0,.15,.3,.5));
            window->SetAlignment(HA_LEFT,VA_TOP);

            window_text=new Text(context_);
            window_text->SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"),14);
            window_text->SetColor(Color(.8,.85,.9));
            window_text->SetAlignment(HA_LEFT,VA_TOP);
            window_text->SetText("Hello Urho!");
            window->AddChild(window_text);
[/code]

When setting the cursor every frame:
[code]
    void HandleUpdate(StringHash eventType,VariantMap& eventData)
    {
        GetSubsystem<Urho3D::UI>()->GetCursor()->SetShape(Urho3D::CursorShape::CS_RESIZEHORIZONTAL);
...
[/code]
I can see the set cursor but only if it's not over the window. When it is over the window or when I'm not setting it every frame I see the normal arrow cursor.
Is that normal?

-------------------------

1vanK | 2017-01-02 01:10:50 UTC | #7

[code]
void Window::OnHover(const IntVector2& position, const IntVector2& screenPosition, int buttons, int qualifiers, Cursor* cursor)
{
    UIElement::OnHover(position, screenPosition, buttons, qualifiers, cursor);

    if (dragMode_ == DRAG_NONE)
    {
        WindowDragMode mode = GetDragMode(position);
        SetCursorShape(mode, cursor);
    }
    else
       SetCursorShape(dragMode_, cursor);
}
[/code]

-------------------------

gawag | 2017-01-02 01:10:50 UTC | #8

[quote="1vanK"][code]
void Window::OnHover(const IntVector2& position, const IntVector2& screenPosition, int buttons, int qualifiers, Cursor* cursor)
{
    UIElement::OnHover(position, screenPosition, buttons, qualifiers, cursor);

    if (dragMode_ == DRAG_NONE)
    {
        WindowDragMode mode = GetDragMode(position);
        SetCursorShape(mode, cursor);
    }
    else
       SetCursorShape(dragMode_, cursor);
}
[/code][/quote]
So Window is setting the cursor shape every frame when hovering. So its normal to set the cursor every frame? Seemed weird.

-------------------------

