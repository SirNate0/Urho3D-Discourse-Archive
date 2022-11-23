weitjong | 2017-01-02 01:12:02 UTC | #1

The SF.net virus scanner has wrongly flagged up 4 of our build artifacts from the last CI packaging build (snapshot 1.5-712) as containing potentially malicious or unwanted software. At the moment the summary is only viewable by admins of the project. The "Malware warning" will be associated with our project download page when we do nothing. The suspicious files are:

[ul][li]Urho3D/Snapshots/Urho3D-1.5.712-Linux-64bit-STATIC-snapshot.rpm[/li]
[li]Urho3D/Snapshots/Urho3D-1.5.712-Linux-STATIC-snapshot.rpm[/li]
[li]Urho3D/Snapshots/Urho3D-1.5.712-Raspberry-Pi-STATIC-snapshot.rpm[/li]
[li]Urho3D/Snapshots/Urho3D-1.5.712-Raspberry-Pi-STATIC-v7a-snapshot.rpm[/li][/ul]
However, I have no reason to believe those files are being compromised. All our build artifacts are built by Travis CI using the same source code in the GitHub without human intervention. I have requested SF.net to whitelist those files just now. Let see how it goes.

-------------------------

rasteron | 2017-01-02 01:12:03 UTC | #2

I still can't get over the fact that you still host those files on SF. SF was really good and somewhat a pioneer back in the day, but now is a breeding ground of malware afaik. This is kinda old news but here are some links:

[information-age.com/industry ... s-software](http://www.information-age.com/industry/software/123459675/hotbed-malware-another-blow-sourceforge-google-discovers-588-pages-malicious-software)
[infoworld.com/article/292973 ... icide.html](http://www.infoworld.com/article/2929732/open-source-software/sourceforge-commits-reputational-suicide.html)
[en.wikipedia.org/wiki/SourceFor ... ed_malware](https://en.wikipedia.org/wiki/SourceForge#Project_hijackings_and_bundled_malware)

I would not be surprised if this is related so why not just host it all on GitHub ..or somewhere else?

-------------------------

weitjong | 2017-01-02 01:12:03 UTC | #3

Well, your links are actually dated. SF.net was good like you said and became (note the past tense) bad, and now already turned a new leaf. I am willing to give it a second chance. The malware alert came from SF.net itself.  I suppose that is one of things it does to show they have changed, but in this case it has backfired on us.

-------------------------

rasteron | 2017-01-02 01:12:03 UTC | #4

[quote] and now already turned a new leaf.[/quote] 

That's really tough to say at the moment. As I've said, a lot of options out there why still SF? Is this a nostalgia thing? :wink:

[quote]The malware alert came from SF.net itself. I suppose that is one of things it does to show they have changed, but in this case it has backfired on us.[/quote]

malware rep SF.net doing a false positive on trusted Urho3D? ..hey it's an oxymoron! :slight_smile:

-------------------------

weitjong | 2017-01-02 01:12:03 UTC | #5

Just to make sure we are on the same page. [sourceforge.net/blog/sourceforg ... ure-plans/](https://sourceforge.net/blog/sourceforge-acquisition-and-future-plans/). Of course, it is still early to say whether the new owner of SF.net could turn the tide or not. But one thing for sure the "adware" DevShare program is over.

As for why we haven't moved:

[ul][li]Previously there was worry that we could not really remove our project from SF.net, i.e. worry of being hijack. Ironically, now the risk is lower or eliminiated, it may actually speed up devs abandoning SF.net.[/li]
[li]We use SF.net as "file release system" because it has download mirror sites all over the world. I am not aware of other free services that provide the same capability.[/li]
[li]We have spent a significant amount of time to fully automate the file upload with digital keys setup from Travis-CI and AppVeyor VMs to SF.net. Although we are not being locked in but any migration will need to asses this. Personally I will not probably spend time on this work again unless it is broken, which is not the case at the moment.[/li][/ul]
Also remember that our project remains being maintained by volunteers on their free time. We do not have any sponsors to date, so we rely heavily on the free services out there which may impose some  "acceptable" restrictions on us or come with some strings attached.

As for why we don't use GitHub for this purpose. It is because we only use GitHub as "source code repository". With a few exceptions like ccache's cache objects or pre-installed SDK, there are no binaries in our GitHub repositories and we intend to keep it that way. Besides, we don't want to put all our eggs in one basket.

-------------------------

weitjong | 2017-01-02 01:12:04 UTC | #6

Update: those snapshot build artifacts have been whitelisted as per requested. However, I am not sure yet at this moment how this whitelisting works. Hopefully it is just a one off incident.

-------------------------

GSpub64 | 2017-01-02 01:12:04 UTC | #7

....In case this helps....

I used GCC/G++ 4.9.3 to compile Urho3D on my linux system...

I've had a look at my install log that I copied form terminal during the make process on my linux pc here: ( i've also attached the log with my username snip'd )... I found several things that might cause the black list in some virus scanners: the most notable of which seems to be with a function that can pause a user's computer during use and another function was recommended to replace it.

If you open the log file i've attached in gedit or another text editor/viewer with line numbers turned on and no text wrapping then i can refer to the line numbers for quick reference:

.......hmm I don't see a button for uploading attachments, probably because this is my 2nd post ever here.......

[code]168: Scanning dependencies of target StanHull
169: [ 16%] Building CXX object Source/ThirdParty/StanHull/CMakeFiles/StanHull.dir/hull.cpp.o
170: ((SNIP))/Urho3D-1.5/Source/ThirdParty/StanHull/hull.cpp: In function ?int StanHull::overhull(StanHull::Plane*, int, StanHull::float3*, int, int, StanHull::float3*&, int&, int*&, int&, float)?:
171:((SNIP))/Urho3D-1.5/Source/ThirdParty/StanHull/hull.cpp:2590:28: warning: converting to non-pointer type ?int? from NULL [-Wconversion-null]
172:   if(verts_count <4) return NULL;
173:                             ^
174: Linking CXX static library libStanHull.a
175: [ 16%] Built target StanHull[/code]


I think this might be the issue: message from g++ [[ `tmpnam` is dangerous, better use `mkstemp` instead ]]

[code]256: Scanning dependencies of target lua_interpreter
257: [ 25%] Building C object Source/ThirdParty/Lua/CMakeFiles/lua_interpreter.dir/src/lua.c.o
258: Linking C executable ../../../bin/lua
259: libLua.a(loslib.c.o): In function `os_tmpname':
260: loslib.c:(.text+0x23d): warning: the use of `tmpnam' is dangerous, better use `mkstemp'
261: [ 25%] Built target lua_interpreter
262: Scanning dependencies of target luac
263: [ 25%] Building C object Source/ThirdParty/Lua/CMakeFiles/luac.dir/src/luac.c.o
264: Linking C executable ../../../bin/luac
265: [ 25%] Built target luac[/code]


knet:

[code]278:  Scanning dependencies of target kNet
...
300: [ 29%] Building CXX object Source/ThirdParty/kNet/CMakeFiles/kNet.dir/src/unix/UnixEvent.cpp.o
301: ((SNIP))/Urho3D-1.5/Source/ThirdParty/kNet/src/unix/UnixEvent.cpp: In member function ?void kNet::Event::Set()?:
302: ((SNIP))/Urho3D-1.5/Source/ThirdParty/kNet/src/unix/UnixEvent.cpp:157:32: warning: ignoring return value of ?ssize_t read(int, void*, size_t)?, declared with attribute warn_unused_result [-Wunused-result]
303:   read(fd[0], &val, sizeof(val));
304:                                 ^
305: Linking CXX static library libkNet.a
306: [ 29%] Built target kNet[/code]


LibCpuId:

[code]542: Scanning dependencies of target LibCpuId
...
548: [ 50%] Building C object Source/ThirdParty/LibCpuId/CMakeFiles/LibCpuId.dir/src/rdtsc.c.o
549: ((SNIP))/Urho3D-1.5/Source/ThirdParty/LibCpuId/src/rdtsc.c: In function ?cpu_clock_by_ic?:
550: ((SNIP))/Urho3D-1.5/Source/ThirdParty/LibCpuId/src/rdtsc.c:268:3: warning: format ?%llu? expects argument of type ?long long unsigned int?, but argument 4 has type ?uint64_t? [-Wformat=]
551:    debugf(2, "c = %d, td = %llu\n", c, t1 - t0);
552:    ^
553: Linking C static library libLibCpuId.a
554: [ 50%] Built target LibCpuId[/code]


the same dangerous warning:

[code]556: Scanning dependencies of target tolua++
557: [ 50%] Building C object Source/ThirdParty/toluapp/src/bin/CMakeFiles/tolua++.dir/tolua.c.o
558: [ 50%] Building C object Source/ThirdParty/toluapp/src/bin/CMakeFiles/tolua++.dir/generated/toluabind.c.o
559: Linking C executable ../../../../../bin/tool/tolua++
560: ../../../Lua/libLua.a(loslib.c.o): In function `os_tmpname':
561: loslib.c:(.text+0x23d): warning: the use of `tmpnam' is dangerous, better use `mkstemp'
562: [ 50%] Built target tolua++[/code]


and here:

[code]580: Scanning dependencies of target Urho3D
...
817: [ 76%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/IO/Deserializer.cpp.o
818: [ 76%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/IO/File.cpp.o
819: ((SNIP))/Urho3D-1.5/Source/Urho3D/IO/File.cpp: In member function ?virtual unsigned int 820: Urho3D::File::Read(void*, unsigned int)?:
820: ((SNIP))/Urho3D-1.5/Source/Urho3D/IO/File.cpp:310:84: warning: ignoring return value of ?size_t fread(void*, size_t, size_t, FILE*)?, declared with attribute warn_unused_result [-Wunused-result]
821:                  fread(blockHeaderBytes, sizeof blockHeaderBytes, 1, (FILE*)handle_);
822:                                                                                     ^
823: ((SNIP))/Urho3D-1.5/Source/Urho3D/IO/File.cpp:323:73: warning: ignoring return value of ?size_t fread(void*, size_t, size_t, FILE*)?, declared with attribute warn_unused_result [-Wunused-result]
824:                  fread(inputBuffer_.Get(), packedSize, 1, (FILE*)handle_);
825:                                                                          ^
826: [ 76%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/IO/FileSystem.cpp.o
827: ((SNIP))/Urho3D-1.5/Source/Urho3D/IO/FileSystem.cpp: In member function ?Urho3D::String Urho3D::FileSystem::GetCurrentDir() const?:
828: ((SNIP))/Urho3D-1.5/Source/Urho3D/IO/FileSystem.cpp:534:27: warning: ignoring return value of ?char* getcwd(char*, size_t)?, declared with attribute warn_unused_result [-Wunused-result]
829:      getcwd(path, MAX_PATH);
830:                            ^
831: ((SNIP))/Urho3D-1.5/Source/Urho3D/IO/FileSystem.cpp: In member function ?Urho3D::String Urho3D::FileSystem::GetProgramDir() const?:
832: ((SNIP))/Urho3D-1.5/Source/Urho3D/IO/FileSystem.cpp:711:48: warning: ignoring return value of ?ssize_t readlink(const char*, char*, size_t)?, declared with attribute warn_unused_result [-Wunused-result]
833:      readlink(link.CString(), exeName, MAX_PATH);
834:                                                 ^
835: [ 76%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/IO/Log.cpp.o
836: [ 77%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/IO/Serializer.cpp.o
837: [ 77%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LuaScript/generated/CoreLuaAPI.cpp.o[/code]


and more of the dangerous function here:

[code]580: Scanning dependencies of target Urho3D
...
851: [ 78%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/LuaScript/generated/SceneLuaAPI.cpp.o
852: Linking CXX static library ../../lib/libUrho3D.a
853: Merging all archives into a single static library using ar
854: [ 78%] Built target Urho3D
855: Scanning dependencies of target Urho3DPlayer
856: [ 78%] Building CXX object Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/Urho3DPlayer.cpp.o
857: Linking CXX executable ../../../bin/Urho3DPlayer
858: ../../../lib/libUrho3D.a(loslib.c.o): In function `os_tmpname':
859: loslib.c:(.text+0x23d): warning: the use of `tmpnam' is dangerous, better use `mkstemp'
860: [ 78%] Built target Urho3DPlayer
861: Scanning dependencies of target Assimp
862: [ 78%] Building CXX object Source/ThirdParty/Assimp/CMakeFiles/Assimp.dir/code/Assimp.cpp.o[/code]


here:

[code]861:: Scanning dependencies of target Assimp
...
1012: [ 94%] Building C object Source/ThirdParty/Assimp/CMakeFiles/Assimp.dir/contrib/unzip/ioapi.c.o
1013: [ 94%] Building C object Source/ThirdParty/Assimp/CMakeFiles/Assimp.dir/contrib/unzip/unzip.c.o
1014: ((SNIP))/Urho3D-1.5/Source/ThirdParty/Assimp/contrib/unzip/unzip.c: In function ?unzOpenCurrentFile3?:
1015: ((SNIP))/Urho3D-1.5/Source/ThirdParty/Assimp/contrib/unzip/unzip.c:1177:24: warning: assignment from incompatible pointer type
1016:          s->pcrc_32_tab = get_crc_table();
1017:                         ^
1018: [ 94%] Building C object Source/ThirdParty/Assimp/CMakeFiles/Assimp.dir/contrib/zlib/adler32.c.o
1019: [ 94%] Building C object Source/ThirdParty/Assimp/CMakeFiles/Assimp.dir/contrib/zlib/compress.c.o[/code]


another dangerous message here:

[code]1060: Scanning dependencies of target ScriptCompiler
1061: [ 96%] Building CXX object Source/Tools/ScriptCompiler/CMakeFiles/ScriptCompiler.dir/ScriptCompiler.cpp.o
1062: Linking CXX executable ../../../bin/tool/ScriptCompiler
1063: ../../../lib/libUrho3D.a(loslib.c.o): In function `os_tmpname':
1064: loslib.c:(.text+0x23d): warning: the use of `tmpnam' is dangerous, better use `mkstemp'
1065: [ 96%] Built target ScriptCompiler[/code]


That's all the error and warning messages I got during my installation and compilation of Urho3D on my computer.  NOTE that dispite the errors and warnings, all of the samples work just fine and pretty fast in my machine too!


So I believe the "dangerous" messages form GCC/G++ are likely the cause of the virus scanner programs incorrectly flagging Urho3D or the Urho3DPlayer , imho...


Hope any of that helps someone in some way.

-------------------------

weitjong | 2017-01-02 01:12:04 UTC | #8

Nah. I don't think this was the reason. I believe it was more to cosmic alignment   :wink:  that our build artifacts contain signature of a malware and being wrongly flagged.

-------------------------

weitjong | 2017-01-02 01:12:12 UTC | #9

Our build artifacts were being wrongly flagged again  :frowning: . If we do nothing then soon our download page will look like these for those affected artifacts (Linux and Raspberry RPM version).

[spoiler][img]https://a.fsdn.com/con/img/screen-malware-1.png[/img][/spoiler]
[spoiler][img]https://a.fsdn.com/con/img/screen-malware-2.png[/img][/spoiler]
[spoiler][img]https://a.fsdn.com/con/img/screen-malware-3.png[/img][/spoiler]
I won't waste my time to send another request to whitelist them this time round because I understand now that the new snapshots will be kept wrongly flagged up. So, this post just serves as a head up.

-------------------------

evolarium | 2017-01-02 01:12:12 UTC | #10

I would point out that you can include binary files in Github releases, which are separate from the repository.  As an example, here's a quick test I did with a 1.5 release, including 3 of the build archives:

[url]https://github.com/evolarium/Urho3D/releases/tag/1.5[/url]

This would work fine for new versions, but may not work as well for snapshots, as it depends on having git tags for the version you want to release.  Depends on whether you want to have a bunch of snapshot git tags or not.  A quick search shows someone has written a command-line tool to manage releases, which may or may not be useful:

[url]https://github.com/aktau/github-release[/url]

-------------------------

weitjong | 2017-01-02 01:12:12 UTC | #11

Thanks for the info. However, as you have pointed out it won't work for the snapshot build artifacts. Creating a new tag for each packaging CI build is out of the question, IMHO.

-------------------------

