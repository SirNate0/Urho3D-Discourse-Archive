Dave82 | 2019-12-01 22:15:50 UTC | #1

Hi ! What's the proper way of registering a custom subsytem in the angelscript context ?  And if it registered how can i retreive it in the script ?
[code]
class someScript : ScriptObject
{
      void Start()
     {
          MyCustomSubsystem@ mcs = // How to retreive it ?
     }
}
[/code]
Also is there a way to register susbsytems or other Urho3D::Object as a member of ScriptObject so it can be accessed directly just like "cache" , "sound" and "scene" variables ? 
Thanks !

-------------------------

