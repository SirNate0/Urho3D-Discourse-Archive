lexx | 2017-01-02 01:04:29 UTC | #1

(using urho3d from git, w7 x64)

Animation that comes with Urho3D, works right when flipping. 
But when I try to flip my own animation, crash.

[code]
	AnimatedSprite2D* animatedSprite = playerNode->GetComponent<AnimatedSprite2D>();
        if (input->GetKeyDown(KEY_LEFT))
			animatedSprite->SetFlipX(true);
[/code]

It crashes on AnimatedSprite2D.cpp at OnFlipChanged() method
[code]
void AnimatedSprite2D::OnFlipChanged()
{
    for (unsigned i = 0; i < numTracks_; ++i)
    {
        if (!trackNodes_[i])
            continue;

        StaticSprite2D* staticSprite = trackNodes_[i]->GetComponent<StaticSprite2D>();
        staticSprite->SetFlip(flipX_, flipY_);   /////<<<<<<<<<<<--------- when i==3,   staticSprite==null
    }

    // For editor paused mode
    UpdateAnimation(0.0f);
}
[/code]

Tried "key all" in Spiter, doesnt help. Dont know how I must setup my character that it works right.

Here is my stupid character+anim (you can use whatever images) in case someone wants try it out
ukko2.scml
[removed]

-------------------------

cadaver | 2017-01-02 01:04:29 UTC | #2

It seems just to be an inconsistent use of nullchecks, as there can be track nodes that don't have sprites. I've committed the missing checks, please see if that fixes the crash.

-------------------------

lexx | 2017-01-02 01:04:30 UTC | #3

Seems to work now, thanks.

-------------------------

carmanuel.zarate | 2017-01-02 01:04:30 UTC | #4

When we could have these corrections to the final release version as 1.32, because I have this same problem in the stable version 1.32

-------------------------

GoogleBot42 | 2017-01-02 01:04:31 UTC | #5

Version 1.32 is released... that version is static.  Sometime later the next version of Urho3D will be released when the devs think that it is stable enough (they have added A LOT of new features in just the last two months alone).  Be patient.  :wink:  Remember this is open source so patches don't need to be made to the current version like in most commercial software like Unity.  :slight_smile:  Just download the latest source (also called HEAD). :wink:  Urho3D doesn't really have the manpower to backport all bugfixes to the latest released version.  Generally, the latest HEAD is actually really stable.  Whenever a bug happens it is most of the time very small and is fixed within a day (much of the time within a few hours).

In other words, just use the HEAD version and report any bugs you find. :slight_smile:

-------------------------

lexx | 2017-01-02 01:04:32 UTC | #6

[quote="GoogleBot42"] Generally, the latest HEAD is actually really stable.  Whenever a bug happens it is most of the time very small and is fixed within a day (much of the time within a few hours).

In other words, just use the HEAD version and report any bugs you find. :slight_smile:[/quote]

Just that. Use git version always.

-------------------------

carmanuel.zarate | 2017-01-02 01:04:33 UTC | #7

Thank you very much for your reply, I managed to add the correction in the source code 1.32 and fix the problem.

-------------------------

GoogleBot42 | 2017-01-02 01:04:33 UTC | #8

[quote="carmanuel.zarate"]Thank you very much for your reply, I managed to add the correction in the source code 1.32 and fix the problem.[/quote]

Why do you stick with 1.32?  It is ancient in terms of features and bug fixes...  :neutral_face:   So much has changed since its release...

-------------------------

thebluefish | 2017-01-02 01:04:34 UTC | #9

[quote="GoogleBot42"]
Why do you stick with 1.32?  It is ancient in terms of features and bug fixes...  :neutral_face:   So much has changed since its release...[/quote]

1.32 is a stable release. For people who aren't looking for the latest-and-greatest-and-could-be-a-bit-broken-somehow, it's a good place to be at until the next release comes out.

-------------------------

lexx | 2017-01-02 01:05:01 UTC | #10

I updated urho3d from git (havent done it awhile), same crash again (seems that checks are missing again).

-------------------------

cadaver | 2017-01-02 01:05:02 UTC | #11

Aster removed the check. It will be pushed again soon.

-------------------------

rku | 2017-01-02 01:05:02 UTC | #12

I patched few crashes myself. In case its of any use:
[code]From 0a02a565d07653ad33e67225bc4342d181131ea6 Mon Sep 17 00:00:00 2001
From: rku <rku@sysret.net>
Date: Tue, 5 May 2015 18:25:24 +0300
Subject: [PATCH] Few null checks in AnimatedSprite2D

---
 Source/Urho3D/Urho2D/AnimatedSprite2D.cpp | 5 ++++-
 1 file changed, 4 insertions(+), 1 deletion(-)

diff --git a/Source/Urho3D/Urho2D/AnimatedSprite2D.cpp b/Source/Urho3D/Urho2D/AnimatedSprite2D.cpp
index aa492f7..4592f35 100644
--- a/Source/Urho3D/Urho2D/AnimatedSprite2D.cpp
+++ b/Source/Urho3D/Urho2D/AnimatedSprite2D.cpp
@@ -242,7 +242,8 @@ void AnimatedSprite2D::OnFlipChanged()
             continue;
 
         StaticSprite2D* staticSprite = trackNodes_[i]->GetComponent<StaticSprite2D>();
-        staticSprite->SetFlip(flipX_, flipY_);
+        if (staticSprite)
+            staticSprite->SetFlip(flipX_, flipY_);
     }
 
     // For editor paused mode
@@ -417,6 +418,8 @@ void AnimatedSprite2D::UpdateAnimation(float timeStep)
     for (unsigned i = 0; i < numTracks_; ++i)
     {
         Node* node = trackNodes_[i];
+        if (!node)
+            continue;
         TrackNodeInfo& nodeInfo = trackNodeInfos_[i];
 
         if (!nodeInfo.value.enabled_)
-- 
1.9.1[/code]

-------------------------

cadaver | 2017-01-02 01:05:02 UTC | #13

Thanks, didn't notice that UpdateAnimation possible null access.

-------------------------

