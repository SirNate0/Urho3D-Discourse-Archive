evolgames | 2020-04-30 07:35:10 UTC | #1

Hey guys, little question about raycasting. I'm using the code below to raycast mouse position for a 2d isometric grid-based game. I have z-depth in gameplay, but each sprite node is actually positioned at z=0 and is instead set on a corresponding layer. Using this raycast function works only for top-level nodes. It looks like there are multiple ways to do this, but this was the only way that seemed to work. The drawable it returns works perfect.

However, I'd like to do a "deeper" raycast through the layers where the cursor is positioned. Is there a way to get a list of each node (stacked in the layers on top of each other) in a table or list? Changing maxDistance isn't it because everything is at exactly the same z height of 0, so I'm a bit stumped. If I disable the top-layer node, the single raycast will hit the next one down, though, so I guess I could do sequential single raycasts like this, depending on the use-case, until it finds the desired tile. But I figure if there is a way to get this "stack" of layers in a multi-raycast result, that would be more elegant and efficient.


```
function Raycast(maxDistance)
    local hitPos = nil
    local hitDrawable = nil

    local pos = ui.cursorPosition
    -- Check the cursor is visible and there is no UI element in front of the cursor
    if (not ui.cursor.visible) or (ui:GetElementAt(pos, true) ~= nil) then
        return nil, nil
    end

    local camera = cameraNode:GetComponent("Camera")
    local cameraRay = camera:GetScreenRay(pos.x / graphics.width, pos.y / graphics.height)
    -- Pick only geometry objects, not eg. zones or lights, only get the first (closest) hit
    local octree = scene_:GetComponent("Octree")
    local result = octree:RaycastSingle(cameraRay, RAY_TRIANGLE, maxDistance, DRAWABLE_GEOMETRY)
    if result.drawable ~= nil then
        return result.position, result.drawable
    end

    return nil, nil
end
```

-------------------------

dertom | 2020-04-30 08:33:49 UTC | #2

Sry, I just cross read the topic,...
Using octree:RaycastSingle gives you the nearest Node that the ray hit.
If you want all nodes hit within range you need to use octree:Raycast. Which seems to have the same call signature but returns a list of QueryResults. In there should(!) be all nodes hit...

Hope that helps...(didn't test it though ;) )

ps: link to octree-lua-api:
https://urho3d.github.io/documentation/1.6/_lua_script_a_p_i.html#Class_Octree

-------------------------

