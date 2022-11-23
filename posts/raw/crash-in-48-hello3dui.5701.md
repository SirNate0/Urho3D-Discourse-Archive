stefandd | 2019-11-03 11:39:07 UTC | #1

Hello everyone, this is my firs posting here.

In the current revision of the engine, no matter if built for D3D9, GL3, or D3D11, the 
48_Hello3DUI.lua example crashes. The crash is caused by the line: "    textureRoot = component.root"
in Init3DUI().

I tinkered with the code a bit and get it to not crash (but without proper texture rendering on the spinning cube) by either commenting the line out or by replacing "local component = boxNode:CreateComponent("UIComponent")" in the same function with "local component = boxNode:CreateComponent("UIComponent"):New()"
This makes me believe it is related to the pkg definition of UIComponent and the TOLUA defines there, but I know way too little about the engine to make any progress.

Could someone make the sample run again?

-------------------------

Modanung | 2019-11-03 11:42:08 UTC | #2

Could you open an issue for this on GitHub and link it to this topic?

Also, welcome to the forums! :confetti_ball:

-------------------------

weitjong | 2019-11-03 15:12:14 UTC | #3

I got it working by adding these lines to the `UIComponent.pkg` file. Tested on Linux platform. I don't think it was able to run correctly before.

```
 git diff Source/Urho3D/LuaScript/pkgs/UI/UIComponent.pkg
diff --git a/Source/Urho3D/LuaScript/pkgs/UI/UIComponent.pkg b/Source/Urho3D/LuaScript/pkgs/UI/UIComponent.pkg
index 5a838992a7..488480591a 100644
--- a/Source/Urho3D/LuaScript/pkgs/UI/UIComponent.pkg
+++ b/Source/Urho3D/LuaScript/pkgs/UI/UIComponent.pkg
@@ -5,6 +5,10 @@ $#include "Graphics/Material.h"
 $#include "Graphics/Texture2D.h"
 $#include "Graphics/StaticModel.h"
 
+class UIElement3D : public UIElement
+{
+}
+
 class UIComponent : public Component
 {
     UIComponent();
```

Let me know if this change fixes your problem too.

-------------------------

stefandd | 2019-11-03 15:16:18 UTC | #4

Yes, this fixed it. I also opened an issue on Github as requested.

Another quick question to @weitjong and @Modanung -- I have made some patches to be able to use the latest Luajit 2.1beta3 by carefully migrating the changes made in Urho3d to the previous beta2. These changes seem to work stably and I have worked with them for weeks now (on a Lua project). Would one of you be willing to help proposing these as a pull request. Unfortunately, I am highly inexperienced with git and do not know how to correctly do this.

-------------------------

weitjong | 2019-11-03 17:53:39 UTC | #5

Thanks for the confirmation. In that case I will commit my change to the master branch later. As for upgrading LuaJIT, what difference it will make?

-------------------------

stefandd | 2019-11-03 19:02:41 UTC | #6

I think beta 3 offers the option to use a fully 64-bit garbage collection (by compilation switch) and no more 2G memory limit on the Lua side

-------------------------

weitjong | 2019-11-04 03:53:46 UTC | #7

OK. It may be worth while to have it upgraded then.

We have a fork of LuaJIT repo in our own Urho3D GitHub organization which has a tracking branch that contains all the bits from beta-2 plus the accumulated of our local changes on top of it over the years. The Urho3D project repo has treated LuaJIT as a git subtree. The official way to upgrade the LuaJIT is to rebase that tracking branch in the LuaJIT repo to beta-3 and then git subtree pull the bits over to Urho3D main repo.

-------------------------

