vivienneanthony | 2017-01-02 01:02:15 UTC | #1

Hello,

I have two questions.

1) Do anyone know what's causing the weird alpha using Billboards. I get some weird line or clip that is not transparent. I tried all various .dds and .png images including from different sources and some edited but I get the same problem.

2) How do I get a rotation of a specific point from terrain? So I can match up rock meshes to that proper align so I don't get rocks in air on cliffs.

Thanks for everyone help so far. These two is bugging me.

Vivienne

[img]http://i.imgur.com/Sy5D6Us.png[/img]
[i.imgur.com/Sy5D6Us.png](http://i.imgur.com/Sy5D6Us.png)

-------------------------

vivienneanthony | 2017-01-02 01:02:18 UTC | #2

I tried this. Is it legit?

[code]        RockNode->SetRotation(Quaternion(position_x,terrain->GetHeight(Vector3(position_x,0.0f,position_z)), position_z));[/code]

I'm trying to get the quaternion of a specific point using the spot in terrain.

-------------------------

franck22000 | 2017-01-02 01:02:18 UTC | #3

Hello :slight_smile: Try this:

 RockNode->SetRotation(Quaternion(Vector3::UP, terrain->GetNormal(Vector3(position_x,position_y,position_z))));

-------------------------

vivienneanthony | 2017-01-02 01:02:19 UTC | #4

[quote="franck22000"]Hello :slight_smile: Try this:

 RockNode->SetRotation(Quaternion(Vector3::UP, terrain->GetNormal(Vector3(position_x,position_y,position_z))));[/quote]

It's a beautiful thing for sure. :slight_smile: Happy New Years!

-------------------------

vivienneanthony | 2017-01-02 01:02:19 UTC | #5

Now I just have to figure out the weird billboard issue ....

-------------------------

vivienneanthony | 2017-01-02 01:02:26 UTC | #6

The method seems to work for mostly smooth areas. It doesn't work great for highly elevated areas it seems.

[video]https://www.youtube.com/watch?v=CrkF9NSDWkw&list=PLg3Q9upEQvPRAYaIqhImkUu1RBgSZA_N7&index=27[/video]

-------------------------

