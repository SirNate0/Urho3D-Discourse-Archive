trillian | 2018-08-29 12:46:13 UTC | #1

Hi all,

I've create a simple Hotkey control based on LineEdit, e.g to customize shortcuts in a game. You can find it here:
https://gist.github.com/stievie/878a4f04d2499dc4f1d12dbb7552b2af

Maybe someone can need it.

Best Stefan

-------------------------

Virgo | 2019-01-19 08:31:31 UTC | #2

What is type Key in the code?

-------------------------

trillian | 2019-01-19 09:00:35 UTC | #3

It is defined in InputConstants.h, see
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Input/InputConstants.h#L60

-------------------------

Virgo | 2019-01-19 09:06:14 UTC | #4

:sweat_smile:this is from the master branch... im using urho3d version 1.7, no wonder i cant figure out what it is.

-------------------------

trillian | 2019-01-19 09:26:01 UTC | #5

Oh, I see there is no InputConsts.h in 1.7. I think you can just change it to an (unsigned) int and use the SDLK_* constants instead.

-------------------------

Virgo | 2019-01-19 10:11:47 UTC | #6

I got a serious problem...
cant i add custom ui components to precompiled urho3d library? i tried to add several custom ui components shared on forum to my project and all of them worked just fine except style part.

just like this one

    auto *edit = window->CreateChild<HotkeyEdit>();
    edit->SetStyle("LineEdit");
    edit->SetMinSize(200, 32);
    
    auto *edit2 = window->CreateChild<LineEdit>();
    edit2->SetStyleAuto();
    edit2->SetMinSize(200, 32);
    edit2->SetPosition(0, 32);

![Annotation%202019-01-19%20180936|431x430](upload://p3yPs7jOjVSirq32pSozZsqIU8i.jpeg)

-------------------------

trillian | 2019-01-19 10:35:21 UTC | #7

Hm yes, I also have problems with the styling part from time to tome. For the moment I set the style manually in code, e.g.:

    HotkeyEdit* hkEdit = hkContainer->CreateChild<HotkeyEdit>("HotkeyEditor");
    Texture2D* tex = cache->GetResource<Texture2D>("Textures/UI.png");
    hkEdit->SetTexture(tex);
    hkEdit->SetImageRect(IntRect(48, 0, 64, 16));
    hkEdit->SetBorder(IntRect(4, 4, 4, 4));

![image|410x445](upload://pNiqZvsdyVvtFCAN9cK7IW9M2ZN.png) 

When I don't set the Texture by code, I get the same white control as you, even when I use SetStyle("LineEdit").

Maybe someone can enlighten me what I'm doing wrong.

-------------------------

Virgo | 2019-01-19 10:51:21 UTC | #8

is this Lumak's TabGroup?

-------------------------

trillian | 2019-01-19 10:55:47 UTC | #9

Yes, it's great :grinning:

-------------------------

Virgo | 2019-01-19 11:40:41 UTC | #10

:sob: i need to do your style trick again if i wanna use this TabGroup!

:rofl: i adjusted code for his TabGroup, but the style part is still not working, wth!

-------------------------

trillian | 2019-01-19 12:01:11 UTC | #11

How and when the styling works is not entirely clear to me. In this case i just trial and error around :grin:

-------------------------

weitjong | 2019-01-19 15:44:39 UTC | #12

The styling of all UI-element derived classes are nothing else but a mechanism to apply a set of predefined attributes to the UIElement object. You first define the set of attributes in a "style sheet" or whatever you want to call it, in an XML file. You then reference them by using `UIElement::SetStyle("predefined-style-name")`. The `UIElement::SetStyleAuto()` variant uses the type of the UI-element itself as the name of the style to be applied, i.e. `Button::SetStyleAuto()` is equivalent to `Button::SetStyle("Button")`. But how does the UI subsystem know which "style sheet" you want to use in the first place? In actual fact it does not. So you must do the below quite early on, if you plan to create the UI layout by code.

```
auto* cache = GetSubsystem<ResourceCache>();
auto* stylesheet = cache->GetResource<XMLFile>("path/to/your/stylesheet.xml");
auto* uiRoot = GetSubsystem<UI>()->GetRoot());
uiRoot->SetDefaultStyle(stylesheet);
```

When you create a new UIElement object as a child of some other object that is already in the UI hierarchy, the child object will ask the parent object for a style sheet, if the child does not explicitly have one. So, ultimately the query will reach to the root UI element. That's why the above code is important.

Of course alternatively, you can also set the style sheet you want to use in the individual object before calling the `SetStyle()`. You may want to do this if you want to have different style sheet to be applied than the normal default one, for instance. Or, if you want to create a new object and style it before parenting it.

HTH.

-------------------------

Virgo | 2019-01-19 17:22:53 UTC | #13

actually i did set default to ui root and i create ui elements directly into ui root. but like in this HotkeyEdit, the Text element inside does apply styles, and the BorderImage just wont.

-------------------------

weitjong | 2019-01-19 17:34:50 UTC | #14

I did not look at your code so I don’t know what went wrong. But If you understand what I explained above then you should find the Urho3D UI styling mechanism is quite versatile and flexible. The Urho3D project provided style sheet is actually designed to be used by its Editor. I cannot imagine why anyone would want to use it as it is in one own game. So perhaps Lumak has a modified version of that file but you are not.

-------------------------

Virgo | 2019-01-19 18:29:32 UTC | #15

Lumak's repo https://github.com/Lumak/Urho3D-UI-Components
i copied his `DefaultStyle.xml` and `UI.png` and still does not work

;;

back to HotkeyEdit:
I tried setting default `SetDefaultStyle()` then `SetStyle()`,
and `SetStyle()` with second argument specified, both didnt work.
results are same: only the Text element inside applied style

-------------------------

Virgo | 2019-01-19 18:34:45 UTC | #16

    SetStyle("LineEdit", GetSubsystem<ResourceCache>()->GetResource<XMLFile>("UI/DefaultStyle.xml"));
    SetTexture(GetSubsystem<ResourceCache>()->GetResource<Texture2D>("Textures/UI.png"));
    SetImageRect(IntRect(48, 0, 64, 16));
    SetBorder(IntRect(4, 4, 4, 4));

code snippet above works, it seems like the problem is within BorderImage?

-------------------------

trillian | 2019-01-20 06:16:31 UTC | #17

Thank you for your explanation, this is indeed very useful.

-------------------------

Virgo | 2019-01-20 07:14:38 UTC | #18

:face_with_raised_eyebrow:what, did you figure out how to properly set style?

-------------------------

trillian | 2019-01-20 07:19:39 UTC | #19

Not yet, but it made some things clearer. I need to cleanup my client code anyway one time (at them moment it's a bit messy), then I'll look into it.

-------------------------

Leith | 2019-01-20 07:44:47 UTC | #20

Why does your key enumeration  (the #defines) not take advantage of binary enum?
For example,

```
#define SC_MOD_LSHIFT  1               // Left Shift
#define SC_MOD_RSHIFT  1 << 1          // Right Shift
#define SC_MOD_SHIFT  SC_MOD_RSHIFT | SC_MOD_LSHIFT         // Left or right Shift
```

-------------------------

trillian | 2019-01-20 08:04:31 UTC | #21

Yes, good question. But then the method GetQualName (https://gist.github.com/stievie/878a4f04d2499dc4f1d12dbb7552b2af#file-hotkeyedit-h-L39) wouldn't work anymore. I know it could be changed to work with it, but this control was a quick solution for a problem I had. I agree there is a lot room for improvements :blush:.

-------------------------

Leith | 2019-01-20 09:08:32 UTC | #22

Actually, your GetQualName will still work!
It performs a bunch of AND tests on active bits, and collates a result, it will still work perfectly with a binary enum.
You did not test the combined bitflag enumerations in this method, but had you, it would STILL work (with some positive results appearing more than once) :slight_smile:

Keep up the good work!

-------------------------

