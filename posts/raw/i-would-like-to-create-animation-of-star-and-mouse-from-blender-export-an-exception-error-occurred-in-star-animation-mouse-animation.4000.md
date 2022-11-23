kenji | 2018-02-09 11:22:34 UTC | #1

I would like to create animation of Star and Mouse from Blender export.
An exception error occurred in (Star animation + Mouse animation.)

(OK) Star animation, there was no problem.
(OK) Mouse animation.there was no problem.

(NG)(Star animation, + Mouse animation.)

(Exception error)
System.Exception: Can not add animation state to non-master model. You can omit this exception by subscribing to Urho.Application.UnhandledException event and set Handled property to True.
ApplicationOptions: args - w - p "CoreData; Data" - hd - landscape - portrait.


(Part of code)
```
     private async Task CreateScreent()
        {
            //星のアニメーションを作成します。
            var cache01 = ResourceCache;
            model01 = node.CreateComponent<AnimatedModel>();
            //Polyout.mdl
            model01.Model = cache01.GetModel("Models/Polyout01.mdl");
            model01.SetMaterial(cache01.GetMaterial("Materials/Material.xml"));
			//Walk.ani
            Animation Walk01 = cache01.GetAnimation("Models/Walk01.ani");
            run_walk01 = model01.AddAnimationState(Walk01);
            run_walk01.Weight = 0.5f;
            run_walk01.Looped = true;


            //ねずみのアニメーションを作成します。
	  var cache02 = ResourceCache;
            model02 = node.CreateComponent<AnimatedModel>();
            //Polyout.mdl
            model02.Model = cache02.GetModel("Models/Polyout02.mdl");
            model02.SetMaterial(cache02.GetMaterial("Materials/Material.xml"));
			//Walk.ani
            Animation Walk02 =cache02.GetAnimation("Models/Walk02.ani");
            run_walk02 = model02.AddAnimationState(Walk02);
            run_walk02.Weight = 0.5f;
            run_walk02.Looped = true;
	}

        protected override void OnUpdate(float timeStep)
        {

            var model = node?.GetComponent<AnimatedModel>();
            if (model.NumAnimationStates > 0)
            {//アニメーション効果を出します。
                run_walk01.AddTime(timeStep);
                run_walk02.AddTime(timeStep);
            }
        }
```

-------------------------

Eugene | 2018-02-09 11:42:02 UTC | #2

Avoid multiple drawables created over single node.

-------------------------

