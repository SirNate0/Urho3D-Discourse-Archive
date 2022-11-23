weitjong | 2017-01-02 00:57:40 UTC | #1

Dear site admins,

Is it possible to adjust the Forum scripts to better utilize the available space? The "topic" texts in the last column of "Board index" page are truncated although there are still plenty of space in the column.

Thanks in advance.

-------------------------

cin | 2017-01-02 00:57:40 UTC | #2

We cannot acces to source code of the forum templates. I think what need to write to support forum - [support.prophpbb.com](http://support.prophpbb.com).

-------------------------

weitjong | 2017-01-02 00:57:40 UTC | #3

I suppose they do that on purpose in order to get their premium customer  :wink: . The link you provided shows that their board index also has this truncation issue although it is not as glaring as ours because their last column is not dynamically stretched to fill the screen. Never mind then. Thanks again for the quick reply.

-------------------------

friesencr | 2017-01-02 00:57:40 UTC | #4

I wrote a dotjs hack to fix this problem.

[gist.github.com/friesencr/8662365](https://gist.github.com/friesencr/8662365)
[gist]https://gist.github.com/friesencr/8662365[/gist]

If you have never used dotjs before it allows you to run arbitrary js when a domain matches a filename inside your ~/.js folder
So save that gist as urho3d.prophpbb.com.js and plop it in your .js folder.

For chrome:  This chrome extension uses the addon directory.  You can find it in the options of the addon.
[bit.ly/dotjs-win](http://bit.ly/dotjs-win)

For firefox:
[addons.mozilla.org/en-US/firefox/addon/dotjs/](https://addons.mozilla.org/en-US/firefox/addon/dotjs/)

-------------------------

weitjong | 2017-01-02 00:57:40 UTC | #5

Thanks for that. I use GreaseMonkey on Firefox but will check this one out.

-------------------------

cin | 2017-01-02 00:57:40 UTC | #6

[b]friesencr[/b], I inject your code into footer. Now it work everywhere. Thanks.

-------------------------

carlomaker | 2017-01-02 00:57:40 UTC | #7

[quote="friesencr"]I wrote a dotjs hack to fix this problem.

[gist.github.com/friesencr/8662365](https://gist.github.com/friesencr/8662365)
[gist]https://gist.github.com/friesencr/8662365[/gist]

If you have never used dotjs before it allows you to run arbitrary js when a domain matches a filename inside your ~/.js folder
So save that gist as urho3d.prophpbb.com.js and plop it in your .js folder.

For chrome:  This chrome extension uses the addon directory.  You can find it in the options of the addon.
[bit.ly/dotjs-win](http://bit.ly/dotjs-win)

For firefox:
[addons.mozilla.org/en-US/firefox/addon/dotjs/](https://addons.mozilla.org/en-US/firefox/addon/dotjs/)[/quote]
thanks [b]friesencr[/b]
[quote="cin"][b]friesencr[/b], I inject your code into footer. Now it work everywhere. Thanks.[/quote]
thanks for update

-------------------------

weitjong | 2017-01-02 00:57:40 UTC | #8

Super!! Thank you all.

Since all you are here, is it possible to add a button to mark the topic as solved rather than clicking on Edit button & typing in manually in the subject of the first post? Being a die-hard Perl user, my PHP script-fu is next to zero  :wink: .

-------------------------

carlomaker | 2017-01-02 00:57:41 UTC | #9

[quote="weitjong"]Super!! Thank you all.

Since all you are here, is it possible to add a button to mark the topic as solved rather than clicking on Edit button & typing in manually in the subject of the first post? Being a die-hard Perl user, my PHP script-fu is next to zero  :wink: .[/quote]
i hope i am wrong , but it seems to be only through [url=https://www.phpbb.com/community/viewtopic.php?t=1214795]mod[/url], which is not possible on prophpbb.

-------------------------

