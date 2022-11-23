megapunchself | 2018-08-03 02:09:32 UTC | #1

some games and engines are using rgb/rgby tint/texture mask to create a "customize" system for players change character's colors and after be storaged in a server or game data

i just realized that the albedo is gray, the models got normal map, spec, emission n metalic/metalness texture

unreal and unity got tutorial in docs and wikis, a game example of use this is warframe (evolution engine, peoples are saying dat is c++)

it is just a shader with a script to modify? it is working o urho3d? how it works on urho3d?

i don't know if i can post links but, here is the example and a tutorial video "how it works on the evolution engine (warframe)", i suppose use 2 textures for it? a rgb texture and the alpha texture (video last minutes on gimp)?:

https://www.youtube.com/watch?v=lNBCezMYgr0

https://polycount.com/discussion/160512/warframe-tennogen-contest-final-submissions

- the color changer will change each rgby color

-------------------------

Bananaft | 2018-08-04 12:06:56 UTC | #2

Hello. Welcome to the forum!

You don't need C++ to do that in urho. In LitSolid.glsl shader add something like:

             #ifdef COLORTEX
                diffColor.rgb *= texture2D(sEmissiveMap, vTexCoord2).rgb;
            #endif
Then copy any technique, DiffNormal for example, name it DiffNormalColortex and add COLORTEX as psdefine in it.

Now you can create material with this technique and set your coloring texture into Emissive slot.

-------------------------

megapunchself | 2018-08-03 22:11:21 UTC | #3

nice! thx for the code!  xD
but- for example, if i'll use the "emissive" slot, how can i put a emissive/emission texture glow with this technique?
can I change the "...ure2D(**sEmissiveMap**, vTex..." for other and it still working? or i need code something (or a new) in the glsl and material technique, just like a new slot? two emissive slots?

but anyway, tyvm!! ^^

-------------------------

Bananaft | 2018-08-04 12:06:56 UTC | #4

yeah, you can use any texture slot you want.

Oh, and I jsut realized, there are custom1 and custom2 slots, but I'm not sure how to use them since they are not mentioned in Samplers.glsl or OGLGraphics.cpp

-------------------------

