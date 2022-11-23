nico | 2019-09-23 09:15:26 UTC | #1

Hey ! 
I have a problem with the sound in urho3D.
```
Sound* sound = cache->GetResource<Sound>("Music/Ninja Gods.ogg");
sound->SetLooped(true);  
Node* node = scene_->CreateChild("Sound");
SoundSource* sound_source = node->CreateComponent<SoundSource>();
sound_source->SetSoundType(SOUND_MUSIC); 
sound_source->Play(sound);
```
i use this command to play sound when i start my program but it doesn't work.... 

Does any people have this problem too ??

Thanks for your answer
Have a nice day

-------------------------

Modanung | 2019-09-23 09:14:52 UTC | #2

Two questions:
- Are there any warnings or errors being logged?
- Does sound work for you in sample 14?

Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

nico | 2019-09-23 09:19:31 UTC | #3

Thnaks :)

Yes the SoundEffects work when i start it !

I have no error or warning but this message appear when i start my programm !

'MyExecutableName_d.exe' (Win32) : Chargé 'C:\Windows\SysWOW64\hid.dll'. Impossible de trouver ou d'ouvrir le fichier PDB.
'MyExecutableName_d.exe' (Win32) : Chargé 'C:\Windows\SysWOW64\setupapi.dll'. Impossible de trouver ou d'ouvrir le fichier PDB.
'MyExecutableName_d.exe' (Win32) : Chargé 'C:\Windows\SysWOW64\bcrypt.dll'. Impossible de trouver ou d'ouvrir le fichier PDB.
'MyExecutableName_d.exe' (Win32) : Chargé 'C:\Windows\SysWOW64\wintrust.dll'. Impossible de trouver ou d'ouvrir le fichier PDB.
'MyExecutableName_d.exe' (Win32) : Chargé 'C:\Windows\SysWOW64\XInput1_4.dll'. Impossible de trouver ou d'ouvrir le fichier PDB.
'MyExecutableName_d.exe' (Win32) : Chargé 'C:\Windows\SysWOW64\msctf.dll'. Impossible de trouver ou d'ouvrir le fichier PDB.
'MyExecutableName_d.exe' (Win32) : Chargé 'C:\Windows\SysWOW64\TextInputFramework.dll'. Impossible de trouver ou d'ouvrir le fichier PDB.
'MyExecutableName_d.exe' (Win32) : Chargé 'C:\Windows\System32\DriverStore\FileRepository\nvami.inf_amd64_39900ef41369c3dd\nvldumd.dll'. Impossible de trouver ou d'ouvrir le fichier PDB.
'MyExecutableName_d.exe' (Win32) : Chargé 'C:\Windows\SysWOW64\imagehlp.dll'. Impossible de trouver ou d'ouvrir le fichier PDB.
'MyExecutableName_d.exe' (Win32) : Chargé 'C:\Windows\SysWOW64\rsaenh.dll'. Impossible de trouver ou d'ouvrir le fichier PDB.
'MyExecutableName_d.exe' (Win32) : Chargé 'C:\Windows\System32\DriverStore\FileRepository\nvami.inf_amd64_39900ef41369c3dd\nvd3dum.dll'. Impossible de trouver ou d'ouvrir le fichier PDB.
Le thread 0x3b18 s'est arrêté avec le code 0 (0x0).
'MyExecutableName_d.exe' (Win32) : Chargé 'C:\Windows\SysWOW64\ResourcePolicyClient.dll'. Impossible de trouver ou d'ouvrir le fichier PDB.
'MyExecutableName_d.exe' (Win32) : Déchargé 'C:\Windows\SysWOW64\ResourcePolicyClient.dll'
'MyExecutableName_d.exe' (Win32) : Chargé 'C:\Windows\SysWOW64\nvspcap.dll'. Impossible de trouver ou d'ouvrir le fichier PDB.
'MyExecutableName_d.exe' (Win32) : Chargé 'C:\Windows\SysWOW64\gpapi.dll'. Impossible de trouver ou d'ouvrir le fichier PDB.
'MyExecutableName_d.exe' (Win32) : Chargé 'C:\Windows\SysWOW64\cryptnet.dll'. Impossible de trouver ou d'ouvrir le fichier PDB.
'MyExecutableName_d.exe' (Win32) : Chargé 'C:\Program Files\NVIDIA Corporation\Ansel\Tools\NvCameraWhitelisting32.dll'. Impossible de trouver ou d'ouvrir le fichier PDB.
'MyExecutableName_d.exe' (Win32) : Déchargé 'C:\Program Files\NVIDIA Corporation\Ansel\Tools\NvCameraWhitelisting32.dll'
'MyExecutableName_d.exe' (Win32) : Chargé 'C:\Program Files\NVIDIA Corporation\Ansel\Tools\NvCameraWhitelisting32.dll'. Impossible de trouver ou d'ouvrir le fichier PDB.
'MyExecutableName_d.exe' (Win32) : Déchargé 'C:\Program Files\NVIDIA Corporation\Ansel\Tools\NvCameraWhitelisting32.dll'

-------------------------

brojonisbro | 2019-09-23 10:54:01 UTC | #4

"cant find or open PDB file"

the files are inside System and Program Files, did you know if your NVIDIA drivers are OK?

u tried to run it with Admin Rights?

u compiled the source with debug or release?

look, i find this on google:

A [file] with the PDB [file extension] is most likely a file created in the Program Database format that's used to hold debugging information about a program or module, like a [DLL] or [EXE] file. They're sometimes called symbol files. (by LifeWife)

just trying to help~

-------------------------

Modanung | 2019-09-23 11:32:20 UTC | #5

Could you try replacing the `Sound*` with a `SharedPtr<Sound>`?

-------------------------

weitjong | 2019-09-24 02:09:13 UTC | #6

Are you using the sample code as your template? If yes then observe the highlighted line of code carefully.

https://github.com/urho3d/Urho3D/blob/fda628912d3ba7b0059e26135521f6a285d2dcae/Source/Samples/14_SoundEffects/SoundEffects.cpp#L71

By default Urho3D engine always enables the audio subsystem. However, the base sample code disables it as most of the samples do not use that feature and only reverts it back to enable when the sample app needs it. There was a time the base sample did not do that. So if you just follow some outdated wiki then you might likely end up like this too.

-------------------------

nico | 2019-09-24 09:47:20 UTC | #7

most of the .dll are okay now excpet three : nvldumd.dll - nvd3dum.dll - SS3DevProps.dll
Do you think it doesn't work because of that ?

brojonisbro i install the latest version of NVIDIA drivers now  and i compile with debug !

-------------------------

techel | 2019-09-29 09:12:28 UTC | #8

The PDB files are for debugging purpose only and are irrelevant for your problem.

-------------------------

