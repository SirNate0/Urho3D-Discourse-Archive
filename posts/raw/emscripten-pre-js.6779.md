Dares | 2021-04-01 17:40:45 UTC | #1

hi,
I am trying to use Urho3D with emscripten.
/home/dares/emsdk/upstream/emscripten/emcmake cmake .
worked without any Problems.
but the next step doesnt work :(
 /home/Dares/emsdk/upstream/emscripten/emmake make
reaches 90% but then comes : 

> em++: error: '--pre-js': file not found: '/src/emrun_prejs.js'
> make[2]: *** [Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/build.make:90: bin/Urho3DPlayer.html] Fehler 1
> make[2]: Verzeichnis „/home/dares/Schreibtisch/UrhoEm/Urho3D“ wird verlassen
> make[1]: *** [CMakeFiles/Makefile2:2419: Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/all] Fehler 2
> make[1]: Verzeichnis „/home/dares/Schreibtisch/UrhoEm/Urho3D“ wird verlassen
> make: *** [Makefile:152: all] Fehler 2
> emmake: error: 'make' failed (2)

what am I doing wrong?

-------------------------

Modanung | 2021-04-01 18:57:11 UTC | #2

Did you try `./script/cmake_emscripten.sh`י`bat`? It will ask you to set the `EMSCRIPTEN_ROOT_PATH` environment variable, if you haven't. On Linux: `export EMSCRIPTEN_ROOT_PATH=~/emsdk/upstream/emscripten` should fix that, in your case. Adding the line to `~/.bashrc` will set it automatically in the future.

-------------------------

Dares | 2021-04-01 18:52:10 UTC | #3

thank you :) 
It Compiles now

-------------------------

