mizahnyx | 2019-01-28 18:57:44 UTC | #1

Hi all,

First, thanks to all developers for creating such a hidden jewel. To the date Urho3D remains as one of my favorite engines to play around with.

I want to create a project that could be Docker-compiled to at least native (Linux), web, and Android platforms. I was succesful at installing Docker and compiling the engine for those 3 platforms. However, the compilation is dependent on the environments inside the respective Docker images, so to compile a project, I must also do it using those same Dockerized environments.

How do I do that?

Thanks in advance.

-------------------------

weitjong | 2019-01-29 02:24:51 UTC | #2

Have you looked at our Dockerized Build Environment? Our approach externalizes the build options as variables that can be set during DBE runtime (which is the project build time).

-------------------------

