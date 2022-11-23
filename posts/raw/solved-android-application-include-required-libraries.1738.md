mightymarcus | 2017-01-02 01:09:48 UTC | #1

I'm using Urho3D from haxe (a language that compiles to cpp). For the windows build it's no problem, I know which additional libraries I have to include in my test application.

winmm.lib
imm32.lib
opengl32.lib
kernel32.lib

and some others.

But I don't know for a android build. I included libOpenGLESv2.lib but now I don't know where I have to look for the remaining libraries.

C:\Users\mighty\Urho3D\buildandroidphysics\libs\armeabi-v7a\libUrho3D.a(SDL_android.c.o):SDL_android.c:function Android_JNI_GetNativeWindow: error: undefined reference to 'ANativeWindow_fromSurface'

Maybe someone could explain me how I can build an application for Android on Windows 10 without using Eclipse.

-------------------------

mightymarcus | 2017-01-02 01:09:50 UTC | #2

So no one knows which libraries I need to include?

-------------------------

sovereign313 | 2017-01-02 01:09:51 UTC | #3

Why not just build the APK on the command line?  Then it will have everything you need in the apk, without having to worry about the specific libs.
I suppose you could build the APK on the command line, and then extract it in a new folder to see what it ships with, if you really need to know.

-------------------------

rasteron | 2017-01-02 01:09:51 UTC | #4

You can try and use cmake_generic.sh or bat to peek at the generated makefiles but looking at this error, it looks like you forgot to include the required SDL and/or NDK libraries..

[quote="mightymarcus"]
C:\Users\mighty\Urho3D\buildandroidphysics\libs\armeabi-v7a\libUrho3D.a(SDL_android.c.o):SDL_android.c:function Android_JNI_GetNativeWindow: error: undefined reference to 'ANativeWindow_fromSurface'
[/quote]

-------------------------

mightymarcus | 2017-01-02 01:09:51 UTC | #5

[quote="sovereign313"]Why not just build the APK on the command line?  Then it will have everything you need in the apk, without having to worry about the specific libs.
I suppose you could build the APK on the command line, and then extract it in a new folder to see what it ships with, if you really need to know.[/quote]


I'm using another language which can compile to different native cpp code, e.g. windows, linux, android, iOS.

I can include header files and libs and can specify the directories.

And then I can call the native methods from my IDE (for haxe) through extern classes.

[code]
@:include("Urho3D/Engine/Application.h")
@:native("Urho3D::Application")
@:structAccess
@:unreflective
extern class UrhoApplication
{
	public var engine_:Pointer<Engine>;
	public function Run():Int;
	public function Setup():Void;
	public function Start():Void;
	public function Stop():Void;
}
[/code]

It will then be linked and compiled and packaged to apk all together through the haxe compiler.

With the windows build it was no problem, I just included the files that where included in Visual Studio too.

Urho3D.lib
winmm.lib
imm32.lib
opengl32.lib
kernel32.lib
version.lib
ws2_32.lib
user32.lib
gdi32.lib
winspool.lib
shell32.lib
ole32.lib
oleaut32.lib
uuid.lib
comdlg32.lib
advapi32.lib

But for android I dont know which libraries I have to include, just two of them.

libUrho3D.a
libGLESv2.so

I guess I need libSDL.a and some others to.

But I don't know which ones and where they are.

-------------------------

weitjong | 2017-01-02 01:09:52 UTC | #6

What rasteron has suggested makes sense. If I were you, I would also do a search myself in the source files. Urho3D project is OSS, so take the full benefit of it. Afterall you already know the keyword to search for, like winmm or imm32. Since Urho3D build system supports Android out of the box along with Win32 platform, you will surely find whatever the good "bits" that define the winmm/imm32 for Win32 may be also the one responsible for defining dependency libs for Android platform. Hint: it is in our CMake common module. Another hint: git grep keyword.

-------------------------

mightymarcus | 2017-01-02 01:09:52 UTC | #7

[quote="weitjong"]What rasteron has suggested makes sense. If I were you, I would also do a search myself in the source files. Urho3D project is OSS, so take the full benefit of it.[/quote]

I have to dig into the source code anyways if I want to write my extern classes, and I had to rename e.g. Urho3D::String to Urho3D::UrhoString to bypass conflicts with haxe (there is a String class too) and had to alter the source code with #ifdef RegisterClass #undef RegisterClass (windows ...) to get it working. :wink:

[quote="weitjong"]Afterall you already know the keyword to search for, like winmm or imm32. Since Urho3D build system supports Android out of the box along with Win32 platform, you will surely find whatever the good "bits" that define the winmm/imm32 for Win32 may be also the one responsible for defining dependency libs for Android platform. Hint: it is in our CMake common module. Another hint: git grep keyword.[/quote]

I am very new to Android Development, so I hoped someone can help me right away, but of course I will find it myself too.The hint is indeed helpful, thanks.

-------------------------

mightymarcus | 2017-01-02 01:09:53 UTC | #8

[quote]    if (${TARGET} MATCHES SDL|Urho3D)

        if (WIN32)

            list (APPEND LIBS user32 gdi32 winmm imm32 ole32 oleaut32 version uuid)

        elseif (APPLE)

            list (APPEND LIBS dl)

        elseif (ANDROID)

            list (APPEND LIBS dl log android)
[/quote]

Finally I got it ... libdl.so liblog.so libandroid.so

-------------------------

sovereign313 | 2017-01-02 01:09:55 UTC | #9

Sweet!

Thanks for the follow up.

-------------------------

weitjong | 2017-01-02 01:09:56 UTC | #10

Glad to hear that you have figured it out. However, what you see now may be changed in the future without prior notice.

-------------------------

mightymarcus | 2017-01-02 01:10:02 UTC | #11

No problem.

[SOLVED]

-------------------------

