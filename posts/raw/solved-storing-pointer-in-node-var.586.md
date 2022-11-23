Bluemoon | 2017-01-02 01:01:32 UTC | #1

Does anyone know how to safely store and retrieve a pointer stored in Node Var, I tried it didn't work out well. First I set the node var

[code]
Sprite* sprt = ... ;
myNode->SetVar("Sprite", sprt);
[/code]

then I tried to retrieve it like this 

[code]
Sprite* mySprite = static_cast<Sprite*>(myNode->GetVar("Sprite")->GetPtr();
[/code]

but it throws up some ugly compiler error.

I would be glad if anyone that has gotten this kind of stuff right can show me the way forward :slight_smile:

-------------------------

Stinkfist | 2017-01-02 01:01:32 UTC | #2

You're missing one ")" at least before ";". Is it simply that?

Edit: Also, for future reference, please post the compiler output too for any possible compilation problems.

-------------------------

Bluemoon | 2017-01-02 01:01:32 UTC | #3

[quote="Stinkfist"]You're missing one ")" at least before ";". Is it simply that?

Edit: Also, for future reference, please post the compiler output too for any possible compilation problems.[/quote]

the missing bracket was actually a typo made while posting... But thanks anyway was able to figure out what went wrong and it turned out my code was not at fault :slight_smile:

-------------------------

