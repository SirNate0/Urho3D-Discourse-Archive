mmikkola | 2017-01-02 01:08:41 UTC | #1

I wanted to hide a node and display it after some time, so I created the following animation to test:

[code]
SharedPtr<ValueAnimation> enabledAnim(new ValueAnimation(context_);
enabledAnim->SetKeyFrame(0.0f, false);
enabledAnim->SetKeyFrame(3.0f, true);
enabledAnim->SetKeyFrame(4.0f, false);

node->SetAttributeAnimation("Is Enabled", enabledAnim);
[/code]

Which works great on Windows, but on Linux the node never shows.
I tried working outside the animation system and just used SetEnabled on the node at set intervals in the Update handler, but no luck there either.

Couldn't find a similiar post or a relevant github issue.

This is running 1.5 on a VirtualBox VM with Debian 7.9.

-------------------------

cadaver | 2017-01-02 01:08:42 UTC | #2

Was not able to reproduce (used AngelScript instead of C++, though) on Ubuntu 14 64bit build.

-------------------------

mmikkola | 2017-01-02 01:08:46 UTC | #3

Tried it on debian 7.9 install on a intel nuc computer, same result.
I'm gonna check if it's reproducable with angelscript on debian.

-------------------------

cadaver | 2017-01-02 01:08:46 UTC | #4

In case it's specific to the platform in a way that is not reproducible on usual systems be prepared to do your own debugging to find the cause, then report back your findings so that the bug can be fixed.

-------------------------

