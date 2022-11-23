Bananaft | 2017-09-26 21:18:01 UTC | #1

It would be cool to be able to slap some decals on the level or model and save it to xml.

As I see it: you add DecalSet to your model, then add a child node and add actual decal component to it. Then you can set the size, material, and drag it around. This component will remove and add again a decal on every parameter or transform change. Once level or object is loaded this components and child nodes can be removed.

What do you guys think on feature in general and proposed solution in particular?

-------------------------

hdunderscore | 2017-09-27 10:25:23 UTC | #2

I've done something similar using angelscript scripts, although a bit rough around the edges. I think using angelscript to add level-editor components is a pretty solid strategy, but more something that fits in the community repo when that gets going.

-------------------------

Bananaft | 2017-09-27 11:18:49 UTC | #3

Can you share your work? Even If it is half broken, I want to see it, because I'm thinking about making it myself.

-------------------------

hdunderscore | 2017-09-28 08:23:02 UTC | #4

Sure, it's even cruder than I remember:

    const StringHash EVENT_START("Start");
    const StringHash EVENT_DELAYEDSTART("DelayedStart");
    const StringHash EVENT_NODEPOSITIONUPDATE("NodePositionUpdate");
    const StringHash EVENT_COMPONENTENABLEDCHANGED("ComponentEnabledChanged");

    class DecalSphere: ScriptObject
    {
      float Radius = 1.0;
      float Depth = 1.0;
      Vector3 OffsetPosition = Vector3(0,0,0);
      private float updateRate = 0.1;
      private bool updated = true;
      private float updateTimer = 0.0;
      private Vector3 lastPos;
      private Vector3 lastOffsetPosition;
      private float lastRadius;
      private float lastDepth;
      private Quaternion lastRotation;

      void Start()
      {
        SubscribeToEvent("ComponentEnabledChanged", "Run");
        SubscribeToEvent("SceneUpdate", "NodeUpdate");
        lastPos = node.position;
        lastRotation = node.rotation;
        lastRadius = Radius;
        lastDepth = Depth;
        lastOffsetPosition = OffsetPosition;
      }

      void NodeUpdate(StringHash eventType, VariantMap& eventData)
      {
        float timeStep = eventData["TimeStep"].GetFloat();

        updateTimer += timeStep;
        if (!lastRotation.Equals(node.rotation) || !lastPos.Equals(node.position) || Abs(lastRadius - Radius) > 0.001 || Abs(lastDepth - Depth) > 0.001 || !lastOffsetPosition.Equals(OffsetPosition))
        {
          updated = false;
        }

        if (!updated && updateTimer >= updateRate)
        {
          Print("ASD");
          updateTimer = 0.0f;
          updated = true;
          lastPos = node.position;
          lastRotation = node.rotation;
          lastRadius = Radius;
          lastDepth = Depth;
          lastOffsetPosition = OffsetPosition;
          Run(EVENT_NODEPOSITIONUPDATE, VariantMap());
          Print("ZSD");
        }
      }

      void Run(StringHash eventType, VariantMap& eventData)
      {
        if (eventType == EVENT_COMPONENTENABLEDCHANGED)
        {
          if (eventData["Node"].GetPtr() !is node)
            return;

          if (eventData["Component"].GetPtr() !is node.GetComponent("ScriptInstance"))
            return;
        }

        node.position -= OffsetPosition;
        Sphere sphere;
        sphere.Define(node.position , Radius);
        Drawable@[]@ drawables = octree.GetDrawables(sphere, DRAWABLE_GEOMETRY, 127);
        Print(drawables.length);

        DecalSet@ decals = node.GetComponent("DecalSet");
        decals.RemoveAllDecals();
        for (uint i = 0; i < drawables.length; ++i)
        {
          if (drawables[i] is decals)
            continue;
          Print(drawables[i].typeName);
          decals.AddDecal(drawables[i], node.position, node.rotation, Radius, 1.0f, Depth, Vector2(0,0), Vector2(1,1), 0.0f, 0.1f);
        }
        node.position += OffsetPosition;
        Print(decals.numDecals);
      }
    }

-------------------------

