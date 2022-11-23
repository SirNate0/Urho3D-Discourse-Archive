theak472009 | 2017-01-02 01:07:41 UTC | #1

Hey, good work on the GI project. Too bad it did not reach the finish line.
I am just curious about your Lightmapping project and cannot get it to run from editor. It always says in the LightmapSettings window, generation is disabled. Is it still work in progress?

-------------------------

theak472009 | 2017-01-02 01:07:41 UTC | #2

Thanks man.
Its awesome that you know so much stuff and are willing to share it with all of us.

-------------------------

cadaver | 2017-01-02 01:07:43 UTC | #3

One thing has puzzled me in the lightmapping work. (Why) is it mandatory that the lightmaps be compiled into a PAK file? The Urho resource system itself would not differentiate between filesystem and package access. It of course prevents writing a ton of files and cluttering a directory, but there can be trouble in these cases:

- User wants to compile the whole final project into a pak of its own, in this case pak inside pak isn't supported
- On Android, pak files likewise are not supported, as the project assets are rather packaged into the apk, and individual file access into a pak inside the apk would likely be suboptimal.

-------------------------

