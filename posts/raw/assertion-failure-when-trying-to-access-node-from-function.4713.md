sherb3t | 2018-12-08 15:30:27 UTC | #1

The node is as a public SharedPtr

Here is the function:

    int getPlayerPos(int comp) {
		Vector3 playerPos = playerNode_->GetWorldPosition();

		if (comp) {
			return round(playerPos.z_ / 6);
		}
		else {
			return round(playerPos.x_ / 6);
		}
	}

The function is called within HandleUpdate(). If you need more code just ask.

-------------------------

rku | 2018-12-10 13:00:44 UTC | #2

`playerNode_` is probably empty (null). Make it not null.

-------------------------

Modanung | 2018-12-11 10:08:03 UTC | #3

Or check whether the `playerNode_` is null. If it is, avoid accessing its members and methods.

Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

sherb3t | 2018-12-12 09:06:59 UTC | #4

I do not believe that the node is null. Running this code within the Start() function causes no problems:

> Vector3 playerPos = playerNode_->GetWorldPosition();

-------------------------

rku | 2018-12-12 09:46:03 UTC | #5

Do not believe. Debug.

-------------------------

Modanung | 2018-12-12 10:13:22 UTC | #6

@sherb3t Try adding `assert(playerNode_);` before you otherwise use the pointer and see if the assertion fails.

-------------------------

sherb3t | 2018-12-12 10:29:22 UTC | #7

Still fails. Thanks for the help.

-------------------------

Modanung | 2018-12-12 10:38:47 UTC | #8

If the pointer is null the assertion _should_ indeed fail.

-------------------------

sherb3t | 2018-12-12 11:20:33 UTC | #9

How do I check if it's null. I'm pretty sure it isn't because I'm using it no problem in the start function...

-------------------------

sherb3t | 2018-12-12 11:26:59 UTC | #11

The pointer is infact null when accessed from the function. When I try and check in the Start() function I get an error with this code:

> if (playerNode_.Null()) {
			std::cout << "yes its null \n";
		}

The error is "expression must have a class type".

-------------------------

