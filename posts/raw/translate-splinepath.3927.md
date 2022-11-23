George1 | 2018-01-09 17:03:23 UTC | #1

Hi there! Is there an efficient way to translate SplinePath?

At the moment I have to create a new function inside SplinePath for this.

void SplinePath::TranslatePath(const Vector3 &v)
{
	for (unsigned i = 0; i < controlPoints_.Size(); ++i)
	{
		Vector3 pos = controlPoints_[i]->GetWorldPosition() + v;
		controlPoints_[i]->SetWorldPosition(pos);
	}
}

Why don't we make controlpoints the child of the node where this component is added to.
This way we just need to move the parent node and everything moves with it.

Also, I have tested translate 50 ControlPoints of the SplinePath and I found that it is very slow to update. In my test I can translate 5000 none spline controlpoint nodes faster than that of 50 ControlPoints in the SplinePath.

regards

-------------------------

Modanung | 2018-01-10 10:53:47 UTC | #2

As confirmatory nitpicking, I'd rewrite your function as such:
```
void SplinePath::TranslatePath(const Vector3& delta, TransformSpace space = TS_WORLD)
{
     for (WeakPtr<Node> node: controlPoints_) {

          node->Translate(delta, space);
     }
}
```

-------------------------

George1 | 2018-01-10 03:52:08 UTC | #3

Thanks Modanung,
I rarely use foreach. But that's pretty compact. Do you think there is a performance reduction in that translate function?

I have tested for CATMULL_ROM_FULL_CURVE.

Also, the debug line seems to be edgy if we have lots of nodes. See pic.

![image|547x500](upload://1D7DQhFK8WPkTDuHY48wfgtgLhO.png)

![image|402x500](upload://jf98YS3uFro43NYPkrm2h8YfF6M.png)

Best regards

-------------------------

Modanung | 2018-01-10 17:18:49 UTC | #4

How do you create the spheres? Could _they_ by any chance be offset?

-------------------------

George1 | 2018-01-10 23:51:49 UTC | #5

Sphere is created by adding control point to SplinePath directly.
After more than 20 nodes. The debug line reduce accuracy. Maybe there is a limited in the number of line segments used in the debug code.

regards

-------------------------

George1 | 2018-01-12 06:28:36 UTC | #6

Instead of adding a TranslatePath function. I recommend to expose the control points. Through GetControlPoints()

This way we could translate or do what ever with it without touch core.

Best regards

-------------------------

George1 | 2018-01-17 07:22:49 UTC | #7

The translation of SplinePath node for non linear spline is quite slow.
See small comparision pictures.

![test|421x327](upload://1GI8N8DY05yZmU3reoNPrZnu0iG.gif)

![test2|421x327](upload://kgVxY0Uo5bfXGsrm0H9aiexkho8.gif)

-------------------------

Modanung | 2018-01-17 09:45:11 UTC | #8

Does this hold true when not drawing debug geometry?

-------------------------

George1 | 2018-01-17 10:42:47 UTC | #9

Yes, it also slow without debug lines.
I think there maybe some sort internal code that do a deep update every frame when we move the path.
I'm not too sure, as I linked the lib. so I can't debug into it.

Best regards

-------------------------

Eugene | 2018-01-17 15:06:02 UTC | #10

Probably `SplinePath::OnMarkedDirty` cause lags because `CalculateLength` is quite heavy.

-------------------------

George1 | 2018-01-18 14:51:09 UTC | #11

Thanks Eugene!
Is it possible to temporary disable mark dirty and re-enable (call) when we need it?

We could e.g have a flag in that OnMarkedDirty function.

Or is there an existing global flag that I can used?

Thanks

-------------------------

George1 | 2018-01-18 17:46:26 UTC | #12

Thanks,
I've comment out CalculateLength in OnMarkedDirty. 
Make CalculateLength() public and calls it when I translate the SplinePath
```
void SplinePath::OnMarkedDirty(Node* point)
{

    if (!point)
        return;

    WeakPtr<Node> controlPoint(point);

    for (unsigned i = 0; i < controlPoints_.Size(); ++i)
    {
        if (controlPoints_[i] == controlPoint)
        {
            spline_.SetKnot(point->GetWorldPosition(), i);
            break;
        }
    }

   // CalculateLength();
}
```
![test2|523x294](upload://Eh4YoeelIZ8ReAwhBIBE7HsyDn.gif)

-------------------------

