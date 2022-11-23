ghidra | 2017-01-02 00:59:52 UTC | #1

I'm kind of stuck on how the "node" parameter is working in a scriptObject.

Using node.scene, and node.parent are working as per my late post [url]http://discourse.urho3d.io/t/angelscript-createscriptobject-and-external-class-solved/342/1[/url], at least as long as it is in the update function.
If for example I call a function from update, like raycasting (using the example from navigation.as). If I have a function called raycast, this throws errors, null exception:

[code]
bool raycast(float maxDistance, Vector3& hitPos, Drawable@& hitDrawable){
    hitDrawable = null;
    IntVector2 pos = ui.cursorPosition;

    Camera@ camera = node.scene.GetComponent("Camera");
    Ray cameraRay = camera.GetScreenRay(float(pos.x) / graphics.width, float(pos.y) / graphics.height);
   
   ......

   return false;
}
[/code]

The GetComponent("Camera") doesnt actully return a camera.

also, as another example...
If I do what i am trying in a separate function in update, as long as I pass the uint id it works this way:

[code]
void Update(float timeStep){
	Node@ cameraNode = node.scene.GetNode(_camera_id);
	Camera@ camera = cameraNode.GetComponent("Camera");
	....
}
[/code]

but I dont pass the uint id and try to use a string like:

[code]
void Update(float timeStep){
	Camera@ camera = node.scene.GetComponent("Camera");
	....
}
[/code]

It does not work, although I feel like I see this methodology used in the examples to grab static meshes and animated meshes etc... that is, not having to get the node before grabbing the component.

Just looking for some clarification on what I might be overlooking.
Thank you.

-------------------------

friesencr | 2017-01-02 00:59:52 UTC | #2

You don't usually have a camera directly under the scene since you don't move the scene. 

This code: 
[code]Camera@ camera = node.scene.GetComponent("Camera");[/code]
would be looking for a camera on the scene.  The scene inherits from node so it can but it likely isn't what you want.

The string is actually the type of component you want.  Urho will fetch the first component of that type on that node.   The string is actually converted to a StringHash internally, not that that matters.  In this case the type is a Camera.  The camera is a component.  GetChild

In all of the example code the app holds a sharedptr to a node that is holding the camera.  This is the easiest way of handling it.

-------------------------

