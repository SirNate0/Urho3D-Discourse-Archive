weitjong | 2017-01-02 01:04:51 UTC | #1

We have just completed the Coverity scan on our project. The initial result ([scan.coverity.com/projects/4954](https://scan.coverity.com/projects/4954)) shows our defect density is a little bit higher than other open source projects having similar code size to ours. The defects have not been categorized yet but 832 of 1252 are actually defects from third party libs, so actually our code base quality is not that bad. It can be better of course. Coverity provides a nice web interface to track the defects which encourage team work to categorize and take action on the defects together. So what are you waiting for?  :wink:

-------------------------

weitjong | 2017-01-02 01:04:51 UTC | #2

False positive is a common problem with such static analysis scanning tool. The last step in the configuration, which we have not done it yet, is to upload a so called "modeling file" to teach the tool what to expect and what not from our code base. After this is done, then the false positive should drop to around 10% (as claimed by Coverity Scan). And yes, we need all the help for creating the modeling file too.

-------------------------

sabotage3d | 2017-01-02 01:04:51 UTC | #3

It is worth double checking with Clang Static Analyzer as it is success rate is a lot higher .

-------------------------

weitjong | 2017-01-02 01:04:51 UTC | #4

[quote="sabotage3d"]It is worth double checking with Clang Static Analyzer as it is success rate is a lot higher .[/quote]
Clang static analyzer is a standalone tool. The Coverity Scan is a complete suit of scanning service. It took me only a few hours to read their online pages to figure out how to integrate it with Travis CI (which BTW also already has ready-made "addons" to enable the integration). So even if the former can do better in respect to producing less false positive out of the box, I just don't see how we can integrate with our CI build that easily.

-------------------------

sabotage3d | 2017-01-02 01:04:52 UTC | #5

SDL has a buildbot running it every commit at [buildbot.libsdl.org/waterfall](https://buildbot.libsdl.org/waterfall) .
But you are right my information could be outdated there are too many services now that could be superior.

-------------------------

weitjong | 2017-01-02 01:04:52 UTC | #6

The Buildbot framework looks like a viable alternative for automation of CI, deployment, and release management. From what I understand from its online documentation, it requires a machine to host the service though. We have configured our Travis CI workers (bots) to perform all that kind of automation (including site documentation update and now static analysis scan) for us from the cloud without paying any hosting cost. I am sure if we really want to, we could manually integrate "Clang static analyzer" into our CI build. What I am not sure about are:
[ul][li] How much less false positive it may produce? If at the end we also need to "tune" it in order to suppress them then it is not worth the trouble.[/li]
[li] Will the scanning and analysis time exceed the 50 minutes limit set by Travis CI for non-paying customers like us. With Coverity Scan, the work is offloaded to their server.[/li]
[li] Where will we track those defects report?[/li][/ul]
IMHO, we should give a little time to see how much benefit this current setup bring to our code quality. If in the end it does not help at all then we could just remove it.

-------------------------

weitjong | 2017-01-02 01:08:03 UTC | #7

Since it appears that no one cares much about the result of the static analyzer, I have removed the Coverity Scan status badge with AppVeyor build status badge in the home page of our main website. The scan will still continue to run in the background.

-------------------------

