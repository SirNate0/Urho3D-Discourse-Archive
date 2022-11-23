rikorin | 2017-01-02 01:08:36 UTC | #1

Solved.
Urho3d build system won't be able to invoke mklink if the dev account is also an admin with mklink privilege granted.

-------------------------

thebluefish | 2017-01-02 01:08:36 UTC | #2

Run as Administrator...

But it's just a warning. It doesn't prevent use of the library.

-------------------------

rikorin | 2017-01-02 01:08:36 UTC | #3

[quote="thebluefish"]Run as Administrator...[/quote]
Tried that, nothing changes.
[quote="thebluefish"]But it's just a warning. It doesn't prevent use of the library.[/quote]
I know, but still.

-------------------------

weitjong | 2017-01-02 01:08:37 UTC | #4

[quote="rikorin"][quote="thebluefish"]Run as Administrator...[/quote]
Tried that, nothing changes.
[quote="thebluefish"]But it's just a warning. It doesn't prevent use of the library.[/quote]
I know, but still.[/quote]

Do or do not. There is no try.

You must set your Windows account as if it is a Linux one. Ask your Windows Admin to do that for you. If you are the Admin, well, read on. Create a new account called it "root" and make it be the true administrator account. Your own dev account should be a normal account, not an administrator. Use the root account to grant your dev account to create mklink, if it does not have that privilege granted yet. From my past experience the mklink setup in our CMake scripts won't work when the dev account is also an admin with mklink privilege granted. Exactly as you have observed.

So, "do" all the above right or "don't do" anything at all. Even "Run as Administrator" work as expected in the latter case, although it is not recommended to do so.

-------------------------

rikorin | 2017-01-02 01:08:37 UTC | #5

Just as I thought the problem is me using admin account (but that's weird).
Well, I don't want to make another account, so I'll just leave it as is.

-------------------------

weitjong | 2017-01-02 01:08:37 UTC | #6

[quote="rikorin"]Just as I thought the problem is me using admin account (but that's weird).[/quote]
Yes, I couldn't understand and even stand the weirdness of Windows as well.

-------------------------

Modanung | 2017-01-02 01:08:39 UTC | #7

[quote="weitjong"]Yes, I couldn't understand and even stand the weirdness of Windows as well.[/quote]
Hear, hear

-------------------------

rikorin | 2017-01-02 01:08:39 UTC | #8

[quote="Modanung"]Hear, hear[/quote]
Oh, you're not serious, right? I'm booting in my linux installation only to test my code there. I don't like Windows at all and I wish Linux could be a good replacement, but for now it's out of question.
It's buggy, lacks tools (well, it might be fine for a hardcore programmer who uses emacs, but I'm an artist), and for me it's also much slower than Windows even when I use proprietary NVIDIA drivers (and it eats a lot of processor time for no reason too). FPS is almost two(!) times lower in Blender, for example. Also the filesystem is slower too, resizing it is a pain, and it can't properly handle folders with thousands of images. Just try to sort them and you'll see what I mean. It's also still has bug with language switching (if there is more than 2 languages), and ugly visual bug in the file manager (the background turns gray all the time). And those huge and ugly fonts, unresponsive UI...

-------------------------

weitjong | 2017-01-02 01:08:40 UTC | #9

[quote="rikorin"][quote="Modanung"]Hear, hear[/quote]
Oh, you're not serious, right? I'm booting in my linux installation only to test my code there. I don't like Windows at all and I wish Linux could be a good replacement, but for now it's out of question.
It's buggy, lacks tools (well, it might be fine for a hardcore programmer who uses emacs, but I'm an artist), and for me it's also much slower than Windows even when I use proprietary NVIDIA drivers (and it eats a lot of processor time for no reason too). FPS is almost two(!) times lower in Blender, for example. Also the filesystem is slower too, resizing it is a pain, and it can't properly handle folders with thousands of images. Just try to sort them and you'll see what I mean. It's also still has bug with language switching (if there is more than 2 languages), and ugly visual bug in the file manager (the background turns gray all the time). And those huge and ugly fonts, unresponsive UI...[/quote]
Funny that I could probably say the same things but for the other way round.  :laughing:
This is off-topic, so I suggest we don't waste energy on this. What matter is the freedom to choose what one wants to use.

-------------------------

