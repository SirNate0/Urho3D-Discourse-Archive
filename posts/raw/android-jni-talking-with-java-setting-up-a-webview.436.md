hdunderscore | 2017-01-02 01:00:22 UTC | #1

Hey, I've been working with android a bit and put together a perhaps dirty method of getting some urho3d c++ to java talk working, and it's rather simple:

The following code will show how to call a java function we will create called '[i]gotoGoogle[/i]', which will be tacked onto [b]SDLActivty.java[/b] located in [b]Android/src/org/libsdl/app[/b]. The Java code will then call a c++ function we will create to inform out app when it's ready.

Note: There is probably a cleaner way to do this (eg, extending SDLActivity), however I'm not familiar enough with android to know how-- contribute if you do !

[size=200]In SDLActivtiy.java:[/size]
File: [b]Android/src/org/libsdl/app/SDLActivity.java[/b]:

Add these imports:
[code]import android.widget.ViewSwitcher;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import com.github.urho3d.R;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;[/code]
[ul]
[li]ViewSwitcher is what will allow us to seamlessly switch between our urho application and the WebView (you can add animations, etc.)[/li]
[li]WebView and WebViewClient allow us to embed a browser / handle events in the browser.[/li]
[li]the R class is a machine-generated class that lets us access resources (eg, xml resources in [b]Android/res[/b])[/li]
[li]AnimationUtils lets us load animations from supplied resources[/li][/ul]


[size=150]In SDLActivtiy class:[/size]
Define these members in the [b]SDLActivity[/b] class:
[code]protected static WebView webview;
protected static ViewSwitcher layoutSwitcher;[/code]
The WebView and ViewSwitcher are like UIElements in Urho3d, it holds the functionality for the widget and renders its contents.

Add these initializers to [b]public static void initialize()[/b] in [b]SDLActivity[/b]:
[code]layoutSwitcher = null;
mJoystickHandler = null;[/code]

At the bottom of [b]protected void onCreate(Bundle savedInstanceState)[/b] in [b]SDLActivity[/b], change:
[code]mLayout = new AbsoluteLayout(this);
mLayout.addView(mSurface);

setContentView(mLayout);[/code]

to: 

[code]webview = new WebView(this);

mLayout = new AbsoluteLayout(this);
mLayout.addView(mSurface);

layoutSwitcher = new ViewSwitcher(this);
layoutSwitcher.addView(mLayout);
layoutSwitcher.addView(webview);

You will need to set up
Animation animIn, animOut;
animIn = AnimationUtils.loadAnimation(this, R.anim.fadein);
animOut = AnimationUtils.loadAnimation(this, R.anim.fadeout);

layoutSwitcher.setInAnimation(animIn);
layoutSwitcher.setOutAnimation(animOut);

setContentView(layoutSwitcher);[/code]
Note: Later, we will create the resources that R.anim.fadein and R.anim.fadeout reference.

Now the meat of the Java, the function we will call from c++ to switch into the WebView -- add these to [b]SDLActivity[/b]:
[code]public void gotoGoogle() {
        runOnUiThread(new Runnable() {
        // Note: You must handle UI events like switching views and working with web view in the UI thread.
            @Override
            public void run() {
                layoutSwitcher.showNext();
                webview.getSettings().setJavaScriptEnabled(true); // there can be security concerns with javascript.
                webview.getSettings().setBuiltInZoomControls(true);

                webview.loadUrl("http://www.google.com");
                webview.setWebViewClient(new WebViewClient(){
                    @Override
                    public void onPageStarted(WebView view, String url, Bitmap favicon){
                       super.onPageStarted(view, url, favicon);
                       // just an example of capturing the page start loading event
                       Log.d("java urho", "Loading: " + url); // goes to the system console/logcat
                    }

                    @Override
                    public void onPageFinished(WebView view, String url) {
                        super.onPageFinished(view, url);
                            // We will close the webview as soon as the page is loaded... add your own logic !
                            returnWebviewUrl(url);
                            hideWebview();
                    }

                    @Override
                    public boolean shouldOverrideUrlLoading(WebView view, String url) {
                        // This allows us to follow links in the web view without them being deferred to another browser. You may or may not want this.
                        view.loadUrl(url);
                        return true;
                    }
                });
            }
         });
    }

    public void hideWebview() {
        layoutSwitcher.showPrevious();
    }[/code]

And one last important declaration so that we can call a c++ function that we will define:
[code]    public native String returnWebviewUrl(String url);[/code]

[size=200]Animation Resources:[/size]
Let's create the animation resources, [b]Android/res/anim/fadein.xml[/b] and [b]Android/res/anim/fadeout.xml[/b]:
[b]Android/res/anim/fadein.xml[/b]:
[code]<?xml version="1.0" encoding="utf-8"?>
<set xmlns:android="http://schemas.android.com/apk/res/android"
    android:shareInterpolator="false" >

    <alpha
        android:duration="500"
        android:fromAlpha="0.0"
        android:toAlpha="1.0" >
    </alpha>

</set>
[/code]

[b]Android/res/anim/fadeout.xml[/b]
[code]<?xml version="1.0" encoding="utf-8"?>
<set xmlns:android="http://schemas.android.com/apk/res/android"
    android:shareInterpolator="false" >

    <alpha
        android:duration="200"
        android:fromAlpha="1.0"
        android:toAlpha="0.0" >
    </alpha>

</set>
[/code]

[size=200]C++:[/size]
Thankfully, we don't have to worry about setting things up on the C++ away from our main source-- everything works from there.

To call [b]gotoGoogle()[/b] from C++, we'll set up a function that looks like this:
[code]#if defined(ANDROID)

#include "Log.h"

#include <SDL.h>
#include <jni.h>
#include <string.h>

#define JAVA_CHECK_EXCEPTION(env, msg) \
while (env->ExceptionCheck()) \
{\
    LOGDEBUG(String("Exception:: ") + msg));\
    env->ExceptionDescribe();\
    env->ExceptionClear();\
}

void JavaGotoGoogle()
{
    LOGDEBUG("JavaGotoGoogle()");

    JNIEnv *env = static_cast<JNIEnv*>(SDL_AndroidGetJNIEnv());
    jobject activity = static_cast<jobject>(SDL_AndroidGetActivity());
    jclass clazz = env->GetObjectClass(activity);
    jmethodID gotoGoogle = env->GetMethodID(clazz, "gotoGoogle", "()V");// Note the signature string..

    LOGDEBUG(String((int) loginGoogle)); // inspect that we get a handle -- should do error checking..

    JAVA_CHECK_EXCEPTION(env, "Preperation"); // Macro to check for errors. Should really check after each call. Calling before the next bit to clear any errors that may happen earlier.

    env->CallVoidMethod(activity, gotoGoogle); // the actual call to java.
    JAVA_CHECK_EXCEPTION(env, "env->CallVoidMethod(clazz, gotoGoogle);"); //find out if the call went through- if not what were the errors.

    env->DeleteLocalRef(activity);
}
[/code]

To define the 'returnWebviewUrl' function we called in Java, we do the following:
[code]
extern "C" {
    JNIEXPORT jstring JNICALL Java_org_libsdl_app_SDLActivity_returnWebviewUrl (JNIEnv *env, jobject obj, jstring url)
    {
        LOGDEBUG("Java_org_libsdl_app_SDLActivity_returnWebviewUrl()");
        const char* result = env->GetStringUTFChars(url, 0);
        if (result != NULL)
        {
            String s = String(result);
            LOGDEBUG(s);
        }
        env->ReleaseStringUTFChars(url, result);
        return env->NewStringUTF("Hello from C++ over JNI!");
    }
}
#endif[/code]

Note the name of the function, it has to follow a strict naming convention for Java to find it. It should also be in the global scope.

And that's it ! Pretty simple, although you will need to put your own logic in. Also, currently there's no way to escape the webview if it gets stuck loading-- so you will need to provide your own options (eg, capture the 'back' button, provide GUI elements, etc).

-------------------------

