Azaratur | 2019-04-05 18:41:45 UTC | #1

Hi, i am very new on Urho3d, i work for a company and i have to find and evaluate some 3d engine with a good support for mobile and html5 (trough emscripten).
We will have to create a title and possibly use it for our next future games. We already developed 12 games with cocos2dx and unity, but unfortunately this engine does not have a very good support on html5.

I am trying to compile but i am not sure i did everythings correctly.. 

First of all i build the engine with codeblocks and everythings seems went fine.
So from here i was a little lost.. I will explain what i did:
My root is this
d:\Urho3d
d:\Urho3d\Build (compiled engine)
d:\Test (Hello word copied from d:\Urho3d\Build\Source\Sample\01_HelloWorld)

So i enter in d:\Urho3d and launched:
cmake_emscripten.bat d:\Test3 -DURHO3D_SAMPLES=0

And it does create the base project for emscripten there.
So i enter in d:\Test and launch:
emake make

What i got are:
CoreData.pak
Data.pak
Urho3DPlayer.data
Urho3DPlayer.js
Urho3DPlayer.wasm

Where is my error? Can someone help me?

-------------------------

weitjong | 2019-04-03 10:11:12 UTC | #2

In short, nothing. If you are able to get this far then all is good. Double confirm by listing to see you got the libUrho3D.a (.bc) in the lib folder under build tree. The make command will also return 0 as exit code when it builds cleanly.

-------------------------

Azaratur | 2019-04-03 10:11:53 UTC | #3

Yeah the file is there..
So what's next?
I checked your web sample and those are a lot different from mine.

I also try to load this Urho3DPlayer.js on html but i got some javascript exception

-------------------------

Azaratur | 2019-04-03 10:24:46 UTC | #4

The sample you have on you server seems to search for Urho3d.js (which i don't have) also they look for 2 files in Urho3D Sample_files (which i created in one of my tests, but not in the one i wrote here).

I don't get how complete the task and test it on crhome.
As i told you i try to use Urho3dPlayer.js but i got this error:
Uncaught TypeError: Cannot read property 'length' of undefined
    at _emscripten_get_num_gamepads (Urho3DPlayer.js:1)
    at wasm-function[28379]:48
    at wasm-function[5579]:266
    at wasm-function[6941]:135
    at wasm-function[17019]:304
    at wasm-function[17955]:323
    at wasm-function[17965]:105
    at wasm-function[16623]:5
    at wasm-function[17365]:68
    at wasm-function[16970]:9

-------------------------

weitjong | 2019-04-03 10:29:12 UTC | #5

There is no canonical way to build Urho3D library (and its samples). Read the online doc for the available build options or check the CI build script to see what build options that it uses (if you want to get started with the same option).

-------------------------

Azaratur | 2019-04-03 10:35:48 UTC | #6

Can you just say me which files i should get on the end?
I read the online docs and but still i don't understand if i am in right direction or if i miss/mess something.

What are the .download files i got in some test?

-------------------------

weitjong | 2019-04-03 10:45:09 UTC | #7

The web samples that we generated during our CI build is using the "URHO3D_TESTING=1" build option. This option will provide a basic "html shell". It is also using "EMSCRIPTEN_SHARE_DATA=1". This gives the output as you have just observed.

-------------------------

Azaratur | 2019-04-03 10:48:57 UTC | #8

Ok thank you so much.
Will try to figure it out.

I saw 3 other engines and if i let this work i will probably choose this one.
We have to create a new serie of games and (most probably) port some of our Cartoon Network title on this engine.

Thank you for your help, will let you know if i get it work.

-------------------------

johnnycable | 2019-04-03 15:36:03 UTC | #9

Just tried and it works. I'm on 1.7+. My tree:

> ├── CoreData.pak
> 
> ├── Data.pak
> 
> ├── GameData.pak
> 
> ├── myApp.data
> 
> ├── myApp.html
> 
> ├── myApp.html.map
> 
> └── myApp.js 


run command:


emrun --browser chrome myApp.html

-------------------------

Azaratur | 2019-04-03 15:48:46 UTC | #10

I don't have any idea how you get that html out..
I did what weitjong said and it created those files:

CoreData.pak
Data.pak
Urho3D.js
Urho3D.js.data
Urho3DPlayer.html
Urho3DPlayer.js
Urho3DPlayer.wasm

As i said i was trying to compile HelloWorld Sample.

I try to launch Urho3DPlayer.html and i got:
Urho3D.js:100 Uncaught (in promise) TypeError: Module.addRunDependency is not a function

-------------------------

Azaratur | 2019-04-03 15:49:22 UTC | #11

Will study a little bit on it, most probably i am doing something wrong but i don't understand what and where.

-------------------------

weitjong | 2019-04-03 17:10:20 UTC | #12

If you use "URHO3D_SAMPLES=0" then all the Urho3D provided samples are not included in the build tree. If you want HelloWorld sample then reenable this build option. Also, you can also tell `make` command to just to build a single sample target rather than all of them, which for Emscripten/Web build will take a lot of time. For example `make 01_HelloWorld`. This will also build all the deps required by the 01_HelloWorld target but perhaps you already know that. BTW, the "EMSCRIPTEN_SHARE_DATA=1" build option only makes sense when you eventually build all the sample targets and don't want each of the sample target has its own set of resource paks (got individual file but otherwise contains identical data).

We have changed the Web build system from 1.6 to 1.7 and from 1.7 to current master. You may want to read the porting notes in this page: https://urho3d.github.io/documentation/HEAD/_porting_notes.html

What I told you earlier assume you are using 1.7. I know the documentation is quite sparse, but I hope you get it working. BTW, personally I believe the build system in the master branch is better.

-------------------------

Azaratur | 2019-04-03 17:53:43 UTC | #13

Thank you for your support and sorry if i get a little lost..
Yes i am using the newer version.

What i don't understand now is how use the cmake_emscripten command.. I'll try to explain as better as i can.
I start from beginning so after dl the engine i did make a version for vs2015 by make command to a subdir of Urho unzipped folder.
I compiled all with vs2015 and set the Urho home.

Now as far as i understood i should use cmake_emscripten from the unzipped folder and target the project i would like to build, so i targetted the compiled hello world Urho3d\BUILD\source\etc..
After that i did emmake make but as far as i see i don't have a Helloworld.js but instead a Urho3DPlayer.js so i am a little confused in how it should work.

-------------------------

Azaratur | 2019-04-04 08:13:07 UTC | #14

Today i'll retry from the beginning, but i still get this error on my Urho3DPlayer

Urho3DPlayer.js:1 Uncaught TypeError: Module.removeRunDependency is not a function
    at HTMLScriptElement.s.onload (Urho3DPlayer.js:1)

-------------------------

Azaratur | 2019-04-04 09:04:09 UTC | #15

I finnaly find the way to create hellowrold.js.. But i still got the same bug :frowning:

And when it create the html i got another issue:  
> parseTools.js preprocessor error in shell.html:1: "#!/usr/bin/env firefox"!
> 
> undefined:81
>       throw e;
>       ^
> Unclear preprocessor command on line 0: #!/usr/bin/env firefox
> Traceback (most recent call last):
>   File "C:\HTML5Games\tools\emsdk\emscripten\1.38.30\emcc.py", line 3276, in <module>
>     sys.exit(run(sys.argv))
>   File "C:\HTML5Games\tools\emsdk\emscripten\1.38.30\emcc.py", line 2228, in run
>     memfile, optimizer)
>   File "C:\HTML5Games\tools\emsdk\emscripten\1.38.30\emcc.py", line 3091, in generate_html
>     wasm_binary_target, memfile, optimizer)
>   File "C:\HTML5Games\tools\emsdk\emscripten\1.38.30\emcc.py", line 2864, in generate_traditional_runtime_html
>     shell = read_and_preprocess(options.shell_path)
>   File "C:\HTML5Games\tools\emsdk\emscripten\1.38.30\tools\shared.py", line 3250, in read_and_preprocess
>     run_js(path_from_root('tools/preprocessor.js'), NODE_JS, args, True, stdout=open(stdout, 'w'), cwd=path)
>   File "C:\HTML5Games\tools\emsdk\emscripten\1.38.30\tools\shared.py", line 1091, in run_js
>     return jsrun.run_js(filename, engine, *args, **kw)
>   File "C:\HTML5Games\tools\emsdk\emscripten\1.38.30\tools\jsrun.py", line 155, in run_js
>     raise Exception('Expected the command ' + str(command) + ' to finish with return code ' + str(assert_returncode) + ', but it returned with code ' + str(proc.returncode) + ' instead! Output: ' + str(ret)[:error_limit])
> Exception: Expected the command ['C:/HTML5Games/tools/emsdk/node/8.9.1_64bit/bin/node.exe', 'C:\\HTML5Games\\tools\\emsdk\\emscripten\\1.38.30\\tools/preprocessor.js', 'C:\\Users\\Johnny\\AppData\\Local\\Temp\\emscripten_temp_qssv0c\\settings.js', 'shell.html'] to finish with return code 0, but it returned with code 1 instead! Output:
> Source\Samples\01_HelloWorld\CMakeFiles\01_HelloWorld.dir\build.make:94: recipe for target 'bin/01_HelloWorld.html' failed
> mingw32-make[3]: *** [bin/01_HelloWorld.html] Error 1
> CMakeFiles\Makefile2:1696: recipe for target 'Source/Samples/01_HelloWorld/CMakeFiles/01_HelloWorld.dir/all' failed
> mingw32-make[2]: *** [Source/Samples/01_HelloWorld/CMakeFiles/01_HelloWorld.dir/all] Error 2
> CMakeFiles\Makefile2:1708: recipe for target 'Source/Samples/01_HelloWorld/CMakeFiles/01_HelloWorld.dir/rule' failed
> mingw32-make[1]: *** [Source/Samples/01_HelloWorld/CMakeFiles/01_HelloWorld.dir/rule] Error 2
> Makefile:521: recipe for target '01_HelloWorld' failed
> mingw32-make: *** [01_HelloWorld] Error 2

I am using latest emscripten should i use this one?
https://github.com/urho3d/emscripten-sdk

-------------------------

Azaratur | 2019-04-04 10:36:24 UTC | #16

No way.. Same issue again even using the emscripten sdk in urho3d git.

Cannot create the html file (se above) and if i create a simple hmtl file and load it i get:
Uncaught TypeError: Module.removeRunDependency is not a function
    at HTMLScriptElement.s.onload (02_HelloGUI.js:1)

Uncaught (in promise) TypeError: Module.addRunDependency is not a function
    at DataRequest.open (Urho3D.js:100)
    at runWithFS (Urho3D.js:119)
    at callRuntimeCallbacks (02_HelloGUI.js:1)
    at preRun (02_HelloGUI.js:1)
    at run (02_HelloGUI.js:1)
    at runCaller (02_HelloGUI.js:1)
    at removeRunDependency (02_HelloGUI.js:1)
    at receiveInstance (02_HelloGUI.js:1)
    at receiveInstantiatedSource (02_HelloGUI.js:1)

I don't know what else try, i did every kind of attempt even the silly one.
We managed to port few java games on emscripten but i don't find a way to build the sample of Urho, i am losing hope.


Strangely searching for that error i found it in another engine :slight_smile:
https://github.com/godotengine/godot/issues/17538

-------------------------

Azaratur | 2019-04-05 18:41:09 UTC | #17

OHHHH YESSSS..
I did it..
Strangely enought i had to use an old emscripten to let it work.

-------------------------

weitjong | 2019-04-04 15:55:30 UTC | #18

Congrats! About the EMSDK version, you are right, and that has been discussed before here in the forum a few months ago. For the best result you may want to use the same exact version that our web CI build job uses.

-------------------------

Azaratur | 2019-04-04 16:09:09 UTC | #19

I try to dl this one:
https://github.com/urho3d/emscripten-sdk

But i had issue even with that.

-------------------------

weitjong | 2019-04-04 16:50:26 UTC | #20

I meant to use the same version number as the CI. The repo that you link is not necessarily compatible with your system because you are not using Linux.

-------------------------

johnnycable | 2019-04-05 15:08:14 UTC | #21

mine is: /usr/local/emsdk_portable/emscripten/1.35.0

-------------------------

