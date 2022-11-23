amit | 2017-01-02 01:02:14 UTC | #1

hi,
I am tryin to install urho app on andriod, which starts but fails with no real error info.

here is the build detail:
[code]
C:\Downloads\Urho3D-master\Urho3D-master\android-Build>ant release
Buildfile: C:\Downloads\Urho3D-master\Urho3D-master\android-Build\build.xml

-set-mode-check:

-set-release-mode:

-release-obfuscation-check:
     [echo] proguard.config is ${proguard.config}

-pre-build:

-check-env:
 [checkenv] Android SDK Tools Revision 23.0.2
 [checkenv] Installed at C:\android\adt-bundle-windows-x86_64-20140702\sdk

-setup:
     [echo] Project Name: Urho3D
  [gettype] Project Type: Application

-build-setup:
[getbuildtools] Using latest Build Tools: 20.0.0
     [echo] Resolving Build Target for Urho3D...
[gettarget] Project Target:   Android 4.0
[gettarget] API level:        14
     [echo] ----------
     [echo] Creating output directories if needed...
    [mkdir] Created dir: C:\Downloads\Urho3D-master\Urho3D-master\android-Build\bin
    [mkdir] Created dir: C:\Downloads\Urho3D-master\Urho3D-master\android-Build\bin\res
    [mkdir] Created dir: C:\Downloads\Urho3D-master\Urho3D-master\android-Build\bin\rsObj
    [mkdir] Created dir: C:\Downloads\Urho3D-master\Urho3D-master\android-Build\bin\rsLibs
    [mkdir] Created dir: C:\Downloads\Urho3D-master\Urho3D-master\android-Build\gen
    [mkdir] Created dir: C:\Downloads\Urho3D-master\Urho3D-master\android-Build\bin\classes
    [mkdir] Created dir: C:\Downloads\Urho3D-master\Urho3D-master\android-Build\bin\dexedLibs
     [echo] ----------
     [echo] Resolving Dependencies for Urho3D...
[dependency] Library dependencies:
[dependency] No Libraries
[dependency]
[dependency] ------------------
[dependency] API<=15: Adding annotations.jar to the classpath.
     [echo] ----------
     [echo] Building Libraries with 'release'...
   [subant] No sub-builds to iterate on

-code-gen:
[mergemanifest] Merging AndroidManifest files into one.
[mergemanifest] Manifest merger disabled. Using project manifest only.
     [echo] Handling aidl files...
     [aidl] No AIDL files to compile.
     [echo] ----------
     [echo] Handling RenderScript files...
     [echo] ----------
     [echo] Handling Resources...
     [aapt] Generating resource IDs...
     [echo] ----------
     [echo] Handling BuildConfig class...
[buildconfig] Generating BuildConfig class.

-pre-compile:

-compile:
    [javac] Compiling 5 source files to C:\Downloads\Urho3D-master\Urho3D-master\android-Build\bin\classes
    [javac] Note: C:\Downloads\Urho3D-master\Urho3D-master\android-Build\src\org\libsdl\app\SDLActivity.java uses or overrides a deprecated API.
    [javac] Note: Recompile with -Xlint:deprecation for details.

-post-compile:

-obfuscate:

-dex:
      [dex] input: C:\Downloads\Urho3D-master\Urho3D-master\android-Build\bin\classes
      [dex] input: C:\android\adt-bundle-windows-x86_64-20140702\sdk\tools\support\annotations.jar
      [dex] Pre-Dexing C:\android\adt-bundle-windows-x86_64-20140702\sdk\tools\support\annotations.jar -> annotations-b2c506d27df334a4b9c8344e8d238033.jar
      [dex] Converting compiled files and external libraries into C:\Downloads\Urho3D-master\Urho3D-master\android-Build\bin\classes.dex...
       [dx] Merged dex A (26 defs/28.4KiB) with dex B (2 defs/1.1KiB). Result is 28 defs/33.6KiB. Took 0.1s

-crunch:
   [crunch] Crunching PNG Files in source dir: C:\Downloads\Urho3D-master\Urho3D-master\android-Build\res
   [crunch] To destination dir: C:\Downloads\Urho3D-master\Urho3D-master\android-Build\bin\res
   [crunch] Processing image to cache: C:\Downloads\Urho3D-master\Urho3D-master\android-Build\res\drawable-hdpi\icon.png => C:\Downloads\Urho3D-master\Urho3D-ma
ster\android-Build\bin\res\drawable-hdpi\icon.png
   [crunch]   (processed image to cache entry C:\Downloads\Urho3D-master\Urho3D-master\android-Build\bin\res\drawable-hdpi\icon.png: 54% size of source)
   [crunch] Processing image to cache: C:\Downloads\Urho3D-master\Urho3D-master\android-Build\res\drawable-ldpi\icon.png => C:\Downloads\Urho3D-master\Urho3D-ma
ster\android-Build\bin\res\drawable-ldpi\icon.png
   [crunch]   (processed image to cache entry C:\Downloads\Urho3D-master\Urho3D-master\android-Build\bin\res\drawable-ldpi\icon.png: 0% size of source)
   [crunch] Processing image to cache: C:\Downloads\Urho3D-master\Urho3D-master\android-Build\res\drawable-mdpi\icon.png => C:\Downloads\Urho3D-master\Urho3D-ma
ster\android-Build\bin\res\drawable-mdpi\icon.png
   [crunch]   (processed image to cache entry C:\Downloads\Urho3D-master\Urho3D-master\android-Build\bin\res\drawable-mdpi\icon.png: 59% size of source)
   [crunch] Processing image to cache: C:\Downloads\Urho3D-master\Urho3D-master\android-Build\res\drawable\logo_large.png => C:\Downloads\Urho3D-master\Urho3D-m
aster\android-Build\bin\res\drawable\logo_large.png
   [crunch]   (processed image to cache entry C:\Downloads\Urho3D-master\Urho3D-master\android-Build\bin\res\drawable\logo_large.png: 92% size of source)
   [crunch] Crunched 4 PNG files to update cache

-package-resources:
     [aapt] Creating full resource package...
     [aapt]     (skipping file '.gitignore' due to ANDROID_AAPT_IGNORE pattern '.*')

-package:
[apkbuilder] Current build type is different than previous build: forced apkbuilder run.
[apkbuilder] Creating Urho3D-release-unsigned.apk for release...

-post-package:

-release-prompt-for-password:

-release-nosign:
     [echo] No key.store and key.alias properties found in build.properties.
     [echo] Please sign C:\Downloads\Urho3D-master\Urho3D-master\android-Build\bin\Urho3D-release-unsigned.apk manually
     [echo] and run zipalign from the Android SDK tools.
[propertyfile] Creating new property file: C:\Downloads\Urho3D-master\Urho3D-master\android-Build\bin\build.prop
[propertyfile] Updating property file: C:\Downloads\Urho3D-master\Urho3D-master\android-Build\bin\build.prop
[propertyfile] Updating property file: C:\Downloads\Urho3D-master\Urho3D-master\android-Build\bin\build.prop
[propertyfile] Updating property file: C:\Downloads\Urho3D-master\Urho3D-master\android-Build\bin\build.prop

-release-sign:

-post-build:

release:

BUILD SUCCESSFUL
Total time: 1 minute 40 seconds
[/code]


there is not anythin else, I tested on nexus7 old and zyomi mi3, but it doesnt install

-------------------------

amit | 2017-01-02 01:02:14 UTC | #2

I know there i not much info from my side, but there is none, all is smooth except install.
I copy apk to device and install, it starts but fail with no reason.

does anyone has any test apk?

-------------------------

