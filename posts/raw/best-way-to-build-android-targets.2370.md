zakk | 2017-01-02 01:15:01 UTC | #1

Hello,

For building Android targets, i think there are two ways:

1) Building the whole Android target, including it's own sources (the sources of our games) following instructions in the wiki.
Ok, you have to rebuild all everytime you want to test something different. Why not.

2) Using precompilated libs and Urho3d player, found here: [url]https://sourceforge.net/projects/urho3d/files/Urho3D/1.6/[/url]
As i'm only using [b]Urho3DPlayer[/b], i'm interested doing this.
Is it possible ?

I guess it would be something like this:
2a) creating an empty android project , by copying the [i]Android[/i] folder from the sources.

I've copied it in my [i]/tmp[/i] folder.

[code]

 /tmp/Android$ tree
.
??? AndroidManifest.xml
??? assets
??? build.xml
??? CopyData.bat
??? custom_rules.xml
??? project.properties
??? res
??? ??? drawable
??? ??? ??? logo_large.png
??? ??? drawable-hdpi
??? ??? ??? icon.png
??? ??? drawable-ldpi
??? ??? ??? icon.png
??? ??? drawable-mdpi
??? ??? ??? icon.png
??? ??? layout
??? ??? ??? samples_list_text_view.xml
??? ??? ??? samples_list.xml
??? ??? ??? scripts_list.xml
??? ??? values
???     ??? strings.xml
??? src
    ??? com
    ??? ??? github
    ???     ??? urho3d
    ???         ??? SampleLauncher.java
    ???         ??? ScriptPicker.java
    ???         ??? Urho3D.java
    ??? org
        ??? libsdl
            ??? app
                ??? SDLActivity.java

[/code]

Ok now, i guess that i have three more things to do:

2b) copying my script(s) and data somewhere in [i]assets[/i]

2c) copying pre-compilated Android libs and Urho3DPlayer somewhere in the project tree. But where ?

2d) modifying [i]Urho3D.java[/i] for calling the [i]Urho3DPlayer[/i] instead of running sample put in externals libs (done by default).

[i]and only[/i], i could hope that running [i]ant debug[/i] would compile java files into dex, and builds the whole APK.

Is it possible doing something like this ?

Thank you! :smiley:

-------------------------

sabotage3d | 2017-01-02 01:15:03 UTC | #2

What I usually do is symlink Android, CMake and the cmake_android.sh, cmake_generic.sh, .bash_helpers.sh from Urho3D folder into my project. I call cmake_android and after that build only the lib for the project. After that I make an Android studio project which is for the java part and it loads the lib. There is a new Android Studio CMake toolchain where you can possibly do this in one go.

-------------------------

zakk | 2017-01-02 01:15:04 UTC | #3

Hello,

Thank you for your answer.
As i progress in Android's knowledge, i've seen that gradle (successor of ant) was able to manage dynamic libraries linking.
I don't know if ant can do it, but as gradle seems to be widely adopted, and simpler, i'd rather like using it.

For the moment , still no APK (must understand gradle before), but i post here when i succeed.

-------------------------

sabotage3d | 2017-01-02 01:15:05 UTC | #4

All you need to do is import your Urho3D generated Android project in Android Studio will convert it to gradle for you, again that is what I did.

-------------------------

