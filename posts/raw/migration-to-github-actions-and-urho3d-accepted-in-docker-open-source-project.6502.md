weitjong | 2020-11-04 16:52:27 UTC | #1

We have two announcements to make. First of all is the successful migration from Travis-CI and AppVeyor to GitHub Actions. Although there are still a few teething issues, we are hopeful that they could be ironed out in the next few days. Thanks to GH Actions, the new CI/CD workflow could do more things than otherwise possible in the past. We now have both clang-tidy and clang-format check. We are able to perform Android build without cutting any corners like in the past. We even can do new scaffolding test for Android build now with the improved Gradle build system, done while in the migration process. The overall CI/CD workflow currently has 62 jobs in total, running with 3 types of runners: Linux, MacOS, and Windows. The jobs are massively parallel, so the everything finishes much faster compared to before.

The second thing is about the [Docker Open Source Program](https://www.docker.com/blog/expanded-support-for-open-source-software-projects/). Some of you may have already know that our CI jobs running on Linux host actually rely on Docker technology. Instead of prepping the build environment on each CI run, we actually just download the so-called "Dockerized Build Environment" image and just "run" it. The DBE builds the software for us during its runtime. The DBE image has all the Urho3D prerequisite software component pre-installed. One DBE image per target platform supported by Urho3D. The images are hosted in the docker.io, a public Docker registry provided by Docker Hub. With the acceptance of Urho3D into Docker Open Source Project Program, our DBE images can be pulled without any pull rate restriction.

So, do not hesitate to fork and turn on the CI/CD workflow on your fork.

-------------------------

1vanK | 2020-11-04 23:10:57 UTC | #2

As far as I understood, only 10 jobs are allowed in fork. Or is it possible to customize it?

-------------------------

weitjong | 2020-11-05 04:02:52 UTC | #3

Nothing special on Urho3D repo. We are using GitHub Free account. On paper that should only give us 20 concurrent jobs on Linux/Windows but only 5 on macOS. But in practice I see we get more than that for free. Only the cap limit on macOS is spot on. I am not sure if thing would be different on fork. The document does not state it would be any different. The usage limit really just depends on your own GH account and billing plan. Being open source does have advantage in this case.

-------------------------

johnnycable | 2020-11-05 15:38:38 UTC | #4

Very good job, @weitjong. Thanks!

-------------------------

rku | 2020-11-05 15:43:21 UTC | #5

Hey @weitjong i noticed MinGW and msvc builds do not use caching. In case you are not aware, you may use `ccache` with MinGW (`choco install -y ccache`) and there is a `clcache` project, even though archived, it does work.
```
pip install clcache
"$MSBUILD" "-p:Configuration=Release" "-p:TrackFileAccess=false" "-p:CLToolExe=clcache.exe" "-p:CLToolPath=C:/hostedtoolcache/windows/Python/3.7.9/x64/Scripts/" *.sln
```

New CI setup is awesome. Thank you :)

-------------------------

1vanK | 2020-11-05 15:51:25 UTC | #6

[quote="weitjong, post:3, topic:6502, full:true"]
Nothing special on Urho3D repo. We are using GitHub Free account. On paper that should only give us 20 concurrent jobs on Linux/Windows but only 5 on macOS. But in practice I see we get more than that for free. Only the cap limit on macOS is spot on. I am not sure if thing would be different on fork. The document does not state it would be any different. The usage limit really just depends on your own GH account and billing plan. Being open source does have advantage in this case.
[/quote]

This is pretty weird. Yesterday I had only 10 one-time jobs and my fork was compiling for half a day. But today all ok. I don't know what caused it.

-------------------------

weitjong | 2020-11-08 17:04:56 UTC | #7



-------------------------

