JTippetts | 2020-01-24 07:28:34 UTC | #1

https://jtippetts.github.io/GoldRush.html

I've been working on a small little incremental game project for the last several months, off and on. It's built for the web using the WebGL back-end. The game is similar to and inspired by an idle game called Reactor Idle that I played for a few months last year: you construct units on a map that convert heat, generated by heat sources, into gold. Various game mechanics exist such as direct conversion, water-cooling, steam generation, and power/electricity generation. The game is still very much in development, and much of the artwork and mechanics are still in flux. Here is a development screenshot of it's current state:

![image|666x500](upload://fT1Spiv7AtRHElB2KOiwmBhD9A2.jpeg) 

In this shot, all units currently implemented in the game as of this writing are unlocked using some cheats. The multi-colored icons on the top row of the build menu represent the various heat sources, ranging from a simple campfire all the way up to the ultra-powerful Eldritch Artifact. The game map view shows a map build with various pipe setups, including heat pipes (the red pipes), which can carry heat from heat sources and disperse it to any connected camps, water pipes (blue) which carry water from shoreline pumps to any camps that utilize water cooling, steam pipes (cyan), which carry steam from boilers to any camps that can use steam, as well as some direct-conversion setups on the bottom and on the top.

![image|666x500](upload://c6789igOQFqw9PPDEmOtNm5AONK.jpeg) 

This shot is a more typical gameplay setup from an actual playthrough. It has a water-enabled setup on the top 2/3 of the map, and a science enclave on the bottom.

I keep a fairly up-to-date build live at https://jtippetts.github.io/GoldRush.html if anyone is interested in giving it a go; just bear in mind that it changes frequently, sometimes has cheats enabled for my own testing, and occasionally is completely broken. It has game persistence using local storage, but some builds will reset the game if things change drastically enough. You can also manually reset your game from the Stats menu.

Gameplay (Long):

Select a unit from the build menu on the left. If there are any upgrades that apply to that unit, they are listed below the build menu, along with the price to purchase an upgrade (+) and the amount of gold you get back if you sell-back an upgrade (-). In the top-left corner are displayed your Gold and Science amounts. Building a unit costs Gold. Some technology researches cost Gold, others cost both Gold and Science.

Left-click on the map with a unit selected to build a unit. Right-click a unit already on the map to destroy it. Hold down left and drag to create multiple units; hold down right and drag to delete multiple units. Hold down Ctrl and right click a unit to destroy all units of that given type.

At game start the only unit available (ignore some currently enabled units in testing for now) is a Panner, an old-timer in a cowboy hat who, when constructed, will generate a tiny amount of gold per game tick. By spending gold you can upgrade the amount of gold a panner generates, as well as the duration the panner exists before it must be renewed. Units renew automatically, spending the purchase price of the unit to do so.

After you have earned 1000 gold, you can research Camping under the Research tab, which will unlock two units: Panner Camp and Campfire. (Note that as of this writing, the graphic for Campfire is busted, so it shows a stove-graphic instead. Sorry. :smiley:  ) Camps are units that convert heat to gold. When placed adjacent to a heat source, such as a campfire, they will collect the heat (portioned out equally to all heat-consuming units adjacent to the heat source) and turn it to gold. Camps have an upgradable conversion capacity and excess-heat capacity. Upgrading the Camp Effectiveness increases the amount of heat Camps can convert to gold. Upgrading Heat Conductor Capacity increases the amount of excess heat a Camp can accumulate before it explodes.

If you overheat a Camp beyond its capacity, it will explode. Try to match camps with campfires such that there are enough camps, with enough capacity, to utilize all the heat the fire generates.

After awhile you unlock heat pipes. Heat pipes can be constructed in lines or networks, and allow you to spread the heat from a high-powered heat source out to many camps. If your heat pipes explode, try upgrading Heat Pipe Capacity. The capacity of heat pipes and the over-heat capacity of Camps can allow you to disperse a great deal of heat. You can build Heat Pipes just as you build regular units. The game auto-tiles the pipes so that they automatically configure and hook-up to adjacent heat-enabled units.

After unlocking Heat Pipes, you can eventually research Science, which unlocks another unit type, a Science Hut. Science Huts work similarly to Camps, in that they convert heat to Science. Beware, though; they have a much smaller over-heat capacity than Camps do, and over-heating a Science Hut beyond it's cap causes it to explode and deal a large amount of heat to units in the explosion radius. It's possible to take out your entire science enclave this way if you are not careful.

Eventually you will unlock a higher tier of Camp called a Sluicer Camp. The Sluicer camp operates similarly to Panner camp, in converting heat to gold. However, after unlocking it you will eventually be able to unlock Water Technology, which gives you access to water pipes and water pumps. Water supplied to the Sluicer Camp drastically increases the amount of heat the camp can convert.

And so the game goes. Periodically, new and hotter heat sources are unlocked, as well as new technologies. From the Map tab you can purchase a new Map. The old one is permanently discarded; however, you keep the amounts of your Gold Avg and Science Avg when buying a new map as permanent bonuses. You can view your current Base Gold and Science, as well as some rudimentary map stats, in the Stats button.

When the game is offline, or you are switched away from the tab, the game will accumulate bonus ticks, displayed in the box underneath the Stats tab. Next to the bonus ticks is a button, Go Fast, that will toggle using bonus ticks. Bonus ticks accumulate 1 per 10 seconds of offline time, and when used they increase the speed of your tick rate by 10 ticks per second, allowing you to speed up the game for as long as your bonus ticks hold. You can accumulate bonus ticks while offline, and you can eventually construct a unit which converts power to bonus ticks.

-------------------------

weitjong | 2020-01-24 07:36:58 UTC | #2

Could not start on iPhone Safari.

```
ERROR: Could not create OpenGL context, root cause 'Could not create EGL context (call to eglCreateContext failed, reporting an error of EGL_BAD_MATCH)'
```

-------------------------

JTippetts | 2020-01-24 07:52:48 UTC | #3

Yeah, I wouldn't really try to play this on a mobile. I've seen too many bugs when I've tried it in mobile browsers before, plus I can't really test it on mobile outside of Chrome's emulation. It still has that double-click event bug that causes buttons to double click, and I really have no idea how to even begin tracking that one down.

Edit: Also to note, I am using the experimental GLES3 branch and WebGL2. Maybe that has something to do with being unable to create a context?

Edit(2): I uploaded a regular WebGL build, maybe that will fix the no context thing, but it probably still won't be nice to play on a mobile.

-------------------------

weitjong | 2020-01-24 08:28:53 UTC | #4

At least it can be started now on mobile browser. The WebGL 2 build option is not yet ready, if you ask me.

-------------------------

JTippetts | 2020-01-24 08:31:00 UTC | #5

Yeah, probably not. It works on every desktop browser I've tried it on, but this game only uses default shaders that don't require WebGL2, so I'll just stick with regular WebGL 1 for now.

-------------------------

johnnycable | 2020-01-24 16:35:53 UTC | #6

Looks neat!
It started on my mac, but cannot do anything... tried to buy an island, but the screen gets stuck... can only got back to the starting screen...

-------------------------

JTippetts | 2020-01-24 17:31:09 UTC | #7

You can't build any panner units on the starting map? You won't be able to afford to buy a new map until you have some gold. What do you mean by "screen gets stuck"? Is there anything in the javascript developer console about errors? I don't have access to a Mac to test it out myself.

-------------------------

johnnycable | 2020-01-25 16:22:00 UTC | #8

I've tried with Chrome, and it's not working. 

![Screenshot 2020-01-25 at 17.17.33|690x422](upload://2e42taRHZzVrgCIg4RDXcmE3fzQ.png) 

Safari does.

![Screenshot 2020-01-25 at 17.20.03|533x500](upload://kvZxaFeCLfibJlekXAfe53gSknS.png)

-------------------------

JTippetts1 | 2020-01-25 21:22:43 UTC | #9

Are there any errors in the dev console? I don't have access to a Mac, so I can't test it out for myself.

-------------------------

johnnycable | 2020-01-26 17:28:24 UTC | #10

here's the Chrome console log:

    favicon.ico:1 Failed to load resource: the server responded with a status of 404 ()
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] WARNING: Could not get application preferences directory
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Opened log file Game.log
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Added resource package /Data.pak
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Added resource package /CoreData.pak
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Adapter used WebKit WebKit WebGL
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Set screen mode 2048x1536 rate 0 Hz windowed monitor 0 highDPI
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Initialized input
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Initialized user interface
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource Textures/Ramp.png
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading temporary resource Textures/Ramp.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource Textures/Spot.png
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading temporary resource Textures/Spot.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource Techniques/NoTexture.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource RenderPaths/Forward.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Initialized renderer
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] WARNING: Could not get application preferences directory
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Initialized engine
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource Textures/UrhoIcon.png
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource UI/DefaultStyle.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource Textures/UI.png
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading temporary resource Textures/UI.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource Fonts/Anonymous Pro.ttf
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Font face Anonymous Pro (11pt) has 624 glyphs
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource UI/GameUI.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/GameUI.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource Fonts/BlueHighway.ttf
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Font face BlueHighway (12pt) has 395 glyphs
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Font face BlueHighway (11pt) has 395 glyphs
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Font face BlueHighway (14pt) has 395 glyphs
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource Tiles/stats.json
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource Tiles/heat_source_stats.json
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource Tiles/tiles.json
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource Tiles/heat_source_tiles.json
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource UI/UpgradeBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Font face BlueHighway (18pt) has 395 glyphs
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource UI/UpgradeContent.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeContent.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource Tiles/upgrades.json
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Camp Effectiveness
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Camp Water Effectiveness
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Camp Steam Effectiveness
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Machine Effectiveness
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Boiler Production
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Steam Turbine Production
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Power Line Capacity
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Steam Pipe Capacity
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Water Pipe Capacity
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Water Pump Production
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Science Hut Effectiveness
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Galvanic Laboratory Effectiveness
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Heat Conductor Capacity
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Campfire Thermal Output
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Campfire Lifetime
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Panner Production
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Panner Lifetime
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource Tiles/heat_source_upgrades.json
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Charcoal Thermal Output
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Charcoal Lifetime
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Methane Thermal Output
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Methane Lifetime
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Thermite Thermal Output
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Thermite Lifetime
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Hydrogen Thermal Output
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Hydrogen Lifetime
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Radium Thermal Output
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Radium Lifetime
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Thorium Thermal Output
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Thorium Lifetime
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Uranium Thermal Output
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Uranium Lifetime
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Plutonium Thermal Output
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Plutonium Lifetime
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Vardite Thermal Output
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Vardite Lifetime
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Peridite Thermal Output
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Peridite Lifetime
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Coradite Thermal Output
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Coradite Lifetime
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Zandite Thermal Output
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Zandite Lifetime
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Arcane Thermal Output
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Arcane Lifetime
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Occult Thermal Output
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Occult Lifetime
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Accursed Thermal Output
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Accursed Lifetime
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Eldritch Thermal Output
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] INFO: Pushing upgrade Eldritch Lifetime
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/UpgradeLevelBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource Tiles/heat_source_research.json
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource Tiles/research.json
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource UI/ResearchBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource UI/ResearchContent.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchContent.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/ResearchUnlockEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource UI/StatsWindow.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/StatsWindow.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Font face BlueHighway (16pt) has 395 glyphs
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource Tiles/maps.json
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading resource UI/MapPreviewPane.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Loading UI layout UI/MapPreviewPane.xml
    GoldRush.html:1 [Sun Jan 26 18:24:15 2020] DEBUG: Font face BlueHighway (13pt) has 395 glyphs
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] DEBUG: Loading resource Textures/unknownmap.png
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] DEBUG: Loading resource UI/MapSelectEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] DEBUG: Loading UI layout UI/MapSelectEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] DEBUG: Loading UI layout UI/MapSelectEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] DEBUG: Loading UI layout UI/MapSelectEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] DEBUG: Loading UI layout UI/MapSelectEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] DEBUG: Loading UI layout UI/MapSelectEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] DEBUG: Loading UI layout UI/MapSelectEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] DEBUG: Loading UI layout UI/MapSelectEntry.xml
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] INFO: Setting thumbnail
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] ERROR: Timeline logging not supported in web builds.
    printErr @ GoldRush.html:1
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] DEBUG: Loading resource Tiles/unlocks.json
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] DEBUG: Initialize tilemap
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] DEBUG: Loading resource Sprites/TileSet.xml
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] DEBUG: Loading resource Sprites/Textures/tileset.png
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] DEBUG: Spritesheet loaded.
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] DEBUG: Loading resource Tiles/menugroups.json
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] DEBUG: Loading resource Textures/buttons.png
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] INFO: UnitBuildMenu::Build
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] DEBUG: Font face BlueHighway (36pt) has 395 glyphs
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] INFO: Read gold counter info.
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] INFO: Read ticks and map info.
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] INFO: Generate map.
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] INFO: Generate random map.
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] INFO: Clear up gold counter.
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] INFO: Reset upgrade levels.
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] INFO: Build the map.
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] DEBUG: Loading resource Models/Tile15.mdl
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] DEBUG: Loading resource Materials/groundtextures.xml
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] DEBUG: Loading resource Techniques/Diff.xml
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] DEBUG: Loading resource Textures/groundtextures.png
    GoldRush.html:1 [Sun Jan 26 18:24:16 2020] DEBUG: Loading resource Models/Tile2.mdl
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Loading resource Models/Tile1.mdl
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Loading resource Models/Tile0.mdl
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Loading resource Lighting/twilight.json
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] INFO: Find water-adjacent tiles.
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] INFO: Done.
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] INFO: Read various systems and tile map.
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: a1
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] INFO: Enabled tiles.
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] INFO: UnitBuildMenu::Build
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] INFO: Read saved time data.
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] INFO: Succesfully loaded save.
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Reloading shaders
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Loading resource Shaders/GLSL/Shadow.glsl
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Loading resource Shaders/GLSL/LitSolid.glsl
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Allocated scratch buffer with size 38496
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Allocated new screen buffer size 1024x1024 format 33189
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Compiled vertex shader Shadow(INSTANCED)
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Compiled pixel shader Shadow()
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Linked vertex shader Shadow(INSTANCED) and pixel shader Shadow()
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Compiled vertex shader LitSolid(DIRLIGHT INSTANCED PERPIXEL SHADOW)
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Compiled pixel shader LitSolid(AMBIENT DIFFMAP DIRLIGHT PCF_SHADOW PERPIXEL SHADOW)
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Linked vertex shader LitSolid(DIRLIGHT INSTANCED PERPIXEL SHADOW) and pixel shader LitSolid(AMBIENT DIFFMAP DIRLIGHT PCF_SHADOW PERPIXEL SHADOW)
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Compiled vertex shader LitSolid(DIRLIGHT INSTANCED PERPIXEL)
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Compiled pixel shader LitSolid(DIFFMAP DIRLIGHT PERPIXEL)
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Linked vertex shader LitSolid(DIRLIGHT INSTANCED PERPIXEL) and pixel shader LitSolid(DIFFMAP DIRLIGHT PERPIXEL)
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Loading resource Shaders/GLSL/Basic.glsl
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Compiled vertex shader Basic(DIFFMAP VERTEXCOLOR)
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Compiled pixel shader Basic(DIFFMAP VERTEXCOLOR)
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Linked vertex shader Basic(DIFFMAP VERTEXCOLOR) and pixel shader Basic(DIFFMAP VERTEXCOLOR)
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] INFO: Starting next game state.
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Compiled pixel shader Basic(ALPHAMAP VERTEXCOLOR)
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Linked vertex shader Basic(DIFFMAP VERTEXCOLOR) and pixel shader Basic(ALPHAMAP VERTEXCOLOR)
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Compiled pixel shader Basic(ALPHAMASK DIFFMAP VERTEXCOLOR)
    GoldRush.html:1 [Sun Jan 26 18:24:17 2020] DEBUG: Linked vertex shader Basic(DIFFMAP VERTEXCOLOR) and pixel shader Basic(ALPHAMASK DIFFMAP VERTEXCOLOR)
    GoldRush.html:1 [Sun Jan 26 18:24:18 2020] DEBUG: Loading resource UI/MiniUpgradeBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:18 2020] DEBUG: Loading UI layout UI/MiniUpgradeBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:18 2020] DEBUG: Loading UI layout UI/MiniUpgradeBox.xml
    GoldRush.html:1 [Sun Jan 26 18:24:20 2020] DEBUG: Resized scratch buffer to size 39408
    GoldRush.html:1 [Sun Jan 26 18:24:20 2020] DEBUG: Resized scratch buffer to size 40896
    GoldRush.html:1 [Sun Jan 26 18:24:28 2020] DEBUG: Compiled vertex shader Basic(VERTEXCOLOR)
    GoldRush.html:1 [Sun Jan 26 18:24:28 2020] DEBUG: Compiled pixel shader Basic(VERTEXCOLOR)
    GoldRush.html:1 [Sun Jan 26 18:24:28 2020] DEBUG: Linked vertex shader Basic(VERTEXCOLOR) and pixel shader Basic(VERTEXCOLOR)
    GoldRush.html:1 [Sun Jan 26 18:24:52 2020] DEBUG: Resized scratch buffer to size 45744
    GoldRush.html:1 [Sun Jan 26 18:24:52 2020] DEBUG: Resized instancing buffer to 2048
    GoldRush.html:1 [Sun Jan 26 18:24:52 2020] DEBUG: Resized scratch buffer to size 52272
    GoldRush.html:1 [Sun Jan 26 18:24:52 2020] DEBUG: Resized scratch buffer to size 57552
    GoldRush.html:1 [Sun Jan 26 18:24:52 2020] DEBUG: Resized scratch buffer to size 60528

-------------------------

GoldenThumbs | 2020-01-26 19:26:48 UTC | #11

You're using Mac? How old, because I was fairly certain Apple removed support of OpenGL, not sure if WebGL is included in that but it wouldn't surprise me given how Apple is.

-------------------------

JTippetts1 | 2020-01-26 22:58:26 UTC | #12

Huh, I dont see anything in there to explain it. I've had three other acquaintances try it out on Mac + Chrome and they had no issues, so have no idea what could be going on, other than maybe trying to clear the page cache and reload.

-------------------------

johnnycable | 2020-01-27 16:34:40 UTC | #13

Mojave. OpenGL is deprecated, but present. Don't know WebGL.
Curiously, Safari works fine. 
@JTippetts1 
Tried reloading, no way. Chrome is up to date. Maybe it's some plugin of his...

-------------------------
