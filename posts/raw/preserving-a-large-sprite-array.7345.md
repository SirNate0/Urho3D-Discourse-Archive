evolgames | 2022-11-03 11:35:59 UTC | #1

I'm working on a game with a large procedural map. The game generates the overworld, represented by small sprites in a 2d grid. Wait times for generation are fine. However, to reload this same map later in game as a map screen in the menu would be far too slow. Could I just screenshot it at generation and load that file in somehow? I guess I'd have to figure out the cropping? Or is there a better way?
I'm talking like 1million combines sprites so...

Curious if anyone has done anything similar.

-------------------------

vmost | 2022-11-03 13:17:12 UTC | #2

If you have a maximum resolution for the map you could save a map file that maps each pixel to a grid of underlying sprites. Initialize the file to black then set each map pixel as the world gets generated. If you exceed the bounds of your file, then make additional files in an expanding map composite.

If a change in the world requires a change in the map, it should be straightforward to add an event to world changes that the map-maker can listen to to update relevant map pixels.

-------------------------

evolgames | 2022-11-03 13:44:38 UTC | #3

Hm so it's already a grid of sprites. It takes up 1gb of memory after creation. If I unload them then reloading them takes a while. I should clarify that I already have the data saved in a nested lua table. I am basically stuck between disabling the sprites and keeping them in memory (wasteful) or removing and recreating from the data (slow). But maybe at map gen I could create an image file pixel by pixel and blow it up, since the overworld sprites are 8x8 sprites of solid colors anyway. Need to check if urho has a way to create image data like that. I did that in another framework once.

-------------------------

evolgames | 2022-11-08 14:24:54 UTC | #4

Okay I figured it out.

Took a little tinkering but got image creation working pixel by pixel. This works great for an overworld preview. I also am going to try using this as the base map layer in game, and just spawning entities, waves, and other details on top of it. For example, most games like this have grass cluster tiles every so often instead of regular grass tiles. However, I can just do the clusters randomly and not have to have a sprite for each tile. I can now have the entire map (or a large area) loaded as a single sprite and keep a great frame rate.

Saved the map preview to disk and then used it later as a sprite2d resource. Also will later let the player look at their creations and stuff.

```
function InitImage()
	img = Image:new()
	local sz = SizeIndexToSize(worldgen.mapSize)
	img:SetSize(sz,sz,4)
	return img
end

function AddPixel(x,y,tile)
	local col = spriteColors[tile]
	img:SetPixel(x-1,y-1,col)
end

function AddImage()
	local sz = SizeIndexToSize(worldgen.mapSize)
	
	local texture = Texture2D:new()
	texture:SetFilterMode(FILTER_NEAREST)
	texture:SetNumLevels(1)
	texture:SetSize(sz,sz,graphics:GetRGBAFormat(),TEXTURE_STATIC)
	texture:SetData(img)
	
	local sprite = ui.root:CreateChild("Sprite")
	sprite:SetTexture(texture)
	local m = graphics.width*.007 * (1/(sz*.02))
	sprite:SetSize(sz*m,sz*m)
	sprite:SetPosition(graphics.width/2 - sz*m/2,graphics.height/2 - sz*m/2)
	sprite:SetBlendMode(BLEND_ALPHA)
	
	img:SavePNG("Data/Art/map.png")
end
```

-------------------------

