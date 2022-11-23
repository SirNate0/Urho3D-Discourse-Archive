TheComet | 2017-01-02 01:10:21 UTC | #1

I have a model of a dog and it loops a walk animation. I'd like to procedurally bend his spine when he turns corners. What's the best way to apply a rotation to a bone [b]after[/b] the walk animation has been applied?

-------------------------

Dave82 | 2017-01-02 01:10:21 UTC | #2

Subscibe to the E_SCENEDRAWABLEUPDATEFINISHED and update your bones there.Please note this function is called after the scene update so if you disable scene updates (scene->SetUpdateEnabled(false))
E_SCENEDRAWABLEUPDATEFINISHED is still sent and processed

-------------------------

weitjong | 2017-01-02 01:10:21 UTC | #3

If you want precise control on when it needs to be triggered, you may want to use animation triggering point. That can be declared in the animation XML file.

-------------------------

TheComet | 2017-01-02 01:10:22 UTC | #4

Perfect, thanks!

-------------------------

