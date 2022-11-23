Sir_Nate | 2017-01-02 01:13:45 UTC | #1

I intend to use TOML for some config/resource files for my game. Would there be any interest in TOML scene saving and loading, or do you think XML and JSON are enough?

-------------------------

rku | 2017-01-02 01:13:46 UTC | #2

There is nothing json can not do. Toml seems to be a very niche language and inferior to yaml. For things i have to edit manually i would prefer yaml because it is VERY readable.. For things i do not have to edit manually serialization method is completely irrelevant to me. Toml does not seem that readable.

-------------------------

TheSHEEEP | 2017-01-02 01:13:46 UTC | #3

I support the notion that YAML already is very human readable and editable and at least has some support around different libraries.

TOML also seems nice and readable, but to be honest, that is IMO one of those projects that there just isn't any real need to, except the author's desire to create it.
Like how time and time again new build and packing scripts keep popping up (automake, ninja, some python ones, some Lua ones, ...) while there already are good ones around, that should be used and improved instead of reinventing the wheel for the umpteenth time :wink:

-------------------------

Sir_Nate | 2017-01-02 01:13:47 UTC | #4

Reasonable enough. i'll probably still use it for my project (as an improved INI is pretty much exactly what I was looking for, I prefer equal signs to colons, and I don't foresee needing any of the features YAML offers that TOML does not), but I'll not do serialization other than that.

-------------------------

