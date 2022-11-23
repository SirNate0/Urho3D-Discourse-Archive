nickwebha | 2021-02-26 16:53:12 UTC | #1

If both `SetEchoCharacter()` and `SetText()` are set and you try to use `GetChildStaticCast()` you just get a bunch of whatever `SetEchoCharacter()` was set to.

    auto* lineEditPassword = new Urho3D::LineEdit( context_ );
    lineEditPassword->SetName( "LineEditPassword" );
    lineEditPassword->SetMinHeight( 24 );
    lineEditPassword->SetEchoCharacter( '*' );
    lineEditPassword->SetText( "password here" );

    Urho3D::LineEdit* passwordLineEdit = window_->GetChildStaticCast< Urho3D::LineEdit >( "LineEditPassword", false );

`passwordLineEdit` does not equal "*password here*" but instead equals "*************".

This seems like a bug to me.

-------------------------

JSandusky | 2021-02-25 01:46:31 UTC | #2

Looks correct to me. Which function are you calling that's returning the echo'd version? If it's just that you're seeing the echo'd version in UI then it's correct.

Are you expecting to be able to static-cast away the properties of a class instance?

-------------------------

nickwebha | 2021-02-26 16:51:46 UTC | #3

Sorry, I should have made this comparison before: I am expecting it to act like the HTMLs `<input type="password" />`. Visually it is all *'s but when you retrieve the value it is was what was actually typed.

Right now, if I pre-set the text with `SetText()` (see example above) only *'s come out when retrieving the value.

**Edit**
Consider the password "*password*". In the above example, if I get the value of the LineEdit, all \*'s come out instead of "*password*" (looks like "********"). If I type one character (say "*A*") in the middle of it I get "*\*\*\*\*\*A\*\*\**".

Is `SetEchoCharacter()` only supposed to be a visual thing (like HTMLs `<input type="password" />`, or actually whatever you type into `SetEchoCharacter()`?

-------------------------

Eugene | 2021-02-26 21:03:29 UTC | #4

[quote="nickwebha, post:1, topic:6728"]
`passwordLineEdit` does not equal “ *password here* ”
[/quote]
Do you mean that if you call "GetText" you get hidden text?
My best bet would be this line:
https://github.com/urho3d/Urho3D/blob/f8cb13f49afa1a77743c4fc06582bc1bbc11ed29/Source/Urho3D/UI/LineEdit.cpp#L98

-------------------------

nickwebha | 2021-02-28 01:21:47 UTC | #5

Correct.

If I do not do `SetText()` and still use `SetEchoCharacter()` it works as expected (shows a bunch of *'s but outputs the "real" text). This is in addition to what I mentioned before about typing in the middle of the *'s.

Still feel this is a bug.

-------------------------

