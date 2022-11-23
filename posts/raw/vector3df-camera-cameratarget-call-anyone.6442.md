grokko | 2020-10-17 01:29:01 UTC | #1

Hello Everyone!
  I want to procure a RayCast from my camera to anywhere else in the scene my mouse cursor goes.
To do this we need a cameraTarget or cameraLook. I cannpt find anything similar in the docs.

Can you help?
Thanks
Michael S.

-------------------------

vmost | 2020-10-17 01:28:02 UTC | #2

There is `Node::LookAt()`, although there may be a better way

-------------------------

evolgames | 2020-10-17 02:08:13 UTC | #3

Hey Micheal, check out the Decal sample. I'm pretty sure it raycasts from mouse cursor.
But if you have the mouse hidden at the center of the screen you have to do something like this (in lua, easily convertable):
```
function Raycast(maxDistance)
	local pos=Vector2(graphics.width/2,graphics.height/2)
    local camera = cameraNode:GetComponent("Camera")
    local cameraRay = camera:GetScreenRay(pos.x / graphics.width, pos.y / graphics.height)
    local octree = scene_:GetComponent("Octree")
    local result = octree:Raycast(cameraRay, RAY_TRIANGLE, maxDistance, DRAWABLE_GEOMETRY)
	return result
end
```

Returns your result nodes, which can be multiple or one if you want.
Depending on what this raycast is used for, you might approach the issue differently.

-------------------------

Modanung | 2020-10-17 09:08:51 UTC | #4

It sounds like you're looking for a way to implement basic mouse look. This would not require raycasting, instead converting cursor movement to the camera's node rotation should suffice. But I may not be seeings things.

Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

grokko | 2020-10-20 03:42:20 UTC | #5

Hi Gang!
   I did look into the Decal sample and learned exactly what I wanted.
Speaking of decals,I was also looking into the possibility of having a 3d cursor as a Decal  whilst making the 2d cursor invisible...kindof like a decalled hand for instance touching the target Nodes in R3. I tried it with the example, and the urho fish decal just slips in trails from odd frames, but does lay its mesh decal. I know its a 'frame' engine too and not just a slobber fest. The Raycasting code btw, seems top notch quality easy to use - with the benefit of an enhanced resultQuery to query Node types so easily in the Update scenario...which is great for games.
  For my purposes, I pulled about 20 things from the Demo's to successfully port my 2project over to Urho, and I was up and running in 3 days work, with another few days for the scaffolding.
  Also, the api is good enough!...many of the functions, such as the Quaternion function to represent not just a rotation - but a new axis set and an angle around that set - have enough documentation to track exactly what you need. I'm coming from a Irrlicht project where I used everything in the GPU. 

My next conquest is LogicComponent to register your own StaticModel - like rendering Nodes for weapons and spells

Thanks for a great Engine!
btw my current project has about 64 characters and the performance is awesome indeed.
Kudos for you again!
Lord Fiction

-------------------------

