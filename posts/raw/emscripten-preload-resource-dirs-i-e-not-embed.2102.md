godan | 2017-01-02 01:13:05 UTC | #1

Is it possible to be able to swap out the Data/CoreData folders without rebuilding the UrhoPlayer with Emscripten? I was hoping that the EMSCRIPTE_SHARE_DATA option was related to this, and it does go part way (i.e. it creates the .js file and .data files that are referenced in the emscripten docs here: [kripken.github.io/emscripten-si ... files.html](https://kripken.github.io/emscripten-site/docs/porting/files/packaging_files.html)). However, after building with this option, it still looks like the Data/Core Data pak files are embedded in the UrhoPlayer.js file.

Is there anyway to access the --preload compiler flag?

More generally, I find it very hard to figure out what is happening in the Emscripten toolchain. Is it possible to write a few words about the general flow?

-------------------------

godan | 2017-01-02 01:13:05 UTC | #2

Some specific questions:
- at some point, the Package Tool is called (i.e to create the .pak files). Where does this happen? I can't find anything in the CMake folder.
- where are the compile flags passed to emcc?

-------------------------

godan | 2017-01-02 01:13:05 UTC | #3

Ok, I know a bit more now. I've been finding it quite difficult to understand the Emscripten build process, so in case it helps anyone else, I thought I'd write out my process and thoughts so far. It might all be wrong :slight_smile:, but even that might be useful.

Just to be clear, my goal is to build a Player.js file with the Emscripten toolchain, and be able to swap out different Data/CoreData folders WITHOUT rebuilding the Player.

K, so my little test project folder set up looks like this:

[code]ScratchPad/
        bin/
               CoreData/
               Data/
        CMake/
        SourceFile.h
        SourceFile.cpp
        CMakeLists.txt[/code]

My CMakeLists.txt file is taken more or less directly from the Documentation, and looks like this:

[code]
# Set project name
project (ScratchPad)
# Set minimum version
cmake_minimum_required (VERSION 2.8.6)
if (COMMAND cmake_policy)
    cmake_policy (SET CMP0003 NEW)
    if (CMAKE_VERSION VERSION_GREATER 2.8.12 OR CMAKE_VERSION VERSION_EQUAL 2.8.12)
        # INTERFACE_LINK_LIBRARIES defines the link interface
        cmake_policy (SET CMP0022 NEW)
    endif ()
    if (CMAKE_VERSION VERSION_GREATER 3.0.0 OR CMAKE_VERSION VERSION_EQUAL 3.0.0)
        # Disallow use of the LOCATION target property - therefore we set to OLD as we still need it
        cmake_policy (SET CMP0026 OLD)
        # MACOSX_RPATH is enabled by default
        cmake_policy (SET CMP0042 NEW)
    endif ()
endif ()
# Set CMake modules search path
set (CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/CMake/Modules)
# Include Urho3D Cmake common module
include (Urho3D-CMake-common)
# Find Urho3D library
find_package (Urho3D REQUIRED)
include_directories (${URHO3D_INCLUDE_DIRS})

# Define target name
set (TARGET_NAME ScratchPad)
# Define source files
define_source_files ()

#c11
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

#pass console arg
SET(URHO3D_WIN32_CONSOLE 1)
# Setup target with resource copying
setup_main_executable ()
[/code]

As a sanity check, I compile this with VS and all is well. So, now I configure the project to be built with emscripten. To do this, I wrote a .bat file that looks like this:
[code]
cmake -Bbuild_player_em -H. -DURHO3D_HOME="C:/Dev/Urho3D/Build/emscripten" -DEMSCRIPTEN=1 -DEMSCRIPTEN_ALLOW_MEMORY_GROWTH=1 -DEMSCRIPTEN_SHARE_DATA=1 -G "MinGW Makefiles" -DPLAYER_ONLY=1 -DCMAKE_TOOLCHAIN_FILE="CMake/Toolchains/emscripten.toolchain.cmake"
[/code]

To answer my question in the previous post, the interaction between the various Emscripten options and the project compilation process seems to be mainly in the "setup_main_executable" macro in "Urho3D_cmake_common". That's where the PackageTool gets invoked, and where the SHARE_DATA option gets handled. Onwards!

So, running that bat file, and then cd-ing in to the build folder and running "make", successfully compiles the project. Ok, so here is where I start to get confused. The bin folder now looks like this:

[code]
CoreData.pak
Data.pak
ScratchPad.html
ScratchPad.html.mem
ScratchPad.js
ScratchPad.js.data
[/code]

As I said, this will run in the browser. So, my first (naive) instinct was to simple replace the .pak files with new ones. This does nothing. And the reason is that emscripten compiler takes the .pak files and runs its own packaging tool, which creates the .data file and some javascript code to make it work. That means that web app is not actually referencing the .pak files, rather it is referencing .data file.

Or so I thought. The next thing I did was actually to delete all the pak files, AND the .data file, just to see if it is actually true that all the assets live in the data file. My bin folder now looks like this:
[code]
ScratchPad.html
ScratchPad.html.mem
ScratchPad.js
[/code]

And this runs fine - it seems to not care at all about the .pak OR the .data file. I guess this my main stumbling block right now - why is this? Where do the assets live if not in the data file or the pak files? In this project, the ScratchPad.js file is around 6MB, which suggests that the .pak files have been embedded in to this file (hence the title of the post). However, in "setup_main_executable", it definitely looks like the --preload option is being used:

[code]
            if (EMSCRIPTEN AND NOT EMSCRIPTEN_SHARE_DATA)
                # Set the custom EMCC_OPTION property to preload the *.pak individually
                set_source_files_properties (${RESOURCE_${DIR}_PATHNAME} PROPERTIES EMCC_OPTION preload-file EMCC_FILE_ALIAS "@/${NAME}.pak --use-preload-cache")
            endif ()
[/code]

Ok, so at this point it looks like there are a couple options:

- I'm not setting an option correctly, or I'm missing some flag, or something. Basically, I'm not using the build system correctly.
- I AM using the build system correctly, but there is a bug.
- Both my cmake usage AND the build system are fine, and "preload" and "embed" do not mean what I think they mean.

Sorry for the long post - just really close to a project milestone and this is one of the last items. All help welcome!

-------------------------

weitjong | 2017-01-02 01:13:06 UTC | #4

[quote="godan"]Is it possible to be able to swap out the Data/CoreData folders without rebuilding the UrhoPlayer with Emscripten?[/quote]

I think it is possible, but you need to get your hand dirty. Do not expect the build system to work out all the use cases for you. As it is, our build system is able to embed or preload any input files, however, I believe in this case you actually don't want to do that. Either embedding or preloading will make the input file in question becomes a dependency to the build, i.e. when it changes its timestamp then make will dutifully trigger a rule for relinking and unfortunately for Emscripten, linking phase is its slowest phase. And that's exactly what you don't want.

I think what you need is a custom shell.html and javascript function to swap in/out the assets in preRun module.

-------------------------

godan | 2017-01-02 01:13:07 UTC | #5

After staring at auto generated js code for a while  :open_mouth: , I made some progress.

To answer a previous question: there is caching system built in to emscripten. I'm still not entirely sure how it works, but once you load your resources once, the default behaviour is to cache them (in Chrome temp folder?? On local machine??). So that means, if you delete the ".data" file, the app will still work as long as cache has not been cleared. So, step 1 of having new resources be loaded is to skip this caching part.

The second step is to separate the resource loading js code and the player js code (as weitjong suggests). Now, the resource loading code is actually autogenerated and on the first line of the of Player.js file (i.e. the compiled app js code). I isolated this code and deleted it from the Player.js file. To do this, you find all the code that comes after (and includes) the first "var Module;" block. That is, there is a bunch of code on the first line: "[color=#FF8040]var Module; ......lots....of.....code......;[/color] var Module ..... remove the orange bits. Btw, a good reference is the Atomic Engine Web Build code. After reading through that (and the Deployment assets) I was able to understand the flow of a emscripten web app a bit better.

Then, I copied that auto generated code in to a new file, called "ScratchPadResources.js". I removed all the caching related code and what is left seems to be the resource loading mechanism:

[code]
var Module;
if (typeof Module === "undefined") Module = {};
if (!Module.expectedDataFileDownloads) {
    Module.expectedDataFileDownloads = 0;
    Module.finishedDataFileDownloads = 0
}
Module.expectedDataFileDownloads++;
((function() {
    var loadPackage = (function(metadata) {
        var PACKAGE_PATH;
        if (typeof window === "object") { PACKAGE_PATH = window["encodeURIComponent"](window.location.pathname.toString().substring(0, window.location.pathname.toString().lastIndexOf("/")) + "/") } else if (typeof location !== "undefined") { PACKAGE_PATH = encodeURIComponent(location.pathname.toString().substring(0, location.pathname.toString().lastIndexOf("/")) + "/") } else {
            throw "using preloaded data can only be done on a web page or in a web worker"
        }
        var PACKAGE_NAME = "binScratchPad.data";
        var REMOTE_PACKAGE_BASE = "ScratchPad.data";
        if (typeof Module["locateFilePackage"] === "function" && !Module["locateFile"]) {
            Module["locateFile"] = Module["locateFilePackage"];
            Module.printErr("warning: you defined Module.locateFilePackage, that has been renamed to Module.locateFile (using your locateFilePackage for now)")
        }
        var REMOTE_PACKAGE_NAME = typeof Module["locateFile"] === "function" ? Module["locateFile"](REMOTE_PACKAGE_BASE) : (Module["filePackagePrefixURL"] || "") + REMOTE_PACKAGE_BASE;
        var REMOTE_PACKAGE_SIZE = metadata.remote_package_size;
        var PACKAGE_UUID = metadata.package_uuid;

        function fetchRemotePackage(packageName, packageSize, callback, errback) {
            var xhr = new XMLHttpRequest;
            xhr.open("GET", packageName, true);
            xhr.responseType = "arraybuffer";
            xhr.onprogress = (function(event) {
                var url = packageName;
                var size = packageSize;
                if (event.total) size = event.total;
                if (event.loaded) {
                    if (!xhr.addedTotal) {
                        xhr.addedTotal = true;
                        if (!Module.dataFileDownloads) Module.dataFileDownloads = {};
                        Module.dataFileDownloads[url] = { loaded: event.loaded, total: size }
                    } else { Module.dataFileDownloads[url].loaded = event.loaded }
                    var total = 0;
                    var loaded = 0;
                    var num = 0;
                    for (var download in Module.dataFileDownloads) {
                        var data = Module.dataFileDownloads[download];
                        total += data.total;
                        loaded += data.loaded;
                        num++
                    }
                    total = Math.ceil(total * Module.expectedDataFileDownloads / num);
                    if (Module["setStatus"]) Module["setStatus"]("Downloading data... (" + loaded + "/" + total + ")")
                } else if (!Module.dataFileDownloads) {
                    if (Module["setStatus"]) Module["setStatus"]("Downloading data...")
                }
            });
            xhr.onload = (function(event) {
                var packageData = xhr.response;
                callback(packageData)
            });
            xhr.send(null)
        }

        function handleError(error) { console.error("package error:", error) }

        var fetched = null,
            fetchedCallback = null;
        fetchRemotePackage(REMOTE_PACKAGE_NAME, REMOTE_PACKAGE_SIZE, function(data) {
            if (fetchedCallback) {
                fetchedCallback(data);
                fetchedCallback = null;
            } else {
                fetched = data;
            }
        }, handleError);

        function runWithFS() {
            function assert(check, msg) {
                if (!check) throw msg + (new Error).stack
            }

            function DataRequest(start, end, crunched, audio) {
                this.start = start;
                this.end = end;
                this.crunched = crunched;
                this.audio = audio
            }
            DataRequest.prototype = {
                requests: {},
                open: (function(mode, name) {
                    this.name = name;
                    this.requests[name] = this;
                    Module["addRunDependency"]("fp " + this.name)
                }),
                send: (function() {}),
                onload: (function() {
                    var byteArray = this.byteArray.subarray(this.start, this.end);
                    this.finish(byteArray)
                }),
                finish: (function(byteArray) {
                    var that = this;
                    Module["FS_createDataFile"](this.name, null, byteArray, true, true, true);
                    Module["removeRunDependency"]("fp " + that.name);
                    this.requests[this.name] = null
                })
            };
            var files = metadata.files;
            for (i = 0; i < files.length; ++i) {
                (new DataRequest(files[i].start, files[i].end, files[i].crunched, files[i].audio)).open("GET", files[i].filename)
            }

            function processPackageData(arrayBuffer) {
                Module.finishedDataFileDownloads++;
                assert(arrayBuffer, "Loading data file failed.");
                assert(arrayBuffer instanceof ArrayBuffer, "bad input to processPackageData");
                var byteArray = new Uint8Array(arrayBuffer);
                var curr;
                if (Module["SPLIT_MEMORY"]) Module.printErr("warning: you should run the file packager with --no-heap-copy when SPLIT_MEMORY is used, otherwise copying into the heap may fail due to the splitting");
                var ptr = Module["getMemory"](byteArray.length);
                Module["HEAPU8"].set(byteArray, ptr);
                DataRequest.prototype.byteArray = Module["HEAPU8"].subarray(ptr, ptr + byteArray.length);
                var files = metadata.files;
                for (i = 0; i < files.length; ++i) { DataRequest.prototype.requests[files[i].filename].onload() }
                Module["removeRunDependency"]("datafile_binScratchPad.data")
            }

            Module["addRunDependency"]("datafile_binScratchPad.data");
            if (!Module.preloadResults) Module.preloadResults = {};

            Module.preloadResults[PACKAGE_NAME] = { fromCache: false };
            if (fetched) {
                processPackageData(fetched);
                fetched = null;
            } else {
                fetchedCallback = processPackageData;
            }
        }
        if (Module["calledRun"]) { runWithFS() } else {
            if (!Module["preRun"]) Module["preRun"] = [];
            Module["preRun"].push(runWithFS)
        }
    });

    loadPackage({ "files": [{ "audio": 0, "start": 0, "crunched": 0, "end": 157508, "filename": "/CoreData.pak" }, { "audio": 0, "start": 157508, "crunched": 0, "end": 11440897, "filename": "/Data.pak" }], "remote_package_size": 11440897, "package_uuid": "7fd80462-f151-458c-8e32-73ec819b2b73" })
}))();

[/code]

Ok, so I now have a "ScratchPadResources.js" file and a "ScratchPad.js" player file. Then, you simply adjust the shell (i.e. the webpage that loads the js code) to first run the Resources script, and then the Player script. Here is the relevant lines way at the bottom of the autogenerated webpage:

[code]
    <script async type="text/javascript" src="ScratchPadResource.js"></script>
    <script async type="text/javascript" src="ScratchPad.js"></script>

  </body>
</html>
[/code]

And that's it! Start up a webserver, and I can now swap out the .data file with a new one, reload the page, and the new resources are used. So that's good. What remains is to somehow call the emscripten packaging tool on the .pak files to create that new .data file.....

-------------------------

weitjong | 2017-01-02 01:13:07 UTC | #6

Glad you made some progress there. Just want to point out that there is no need for step 1 to skip the caching part. The Emscripten caching logic is actually quite good last time I checked it. Unless your *.data files are identical, they should have different UUID assigned. The caching logic uses UUID to decide whether a local cache copy is still "fresh" or not. Just my two cents.

-------------------------

godan | 2017-01-02 01:13:09 UTC | #7

Success! It's a bit of a hack, but it works. Here's what you need to do:

GOAL: To build a player (like the UrhoPlayer) once, and then be able to update the resources packages.

STEPS:

- Build the Player with Empscripten with the following options: -DURHO3D_PACKAGING=1 -DEMSCRIPTEN=1 -DWEB=1 -DEMSCRIPTEN_ALLOW_MEMORY_GROWTH=1
- Delete from your Player.js file the first Module definition:  "[color=#FF0000]var Module; ......lots....of.....code......;[/color] var Module....
- Open up a console and navigate to your resource directories.
- Run the Urho packaging tool on both resource dirs. You should now have two .pak files
- run the Emscripten packaging tool manually: python file_packager.py AppAssets.data --preload Data.pak --preload CoreData.pak --js-output="AppResources.js"
- Add this to the .html file line:

[code]
    <script async type="text/javascript" src="AppResources.js"></script>
    <script async type="text/javascript" src="Player.js"></script>
  </body>
</html>
[/code]

And that's it. All the various files should be in one directory, and then you can start a local server and test it out.

NOTE: It's a real pain manually editing the Player.js file. Does that asset loading text get created because of URHO3D_PACKING=1? When I turn it off, Emscripten complains that ALLOW_MEMORY_GROWTH has not been set. Is that a bug?

-------------------------

weitjong | 2017-01-02 01:13:09 UTC | #8

[quote="godan"]When I turn it off, Emscripten complains that ALLOW_MEMORY_GROWTH has not been set. Is that a bug?[/quote]
Yes, it sounds like it.

-------------------------

weitjong | 2017-01-02 01:13:09 UTC | #9

A quick fix for this bug in question has been pushed to master branch just now.

-------------------------

