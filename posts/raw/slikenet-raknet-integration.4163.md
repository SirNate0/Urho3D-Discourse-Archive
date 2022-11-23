Miegamicis | 2018-04-09 21:44:23 UTC | #1

Currently I'm trying to implement [this](https://github.com/SLikeSoft/SLikeNet) library in the Urho3D engine to completely replace kNet and allow all the nice features that are available in RakNet but not in kNet library (NAT Punchtrough, LAN discovery and other nice things).

I need advice on how to proceed further. As I understood RakNet doesn't have distinction between client and server connections but in engine there are Network and Connection classes which leads to duplicate code in both classes if I keep the existing structure. Changes are inevitable if I want to proceed I just want to understand the best approach to this problem before I move further with the development.

BTW. Library found in [this](https://discourse.urho3d.io/t/recommend-to-use-kcp-to-replace-the-knet/3495) thread.

-------------------------

Eugene | 2018-04-10 06:45:32 UTC | #2

BTW, have you looked at @Sinoid’s port of RakNet for Urho?

-------------------------

Sinoid | 2018-04-10 07:55:40 UTC | #3

There wasn't really any duplication involved in switching to RakNet. It was basically a by-the-numbers piece-wise replacement.

`Connection` was and remained a helper with state-data for an end-point. In RakNet instead of the `kNet::MessageConnection` the `RakNet::AddressOrGUID` and the already initialized peer interface are passed off to `Connection` so it knows who to send everything to for that connection.

The switch to RakNet doesn't eliminate any of the other state tracking per-endpoint that the `Connection` has to do.

It was a pretty boring switch-over. The most excitement was debating where to place the Hash function for RakNet::AddressOrGUID to be used in Urho containers.

Edit: here's a link to the [zip dump for RakNet I did](https://1drv.ms/u/s!ApddaGejzZuYkHMBBpOALfhGzBPo), deliberately not in Github anywhere - but it's a-ok for someone else to put it there. Just an **I** will not support you thing.

-------------------------

Miegamicis | 2018-04-10 07:58:17 UTC | #4

I actually used your code (@Sinoid)  as a base to build everything, but seems like somewhere I made the wrong turn. I'm now digging in a bit deeper and it makes sense how you managed to implement RakNet inside the engine.

-------------------------

Miegamicis | 2018-04-10 10:54:54 UTC | #5

So I dug a bit deeper in the @Sinoid implementation of RakNet. The difference is that I was trying to make the server and client work in paralel in host application since kNet implementation allowed that and I was overcomplicating things. Anyway, I did manage to get it to work.

-------------------------

Miegamicis | 2018-04-11 14:36:44 UTC | #6

Update:
Everyting seems to be working just fine, only thing that I havent yet tested is the package downloading functionality. 
I was able to implement NAT punchtrough functionality which requires server to be hosted on a public host, docker image for that can be found [here](https://hub.docker.com/r/arnislielturks/slikenet-nat-server/)! You're welcome!
Server authorization via password is implemented.
LAN broadcasting was already created by @Sinoid. 
AngelScript bindings are added to support new functionality. Haven't yet created a repo for all of these changes but I'm planning to to that this week if everything goes as planned.

-------------------------

yushli1 | 2018-04-11 14:56:25 UTC | #7

It sounds quite interesting. Is there any plan to merge this into Urho3D's main branch?

-------------------------

Miegamicis | 2018-04-11 15:04:14 UTC | #8

I really hope so. I will create a PR later and after that we'll see how it goes. These are pretty large changes and additional testing is needed to check whether everything else still works as expected. I already know that few samples will have to be fixed but I'm also planning to do that.

-------------------------

Miegamicis | 2018-04-12 10:56:24 UTC | #9

I created PR for this functionality: https://github.com/urho3d/Urho3D/pull/2302

-------------------------

smellymumbler | 2018-04-12 16:13:07 UTC | #10

CI seems to be failing.

-------------------------

Miegamicis | 2018-04-13 08:59:06 UTC | #11

MinGW compiler is the one that fails. I'm trying to fix that.

-------------------------

Miegamicis | 2018-04-25 08:45:21 UTC | #12

This implementation is in the "ready for merge" state, it would be helpful if someone could test this out and give some feedback. Functionality is available in the test branch https://github.com/urho3d/Urho3D/tree/ArnisLielturks-SLikeNet

PR: https://github.com/urho3d/Urho3D/pull/2302

So far I have covered these platforms:
Ubuntu 14.04 (native and cross compiling with MinGW)
Ubuntu 16.04 (native. cross compiling with MinGW and Android NDK r15c ARM and x86)
Windows 10 (Visual Studio, Android NDK r15c ARM and x86)
Raspberry PI 3 (native)

Best way to test this out is to build the engine as usual and run the network samples:
16_Chat
17_SceneReplication
52_NATPunchtrough
53_LANDiscovery

Thanks in advance!

BTW: For the NAT punchtrough functionality testing you can use https://github.com/ArnisLielturks/Urho3D-NAT-server  
OR 
use already prebuilt docker image https://hub.docker.com/r/arnislielturks/slikenet-nat-server/

-------------------------

johnnycable | 2018-04-25 15:15:28 UTC | #13

I'm on Os X. There are two branches, one is Os X Ci specific. Which one do I have to use?

-------------------------

weitjong | 2018-04-25 15:25:05 UTC | #14

Not the OS X specific one. That is a so-called mirror branch and should be short-lived one. If you do a prune then it should be deleted in your local repo.

-------------------------

johnnycable | 2018-04-25 15:26:17 UTC | #15

Ok, thanks (20 char filler)

-------------------------

johnnycable | 2018-04-25 16:35:14 UTC | #16

About the Nat server: where do I have to copy the Urho3D-NAT-server directory exactly, in the Urho build tree? The whole dir or just the files?
cp <+++nat+++server> <Urho3D+++???>

-------------------------

Miegamicis | 2018-04-25 17:51:28 UTC | #17

Copy whole project in the urho source directory. Then run cmake and everything else. NAT punchtrough server is built as a sub project for the engine.

-------------------------

elix22 | 2018-04-26 06:12:44 UTC | #18

NAT Punchthrough Server failed to compile on my Mac (didn't check yet on Windows or Linux).
I had to modify the SLikeNet CMakeLists.txt  file to make it pass .
 -D_RAKNET_SUPPORT_NatPunchthroughServer=1

-------------------------

Miegamicis | 2018-04-26 06:26:48 UTC | #19

Thanks for the info! For the Windows and Linux builds by default all the SLikeNet functionality is built, and I had to disable everything manually that the engine wasn't using. And for the NAT server I just commented out the functionality which is needed for the NAT punchtrough server to work: https://github.com/ArnisLielturks/Urho3D-NAT-server/blob/master/Source/ThirdParty/SLikeNet/CMakeLists.txt#L27-L28

-------------------------

elix22 | 2018-04-26 06:54:14 UTC | #20

OK , my bad , missed this CMakeLists.txt
I used the original that came with the ArnisLielturks-SLikeNet branch.
overwriting the original with the one from NAT-server  passed compilation also on Mac.

All 4 examples worked  on my Mac locally.

-------------------------

elix22 | 2018-04-27 09:56:18 UTC | #21

16_Chat is not working properly .
Open 1 server and 2 chat clients .
send some massage from 1 client , 
The message is not seen/received on the other client.

-------------------------

Eugene | 2018-04-27 12:31:46 UTC | #22

I noticed it too but I thought for some reason it's feature... Because all messages are still traced on server side.
BTW, old Chat is broken too. When I run it in borderless mode, chat log is hidden under bottom edge of screen.

-------------------------

elix22 | 2018-04-27 16:37:43 UTC | #23

It's a bug , although every bug can be considered a feature  :slight_smile:
 
The fix , at the end of the method  below change the following code : 

void Network::HandleIncomingPacket(SLNet::Packet* packet, bool isServer)
{

...
    // Urho3D messages
    if (packetID >= ID_USER_PACKET_ENUM)
    {
        if (isServer)
        {
            HandleMessage(packet->systemAddress, 0, packetID, (const char*)(packet->data + dataStart), packet->length - dataStart);
        }
        else
        {
            MemoryBuffer buffer(packet->data + dataStart, packet->length - dataStart);
			bool processed =  serverConnection_->ProcessMessage(packetID, buffer);
			if (processed == false)
			{
				HandleMessage(packet->systemAddress, 0, packetID, (const char*)(packet->data + dataStart), packet->length - dataStart);
			}
        }
        packetHandled = true;
    }
}

-------------------------

Miegamicis | 2018-04-27 18:56:05 UTC | #24

Thanks for the fix, will test it out and create a commit for these changes.

-------------------------

elix22 | 2018-05-01 18:25:30 UTC | #25

I tried 16_Chat on my iPad and got an exception .
This is a general issue for both iOS and macOS , getaddrinfo() returns NULL if passing the hostname.
But on my Mac I fixed it by adding my hostname to /etc/hosts
Anyway I fixed it by modifying the function below , the code is compiled to support IPv4 only.
If you will compile the code to support IPv6 (RAKNET_SUPPORT_IPV6==1) you will also have to modify the function GetMyIP_Windows_Linux_IPV4And6().
With the below fix you won't need to modify /etc/hosts on macOS.

Basically so far I verified it on 3 devices connected to my WIFI LAN .
Windows laptop
Mac laptop
iPad

The chat app runs on all 3 , with the 2 fixes , all 3 can send/receive messages to/from each other.
```
void GetMyIP_Windows_Linux_IPV4( SystemAddress addresses[MAXIMUM_NUMBER_OF_INTERNAL_IDS] )
{



	int idx=0;
	char ac[ 80 ];
	int err = gethostname( ac, sizeof( ac ) );
    (void) err;
	RakAssert(err != -1);
    const char *localhost_str="localhost";
	
	struct addrinfo *curAddress = NULL;
	err = getaddrinfo(ac, NULL, NULL, &curAddress);

    if(curAddress == NULL)
    {
        err = getaddrinfo(localhost_str, NULL, NULL, &curAddress);
    }
    
	if ( err != 0 || curAddress == 0 )
	{
		RakAssert(false);
		return ;
	}
	while (curAddress != NULL && idx < MAXIMUM_NUMBER_OF_INTERNAL_IDS)
	{
		if (curAddress->ai_family == AF_INET) {
			addresses[idx].address.addr4 = *((struct sockaddr_in *)curAddress->ai_addr);
			++idx;
		}
		curAddress = curAddress->ai_next;
	}
	
	while (idx < MAXIMUM_NUMBER_OF_INTERNAL_IDS)
	{
		addresses[idx]=UNASSIGNED_SYSTEM_ADDRESS;
		idx++;
	}

}
```

-------------------------

