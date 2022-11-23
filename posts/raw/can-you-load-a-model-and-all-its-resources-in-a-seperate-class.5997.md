GodMan | 2020-03-16 20:48:38 UTC | #1

I have some templates that are for different NPCs, for example I have a AI_Melee class that I'm trying to load the character model and setup it's animation controller all in that class. That way I don't have so much of it in my main program. Is this bad practice?

-------------------------

SirNate0 | 2020-03-16 21:30:22 UTC | #2

That's the approach I took. I went as far as separating a resource and a component class for some of the character types. I'll let others comment on whether it's a good practice.

-------------------------

GodMan | 2020-03-16 21:34:50 UTC | #3

It just seems easier and cleaner approach. I have not seen a class where someone loaded the actual 3d model and applied it to the node, but I've seen some classes where they actually loaded basically everything else.

-------------------------

jmiller | 2020-03-17 08:45:26 UTC | #4

It seems natural enough to take an approach with different classes. Just for reference, I have prototyped with a single Player Component with types differentiated by prefabs containing everything asset-related: nodes and transforms, AnimatedModel (sometimes pasted from editor), physics components, materials..

```
Player::OnNodeSet(Node* node) {
  if (node == nullptr) { return; }
  node_->LoadXML(node_->GetVar("template").GetString());
  // Subscribe to some events, cache some pointers, create more stuff.. Ninja.as for more
}

playerNode->SetVar("template", "Players/Urho.xml");
playerNode->CreateComponent<Player>();
```

-------------------------

