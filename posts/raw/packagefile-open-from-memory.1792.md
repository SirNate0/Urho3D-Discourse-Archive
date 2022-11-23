Enhex | 2017-01-02 01:10:11 UTC | #1

If someone wants to encrypt and decrypt a package file, the package file needs to be able to be loaded from memory, so there's no need to save the decrypted version to a file first.

VectorBuffer could be used:
Open a file, use VectorBuffer::SetData(Deserializer&) to read it into a VectorBuffer, use VectorBuffer::GetModifiableData() to work on the VectorBuffer, and use the VectorBuffer to open a package from memory.

Protecting assets is required by the license of some asset sellers.

-------------------------

thebluefish | 2017-01-02 01:10:11 UTC | #2

While I agree that we should have a way to open PackageFile from memory, I do want to point out that this method of encryption would likely kill performance. Decrypting the entire package for a single file within could cause longer-than-normal load times -or- a larger memory footprint. Might I suggest performing the encryption on the individual files within Package? You could create a Resource called EncryptedResource, that that would facilitate the decryption. Then the EncryptedResource files would be loaded from within the Package, decrypted, and then converted to the desired Resource.

-------------------------

Enhex | 2017-01-02 01:10:11 UTC | #3

Yes, there's a performance sacrifice, but decrypting a single package file should be faster than many files, especially if it's compressed since what matters the most is how many bytes you decrypt, and opening many files is slower than a single file.

A better solution when using a package file is to just encrypt the header and/or the first file, so you have to decrypt them to be able to open the package. That would be the fastest option.

Also having to maintain a single protected package file is much easier and less error prone than having to maintain many protected files which may be mixed with non-protected files.

-------------------------

Lumak | 2017-01-02 01:10:12 UTC | #4

This might help - [url]http://urho3d.prophpbb.com/topic1873.html[/url]

-------------------------

Enhex | 2017-01-02 01:10:12 UTC | #5

[quote="Lumak"]This might help - [url]http://urho3d.prophpbb.com/topic1873.html[/url][/quote]
One of the problems I want to avoid is forking from Urho's source, so I don't have to deal with maintenance.
Your solution forks the PackageFile class, so if there are any changes to it you'll have to refactor it.

Having API for opening the PackageFile from memory doesn't require forking the class because you'll be doing everything externally, so it avoids any maintenance problems.

-------------------------

Lumak | 2017-01-02 01:10:12 UTC | #6

[quote="Enhex"]
One of the problems I want to avoid is forking from Urho's source, so I don't have to deal with maintenance.
Your solution forks the PackageFile class, so if there are any changes to it you'll have to refactor it.

Having API for opening the PackageFile from memory doesn't require forking the class because you'll be doing everything externally, so it avoids any maintenance problems.[/quote]

I don't fork the PackageFile class, rather, inherit from it.  The only difference is how you open the file, and I'm not sure how much of that will change.  The rest of how the PackageFile class functions hasn't been altered. I don't know if you see that or not.
The method that I provided is one easy solution to protect your assets.  But I'm sure there are other ways.

-------------------------

Enhex | 2017-01-02 01:10:12 UTC | #7

By fork I mean creating a new version which is detached from the source.

you fork the Open() function.
If in the future PackageFile::Open() changes, your fork probably will no longer be compatible and you'll have to refactor in the changes.
That means you have to constantly keep an eye out for any changes happening to PackageFile, or get notified to such changes when something breaks.

-------------------------

cadaver | 2017-01-02 01:10:13 UTC | #8

Right now the support code for PackageFile operation in the File class is badly coded. It will need a refactor so that PackageFile will only hand out Deserializers, and File only concerns itself with abstracting access (read/write/seek) to a filesystem file. This will cascade to other places which do dynamic cast to File*, this will need to be refactored and instead everything necessary should be in Deserializer. So it isn't a trivial operation on the whole.

In the end I believe PackageFile should robustly support subclassing for things like loading from memory or encryption/decryption. It has done its task for a long time with little changes, so I don't think that after those changes (if made successfully) breakage needs to be realistically feared.

-------------------------

