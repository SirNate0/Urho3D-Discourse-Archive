codingmonkey | 2017-01-02 01:01:26 UTC | #1

I have 3d level, it mean that AI should move in all 3-dimensions. And for this 3d navigation on map for my ai-enemies i spawn a many empty nodes on map with vars (ai=1) then a get they in code and set as waypoints in enemy::LogicComponent. 

And recently i saw splinePath and add it to ai root node but not find any possibility to manipulate with path in editor. 
Perhaps i wrong and its only for in code purpose.

Any way) I want know how SplinePath working ?

-------------------------

hdunderscore | 2017-01-02 01:01:26 UTC | #2

Perhaps I misunderstood the question, but you can drag nodes from the hierarchy to the Node ID fields of a spline path and then affect the path with those nodes.

-------------------------

codingmonkey | 2017-01-02 01:01:27 UTC | #3

that's what I did with splines
[url=http://savepic.org/6549649.htm][img]http://savepic.org/6549649m.png[/img][/url]

[code]
	PODVector<Node*> aiWaypoints_;
	SharedPtr<SplinePath> botSplinePath_;

	Node* aiNode_ = scene_->GetChild("AI", true);
	botSplinePath_ = bot_->GetComponent<SplinePath>();
	
	aiNode_->GetChildren(aiWaypoints_);
	for (int i = 0; i<aiWaypoints_.Size(); i++) 
	{
		botSplinePath_->AddControlPoint(aiWaypoints_[i]);
	}
	botSplinePath_->AddControlPoint(aiWaypoints_[0]);
	botSplinePath_->SetSpeed(3.0f);
	botSplinePath_->SetControlledNode(bot_);[/code]

[code]
void GameMain::UpdateBotPosition(float timeStep) 
{
	if (botSplinePath_->IsFinished()) botSplinePath_->Reset();
	botSplinePath_->Move(timeStep);
}
[/code]

I just tried to understood how they worked
And how can I use them to move the bots

-------------------------

