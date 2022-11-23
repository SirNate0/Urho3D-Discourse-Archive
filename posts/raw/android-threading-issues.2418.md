sabotage3d | 2017-01-02 01:15:18 UTC | #1

Hi, I have some problems with the threading on Android. If I open native UI on top of Urho3D it opens it in seperate thread. Then I cannot send events or use the resource system. Is there a safe way to work with native UI elements on Android?
For example if I open a new intent and try to access events or resources I am getting these errors. 
[code]Intent intent = new Intent();[/code]
[code]Urho3D: Sending events is only supported from the main thread[/code]
[code]Urho3D: Attempted to get resource from outside the main thread[/code]
If I try to open an intent on the main thread like this:
[code]Intent intent = new Intent(Urho3D.this, Urho3D.class);[/code]
I am getting this error:
[code]Urho3D: Could not create window, root cause: 'Android only supports one window'[/code]

-------------------------

