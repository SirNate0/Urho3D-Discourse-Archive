rogerdv | 2017-01-02 01:04:14 UTC | #1

Im using a ListView to display an scrolling list of messages, but the list keeps always the top messages, that were added first, and the newer ones are displayed only when I manually scroll the list. How can I force the ListView to always display the latest added elements?

-------------------------

cadaver | 2017-01-02 01:04:14 UTC | #2

There's no automatic or forced functionality for that, but you can set the scroll position programmatically after you add a new item. Check either SetViewPosition() or EnsureItemVisibility().

-------------------------

rogerdv | 2017-01-02 01:04:15 UTC | #3

EnsureItemVisibility is not available in AngelScript, or at least was renamed and I cant find it in the docs. There is a SetviewPosition, but the parameters are not documented in AS API and I cant find it in the C++ documentation.

-------------------------

cadaver | 2017-01-02 01:04:15 UTC | #4

As per the tradition of the AngelScript scripting API, Set / Get functions are often turned into properties. In this case too: IntVector2 viewPosition

-------------------------

