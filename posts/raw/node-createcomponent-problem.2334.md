trillian | 2017-01-02 01:14:48 UTC | #1

Hi,

I may be totally wrong, I just started to use this engine, and my C++ skills are a bit rusty (especially when it comes to templates).

My Class hierarchy:

[code]Character : public LogicComponent  // Taken from the character demo
 - Player : public Character
 - NonPlayer : public Character[/code]

I register first the Player class with [code]context->RegisterFactory<Player>()[/code], and then do the same with NonPlayer. I [i]don't[/i] register the Character class.

When I instantiate the player with [code]player_ = objectNode->CreateComponent<Player>();[/code] I get an instance of NonPlayer instead of Player.

When I just register Player, but not NonPlayer, everything is fine and I get an instance of Player. Maybe there is some problem with RTTI when the two classes inherits from the same Superclass.

I could investigate it further, but I find templates hard to debug, and maybe this system is not supposed to be used this way, and I should change my approach completely. So I thought I ask first  :smiley: .

Anyway, awesome Engine!

-------------------------

1vanK | 2017-01-02 01:14:48 UTC | #2

Mya be you forgor to change URHO3D_OBJECT(class_name, base_class_name);

-------------------------

trillian | 2017-01-02 01:14:48 UTC | #3

Oh so easy  :astonished: . Thank you, that solved the problem.

-------------------------

