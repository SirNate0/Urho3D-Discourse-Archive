hualin | 2017-01-02 00:59:29 UTC | #1

Hi,
currently the PackageFile is not available on android platform. I tried that put the pak file under Data directory and it could read through ResourceCache. But the fopen can't open it. Therefore the ResourceCache can't read file from the package. 
Is there any way to use package file on android?

-------------------------

cadaver | 2017-01-02 00:59:29 UTC | #2

Consider that on Android the files are already packaged inside the APK. The SDL library handles access to them via the AssetManager; you can assume the files are compressed, and cannot be seeked through normally. Instead seeking is "emulated" by reading the compressed stream from the begin again, until the desired position is reached. In that case we don't want to add our own "layer" of file packaging, as it would (because it involves continuous seeks inside the PackageFile) result in worse performance.

The PackageFile should be functional on Android if you're reading from somewhere else than the APK (like a memory card), but inside the APK it doesn't make sense. So just copy your individual files/directories into the Assets folder for packaging into the APK.

-------------------------

hualin | 2017-01-02 00:59:29 UTC | #3

Well, I see now.
I want to use package file on android, because I want to encrypt the resources. 
Now I will package the file and extract it to the sdcard or internal data folder when the app startup in first time.
Thank you, cadaver.

-------------------------

friesencr | 2017-01-02 00:59:29 UTC | #4

android 4.4 kitkat has had some changes on permission to reading off of sdcards.  Read only might be ok.  You may want to read up on kitkat and memory cards.

-------------------------

hualin | 2017-01-02 00:59:29 UTC | #5

Oh, Thank you, friesencr.
I haven't been noticed that problem.

-------------------------

