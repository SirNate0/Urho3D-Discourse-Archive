elemusic | 2017-01-02 01:10:54 UTC | #1

Just Find theDebugRenderer AddLine can draw line,which is good.

the only problem is how can i draw these line after the sprite?

 i try to draw line like
[code]
DebugRenderer* debug = scene_->GetComponent<DebugRenderer>();
for (int i = 0; i < 512; ++i)
{
	debug->AddLine(Vector3(i, 0, 10), Vector3(i, 100, 10), Color(1.0f, 1.0f, 1.0f));
}
[/code]
my sprite is at (0,0,0)
the line just block my sprite,and (i,0,-10) not work either.

can i set the drawing order or did i do something wrong?

-------------------------

elemusic | 2017-01-02 01:10:57 UTC | #2

nobody reply,does it mean i have to do it myself,or rewrite the drawline geometry

-------------------------

weitjong | 2017-01-02 01:10:58 UTC | #3

The DebugRenderer, as its name implies, should only be used for debugging purpose. It should not be used as if it is part of your scene construction. It has been awhile since I last see those code but if I recall correctly the debug batch is always done last so those debug lines would always be rendered over your other drawables. I believe what you are looking for is CustomGeometry component.

-------------------------

