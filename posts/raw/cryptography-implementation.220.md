silverkorn | 2017-01-02 00:58:57 UTC | #1

Hey team!

I've been looking to add some cryptography in Urho3D for transferring and stocking sensible/confidential data.
I found LibTomCrypt which may easily fit in the project as it's optimized to run on many OS and architectures.

I've tested the compilation through MinGW (32bit + 64bit) and GCC (32bit) and it seems to work properly so far.
The total size of the whole library is personally quite heavy once compiled (~800kb on Win32) but I'll compile only the necessary, common and/or and light hashing algorithms + public key infrastructures.

Now my question, shall I map and adapt the cryptographic functions in the "Core" section or in a new section called something like "Cryptography"?
Also, is it OK if this library is Public Domain?

BTW, sorry if there's some inconsistency, I'm more a scripting guy with network/system administration background then C/C++ programming.  :confused: 
Thanks!

-------------------------

Canardian | 2017-01-02 00:58:57 UTC | #2

I would take a look at Threefish, as LibTomCrypt has only the older versions called Blowfish and Twofish:
[schneier.com/threefish.html](https://www.schneier.com/threefish.html)
[code.google.com/p/geesefly/](https://code.google.com/p/geesefly/)

-------------------------

cadaver | 2017-01-02 00:58:57 UTC | #3

I don't mean my opinion to be the final say on this, but I'm not sure if cryptography should be in scope of Urho3D itself. Basically, if you need it in your own project, you can always integrate whatever library you like.

-------------------------

silverkorn | 2017-01-02 00:58:57 UTC | #4

[quote="cadaver"]I don't mean my opinion to be the final say on this, but I'm not sure if cryptography should be in scope of Urho3D itself. Basically, if you need it in your own project, you can always integrate whatever library you like.[/quote]

To be honest, I think it's important to have a minimum, just as I initially focused (Basic hashing and a PKI for transfers, this might decrease the result size by a lot).

Here's the main reason, if you want to make a managed and/or online game, you usually use a username/password structure, which is extremely unsecured exposed directly through the Web. Using a basic sniffer would easily see all this data, so PKI would be useful there.
I recently heard that there's organizations "legally" exploiting not known bugs, remember Heartbleed from OpenSSL? It was already discovered earlier but officially tested and proved by some Google's security staff before confirming it was leaking sensible data.

The hashing becomes important for the server side because unfortunately the industry is frequently "obliged" to follow audits.
Using them with keys + salt does the trick to avoid hackers having access to at least the passwords, which only needs to fit the digested result.

So I thought having a "light" compile flag for clients, with like few well known hashing algorithms (MD5, SHA1, SHA256 & SHA512) + PKI (RSA/PKCS#1) and a "full" compile flag for servers.

[quote="cadaver"]I don't mean my opinion to be the final say on this[/quote]
You're the father of Urho3D, if you fell this may have bad behavior to your child, I shall not impose it.  :smiley: 

But if you are not comfortable with these, well... No problem, I can create a repository which could be mergeable manually with your master, so it could be "plugin"-like and it will also mean that it's not directly supported by the main community (thought I would really like some feedback about it's compilation through principally Apple side since  don't own any of those).

To give you the main reason for this implementation, my current focus is to create a complete standalone server with Urho3D which could run properly on all platforms supported by Urho3D, such a Raspberry Pi or even an Android smartphone. 
Finally! Complete portable servers would be possible! :slight_smile:

-------------------------

cadaver | 2017-01-02 00:58:57 UTC | #5

I do see the merit of implementing cryptography as part of the engine, because it would avoid duplicate effort (assuming we end up with a set of crypto features/algorithms most are satisfied with) and could be made to integrate nicely with the IO classes like Serializer / Deserializer. Would like to hear others' opinions too.

Thinking of an engine integration, I'd prefer it to be a separate "sub"-library such as Crypto or Cryptography instead of putting it directly into the Core. Probably having 3 build levels would be ideal: crypto off (similar to URHO3D_ANGELSCRIPT=0, which disables AngelScript support completely), light crypto, and full.

-------------------------

silverkorn | 2017-01-02 00:58:57 UTC | #6

Ok, I'll focus with these guidelines.
You can follow the progress here: [url]https://github.com/silverkorn/Urho3D/tree/libtomcrypt-implementation[/url]

I could also add the suggestion from Canardian later.

-------------------------

friesencr | 2017-01-02 00:58:58 UTC | #7

For sending passwords over the wire I would use an https post.  The  http client can be compiled against openssl.

-------------------------

Canardian | 2017-01-02 00:58:58 UTC | #8

I wouldn't mind have one proven crypt/decrypt function in Urho3D, but it makes no sense for an game engine to have several. For a converter tool, it makes more sense, like the AssImpLib converter tool. From what I read, Threefish is currently the best, but there will be better ones in future also. The same goes for all other features in Urho3D: only include the best available, and forget the rest.

Currently Urho3D makes like 6MB big exe files at minimum, even when I disable all features I don't need. It would be nice if we could have a much smaller exe size, which only includes the code which the game actually uses. That would be seperate feature suggestion, but the crypt feature would benefit from it also.

I would personally need a crypt function to crypt sqlite3 records, and sqlite3 could be also included in Urho3D via some cmake defines. The sqlite3 db would be needed to read/write game data, which is kept in sync with the server's sqlite3 db.

-------------------------

silverkorn | 2017-01-02 00:58:58 UTC | #9

[quote="friesencr"]For sending passwords over the wire I would use an https post.  The  http client can be compiled against openssl.[/quote]

That was also my thoughts, but it's not currently straightforward with Civetweb (though I guess we only need to set a build flag like "OPENSSL_LIB=path" but we still need to compile a third party manually beside) but still I want to permit a simple, light and independent way to implement custom and well known techniques to encrypt and use PKI with the native UDP socket or Serialize / Deserialize methods.
RSA is what is mostly used with SSH2 and it's pretty robust. I would be ready to prepared an little handshake system for public-private asymmetric keys when requested on the UDP socket.

Otherwise, I've looked into axTLS/axhttpd ([url]http://axtls.sourceforge.net/[/url]) instead of Civetweb as it doesn't depend on OpenSSL and the license is interesting.
I think we could use this one instead if someone is good enough to test and confirm the send/receive mechanism on SSL/TLS and if people approve. :wink:


[quote="Canardian"]I would personally need a crypt function to crypt sqlite3 records, and sqlite3 could be also included in Urho3D via some cmake defines. The sqlite3 db would be needed to read/write game data, which is kept in sync with the server's sqlite3 db.[/quote]

Haha! You read in my mind, this was my next step! :slight_smile:
Though, more useful on a server than a client side, so this why another build flag for SQLite3.

-------------------------

silverkorn | 2017-01-02 00:58:58 UTC | #10

[quote="Canardian"]I wouldn't mind have one proven crypt/decrypt function in Urho3D, but it makes no sense for an game engine to have several.[/quote]
Yes and no. 
It still depends, this is why I'll focus on NONE (for simple games, default), LIGHT (mostly for clients to keep it lightweight, so well known encryptions + PKI (RSA-only?)) and FULL (mostly for servers, including all).

Yes for simple game and simple encryption.
No for those having a bigger project, sometime you rely on other apps and if there's only, by example, Threefish encryption and it's not supported by the external software, it's not really great. Also, I was strictly searching for PKI algorithms because someone having the public key (the client) for encrypting his information cannot decrypt with it, only the holder of the private key (the server) can decrypt this information.

Anyway, LibTomCrypt has building definitions (LTC_*), so we can define the most useful algorithms in the "LIGHT" build.

Just remember that depending on the needs: 
[ul]
[li][b][u]Hash[/u][/b] is useful for non reversible encryption, such as password, just make sure to salt wisely when storing it and during evaluation (from the server) so in case of intrusion, rainbow tables will only find unmatching values;[/li]
[li][b][u]Encryption (Symmetric)[/u][/b] is useful on a one on one communication, a key will both encrypt and decrypt the information, it's dangerous to transfer the key online;[/li]
[li][b][u]Public-key Infrastructure (Asymmetric)[/u][/b] is extreme useful. As mentioned before, it's useful for sending a generic key to many people and the key is only useful to encrypt the data, they would need the private key, logically only available on the server-side but "shareable" if needed, so only these holders can decrypt it.[/li][/ul]

-------------------------

Canardian | 2017-01-02 00:58:58 UTC | #11

[quote="silverkorn"]Though, more useful on a server than a client side, so this why another build flag for SQLite3.[/quote]
Yes, but for optimal performance, you don't want to query the server each time the player opens his inventory or moves some objects. Let the background replicator handle it in a lower frequency thread.

-------------------------

cadaver | 2017-01-02 00:58:58 UTC | #12

[quote="Canardian"]
Currently Urho3D makes like 6MB big exe files at minimum, even when I disable all features I don't need. It would be nice if we could have a much smaller exe size, which only includes the code which the game actually uses. That would be seperate feature suggestion, but the crypt feature would benefit from it also.[/quote]

The large size is because the Engine class basically depends on and registers everything, like physics, navigation etc. libraries which might not even be used. Same happens with the scripting libraries which have been hardwired to bind all engine functionality to script.

Without scripting it would be quite possible to require the user to manually register needed libraries and subsystems, in which case the Engine would not need to have to depend on them all -> unused features would not get linked. However, enabling scripting support (at least the way it's currently done) would still cause everything to be linked.

-------------------------

silverkorn | 2017-01-02 00:58:58 UTC | #13

[quote="Canardian"]Yes, but for optimal performance, you don't want to query the server each time the player opens his inventory or moves some objects. Let the background replicator handle it in a lower frequency thread.[/quote]
Indeed! 
I guess this shall be done by the programmer (or as the default behavior) because the opposite may also be desired in some other case, SQLite can put databases in memory and if you have a light table but active exigence to call data from it, may it be. :slight_smile:
We never know, the server may have strong specs used for heavy duty targeting on real-time.

-------------------------

boberfly | 2017-01-02 00:58:58 UTC | #14

Hi,

Some cryptography for things like save files would be great, so integrating it to serializer/deserializer sounds great to me. That would be the simplest practical use case I can think of for an offline standalone game so I think it is worth integrating into the mainline code as a compile option.

Cheers

-------------------------

Canardian | 2017-01-02 00:58:59 UTC | #15

It would be perhaps more efficient to use the built-in LZ4 compression to save "encrypted" local data on disk, because then it's also smaller in size.

-------------------------

silverkorn | 2017-01-02 00:58:59 UTC | #16

Can LZ4 support a key?
If people wants an additional layer of security (thin layer of varnish :slight_smile:), they can encrypt it with a static key (or possibly a dynamic key) because otherwise, using 7zip or any other compression browser on this data would reveal the whole stuff straight-forwardly since it's purpose is to shrink and not really to hide...
Just like CRC32 in the the irreversible world, it's made for data integrity and not hashing due to it's obvious result and it's great processing speed.
Same goes for MD5/SHA1 usually used for hashing due to more complicated result which change the whole result by changing a tiny value and the speed may be slower than data integrity algorithms.

-------------------------

cadaver | 2017-01-02 00:58:59 UTC | #17

LZ4 is a speed-optimized compression format that is byte-aligned, so you'll see occasional pieces of cleartext instead of bit garbage, and it doesn't support an encryption key.

-------------------------

silverkorn | 2017-01-02 01:00:51 UTC | #18

Sorry for my "laziness" with this, I invite anyone more eased with CMake and C/C++ programming skills to implement this feature.

Otherwise, if not one still interest to take this duty, I would re-orient myself into the [url=http://botan.randombit.net/]Botan[/url] library (Named "OpenCL" previously but lost track because of the more recently famous Khronos standard) because of it's better and up-to-date updates by someone eased with security and also with it's permissive 2-Clauses BSD license (without the weird publicity requirement from OpenSSL).

The reason to use it is also that it has a TLS protocol ready to use on any wanted stream such as files, network and as suggested by cadaver, on serialized/unserialized entities/nodes.

So, this is just a what I have on my mind for now... I'll try to reserve more time to add this.

-------------------------

