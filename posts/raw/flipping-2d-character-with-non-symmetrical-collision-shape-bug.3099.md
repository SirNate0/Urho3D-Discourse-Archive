ricab | 2017-05-03 20:33:00 UTC | #1

Hello,

In 2D, what approach would you suggest to flip a character whose collision shape is not symmetrical? 

`SetFlip` only applies to sprites, but other components may need to reflect the flip (e.g. non-centered trail particles). 

Therefore, I am trying to go with a negative scale of the character's node: `node->Scale2D(Vector2{1.f,-1.f});`. However, the collision shape does not seem to see the scale at all! It stays just the same... Is this somehow to be expected for some reason I am missing?

It looks like a _bug_ to me, so I opened [#1926](https://github.com/urho3d/Urho3D/issues/1926). I am on a linux/gcc config here. Can anyone confirm they see the same? To reproduce, just add the following to `Urho2DConstraints::HandleUpdate` (sample 32) before running it and pressing <kbd>F</kdb>

```
  if(input->GetKeyPress(KEY_F))
      scene_->GetChild("Polygon")->Scale2D(Vector2{1,-1});
```

-------------------------

