umen | 2017-01-02 00:59:01 UTC | #1

Any plan to automate the  process  of creation of new projects? 
Something like command line utility that will take parameters and will create the directory's structure and basic hello world sources in it , 

Also the cmake argumets parameters , can they be added into the cmake_* script . 
Something like :
cmake_ios.sh --help 
And it will output the [urho3d.github.io/documentation/a00001.html](http://urho3d.github.io/documentation/a00001.html)  Build options table . 

[b]UPDATE :[/b]
also i found that the Urho3DPlayer.exe dosn't have any help switch , and the -s -w arguments are hidden in the running scripts 
so i guess adding some kind of "-help" switch will be helpful also 

The intention of all those actions is to avoid going each time to the help pages and stream line the work process .
Thanks

-------------------------

weitjong | 2017-01-02 00:59:01 UTC | #2

Actually we do have it already, although it is left as an undocumented feature because it does not work yet on Windows platform currently. The feature should work on all Unix-alike platforms: Linux, Mac, and even Raspberry Pi. The prerequisite software is "Rake". Once installed, you can create a new project using the "scaffolding" task. In the command line, go to the Urho3D project root directory where the file called "Rakefile" is located and enter:

rake scaffolding dir=/path/to/your/new-project project=your-project-name target=your-project-name

It will create a new project in the specified directory. The new project copies the source code for building Urho3DPlayer. User is expected to replace the source codes with their own naturally. But as it is, the new project will compile and build. It expects to find Urho3D library (either static or shared) in the Urho3D project root directory. So, you must first build Urho3D library successfully before building the new project. The steps to configure the new project is exactly the same as how Urho3D project is being configured. In fact, the scaffolding task just creates the symbolic links to the cmake_*.sh scripts that you normally use for Urho3D in the new project directory.

Adding CMake script argument to show the build option help page is a good idea. The build option table is actually also available in Readme.txt in plain text. The file is in the same location as those cmake_*.sh scripts. So, I reckon it will be easy to "grep" the section and output it on demand. If somebody want to enhance the scripts, this is the approach I would suggest. Personally I don't see any need though. We have enhanced our CMake build scripts to use CMake cache last year. The build options are cached after the first invocation. Subsequently the same script can be invoked without any options because CMake uses the previously cached build options automatically. Also, I find most of the time running "make" via command line or Alt+F7 in VS or ?+B in Xcode alone is sufficient to detect any source code changes (even in Lua *.pkg file) and the project would build itself incrementally. The only time I need to re-invoke the script again is when there are new source codes being added into the project.

-------------------------

friesencr | 2017-01-02 00:59:01 UTC | #3

For those that do not know.  Rake is make that runs on ruby.  If you have a ruby installation its a matter of installing the gem via rubygems.

The windows option would be to install ruby via the installers.
[rubyinstaller.org/](http://rubyinstaller.org/)

and do a 
`gem install rake`
in the command line

EDIT:
I would like to see some sort of scaffolding option for making a urho3d plugin.  There are lots of event hooks in urho.  Having some conventions on the build level to unify the cool work everyone in the community would be a nice add.

-------------------------

umen | 2017-01-02 00:59:01 UTC | #4

Thanks for your quick replay guys , 
well i hope the complete windows included  "Create project" will be working in the next versions ...  its will be great . 

Question about the CMAKE cache , 
first time i pull the sources and create the vs project via cmake like this :

[code]cmake_vs2012.bat -DURHO3D_SAMPLES=1 -DURHO3D_OPENGL=1[/code]
then 
i do git pull each day , then i delete all *.obj  *.lib *.exe files 
then i do cmake_clean . 
in this point do i need to run cmake_vs2012.bat with my arguments ? or not

-------------------------

weitjong | 2017-01-02 00:59:01 UTC | #5

You don't need to call cmake_clean after git pull. You only call cmake_* script again when you see there are new files being added or old files being deleted or moved to other places.
Or put it another way: after a git pull, just do a normal build. If the build fails, invoke a cmake_* without any arguments first and then build again. If that fails too, only then do a cmake_clean and invoke the cmake_* with the whole shebang. If that fails again, nuke the project root directory and start from scratch.

-------------------------

umen | 2017-01-02 00:59:03 UTC | #6

Thanks for the info

-------------------------

