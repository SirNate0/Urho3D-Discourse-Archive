NiteLordz | 2017-01-02 01:02:50 UTC | #1

I am curious as to what you guys edit your angelscript files in.  I know that Urho3D generates an AngelScript.h file, that says it can be used for code completion.  How do i enable this ?

-------------------------

weitjong | 2017-01-02 01:02:52 UTC | #2

Check this topic [topic45.html](http://discourse.urho3d.io/t/configuring-codelite-for-editing-as-scripts/68/1). I can use the AngelScript.h to enable code completion on my Eclipse IDE too.

-------------------------

NiteLordz | 2017-01-02 01:02:52 UTC | #3

Thanks!!!

-------------------------

JulyForToday | 2017-01-02 01:03:05 UTC | #4

I use notepad++. [url=http://www.jazz2online.com/downloads/7300/notepadplusplus-angelscript-language-support/]I found a user defined language file for angelscript for syntax highlighting[/url]. I had to manually tweak the colors (I use a dark background, and that file assumes you use a white one). Doesn't have code completion though, I'll really have to look into eclipse for that. I find myself looking at the ScriptAPI page, using ctrl+f a whole lot.

One really nice thing about the editor is that it recompiles scripts on the fly when there are changes. You have to have something in the scene with a scriptinstance referencing your angelscript module. Then when any file used by that module changes, you will see a message in the editor's console (F1). Either it will say the module compiled, or it will give you a nice error message, indicating the particular file, and line number.

So I have the editor with an open console on one screen, and notepad++ open on the other, and the moment I save in notepad++ I instantly get a message on the console if what I just did was valid or not. Instant feedback. :sunglasses:   Gotta love it. Plus it doesn't matter what code editor you use. :smiley:

Just remember you have to reference the right script file in a scriptinstance. Gotta reference the script file the module starts in, not the particular script file containing your class. I ran into trouble with that originally, and [url=http://discourse.urho3d.io/t/solved-getting-script-object-after-instantiating/576/1]this post helped me fix it[/url].

-------------------------

