ghidra | 2017-01-02 01:00:54 UTC | #1

Im curious what the best structure for storing project files is used by most here. 
Currently I am just making a folder that I can sybmolically link into the scripts folder, that houses my classes. I then back that up to git. But it doesnt include any shader files. Is it clean to make a folder in there to hold shader files, and any texture files I might need?

I'm asking, because I am about to start a simple project with a friend, and we'd like to use git to share files. But simply the files associated with the project. Not all of urho. It seems easy enough to keep that linked to git too and pull when we want to try out new builds etc.

-------------------------

silverkorn | 2017-01-02 01:00:54 UTC | #2

[quote="ghidra"][...] we'd like to use git to share files. But simply the files associated with the project. Not all of urho.[/quote]
For that part, you probably already know but there's [b]submodules[/b] for this purpose and it's better to use on a Windows OS since symlinks are not always available/possible (Windows Vista and above + admin rights (unless you add specific local security policy rights)): [url]http://git-scm.com/book/en/v2/Git-Tools-Submodules[/url].

-------------------------

friesencr | 2017-01-02 01:00:55 UTC | #3

For a quick hack create Empty Data/CoreData folders in your Bin folder then symlink CoreData and Data from your urho source folder into your Extra folder.  Extra scoops up any folders in there and makes them resource paths.

-------------------------

thebluefish | 2017-01-02 01:00:56 UTC | #4

What I do is I have a /Data/ directory in the root of my project that contains CoreData, Data, and GameData (an extra package with all of my new data so that it can be sent from server to client).

Then I have a PackageScript.bat which does the following:

[code]
PackageTool CoreData ./Packages/CoreData.pak -c
PackageTool Data ./Packages/Data.pak -c
PackageTool GameData ./Packages/GameData.pak -c
[/code]

I have a SynchronizeData_Debug.bat which copies all of the packages to my Debug folder:
[code]
set targetfolder="../_bin/Debug/"
set sourcefolder="Packages"

cd /d %targetfolder%
for /F "delims=" %%i in ('dir /b') do (rmdir "%%i" /s/q || del "%%i" /s/q)
cd /d "%~dp0"
xcopy /e /d /c /y %sourcefolder% %targetfolder%
[/code]

Additionally, I build my game as a .DLL library with a custom starting point, GameMain. I have a separate executable that loads this DLL and runs the game ([url=http://discourse.urho3d.io/t/client-server-framework/474/1]You can view my example framework if you want to see how this is done[/url]). I've recently added in functionality for the debug build of this wrapper executable to automatically run the scripts before the game is executed. This ensures that I can work entirely with the /Data/ directory and the game will automatically pull game asset updates as they come in.

-------------------------

