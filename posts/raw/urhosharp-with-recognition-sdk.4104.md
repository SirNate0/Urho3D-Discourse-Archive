robyava | 2018-03-19 14:43:41 UTC | #1

Hello everybody,
we successfully integrated Xamarin.Forms UrhoSharp with our native Recognition SDK.
What we reach is that we have a Urho Base CameraScene with photo camera rendering (yuv format)
feeded from data coming from our SDK, and a generic Recognition Scene (a subclass of previous CameraScene) that build a generic 3D scene. Our last working is try to integrate a iOS native view (with geolocalization and recognition functionalities) over a Recognition Scene, but we have troubles with Touch Handling.
What we would like to ask is how Urho manage touch interaction when we mix a Camera Scene (derived from Application base scene) with iOS native view.  What is the behavior in this case of touch handling? Please note that in native project we use new embedding Xamarin Forms functionality and we derive a ViewController from UrhoSurface and add it to a iOS native view hierarchy.  
Thanks a lot
Regards
Roberto

-------------------------

