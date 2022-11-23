sabotage3d | 2017-01-02 01:01:16 UTC | #1

Hi ,
What is the best way to query Multitouch coordinates, absolute and relative ? 
I had a look in the documentation but I can only see GetMousePosition () . Is it applicable for touch events ?

Thanks in advance,

Alex

-------------------------

hdunderscore | 2017-01-02 01:01:16 UTC | #2

You would do something like...
[code]for(int i = 0; i < input.GetNumTouches(); i++)
{
    TouchState* ts = input.GetTouch(i);
}[/code]

[urho3d.github.io/documentation/H ... input.html](http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_input.html)
[urho3d.github.io/documentation/H ... state.html](http://urho3d.github.io/documentation/HEAD/struct_urho3_d_1_1_touch_state.html)

-------------------------

sabotage3d | 2017-01-02 01:01:16 UTC | #3

Thanks a lot :slight_smile:
Just one thing can we get both relative and absolute position ?

-------------------------

hdunderscore | 2017-01-02 01:01:16 UTC | #4

It looks like they are both available in TouchState (absolute: position_ / lastPosition_, relative: delta_).

-------------------------

sabotage3d | 2017-01-02 01:01:17 UTC | #5

thanks it works quite well
Just one thing if we want to check for a touch event is that the best way to do it :


[code]bool touchEvent = false;

if(input->GetNumTouches()>0) 
{  
	touchEvent = true ;  
}[/code]

I wonder if there is something similar to SDL:

[code]if (evt.type == SDL_FINGERDOWN) {
    SDL_Touch *state = SDL_GetTouch(evt.tfinger.touchId);
}[/code]

-------------------------

hdunderscore | 2017-01-02 01:01:17 UTC | #6

That way works, but if you want another method you can subscribe to the touch events:
TouchBegin
TouchMove
TouchEnd

eg:
[code]SubscribeToEvent("TouchBegin", "Handle_TouchBegin");
}

void Handle_TouchBegin(StringHash eventType, VariantMap& eventData)
{
    log.Info("TouchBegin");
}[/code]

[urho3d.github.io/documentation/H ... _list.html](http://urho3d.github.io/documentation/HEAD/_event_list.html)

-------------------------

sabotage3d | 2017-01-02 01:01:18 UTC | #7

Awesome works like a charm :slight_smile:

-------------------------

