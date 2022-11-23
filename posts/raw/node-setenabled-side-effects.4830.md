Leith | 2019-01-17 09:19:02 UTC | #1

If a node is disabled, and therefore its components are disabled, can I assume that A) their components will NOT receive events that they have subscribed to, and B) that they WILL nonetheless be serialized to disk as part of the owner scene?
And is there a way for Nodes/Components to Opt Out of Scene Serialization, without being removed from the scene?

-------------------------

Leith | 2019-01-17 12:00:06 UTC | #2

This question was answered in another thread - yes, events will not be sent, yes, disabled stuff is serialized, and yes, nodes and components can opt out of it. I don't have the link in front of me, but yes.

Thank you all for your patience.

-------------------------

Leith | 2019-01-19 06:03:34 UTC | #3

Apparently, I am not done yet.
Children of a disabled node are still rendered. Why?
Should I really disable the entire child tree? Why?

If a node is disabled, why are its children being visited?
How does this relate to batching?

-------------------------

