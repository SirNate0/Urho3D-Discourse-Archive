lexx | 2017-01-02 01:04:30 UTC | #1

I need to know every node's name in scene_, how would I do it?

Something like
[code]
       ..load scene...

	PODVector<Node*> nodes;
	scene_->GetChildrenRecursive(nodes);

	foreach(Node n in nodes)
		print( n.GetName() );
[/code]
(not working example)

-------------------------

TikariSakari | 2017-01-02 01:04:30 UTC | #2

I have used something simple like this for printing hierarchy. It might not be the most optimal solution to your problem, since GetChildren seems to have one version where you can ask children recursively. 

[code]
void MainGame::printNodeHierarchy( Node* node ) {    
    LOGINFO( "Main:" + node->GetName() );
    const auto& children = node->GetChildren();
    for( unsigned int i = 0; i < children.Size(); ++i ) {
        Node* node = children[i];
        LOGINFO( "Child:" + node->GetName() );

        LOGINFO( "Position:" + String( node->GetPosition() ) );
        printNodeHierarchy( node);

    }

}

[/code]

And then calling it by passing a scene to it since scenes are inherited by nodes, although it is using c++11.

-------------------------

lexx | 2017-01-02 01:04:30 UTC | #3

Thanks, it works. I use name checking only in CreateScene() method so it is fast enough.

[quote]
although it is using c++11.
[/quote]
Works even I dont use c++11 (still using old VS2010).

-------------------------

GoogleBot42 | 2017-01-02 01:04:31 UTC | #4

[quote="lexx"]Works even I dont use c++11 (still using old VS2010).[/quote]

VS2010 actually does support *some* c++11 it is VS2008 that really lacks support (if any at all).

-------------------------

