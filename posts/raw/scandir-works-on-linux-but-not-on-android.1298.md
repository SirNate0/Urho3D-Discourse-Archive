practicing01 | 2017-01-02 01:06:40 UTC | #1

Hello, the size of the results is 0 when running ScanDir on android but the right size when ran on linux.  Am I doing something wrong?  Thanks for any help.

[code]
Vector<String> files;

main_->filesystem_->ScanDir(files,
		main_->filesystem_->GetProgramDir() + "Data/Urho2D/" + name + "/animations/",
		"*", SCAN_FILES, false);
[/code]

-------------------------

cadaver | 2017-01-02 01:06:40 UTC | #2

ScanDir unfortunately doesn't work inside the .apk, at least at the moment. However, there is an API call in the Android AssetManager which should allow at least limited support, it's just a matter of trying it out.

-------------------------

