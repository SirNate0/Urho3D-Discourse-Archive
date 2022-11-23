jijingLiu | 2017-01-02 01:12:03 UTC | #1

i have build an apk, and use PackageTool to pack resources.
but i got error here:
[code]
bool PackageFile::Open(const String& fileName, unsigned startOffset)
{
#ifdef ANDROID
    if (URHO3D_IS_ASSET(fileName))
    {
        URHO3D_LOGERROR("Package files within the apk are not supported on Android");
        return false;
    }
#endif
...
}
[/code]
is there has some reason for  Package files within the apk are not supported on Android and what do i need to do to use PackageTool on android?

-------------------------

cadaver | 2017-01-02 01:12:03 UTC | #2

Files within the .apk have to be accessed using SDL's rwops helper functions (which on Android use the  asset manager). Support for reading files from inside a package file inside an .apk simply hasn't been implemented (yet).

The asset manager functionality is not very good for arbitrary access including file seeks, which the package files support would require, so it's somewhat questionable if this should even be implemented. The .apk already is a package of it's own kind, so I'd just recommend using individual files on Android.

-------------------------

jijingLiu | 2017-01-02 01:12:04 UTC | #3

OK, thanks.

-------------------------

