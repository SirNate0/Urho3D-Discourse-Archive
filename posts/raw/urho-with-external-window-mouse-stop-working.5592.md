Elendil | 2019-09-17 22:17:12 UTC | #1

When I use Urho with external window, mouse stop working. I am not sure why, but I guess external window not send mouse in to urho?

Keyboard is working. I use WPF as external window, therefore if you know Windows only solution it never mind.

-------------------------

Elendil | 2019-09-19 10:48:16 UTC | #2

I found solution. I use Urho example from wikipedia and there is

    if (!GetSubsystem<Input>()->IsMouseVisible()) { ... }

I only guess, if Urho use external window, `GetSubsystem<Input>()->IsMouseVisible()` is allways true and therefore code inside this `if` never happens. Therefore changing under Urho MouseVisibility never go false.

-------------------------

