Aliceravier | 2021-03-17 15:55:07 UTC | #1

Hi!

I am working on a raspberry pi4 in Raspbian.

I am trying to use Urho3D while another process is trying to access a sound card attached to the pi. 
However, the process cannot access the sound card while the game is running. (The other process is based on RTAudio).

I was wondering if this is because Urho3D is taking control of the sound card and blocking access from the other process. If so, would it be possible to disactivate the sound elements in Urho to give the other proess full access to them?

Thanks for any help on this.

-------------------------

