weitjong | 2019-04-15 02:03:55 UTC | #1

Well, not quite there yet. I think I am able to publish the library to bintray now if I have an actual release version. However, I cannot do it just yet because we don't have a release version and it does not accept anything with '-SNAPSHOT' as the version name. I learnt that the hard way. The snapshots would have to go to Artifactory. But at the very least I have tested the build script to publish to bintray already (just for testing only).

-------------------------

weitjong | 2019-04-15 02:25:59 UTC | #2

After sleeping on it, I have decided to keep thing simpler by not having SNAPSHOT version uploaded to Artifactory. It means on the jcenter there will be “release” versions: rolling release and stable release. For example:

* 1.8-BETA (rolling release from CI/CD)
* 1.8 (actual point release after git tagging)

There is subtle difference between `*-SNAPSHOT` and the proposed `*-BETA` versioning scheme. The Gradle build system will auto-invalidate the snapshot version from download cache after a configured period, while it won’t do this for the latter. User would have to invalidate the cache manually or set a flag for Gradle to refresh the dependencies. I think we can live with that and in fact could be better even for our case.

-------------------------

weitjong | 2019-04-15 16:27:53 UTC | #3

Yes! My request to include the 'urho3d-lib' package in JCenter has been approved. Next, I will have to figure out how to make Travis-CI performs the continuous deployment to bintray and also to figure out how to build a universal AAR with all the ABIs included without exceeding the 50 minutes job limit that our free account imposed.

-------------------------

Miegamicis | 2019-04-15 19:47:18 UTC | #4

Great news! Looking forward for the future build options.

-------------------------

weitjong | 2019-04-16 00:34:07 UTC | #5

With the Urho3d AAR already in JCenter, it means user “just” need to declare the lib as one of its dependency in the Gradle build script in order to use the lib. I have added some extra stuff (C++ headers, etc) in the AAR, so the downstream build script requires some custom Gradle tasks to extract them out. The custom Gradle tasks can be implemented inside a custom Gradle plugin too, so it can be easily shared and reused in the downstream build script simply by applying the plugin. This is why I have a plugin skeleton code checked in already a few months ago. That’s the original grand plan. :)

-------------------------

weitjong | 2019-04-17 00:44:23 UTC | #6

I have created a new dev branch called ‘using-AAR‘. The Bintray upload task is configured there now and should be a no brainer to get it invoked by Travis “securely”.

Looking at the typical Android CI build time, I think at most we could get away with having two ABIs in a single build. So probably it would be “x86_64,x86” and “arm64-v8a,armeabi-v7a”.

-------------------------

Modanung | 2019-04-17 11:57:24 UTC | #7

That all sounds pretty cool.

I assume you plan to extend the documentation as well? [:green_book:](https://urho3d.github.io/documentation/HEAD/_building.html#Building_Android)

-------------------------

weitjong | 2019-04-17 12:38:35 UTC | #8

Yes, the doc will be updated accordingly when it is ready to be merged. Now the bespoke custom plugin is not even completed.

-------------------------

weitjong | 2019-04-19 10:28:47 UTC | #9

[quote="weitjong, post:6, topic:5103"]
I have created a new dev branch called ‘using-AAR‘. The Bintray upload task is configured there now and should be a no brainer to get it invoked by Travis “securely”.
[/quote]

It was slightly complicated than I thought. The uploading mechanism from the bintray plugin works like a charm, the complication actually come from the necessity to encrypt the API key in the environment variable and make that variable pass a long nicely from Travis-CI VM to our docker container.

-------------------------

weitjong | 2019-04-22 02:48:11 UTC | #10

[quote="weitjong, post:6, topic:5103"]
Looking at the typical Android CI build time, I think at most we could get away with having two ABIs in a single build. So probably it would be “x86_64,x86” and “arm64-v8a,armeabi-v7a”.
[/quote]

Without the build cache, CI only got enough time for two ABIs and not exceeding 50 minutes limit. But with a good cache, I reckon it only needs less than 30 minutes for all four ABIs. I still want a universal AAR and I think there is a way to achieve that now.

-------------------------

weitjong | 2019-04-24 00:34:30 UTC | #11

It looks like the (free) OSS account on Bintray imposes individual file upload size to 250MB. So after painstakingly setting up the build mechanism on Travis-CI to workaround the universal AAR build with its 50 minutes build time limit for free account,  now I am having another limit for publishing it. Sigh. I may have to skip the publishing of STATIC AAR as it is the only one exceeding and move on to the plugin development. BTW, user can always build the AAR locally too using `./gradlew publishToMavenLocal`. It is not documented in our online doc but it is actually one of the standard gradle task when `maven-publish` plugin is applied. You just need to have a host machine with plenty of memory to do a universal build.

-------------------------

weitjong | 2019-04-25 01:04:24 UTC | #12

Not giving up. It appears only the STATIC-debug AAR is exceeding the limit and the STATIC-release is still within the limit. So, reconfigure to exclude the former only.

Edit: It works.

-------------------------

