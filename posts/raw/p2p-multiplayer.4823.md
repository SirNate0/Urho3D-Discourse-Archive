Miegamicis | 2019-01-15 08:32:50 UTC | #1

@Leith Thanks for your contributions! While you're at it, could you please check my P2P implementation I would like to get some feedback on that. https://github.com/urho3d/Urho3D/pull/2400
The problem that I see with my code changes is that the `Network::HandleIncomingPacket` method is 200+ lines of code.

-------------------------

Leith | 2019-01-15 08:32:50 UTC | #2

I will try to review it, I am still finding my feet so bear with me while I try to adapt

-------------------------

Leith | 2019-01-15 08:32:50 UTC | #3

maybe it would be faster and safer for me to review that method in isolation? perhaps you can email me that one file in isolation and I can look at that one method in isolation, 200+ lines of code is not a lot for a generic handler, but I may have some useful observations to report

-------------------------

Miegamicis | 2019-01-15 08:32:50 UTC | #4

Here it is: https://github.com/urho3d/Urho3D/blob/p2p-multiplayer/Source/Urho3D/Network/Network.cpp

-------------------------

Leith | 2019-01-15 08:32:50 UTC | #5

Gah, thats a lot to take in, and I assume you changed little - I will save your file for tomorrow, feed it into a diffing engine, and find out what you did :slight_smile:

-------------------------

Leith | 2019-01-15 08:32:50 UTC | #6

I'm not going to make any sense from your work today, it's been a long hot day
I will start tomorrow morning with a fresh outlook and pick on your (possibly quite good) work. The big boys around here seem to accept your changes. Let me look too and I may make some last minute suggests.

-------------------------

Leith | 2019-01-15 08:32:50 UTC | #7

The code appears long because there's a lot of cases to handle, but the amount of code for any given case looks quite reasonable... code does not look too horrible, although I did spot something strange:
 
           if (!isServer)
            {
                OnServerDisconnected();
}

What? If we're NOT A SERVER, we call OnServerDisconnected? Is that intentional?

I only recommend two things - the first IF case should be followed by ELSE, ie, made part of the main outer case handler. The other suggestion would be to convert the outer case handler to use SWITCH CASE, just to assist in making the code a bit more readable - although that is my personal opinion, and I am yet to read a coding standards document for Urho.

-------------------------

Miegamicis | 2019-01-15 08:32:50 UTC | #8

Yes, that's intentional. Because you can't disconnect from the server if you are the server. If i remember correctly, this event is also sent out if the connection to the NAT server disappears but that's another topic. I just wanted to get some feedback on the code quality. Thanks!

-------------------------

Leith | 2019-01-15 08:32:50 UTC | #9

You may want to comment this - typically, onServerXXX is only callable on servers, and OnClientXXX is only callable on clients - if we are both, we can call both, but generally speaking, Server api should not be named for client callers.

-------------------------

Miegamicis | 2019-01-15 08:32:50 UTC | #10

It's a bit different on the Urho. When client disconnects the `ClientDisconnected` method is called, when the server disconnects `OnServerDisconnected` method is called. But maybe this is another area that could be improved.

-------------------------

Leith | 2019-01-15 08:32:50 UTC | #11

thats precisely my point - the server and client side had well formed naming conventions for what would be called, while in your example, a client called a method named serverXXX

-------------------------

Leith | 2019-01-15 08:32:50 UTC | #12

i think the code is good, but we need good naming conventions for networking, its very important

-------------------------

Miegamicis | 2019-01-15 08:32:50 UTC | #13

Don't forget that single application can be the server and client at the same time. And p2p complicates it even more since all of the participants are the clients and servers.

-------------------------

Leith | 2019-01-15 08:32:50 UTC | #14

Yes, it clouds naming conventions, but we can use the diamond pattern here - we can separate client and server sides, into two classes, who are both inherited by the p2p class - we just need to add a comment and nod to the fact that we can call both, since we are both, and clarify it for the reader

-------------------------

Miegamicis | 2019-05-30 12:18:12 UTC | #15

I want to revive the conversation here.

P2P main functionality was finished a while ago, I think I managed to do all the work I wanted there and also created additional repo which contains P2P extended demo which works with the same stack mentioned in this thread. New repo is here: https://github.com/ArnisLielturks/Urho3D-P2P-Multiplayer
The PR contains dumbed down demos just to show the functionality. 
I'm planning to add Terraform scripts to automate the P2P stack creation (NAT master server and session master server) so that anyone could set it up as easy as possible and test it out.

There are still some grey areas with the P2P functionality like how to handle replication with the old server-client approach and make it consistent between p2p connections etc.

I see that there is ReplicaManager built in the SLikeNet core but haven't yet tested it.

Would be helpful if someone could test it and give some feedback on it, otherwise not really sure how to move forward with this.

-------------------------

smellymumbler | 2019-05-30 20:04:06 UTC | #16

Currently working on a small bomberman clone that maybe can be a good guinea pig for this!

-------------------------

Miegamicis | 2019-05-30 20:07:07 UTC | #17

Sounds cool, let me know if I can help in any way!

-------------------------

suppagam | 2019-07-18 01:37:51 UTC | #18

Thank you so much for the example. That was really useful and easy to understand. :star_struck:

-------------------------

