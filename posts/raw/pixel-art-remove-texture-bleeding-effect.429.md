scorvi | 2017-01-02 01:00:21 UTC | #1

hey 
so i am programming a pixel art game and just could not find a way to remove the texture bleeding effect ... 
i thought with the parameter <quality low="0" /> the texture filter was set also to nearest  but i thought wrong :-/ 

so here is xml file for a pixel art texture:
[code]<texture>
  <filter mode="nearest" />
<mipmap enable="false" />
<quality low="0" />
</texture>
[/code]

[b]Before:[/b]
[spoiler][img]http://i.imgur.com/FIsTifD.png[/img][/spoiler]
[b]After:[/b]
[spoiler][img]http://i.imgur.com/xBbNH6x.png[/img][/spoiler]

-------------------------

gunnar.kriik | 2017-01-02 01:00:21 UTC | #2

Hi,

What you're referring to as texture bleeding, is known as "texture filtering". The texture "bleeding" effect is because multiple texels are sampled (bilinear, trilinear filtering) at one point to combine the output color. "Nearest" means that it only samples one color, whatever is the closest to match. 

You probably still want to enable mipmapping though, but if it's a 2D game then it probably doesn't matter.

-------------------------

setzer22 | 2017-01-02 01:00:21 UTC | #3

Thanks! It was kind of tricky to figure this out myself as a newbie (I still am  :smiley: ), so I think this will help many people out there.

-------------------------

