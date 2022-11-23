Pihozamo | 2019-04-29 13:08:04 UTC | #1

Hello, 

I was trying out Urho3D on Android, and checking the forums, it seems that some people had success on running the Launcher app, however, I can't get it to install. Is anyone having the same issue? I know the Android build had some changes recently, but it seems that people managed to get it working.

-------------------------

Miegamicis | 2019-04-29 13:19:30 UTC | #2

In some cases the application fails to install on my phone when the Google Play app has access to the internet. It's a random issue not just with the Urho3D app.

-------------------------

Pihozamo | 2019-04-29 13:43:16 UTC | #3

Yeah I saw something about the google app store scanner messing up with the installation, so I disabled it. I tried installing it without internet, but it's still failing. It fails to install too on android emulator (tried Android 8 and 9).

-------------------------

weitjong | 2019-04-29 15:06:04 UTC | #4

I almost always use SHARED lib type during development of the build script and I have never encountered any installation error before, at least not the one you guys described above.

-------------------------

Pihozamo | 2019-04-29 15:59:04 UTC | #5

I followed the tutorial on [here](https://urho3d.github.io/documentation/HEAD/_building.html#Building_Android), so I'm assuming that's the way you compiled it? I'm using Linux and Android Studio btw

-------------------------

weitjong | 2019-04-29 17:07:29 UTC | #6

Yes. That is the right page. That section was rewritten by me, unless I have I forgotten anything then what’s described in there is how I do the Android build.

I am using Linux host and IntelliJ IDEA as my IDE. I also just invoke Grade wrapper via CLI. At the initial stage I used Android Studio too. After the Gradle version upgrade recently, I believe you need to use preview version of the Android Studio. I wonder that is the cause. Using IntelliJ IDEA allows me to explore the bleeding edge of the Gradle with no sweat.

-------------------------

Pihozamo | 2019-04-29 17:34:54 UTC | #7

Tried again but this time building with ./gradlew build, same thing. As for the version, I'm using the Canary build of Android Studio, since it's the only one that uses Gradle 3.5.

-------------------------

elix22 | 2019-04-29 19:06:46 UTC | #8

It's not clear from your post what exactly is failing , any errors ?  .
I don't have any issues with either compiling or installing on any android device with any version ( I have many of them :slight_smile: ) , never tried it on an emulator .

The following works for me ( I am using Mac , but I guess it should work also on a Linux machine)

Make sure that your .bashrc is configured correctly specifically these environment variables should be set pointing to your SDK and NDK.
ANDROID_NDK_HOME
ANDROID_NDK
ANDROID_HOME
In addition your PATH (in .bashrc)  should also contain "Android/sdk/tools"

For development I am using
./gradlew assembleDebug -P URHO3D_LUA=0 -P ANDROID_ABI=armeabi-v7a -P URHO3D_ANGELSCRIPT=1

The generated APK can be found in 
 Urho3D/android/launcher-app/build/outputs/apk/debug/launcher-app-armeabi-v7a-debug.apk

installing using adb 
adb install -r launcher-app-armeabi-v7a-debug.apk

-------------------------

Pihozamo | 2019-04-29 19:31:06 UTC | #9

Ok gonna try to do it that way, will update shortly. 

And about that error, that's the thing, it just fails to install with no error whatsoever. [Here](https://i.imgur.com/NO0S4h4.png) is a print from the emulator, and there's no log too. The .apk I trying to install is the one generated on the release build named "launcher-app-release-unsigned.apk".

-------------------------

elix22 | 2019-04-29 19:40:39 UTC | #10

Well the error is obvious , your apk is not signed .
launcher-app-release-unsigned.apk
You have to sign it with release keys.

using my way it will sign it with debug keys , will allow you to install it .
Once again I am not sure that using an emulator is the right way to go , you have to try it on a real device

-------------------------

Pihozamo | 2019-04-29 19:46:20 UTC | #11

Well, that may be, however, I enabled the installation from unknown sources, so that shouldn't be an issue. However who knows, I will try it later. I also tried on a real device, same thing.

-------------------------

Pihozamo | 2019-04-29 20:56:38 UTC | #12

Update: following your way it works just fine! Apparently even if you turn on accept unknown sources on the android settings, you still gotta sign it. After following the tutorial [here](http://www.androiddevelopment.org/2009/01/19/signing-an-android-application-for-real-life-mobile-device-usage-installation/) I self-signed the .apk and now it installs just fine. 

Thanks everyone for your help.

-------------------------

weitjong | 2019-04-29 23:35:08 UTC | #13

Glad you figured it out already. Just want to add that using the IDE then one can install by a click of a button. :smiley:

-------------------------

Pihozamo | 2019-04-30 01:43:40 UTC | #14

Dammit, now what's happening is that when I build the release version of the launcher app, I can't run any examples, they all crash. There's no log output either.

-------------------------

Pihozamo | 2019-05-01 12:48:43 UTC | #15

So there's no way to get it running on release? You guys always use it on debug?

-------------------------

elix22 | 2019-05-03 06:16:44 UTC | #16

Yes , it's a known issues , there are some threads talking about it .
The fix is very simple 
You have to modify 2 functions as shown below

```
unsigned VectorBuffer::Write(const void* data, unsigned size)
{
    if (!size)
        return 0;

    if (size + position_ > size_)
    {
        size_ = size + position_;
        buffer_.Resize(size_);
    }

    auto* srcPtr = (unsigned char*)data;
    unsigned char* destPtr = &buffer_[position_];
    position_ += size;
    memcpy(destPtr, srcPtr, size);

    return size;
}
```

```
unsigned MemoryBuffer::Write(const void* data, unsigned size)
{
    if (size + position_ > size_)
        size = size_ - position_;

    if (!size)
        return 0;

    auto* srcPtr = (unsigned char*)data;
    unsigned char* destPtr = &buffer_[position_];
    position_ += size;
    memcpy(destPtr, srcPtr, size);

    return size;
}
```

-------------------------

Pihozamo | 2019-05-02 00:58:44 UTC | #17

Thanks, honestly it wouldn't be such a big issue if it weren't for the way larger file size :stuck_out_tongue:

By changing those funcs nothing else changes? What's the downside?

-------------------------

elix22 | 2019-05-03 08:56:23 UTC | #18

There is no downside , the  upside is that it fixes unaligned write on ARM

You can read about it in https://github.com/urho3d/Urho3D/issues/2386 

It should be merged into master

-------------------------

weitjong | 2019-05-03 12:18:53 UTC | #19

PR is welcome.......

-------------------------

elix22 | 2019-05-03 17:52:44 UTC | #20

Done
20  characters .

-------------------------

weitjong | 2019-05-04 01:47:07 UTC | #21

Thanks for your PR. It is merged.

-------------------------

elix22 | 2019-05-04 12:31:42 UTC | #22

While working on my code 
I found one more use case of Android crash in ARM/release configuration while calling MemoryBuffer::Read() or VectorBuffer::Read()

Previous fix was for crash  on MemoryBuffer::Write() , VectorBuffer::Write() 

updated the PR
https://github.com/urho3d/Urho3D/pull/2445

-------------------------

weitjong | 2019-05-04 14:47:51 UTC | #23

Yeah, I also have a feeling the same pattern of code might get used in a few places in our code base.

-------------------------

