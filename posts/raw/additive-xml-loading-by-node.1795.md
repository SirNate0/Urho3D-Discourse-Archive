Bluemoon | 2017-01-02 01:10:12 UTC | #1

The LoadXML method of Scene and Node first wipes off every component and child node before loading. Having a method that loads from XML but instead adds to the already existing components and child nodes will really be helpful.
I would like to know the general opinion on this just to be sure I'm not the only one yearning for it  :laughing:

-------------------------

cadaver | 2017-01-02 01:10:13 UTC | #2

You should already be able to do additive loading by the Instantiate family of functions. Though the option for e.g. Scene::Load to not clear the existing content should not be hard to add. Just need to check how it will handle e.g. ID conflicts.

-------------------------

TheComet | 2017-01-02 01:10:17 UTC | #3

[quote="cadaver"]You should already be able to do additive loading by the Instantiate family of functions. Though the option for e.g. Scene::Load to not clear the existing content should not be hard to add. Just need to check how it will handle e.g. ID conflicts.[/quote]

The most sane thing to do IMO would be to just refuse to create that particular component and write an error to the log. It should be the programmer's responsibility to make sure there are no conflicts.

-------------------------

cadaver | 2017-01-02 01:10:18 UTC | #4

Probably the loading code would already just assign another ID. This is something a scene author does not have good control over, since e.g. in the editor when you click "New replicated node" the next free ID is used, but the editor has no way of knowing you have the intention of merging multiple separately authored scenes.

-------------------------

TheComet | 2017-01-02 01:10:18 UTC | #5

Ah, in that case I agree.

-------------------------

