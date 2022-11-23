Ray_Koopa | 2017-01-02 01:13:42 UTC | #1

I've built Urho3D as instructed and want to start the Editor out of Urho3D-1.5-Build\bin\

What is problematic to me is that the Editor always shows the Urho3D-1.5-Build\bin\Data folder as the Root in the Resource Browser. Thus I see a lot of Ninja War files.
Even when I set the resource path to the folder of my game and refresh the Resource Browser, it sticks to Urho3D-1.5-Build\bin\Data.

Is there any way to change this? I want it to point at my own game's Data folder.

-------------------------

1vanK | 2017-01-02 01:13:42 UTC | #2

Simplest way - copy player and editor.bat to game folder :)

EDIT: and scripts, and ui textures + xmlfiles :))

I think, correct way is not place your data to "Data folder", but create another dir "GameData" and use it for  own resources

-------------------------

cadaver | 2017-01-02 01:13:42 UTC | #3

Yes, this is not strictly speaking a bug, because the Resource Browser represents a view of all resource paths registered to the engine, just like the Urho resource system internally operates. This includes both the resources from the editor's executable directory, as well as the resource path you set yourself.

-------------------------

Ray_Koopa | 2017-01-02 01:13:43 UTC | #4

So that means I gotta merge my game data directory with the editor's one?

I guess a cleaner way for me would be to just copy my created resources back to the game folder then, as I don't wanna accidentally include Editor resources in my game folders and my source control.

EDIT: I just created a symlink to my game's data folder in the Editor's data folder. With a minus at the front. That makes it appear at the very top of the Resource Browser, and works fine so far.

-------------------------

