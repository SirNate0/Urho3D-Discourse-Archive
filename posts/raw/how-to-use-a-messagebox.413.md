scorvi | 2018-01-09 19:06:35 UTC | #1

hey,

i want to use the MessageBox class in a c++ project but i get every time an Error !!
the error is at:
[code]void RefCounted::ReleaseRef()
{
    assert(refCount_->refs_ > 0);
    (refCount_->refs_)--;
    if (!refCount_->refs_)
        delete this;
}[/code]
refCount is zero .... but i dont know what i did wrong!

i am using as a quit message: 
[code]
void SimpleSnake::Quit()
{

	GetSubsystem<UI>()->GetCursor()->SetVisible(true);

	messageBox_ = new Urho3D::MessageBox(context_, "Do you really want to exit the Game ?", "Quit Game ?");
	if (messageBox_->GetWindow() != NULL)
	{
		Button* cancelButton = (Button*)messageBox_->GetWindow()->GetChild("CancelButton", true);
		cancelButton->SetVisible(true);
		cancelButton->SetFocus(true);
		SubscribeToEvent(messageBox_, E_MESSAGEACK, HANDLER(SimpleSnake, HandleQuitMessageAck));
	}
}

void SimpleSnake::HandleQuitMessageAck(StringHash eventType, VariantMap& eventData)
{
	using namespace MessageACK;

	bool ok_ = eventData[P_OK].GetBool();
	

	GetSubsystem<UI>()->GetCursor()->SetVisible(false);


	if (ok_)
	{
		engine_->Exit();
	}
	
}
[/code]

-------------------------

cadaver | 2018-01-09 19:06:28 UTC | #2

MessageBox is a bit unusual class, as it destroys itself after it has been acknowledged. This is done by the "this->ReleaseRef()" call in the following code:

[code]
void MessageBox::HandleMessageAcknowledged(StringHash eventType, VariantMap& eventData)
{
    using namespace MessageACK;

    VariantMap& newEventData = GetEventDataMap();
    newEventData[P_OK] = eventData[Released::P_ELEMENT] == okButton_;
    SendEvent(E_MESSAGEACK, newEventData);

    this->ReleaseRef();
}
[/code]
Calling ReleaseRef() is illegal and will assert/crash if the object is not being currently held in a SharedPtr. I assume that your messageBox_ member variable is a raw pointer? In that case, changing it to a SharedPtr should fix the issue.

-------------------------

scorvi | 2017-01-02 01:00:14 UTC | #3

yes at first i had a raw pointer and i got an assert/crash at the MessageACK Event. 

now i am using the SharedPtr but i get an  assert/crash the second time i call Quit() ...  because 
[code]messageBox_ = new Urho3D::MessageBox(context_, "Do you really want to exit the Game ?", "Quit Game ?");[/code]
calls ReleaseRef() .... 
how do i use it the right way ?

-------------------------

weitjong | 2018-01-09 19:06:28 UTC | #4

I agree with Lasse that the MessageBox class is a little unusual. It was created for showing modal dialog box in the Editor via AngelScript API binding. As it is now, it would be a little clumsy to use in C++ language directly. Try not to use SharedPtr instance variable. Just declare the SharedPtr as local variable to your Quit() method and call AddRef() before the local variable goes out of scope. As already pointed out, the class will destroy itself later on when it has been acknowledged by calling ReleaseRef().

-------------------------

scorvi | 2018-01-09 19:05:52 UTC | #5

[quote="weitjong"]I agree with Lasse that the MessageBox class is a little unusual. It was created for showing modal dialog box in the Editor via AngelScript API binding. As it is now, it would be a little clumsy to use in C++ language directly. Try not to use SharedPtr instance variable. Just declare the SharedPtr as local variable to your Quit() method and call AddRef() before the local variable goes out of scope. As already pointed out, the class will destroy itself later on when it has been acknowledged by calling ReleaseRef().[/quote]

i am doing it now this way, thx!

-------------------------

sirop | 2018-01-09 16:54:02 UTC | #6

Hello.

Is this advice somehow still valid in 2018?

I try smth. like:
```
 SharedPtr<Urho3D::MessageBox> msgbox = new Urho3D::MessageBox(context_, "Check the USB connection", "USB AIR GAP");
```
which yields:

> D:\QtProjects\Urho3d\CPS_GAME\Navigation.cpp:1457: Fehler: C2039: "MessageBoxW": is not an element von "Urho3D"

What shall I do?

Thanks.

-------------------------

Eugene | 2018-01-09 18:43:45 UTC | #7

[quote="sirop, post:6, topic:413"]
What shall I do?
[/quote]

Congratulations! You triggered WinAPI mine and died.
Good way: Ensure that no Windows.h bullshit is exposed into your source code. Probably impossible.
Bad way: "Escape" your code like this `(Urho3D::MessageBox)`

-------------------------

sirop | 2018-01-09 19:31:53 UTC | #8

See. So it is easier to make up  one's own ad hoc MessageBox out of UIElement and some Text.
That's which I'll do.

-------------------------

Eugene | 2018-01-09 19:49:47 UTC | #9

Huh. Nope, it’s easier to escape these terrible WinApi macros.

-------------------------

Eugene | 2018-01-10 11:32:36 UTC | #11

Sorry, I was wrong about escaping, it won't work in this case.
Well, the simplest solution is to `#undef MessageBox` after your C++ includes. Thanks MS for this shitty WinAPI design.

-------------------------

sirop | 2018-01-10 15:30:47 UTC | #12

Yes,  I had my doubts already, but was too shy to reask.
Your latest post with

> #undef MessageBox after your C++ includes

lets my code compile now.

-------------------------

Dave82 | 2018-01-10 16:11:58 UTC | #13

Oh the ugly WinAPI... if it's not enough to fiddle with gibberish C spagetti, they had to use lowercase macros.Seriously.. Who the hell would use lowercase macros ? And if that's not enough already, they had to use the most generic keywords like MessageBox , min , max. I really want to speak with the idiot who greenlit these dumb ideas... How dumb one can be defining a macro NOMINMAX to actually NOT HAVE min and max defined ? That's like asking someone "Hey , you don't want a beer ?" and expecting a yes or no as answer..

-------------------------

Virgo | 2019-01-24 04:37:34 UTC | #14

:rofl: i tried methods mentioned in this thread, but still cant get rid of it
![image|690x41](upload://jSM64FRnp3ipcV8K1zQdJwSrqpV.jpeg)  
does MessageBox work with precompiled urho3d?

-------------------------

SirNate0 | 2019-01-24 23:02:39 UTC | #15

I suspect (given that the error is about some MessageBox**W**) that you're including the WinAPI files that have the define, then including the Urho MessageBox include, then you have your #undef. If that's the case, move the undef before the Urho includes and see if that works.

-------------------------

Virgo | 2019-01-25 02:12:21 UTC | #16

im using precomplied headers for external libraries, this is my pch for urho3d

    #if defined __cplusplus
    
    //#undef MessageBox
    #define URHO3D_PHYSICS true
    #define URHO3D_LOGGING
    #include <Urho3D/Urho3DAll.h>
    #include <Urho3D/UI/MessageBox.h>

    #endif

this gives the above compile error, if i uncomment the undef, it says `'MessageBox': is not a member of 'Urho3D'`

btw im using qt creator as ide, not sure if its the culprit.

-------------------------

Virgo | 2019-01-25 02:41:56 UTC | #17

oh and i only use Poco and Urho3D and those c++ standard libraries, no Qt or windows ones

-------------------------

Miegamicis | 2019-01-25 21:07:14 UTC | #18

Unfortunately the fix:

```
#ifdef MessageBox
#undef MessageBox
#endif
```

doesn't always work for me too, this issue keeps appearing from time to time with my projects. I would like to suggest changing `MessageBox` object to something else like `PopupMessage` or `NonWinApiMessageBox`.

-------------------------

