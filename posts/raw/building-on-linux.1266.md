ssake | 2017-01-02 01:06:29 UTC | #1

I built urho3d like this

cmake ../Urho3D
make all
sudo make install

Only AngelScript  Box2D  Bullet  kNet  SDL
can be found in /usr/local/include/Urho3D/ThirdParty

Most of the third party libraries are not included, like PugiXml, GLEW and there seems to be many more.

What to do?

-------------------------

Enhex | 2017-01-02 01:06:30 UTC | #2

Have you followed the building instructions? (not a linux user so I don't know if you're missing anything)
[urho3d.github.io/documentation/H ... lding.html](http://urho3d.github.io/documentation/HEAD/_building.html)

-------------------------

weitjong | 2017-01-02 01:06:30 UTC | #3

Welcome to our forum.

It is intentional. We try to hide the headers of third party libraries to Urho3D library users in general. So, what you are observing is the same on all platforms. Only a few headers are exposed due to one of these two reasons:

[ol]
[li] they are included in the headers of Urho3D. So we have to install them to fulfil the dependency. Most exposed headers fall under this category.[/li]
[li] they may be required by Urho3D library users to extend the functionality in their own apps. Headers fall under this category are Lua, nanodbc, and SQLite.[/li][/ol]

-------------------------

