SteveU3D | 2017-03-18 02:08:54 UTC | #1

Hi,
To use Urho3D, one must put the folders Data and CoreData in the exe folder. I would like to change that and put Data and CoreData in bin/Urho3DResoureces for example, the exe stays in bin. How to do that?

Thanks

-------------------------

SteveU3D | 2017-02-03 14:40:33 UTC | #2

Sorry, I found the answer.
Just use engineParameters_["ResourcePaths"]="yourFolder/Data;yourFolder/CoreData";

-------------------------

