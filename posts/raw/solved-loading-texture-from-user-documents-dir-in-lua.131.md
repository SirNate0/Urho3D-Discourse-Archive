Mike | 2017-01-02 00:58:16 UTC | #1

I'm desperatly trying to load a texture in lua using:
[code]
local texture = Texture2D():Load(fileSystem:GetUserDocumentsDir() .. "MyTexture.png")
[/code]
I get "ERROR: Null image, can not load texture".

-------------------------

friesencr | 2017-01-02 00:58:16 UTC | #2

all resources are loaded from resource directories.  urho has a virtual filesystem it imposes on its users.  if you wanted to load a resource from the users directory you would have to add that folder as a resource directory.

Edit: sorry i didn't see you were using load.  i need sleep.

-------------------------

cadaver | 2017-01-02 00:58:17 UTC | #3

This is a Lua bindings order issue. The string overload should be specified last in the .pkg file, but in this case the string overload is in the base class (Resource) while Texture2D Load() that takes an image pointer is registered later. I think you can work around it by loading an image from filename, then loading the image into your Texture2D.

-------------------------

Mike | 2017-01-02 00:58:17 UTC | #4

I've tried this one with no success (same error):

[code]
local texture = Texture2D():Load(Image():Load(fileSystem:GetUserDocumentsDir() .. "Procedural.png"))
[/code]
Is this what you were thinking about?

-------------------------

aster2013 | 2017-01-02 00:58:17 UTC | #5

Hi, mike, 

Dont write all code in one line.[quote]local texture = Texture2D():Load(Image():Load(fileSystem:GetUserDocumentsDir() .. "Procedural.png"))[/quote]

You need write like this:
[code]local image = Image()
image:Load(fileSystem:GetUserDocumentsDir() .. "Procedural.png")

local texture = Texture2D()
texture:Load(image)
[/code]

-------------------------

Mike | 2017-01-02 00:58:17 UTC | #6

Thanks Aster,

From Cadaver's explanations, it indeed makes sense to split the 2 loads and it works fine now.
However a segmentation fault is always reported when I exit (using 'Esc' key).

For example, if I replace the 'logoTexture' in Utilities/Sample.lua, a segfault is issued on exit.

-------------------------

aster2013 | 2017-01-02 00:58:17 UTC | #7

[quote]
However a segmentation fault is always reported when I exit (using 'Esc' key).
For example, if I replace the 'logoTexture' in Utilities/Sample.lua, a segfault is issued on exit.[/quote]

It because the Sprite keep the texture as shared pointer. For this issue you must create Texture2D with Texture2D:new() and then assign to Sprite.

-------------------------

Mike | 2017-01-02 00:58:17 UTC | #8

Many thanks, it now works perfectly  :stuck_out_tongue:

-------------------------

