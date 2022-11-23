nmpribeiro | 2019-01-06 10:41:32 UTC | #1

Hi all!
So I have the following error on my emscripten build:
```
[ 90%] Linking CXX executable ../../../bin/Urho3DPlayer.html
INFO:root:Enabling --no-heap-copy because -s ALLOW_MEMORY_GROWTH=1 is being used with file_packager.py (pass --no-heap-copy to suppress this notification)
parseTools.js preprocessor error in undefined:1: "#!/usr/bin/env "!

undefined:106
      throw e;
      ^
Unclear preprocessor command: #!/usr/bin/env 
Traceback (most recent call last):
  File "/opt/emsdk/emscripten/1.38.19/emcc.py", line 3091, in <module>
    sys.exit(run())
  File "/opt/emsdk/emscripten/1.38.19/emcc.py", line 2093, in run
    memfile, optimizer)
  File "/opt/emsdk/emscripten/1.38.19/emcc.py", line 2735, in generate_html
    shell = read_and_preprocess(options.shell_path)
  File "/opt/emsdk/emscripten/1.38.19/tools/shared.py", line 3107, in read_and_preprocess
    run_js(path_from_root('tools/preprocessor.js'), NODE_JS, args, True, stdout=open(stdout, 'w'), cwd=path)
  File "/opt/emsdk/emscripten/1.38.19/tools/shared.py", line 1125, in run_js
    return jsrun.run_js(filename, engine, *args, **kw)
  File "/opt/emsdk/emscripten/1.38.19/tools/jsrun.py", line 149, in run_js
    raise Exception('Expected the command ' + str(command) + ' to finish with return code ' + str(assert_returncode) + ', but it returned with code ' + str(proc.returncode) + ' instead! Output: ' + str(ret)[:error_limit])
Exception: Expected the command ['/opt/emsdk/node/8.9.1_64bit/bin/node', '/opt/emsdk/emscripten/1.38.19/tools/preprocessor.js', '/tmp/emscripten_temp_68ynej/settings.js', 'shell.html'] to finish with return code 0, but it returned with code 1 instead! Output: 
Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/build.make:97: recipe for target 'bin/Urho3DPlayer.html' failed
make[2]: *** [bin/Urho3DPlayer.html] Error 1
CMakeFiles/Makefile2:1421: recipe for target 'Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/all' failed
make[1]: *** [Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/all] Error 2
Makefile:151: recipe for target 'all' failed
make: *** [all] Error 2
```

Ubuntu 18.04
Steps to reproduce:
1. `git clone https://github.com/urho3d/Urho3D.git emscripten_urho3d`
2. `cd emscripten_urho3d/`
3. `./script/cmake_emscripten.sh emscripten_build`
4. `cd emscripten_build`
5. `make`

Does anyone have a clue on how to go about this error? I will try to re-install emscripten emsdk, and check if I can avoid that node installation somehow.

Thanks in advance!

-------------------------

weitjong | 2019-01-07 09:46:40 UTC | #2

You do not need a separate node.js installation, to my understanding the EMSDK already bundles it. The problem with web build is, it depends on Emscripten compiler toolchain which is a moving target by itself. They break our web build from time to time, even on minor version changes. The last version that we have tested working with Urho3D project is 1.38.4 (incoming). I haven't got time to test out the latest version yet, so it could be error-ed out as well (assuming you have not  done anything wrong in its installation).

However, you can try the following two solutions, both use the same Emscripten version 1.38.4 that we have tested to be working for our web build.

1. You can clone the `incoming` branch from https://github.com/urho3d/emscripten-sdk repo and activate it afterward before attempting to use it.
2. Or try to get the Docker-CE installed first then use our newly minted Web DBE (See doc [here](https://urho3d.github.io/documentation/HEAD/_building.html#Dockerized_Build_Environment)) to build the Urho3D project inside a docker container.

Good luck.

-------------------------

nmpribeiro | 2019-01-07 09:47:15 UTC | #3

Hi @weitjong

All working now :slight_smile: thanks for the missing bit of information - I would recommend to specify in the build documentation that the forked github emscripten-sdk repo is version 1.38.4, and this is the tested version with Urho3D.

-------------------------

weitjong | 2019-01-07 10:40:12 UTC | #4

Glad to hear that. Although to put that information in the documentation is a good idea, we don't want to tie our web build to a specific Emscripten version, and also it would actually add extra effort on our side to keep maintaining the info to be up-to-date. Like I said earlier, it is a moving target. We will catch it up sooner or later and the whole thing repeats again.

FWIW, the last tested version number is always available here.
https://github.com/urho3d/emscripten-sdk/tree/sdk-update-trigger

-------------------------

nmpribeiro | 2019-01-07 19:07:58 UTC | #5

You can have a list of tested working versions, or track that github readme (or link it heh). Also, be a tiny little bit more explicit that the emscripten sdk tested version are there on that readme.

If you kindly do that, I will rest my case! :smile:

-------------------------

