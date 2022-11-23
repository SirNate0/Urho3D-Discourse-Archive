rasteron | 2017-01-02 01:06:22 UTC | #1

Hi,

I'm still familiarizing myself again with Urho3d events, particularly network management and debugging it. I'm trying to log connection status from server but somehow it does not appear in the console. I already tried [b]log.Info()[/b] or [b]Print()[/b] with connect and disconnect events and using OpenConsoleWindow(); The only thing that works so far is on the client side and if I place the log commands in the main loop (server side).

Is there a way to get client info everytime it connects/disconnects through Scripting API?

-------------------------

