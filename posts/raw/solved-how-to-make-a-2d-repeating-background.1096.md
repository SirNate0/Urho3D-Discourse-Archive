yushli | 2017-01-02 01:05:25 UTC | #1

I can't find the api to do that. also the repeating background can be animated to move forward/backward.

-------------------------

yushli | 2017-01-02 01:05:26 UTC | #2

maybe more specific about this. suppose we need to make a plane flying forward across the dark sky. the dark sky can be mimic by using a small black image with a few stars, then repeating this small image to form the background. also the flying can be mimic by moving the black sky background backward. I cannot find the proper APIs to do that.

-------------------------

weitjong | 2017-01-02 01:05:26 UTC | #3

I suppose you can try to have a quad command in the RenderPath. Bound the background texture to the quad. Then animate the UV of the texture in the shader. I think you can get the elapsed time in the shader parameter.

-------------------------

Bananaft | 2017-01-02 01:05:26 UTC | #4

Hi.

You just update it's position in every frame. I'm not familiar with Urho2D, but I made similar thing for 3d side-scroller prototype, i did recently.

[code]
class Scenery : ScriptObject
{
	void Update(float timeStep)
	{
		node.position = node.position + Vector3(0,0,-1 * flightspeed * timeStep);                                                    // move node in current frame
		if (node.position.z < -1 * sceneSize) node.position = Vector3(node.position.x,node.position.y,node.position.z + sceneSize);  // check if you flew past landscape model, and if so move
	}                                                                                                                               // node backwards, to fly by same landscape again
}
[/code]

Two similar landscape models was linked to this node in succession. <sceneSize> is the length of single landscape model. When you fly by first model, you see second(same) model, and when it jumps you backwards, you won't notice it.

-------------------------

yushli | 2017-01-02 01:05:28 UTC | #5

the problem can be narrowed down to like this: a texture is of size 128x128, and the surface is 256x256. Now there are two ways to use the texture to cover the surface: one is to scale the texture by 2; the other is to repeat the texture both horizontally and vertically. Currently Urho3d has the first way with the API of SetScale(), but doesn't have the (easy) API to do the second way. I would like to suggest to add this API in Urho3D.

-------------------------

cadaver | 2017-01-02 01:05:28 UTC | #6

The tiling settings are controlled in the Material class. See Material::SetUVTransform(), or the material editor window in the editor. In 2D components like StaticSprite2D you'll need to set a material into use instead of just the sprite image.

-------------------------

