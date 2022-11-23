Useless | 2017-01-02 01:08:24 UTC | #1

Hi i'm new in programming stuff, i i'm struggling to check collision with an Spriter Animated Sprite and a tile. I tried messing with the bounding box from the AnimatedSprite2D and creating a custom from an tile node, but i don't seen to understand it well, it don't intersect. Do anyone 


i'm following this article: [url]http://www.wildbunny.co.uk/blog/2011/12/14/how-to-make-a-2d-platform-game-part-2-collision-detection/[/url]
[code]
    void ResolveCollision(Node* tile) {
        BoundingBox actorBBox = animSprite->GetBoundingBox();
        actorBBox.Transform(node_->GetTransform());

        std::cout << "tile " << tile->GetPosition().ToString().CString() << "\n;";
        std::cout << node_->GetPosition().ToString().CString() << "\n;";

        if (actorBBox.IsInside(tile->GetPosition()) != OUTSIDE)
            std::cout << "NOT FIRING" << "\n";
    }

    void PosCollisions(float timeStep) {
        Vector2 position = node_->GetPosition2D() + Vector2(0, 0.5f);
        Vector2 predictedPos = position + (Vector2(velocity.x_, velocity.y_) * timeStep);

        Vector2 min = Vector2(Min(position.x_, predictedPos.x_), Min(position.y_, predictedPos.y_));
        Vector2 max = Vector2(Max(position.x_, predictedPos.x_), Max(position.y_, predictedPos.y_));


        int mapMinX = -1;
        int mapMinY = -1;
        map_->PositionToTileIndex(mapMinX, mapMinY, min);

        int mapMaxX = -1;
        int mapMaxY = -1;
        map_->PositionToTileIndex(mapMaxX, mapMaxY, max);

        for (int x = mapMinX; x <= mapMaxX; x++) {
            for (int y = mapMinY; y <= mapMaxY; y++) {
                Node* tile = map_->GetLayer(0)->GetTileNode(x, y);
                if (tile) {
                    ResolveCollision(tile);
                }
            }
        }
    }
[/code]
Edit: Updated Code

-------------------------

1vanK | 2017-01-02 01:08:24 UTC | #2

Why not use the Physics2D components?

-------------------------

Useless | 2017-01-02 01:08:24 UTC | #3

Box2D is a overkill for me... for that i would have to fight the engine to make the desirable behavior.

Also is there a way to setup a static bbox on the scml file?


Made something a bit simpler:
Point based
[code]      void AdjustPosition(Vector2 pos, float timeStep) {
        Vector2 tilePos = (node_->GetPosition2D() + pos + (Vector2(velocity.x_, velocity.y_) * timeStep));
        Node* tile = GetTileNode(tilePos);
        if (tile == NULL)
            return;
        Vector3 dir = tile->GetPosition() - node_->GetPosition() + pos;
        dir.Normalize();

        //dir = GetGreaterAxis(dir); //Need to check if the tile axis is occluded

        if (dir.y_ < 0) {
            node_->SetPosition2D(Vector2(node_->GetPosition2D().x_, tile->GetPosition2D().y_ + 0.32f - 0.01f));
            velocity.y_ = 0;
            return;
        }
        if (dir.x_ < 0) {
            //Tile size + half character width + 0.2
            node_->SetPosition2D(Vector2(tile->GetPosition2D().x_ + 0.64 - 0.2f, node_->GetPosition2D().y_));
            //velocity.x_ = 0;
            return;
        }
        if (dir.x_ > 0) {
            node_->SetPosition2D(Vector2(tile->GetPosition2D().x_ - 0.1f, node_->GetPosition2D().y_));
            //velocity.x_ = 0;
            return;
        }
    }

    void ResolveCollisions(float timeStep) {
        AdjustPosition(Vector2(0, 0), timeStep);
        AdjustPosition(Vector2(0.1, 0.2), timeStep);
        AdjustPosition(Vector2(0.1, 0.5), timeStep);
        AdjustPosition(Vector2(-0.1, 0.2), timeStep);
        AdjustPosition(Vector2(-0.1, 0.5), timeStep);
    }  [/code]

-------------------------

