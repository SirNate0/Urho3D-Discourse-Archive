KonstantTom | 2017-01-02 01:11:45 UTC | #1

Hello! How to create android live wallpaper using urho3d and c++? I've created small urho3d application with scene (such as 04_StaticScene sample), but how to route render from SDLActivity to WallpaperService.Engine??

-------------------------

Egorbo | 2017-01-02 01:11:45 UTC | #2

It won't be easy, definitely will require some changes in SDLActivity.java.
See [learnopengles.com/how-to-use ... wallpaper/](http://www.learnopengles.com/how-to-use-opengl-es-2-in-an-android-live-wallpaper/) how to use Opengl in WallpaperService

-------------------------

KonstantTom | 2017-01-02 01:11:45 UTC | #3

Thanks, I will read about it. 
Maybe anyone know easier way? :slight_smile:

-------------------------

rku | 2017-01-02 01:11:45 UTC | #4

Wouldnt that be a real battery burner?

-------------------------

