OvermindDL1 | 2017-01-02 01:10:55 UTC | #1

So, a screenshot of the programmer-art test project:
[img]http://overminddl1.com/screenshots/tmp/Urho2D-Borked.png[/img]
This is using the SpriteSheet2D, but it would happen with any kind of Sprite that is using non-full texture.  Apparently whoever designed the Urho2D system locks all UV coordinate to integers, which are then multiplied with 0.0999999... (0.1 not represented accurately due to floating point), which then causes issues with the side pixels leaking since they never actually shifted the inward a little to compensate for the floating point inaccuracy.  This combined with the fact that Urho2D does nonsensical precision losing things like:
[code]
    float invWidth = 1.0f / (float)texture_->GetWidth();
    float invHeight = 1.0f / (float)texture_->GetHeight();

    rect.min_.x_ = rectangle_.left_ * invWidth;
    rect.max_.x_ = rectangle_.right_ * invWidth;

    rect.min_.y_ = rectangle_.bottom_ * invHeight;
    rect.max_.y_ = rectangle_.top_ * invHeight;
[/code]
Causes it to slowly hemorrhage accuracy as far as I can tell.

So, first question, why is this bound to integers instead of floating for UV's, and why is it scaling UV's one way, then the other, losing accuracy?  And why oh why does PIXEL_SIZE exist?!

The test image files are:
[url=http://overminddl1.com/screenshots/tmp/Testing.png]Image[/url]
[url=http://overminddl1.com/screenshots/tmp/Testing.json]Image-spritesheet-json[/url]
[url=http://overminddl1.com/screenshots/tmp/Testing.xml]Image-xml[/url]

Of course no such issue if I render my own verts, but I would prefer not to rewrite Urho2D to fix what seems like a major design flaw if someone can explain how you are supposed to work around these integer rounding bugs to begin with?

-------------------------

1vanK | 2017-01-02 01:10:55 UTC | #2

[code]<texture>
    <address coord="u" mode="clamp" />
    <address coord="v" mode="clamp" />
<texture>[/code]

-------------------------

1vanK | 2017-01-02 01:10:55 UTC | #3

[quote="OvermindDL1"]And why oh why does PIXEL_SIZE exist?!
[/quote]

[github.com/urho3d/Urho3D/pull/1209](https://github.com/urho3d/Urho3D/pull/1209)

-------------------------

OvermindDL1 | 2017-01-02 01:10:57 UTC | #4

[quote="1vanK"][code]<texture>
    <address coord="u" mode="clamp" />
    <address coord="v" mode="clamp" />
<texture>[/code][/quote]
Nope, no change, and that should only affect what happens on image edges, and as this is a spritesheet then it is not getting to those edges anyway since I am using a tiny part of the sheet.  I was able to fix it by massaging Sprite2d.cpp's GetTextureRectangle function output (shifting UV's tiny-bit inwards), but that only works for my sizes and would not work generically.  Need to overhaul Urho2D to get rid of that friggin PIXEL_SIZE and have UV's use 0.0-1.0 floats instead of integers that lose precision.  Why was that style picked anyway?  It will not scale as I allow different texture sizes to override things, the very design of Urho2D taking integer UV's makes no sense..

-------------------------

OvermindDL1 | 2017-01-02 01:10:57 UTC | #5

Specifically this is what I did:

Replace in file Sprite2D.cpp starting at line 172 from this:
[code]
    rect.min_.x_ = rectangle_.left_ * invWidth;
    rect.max_.x_ = rectangle_.right_ * invWidth;

    rect.min_.y_ = rectangle_.bottom_ * invHeight;
    rect.max_.y_ = rectangle_.top_ * invHeight;
[/code]
To become this:
[code]
    rect.min_.x_ = rectangle_.left_ * invWidth + 0.0001;
    rect.max_.x_ = rectangle_.right_ * invWidth - 0.0001;

    rect.min_.y_ = rectangle_.bottom_ * invHeight + 0.0001;
    rect.max_.y_ = rectangle_.top_ * invHeight - 0.0001;
[/code]
Although not generic or properly done, it does fix the spritesheet rendering issues in 99% of cases (which is more than what the spritesheet supports now), and would consequently fix sprites so that the CLAMP mode being force-set in code is likely not necessary anymore.

I would be amenable to that being put in master as it does resolve a few issues (though still not done 'properly', though the proper way involves getting rid of the integer UV addressing and go back to floats, even if it is scaled to pixels).  Only case I see it failing is if they have, say, a 2048x2048 texture and are showing an individual pixel or so as a sprite...

If that is added to master then the lines of 109 in Sprite2D.cpp of:
[code]
    // Ensure the texture doesn't have wrap addressing as that will cause bleeding bugs on the edges.
    // Could also choose border mode, but in that case a universally good border color (without alpha bugs)
    // would be hard to choose. Ideal is for the user to configure the texture parameters in its parameter
    // XML file.
    if (texture_->GetAddressMode(COORD_U) == ADDRESS_WRAP)
    {
        texture_->SetAddressMode(COORD_U, ADDRESS_CLAMP);
        texture_->SetAddressMode(COORD_V, ADDRESS_CLAMP);
    }
[/code]
Could likely be removed then as bleeding edge bugs should not occur anymore (test though on this part, I can foresee a few cases they can still happen, but it 'should' be safe).

-------------------------

OvermindDL1 | 2017-01-02 01:10:57 UTC | #6

[quote="OvermindDL1"]Specifically this is what I did:

Replace in file Sprite2D.cpp starting at line 172 from this:
[code]
    rect.min_.x_ = rectangle_.left_ * invWidth;
    rect.max_.x_ = rectangle_.right_ * invWidth;

    rect.min_.y_ = rectangle_.bottom_ * invHeight;
    rect.max_.y_ = rectangle_.top_ * invHeight;
[/code]
To become this:
[code]
    rect.min_.x_ = rectangle_.left_ * invWidth + 0.0001;
    rect.max_.x_ = rectangle_.right_ * invWidth - 0.0001;

    rect.min_.y_ = rectangle_.bottom_ * invHeight + 0.0001;
    rect.max_.y_ = rectangle_.top_ * invHeight - 0.0001;
[/code]
Although not generic or properly done, it does fix the spritesheet rendering issues in 99% of cases (which is more than what the spritesheet supports now), and would consequently fix sprites so that the CLAMP mode being force-set in code is likely not necessary anymore.

I would be amenable to that being put in master as it does resolve a few issues (though still not done 'properly', though the proper way involves getting rid of the integer UV addressing and go back to floats, even if it is scaled to pixels).  Only case I see it failing is if they have, say, a 2048x2048 texture and are showing an individual pixel or so as a sprite...

If that is added to master then the lines of 109 in Sprite2D.cpp of:
[code]
    // Ensure the texture doesn't have wrap addressing as that will cause bleeding bugs on the edges.
    // Could also choose border mode, but in that case a universally good border color (without alpha bugs)
    // would be hard to choose. Ideal is for the user to configure the texture parameters in its parameter
    // XML file.
    if (texture_->GetAddressMode(COORD_U) == ADDRESS_WRAP)
    {
        texture_->SetAddressMode(COORD_U, ADDRESS_CLAMP);
        texture_->SetAddressMode(COORD_V, ADDRESS_CLAMP);
    }
[/code]
Could likely be removed then as bleeding edge bugs should not occur anymore (test though on this part, I can foresee a few cases they can still happen, but it 'should' be safe).[/quote]


EDIT0:  Actually, let me wrap that magic number up in a member variable, add getters/setters, and I'll submit a PR, gimme a few minutes to do that and test it.

EDIT1:  Done:  [github.com/urho3d/Urho3D/pull/1239](https://github.com/urho3d/Urho3D/pull/1239)

-------------------------

