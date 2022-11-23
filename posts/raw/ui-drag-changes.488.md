hdunderscore | 2017-01-02 01:00:49 UTC | #1

Hey,

I've been slowly working on some UI drag changes and am getting closer to pull-request, but wouldn't mind some tips with how to set up the scripting.
[quote]- Multi-touch drag support
- Combo press touch support -- you get id mask of pressed buttons + number of buttons + the average of their positions
- Improved drag canceling support

Line edit now has a numeric mode:
- Supports setting a precision for # of decimal points formatting.
- Supports drag editing; can set increment amount, increment smoothing, button mask to activate the drag.
- E_TEXTFINISHED is sent when LineEdit is defocused (press enter, escape, press away from it / finishing a drag).[/quote]

Branch:https://github.com/hdunderscore/Urho3D/tree/drag_clean
Commit with all differences: [github.com/hdunderscore/Urho3D/ ... 2dd36a7636](https://github.com/hdunderscore/Urho3D/commit/40a1ddbbe918dde7ae7f24fd1d25c12dd36a7636)
An earlier pull-request I closed: [github.com/urho3d/Urho3D/pull/473](https://github.com/urho3d/Urho3D/pull/473)

A summary of changed function signatures:
UI.cpp: 
[color=#FF8080]-UIElement* UI::GetDragElement() const[/color]
[color=#008040]+const HashMap<UIElement*, int> UI::GetDragElements()[/color]

UIElement.cpp (and derivatives):
[color=#FF8080]-void Slider::OnDragEnd(const IntVector2& position, const IntVector2& screenPosition, Cursor* cursor)[/color]
[color=#008040]+void Slider::OnDragEnd(const IntVector2& position, const IntVector2& screenPosition, int dragButtons, int buttons, Cursor* cursor)[/color]

A summary of new functions:
UIElement.cpp
[color=#008040]+virtual void OnDragCancel(const IntVector2& position, const IntVector2& screenPosition, int dragButtons, int buttons, Cursor* cursor);[/color]

New event related:
UIEvents.h - E_TEXTFINISHED:
[color=#008040]+    PARAM(P_VALUE, Value);                 // Float[/color]

UIEvents.h - E_DRAG*:
[color=#008040]+    PARAM(P_BUTTONS, Buttons);              // int[/color]
[color=#008040]+    PARAM(P_NUMBUTTONS, NumButtons);        // int[/color]

New Exposed attribute accessors:
[code]+    ENUM_ACCESSOR_ATTRIBUTE(LineEdit, "Line Edit Mode", GetMode, SetMode, LineEditMode, lineEditModes, LEM_ALL, AM_FILE);
+    ACCESSOR_ATTRIBUTE(LineEdit, VAR_INT, "Numeric Precision", GetNumericPrecision, SetNumericPrecision, unsigned, 4, AM_FILE);
+    ACCESSOR_ATTRIBUTE(LineEdit, VAR_FLOAT, "Value", GetValue, SetValue, float, 0.0f, AM_FILE);
+    ACCESSOR_ATTRIBUTE(LineEdit, VAR_INT, "Drag Edit Combo", GetDragEditCombo, SetDragEditCombo, int, MOUSEB_RIGHT, AM_FILE);
+    ACCESSOR_ATTRIBUTE(LineEdit, VAR_FLOAT, "Drag Edit Increment", GetDragEditIncrement, SetDragEditIncrement, float, 0.1f, AM_FILE);
+    ACCESSOR_ATTRIBUTE(LineEdit, VAR_FLOAT, "Drag Edit Smooth", GetDragEditSmooth, SetDragEditSmooth, float, 0.1f, AM_FILE);[/code]

There may be other functions that need to be exposed to scripting/attributes, I'll need to comb over the commit.

Thanks

-------------------------

cadaver | 2017-01-02 01:00:49 UTC | #2

If the HashMap is problematic, you could alternatively expose a Vector or PODVector of the dragged elements, and make it so that the drag touch ID is retrievable from the element itself.

-------------------------

hdunderscore | 2017-01-02 01:00:50 UTC | #3

I made the change, however I am realising that I need to do some extra step (intermediate function converting from vector to array). This is what I have so far:
[b]UI.h:[/b]
[code]const Vector<UIElement*> GetDragElements();[/code]

[b]UIAPI.cpp:[/b]
[code]
static CScriptArray* UIGetDragElements(UI* ptr)
{
    return VectorToArray(ptr->GetDragElements(), "const Array<UIElement@>");
}

static void RegisterUI(asIScriptEngine* engine) 
{
...
engine->RegisterObjectMethod("UI", "const Array<UIElement@> GetDragElements()", asFUNCTION(UIGetDragElements), asCALL_CDECL_OBJLAST);
...
}
[/code]
I've tried a few variations of the above too, however I get an error when I try to run an application (eg, editor):
[quote]ERROR: :0,0 Failed in call to function 'RegisterObjectMethod' with 'UI' and 'const Array<UIElement@> GetDragElements()' (Code: -10)
ERROR: :0,0 Invalid configuration. Verify the registered application interface.
ERROR: Failed to compile script module Scripts/Editor.as [/quote]

-------------------------

cadaver | 2017-01-02 01:00:50 UTC | #4

In AngelScript arrays are returned by handle, so your function declaration should be something like "const Array<UIElement@>@ GetDragElements()". Also, you likely have to use VectorToHandleArray instead so that refcounting of the elements inside the array is handled correctly.

-------------------------

hdunderscore | 2017-01-02 01:00:58 UTC | #5

That worked perfectly, thanks for that !

I've been busy the last few days, so not many changes. At the moment the biggest issue I have is a hard to track bug that causes editor to crash when saving a new file.

Since it might take a while to get everything ready, I'll start splitting off the small changes into their own pull-requests which should also help with evaluating the changes.

-------------------------

