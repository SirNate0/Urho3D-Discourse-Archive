UnrealDoggie | 2021-03-15 20:21:34 UTC | #1

Hi,
I am wondering if I can add resource dirs during runtime. I am not developing a game but want the
possiblity of creating, saving, loading different scenes during run-time from different directories e.g 
SceneA which contains sceneA.xml + accompanying
Models, Materials subdirectories.

ResourceCache* cache = GetSubsystem<ResourceCache>();
cache->RemoveResourceDir(oldresourcePath);
cache->AddResourceDir(resourcePath); 
scene_->LoadXML(...);

Is this way advisable or there will be issues?

Regards,

-------------------------

vmost | 2021-03-15 21:47:55 UTC | #2

Have you tried testing it out? Seems like your only problems would come from trying to access a resource that doesn't exist.

-------------------------

Modanung | 2021-03-16 06:46:58 UTC | #3

Yes, adding resource folders at run-time is perfectly legitimate.

Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

JSandusky | 2021-03-16 02:47:48 UTC | #4

If you remove a directory while an async load is in progress that depends on it then obviously nothing is going to continue to load and your log will be packed with error messages. If your resources are "overloaded" (same relative name) then portions of the async load will also be scrambled between the the intended and the "new" resource paths.

Otherwise there shouldn't be issues.

-------------------------

UnrealDoggie | 2021-03-16 02:59:09 UTC | #5

Thanks for the assurance & ur welcome!

-------------------------

UnrealDoggie | 2021-03-16 03:14:32 UTC | #6

Thanks for ur reply. So would calling
scene_->StopAsyncLoading() eliminate this concern?
As for the "overloaded" part, I guess I will have to manage between different scenes carefully, hence the RemoveResourceDir as I need to deal with 1 scene at a time.
This leads to the question if I made use of urho3d basic  models like box, cylinder etc, will the scene just reference urho3d default  Models directory?
Thanks.

-------------------------

UnrealDoggie | 2021-03-16 03:23:29 UTC | #7

Hi,
Yes I have. It seems to work but I m a newbie to Urho3d to be sure it is the correct approach. Hence the question.
My first evil way was 
engineParameters_[EP_RESOURCE_PATHS] = resourcePath;// +";Data;CoreData";
engine_->InitializeResourceCache(engineParameters_, false); 
Well it didnt feel right.

Thanks.

-------------------------

JSandusky | 2021-03-16 06:46:58 UTC | #8

Yes, stopping it will (obviously it halts where ever it is at, but you can change scope of UpdateAsyncLoading and call until progress is complete). Only matters if you do use it though, async load is opt-in.

[quote="UnrealDoggie, post:6, topic:6758"]
This leads to the question if I made use of urho3d basic models like box, cylinder etc, will the scene just reference urho3d default Models directory?
[/quote]

Assuming you've left CoreData and Data as directories then yes.

-------------------------

UnrealDoggie | 2021-03-16 08:48:14 UTC | #9

Good to know. Thanks!

-------------------------

