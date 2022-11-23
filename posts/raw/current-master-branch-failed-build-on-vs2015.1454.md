George | 2017-01-02 01:07:49 UTC | #1

Hello just downloaded the new update from GIT.
There seem to be a little problem with build.

The current master git branch failed to build on VS 2015 with the following error in the file DebugMemoryLeachCheck.h
This is in VS ultimate edition.


Severity	Code	Description	Project	File	Line	Suppression State
Error	C2323	'operator delete[]': non-member operator new or delete functions may not be declared static or in a namespace other than the global namespace	kNet	E:\ProjectCodes\GitHub\Urho3D\Source\ThirdParty\kNet\include\kNet\DebugMemoryLeakCheck.h	52	
Error	C2323	'operator new': non-member operator new or delete functions may not be declared static or in a namespace other than the global namespace	kNet	E:\ProjectCodes\GitHub\Urho3D\Source\ThirdParty\kNet\include\kNet\DebugMemoryLeakCheck.h	37	
Error	C2323	'operator new[]': non-member operator new or delete functions may not be declared static or in a namespace other than the global namespace	kNet	E:\ProjectCodes\GitHub\Urho3D\Source\ThirdParty\kNet\include\kNet\DebugMemoryLeakCheck.h	42	
Error	C2323	'operator delete': non-member operator new or delete functions may not be declared static or in a namespace other than the global namespace	kNet	E:\ProjectCodes\GitHub\Urho3D\Source\ThirdParty\kNet\include\kNet\DebugMemoryLeakCheck.h	47	

Anyone know how to solve this issue?

Thanks

-------------------------

George | 2017-01-02 01:07:49 UTC | #2

Seems like the Network module is broken.

I unchecked URHO3D_NETWORK option in CMake and it builds fine in VS2015.

Regards

-------------------------

cadaver | 2017-01-02 01:07:49 UTC | #3

Which .cpp file was it compiling when you did get this error?

DebugMemoryLeakCheck.h itself does not define a namespace, so this would look like the file is included somewhere from within a namespace erroneously. Personally I've not seen this error in VS debug builds.

Alternatively, if the static keyword is the problem, does removing it allow the compilation to finish? Again, not seen this on VS2015 personally; this particular file has been unchanged for a long time.

-------------------------

George | 2017-01-02 01:07:49 UTC | #4

Hi mate,
I'm not sure my self. It was previously build just fine. I think the last time I build Urho3D was approximately 1 month ago, which built just fine. 

I'm not sure what has been updated. It could be VS2015 update1 that is causing the issue.

Let me delete everything and rebuilt it to make sure.

Regards

-------------------------

George | 2017-01-02 01:07:49 UTC | #5

Hi I've just did a complete rebuild.

Disable URHO3D_NETWORK option in CMake Gui is the only thing that makes VS2015 build. But now I don't have the network module.

Regards

-------------------------

cadaver | 2017-01-02 01:07:49 UTC | #6

Ok. Will try to install the update and reproduce.

-------------------------

cadaver | 2017-01-02 01:07:49 UTC | #7

Reproduced and fixed in master branch.

-------------------------

