Sasha7b9o | 2017-01-02 01:07:57 UTC | #1

Perhaps, it would be more convenient for users of the engine if names of classes began with a prefix "U".
Thus, it would have an opportunity to have the classes
class Camera : public UCamera {};
class Object {};
etc.

-------------------------

cadaver | 2017-01-02 01:07:57 UTC | #2

We already have Urho3D namespace, so I don't see much of a need for this.

Note that when you subclass Urho classes like components, you might break factories / serialization / net replication if you don't know what you're doing. Usually you should rather be creating your own logic components and composing them into nodes alongside with Urho's built-in components.

-------------------------

Sasha7b9o | 2017-01-02 01:07:57 UTC | #3

[quote="cadaver"]We already have Urho3D namespace, so I don't see much of a need for this.[/quote]
Ok. It is a pity.

In principle, I solved a problem thus:
[code]#define UButton Urho3D::Button

class Button : public UButton {};[/code]

But macro COPY_BASE_ATTRIBUTES(UButton) in function void Button::RegisterObject(UContext *context) look so:
[code]namespace Urho3D
{
context->CopyBaseAttributes<Urho3D:Button, Button>()
}[/code]
And the program is included into an infinite cycle.

[quote]Note that when you subclass Urho classes like components, you might break factories / serialization / net replication if you don't know what you're doing. Usually you should rather be creating your own logic components and composing them into nodes alongside with Urho's built-in components.[/quote]
Thanks. I will pay attention.

-------------------------

Enhex | 2017-01-02 01:07:57 UTC | #4

What's the point of regressing to C with Classes?
Just derive directly from Urho3D::Button or add "using namespace Urho3D;"

-------------------------

Sasha7b9o | 2017-01-02 01:07:57 UTC | #5

[quote="Enhex"]add "using namespace Urho3D;"[/quote]

I think, to mix personal and others' classes are very bad idea. Besides, it won't solve a problem. As C++ will distinguish my Buttun fron Urho3D::Button?

-------------------------

cadaver | 2017-01-02 01:07:57 UTC | #6

In a problem case like this you could call CopyBaseAttributes yourself without using the macro. Arguably macros are always more errorprone than template functions; they're provided for convenience only and nothing says you have to use them.

Additionally, it doesn't sound very descriptive if you name your class just Button. What is the functionality you're adding to the engine's built-in Button class?

-------------------------

Sasha7b9o | 2017-01-02 01:07:57 UTC | #7

[quote="cadaver"]Arguably macros are always more errorprone than template functions; they're provided for convenience only and nothing says you have to use them.[/quote]
Of course.
Tell, but whether really macroes COPY_BASE_ATTRIBUTES() etc. from Serializable.h have to be in namespace "Urho3D"?

[quote]Additionally, it doesn't sound very descriptive if you name your class just Button. What is the functionality you're adding to the engine's built-in Button class?[/quote]
In my button are added:
multilingual text,
concrete style,
hint,
events for change state cursor,
and some additional parameters for creation:
[code]lButton::lButton(UContext *context) :
    UButton(context)
{
    SetStyle("MainMenuButton");

    label = Label::Create("", SET::MENU::FONT::SIZE::ITEM);
    AddChild(label);
}

lButton::lButton(UIElement *uielement, char *text, int width /* = -1 */, int height /* = -1 */) :
    UButton(gContext)
{
    SetStyleAuto(gUIRoot->GetDefaultStyle());
    SetStyle("MainMenuButton");
    label = Label::Create(text, SET::MENU::FONT::SIZE::ITEM);
    AddChild(label);

    if (uielement)
    {
        uielement->AddChild(this);
    }

    if (width == -1 && height == -1)
    {

    }
    else if (width == -1)
    {
        SetFixedHeight(height);
    }
    else if (height == -1)
    {
        SetFixedWidth(width);
    }
    else
    {
        SetFixedSize(width, height);
    }

    SubscribeToEvent(this, Urho3D::E_HOVERBEGIN, HANDLER(lButton, HandleHoverBegin));
    SubscribeToEvent(this, Urho3D::E_HOVEREND, HANDLER(lButton, HandleHoverEnd));
}

void lButton::RegisterObject(UContext *context)
{
    context->RegisterFactory<lButton>("UI");

    COPY_BASE_ATTRIBUTES(UButton);
}

void lButton::SetText(char *text)
{
    label->SetText(text);
}

void lButton::SetHint(char *text)
{
    hint = new Hint(text);
}

void lButton::HandleHoverBegin(StringHash, VariantMap&)
{
    gCursor->SetSelected();
}

void lButton::HandleHoverEnd(StringHash, VariantMap&)
{
    gCursor->SetNormal();
}

void lButton::OnClickBegin(const IntVector2& position, const IntVector2& screenPosition, int button, int buttons, int qualifiers, UCursor* cursor)
{
    UButton::OnClickBegin(position, screenPosition, button, buttons, qualifiers, cursor);

    if(buttons == Urho3D::MOUSEB_RIGHT)
    {
        if(hint)
        {
            if(gHint)
            {
                gUIRoot->RemoveChild(gHint);
            }
            hint->SetPosition(screenPosition.x_, screenPosition.y_ - hint->GetHeight());
            gUIRoot->AddChild(hint);
            hint->BringToFront();
            gHint = hint;
            gCounterHint = 0;
        }
    }
}[/code]
And, nevertheless, the Button because it is the standard button for my appendix is called simply.

-------------------------

Enhex | 2017-01-02 01:07:58 UTC | #8

[quote="Sasha7b9o"][quote="Enhex"]add "using namespace Urho3D;"[/quote]

I think, to mix personal and others' classes are very bad idea. Besides, it won't solve a problem. As C++ will distinguish my Buttun fron Urho3D::Button?[/quote]
The "Urho3D::" part, just like you would with the "U" you suggested (which is very ambiguous).
The difference is that you can use namespaces to avoid having to type them all the time.

-------------------------

cadaver | 2017-01-02 01:07:58 UTC | #9

Including the macros inside the Urho3D namespace is just file formatting and illustrates that conceptually they belong to Urho3D. However, the preprocessor doesn't understand namespaces so it won't actually matter to it where they are defined.

-------------------------

Sasha7b9o | 2017-01-02 01:07:58 UTC | #10

[quote="Enhex"]The "Urho3D::" part, just like you would with the "U" you suggested (which is very ambiguous).
The difference is that you can use namespaces to avoid having to type them all the time.[/quote]
I am afraid, I don't understand you, or we speak about different things. Sorry.

Unfortunately, option[code]class Button : public Urho3D::Button {};

void Button::RegisterObject(UContext *context)
{
    context->RegisterFactory<Button>("UI");

    context->CopyBaseAttributes<Urho3D::Button, Button>();
}[/code] too doesn't work.
It is a pity.

-------------------------

Sasha7b9o | 2017-01-02 01:07:58 UTC | #11

[quote="cadaver"]However, the preprocessor doesn't understand namespaces so it won't actually matter to it where they are defined.[/quote]
Yes, it is valid, now and I understood)
All right, we will write a prefix before the our class.

-------------------------

cadaver | 2017-01-02 01:07:58 UTC | #12

Actually what happens is that because the class names are same, excluding namespace, they get the same name hash, and the engine attribute & factory system gets confused. You are essentially "overwriting" the existing Button class with your class. 

If you want this to happen, and you never need to instantiate or load plain Urho3D::Button's, you can skip the call to CopyBaseAttributes (instead you can just register your own extra attributes).

If you don't want this to happen, rename your class.

I'll make a fix to CopyBaseAttributes however that it returns immediately if the classnames are the same.

-------------------------

Sasha7b9o | 2017-01-02 01:07:58 UTC | #13

[quote="cadaver"]If you want this to happen, and you never need to instantiate or load plain Urho3D::Button's, you can skip the call to CopyBaseAttributes (instead you can just register your own extra attributes).[/quote]
Ok, thanks.

[quote]I'll make a fix to CopyBaseAttributes however that it returns immediately if the classnames are the same.[/quote]
It seems to me, in this case it is necessary to display the message WARNING.

-------------------------

cadaver | 2017-01-02 01:07:58 UTC | #14

Since the class names are just hashes at that point, it will not potentially be anything legible. But yes, that can be added.

-------------------------

