practicing01 | 2017-01-02 01:04:01 UTC | #1

Edit: A combination of hd's suggestion in several places + removing/readding the project in eclipse fixed it because eclipse is gimpware.

Hello, I'm trying to include [url=https://github.com/practicing01/Urho3DTemplate/blob/master/MoveTowards.h]this[/url] and eclipse says it can't resolve LogicComponent.  The samples that use it compiled fine, the only thing I've done out of the ordinary is that my project is a rake of urho.  Keep in mind I didn't have problems with this in 1.32.

-------------------------

hdunderscore | 2017-01-02 01:04:01 UTC | #2

You need:
[code]#include <Urho3D/Urho3D.h>[/code]

-------------------------

