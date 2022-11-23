umen | 2017-01-02 01:09:03 UTC | #1

I think is deserved dedicated thread .
reading this : [urho3d.github.io/documentation/1 ... lding.html](http://urho3d.github.io/documentation/1.4/_building.html)  in the documentation 
or this thread : [topic1406.html](http://discourse.urho3d.io/t/android-unable-to-find-resource-paths/1357/1)
i didn't understand what i should do .
i compiled successfully the 23_Water example and tried to deploy it to my device ( iPhone 5 ) 
but it gave me error :
[code]
015-12-26 09:13:11.843 23_Water[1486:864806] Created 1 worker thread
2015-12-26 09:13:11.848 23_Water[1486:864806] Added resource path /private/var/mobile/Containers/Bundle/Application/FB626FAB-96FD-41D1-87AD-504FE05A3423/23_Water.app/Data/
2015-12-26 09:13:11.849 23_Water[1486:864806] Added resource path /private/var/mobile/Containers/Bundle/Application/FB626FAB-96FD-41D1-87AD-504FE05A3423/23_Water.app/CoreData/
2015-12-26 09:13:11.850 23_Water[1486:864806] Skipped autoload path 'Autoload' as it does not exist, check the documentation on how to set the 'resource prefix path'
[/code]

from SDL_uikitopenglview.m
line 96 
[code][context renderbufferStorage:GL_RENDERBUFFER_OES fromDrawable:(CAEAGLLayer*)self.layer];[/code]
[img]http://i.imgur.com/YJvpHkn.png[/img]

also all my data files are in the bin directory 

[img]http://i.imgur.com/iFscsTk.png[/img]

is there something that i missed in creating the or deployment  the project to device ?

-------------------------

weitjong | 2017-01-02 01:09:04 UTC | #2

To my understanding, the autoload is a feature not a bug.  :wink:
The message you observed should just be a warning log entry instead of an error log entry. In other platform you can see the distinction of the log entry type more clearly. In iOS platform it looks like the log entry type is not displayed. Do you actually have any specific problem with your app despite all this? BTW, we all get this warnings unless we actually have the "autoload" directory created. Perhaps we could silence this warning.

-------------------------

umen | 2017-01-02 01:09:04 UTC | #3

Thanks for the replay , maybe i was misunderstood 
but i have exception in deployment see line 96 in the picture 
and the log print is the last thing i see   , maybe it warning but it the last thing .
so the problem is the exception not the log.

-------------------------

weitjong | 2017-01-02 01:09:04 UTC | #4

I see. Perhaps then you need to change the subject of this topic. As for your exception, I have no idea what went wrong.

-------------------------

umen | 2017-01-02 01:09:09 UTC | #5

Did some successfully deployed to iOS real device , it seams that there is always problems with iOS device deployment . no matter what version .
Thanks

-------------------------

weitjong | 2017-01-02 01:09:10 UTC | #6

There is a bug in iOS 8.2 on your iPhone. See: [github.com/BradLarson/GPUImage/issues/2022](https://github.com/BradLarson/GPUImage/issues/2022).

-------------------------

