George1 | 2020-05-13 09:49:18 UTC | #1

Hi Guys,
I'm using new exporter from 1vanka branch to export imported obj file.

The model and texture are exported fine.  The material file has problem exporting.

I get an error in exporting material file like below using both eeve and cycle renderers.

![image|690x265](upload://zRWJse0HXYdOKfDy8lNjPoCzqNt.png)

-------------------------

1vanK | 2020-05-13 09:48:42 UTC | #2

You can not use any material. You need clone and tune predefined materials as shown on video https://discourse.urho3d.io/t/exporting-materials-from-blender-2-83-to-urho3d/5845

-------------------------

George1 | 2020-05-13 09:22:19 UTC | #3

I see, is this always the case with existing exporter?

Thanks I'll check the other video out.

-------------------------

1vanK | 2020-05-13 09:31:34 UTC | #4

Converting ANY cycles shader node tree required generating Urho's shader on the fly. In Urho we have 3 predefined shaders, so in Blender you need use predefined materials wich corresponds to existed Urho'S shaders.

-------------------------

George1 | 2020-05-13 09:41:06 UTC | #5

I see, because I was using the Principled BSDF material. We don't have that.

Sorry, I never have to deal with shader, so my knowledge is limitted.  But which three shaders are you referred to.   LitSolid, PBRLitSolid, Basic or BRDF.

Thanks

-------------------------

1vanK | 2020-05-13 09:44:24 UTC | #6

LitSolid, Unlit, PBR

-------------------------

