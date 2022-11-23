rku | 2017-01-02 01:11:49 UTC | #1

Hey i wonder.. Would there be any will to migrate from angelscript to c++ for editor? This particular thing especially bugs me. Where Urho3D code is very clearly written and is simply easy to read and improve upon the editor code is exact opposite. It seems like a maze of functions crammed one on top of each other with bulk of manual UI management interwoven to spice it up. Urho's UI is not exactly well suited for complex UIs as needed by editor but you guys seem to have pulled it off. However code is is less than pleasant to work with. UI system shotcomings could be easily hidden away in custom widget classes so they dont mix with other code like it is now. And then it is written in angelscript - a scripting language that takes away our tools we use (IDEs/debuggers/linters/etc) and gives no convenience in exchange. When you have to do typecasting (!!) in a scripting language then something really is amiss..

You probably noticed multiple people started writing their own editors in c++. I know at least two. [url=https://github.com/scorvi/Urho3DIDE]Urho3DIDE[/url] is long-abandoned sadly. There was another one written using ImGui (cant find the link now). And then its me doing same thing all over again. My reason for going that way is lack of easy integration. I want editor that is built into the game. Editor that can manage game scene next to game code operating on that scene. Sure we could plug angelscript editor into our games for this purpose but working with such system i see less than ideal due to reasons mentioned above.

Would it not be better to make editor in c++? Same language as engine is written in, so it seamlessly integrates into the whole package. We could do some careful thinking and allow building editor into the game so it can operate on supplied scene while by default building it as external tool. Something like libEditor and Editor executable. And with some effort code would be as clean as of engine itself lowering bar of entry for contributions in that direction. As funny as it sounds angelscript indeed makes it harder to contribute to or extend editor. The only possibly positive thing current editor has is no need for compiling before it can be run. But in reality i do not think this is really that imporant. Standalone editor is pretty small tool, building it would take negligible amount of time anyway.

So what do you people think? I myself would gladly redirect my efforts to work on official editor instead of private one.

-------------------------

PeaceSells50 | 2017-01-02 01:11:49 UTC | #2

I am currently working on moving Scorvi's work forward. I have got it working in 1.5 and have been slowly moving functionality from the Angelscript editor into c++. It is slow going because I don't have a lot of time. At some point I would like to create a git hub repository for it. I will send a reply post in the not so distant future with the repository.

-------------------------

rku | 2017-01-02 01:11:50 UTC | #3

Im not on the fast pace either. Combined effort however could benefit us all. Cant wait for that repo.

-------------------------

PeaceSells50 | 2017-01-02 01:11:50 UTC | #4

The repository is here: [github.com/PeaceSells50/Urho3D.git](https://github.com/PeaceSells50/Urho3D.git). We should probably decide what we each want to work on so we don't do duplicate work.

-------------------------

PeaceSells50 | 2017-01-02 01:11:50 UTC | #5

I added 3 issues to the GitHub repository. I will work on the Context Menus for the Hierarchy Window. If you want you can take either one of the other 2 issues or add a new issue.

-------------------------

rku | 2017-01-02 01:11:51 UTC | #6

Great. Which branch do we work on? Because i pulled IDE branch and its horribly broken. I have it almost fixed but it occurred to me maybe its wrong branch.

Edit:
I gave code some love and now it is in a bit better shape. Heck it builds on linux! Previous developer was clearly not interested in cross-platform development. While at that i allowed myself to do bulk of other improvements and reorganization so it better fits into Urho3D codebase.

See it here [github.com/r-ku/Urho3D/tree/IDE](https://github.com/r-ku/Urho3D/tree/IDE)

-------------------------

PeaceSells50 | 2017-01-02 01:11:52 UTC | #7

Wow. Awesome work! IDE was the correct branch. It compiled just fine on windows. I did not test Linux. Its cool that we have linux and windows covered by the two of us. Do we just want to work from your branch then?

-------------------------

