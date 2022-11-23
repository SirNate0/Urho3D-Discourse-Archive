hcomere | 2017-06-13 11:05:49 UTC | #1

Hello,

I currently have my network layer done with WebSockets / WebRTC DataChannels for both Desktop and Web worlds.
I have also done some kind of client predicition / server reconciliation / redundancy to fight packet lost and some other networking techniques.

But as i am porting my game to Urho3D, i feel most of my work is redundant with Urho3D network subsystem so i plan to use it instead of redoing it myself.

My first observation is that UrhoPlayer does not work on web, i guess it is due to absence of network subsystem when compiling with emscripten ?

How can replace the kNet part with my WebSockets / WebRTC layer and still can use Urho3D network stuff like world replication ?

Regards,
Harold

-------------------------

