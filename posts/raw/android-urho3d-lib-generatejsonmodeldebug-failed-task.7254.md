Joshua-PotatoMan | 2022-05-07 09:51:26 UTC | #1

hi i am new to urho3d engine i've been using it for that past a couple of days and everything was going smoothly... however yesterday i tried to compile the urho3d librays for android using  gradle   and it failed with this error 
--------------------------------------------------------------------------------------->
> Task :android:urho3d-lib:generateJsonModelDebug FAILED
FAILURE: Build failed with an exception.
 What went wrong:
Execution failed for task ':android:urho3d-lib:generateJsonModelDebug'.
> java.lang.NullPointerException (no error message) 

-------------------------------------------------------------------------------------->

i did look at the legacy docs and found that i had to install data & autoload  in an asset folder inside launcher-app and Coredata in assets inside urho3d-lib
however that didn't fix the problem and i still get the same problem 

i used android studio and it failed to sync to the libray.

if this has happen before or its just a new problem i'd be happy if you tell me how to fix it ;)

-------------------------

weitjong | 2022-05-07 16:57:22 UTC | #2

If you use main branch to build then follow the new online doc where it specifically states the version of the currently supported Android plugin and NDK.

https://urho3d.io/docs/getting-started/installation

You are on your own when you use other newer version available. I suspect if you newly installed Android Studio then you might have newer Android plugin that Urho does support. That’s the only reason I can think of that causing the initial gradle sync to fail. Having said that, I f you are able to use the latest plugin and get it to work, please share your fixes.

-------------------------

tungts1101 | 2022-05-23 05:44:17 UTC | #3

I also got this error with the main branch. I check the gradle plugin version in File\Project Structure in Android Studio and it is 4.0.2. Do you have any hint in this problem?

-------------------------

1vanK | 2022-08-05 20:45:25 UTC | #4

I'm still investigating this issue. Some cmake versions conflicts. After this <https://github.com/urho3d/Urho3D/pull/2949> minimal CMake version is 3.15, but old Android sdk can use old cmake plugin only

-------------------------

1vanK | 2022-08-13 19:20:16 UTC | #5

I have no experience with mobile development. Can You test/hilp with this https://github.com/urho3d/Urho3D/pull/3049

-------------------------

feresmu | 2022-08-30 12:23:38 UTC | #6

Hi.
With the last sources it compiles without errors with Android Studio Chipmunk | 2021.2.1 Patch 2

The apk runs but shows nothing.

That is because launcher-app-debug.apk have only libUrho3DPlayer.so in lib\armeabi-v7a\ folder

It seems that CMakeLists.txt are ok. Any idea to fix it?

-------------------------

SirNate0 | 2022-08-30 12:27:22 UTC | #7

Were the samples enabled for the build?

-------------------------

1vanK | 2022-08-30 15:15:10 UTC | #8

https://github.com/urho3d/Urho3D/blob/master/android/launcher-app/CMakeLists.txt#L16-L17

-------------------------

feresmu | 2022-08-30 19:11:02 UTC | #9

If I uncomment that the apk have all the .so samples but still shows nothing

-------------------------

elix22 | 2022-08-31 06:54:19 UTC | #10

Logcat is your best friend in debugging such issues .

Make sure that the assets folder in your APK is not empty.
You can unzip the APK by changing its extension to ".zip" and verify that the assets are there.

**Android/app/src/main/assets/Data**
**Android/app/src/main/assets/CoreData**

-------------------------

feresmu | 2022-08-31 13:20:52 UTC | #11

I have the assets and .so samples in the apk

I think the problem is that LauncherActivity cannot find (and because that, doesn't show) the library files.

If I modify LauncherActivity.kt in this way:
```
class LauncherActivity : ExpandableListActivity() {

    // Filter to only include filename that has an extension
    private fun getScriptNames(path: String) = assets.list(path)!!.filter { it.contains('.') }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

			// Start CharacterDemo sample 
            startActivity(
                Intent(this, MainActivity::class.java)
                    .putExtra(
                        MainActivity.argument,
						"18_CharacterDemo"
                    )
            )		
return;
```
it works if I launch 18_CharacterDemo only. So the problem seems to be UrhoActivity.getLibraryNames() function

-------------------------

1vanK | 2022-08-31 12:25:18 UTC | #12

It would be nice if you create a pull request with a fix

-------------------------

feresmu | 2022-08-31 13:25:01 UTC | #13

I' don't know how to fix the problem (not yet at least ;) (I have clarified my post)

But it seems to be UrhoActivity.getLibraryNames() function (I am not android/urho3d expert, not know what would be the problem)

-------------------------

SirNate0 | 2022-08-31 13:37:02 UTC | #14

I'm not sure, but I suspect the filtering looking for the `.` in the name may be wrong since you are adding a name without the `.` and it works.

-------------------------

