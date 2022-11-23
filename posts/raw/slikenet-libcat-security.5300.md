Tabasco | 2019-07-16 21:38:21 UTC | #1

Prior to SlikeNet replacing kNet I had my own framework with RakNet (that's a lot of nets)
I had a proof of concept compiled with LIBCAT_SECURITY enabled and a certificate pair for encryption.

With more recent builds I have to copy sections of the SlikeNet source to the Urho third party source tree to enable building this way.

Was this trimmed out for any particular reason?  I've seen enough good shooters ruined by simple network cheats that can headshot the entire map on a whim that I am concerned about security but I'm not experienced enough to be familiar with the best solutions.

-------------------------

Miegamicis | 2019-07-17 04:52:02 UTC | #2

There's a lot of functionality that SLikeNet provides that is not yet used by the engine and encryption is one of them. This is one of the things that I'm concerned about too, but due to lack of free time lately I'm unable to provide the much needed improvements and updates for the engine networking.

-------------------------

Leith | 2019-07-17 06:46:49 UTC | #3

Hey, my todo list grows and grows, but its an area of experience for me and also an area of concern.. I have decades of experience in network coding, and some extensive knowledge of key areas of weakness in networked games, how to identify and exploit weaknesses, and how to defend against the typical game attacks. I have written papers on the topic in the past, but I currently have no experience with our implementation.

-------------------------

Tabasco | 2019-07-17 22:37:38 UTC | #4

I appreciate all that you guys are doing.  If I can clean up my build process I can submit a PR that would at least allow the option to be defined and then add to the network API for setting up encrypted connections.  Once the keys are generated it's actually pretty simple to implement.

-------------------------

Leith | 2019-07-18 05:10:34 UTC | #5

I would request that encryption be declared by common interface and implemented as concrete implementation of common interface. I might want to use a different encryption algorithm or implementation and it would be nice to know it's easy to do that... please? :)

-------------------------

Tabasco | 2019-07-21 23:34:56 UTC | #6

For the moment I'm just leveraging the existing features of SLikeNet / RakNet.  It relies on the cat library and, when enabled, that just allows you to set up keys and associate them with a peer instance.

It basically amounts to this:

    ifstream inpub("data/pants");
    ifstream inpriv("data/knickers");

    string public_key( (istreambuf_iterator<char>(inpub)), (istreambuf_iterator<char>()) );
    string private_key( (istreambuf_iterator<char>(inpriv)), (istreambuf_iterator<char>()) );

    peer = SLNet::RakPeerInterface::GetInstance();
    peer->InitializeSecurity(public_key.c_str(), private_key.c_str());

Clients just connect with a public key.

    SLNet::PublicKey pk;
    pk.remoteServerPublicKey = const_cast<char*>(public_key.c_str());
    pk.publicKeyMode = SLNet::PKM_USE_KNOWN_PUBLIC_KEY;
    peer->Connect(host, SERVER_PORT, 0, 0, &pk);

What I have right now is the bare minimum for whatever future design is chosen and allows for low level SLNet integration in a project.  It builds with the cat library enabled and compiles the SLNet encryption sample to the bin/tools directory so keys can be easily generated from the command line.  I've also updated the bundled SLikeNet to a more recent version.

-------------------------

