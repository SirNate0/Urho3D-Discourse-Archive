Elendil | 2018-12-09 10:40:48 UTC | #1

I have little trouble understand Events in Urho.
When can I use SendEvent and which type of event I have to use?
Another question is for VarianMap, which event should I use for detect the event?

for example I use SendEvent inside HandleUpdate (from tutorial sample project) with this code:

    VariantMap eData;
    if (input->GetKeyPress(KEY_O))
    			{
    				eData[Update::P_TIMESTEP] = "hmm"; 
    				SEND_EEVENT = true;
    			}
    if (SEND_EEVENT == true)
    		{
    			SEND_EEVENT = false;
    			SendEvent(E_UPDATE, eData);
    		}

but after this SendEvent() urho goes in to infinite loop and then crash. when I change eData in to eventData from function arguments, and don't send data, then it is working and I can read "hmm" from eventData. Then I start thinking, maybe I should use SendEvent outside HandleUpdate function?

-------------------------

Miegamicis | 2018-12-08 22:00:03 UTC | #2

`E_UPDATE` is one of the core events in the engine so you shouldn't call it manually. Create your own events if you want to add additional logic.

```
VariantMap myData = GetEventDataMap();
myData["SomeText"] = "Hello, world!";
myData["Number"] = 1;
SendEvent("MyCustomEvent", myData);
```

and add a listener to it

```
SubscribeToEvent("MyCustomEvent", URHO3D_HANDLER(MyClass, HandleMyCustomEvent));

...

void MyClass::HandleMyCustomEvent(StringHash eventType, VariantMap& eventData)
{
    String text = eventData["SomeText"].GetString();
    int number = eventData["Number"].GetInt();
}

```

When you send an event in the application, all the objects which subscribed to it will receive it immediately. When you called the `E_UPDATE` event your application probably got stuck in the HandleUpdate method because it was called over and over again without letting the engine to run the next frame.

-------------------------

Elendil | 2018-12-08 22:10:27 UTC | #3

Thanks, it is now clear to me.

One thing, you wrote:
`VariantMap myData = GetEventDataMap();`
is the GetEventDataMap necessary? I create only VariantMap without GetEventDataMap, and it is working. Or for what is good set VariantMap = GetEventDataMap ?

-------------------------

Miegamicis | 2018-12-08 22:23:16 UTC | #4

Thats one of the optimizations to avoid creating the VariantMap on the fly which should give a performance boost, as far as I know. Not sure how much performance it gives tho.

-------------------------

Elendil | 2018-12-08 22:26:25 UTC | #5

Thanks. Urho3D Events Documentation should be extented to this informations. I think they are helpfull.

-------------------------

jmiller | 2018-12-09 00:16:08 UTC | #6

Here are some references..
Events: https://urho3d.github.io/documentation/HEAD/_events.html
`GetEventDataMap()`: https://urho3d.github.io/documentation/HEAD/_main_loop.html

-------------------------

Sinoid | 2018-12-09 04:03:05 UTC | #7

Do be aware that the VariantMaps returned by `GetEventDataMap()` are not cleared to an empty state (unless that's changed recently) so they *can* contain old/invalid fields if you don't fully set all of the Event's parameters - not a big deal because you usually will be doing that.

**Edit:** the above is entirely incorrect.

-------------------------

weitjong | 2018-12-09 04:01:25 UTC | #8

The method clears the VariantMap object first before reusing it.

-------------------------

Sinoid | 2018-12-09 04:02:24 UTC | #9

Oh, then I'm misremembering it. Thanks for the correction.

-------------------------

