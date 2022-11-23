Enhex | 2017-01-02 01:09:49 UTC | #1

3D model stores usually offer great value-for-price if you find what you need.
The problem is that almost all of them have a license that require that the product must be incorporated product.
The definition of incorporated product on cg-trader's license is:
[quote]7. Incorporated Product ? Product that cannot be extracted from an application or other product and used as stand-alone object without the use of reverse engineering tools or techniques. For avoidance of doubt, Incorporated Product is such use of a Product that does not allow further distribution of the Product outside of the application or product containing the Incorporated Product.

...

21.3. If you use any Product in software products (such as video games, simulations, or VR-worlds) you must take all reasonable measures to prevent the end user from gaining access to the Product. Methods of safeguarding the Product include but are not limited to:

- using a proprietary disc format such as Xbox 360, Playstation 3, etc.;

- using a proprietary Product format;

- using a proprietary and/or password protected database or resource file that stores the Product data;

- encrypting the Product data.[/quote]

I don't think messing with formats is a good idea, so just password protecting and encryption should be good enough.
Considering Urho3D already has PackageFile, which can be loaded. Just adding password/encryption feature to it solves this problem.
Urho's editor should be able to access protected PackageFile's too.

Is it possible to load a PackageFile from memory?

-------------------------

cadaver | 2017-01-02 01:09:49 UTC | #2

This has been discussed before.

Out of the box, it can be argued that Urho already offers a proprietary container (the PackageFile). To scramble the data, it can be LZ4 compressed on creation. Though me saying this doesn't constitute legal advice so any risk you take is your own.

You are welcome to work on and contribute password protection or encryption. Though I would be somewhat wary of including anything like it to the base Urho sources because it requires cryptography expertise (which I don't have especially, so I couldn't really comment reliably on the quality of an implementation) and a bad implementation could offer a false sense of security.

For a quick & dirty solution you could just implement some additional scrambling to the PackageFile creation & reading in a custom build.

-------------------------

Enhex | 2017-01-02 01:09:49 UTC | #3

PackageFile is open format so it doesn't count as [url=https://en.wikipedia.org/wiki/Proprietary_format]proprietary format[/url].

Considering the PackageFile requires some degree of reverse engineering since the assets in the package can't just be loaded into a 3D tool or extracted, and even more so with compression, so that might be enough.
I just asked CGTrader support and they verified it's good enough.

-------------------------

thebluefish | 2017-01-02 01:09:49 UTC | #4

[quote="Enhex"]I just asked CGTrader support and they verified it's good enough.[/quote]

Thanks for getting this clarified.

I think we should offer some form of password protection. Whether it's "strong" protection or not really doesn't matter, hackers are going to get it either way. Just as long as it's actually encrypted, ie not the kind of "password protection" that ZIP or PST files would use.

-------------------------

Mike | 2017-01-02 01:09:49 UTC | #5

I've seen [url=https://github.com/lqez/npk]this libray[/url] integrated in a game engine (it is MIT licensed). It provides package and xxtea encryption.

-------------------------

Enhex | 2017-01-02 01:09:51 UTC | #6

I did look into Crypto++, it seems a bit complicated because you have to be familiar with how encryption works and the algorithms, but as far as I'm concerned the main thing to care about is performance.
The library has implementations of many algorithms, and provides benchmarks: [cryptopp.com/benchmarks.html](https://www.cryptopp.com/benchmarks.html)

If we add to PackageFile a function to open a package from memory instead of file, the file can be first loaded into memory and decrypted, letting the user do it by himself.

Though I'm not sure how to pass encrypted packages via command line and have them decrypted. This is improtant so for example Urho's editor could use encrypted packaged resources.
A simple solution would be to have a single global key for decrypting all packages. While sufficient for complying with asset protection requirement and most cases, it's inflexible.

Another option is just to offset the real beginning of the file, and then you essentially creating a proprietary format. PackageFile already has startOffset parameter.
Still will require some way to communicate the offset via command line and with the editor.

-------------------------

thebluefish | 2017-01-02 01:09:51 UTC | #7

Ideally, with the editor, you would work with unprotected asset packs or folders. Though a keyfile or passphrase should be sufficient to allow the editor access to the assets.

-------------------------

abcjjy | 2017-01-02 01:12:37 UTC | #8

Try this [github.com/nmoinvaz/minizip](https://github.com/nmoinvaz/minizip).

I've tried it in other project. It provides aes256 encryption. And it is a zlib extension. Although the api looks strange at first, it fits your needs perfectly.

-------------------------

