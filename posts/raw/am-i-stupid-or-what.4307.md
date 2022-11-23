slapin | 2018-06-11 12:20:09 UTC | #1

Hi all!

It looks like I become lazy and stupid. The concept of global to local and backwards
tends to be overwhelming to me at times.
So while I was working on character appearance editor
I use approach which looks simpler - change bones so that overall character appearance changes.
This works OKish, but has obvious problems.
I implemented this class which is at core of things:

https://gist.github.com/6cfbfe4852cc2d9809f0b5ff7c9dcb36

When changing bone we need to counter-change child bones if we don't want them changed.
For example, we change nech width but do not want to change head width at the same time, so we need
to have head width back.

Manually changing that is really not nice, not nice at all. That is too much. So I implemented the following code (see gist above for context):

```c++
                void SetSliderValue(float value)
 		{
			slider_cur = value;
			/* Save original transforms for bones we want to keep sizes */
			for (int i = 0; i < preserve.Size(); i++) {
				preserve[i].orig_scale = preserve[i].node->GetWorldScale();
				preserve[i].orig_pos = modifiers[i].node->GetWorldPosition();
				preserve[i].orig_rot = modifiers[i].node->GetWorldRotation();
			}
			for (int i = 0; i < modifiers.Size(); i++) {
				Urho3D::Vector3 orig_scale = modifiers[i].node->GetScale();
				Urho3D::Vector3 orig_pos = modifiers[i].node->GetPosition();
				modifiers[i].node->SetScale(orig_scale + modifiers[i].scale * value);
				modifiers[i].node->SetPosition(orig_pos + modifiers[i].translation * value);
			}
			/* Restore original transforms for bones we want to keep sizes */
			for (int i = 0; i < preserve.Size(); i++) {
				if (preserve[i].flags & SCALE)
					preserve[i].node->SetWorldScale(preserve[i].orig_scale);
				if (preserve[i].flags & TRANS)
					preserve[i].node->SetWorldPosition(preserve[i].orig_pos);
				if (preserve[i].flags & ROT)
					preserve[i].node->SetWorldRotation(preserve[i].orig_rot);
			}
}
```

So here we save global transform, then do our slider work then restore global transform (of bones we do not want to change by this slider)

I thought it should work like this, but it looks like it won't. If I hardcode values of stored transform, it works fine, which makes me think that idea is not entirely stupid, but something is not right. Any ideas?

-------------------------

