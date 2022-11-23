1vanK | 2017-01-02 01:10:52 UTC | #1

Target is the green cube. How to fix it? Maybe there are some settings

[video]http://www.youtube.com/watch?v=6n-UK8GLqM0[/video]

Sorry for quality. I don't know why Youtube did it so low

-------------------------

weitjong | 2017-01-02 01:10:52 UTC | #2

Have you tried to tune the pushiness and avoidance parameters? It is kind of trial and error to get to one desired behavior.

-------------------------

1vanK | 2017-01-02 01:10:52 UTC | #3

[quote="weitjong"]Have you tried to tune the pushiness and avoidance parameters? It is kind of trial and error to get to one desired behavior.[/quote]

Obstacle avoidance have no any effect (I have no obstacles in scene).
SetNavigationPushiness just change gathering position

-------------------------

weitjong | 2017-01-02 01:10:53 UTC | #4

Ah right, there is no obstacle yet in your scene yet  :wink: . Perhaps, the radius then.

-------------------------

1vanK | 2017-01-02 01:10:53 UTC | #5

[code]        if (scope & SCOPE_NAVIGATION_PUSHINESS_PARAMS)
        {
            switch (navPushiness_)
            {
            case NAVIGATIONPUSHINESS_LOW:
                params.separationWeight = 4.0f;
                params.collisionQueryRange = radius_ * 16.0f;
                break;

            case NAVIGATIONPUSHINESS_MEDIUM:
                params.separationWeight = 2.0f;
                params.collisionQueryRange = radius_ * 8.0f;
                break;

            case NAVIGATIONPUSHINESS_HIGH:
                params.separationWeight = 0.5f;
                params.collisionQueryRange = radius_ * 1.0f;
                break;
            }
        }[/code]

Is there a way to manually change the params without modifying the engine?

-------------------------

