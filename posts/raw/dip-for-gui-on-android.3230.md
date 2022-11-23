redmouth | 2017-06-09 07:49:04 UTC | #1

Any way to compute density independent pixel size for UIs on android? thanks.

-------------------------

kostik1337 | 2017-06-09 07:54:42 UTC | #2

I haven't done something like this, but i think, you can get screen dpi with android api in java, pass it into your C++ code via JNI, and then scale all your widgets using this variable

-------------------------

johnnycable | 2017-06-09 10:32:04 UTC | #3

What about [the google way](https://developer.android.com/guide/practices/screens_support.html) for that?

-------------------------

extobias | 2017-06-09 13:23:19 UTC | #4

Hi, you could pass as an argument to your urho app.

SDLActivity.java
[code]
    protected String[] getArguments() {

        // Urho3D: always return the "app_process" as the first argument instead of empty array
        String[] ret = new String[3];
        ret[0] = "app_process";

        String lang = Locale.getDefault().getLanguage();
        ret[1] = lang;

        DisplayMetrics metrics = getResources().getDisplayMetrics();
        String dpi = Float.toString( metrics.xdpi ) + "," + Float.toString( metrics.ydpi );
        ret[2] = dpi;
        
        return ret;
    }
[/code]

MyApp.cpp (urho3d application subclass)
[code]
#ifdef __ANDROID__
    Urho3D::Vector<Urho3D::String> args = Urho3D::GetArguments();
    if( args.Size() >= 1)
        m_appLang = args[0];
    if( args.Size() >= 2)
        m_screenDPI = args[1];
#endif
[/code]

hope this would help.
Best regards.

-------------------------

redmouth | 2017-06-09 13:31:28 UTC | #5

Good solution, I think your code can be picked into master branch.

-------------------------

