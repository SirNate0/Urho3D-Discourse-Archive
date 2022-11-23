Eugene | 2017-01-02 01:14:29 UTC | #1

What does it depend on?

-------------------------

cadaver | 2017-01-02 01:14:29 UTC | #2

Ultimately it depends on whether the OnSetEnabled() virtual function has been implemented. I know some subsystem-like components are missing this. For example PhysicsWorld has a slightly different situation, as it has a function called SetUpdateEnabled() which allows to set automatic per-frame physics simulating on/off. However the PhysicsWorld is never wholly "disabled" as such, but it could also be manually stepped even if SetUpdateEnabled() is false.

-------------------------

Eugene | 2017-01-02 01:14:29 UTC | #3

Understood.
How is it handled by Editor?
Some components have X button and some don't have it.
Components that don't have X button can't be enabled/disabled even through menu command.

-------------------------

cadaver | 2017-01-02 01:14:29 UTC | #4

It checks for "Is Enabled" being the first attribute.

-------------------------

