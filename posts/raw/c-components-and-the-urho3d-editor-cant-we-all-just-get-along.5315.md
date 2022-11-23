Leith | 2019-07-20 06:18:22 UTC | #1

I've had an eventful couple of days!

I got the latest version of the Editor working - apparently, the issue was that the resource path I had set contained old editor scripts, which were located and loaded in preference to those in the editor binary path. I'm not certain that's all it was, but that was something I took the time to eliminate, between the editor not working, and suddenly working.

With a working editor, I fairly quickly got my BehaviorTree C++ components working within the editor.
This involved dumping a copy of the relevant code into the Urho3DPlayer project source folder (I really should have used symlinks), editing the Urho3DPlayer.cpp sourcecode to register your components, and then regenerating the Urho build folder (cmake) and recompiling urho (make).
It involved some subtle changes to my component sourcecode, so I really do regret not using symlinks - but I have no experience to tell me that cmake could pick up on them (more on this below)

If you get "undefined symbol" errors, you've missed a step... regenerating the build folder involves scanning the build target folders, including Urho3DPlayer, for any new .cpp files that need compiling - but to my knowledge it does not scan recursively... have to plonk all the files together. Anyway, it causes the CMakeLists.txt file to be regenerated to include your new files, and is the major reason you might see "undefined blah" errors later...

I was pretty chuffed to see my c++ behaviortree code executing in response to a script based caller agent! Basically, script agents call a c++ entrypoint for behaviortree execution, while some behaviortree nodes can call back into script methods. C++ is providing the muscle, while script is providing flexibility and rapid iteration.

After that, I tried to pull in my gamestate manager components... this was a messy affair, I spent the rest of the day hacking a solution whereby I'm able to detect the lack of a state manager at runtime, and late-start that system (it lives in a separate scene to the game scene, and so the editor is unaware it should exist... previously, my Application class took care of that detail upfront...)

Now I've got that working, I've run into yet another resource path issue, probably been six or so today... progress is still progress.

I can now load a game scene in the editor, hit play, and my code will notice there's no game state manager, it will create one, and assign the editor's game scene to the manager's gameplaystate ... this currently results in the editor showing my intro scene, main menu, and so on, as if my c++ application had just started.

-------------------------

Leith | 2019-07-21 06:52:13 UTC | #2

Having dealt with the remaining resource issue, I am now able to overload the scene in the editor (asyncronously) - now when my test scriptagent executes its behaviortree logic, and we reach a nested call from c++ back into script, I slam into a segfault.
[quote]
[Sun Jul 21 15:57:39 2019] WARNING: ScriptService being Initialized
Reached nested script method: Door
./Editor.sh: line 3: 11726 Segmentation fault      (core dumped) $(dirname $0)/Urho3DPlayer Scripts/Editor.as $OPT1 $@
leith@leith-desktop:~/Desktop/NewFolder
[/quote]

This does not happen in my pure c++ application!

Since I had to make changes to the codebase to accomodate the editor, and since I failed to try using symlinks, my next step is to backport the changed files into my c++ project and see if I can reproduce the issue. This will also give me a chance to try replacing the files I dumped into the Player project with symlink files, and see if cmake can follow the links.

-------------------------

