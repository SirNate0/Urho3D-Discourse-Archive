cirosantilli-china | 2018-02-02 08:12:45 UTC | #1

So basically using `glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)`.



For 3D materials, there is:

```
void SetUVTransform(const Vector2& offset, float rotation, const Vector2& repeat);
```

How to do the same in 2D?

If I try `staticSprite->SetTextureRect`, it uses `GL_CLAMP_TO_EDGE` by default instead of repeating.

-------------------------

Eugene | 2018-02-02 08:59:33 UTC | #2

If you have sprite atlas with multiple textures, there is no built-in way of doing sprite repeating. Sprite is always single quad, but repeated sprite has to be more complicated. Maybe this could be changed tho, doesn't sound like hard task.

If you have just a single sprite texture, set texture address mode as "wrap" and set custom texture rectangle
https://urho3d.github.io/documentation/1.7/_materials.html

-------------------------

cirosantilli-china | 2018-02-03 09:33:44 UTC | #3

Thanks Eugene,

I had seen the wrap of Material, but how to use materials in 2D? Which method of which class is used to set the material?

E.g. I have something along:

```
        auto node = this->scene->CreateChild("Box");
        node->SetPosition2D(Vector2(this->GetWindowWidth() / 2.0f, this->GetWindowHeight() / 2.0f));
        auto box = node->CreateComponent<CollisionBox2D>();
        box->SetSize(Vector2(width, height));
        auto staticSprite = node->CreateComponent<StaticSprite2D>();
        auto boxSprite = this->resourceCache->GetResource<Sprite2D>("Urho2D/Box.png");
        boxSprite->SetRectangle(IntRect(0, 0, 100, 100));
        staticSprite->SetSprite(boxSprite);
        staticSprite->SetTextureRect(Rect(
            width / 2.0f,
            -height / 2.0f,
            -width / 2.0f,
            height / 2.0f
        ));
        staticSprite->SetUseTextureRect(true);
```

-------------------------

Eugene | 2018-02-03 10:59:29 UTC | #4

[quote="cirosantilli-china, post:3, topic:3980"]
I had seen the wrap of Material, but how to use materials in 2D? Which method of which class is used to set the material?
[/quote]

1. There's Custom Material property of the StaticSprite

2. I'm unsure, but if you set wrapping for texture, you shouldn't need any custom material at all...

-------------------------

cirosantilli-china | 2018-02-03 20:39:33 UTC | #5

I've tried to use:

```
staticSprite->SetCustomMaterial(this->resourceCache->GetResource<Material>("Materials/StoneTiled.xml"));
```

with the above code, and I removed:

```
        auto boxSprite = this->resourceCache->GetResource<Sprite2D>("Urho2D/Box.png");
```

but when I do that, I see nothing on the screen.

Do I need to do some extra setup like lights for it to work?

Runnable code: https://github.com/cirosantilli-lovechina/Urho3D-cheat/blob/0950a0c6a5cf4ff718e45bf9e62912c68d46f278/sprite_repeat.cpp

-------------------------

Eugene | 2018-02-03 20:51:01 UTC | #6

I've just tried with editor. It seems to work when _both_ material and sprite are set.

-------------------------

