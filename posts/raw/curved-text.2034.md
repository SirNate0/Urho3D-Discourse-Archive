Victor | 2017-01-02 01:12:26 UTC | #1

I was wondering if there was a good way to draw text along a curve with the Text3D component? It seems like it would be ideal to use the text_ (and using the uiVertexData positions), private member variable to achieve this however there's currently no possible way to access that variable outside of the class. Perhaps there's another way? Using Text3D::GetRawData() just returns null so I'm not sure of another alternative to accomplish this. Thanks!

-------------------------

cadaver | 2017-01-02 01:12:26 UTC | #2

Will be a minor change to change text_ to protected and then you could subclass Text3D.

EDIT: all Text3D data that was previously private is now protected in the master branch.

-------------------------

Victor | 2017-01-02 01:12:27 UTC | #3

[quote="cadaver"]Will be a minor change to change text_ to protected and then you could subclass Text3D.

EDIT: all Text3D data that was previously private is now protected in the master branch.[/quote]

Awesome thanks! I was just about to say that the uiBatches and uiVertexData were also things I would need but it seems you've already taken care of that! :slight_smile: Here's what I got so far, although I'm still tweaking the curve. Thanks again man!

[img]http://i.imgur.com/uWeoMpm.png[/img]

-------------------------

yushli | 2017-01-02 01:12:27 UTC | #4

That looks like a nice feature to have. Care to share some code on how to achieve this?

-------------------------

Victor | 2017-01-02 01:12:27 UTC | #5

[quote="yushli"]That looks like a nice feature to have. Care to share some code on how to achieve this?[/quote]

Sure thing! Later tonight I'll create a repo and post what I have so far, but it's not perfect. Maybe someone out there can perfect it though!

One note however, I have noticed that values I get from Unity and Urho using the Vector math methods are different. To resolve this I've been using the glm library for all vector/quaternion math. An example is when you have the following:

[code]
Vector3 dir = (0, 0, 0);
Vector3 up = Vector3::UP;
float angle Angle(dir, up)
[/code]

You'll either get back 0 or nan (can't remember) for the angle. However Unity will translate this as 90.0 degrees. GLM returns back in radians, however once you convert it you would see that it returns 90 degrees as well. Not sure if I did something wrong but I just ended up using glm to be the happy medium in my port from Unity to Urho. Perhaps Urho was also returning radians and I just didn't notice heh :slight_smile:.

EDIT:
If you see here [url]https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Math/Vector3.h#L232[/url] it will find the magnitude of the dir and so you end up with a n / 0 case.

-------------------------

Victor | 2017-01-02 01:12:28 UTC | #6

Still working out some issues, so I probably won't have any examples soon. However [b]yushli[/b], the only thing I'm really doing to curve my text is manipulating this example here:

[url]https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/UI/Text3D.cpp#L492-L542[/url]

You can get a curve through using a parabola method like the following:

[code]
    static glm::vec3 SampleParabola(glm::vec3 start, glm::vec3 end, float height, float t)
    {
        if (glm::abs(start.y - end.y) < 0.1f)
        {
            //start and end are roughly level, pretend they are - simpler solution with less steps
            glm::vec3 travelDirection = end - start;
            glm::vec3 result = start + t * travelDirection;
            result.y += glm::sin(t * glm::pi<float>()) * height;
            return result;
        }
        else
        {
            //start and end are not level, gets more complicated
            glm::vec3 travelDirection = end - start;
            glm::vec3 levelDirection = end - glm::vec3(start.x, end.y, start.z);
            glm::vec3 right = glm::cross(travelDirection, levelDirection);
            glm::vec3 up = glm::cross(right, travelDirection);
            if (end.y > start.y) up = -up;
            glm::vec3 result = start + t * travelDirection;
            result += (glm::sin(t * glm::pi<float>()) * height) * glm::normalize(up);
            return result;
        }
    }
[/code]

I hope that helps!

-------------------------

yushli | 2017-01-02 01:12:28 UTC | #7

Thanks for your example code Victor. I will try it out. Take your time. Urho3d's community is such a nice one as I can always get something new to learn from.

-------------------------

Victor | 2017-01-02 01:12:28 UTC | #8

[quote="yushli"]Thanks for your example code Victor. I will try it out. Take your time. Urho3d's community is such a nice one as I can always get something new to learn from.[/quote]

No prob! When iterating over the vertexData you can handle each triangle in the following way as well:

[code]
for (unsigned i = 0; i < uiVertexData->Size(); i += (UI_VERTEX_SIZE * 6)) {        
        // Triangle #1
        Vector3& v1 = *(reinterpret_cast<Vector3*>(&(*uiVertexData)[i]));  // Bottom-left
        Vector3& v2 = *(reinterpret_cast<Vector3*>(&(*uiVertexData)[i + (UI_VERTEX_SIZE * 1)]));  // Bottom-right
        Vector3& v3 = *(reinterpret_cast<Vector3*>(&(*uiVertexData)[i + (UI_VERTEX_SIZE * 2)]));  // Top-left

        // Triangle #2
        Vector3& v4 = *(reinterpret_cast<Vector3*>(&(*uiVertexData)[i + (UI_VERTEX_SIZE * 3)]));  // Bottom-right
        Vector3& v5 = *(reinterpret_cast<Vector3*>(&(*uiVertexData)[i + (UI_VERTEX_SIZE * 4)]));  // Top-right
        Vector3& v6 = *(reinterpret_cast<Vector3*>(&(*uiVertexData)[i + (UI_VERTEX_SIZE * 5)]));  // Top-left
}
[/code]

Both of those triangles will make up a single character. :slight_smile:

-------------------------

Victor | 2017-01-02 01:12:32 UTC | #9

So I'm still working on solving this issue. I think the main issue I'm noticing is that when dealing with the vertices for a text object, I'm not able to convert world space coordinates properly for the text (I think this is my own fault for not understanding something properly). When attempting to apply the height of the text onto the terrain I start getting even weirder results. I also included a stroke effect to see what happens.

My goal is to convert my old project over into Urho. So far so good, just getting hung up on this text stuff. Perhaps this is more custom and I should try to rewrite a few things to fit my needs, but the world space to local space for the text object is really what seems to be my issue. Also, a way to set the min/max font size seems to be another hurdle I'm having as well.

My Urho Example (sorry, I haven't implemented water yet, that's next!):
[img]http://i.imgur.com/oVtqiVh.png[/img]

My Old Example:
[img]http://i.imgur.com/9rcfwu0.png[/img]

One huge plus about Urho so far is the fact that it's super fast when loading all of these textures/data points!

-------------------------

TheComet | 2017-01-02 01:12:33 UTC | #10

That looks really cool!

-------------------------

Modanung | 2017-01-02 01:12:36 UTC | #11

[quote="TheComet"]That looks really cool![/quote]
Hear, hear!

-------------------------

Victor | 2017-01-02 01:12:36 UTC | #12

Honestly, I haven't been able to figure out the text issue... For some reason I can't figure out how to apply the terrain's height correctly with the text's localized position. Also, as you saw in my image the stroke kinda goes all over the place as it doesn't update with the curve :frowning:

For now I've just moved on and I may or may not revisit this... Honesty, in the direction I'm going it might not matter to have text on the map, just have the border lines:

[img]http://i.imgur.com/ysNry1y.png[/img]

I did finally update my branch with the recent changes made and started to rebuild the class, but for now I'm going to just move on.

Re-implementation of the class (sorry, I know it's not much)
CurvedText.h: [gist.github.com/victorholt/6f5a ... c160ffc155](https://gist.github.com/victorholt/6f5ae49a800ba06c1aac70c160ffc155)
CurvedText.cpp: [gist.github.com/victorholt/2c77 ... 53bbe145ee](https://gist.github.com/victorholt/2c7757dd6fba7504b5018053bbe145ee)

-------------------------

Lumak | 2017-01-02 01:12:42 UTC | #13

What ever game you're making, it looks interesting. It kind of reminds me of the board game Risk, but yours is in 3D.

-------------------------

Victor | 2017-01-02 01:12:43 UTC | #14

[quote="Lumak"]What ever game you're making, it looks interesting. It kind of reminds me of the board game Risk, but yours is in 3D.[/quote]

Thanks man! 

My inspiration is from games like Europa Universalis and Crusader Kings 2. I hope to have a game which is highly moddable like those games, although my focus is more on fantasy gameplay than historical. Although, ideally, if you wanted to play a historical game you can either port CK2's base game or any of the other CK2 mods into this game when it is completed. :slight_smile:

-------------------------

Victor | 2017-01-02 01:12:49 UTC | #15

Ok, I think this should be marked as solved. Using 1vanK SpriteBatch ([topic596.html](http://discourse.urho3d.io/t/spritebatch-beta-same-like-in-xna-or-d3dxsprite/591/1)) as my inspiration I was able to finally get this all working. Just needed some good examples of using the font class properly. Thanks 1vanK!

[img]http://i.imgur.com/yQOGXKj.png[/img]

-------------------------

