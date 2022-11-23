lexx | 2017-06-11 13:11:46 UTC | #1

Hi.

* Downloaded Urho3d from github. 
* Got  libUrho3D.so and libUrho3DPlayer.so  files from Urho3D-1.6.964-Android-SHARED-snapshot.tar.gz 
* Copied urho assets to Urho3D/Android/assets

I get Urho3D/Android/bin/Urho3D-debug.apk when I write (in Urho3D/Android)
  ant debug

 
So how to make working apk-file which includes  libUrho3D.so, libUrho3DPlayer.so and some  angelscript file? 
I dont know where to copy those libraries, and dont know how apk then starts libUrho3DPlayer.

-------------------------

slapin | 2017-06-11 13:34:30 UTC | #2

Well, Android build of Urho is a mystery for me too, will wait for answers too...

-------------------------

lexx | 2017-06-12 17:04:47 UTC | #3

Got player to work. 
I dont know how to use SHARED version but I downloaded Urho3D-1.6.964-Android-STATIC-snapshot.tar.gz and copied  libUrho3D.a and libUrho3DPlayer.so to Urho3D/Android/libs/armeabi-v7a   and then

> ant debug

and got Urho3D-debug.apk which starts NinjaSnowWar.

-------------------------

