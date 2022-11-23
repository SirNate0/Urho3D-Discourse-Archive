rogerdv | 2017-01-02 01:05:17 UTC | #1

I trying to download Urho 1.4 for windows, but cant find a working download. The links in the official page stays forever loading, only once I got the download started, and got an error: Authentication failed. Tried to use mirrorservice, but get the same error. any idea about whats happening? I even tried in a  public internet room, with broadband and cant make sourceforge start download.

-------------------------

rasteron | 2017-01-02 01:05:17 UTC | #2

Looks ok from here. Also try using download managers, like this one I use it's opensource  :wink: 

[freedownloadmanager.org/](http://www.freedownloadmanager.org/)

-------------------------

jmiller | 2017-01-02 01:05:18 UTC | #3

Buenos di?s, roger :slight_smile:

Some sourceforge downloads have been problematic for me in the past couple of days, sometimes not starting.
[jdownloader.org/](http://jdownloader.org/) - a free Java download manager that can resume.
Chromium can resume as well, but you may have to enable that in chrome://flags/

If you still have trouble, let us know specifically which version you want, and we can find a way.

-------------------------

rogerdv | 2017-01-02 01:05:19 UTC | #4

Will try using jdownloader. Im currently using downthemall, a firefox add-on.

-------------------------

rogerdv | 2017-01-02 01:05:21 UTC | #5

Negative. JDownloader cant capture the link (reports the file as offline). Tried to download the recent snapshot, but got the authentication failed error. Can project admins check if the downloads are enabled for all countries? It is not the typical Sourceforge alert that the download is blocked, but I cant think what else could be.

-------------------------

weitjong | 2017-01-02 01:05:21 UTC | #6

I am sorry to hear that. I am not sure why it happened but I would try one of these. Verify the browser setting does not prevent SF.net to redirect to its download mirror. Try to download using direct link provided by SF.net. Try to download using other mirrors that you haven't tried so far. Perhaps US mirrors instead of local ones although it would be slower probably. Try to use a CLI instead of GUI to download. I would recommend "aria2", "wget", "curl" (in that order). The first two knows how to follow "HTTP redirects" automatically, while the third has to be told by passing "-L" option.

I have also double checked the settings in the Admin page. The only check box I can think of that could limit the download for certain countries is the US "Export Control" for encryption software, but we have that check box unticked since the very beginning. Besides Cuba is friend of US already, isn't it?  :wink:

-------------------------

rasteron | 2017-01-02 01:05:22 UTC | #7

[b]@rogerdv[/b]

told you, freedownloadmanager never fails (at least for me )

[img]http://i.imgur.com/UjPd1jR.png[/img]

and as [b]weitjong[/b] mentioned, also try using the SF direct link with that. good luck.

-------------------------

rogerdv | 2017-01-02 01:05:22 UTC | #8

Changed mirror to heanet, didnt worked, then tried with wget and it is downloading now. @weitjong, the "friendship" process will still take a long time, or might even halt, because our government insists in asking without giving.

-------------------------

jmiller | 2017-01-02 01:05:23 UTC | #9

[quote="rogerdv"]Changed mirror to heanet, didnt worked, then tried with wget and it is downloading now. @weitjong, the "friendship" process will still take a long time, or might even halt, because our government insists in asking without giving.[/quote]
There has been inflexibility on other sides as well, but things change.. To friendship!

Glad you got it working

-------------------------

