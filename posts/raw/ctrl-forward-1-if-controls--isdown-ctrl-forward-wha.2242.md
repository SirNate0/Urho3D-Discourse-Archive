GnastyGnork | 2017-01-02 01:14:10 UTC | #1

Character.h
[code]const int CTRL_FORWARD = 1;
const int CTRL_BACK = 2;
const int CTRL_LEFT = 4;
const int CTRL_RIGHT = 8;
const int CTRL_JUMP = 16;[/code]

Character.cpp
[code]    if (controls_.IsDown(CTRL_FORWARD))
        moveDir += Vector3::FORWARD;
    if (controls_.IsDown(CTRL_BACK))
        moveDir += Vector3::BACK;
    if (controls_.IsDown(CTRL_LEFT))
        moveDir += Vector3::LEFT;
    if (controls_.IsDown(CTRL_RIGHT))
        moveDir += Vector3::RIGHT;[/code]

I know im a noob but i cant find a correlation between those numbers (1,2,4,8,16) and the keys that i am pressing... 
Also why does the character in the demo move right when i press F1? 

Could someone ELI5 this to me?

-------------------------

1vanK | 2017-01-02 01:14:11 UTC | #2

[code]character_->controls_.Set(CTRL_FORWARD | CTRL_BACK | CTRL_LEFT | CTRL_RIGHT | CTRL_JUMP, false);
character_->controls_.Set(CTRL_FORWARD, input->GetKeyDown(KEY_W));
character_->controls_.Set(CTRL_BACK, input->GetKeyDown(KEY_S));
character_->controls_.Set(CTRL_LEFT, input->GetKeyDown(KEY_A));
character_->controls_.Set(CTRL_RIGHT, input->GetKeyDown(KEY_D));
[/code]

-------------------------

JTippetts | 2017-01-02 01:14:11 UTC | #3

The numbers 1,2,4,8,etc... denote bits in an integer variable stored by controls. They mean whatever you need them to mean. As 1vanK indicated, you can query the status of your chosen key and set the particular bit flag either true or false, depending on the state of the key. 1 means the first bit, 2 means the second bit, 4 is the third, 8 is the fourth, and so on. Adding these numbers together, or using the operator | (bitwise OR operator) creates a composite value indicating the state of all controls, packed into an integer representation for compactness.

-------------------------

