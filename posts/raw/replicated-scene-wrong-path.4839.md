Liichi | 2019-01-19 20:46:33 UTC | #1

Hi, I'm having problem connecting the client of my game (running on linux) to the server (running windows).

_LOG:_
> INFO: Connecting to server 192.168.1.3:2345
> ERROR: Could not find resource C:/Users/username/lgk/build/bin/Data/Scenes/scene1.xml
> ERROR: Null file for async loading

If the client and the server are both in Linux everything works correctly.

It seems that the server is sending the wrong scene path, it should be **Data/Scenes/scene1.xml** instead of **C:/Users/username/lgk/build/bin/Data/Scenes/scene1.xml**.

Can somebody help me? Thanks! :slight_smile:

(Im using version 1.7)

-------------------------

Leith | 2019-01-20 01:09:41 UTC | #2

I'm not certain this is your solution (I'm still less than a week in Urho) but take a look at ResourceCache::SanitateResourceName - looks like it strips unnecessary path information.

-------------------------

Liichi | 2019-01-20 01:53:28 UTC | #3

Hi, thanks for helping. Maybe that method should be used in this line:
 https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Network/Connection.cpp#L186

-------------------------

Leith | 2019-01-20 01:53:51 UTC | #4

I tend to agree - at least for the case of networking, it makes sense (to me) to always sanitize resource filepaths, though I am presuming that the ResourceCache is capable of 're-decorating' them internally for platforms that require absolute paths. I think that is what the resourcepath prefix stuff is about?

-------------------------

