Taymindis | 2017-10-13 02:08:29 UTC | #1

Greeting, 
I m new to Urho 3d,  I am migrating from other c++ game engine to urho3d, But I have a difficulties to handle the scroll view. 

**_Questions: - _**
**_1. It only render the element which within the size, when scroll down, it is empty_**
**_2.  How do I listen the scroll view event(onMove, onSlide .etc)_**


This is my sample code below, but i
```cpp
 _scrollV = GetSubsystem<UI>()->GetRoot()->CreateChild<ScrollView>();    
    _scrollV->SetStyleAuto();
    _scrollV->SetSize(GetSubsystem<UI>()->GetRoot()->GetWidth()/2, GetSubsystem<UI>()->GetRoot()->GetHeight()/3);
    _scrollV->SetPosition(0, 0);
    _scrollV->SetPriority(100);
    _scrollV->SetColor(Color::BLACK);
    _scrollV->SetEnabled(true);
    _scrollV->SetDeepEnabled(true);
    _scrollV->SetSelected(true);
    _scrollV->SetHovering(true);
    _scrollV->SetScrollBarsVisible(true, true);
    
    
    SharedPtr<Urho3D::UIElement> chatContentElement(_scrollV->CreateChild<Urho3D::UIElement>());
    _scrollV->SetContentElement(chatContentElement);
    chatContentElement->SetLayoutMode(Urho3D::LM_VERTICAL);
    chatContentElement->SetStyleAuto();
    chatContentElement->SetPosition(0, 0);
    chatContentElement->SetAlignment(Urho3D::HA_LEFT, Urho3D::VA_BOTTOM);
    
    chatContentElement->SetSize(_scrollV->GetSize());
    
    for(int i=20;i>0;i--) {
        // Construct new Text object
        SharedPtr<Text> helloText(new Text(context_));
        
        // Set String to display
        helloText->SetText("Hello World from Urho3D Hello World from Urho3D Hello World from Urho3D Hello World from Urho3D Hello World from Urho3D ");
        
        // Set font and text color
        helloText->SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.sdf"), GetSubsystem<UI>()->GetRoot()->GetMaxWidth());
        helloText->SetColor(Color::GREEN);
        
        helloText->SetPosition(0 , GetSubsystem<UI>()->GetRoot()->GetHeight()  * (i/20) );
        helloText->SetPriority(100);
        _scrollV->GetContentElement()->AddChild(helloText);
    }
    
    SubscribeToEvent(_scrollV, E_MOUSEBUTTONDOWN, URHO3D_HANDLER(HelloWorld, HandleScrollUpdate) );
```

-------------------------

Eugene | 2017-10-13 07:15:45 UTC | #2

[quote="Taymindis, post:1, topic:3653"]
1. It only render the element which within the size, when scroll down, it is empty
[/quote]

I think I know what are you talking about, but could you provide screenshot?
You probably should increase minimal size of inner elements.

[quote="Taymindis, post:1, topic:3653"]
2.  How do I listen the scroll view event(onMove, onSlide .etc)
[/quote]
Is E_SCROLLBARCHANGED event **from `ScrollBar`** enough for you?

-------------------------

Taymindis | 2017-10-13 12:46:36 UTC | #3

Hi Eugene, 

1. Attached Screen Shot For References![29 PM|607x500](upload://a6WrCCjNOMHbgdm3SoTWkuJp0tV.png)


2. I couldn't find out E_SCROLLBARCHANGED event, is this define at other header file? The purpose I want to make it scrollbar move physically. 

3. Should I use ListView instead of scrollbar view?

-------------------------

Eugene | 2017-10-13 14:26:13 UTC | #4

[quote="Taymindis, post:1, topic:3653"]
helloText-&gt;SetPosition
[/quote]
Well, start with removing this line. You shouldn't set position and size of your elements manually if you use automatic layout (vertical or horizontal).

[quote="Taymindis, post:1, topic:3653"]
chatContentElement-&gt;SetSize(_scrollV-&gt;GetSize());
[/quote]
Here is the same. You literally forced your content to have the same size as your window. If you use ScrollView, you probably want the content to be _bigger_.

[quote="Taymindis, post:3, topic:3653"]
I couldn’t find out E_SCROLLBARCHANGED event, is this define at other header file?
[/quote]
https://github.com/urho3d/Urho3D/blob/ee054a1507cb3518c57d4ebc43cfd6dc93de9a27/Source/Urho3D/UI/UIEvents.h#L213

[quote="Taymindis, post:3, topic:3653"]
Should I use ListView instead of scrollbar view?
[/quote]
Depends on desired functionality.

-------------------------

Taymindis | 2017-10-13 13:43:11 UTC | #5

Hi Eugene, 

1. I have applied your suggestion and I also remove this line 
``` chatContentElement->SetAlignment(Urho3D::HA_LEFT, Urho3D::VA_BOTTOM); ```
And now is working fine.

2. I've tried sample a. and it's not working, but b. is working fine. Am I missing something or ?
 a.
```  SubscribeToEvent(_scrollV, E_SCROLLBARCHANGED, URHO3D_HANDLER(HelloWorld, HandleScrollUpdate) ); ```  
b.
``` SubscribeToEvent( E_SCROLLBARCHANGED, URHO3D_HANDLER(HelloWorld, HandleScrollUpdate) );``` <<< it is working

-------------------------

Eugene | 2017-10-13 13:47:55 UTC | #6

[quote="Taymindis, post:5, topic:3653"]
Am I missing something or ?
[/quote]
Yep, you are. `E_SCROLLBARCHANGED` is
[quote="Eugene, post:2, topic:3653"]
event from ScrollBar
[/quote]

-------------------------

Taymindis | 2017-10-13 14:20:14 UTC | #7

Hi Eugene, 

Noted with Thanks :slight_smile: :+1:

-------------------------

jmiller | 2017-10-13 14:44:13 UTC | #8

Hi Taymindis, glad you got this working.

Just to be clear for others, we refer to these methods of Object.h
[code]
/// Subscribe to a specific sender's event.
void SubscribeToEvent(Object* sender, StringHash eventType, EventHandler* handler);
/// Subscribe to an event that can be sent by any sender.
void SubscribeToEvent(StringHash eventType, EventHandler* handler);
[/code]

-------------------------

