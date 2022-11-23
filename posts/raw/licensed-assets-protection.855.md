arkoz | 2017-01-02 01:03:32 UTC | #1

Hi there

I have an question about protecting all assets that will be published with the game. I know there's no 100% protection against it, but it's still required by most asset stores that i've seen.

According to an (for example) gamedfevmarket license, im not allowed to :
[quote](e) Allow the user of the Non-Monetized Media Product to extract the Licensed Asset or Derivative Works and use them outside of the Non-Monetized Media Product.[/quote]

Ive found that there was an issue on github about that, buts already closed (issue #9 on github)

Is there an another way to protect assets that will satisfy license agreements like that one above?

Thanks in advance

-------------------------

GoogleBot42 | 2017-01-02 01:03:32 UTC | #2

Maybe you could encrypt the assests somehow using a thirdparty libray...  Sure someone could still take the assets from the game but IMO it is good enough.  But I am not an attorney so take this as a grain of salt.  :slight_smile:  Does anyone know what is considered appropriate for asset protection?

-------------------------

hdunderscore | 2017-01-02 01:03:32 UTC | #3

That's pretty arbitrary, you could extract visual assets from memory using a graphics debugger.

There is the package tool that comes with Urho, although I don't believe it supports encryption at the moment.

-------------------------

thebluefish | 2017-01-02 01:03:33 UTC | #4

Basically what the quotes statement means is that you cannot release these resources yourself, or give users the rights to use these assets on their own. There is no guaranteed "minimum" encryption with it, as long as you yourself specify in your user agreement that they are not allowed to use the assets.

The funny thing about these kind of agreements is that they are almost never enforceable. Most, if not all, countries will see a custom file format as the equivalent of voodoo magic.

With that said, Urho3D already has support for packaged files. It shouldn't be too difficult to specify encryption during this process.

-------------------------

cadaver | 2017-01-02 01:03:33 UTC | #5

You can compress the package (-c switch in PackageTool), and in any case it will not be directly openable in eg. Zip or Rar programs. However an enthusiast with time on their hands will always manage to reverse-engineer & extract the package.

I would agree too that the license cannot hold you responsible for 100% foolproof technical protection, because that's not achievable considering the game needs to read the assets itself. Also consider that if you were using a closed engine without a source license, in that case you would not even have a say in how the assets get packaged.

-------------------------

arkoz | 2017-01-02 01:03:33 UTC | #6

Thanks for all replies.

turbosquid has more detailed description of that point :
[quote]b. Access to Stock Media Products. You must take all reasonable and industry standard measures to prevent other parties from gaining access to Stock Media Products. Stock Media Products must be contained in proprietary formats so that they cannot be opened or imported in a publicly available software application or framework, or extracted without reverse engineering. You may NOT publish or distribute Stock Media Products in any open format, or format encrypted with decryptable open standards (such as WebGL or an encrypted compression archive).[/quote]

I think all others comes to that interpretation.

So i need to teach PackageTool and Urho IO system to deal with the encryption.
Too bad LZ4 dosen't support that oob, also implementing that will have (some) impact on performance.

However still i don't know how to deal with the "encrypted compression archive", which in the end that's gonna look like.
At least for me but im a programmer not a lawyer.

-------------------------

cadaver | 2017-01-02 01:03:33 UTC | #7

I don't read that as "you must encrypt the data", but rather that you must not use eg. a password-protected ZIP archive. 

If you're concerned that a vanilla Urho archive can be considered an open format, then the simplest thing you can do is to add some data to the package file header and not publish the Urho modifications you made to enable that. Bam! A new proprietary format that needs reverse-engineering is born.

But note that I'm not a lawyer either :slight_smile:

-------------------------

thebluefish | 2017-01-02 01:03:35 UTC | #8

Those are some pretty general terms. Technically you could compress it as a .zip and then reverse every bit, and nobody would technically be able to read the assets without reverse-engineering.

-------------------------

GoogleBot42 | 2017-01-02 01:03:37 UTC | #9

[quote="thebluefish"]Those are some pretty general terms. Technically you could compress it as a .zip and then reverse every bit, and nobody would technically be able to read the assets without reverse-engineering.[/quote]

That is exactly what I was thinking could be done.  :laughing:

-------------------------

dds | 2017-01-02 01:04:35 UTC | #10

irrlicht lib supports  encrypt zip files load  you just def password in your Source 
there zlib license you might just use there io part of there lib
they use little lib for that but forgot what name it was


keep bin reader find password 
if password was = password7765456

string pass = "pass";

med of your code put 
pass += "word77";

some where end before you going use zip file 

pass += "65456";

sorry for my bad type skills

-------------------------

GoogleBot42 | 2017-01-02 01:04:35 UTC | #11

[quote="dds"]keep bin reader find password 
if password was = password7765456

string pass = "pass";

med of your code put 
pass += "word77";

some where end before you going use zip file 

pass += "65456";

sorry for my bad type skills[/quote]

That doesn't seem very secure to me.  I wouldn't define that as a "reasonable and industry standard measure to prevent other parties from gaining access to Stock Media Products"

Even a novice hacker could easily get the key...

-------------------------

