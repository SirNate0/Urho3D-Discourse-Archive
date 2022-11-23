lexx | 2017-06-10 03:53:51 UTC | #1

Hi.
I checked https://urho3d.github.io/samples/  web+AS, works great so I want  to try this too.

I downloaded web shared -packet from https://sourceforge.net/projects/urho3d/files/Urho3D/Snapshots/

Examples in  Urho3D-1.6.944-Web-SHARED-snapshot\share\Urho3D\Applications\  directory works on firefox, but Urho3DPlayer doesn't show anything but black screen. 

Log shows no error:
> [Sat Jun 10 06:45:52 2017] INFO: Opened log file Urho3D.log
> [Sat Jun 10 06:45:52 2017] INFO: Added resource package /Data.pak
> [Sat Jun 10 06:45:52 2017] INFO: Added resource package /CoreData.pak
> [Sat Jun 10 06:45:52 2017] INFO: Set screen mode 1024x768 windowed monitor 0
> [Sat Jun 10 06:45:52 2017] INFO: Initialized input
> [Sat Jun 10 06:45:52 2017] INFO: Initialized user interface
> [Sat Jun 10 06:45:52 2017] INFO: Initialized renderer
> [Sat Jun 10 06:45:52 2017] WARNING: Could not get application preferences directory
> [Sat Jun 10 06:45:52 2017] INFO: Set audio mode 48000 Hz stereo interpolated
> [Sat Jun 10 06:45:52 2017] INFO: Initialized engine
> [Sat Jun 10 06:45:53 2017] INFO: Scripts/NinjaSnowWar.as:62,1 Compiling void Start()
> [Sat Jun 10 06:45:53 2017] INFO: Scripts/NinjaSnowWar.as:90,9 Candidates are:
> [Sat Jun 10 06:45:53 2017] INFO: Scripts/NinjaSnowWar.as:90,9 void StartGame(int connection)
> [Sat Jun 10 06:45:53 2017] INFO: Scripts/NinjaSnowWar.as:168,1 Compiling void InitNetworking()
> [Sat Jun 10 06:45:53 2017] INFO: Scripts/NinjaSnowWar.as:320,1 Compiling void SpawnPlayer(int)
> [Sat Jun 10 06:45:53 2017] INFO: Scripts/NinjaSnowWar.as:568,1 Compiling void HandleClientIdentity(StringHash, VariantMap&inout)
> [Sat Jun 10 06:45:53 2017] INFO: Scripts/NinjaSnowWar.as:578,1 Compiling void HandleClientSceneLoaded(StringHash, VariantMap&inout)
> [Sat Jun 10 06:45:53 2017] INFO: Scripts/NinjaSnowWar.as:588,1 Compiling void HandleClientDisconnected(StringHash, VariantMap&inout)
> [Sat Jun 10 06:45:53 2017] INFO: Scripts/NinjaSnowWar.as:652,1 Compiling void HandleNetworkUpdateSent()
> [Sat Jun 10 06:45:53 2017] INFO: Scripts/NinjaSnowWar.as:726,1 Compiling void SendScore(int)
> [Sat Jun 10 06:45:53 2017] INFO: Scripts/NinjaSnowWar.as:736,1 Compiling void SendHiscores(int)
> [Sat Jun 10 06:45:53 2017] INFO: Scripts/NinjaSnowWar.as:860,1 Compiling void CheckEndAndRestart()
> [Sat Jun 10 06:45:53 2017] INFO: Scripts/NinjaSnowWar.as:877,9 Candidates are:
> [Sat Jun 10 06:45:53 2017] INFO: Scripts/NinjaSnowWar.as:877,9 void StartGame(int connection)
> [Sat Jun 10 06:45:53 2017] INFO: Scripts/NinjaSnowWar.as:880,1 Compiling void UpdateControls()

So I uploaded Urho3DPlayer.html, Urho3DPlayer.js, Urho3D.js and Urho3D.js.data files to my home page to test, same thing, black screen.
Tried some other test too, using   ..../Urho3DPlayer.html?00_Test.as  and no error, only black screen.

How to use Urho3DPlayer in web?

-------------------------

weitjong | 2017-06-10 10:07:31 UTC | #2

Urho3DPlayer needs a script name to play. If none provided then it is defaulted to play (network) NinjaSnowWar.as. Unfortunately as of this moment the network subsystem is not yet ported to Web platform, so the script failed to run and you saw black screen. To play any other AS script, however, just passing its name in the request parameter. Mouse over our online demo URL links to see how exactly this is done.

-------------------------

lexx | 2017-06-10 06:12:12 UTC | #3

Ahaa, thats why, thanks for the info about networking.

I had problems with other scripts too, but just noticed that scripts must be in different directory than player.

-------------------------

