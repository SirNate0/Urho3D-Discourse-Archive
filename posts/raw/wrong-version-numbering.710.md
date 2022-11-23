Enhex | 2017-01-02 01:02:19 UTC | #1

I noticed that Urho3D got wrong version numbering - mistaking the point to a decimal number instead of a separator.
This is wrong because what happens after x.99?

Usually version numbers go like this:
major.minor.patch

When major means big change to the API, usually something that isn't compatible with previous major versions.
Minor means additions to the API that shouldn't break anything.
Patch means small bug fixes, optimizations, and other things which don't change the API.

This way it gives developers useful info like if they can upgrade their project to a newer version without breaking it, and if there's new features.

In order to fix it you can start with a minor version equal to the highest number you have so far(32) and continue counting from there.

-------------------------

weitjong | 2017-01-02 01:02:35 UTC | #2

[quote="Enhex"]Usually version numbers go like this:
major.minor.patch

When major means big change to the API, usually something that isn't compatible with previous major versions.
Minor means additions to the API that shouldn't break anything.
Patch means small bug fixes, optimizations, and other things which don't change the API.[/quote]
Why you have the impression that this is not already the case? Our library version has major.minor.patch format. See "librevision.h" file. The major.minor is derived from our Git release tag, while the patch is derived from the number of commits since the last tag. The Git release tag is human controlled. The patch number is auto-incremented by Git. This is done so for practical reason. That is, the contributors are not burden to update this file manually and are not confront with decision making to decide whether a commit is small or API breaking on each commit.

Perhaps, you have mistaken it with our soversion which is stored in ".soversion" file. The soversion is only used for versioning the shared library. Our soversion is also auto-incremented, however, only when the build system detects there is a change in the API documentation. Again, since this is not controlled by a human for practical reason, the build system always increase the patch number of the soversion (no matter how big or small the API change is) and only bump the minor version when the patch number has reached 255, and so on for the minor number before bumping the major number. See [github.com/urho3d/Urho3D/issues/419](https://github.com/urho3d/Urho3D/issues/419) for more detail.

I hope this answers your query.

-------------------------

