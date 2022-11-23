rbnpontes | 2017-01-02 01:15:13 UTC | #1

Hello guys, i searched in forum about Android Build, i followed the instrucions, but i can finish because when i use "android -update" won't work, the bash command give-me a error for invalid command, i searched in android tools and i found android.bat in folder, but still doestn work, i need help, im not expert in cmake operations or Build operations, in android website, the android command is obsolete

-------------------------

weitjong | 2017-01-02 01:15:14 UTC | #2

No, the document is still up-to-date. The same steps outlined there are exactly what has been carried out in our Android-CI build. Notice that there should not be a dash character in the argument for the "android" command. Have you installed Android SDK in your system or use the "android" command to keep your SDK current?

-------------------------

rbnpontes | 2017-01-02 01:15:14 UTC | #3

I have Android SDK installed correctly

-------------------------

yushli | 2017-01-02 01:15:14 UTC | #4

You need to open a window console to execute the android command instead on the bash console.

-------------------------

