TrevorCash | 2017-09-28 14:43:44 UTC | #1

I am having trouble with the Vector and HashMap classes..

I have a HashMap that uses (int, String) pairs.  At one point in my program i convert the keys into a Vector<int>:

> 	Vector\<int> densities = mMaterialZLevels.Keys();
> 	
> 	for (int i = 0; i < densities.Size(); i++) {
> 		URHO3D_LOGINFO("i: " + String(i) + " : " + String(densities[i]));
> 	}

This prints out:

> [Wed Sep 27 13:05:47 2017] INFO: i: 0 : 10
> [Wed Sep 27 13:05:47 2017] INFO: i: 1 : 410
> [Wed Sep 27 13:05:47 2017] INFO: i: 2 : 2146731646

Which is to be expected (except for the last number which i never insert as a key into the map.)

Now when I introduce a pop operation on the vector:
> 	Vector\<int> densities = mMaterialZLevels.Keys();
> 	densities.Pop();//remove arronious big number..??
> 
> 	for (int i = 0; i < densities.Size(); i++) {
> 		URHO3D_LOGINFO("i: " + String(i) + " : " + String(densities[i]));
> 	}

I get the following output:

> [Wed Sep 27 13:09:23 2017] INFO: i: 0 : 10

showing only 1 element in the list while there should be 2.


This is the first time I have used the Keys() function on a HashMap.  Could there be a bug there?  Or am I missing something obvious?


The definition of mMaterialZLevels:

> HashMap\<int, String> mMaterialZLevels;

I am using Visual Studio 2017 64bit, ReleaseWithDebug configuration.

Best - Trevor.

-------------------------

Eugene | 2017-09-27 20:00:47 UTC | #2

This looks crazy. Could you make minimal compilable piece of code that reproduces the problem?
Works fine for me:

    HashMap<int, String> mMaterialZLevels = { { 10, "1" }, { 410, "2" } };
    Vector<int> densities = mMaterialZLevels.Keys();
    for (int i = 0; i < densities.Size(); i++)
    {
        URHO3D_LOGINFO("i: " + String(i) + " : " + String(densities[i]));
    }

-------------------------

TrevorCash | 2017-09-28 14:43:16 UTC | #3

[quote="Eugene, post:2, topic:3614"]
HashMap&lt;int, String&gt; mMaterialZLevels = { { 10, "1" }, { 410, "2" } };
Vector&lt;int&gt; densities = mMaterialZLevels.Keys();
for (int i = 0; i &lt; densities.Size(); i++)
{
    URHO3D_LOGINFO("i: " + String(i) + " : " + String(densities[i]));
}
[/quote]

I agree,  I ended up reworking this section of my code anyway - and I did test your quick sample in my setup and it works fine.

Closing.

-------------------------

Eugene | 2017-09-28 16:32:19 UTC | #4

BTW, have you tried my debug visualizer for Urho types?
It could be helpful.
https://github.com/eugeneko/Urho3D-Debug

-------------------------

TrevorCash | 2017-09-28 19:42:54 UTC | #5

I just added it to my project, Is it supposed to show individual elements in Vectors and HashMaps?  I'm not sure its working for me because I haven't seen a difference.

-------------------------

Eugene | 2017-09-28 19:50:58 UTC | #6

Yes, I always use it. However, I use VS 2015
It is able to render most of containers, pointers and variant.
Could you check logs in output window for errors?

-------------------------

TrevorCash | 2017-09-28 19:57:08 UTC | #7

Heres the Debug output:

> 'GreatGame_d.exe' (Win32): Loaded 'C:\Users\casht\Repos\greatgame\Build\bin\GreatGame_d.exe'. Symbols loaded.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\ntdll.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\kernel32.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\KernelBase.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\imm32.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\winmm.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\user32.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\win32u.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\msvcrt.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\gdi32.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\winmmbase.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\winmmbase.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Unloaded 'C:\Windows\System32\winmmbase.dll'
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\gdi32full.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\winmmbase.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Unloaded 'C:\Windows\System32\winmmbase.dll'
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\cfgmgr32.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\msvcp_win.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\ucrtbase.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\ucrtbase.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Unloaded 'C:\Windows\System32\ucrtbase.dll'
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\ws2_32.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\sechost.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\version.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\rpcrt4.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\shell32.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\d3d9.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\msvcp140d.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\SHCore.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Users\casht\Repos\greatgame\Build\bin\d3dcompiler_47.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\advapi32.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\combase.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\vcruntime140d.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\ucrtbased.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\bcryptprimitives.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\dwmapi.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\windows.storage.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\shlwapi.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\kernel.appcore.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\powrprof.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\profapi.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\ole32.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\oleaut32.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\NapiNSP.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\pnrpnsp.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\nlaapi.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\mswsock.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\dnsapi.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\nsi.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\IPHLPAPI.DLL'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\winrnr.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\wshbth.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Program Files\Bonjour\mdnsNSP.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\uxtheme.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\clbcatq.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\dinput8.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\hid.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\setupapi.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\devobj.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\wintrust.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\msasn1.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\crypt32.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\XInput1_4.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\dsound.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\MMDevAPI.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\propsys.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\wdmaud.drv'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\ksuser.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\avrt.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\AudioSes.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\WinTypes.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\msacm32.drv'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\msacm32.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\midimap.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\msctf.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\TextInputFramework.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\CoreUIComponents.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\CoreMessaging.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\ntmarta.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\usermgrcli.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\DriverStore\FileRepository\nv_ref_pubwu.inf_amd64_f9309145156afb40\nvldumdx.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\imagehlp.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\cryptsp.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\rsaenh.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\bcrypt.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\cryptbase.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\DriverStore\FileRepository\nv_ref_pubwu.inf_amd64_f9309145156afb40\nvd3dumx.dll'. Cannot find or open the PDB file.
> The thread 0x3e28 has exited with code 0 (0x0).
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\ResourcePolicyClient.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Unloaded 'C:\Windows\System32\ResourcePolicyClient.dll'
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Program Files (x86)\NVIDIA Corporation\3D Vision\nvSCPAPI64.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\psapi.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\pid.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Unloaded 'C:\Windows\System32\pid.dll'
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\pid.dll'. Cannot find or open the PDB file.
> 'GreatGame_d.exe' (Win32): Unloaded 'C:\Windows\System32\pid.dll'
> 'GreatGame_d.exe' (Win32): Loaded 'C:\Windows\System32\Windows.UI.dll'. Cannot find or open the PDB file.

![image|193x186](upload://oFjb25pJ5IGnjNQHtbhMQrd77PH.png)

-------------------------

Eugene | 2017-09-28 20:10:56 UTC | #8

Well, DLL loading is not interesting.
Ensure that diagnostic is turned on and _try to debug some type_ like Vector.
If type is not visualized because of visualizer errors, Output window will contain Natvis logs.
[details="Somewhere in Options"]
![image|690x460](upload://dS6pohUNRKcJfjOCzcKCyWJHFe5.png)
[/details]

-------------------------

TrevorCash | 2017-09-28 20:14:54 UTC | #9

> Natvis: C:\Users\casht\Documents\Visual Studio 2017\Visualizers\Urho3D.natvis(7,11): Fatal error: DTD is prohibited.
> Natvis: C:\Users\casht\Repos\GreatGame\Urho3D.natvis(7,11): Fatal error: DTD is prohibited.
![image|690x275](upload://eZWtHuLlZLlNTJ73phH6otmzVjI.png)

-------------------------

Eugene | 2017-09-28 20:24:53 UTC | #10

That's crazy (x2)
It looks like VS bug because the Natvis XML doesn't have any DTD...
Maybe it worths to ask Microsft community and/or report a bug.

Ensure that the XML has Windows-style line ending.
It's sounds strange, but bad line endings make Visual Studio insane.

-------------------------

TrevorCash | 2017-09-28 20:33:57 UTC | #11

Woops - looks like I downloaded the wrong file contents from github. Visual Studio was trying to parse some html.

Its working now - Thanks Eugene this will be super helpful.

-------------------------

