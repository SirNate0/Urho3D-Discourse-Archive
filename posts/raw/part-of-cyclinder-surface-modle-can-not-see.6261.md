fanchenxinok | 2020-07-13 01:53:02 UTC | #1

hi all,

i create a nurbs cylinder model without up and down surface in blender. 
in blender i can render a texture on the surface show in the following image:
 ![捕获1|690x278](upload://1sCA8FQA1uw1ZcuO9k3GHOCUSdC.png) 
then i export this modle as cylinder_surface.mdl, and use Urho3D Editor to open it,
and render texture on it, but part of modle can not see(marked with red box):
![捕获2|599x427](upload://3W5S1VGhvRRI2ZxeDaHB7EKkawx.png) 

what can cause this problem? could anyone help me figure out this problem?

best regards!

-------------------------

SirNate0 | 2020-07-13 02:17:16 UTC | #2

You need to disable culling in the material. If I remember correctly, blender by default does not cull back faces. That's less efficient with a typical (closed) models so Urho by default will cull back faces, as that is generally what is desirable for a game model (with exceptions like your model).

-------------------------

fanchenxinok | 2020-07-13 02:48:41 UTC | #3

thanks for your reply, 
yes, if i enable culling in blender, back faces will cull. 
i call material->SetClullMode(CULL_NONE), then fix this problem.

best regards!

-------------------------

