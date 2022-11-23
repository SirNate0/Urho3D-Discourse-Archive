Enhex | 2017-01-02 01:08:02 UTC | #1

After the AngelScript version update protected property is available.
Urho's editor hides private properties but not protected properties.

It should also hide protected properties since they're not public, they're just like private but allowing derived classes to access them.
It will be very helpful to make sure the editor doesn't give the user access to edit properties it shouldn't have access to, both to prevent data corruption and to only keep relevant properties listed in the editor.

-------------------------

Enhex | 2017-01-02 01:08:03 UTC | #2

[quote="Sinoid"]
That's not accurate. With the version update private is now truly private, and protected replaces the previous private behavior. Previously private was the equivalent (mostly) of protected in other languages.[/quote]


Didn't know that private functioned as protected before, thanks.

-------------------------

