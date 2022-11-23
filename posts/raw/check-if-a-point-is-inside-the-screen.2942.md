sabotage3d | 2017-03-22 21:59:04 UTC | #1

Hi,
I am trying to check if a point is inside the screen, but I can't get it to work. I am constructing a rect that should represent the normalised screen area and I am trying to detect if the mouse position is inside this rect. My screen resolution is 1920 by 1200. Let me know if I am doing something terribly wrong.

    Rect bbox;
    Vector2 bbox_min = Vector2(0.0,0.0);
    Vector2 bbox_max = Vector2(0.9,0.9);
    bbox = Rect(bbox_min, bbox_max);

    Camera* camera = scene_->GetChild("Camera")->GetComponent<Camera>();
    Vector3 result = camera->WorldToScreenPoint(mousePosition);

    if(bbox.IsInside(Vector2(result.x_, result.y_))==INSIDE)
    	cout << "Inside" << endl;

-------------------------

1vanK | 2017-03-22 22:11:03 UTC | #2

[quote="sabotage3d, post:1, topic:2942"]
Vector3 result = camera-&gt;WorldToScreenPoint(mousePosition);
[/quote]

mouse already in screen coords

-------------------------

sabotage3d | 2017-03-23 00:14:46 UTC | #3

Sorry I didn't explain it properly. First I am transforming mousePosition to world space as I am driving some objects around. Then I am transforming back to screen space.

    Vector3 pos = camera->ScreenToWorldPoint(Vector3(mousePosition_.x_ / graphics->GetWidth(), mousePosition_.y_ / graphics->GetHeight(), 10.0f));
    //Later 
    Camera* camera = scene_->GetChild("Camera")->GetComponent<Camera>();
    Vector3 result = camera->WorldToScreenPoint(pos);

-------------------------

1vanK | 2017-03-23 05:46:58 UTC | #4

From the above code it is not clear what you want to do
```
Vector3 pos = camera->ScreenToWorldPoint(Vector3(mousePosition_.x_ / graphics->GetWidth(), mousePosition_.y_ / graphics->GetHeight(), 10.0f));
```
Why do you use a value of 10?

-------------------------

sabotage3d | 2017-03-23 15:42:12 UTC | #5

[quote="1vanK, post:4, topic:2942"]
camera-&gt;ScreenToWorldPoint(Vector3(mousePosition_.x_ /
[/quote]

This is in the particle example.
https://github.com/urho3d/Urho3D/blob/ee054a1507cb3518c57d4ebc43cfd6dc93de9a27/Source/Samples/25_Urho2DParticle/Urho2DParticle.cpp#L153

-------------------------

1vanK | 2017-03-23 18:08:49 UTC | #6

Yes, it works for orto camera only. Your app is 2D?

-------------------------

sabotage3d | 2017-03-23 18:22:19 UTC | #7

Yes it is in 2d with Ortho camera.

-------------------------

sabotage3d | 2017-03-25 19:11:11 UTC | #8

Solved my min bounds were wrong.

-------------------------

