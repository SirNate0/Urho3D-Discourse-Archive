setzer22 | 2017-01-02 01:03:24 UTC | #1

Hello all!

When using the editor and importing an animated model with its skeleton (Jack itself does this). A node is created for each of its skeleton bones and added to the hierarchy. While this is perfectly fine, even the most simple skeletons completely destroy the hierarchy view making it mostly unnavigable (too many nodes).

Is there a good way to collapse those by default? I'm aware I can collapse all nodes using the "Collapse" button with the "All" option marked, but that really collapses all nodes and I'm not interested in that. Maybe collapse everything but the first level? Is that possible with the editor right now? 

Of course this can be done manually, this is what I've been doing until now. But it gets tiring when you've got a lot of models on the scene.

BONUS QUESTION: The editor displays components and nodes in the order they're stored in the XML file and adds new ones at the bottom. Can I change that order through the editor's GUI? I can't seem to find how...

Thank you :smiley:

-------------------------

hdunderscore | 2017-01-02 01:03:37 UTC | #2

Collapsing in editor is an untamed beast at the moment.

I have been looking at node re-ordering in the editor hierarchy and almost have that ready. I didn't even think about component re-ordering :astonished:

-------------------------

setzer22 | 2017-01-02 01:03:38 UTC | #3

I know it's ugly but I kind of rely on component reordering to make sure some components are loaded before others. Same thing for objects. The feature becomes quite handy in that situation. Good to know it's almost ready :smiley:

As for auto-collapsing, a quick workaround I'm using is collapse all nodes manually every time I start the editor: Select scene rooot -> Hit all checkbox -> Hit collapse button. Even though some control over that (maybe with XML metadata?) would be awesome!

-------------------------

