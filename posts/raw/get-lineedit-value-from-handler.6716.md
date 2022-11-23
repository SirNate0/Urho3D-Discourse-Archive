nickwebha | 2021-02-16 15:30:22 UTC | #1

In my `Start()` function I have:
> auto* lineEditUsername = new LineEdit( context_ );
> lineEditUsername->SetName( "LineEditUsername" );
> lineEditUsername->SetMinHeight( 24 );
> window_->AddChild( lineEditUsername );
> lineEditUsername->SetStyleAuto();
> ...
> auto* loginButton = new Button( context_ );
> loginButton->SetName( "ButtonLogin" );
> loginButton->SetMinHeight( 24 );
> Text* t = new Text( context_ );
> t->SetFont( cache->GetResource< Font >( "Fonts/Anonymous Pro.ttf" ), 15 );
> t->SetHorizontalAlignment( HA_CENTER );
> t->SetVerticalAlignment( VA_CENTER );
> t->SetText( "Login" );
> loginButton->AddChild( t );
> SubscribeToEvent( loginButton, E_RELEASED, URHO3D_HANDLER( Login, HandleLoginPressed ) );

Then the handler:
> void HandleLoginPressed( StringHash eventType, VariantMap& eventData ) {
> 	UIElement* username = window_->GetChild( "LineEditUsername", true );
> 
> 	std::cout << typeid( username ).name() << ' ' << username->GetName().CString() << ' ' << username << std::endl;
> };

This is all based on code from the samples.

My question is how do I get the value of the LineEdit in the handler? I have searched the samples (which never seem to do this), the documentation, and this forum but I can not figure this out.

-------------------------

JTippetts1 | 2021-02-16 15:43:31 UTC | #2

Since the event being handled by HandleLoginPressed is fired by the button, and not by the LineEdit control, the LineEdit control will not be present in the eventData map. Instead, you can obtain it manually by calling `window_->GetChildStaticCast<LineEdit>("LineEditUsername", true)` which will search window_'s children for a UI element named "LineEditUsername". The true parameter specifies a recursive search, which is useful if the control is not a direct child of window_, but is instead somewhere further down the hierarchy.

Then to get the value of the line edit, you call LineEdit::GetText.

-------------------------

nickwebha | 2021-02-16 16:18:46 UTC | #3

I had tried just this but with `CreateChild` (not `GetChildStaticCast`). Now it works. I will read up on the differences.

Thank you! I was pulling my hair out.

-------------------------

JTippetts1 | 2021-02-16 16:47:32 UTC | #4

The difference is that GetChild() returns a generic UIElement pointer, while GetChildStaticCast casts the pointer to the proper derived type. UIElement doesn't have a GetText method, but LineEdit does, so to do anything with the pointer it has to be cast to the correct type. You could also manually call StaticCast on the pointer returned by GetChild() if you want, it's the same thing.

-------------------------

