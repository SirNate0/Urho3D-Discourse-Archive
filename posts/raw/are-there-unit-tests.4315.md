TheComet | 2018-06-13 23:04:43 UTC | #1

Does Urho3D have anything that resembles unit testing? I'm doing some work with IK and keeping trees synchronized and it would help if I were able to make sure I'm dirtying the solver properly for all possible scene changes.

-------------------------

weitjong | 2018-06-14 00:45:11 UTC | #2

Not at the moment. For testing the solver or anything that is non-graphical, I can see the value of having unit test in place.

-------------------------

LordGolias | 2018-06-24 07:06:04 UTC | #3

I second this. In my experience in Open Source, this is actually a great way of building trust in the code without rellying on extremely knowledgable people about the code to review every PR: if it breaks tests, there must be a very good reason to do so (and change the test).

Some things that would need to be done:

1. Decide on a testing framework to do it (e.g. [google tests](https://github.com/google/googletest))
2. Implement the barebones of unit testing (directories, Cmake)
3. Integrate Unit testing to CI/Travis

-------------------------

