najak3d | 2021-03-01 00:04:13 UTC | #1

Our app uses a tiled map presentation, where we define "danger" colors for the terrain based upon a dynamic elevation setting.  (e.g. everything above 2000' will show RED, but this 2000' is a global setting that changes rapidly at run-time).

We're trying to avoid the load of rapidly setting this Shader parameter for every instance of the Material in our scene.   Ideally, we set it ONCE and all of the materials just see it automatically.

Is this possible with Urho3D?

-------------------------

JSandusky | 2021-03-02 02:27:19 UTC | #2

In the most minimal sense that isn't possible as Materials don't manage constant state. During the batch loop they pump their parameters into the constant-buffers that `Graphics` manages.

You could add a bulk set like `static void Material::SetShaderParameterInBulk(const Vector<SharedPtr<Material> >& materials, const String& name, const Variant& value)` to tightly loop through them first to set the value directly and again to do the parameter-hash and memory size updates on each of them. C++ side that probably won't have any major wins, but from script (be it As, Lua, or C#) it'll be more significant because of less marshaling.

That's as close as you could there without the larger amount of work required to to add cbuffer management into materials. Since they'd be working with their own private custom-params cbuffer in that case there wouldn't be any wins to be had that way anyways as you couldn't really "inherit" that in a fashion that wouldn't just trigger a heap of calls in another fashion (like an event).

-------------------------

Bananaft | 2021-03-12 19:19:45 UTC | #3

Yes, its trivial! You just add a new uniform. Check how other uniforms are set in View.cpp. PSP_DELTATIME for example.

-------------------------

JSandusky | 2021-03-13 04:08:13 UTC | #4

There are caveats with that because the batch loop is going to steam roll over a lot of that (it won't steamroll over stuff you've crammed into odd places that aren't per draw) while it sources parameters from the materials.

It does apply though if you're doing explicit rendering from an event in the renderpath though.

-------------------------

