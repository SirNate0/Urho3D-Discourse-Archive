scorvi | 2017-01-02 00:59:02 UTC | #1

hey

i am running the sample game on linux and android in a local network (with a router). BUT i get a checksum error ... dont know why! 
log: 
[code][Sun May  4 14:46:05 2014] INFO: Opened log file Urho3D.log
[Sun May  4 14:46:05 2014] INFO: Created 1 worker thread
[Sun May  4 14:46:05 2014] INFO: Added resource path /home/vitali/Downloads/urho3d-Urho3D/Bin/CoreData/
[Sun May  4 14:46:05 2014] INFO: Added resource path /home/vitali/Downloads/urho3d-Urho3D/Bin/Data/
[Sun May  4 14:46:05 2014] INFO: Set screen mode 1024x768 windowed
[Sun May  4 14:46:05 2014] INFO: Initialized input
[Sun May  4 14:46:05 2014] INFO: Initialized user interface
[Sun May  4 14:46:05 2014] INFO: Initialized renderer
[Sun May  4 14:46:05 2014] INFO: Set audio mode 44100 Hz stereo interpolated
[Sun May  4 14:46:05 2014] INFO: Compiled script module Scripts/NinjaSnowWar.as
[Sun May  4 14:46:06 2014] INFO: Connecting to server 192.168.178.48:1234
[Sun May  4 14:46:06 2014] INFO: Connected to server
[Sun May  4 14:46:06 2014] INFO: Loading scene from Scenes/NinjaSnowWar.xml
[Sun May  4 14:46:07 2014] ERROR: Scene checksum error
[/code]

i have the same problem running my verse server/client on android and connecting to it on linux/windows, can not pass the checksum test ...
can the error be because of the Endianess ( Little Endian & Big Endian ) ?

edit:

tested  sample game on two android devices and it is working !  so only connections between android and win/linux does not work ...:-/

-------------------------

cadaver | 2017-01-02 00:59:02 UTC | #2

This should be fixed in the master branch. Android did not calculate file checksums properly, leaving them to 0.

-------------------------

scorvi | 2017-01-02 00:59:03 UTC | #3

wow thx that was fast ! 

hmm can you say how you narrowed the bug down ? because i have to find out why the client server authentication with verse is not working ... i can say it is because auf the encryption and decryption process but not more ... the logging process in the verse lib is done with printf and android does not print those out ...

-------------------------

cadaver | 2017-01-02 00:59:03 UTC | #4

I knew that it would be File::GetChecksum() giving a different (wrong) value. When I looked at that function, I saw it was just checking the file handle for being null (it's legal to be null when we are reading data from a file within the APK) and I'd already fixed similar errors before.

-------------------------

