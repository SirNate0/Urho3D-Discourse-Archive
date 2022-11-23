vivienneanthony | 2017-01-02 01:09:37 UTC | #1

Hi

Do anyone know what could cause this error on the Windows side using VS?

[pastebin.com/UNCEhtTm](http://pastebin.com/UNCEhtTm)

The source is [github.com/vivienneanthony/Urho ... evelopment](https://github.com/vivienneanthony/Urho3D-Hangars/tree/development)

Any help is appreciated.


Vivienne

-------------------------

thebluefish | 2017-01-02 01:09:38 UTC | #2

Did you actually download/install the ODBC driver first?

-------------------------

vivienneanthony | 2017-01-02 01:09:38 UTC | #3

Hi

I think so. I will ask the programmer. We have not had problems before.. I know in the pass I had to change the nano to a more friendly mysql version specifically make files but that should not be a issue.

I asked the programmer to test building the make file project again. Hoping my quick overwrite fix in the morning works.

Vivienne

-------------------------

weitjong | 2017-01-02 01:09:38 UTC | #4

The CMake already gave you a clear error and even give you the offending line number. Incidentally, I also stumbled upon this issue while I was merging nanodbc upstream changes into our codebase. The fix was just in yesterday in the master branch. In case you are using 1.5 then you can back port the fix easily.

-------------------------

vivienneanthony | 2017-01-02 01:09:39 UTC | #5

[quote="weitjong"]The CMake already gave you a clear error and even give you the offending line number. Incidentally, I also stumbled upon this issue while I was merging nanodbc upstream changes into our codebase. The fix was just in yesterday in the master branch. In case you are using 1.5 then you can back port the fix easily.[/quote]

Hi

I seen the commit. I've already applied the changes. I'm just waiting for the VB Visual Basic person to test if the make files create at minimum.

I seen that tagging was adding but waiting on that. I would love to use it but I also know I would have to use the additional ImGui related Draw functions in Urho3D because I'm implementing Imgui at minimum for a editor.

[youtube.com/watch?v=g92xG8ZMMA0](https://www.youtube.com/watch?v=g92xG8ZMMA0)

Vivienne

-------------------------

