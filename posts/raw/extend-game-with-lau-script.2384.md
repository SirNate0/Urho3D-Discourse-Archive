shipiz | 2017-01-02 01:15:05 UTC | #1

Hi everyone,

I'm currently writing a game in c++, so i would like to add option for external mods which would basically extend the data model of the game with new items. Although i'm unable to figure it out how to just have lua tables that hold that and could be loaded into c++, parsed and populate in game objects. Of course core game data would be written in lua also. 

for example i imagined lua script to be something like this which doesn't have any logic just the plain data
[code]
data =
{
            name = entity_name,
            type = entity_type,
            properties = {
                property1 = 1,
            }
}
[/code]

Essentially most of the lua scripts will just be tables that contain data about the game, and game logic will be written in c++. I would add later option to extend the entities by providing your own logic.

I went through the source code of lua scripts, but couldnt figure out how to load lua table into c++ and read the data from it. Does urho supports something like that at all? since most of the examples are instantiating objects which are defined in lua and attaching them as a components ?

-------------------------

Eugene | 2017-01-02 01:15:06 UTC | #2

What's the point of script that is not actually a script but just data? Urho don't support 'backward' data transfrerring from script to engine because it's misuse of scripts. Why not to store data in more appropriate format?

-------------------------

shipiz | 2017-01-02 01:15:06 UTC | #3

I'm not sure what is the right choice, i was thinking to use json as a data store which can be easily modified/added. Basically idea is to have game logic written in c++, and lua to be used for entity logic and as data that describes each entity. for example:

lets say i have a spaceship. there could be multiple spaceships, so the idea is to have them described in lua table (like, texture, model, capacity, hulls/shields, speed etc.), now most of the spaceships will use the same lua script which will do something when simulation starts, but i would also like to add option for user to create his own logic for a particular spaceship and extend spaceship data with new ships which he can use ingame.

-------------------------

