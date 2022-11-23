att1 | 2019-07-29 11:17:25 UTC | #1

Hi, I encountered a problem, I want to submit my game app created with urho3d engine to google play, but I must submit it with Android App Bundle format. 
How can I compile my project with this format? 
Thank you very much!

-------------------------

Modanung | 2019-07-29 12:03:04 UTC | #2

Hi there, and welcome to the forums.

Does [this thread](https://discourse.urho3d.io/t/package-files-on-android/1982/2?u=modanung) provide an answer to your question?

-------------------------

att1 | 2019-07-29 13:45:02 UTC | #3

Thank you for your reply, but I think it has no help.

-------------------------

johnnycable | 2019-07-29 15:00:35 UTC | #4

As any other Android App.

https://developer.android.com/guide/app-bundle/

cmd line is probably faster:

https://developer.android.com/studio/build/building-cmdline#build_bundle

and that boils down to run:

> ```
> ./gradlew :base:bundleDebug
> ```

into your app directory

-------------------------

Lumak | 2019-07-29 15:10:16 UTC | #5

Simplest way is to use Android Studio:
1 - Build your Urho3D project for Android
2 - rest shown in the images below:

https://imgur.com/DEbxGaw

https://imgur.com/O4scyn9

-------------------------

att1 | 2019-07-29 15:50:19 UTC | #6

I opened my project with android studio, it says must use android studio with version 3.5, so I download the android studio version 3.5 beta, but it can not update the Gradle plugin.

-------------------------

Lumak | 2019-07-29 15:59:06 UTC | #7

You'll need to manually edit the gradle wrapper properties file as shown here
https://github.com/Lumak/Urho3D-Android-Project#android-studio-import

**Note** There is entirely new build process for Urho3D for Android (head of master branch) and it's not something that I use. The method that I use is prior to the latest method, using Urho3D 1.7 version -- just FYI.

-------------------------

