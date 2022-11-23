Miegamicis | 2018-08-31 13:32:00 UTC | #1

If you are following the Urho3D repository on github you maybe know that previous kNet networking library was replaced with the more powerfull SLikeNet library. It introduces few new things like password authentication for client/server connections, LAN discovery and NAT punchtrough mode. I will talk a bit more about the NAT punchtrough functionality - how to set it up etc.

---

**What is NAT punchtrough?** 

In short - it's a tehcnique that allows you to host publicly available servers if you are behind router without changing router settings.

More information about it here: http://www.raknet.net/raknet/manual/natpunchthrough.html

---

**How to use it?**

The engine contains 52_NATPunchtrough sample but it's useless unless you have a NAT punchtrough master server to connect to. So here i will show you how to get it up and running.

There are 2 possible ways how to do that:

1.  Run a docker image which already contains it

2. Build it yourself

---

If you want to go with the 1st option, here's the docker image that gets the job done:

https://hub.docker.com/r/arnislielturks/slikenet-nat-server/

If everything worked you should be able to connect to NAT punchtrough master server with the 52_NATPunchtrough sample. By default master server uses 61111 UDP port but you can easily change it to something else

---


If that's not an option you can always build the NAT punchtrough master server yourself.

I have created a repo which allows to build it on top of Urho3D engine as a subproject: https://github.com/ArnisLielturks/Urho3D-NAT-server

Just copy the `Source` folder content from the repo to the Urho3D engine `Source` folder. Build the engine as usual and if everything worked, you should see `NATServer` executable in the build `bin` directory. 

**Note:** NAT punchtrough master server should be placed on a public server!

---

**How to let others join my server?**

52_NATPunchtrough sample shows just how to do that. When you create a server using NAT punchtrough mode your server will generate unique GUID. You can then retrieve it by calling `Network::GetGUID` (https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Network/Network.h#L74).

This GUID is later used by others to allow them to connect to your server using NAT punchtrough mode. Instead of calling `Network::Connect` they'll have to call `Network::AttemptNATPunchtrough` (https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Network/Network.h#L76)

---

**One more thing!** I actually have already running NAT punchtrough master server on Digital Ocean so if you would like just to test it out you can access it here: `178.62.212.92:61111`. It was built with the repo mentioned previously.

---

If you have any other questions, don't hesitate to ask.

-------------------------

tni711 | 2018-09-01 01:57:29 UTC | #2

I built the sample and tested it against your NAT punchtrough master server. It works! Really cool!


![52%20NATPunchtrough%20GUI|666x500](upload://pYZkgw7GneSbtsB4ZGT4jDZrqqs.png)

-------------------------

