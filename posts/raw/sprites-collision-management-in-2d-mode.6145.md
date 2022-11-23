zedraken | 2020-05-09 12:56:57 UTC | #1

Hello all,

I am currently experimenting collision detection of sprites in Urho2D. To do that, I have create a wall and a tennis ball as shown on the picture below:

![collisions_urho2D|638x500](upload://vi9e7OaSFcevul4L2W5JhPV2VAV.png) 

I can control the ball movement using the key pad (left, right, down and up) and I move the ball until it collides with the wall. I do not want to rely on any physics for ball movement (like gravity for example). 

In my code, I have connected the events E_PHYSICSBEGINCONTACT2D and E_PHYSICSENDCONTACT2D to detect when the collision begins and when it ends.

I do not want the ball to go through the wall, consequently this means that when I press the down key to move the ball toward the wall, the first thing I do before actually moving it is to store its current position. Then I apply the ball movement like this:

    void TestSprite::HandleUpdate(StringHash eventType, VariantMap& eventData)
    {
        using namespace Update;
        float time_step = eventData[P_TIMESTEP].GetFloat();

        mPreviousPosition = mBallNode->GetPosition2D();
        switch(mDirection)
        {
            case DOWN:
                mBallNode->SetPosition2D(mPreviousPosition + Vector2(0.0f, -mSpeed * time_step));
            break;
            case UP:
                mBallNode->SetPosition2D(mPreviousPosition + Vector2(0.0f, mSpeed * time_step));
            break;
            case LEFT:
                mBallNode->SetPosition2D(mPreviousPosition + Vector2(-mSpeed * time_step, 0.0f));
            break;
            case RIGHT:
                mBallNode->SetPosition2D(mPreviousPosition + Vector2(mSpeed * time_step, 0.0f));
            break;
        }
    }

I apply an offset to the stored position (the current one) using a specific speed and this gives the new ball position.

Then, when I detect the start of a collision (event E_PHYSICSBEGINCONTACT2D), this means that obviously the ball has hit the wall. In that case, I move the ball back to the previously stored position.

    void TestSprite::BeginCollision(StringHash eventType, VariantMap& eventData)
    {
        mBallNode->SetPosition2D(mPreviousPosition);
    }

The ball is moved back so it cannot "enter" into the wall.

However, from that point, if I move the ball down again, then no more E_PHYSICSBEGINCONTACT2D event is triggered and the ball can cross the wall.

I have observed that I do not have any E_PHYSICSENDCONTACT2D event meaning that the engine did not detect the end of the collision. I assume this is why it does not detect any new collision.

My question is if it is possible to reset the collision state or something like that in such a way that when I move the ball back to its previous position (just before the collision), then the engine is able to detect a new collision.

Or is there any other way or algorithm to avoid having the ball going through the wall ?

Maybe someone has already implemented that behavior and can give me some tips, that will be greatly appreciated :slight_smile:

Thanks!

Charles

-------------------------

zedraken | 2020-05-07 19:38:59 UTC | #2

I had a look at the file "Urho2D/PhysicsWorld2D.h" and I found the "Raycast(…)" function. Maybe I have to do a raycasting in the direction of the movement to see if there will be a collision event ?

-------------------------

zedraken | 2020-05-09 07:56:18 UTC | #3

Hello,

I keep trying to solve my issue and maybe what I describe below will be of any help for anybody :slight_smile: 

I have modified the way to detect collisions by relying on the raycast functionalities.
I first removed my E_PHYSICSBEGINCONTACT2D and E_PHYSICSENDCONTACT2D handlers, meaning that collisions are no more managed using handlers.

In the E_UPDATE handler, I check for any key press and in such a case, I compute the new ball position. Then, using that position, I raycast in the displacement direction (down if I press the KEY_DOWN). If the raycast does not return any hit (no collision), then I move the ball as usual with its own speed. Otherwise, if there is a hit, then I move the ball to the position of the collision point minus a small offset.
Here is the code…

     …
     ballPos = mBallNode->GetPosition2D();

     if(input->GetKeyDown(KEY_DOWN))
        {
            // set direction vector to down
            Vector2 direction = Vector2::DOWN;

            // compute new position as if there is no obstacle
            newPosition = ballPos + direction * mSpeed * time_step;
            
            // raycast in the displacement direction
            PhysicsRaycastResult2D castResult;
            mScene->GetComponent<PhysicsWorld2D>()->RaycastSingle(castResult, ballPos, newPosition, M_MAX_UNSIGNED);
            if(castResult.body_ == NULL)
            {
              // no collision, move the ball to its new position
              mBallNode->SetPosition2D(newPosition);
            }
            else
            {
              // collision… Set new ball position to collision point
              mBallNode->SetPosition2D(castResult.position_ - direction * castResult.distance_);
            }
        }

The results are quite encouraging and at some point, the ball does not go through the wall, but the raycast detect a collision after the ball has overlapped a little bit the wall like it is shown on the picture below…

![Test sprites with Urho2D (800x600)_093|638x500](upload://rLU5wYSmXEcICKX8XtQj9BjWrTi.png) 

The ball will not go further through the wall but the result is not exactly the expected one. Of course I could adjust the collision shape dimension but I am wondering if there is a clean way to solve that small issue ?

Thanks!

-------------------------

Modanung | 2020-05-09 11:54:49 UTC | #4

You may want to have a look at sample 50. Just as with 3D physics, one should *apply forces* to physics objects instead of "teleporting" them around by setting their position.

-------------------------

zedraken | 2020-05-21 10:04:08 UTC | #5

Hi all, I am back with some delay :slight_smile:
Anyway, I was able to solve my small issue. I took into account the Modanung advice, i.e. let the physic engine handle collision and ball position.
Now, I do not explicitly change  the ball position by using the "SetPosition2D" function.
Instead, I just apply a velocity to the ball rigid body associated component depending on the arrow key on which I am pressing.
Here is the code snippet I wrote into the E_UPDATE event handler:

>     void TestSprite::HandleUpdate(StringHash eventType, VariantMap& eventData)
>     {
>         using namespace Update;
>         float time_step = eventData[P_TIMESTEP].GetFloat();
>         Input* input = GetSubsystem<Input>();
>         Vector2 direction = Vector2::ZERO;
> 
>         mBallNode->GetComponent<RigidBody2D>()->SetLinearVelocity(Vector2::ZERO);
> 
>         // Set velocity vector depending on the pressed key.
>         if(input->GetKeyDown(KEY_DOWN)) {
>             direction.y_ = -mSpeed;
>         } else if(input->GetKeyDown(KEY_UP)) {
>             direction.y_ = mSpeed;
>         }
>         if(input->GetKeyDown(KEY_LEFT)) {
>             direction.x_ = -mSpeed;
>         } else if(input->GetKeyDown(KEY_RIGHT)) {
>             direction.x_ = mSpeed;
>         }
> 
>         // Set the ball velocity
>         mBallNode->GetComponent<RigidBody2D>()->SetLinearVelocity(direction);
>     }

The first thing I do is to set to zero the ball velocity.

Then, depending on the arrow key, I update the x or y component of a Vector2 variable accordingly. For example, if I press the down key (or up key), then I update the y_ part of the vector.
I do the same for the left or right keys and the result is a combination of two displacements, one on each axis. So it is possible to move up and right at the same time for example.

Then I apply that resulting vector to the rigid body associated to the ball.

And one last thing, I set the gravity to 0.0 since I do not want gravity force to be applied on the ball.

And it works fine! By using the arrow keys, I am able to move the ball around in the four directions. Thus, collisions are properly managed and my ball does not cross anymore the wall.

In fact, it was much simpler than I had foreseen before.

Thanks to Modanung for his advice!

Have a nice day.

-------------------------

