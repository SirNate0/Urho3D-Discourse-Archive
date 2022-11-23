Hevedy | 2017-01-02 00:58:18 UTC | #1

After add models, play with editor, create scenes, the structure of the folders create a mega mix soup, where in the same folder are 6 types of files.
Now i give the idea of create this structure for organize things better.
Here the idea:

[code]Original
-Bin
 -CoreData
 -Data
  -Fonts
   -*.*
  -LuaScripts
   -*.*
  -Materials
   -*.*
  -Models
   -*.*
  -Objects
   -*.*
  -Particle
   -*.*
  -PostProcess
   -*.*
  -Scenes
   -*.*
  -Scripts
   -*.*
  -Sounds
   -*.*
  -Textures
   -*.*
  -UI
   -*.*
  -Urho2D
   -*.*
[/code]

[code]Changed
-Bin
 -Profile
  -Logs
   -(Here save all logs of bin)
  -ScreenShots
   -(Here save screenshots from 9)

 -CoreData

 -Data
  -Editor
   -Prefabs
    -(Here editor prefabs)
   -Nodes
    -(Nodes from editor)

  -Media
   -Animations
    -(.ani animations of models, in subfolders)(Example: NinjaSnowWar/Ninja_Attack1.ani ...)
   -Fonts
    -(fonts)
   -Models
    -(.mdl, in subfolders)
   -Music
    -(.ogg and others, in subfolders)
   -Sounds
    -(.wav and others, in subfolders)
   -Textures
    -(.png and others, in subfolders)(No xml)
   -Videos
    -(Videos, no videos at this moment)

  -Objects
   -Animations
    -(.xml , in subfolders)(Example: NinjaSnowWar/Ninja_Stealth.xml ...)
   -Definitions
    -(.xml, in subfolders)(Example: NinjaSnowWar/Potion.xml ...)
   -Materials
    -(.xml , in subfolders)(Example: NinjaSnowWar/SnowCrate.xml ...)
   -Models
    -(.txt (this need rename, example .skin), in subfolders)(Files created to define the textures of    model)
   -Particle
    -(.xml , in subfolders)(Example: Smoke.xml ...)
   -Shaders
    -(.xml , in subfolders)(Example: Common/Bloom.xml ...)
   -Scenes
    -(.xml  for scenes scripts ?, in subfolders)
   -GUI
    -(.xml , in subfolders)(Example: EditorIcons.xml ...)

  -Scenes
   -NinjaSnowWar
    -(.xml ,scene files)

  -Scripts
   -AS
    -(.as , in subfolders)(Example: Editor/Editor.as ...)
   -Lua
    -(.lua, in subfolders)(Example: Demos/01_HelloWorld.lua ...)

  -Urho2D
    -(Same of Data/ )

[/code]

*subfolders example of new Media/Models/ folder:
[code]
-Media
 -Models
  -Common (Common mdl files)
  -Primitives (Primitives mdl files (Cube, Sphere...))
  -Demos (mdl Jack)
  -Editor (mdl axis)
  -NinjaSnowWar (mdl of ninja scene)
[/code]

-------------------------

Azalrion | 2017-01-02 00:58:18 UTC | #2

Anything that will cause an error to be thrown in the logs when using urho independently such as MessageBox.xml should be included in CoreData.

-------------------------

cadaver | 2017-01-02 00:58:18 UTC | #3

Another thing to consider is tools. When you import a scene, it's quite easy to program the tool to output models to Models subfolder, materials to Materials subfolder, textures to Textures etc. Anything more complicated than that and it's no longer easy for the tool to know where it should put everything.

-------------------------

Mike | 2017-01-02 00:58:18 UTC | #4

I prefer to have one folder for each model, for example:
[code]
Models
    Model1 folder (example Ninja)
        Ninja.mdl (model)
        Ninja.txt (material list)
        anims.ani (anims)
        Textures folder (for textures specific to this model)
            ...
        Materials folder (for materials specific to this model)
            ...
    Model2 folder...
[/code]
And use generic 'Textures' and 'Materials' folders for shared resources only.
But it requires heavy manual tweaks.

-------------------------

friesencr | 2017-01-02 00:58:19 UTC | #5

Bits of the editor styles have crept into the DefaultStyle.xml.  A refactoring of the styles may be in order as well.

-------------------------

