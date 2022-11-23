Vivek | 2017-01-02 01:04:22 UTC | #1

I have build the android launch app which launches individual 3D sample but the problem is I cannot go back to the launcher unless untill I kill the app.
What is the right way to kill the individual 3D sample on Android(to be used in custom launcher).

-------------------------

weitjong | 2017-01-02 01:04:22 UTC | #2

This is a known problem with our Sample Launcher on Android. It is actually not a problem on the launcher app per se, to me, it is more a design issue on Android platform. After user choosing a sample to launch, the launcher loads the corresponding *.so and launch the sample. The problem is, after a *.so is loaded, Android API does not provide an easy way to unload it. The selected sample remains effective until you kill and restart the app. If anyone know how to unload a shared library then you may help to contribute to fix this.

-------------------------

