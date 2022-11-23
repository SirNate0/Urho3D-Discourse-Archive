Dave82 | 2017-01-02 01:07:42 UTC | #1

Hi i tried to register some of my nodes' functions but when i try to call them from the script the game crashes :

I register it like this : (The INFPlayer is a derived class from INFNode which is derived from Urho3d::Node)
[code]RegisterObject<INFPlayer>(scriptEngine , "INFPlayer");[/code]

After this i register a global function called getCurrentPlayer() which returns an INFPlayer pointer

[code]engine->RegisterGlobalFunction("INFPlayer@ getCurrentPlayer()", asFUNCTION(INFPlayer::getCurrentPlayer), asCALL_CDECL);[/code]

But whenever i try to call this function from the script the game crashes.I'm pretty sure i'm missing something... So whats the proper way of registering a custom Node ?

If i register Urho3d::Application static functions it works fine , the crash happens only with Nodes

-------------------------

cadaver | 2017-01-02 01:07:43 UTC | #2

You should not subclass Node, but just create new components. Subclassing Node will bite you in the ass when you try to load/save or network synchronize the scene and it doesn't know to create the custom nodes on the opposite side.

-------------------------

Dave82 | 2017-01-02 01:07:43 UTC | #3

Hi Cadaver ! And thanks for the quick reply ! I have my own save/load mechanism so i wont use those , neither the networking part .The game has an extremely large level(s) so i can't load it at once , therefore i split them into segment chunks.
The point of subclassing the Node is simply having a "Recursive" access to the scene graph structure.This works very well so far , and i have really clean code thanks to this.

e.g a simple call to a someSegment->build() builds the segment.All child nodes in the segment will call their build() functions recirsively and do their job.

Using components would really mess things up since they are not recursive , so i would need to code some kind of a Component Graph to have a component child parent structure to keep track of the whole scene structure.Not to mention is still need Nodes in the scene to use these components

I still can expose some global functions from my Urho3d::Application and use those if Custom Node registration is not possible , but it would be really useful
Thanks

EDIT Don't get me wrong i found the Component system very useful in lot of situations ! Like a MuzzleFlash component or a CharacterController component ! Makes c++ as you write scripts  :slight_smile: it's very convenient ! but in this situation i would rather go with subclassing (if possible ofcourse)

-------------------------

Dave82 | 2017-01-02 01:07:43 UTC | #4

[quote]Also, you're downstream from RefCounted in inheritance so you should be using the autohandle registration syntax.[/quote]

Thank you very much for the help ! It works perfectly now .

-------------------------

