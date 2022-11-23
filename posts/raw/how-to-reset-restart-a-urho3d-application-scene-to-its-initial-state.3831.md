cirosantilli | 2017-12-13 11:03:00 UTC | #1

http s://stackoverflow.com/questions/47729172/how-to-reset-restart-a-urho3d-application-to-its-initial-state

[link is deleted by Admin]

-------------------------

1vanK | 2017-12-09 13:55:59 UTC | #2

save and load from file?

-------------------------

cirosantilli | 2017-12-09 14:11:35 UTC | #3

Thanks, any way to do it without writing to files? Feels unnecessary.

-------------------------

Eugene | 2017-12-09 14:15:12 UTC | #4

Well, _don't_ save and then just load from file. Or save into `XMLFile` if you need saving.

-------------------------

1vanK | 2017-12-09 14:20:28 UTC | #5

```
Save(Serializer& dest)
```
possible serializer can be memory buffer, but at once I do not remember how

-------------------------

cirosantilli | 2017-12-09 14:23:45 UTC | #6

OK, I see `virtual bool Save(Serializer& dest) const override;`, thanks.

Any way that avoids serialization altogether? That would be most elegant.

-------------------------

1vanK | 2017-12-09 14:26:18 UTC | #7

I think you can not just memcpy scene, since it contains many pointers to other objects

-------------------------

Eugene | 2017-12-09 14:32:15 UTC | #8

[quote="cirosantilli, post:6, topic:3831"]
Any way that avoids serialization altogether?
[/quote]

There is no deep copy of the Scene. Actually, such copying brings more problems than benefits because Scene isn't an inert object. It is living on its own. So keeping Scene somewhere just to resore from it later may lead to side effects.

-------------------------

cirosantilli | 2017-12-09 14:40:39 UTC | #9

I feel copying could be avoided in theory since this is the initial state, which I'm setting up step by step in `Start()`.

But I tried naively to call `Start()` and it does not work because the UI becomes repeated.

-------------------------

1vanK | 2017-12-09 14:47:31 UTC | #10

Create new scene and delete old...

-------------------------

Modanung | 2017-12-10 09:18:39 UTC | #11

How about `Scene::Clear()`? This removes all `Component`s and `Node`s from a scene.

[quote="cirosantilli, post:9, topic:3831"]
But I tried naively to call Start() and it does not work because the UI becomes repeated.
[/quote]

As @weitjong said later: You could call `GetSubsystem<UI>()->GetRoot()->RemoveAllChildren() ` to clear the UI.

-------------------------

Eugene | 2017-12-09 14:48:59 UTC | #12

If you want to naively call Start, you should ensure that you reset everything you initialized during previous Start call. Should work.

-------------------------

1vanK | 2017-12-09 15:05:02 UTC | #13

Just remember that recreating/switch of scene should be doing before the handling of any events. 

```
class Game : public Application
{
    URHO3D_OBJECT(Game, Application);

public:
    Game(Context* context) : Application(context)
    {
        SubscribeToEvent(E_BEGINFRAME, URHO3D_HANDLER(Game, ApplyGameState));
```

```
 void ApplyGameState(StringHash eventType, VariantMap& eventData)
    {
        if (GLOBAL->gameState_ != GLOBAL->neededGameState_)
        {
             GLOBAL->gameState_ = GLOBAL->neededGameState_;
             DoSomething();
        }

        if (GLOBAL->currentLevelIndex_ != GLOBAL->neededLevelIndex_)
        {
            GLOBAL->currentLevelIndex_ = GLOBAL->neededLevelIndex_;
            StartLevel(GLOBAL->currentLevelIndex_);
        }
    }
```

-------------------------

johnnycable | 2017-12-09 15:29:10 UTC | #14

You have to manage changing scene and its data by application-dependent specific class or data store.
Uhro can manage your scene graphically, but if you need to restart over a level you have to use a level manager

-------------------------

cirosantilli | 2017-12-10 00:33:11 UTC | #15

Thanks, I was kind of hoping that there would be a `Clear()` like method for the whole application (in particular, the `UI` does not get reset with `Scene->Clear`, but this solution is acceptable to me.

-------------------------

weitjong | 2017-12-10 01:30:16 UTC | #16

The UI (and usually also the Camera) is not part of the Scene, so calling scene's clear would not clear the UI (and camera). You can clear the UI by removing all the children of the root UI element. Assuming "ui" is your UI subsystem singleton object then calling `ui->GetRoot()->RemoveAllChildren()` should work.

-------------------------

artgolf1000 | 2017-12-11 00:39:09 UTC | #17

I had written a level manager: https://discourse.urho3d.io/t/levels-fade-effect/2257, which can switch levels dynamically.

-------------------------

weitjong | 2017-12-13 11:45:29 UTC | #18



-------------------------

