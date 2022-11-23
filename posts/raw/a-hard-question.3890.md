spwork | 2017-12-29 08:45:01 UTC | #1

I had a game, there is a mouse drag box to select building delete functions, but deleted when there is such a problem, some time can remove some normal, when node acquired from the RigidBody2D pointer to 0xDDDDDDDD, why this is the case, if I don't use node->Remove () is not wrong, different objects there will be a correlation between? How should I correct it?  

        PODVector<RigidBody2D*> bodys;
        SCENEMANAGER->GetScene()->GetComponent<PhysicsWorld2D>()
        			->GetRigidBodies(bodys, Rect(x, y, cx, cy));

    		auto mapMg = MAPMANAGER;
    		for (auto i = bodys.Begin(); i != bodys.End();i++)
    		{
    			auto node = (*i)->GetNode();
    			if (!node->HasTag("Building"))continue;
    			
    			auto pos = node->GetPosition2D();
    			mapMg->GetMapNode(pos.x_, pos.y_)->DelNode();
    			node->Remove();
    		}

-------------------------

spwork | 2017-12-29 09:18:29 UTC | #2

Ha ha, I know, some buildings have multiple collisions, so the same rigid body has been added many times, so that the same node will be deleted many times, and repeat the deletion of the same node will be wrong.

-------------------------

