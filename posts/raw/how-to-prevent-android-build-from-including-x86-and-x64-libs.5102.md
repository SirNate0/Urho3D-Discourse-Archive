att | 2019-04-15 01:07:15 UTC | #1

I have noticed that x86 and x86_64 lib exist in the lib folder of apk, how can prevent it?
This will make the apk size very big.

-------------------------

weitjong | 2019-04-15 02:00:33 UTC | #2

Use the `ANDROID_ABI` Gradle parameter. If it is set, it is expected to be a comma separated list of ABI without any white spaces. So, list all the ABIs you need.

-------------------------

