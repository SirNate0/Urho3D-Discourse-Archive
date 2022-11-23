Virgo | 2018-11-15 19:47:02 UTC | #1

Im trying to write my own scene editor in c++ as practice, and encountered this problem...
somebody some help plz xD

-------------------------

Virgo | 2018-11-15 19:52:51 UTC | #2

:joy:by problem i mean unable to find the corresponding function in c++ for GetObjectsByCategory

-------------------------

Modanung | 2018-11-15 20:23:50 UTC | #3

Urho has something called _tags_, could that be what you're looking for?

-------------------------

Virgo | 2018-11-15 20:31:57 UTC | #4

oops, just noticed i provided too less info, sry for that xD
what i wanted is something like this
in the editor it uses GetObjectCategories() and GetObjectsByCategory()
and i checked the api docs we do have Context::GetObjectCategories() in c++, but no GetObjectsByCategory()...
![image|535x439](upload://lns7CEEXBmEE1NFJnAUVaWf0Fjh.jpeg) ![image|690x330](upload://hr6qNr3O3sr4euQQKyta8mNtp0T.jpeg)

-------------------------

Modanung | 2018-11-15 21:01:49 UTC | #5

Then I think this method is part of the editor's code. Did you look where GetObjectsByCategory() is defined?

-------------------------

Virgo | 2018-11-15 21:03:30 UTC | #6

not found in any of the .as files came with the engine

-------------------------

Sinoid | 2018-11-15 22:37:45 UTC | #7

It's just `const HashMap<String, Vector<StringHash> >& Context::GetObjectCategories() const`

The info you really want comes from the factory table. Get the factory table, index by the hash above, and use the factory for getting the name or creating and instance.

-------------------------

Virgo | 2018-11-15 22:38:05 UTC | #8

that seems to be what i need! xD

-------------------------

