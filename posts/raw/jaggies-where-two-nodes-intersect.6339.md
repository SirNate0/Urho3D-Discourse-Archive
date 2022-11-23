btschumy | 2020-08-21 21:15:07 UTC | #1

Once again I come to you all for advice.  In my galaxy visualization, I have various deep sky objects that are implemented as billboards with the FaceCameraMode = FaceCameraMode.RotateXyz.  As I pan around, viewing the galaxy from different angles, the symbols representing the deep sky objects stay facing the camera.

If the deep sky object is close to the plane of the galaxy (which many are), when the orientation is such that the galaxy and the billboard symbol are almost co-planer, I get jaggies where the two objects intersect.

This is really ugly and I need to find a solution if I'm to continue to use Urho3D for this project.  Hopefully there is some magic setting I can use to reduce the jaggies.

This video shows the problem (I've made the deep sky object much bigger here it make the problem more apparent):

https://www.otherwise.com/movies/Urho3D_Jaggies.mp4

Here is how the galaxy and deep sky object is drawn (with different textures of course):
```
<?xml version="1.0" encoding="UTF-8"?>
<material>
    <technique name="Techniques/GalaxyTechnique.xml" />
    <texture unit="diffuse" name="Textures/Galaxy-North.dds" />
    <shader psdefines="ALPHAMASK" />
    <cull value="none" />
</material>
```
```
<technique vs="UnlitParticle" ps="UnlitParticle" vsdefines="VERTEXCOLOR" psdefines="DIFFMAP VERTEXCOLOR">
    <pass name="alpha" depthwrite="true" blend="alpha" />
</technique>
```
The render order is such that the deep sky is drawn before the galaxy.

Any help you can provide would be greatly appreciated.

Bill

-------------------------

JTippetts1 | 2020-08-23 02:26:47 UTC | #2

Looks like Z-fighting. If 2 geometries are very near to co-planar, then math quirks when rasterizing will alternately favor one over the other. It'll be a problem regardless of what engine you use, if you insist on trying to use coplanar or near-coplanar geometry. You could try using Material::SetRenderOrder again to try to control the render order of your objects, though as it only gives you 128 levels of priority it might not really be the ideal solution. You could also try applying a depth bias to one or the other material. But ultimately, you just want to try to avoid the case of coplanar polygons.

-------------------------

btschumy | 2020-08-21 22:29:45 UTC | #3

I've tried playing with the render order and  the deep sky objects need to be rendered before the galaxy so they will show through the translucent galaxy.  I've tried every possible permutation of things and this is as good as I can get.

I will say that somehow Apple's SceneKit handles this just fine.  There is always a nice smooth transition where the objects intersect.  Not sure how they do it.

My fall back is not to implement deep sky objects as billboards but instead as a textured sphere.  This is not ideal.  It will probably be slower to render and getting an appropriate texture might be hard.  Astronomers are used to specific symbols to represent the various categories of deep sky objects.

My second fall back is to try a different engine.  However, UrhoSharp is the only thing I can find that integrates smoothly in a Xamarin app.

Uggh.

-------------------------

btschumy | 2020-08-21 22:58:16 UTC | #4

After reading a bit about z-fighting, I thought I'd see if adjusting the camera's NearClips and FarClip would help.  It seemed like a resolution problem and I had my Near and Far set to almost the maximum.

Reducing the difference does seem to resolve the fighting.  Now I need to experiment to find a range that will work for my particular application.

-------------------------

