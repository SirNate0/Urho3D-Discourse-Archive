Miegamicis | 2019-01-18 09:51:05 UTC | #1

Does anyone know how to get the HTTPS requests work in the engine? For now HttpRequest only support HTTP requests, HTTPS request fail with the message "SSL is not initialized". Documentation is a bit scarse and cover mostly the web server part.

-------------------------

weitjong | 2019-01-18 20:14:12 UTC | #2

Although the underlying 3rd-party lib (Civetweb) supports SSL, however, we don't use the original CMakeLists.txt from the upstream. So, there is no way we can enable the SSL build option at the moment (unless you hack your way in and make the necessary changes).

-------------------------

Miegamicis | 2019-01-18 17:38:20 UTC | #3

Already tried few options, none of them worked. Maybe while I'm at it it's worth updating the civetweb too, as I checked, current version is from 2015.

-------------------------

weitjong | 2019-01-18 17:49:22 UTC | #4

Yes. That would be great. As I understand it, the lib itself depends on OpenSSL library. So the build system needs to be adjusted as well to pull in the deps.

-------------------------

Miegamicis | 2019-01-22 10:31:03 UTC | #5

I got so far that my implementation is now working on unix systems which by default comes with the openssl, as far as I know. But I'm having difficulty with the MinGW builds. What would be the best way to pull in OpenSSL dependency for these builds? Prebuilt Urho3D repository for openssl? Prebuilt Docker image? 

Also I still have to test this with Visual Studio builds, I hope nothing unusual will pop out.

-------------------------

weitjong | 2019-01-22 10:58:29 UTC | #6

Why don’t you just modify the http request demo and let the CI test it so you don’t need to perform this yourself.

-------------------------

Miegamicis | 2019-01-22 11:22:24 UTC | #7

I already modified `43_HttpRequestDemo`. CI completes without errors, but when making actual HTTPS request, error will be generated in the console: 
```ERROR: HttpRequest error: SSL is not initialized```

-------------------------

weitjong | 2019-01-22 11:36:41 UTC | #8

If you exit the app with an error status then the error should ripple back up to CI.

-------------------------

Miegamicis | 2019-01-22 12:21:26 UTC | #9

It's a silent error. So the app will not be terminated

-------------------------

Leith | 2019-01-24 09:08:27 UTC | #10

I'm going to make an issue of this, I tend to use web connections in my games, and https is increasingly important, I don't know anything about the issue (or issues) yet, but I just added it to my list.

-------------------------

Miegamicis | 2019-01-24 09:23:27 UTC | #11

No need, there is already branch with my changes here which seem to work: https://github.com/urho3d/Urho3D/tree/civetweb-update

Will make PR a bit later

-------------------------

Leith | 2019-01-24 09:34:14 UTC | #12

All good :wink: At least I can reserve my energy for other issues!

-------------------------

