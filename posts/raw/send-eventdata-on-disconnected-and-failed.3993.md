dev4fun | 2018-02-07 02:47:36 UTC | #1

Its posible send an event data on events "E_SERVERDISCONNECTED" and "E_CONNECTFAILED"? Im modifying the Urho3D::Network, and I want customize this events to send a code to client side. This way when client side receives the event of "CONNECTFAILED", I can know for what reason this happens.

Example:
   Wrong password, then I send event : E_CONNECTFAILED with the code 400
   Client will receive event, and the code 400, this way I can show a text to inform game that was disconnected because of inserted a wrong password.

Thanks.

-------------------------

Eugene | 2018-02-07 08:32:43 UTC | #2

You could pass as much data as you need with any event.
Just use appropritate `SendEvent` signature

-------------------------

dev4fun | 2018-02-07 18:49:28 UTC | #3

Hmm sure. 'll try this, thanks for ur help.

-------------------------

