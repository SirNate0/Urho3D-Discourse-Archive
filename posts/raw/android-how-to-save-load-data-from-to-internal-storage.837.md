TikariSakari | 2017-01-02 01:03:19 UTC | #1

Hello, I am new to urho3d, well pretty much just installed it, and it really seems quite nice engine. Sadly there aren't that many tutorials around and the only guidelines would be the samples I think?

I was wondering is there something for save files? Like lets say I want to save progress on my game on android, is there some premade libraries for it? Like I would prefer to use internal storage to use save files for a game, where should I start digging this stuff? I tried to google around, but couldn't really find anything.

Thank you in advance.

Edit: I think this question should have been inside support forums, sorry for posting it in a wrong place.

-------------------------

jmiller | 2017-01-02 01:03:23 UTC | #2

Welcome to the forum [b]TikariSakari[/b] :slight_smile:

The sample programs save scene data to XML file ("F5 to save scene, F7 to load")
18_CharacterDemo does saves (serializes) data external to the scene.

You might find useful: XMLElement and XMLFile
[urho3d.github.io/documentation/H ... ement.html](http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_x_m_l_element.html)
[urho3d.github.io/documentation/H ... _file.html](http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_x_m_l_file.html)

or the File class
[urho3d.github.io/documentation/H ... _file.html](http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_file.html)

HTH

-------------------------

cadaver | 2017-01-02 01:03:23 UTC | #3

As for the directory where to save, try either FileSystem::GetUserDocumentsDir() or FileSystem::GetAppPreferencesDir(). I don't remember personally trying to save data on an Android application, so your mileage may vary.

-------------------------

Mike | 2017-01-02 01:03:23 UTC | #4

I'm using FileSystem::GetUserDocumentsDir() and it works great.
Note that user documents dir is located at /data/data/com.github.com.urho3d/files/ (unless you modify the manifest otherwise).
FileSystem::GetAppPreferencesDir() is for desktop.

You can also refer to this post [url]http://discourse.urho3d.io/t/android-writing-in-resource-cache/88/1[/url].

-------------------------

cadaver | 2017-01-02 01:03:23 UTC | #5

Had a vague memory that we'd ported code from SDL hg to handle SDL_GetPrefPath() on non-desktop platforms, but apparently remembered wrong. Anyway, there are also SDL Android specific functions SDL_AndroidGetInternalStoragePath() & SDL_AndroidGetExternalStoragePath(), but like Mike said GetUserDocumentsDir() should work fine.

-------------------------

