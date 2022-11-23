UrOhNo3D | 2017-01-02 01:08:25 UTC | #1

Hi,

I am looking to build a single executable which does not need to reference resource files by simply including them all so that it can be distributed as a single file, as I do not wish for the images, etc, to be easily available when distributed.

Is there a simple way to do this?
Thanks! :smiley:

-------------------------

1vanK | 2017-01-02 01:08:25 UTC | #2

EDIT: U can pa?k resources by using bin\tool\PackageTool.exe

-------------------------

UrOhNo3D | 2017-01-02 01:08:25 UTC | #3

Fundamentally, this still leaves the resources exposed separate form the application. A self-extracting archive will still leave the files as editable once it has extracted!

Is there no way to add their data contents into the application itself?

-------------------------

1vanK | 2017-01-02 01:08:25 UTC | #4

[quote="UrOhNo3D"]Fundamentally, this still leaves the resources exposed separate form the application. A self-extracting archive will still leave the files as editable once it has extracted!

Is there no way to add their data contents into the application itself?[/quote]

i fixed my post :)

-------------------------

Sir_Nate | 2017-01-02 01:08:28 UTC | #5

I don't believe that it is possible internally with Urho3D, but you could try something suggested on [stackoverflow.com/questions/4158 ... -using-gcc](http://stackoverflow.com/questions/4158900/embedding-resources-in-executable-using-gcc)

Also, if you are doing this because of intellectual property concerns, you should be aware that such resources can probably still be extracted from the executable with only slightly more difficulty than from the package file. (And even if they couldn't -- e.g. if you encrypted them -- it is still possible to obtain the resources by dumping the memory and extracting the models and textures from that (though this should be far more difficult)).

If, on the other hand, you are doing it in order to prevent cheating, you could consider storing checksums for the resources, and comparing those checksums to computed checksums for the resources when you use them.

And your other option is to create all of your resources in code -- I know it can be done with models, at least, and it should be possible with images, but this is likely not the kind of solution you are looking for.

-------------------------

cadaver | 2017-01-02 01:08:28 UTC | #6

It should be possible to concatenate a package file to the executable, then simply attempt to open the executable as a package. If you look at PackageFile::Open() code, if it fails to get the package header from the file beginning, it seeks to file end, reads a size value which is used as negative offset, and retries. This was done on request for the exe-linking scenario.

-------------------------

Canardian | 2017-01-02 01:08:33 UTC | #7

Single exe apps are indeed possible.

Urho3D's PackageFile->Open(fileName[,startOffset]) method checks first for the package ID ("UPAK" or "ULZ4") at the beginning of the exe, and then gets the package file length from the end of the exe (in this case a file which has exe+pak copied together as one singleexe), and then seeks to the beginning of the pak file inside the singleexe.

So, first I compile my app, and then copy the exe+pak into one single exe:
[code]copy /b AppCode.exe+AppData.pak AppFinal.exe[/code]
In my app's Setup method, I do this:
[code]engineParameters_["ResourcePaths"] = "";    // we need to clear this, so that "Data" resource path is not used
SharedPtr<PackageFile> package(new PackageFile(context_));
package->Open("AppFinal.exe");
GetSubsystem<ResourceCache>()->AddPackageFile(package);
[/code]
And then I have in CodeBlocks' linker options the -static option also, so that the app doesn't need the MinGW runtime dll's either.

-------------------------

