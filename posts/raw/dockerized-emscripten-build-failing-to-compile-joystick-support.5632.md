mizahnyx | 2019-09-28 04:29:31 UTC | #1

First of all, thank you all for the effort put on this wonderful engine.

I just updated both docker images (`docker pull urho3d/dockerized-web`) (`docker pull urho3d/dockerized-native`) and source. Then I tried dockerized native compilation, it went smoothly. Then I tried emscripten dockerized build. Got this error:

    Urho3D/Source/ThirdParty/SDL/src/joystick/emscripten/SDL_sysjoystick.c:193:14: error: implicit declaration of function 'emscripten_sample_gamepad_data' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
    retval = emscripten_sample_gamepad_data();

Any way I can make it build? Also, I never ever have been able to build in the dockerized environment a project (created with rake) outside the main source tree. I tried creating a copy of `dockerized.sh` and adding a mount point for the project directory, no luck.

Thanks in advance!

-------------------------

weitjong | 2019-09-28 06:33:50 UTC | #2

I think I may know why. There is one TODO thing at the back of my mind but I have not got time to do it yet which can explain your web build issue. If you are using the convenient shell script `script/dockerized.sh` then by default it won't use the `:latest` tag of the docker image. Since the script is designed to track the upstream development of Urho3D, it is scripted to use the tag matching the branch/tag you are in. In your case, unless you have specifically requested to use `:latest` tag, the script uses the `:master` tag instead when you are in master branch. However, the `:master` tag in the docker hub has not been updated yet, i.e. it is still behind the `:latest` tag. That's the problem.

I will find time to update the `:master` tag in the docker hub later. For the time being you can explicitly request for `:latest` by using this command.

```
$ DBE_TAG=:latest script/dockerized.sh web
```

Sorry for that. Just remember though that latest does not always mean better or correct.

-------------------------

weitjong | 2019-09-29 14:52:20 UTC | #3

I forgot to answer your other question. The DBE is still new. At the moment it does not provide enough support to let user easily build the downstream project just yet, but it is totally possible. I mean our CI has shown one (quick and dirty) way of doing that and there are other ways too, e.g. building your own custom docker image with your custom Urho3D library already built inside it, or modify the convenient script "dockerized.sh" for your own project to also mount a chosen Urho3D built tree from your host, normally known as URHO3D_HOME, so that it can be referenced inside the container when building your own project.

BTW, I have updated the tags in the "Docker Hub", so the workaround in my earlier post is not needed anymore.


EDIT: In case it is still not obvious to you how the CI does it, I have summarized the nutshell as follows. If you don't have a new downstream project created yet, you can quickly get one via rake scaffolding task.
```
$ rake scaffolding dir=my-downstream-project
```
The new project resides inside the Urho3D project root and this is important for the quick and dirty approach. I come back to that later. Modify the skeleton project to your heart's content and when you are ready to build it, do this below. This uses a feature that all basic docker user should already know.
```
$ script/dockerized.sh web bash
```
and you are now in an interactive shell from inside the container! CD to your downstream project and build it as you would have normally done it.
```
urho3d@fishtank:/path/to/Urho3D/project/root$ cd my-downstream-project
urho3d@fishtank:/path/to/Urho3D/project/root/my-downstream-project$ URHO3D_HOME=$(pwd)/../build/web rake cmake web && rake make web
```
And voila! Exit the shell to go back to the host when you are done. This works because the DBE can see and touch anything inside the Urho3D project root directory and since the downstream project is inside this directory then the DBE can freely perform build operation on it too. As a bonus it also can see the parent directory contains a build tree subdir to be denoted as "URHO3D_HOME". This is why earlier I said it is important to create the new downstream project inside the Urho3D project root if you take this quick and dirty approach. The other approaches I mentioned in my previous post do not have this restriction.

One last thing. If you do using this quick and dirty approach and you don't like to drop into an interactive shell each time you want to build then you are in luck. There is another hidden gem that I believe I haven't told anyone anywhere yet. In the Urho3D project root create a new file ".rake/my-downstream-project.rake". Create the ".rake" subdir if you don't have it yet. And put these lines inside the file.
```
task :build do
  Dir.chdir 'my-downstream-project' do
    system 'URHO3D_HOME=$(pwd)/../build/web/ rake cmake web && rake make web' or abort 'Failed to build'
  end
end
```
Then you can build your downstream project by simply typing this one liner at the Urho3D project root.
```
$ script/dockerized.sh web rake build
```
In the example above I created a new rake task and called it "build". You can substitute that to anything you like.

-------------------------

