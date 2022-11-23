weitjong | 2017-01-02 01:05:06 UTC | #1

All our CI jobs are ccached enabled, even those on Travis CI legacy build infra. I have successfully rolled our own cache store backed by GitHub repository to enable ccache support for legacy build infra. It works better than I expected. I might even say it is better than Travis CI own cache store solution on new infra in certain aspect. We can easily define one cache for each job which is difficult to do using Travis CI native cache solution due to its convoluted configuration setup. We can also easily maintain the cache using GitHub web interface. The cache is nothing more but a git branch in the 'urho3d/cache-store' repository. We can delete a bad cache or tag to backup a good cache easily. With a good cache, a few of our CI jobs take less than 2 minutes to complete now.

For the Urho3D core team members - I also want to let you know the availability of new commit message instructions.
[ul]
[li] [ci only: comma,separated,strings]
This instructs Travis to only create matching CI mirror branch names, thus limiting the number of CI jobs being sent to the queue. This is useful when you need to quickly verify the fix for a certain target platform. The substring is matched using regex.[/li]
[li] [ci scan]
This is a special case to instruct Travis to create the Coverity-Scan mirror branch to trigger a static analysis scan on demand. Note that the static analysis scan job will also be queued automatically when API changes is detected. Do so sparingly as not to exceed the weekly quota set by Coverity Scan service.[/li]
[li] [ccache clear]
This instructs Travis to clear the existing compiler cache before running the build. This is alternative way to clear the cache instead of deleting it from the GitHub web interface.[/li][/ul]

-------------------------

