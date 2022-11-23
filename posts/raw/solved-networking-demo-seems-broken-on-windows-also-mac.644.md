GGibson | 2017-01-02 01:01:50 UTC | #1

When I run 17_SceneReplication there are a few weird things happening depending which operating system I'm on:

[b]Mac OS X 10.9.5[/b]
Urho3D v1.32 static 64-bit from sourceforge
client & server running localhost

1) The client has no change in visuals regardless of keyboard input. Only the server can see the effect of the client, meaning the client has to perform controls while viewing the server view to see what's going on.

2) The connection often drops after 20-60 seconds even though I'm on the default localhost (no address specified).

[b]Windows 7[/b]
Urho3D v1.32 static 64-bit from sourceforge
client & server running localhost

1) I can't right-click to change camera perspective as I can on the Mac side.

[b]Linux[/b]
Urho3D compiled from master
client & server running localhost

(will try this later in the day)

There are no strange error messages on either operating system, so I'm not sure what's going on.

-------------------------

OvermindDL1 | 2017-01-02 01:01:53 UTC | #2

I just tried that sample here on Linux 64-bit, one server and two clients, all working here as of the revision a few days ago, so in linux there does not seem to be an issue at least.

Are you sure the firewall on the other systems is not blocking anything just for a first check?

Ran the debugger on it?

Checked the packets?

-------------------------

cadaver | 2017-01-02 01:01:53 UTC | #3

Briefly tested 17_SceneReplication (Angelscript version) on Windows, connecting from 32bit build to 64bit build, and 64bit build to 64bit. Didn't find problems.

-------------------------

GGibson | 2017-01-02 01:01:54 UTC | #4

I tried on another Windows 7 system and it was fine, so I'll look into the firewall settings for both mac and windows and will post back. Thanks for the firewall suggestion.

-------------------------

GGibson | 2017-01-02 01:01:55 UTC | #5

Tried this last night with the following nonlocalhost combinations over wifi and also HW switch, using latest builds from master as of last night (except windows):

windows7-mac
windows7-windows7
mac-linux
mac-mac
linux-windows7

The most stable is window7-windows7, however the client view never displays anything but the floor. I think it should be displaying a sphere, which the camera follows as you move around?
Mac-Mac was sort of okay, in that in one of my many tests the client displayed the full sphere on the client side, which moved and updated the camera and everything. Still network drops resulting in disconnection / reconnection.

I thought maybe it was an OS limitation of socket buffer size, as stated here [url]http://stackoverflow.com/questions/7968566/what-would-cause-udp-packets-to-be-dropped-when-being-sent-to-localhost[/url] but on mac the buffer size is already quite large (6291456) for IP and I couldn't increase it (error too large).

Why does localhost-localhost have the same issue?

Current thoughts that I will pursue:
* It's a version thing, since I only compiled Urho from source on Mac & Linux?
* Use a debugger - figure out what's going on
* Use Wireshark - figure out what's going on

-------------------------

GGibson | 2017-01-02 01:01:58 UTC | #6

More of the same weirdness, but in logs format. This is the server log output. The client sees almost nothing wrong in this particular capture, with only one received malformed packet so I didn't post the client log output. Each time I run this it's different, which makes me wonder if it's a threading thing since kNet uses different included threading files depending on the OS.

[spoiler][Fri Dec 12 17:39:06 2014] WARNING: Starting Server()
[b][Fri Dec 12 17:39:06 2014] INFO: Started server on port 2345[/b]
41.056: recvfrom (8) in socket :0 (UDP server, connected=true, readOpen: true, writeOpen: true, maxSendSize=1400, sock: 0.0.0.0:2345, peer: (-), socket: 6, this: 0x7fdf8b01ece0)
41.0561: Received a datagram of size 8 to socket :0 (UDP server, connected=true, readOpen: true, writeOpen: true, maxSendSize=1400, sock: 0.0.0.0:2345, peer: (-), socket: 6, this: 0x7fdf8b01ece0) from endPoint 127.0.0.1:54541.
[Fri Dec 12 17:39:10 2014] WARNING: NewConnectionEstablished(): sending event E_CLIENTCONNECTED to client
[b][Fri Dec 12 17:39:10 2014] INFO: Client 127.0.0.1:54541 connected[/b]
41.0643: MessageConnection::EndAndQueueMessage: Queued message of size 2 bytes and ID 0xA.
[Fri Dec 12 17:39:10 2014] DEBUG: Loading resource Models/Sphere.mdl
[Fri Dec 12 17:39:10 2014] DEBUG: Loading resource Materials/StoneSmall.xml
41.0649: MessageConnection::EndAndQueueMessage: Queued message of size 1 bytes and ID 0x1.
41.0837: MessageConnection::EndAndQueueMessage: Queued message of size 14 bytes and ID 0x14.
41.0854: Socket::EndSend: Sent out 37 bytes to socket 127.0.0.1:54541 (UDP Slave, connected=true, readOpen: true, writeOpen: true, maxSendSize=1400, sock: 0.0.0.0:2345, peer: (-), socket: 6, this: 0x7fdf88e59580).
41.0859: recvfrom (11) in socket :0 (UDP server, connected=true, readOpen: true, writeOpen: true, maxSendSize=1400, sock: 0.0.0.0:2345, peer: (-), socket: 6, this: 0x7fdf8b01ece0)
41.086: Received a datagram of size 11 to socket :0 (UDP server, connected=true, readOpen: true, writeOpen: true, maxSendSize=1400, sock: 0.0.0.0:2345, peer: (-), socket: 6, this: 0x7fdf8b01ece0) from endPoint 127.0.0.1:54541.
41.086: Received a fragment of size 2b (index 1) for a transfer with ID 2, but that transfer had not been initiated!
[b]41.0861: Malformed UDP packet![/b] Byteofs 11, Packet length 11. Expected 514 bytes of message content, but only 0 bytes left!
41.0861: kNet::NetException thrown when processing UpdateConnection() for client connection: Malformed UDP packet received! Message payload missing.
41.0972: Received a fragment of size 2b (index 1) for a transfer with ID 2, but that transfer had not been initiated!
[b]41.0973: Malformed UDP packet![/b] Byteofs 11, Packet length 11. Expected 514 bytes of message content, but only 0 bytes left!
41.0973: kNet::NetException thrown when processing UpdateConnection() for client connection: Malformed UDP packet received! Message payload missing.
41.0974: recvfrom (50) in socket :0 (UDP server, connected=true, readOpen: true, writeOpen: true, maxSendSize=1400, sock: 0.0.0.0:2345, peer: (-), socket: 6, this: 0x7fdf8b01ece0)
41.0974: Received a datagram of size 50 to socket :0 (UDP server, connected=true, readOpen: true, writeOpen: true, maxSendSize=1400, sock: 0.0.0.0:2345, peer: (-), socket: 6, this: 0x7fdf8b01ece0) from endPoint 127.0.0.1:54541.
41.0974: Received a fragment of size 2b (index 1) for a transfer with ID 2, but that transfer had not been initiated!
[b]41.0975: Malformed UDP packet![/b] Byteofs 11, Packet length 11. Expected 514 bytes of message content, but only 0 bytes left!
41.0975: kNet::NetException thrown when processing UpdateConnection() for client connection: Malformed UDP packet received! Message payload missing.
41.1204: recvfrom (13) in socket :0 (UDP server, connected=true, readOpen: true, writeOpen: true, maxSendSize=1400, sock: 0.0.0.0:2345, peer: (-), socket: 6, this: 0x7fdf8b01ece0)
41.1204: Received a datagram of size 13 to socket :0 (UDP server, connected=true, readOpen: true, writeOpen: true, maxSendSize=1400, sock: 0.0.0.0:2345, peer: (-), socket: 6, this: 0x7fdf8b01ece0) from endPoint 127.0.0.1:54541.
[Fri Dec 12 17:39:11 2014] WARNING: ClientDisconnected(): disconnect
[b][Fri Dec 12 17:39:11 2014] INFO: Client 127.0.0.1:54541 disconnected[/b]
41.1485: recvfrom (31) in socket :0 (UDP server, connected=true, readOpen: true, writeOpen: true, maxSendSize=1400, sock: 0.0.0.0:2345, peer: (-), socket: 6, this: 0x7fdf8b01ece0)
41.1486: Received a datagram of size 31 to socket :0 (UDP server, connected=true, readOpen: true, writeOpen: true, maxSendSize=1400, sock: 0.0.0.0:2345, peer: (-), socket: 6, this: 0x7fdf8b01ece0) from endPoint 127.0.0.1:54541.
41.157: recvfrom (31) in socket :0 (UDP server, connected=true, readOpen: true, writeOpen: true, maxSendSize=1400, sock: 0.0.0.0:2345, peer: (-), socket: 6, this: 0x7fdf8b01ece0)
41.1571: Received a datagram of size 31 to socket :0 (UDP server, connected=true, readOpen: true, writeOpen: true, maxSendSize=1400, sock: 0.0.0.0:2345, peer: (-), socket: 6, this: 0x7fdf8b01ece0) from endPoint 127.0.0.1:54541.
[Fri Dec 12 17:39:11 2014] WARNING: NewConnectionEstablished(): sending event E_CLIENTCONNECTED to client
[b][Fri Dec 12 17:39:11 2014] INFO: Client 127.0.0.1:54541 connected[/b]
41.1633: MessageConnection::EndAndQueueMessage: Queued message of size 2 bytes and ID 0xA.
41.1634: MessageConnection::EndAndQueueMessage: Queued message of size 1 bytes and ID 0x1.
41.169: MessageConnection::EndAndQueueMessage: Queued message of size 14 bytes and ID 0x14.
[b]41.18: NetworkServer::ProcessNewUDPConnectionAttempt:[/b] Trying to overwrite an old connection with a new one! Discarding connection attempt datagram!
[Fri Dec 12 17:39:11 2014] WARNING: NewConnectionEstablished(): sending event E_CLIENTCONNECTED to client
[b][Fri Dec 12 17:39:11 2014] INFO: Client 127.0.0.1:54541 connected[/b][/spoiler]

-------------------------

OvermindDL1 | 2017-01-02 01:02:00 UTC | #7

Hmm, it really is reporting truncated UDP packets, interesting...
You really might just have to hook up a debugger and/or wireshark to start tracing as I cannot replicate it here...

-------------------------

GGibson | 2017-01-02 01:02:02 UTC | #8

It works perfectly on both a couple different linux boxes and mac OS X macbooks when I target the DEBUG release:
./cmake_gcc.sh -DURHO3D_SAMPLES=1 -DCMAKE_BUILD_TYPE=DEBUG
Works perfectly between server and client every time on localhost!

But the demo begins breaking when I target the default RELEASE release:
./cmake_gcc.sh -DURHO3D_SAMPLES=1

-------------------------

GGibson | 2017-01-02 01:02:05 UTC | #9

Here is a comparison of localhost captures between working and broken sessions.

Edit: These are Wireshark network capture files - you need Wireshark to view them.

[spoiler]Working (DEBUG target)
[dropbox.com/s/acw46ahtmaq44 ... capng?dl=0](https://www.dropbox.com/s/acw46ahtmaq44ao/good.pcapng?dl=0)
Broken (RELEASE target)
[dropbox.com/s/h20ombchinfc9 ... capng?dl=0](https://www.dropbox.com/s/h20ombchinfc9jn/bad.pcapng?dl=0)[/spoiler]

It's interesting that it appears the server does not respond correctly during the initial handshake.

-------------------------

weitjong | 2017-01-02 01:02:06 UTC | #10

Not able to view the screenshots in your last post. If you believe this is a bug then I suppose you can make a Github issue of it. Not promising it will get fix sooner though.

-------------------------

cadaver | 2017-01-02 01:02:06 UTC | #11

It could be the compiler making release mode "optimizations" or data rearrangements that make the protocol byte-incompatible. This would be very odd however, and I've personally never witnessed that with kNet.
 
What's the compiler & compiler version you're using when a "broken" build is produced?

-------------------------

GGibson | 2017-01-02 01:02:06 UTC | #12

Hi cadaver, thank you for the questions.

I see the same debug vs release broken behavior on the following configurations

Linux
version: Sabayon (gentoo-based, vanilla install)
compiler: g++ (Gentoo Hardened 4.8.3 p1.1, pie-0.5.9) 4.8.3
kernel: 3.17.0-sabayon
processor: x86_64 AMD Phenom(tm) II X4 920 Processor

Mac OSX
version: 10.9.5
compiler: Apple LLVM version 6.0 (clang-600.0.56) (based on LLVM 3.5svn)
kernel: 13.4.0
processor: Intel core i7 x86_64

Am I doing something wrong when I build Urho3D? Here is my process on both systems:
git clone [github.com/Urho3D/urho3d.git](https://github.com/Urho3D/urho3d.git) urho
cd urho
./cmake_gcc.sh -DURHO3D_SAMPLES=1
cd Build
make -j4

-------------------------

GGibson | 2017-01-02 01:03:15 UTC | #13

Wow, thanks for fixing that Lasse! The networking demonstration now works on all my systems.

-------------------------

