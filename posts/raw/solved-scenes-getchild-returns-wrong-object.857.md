TikariSakari | 2017-01-02 01:03:34 UTC | #1

[code]
	Node* boxNode = scene_->CreateChild("BoxInAir");
	boxNode->SetPosition(Vector3(10, 10, 30));
	StaticModel* boxObject = boxNode->CreateComponent<StaticModel>();
	boxObject->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
	boxObject->SetMaterial(cache->GetResource<Material>("Materials/StoneEnvMapSmall.xml"));
	boxObject->SetCastShadows(true);


	 boxNode = scene_->GetChild("BoxInAir");


[/code]

The above code, the boxnode is not same as what I create. I also create 900 bears (just testing performance), and it actually returns one bear.

Actually I did solve the problem. It was on the following thing:

[code]
   for (unsigned int i = 0; i < NUM_MODELS; ++i)
    {
        Node* modelNode = scene_->CreateChild("Jack" + i);
[/code]

Somehow the String cannot concatenate with integers, but it gave me no errors. On the otherhand it seems to add some very cryptic names, like materias names, etc. Also I couldn't find something to turn integers into Urho3D::Strings.

-------------------------

friesencr | 2017-01-02 01:03:34 UTC | #2

i haven't done it in angelscript but to create a Urho String you use the constructor.  ex String(4).

-------------------------

setzer22 | 2017-01-02 01:03:34 UTC | #3

To clarify a bit more, basically Good Ol' C++ just converted your int to a char (truncated, if bigger than 255) and added it to the String as a single character, whatever that character might be, which isn't clearly what you wanted. Unfortunately C++ doesn't provide a protection mechanism to differentiate an unsigned byte from a string character.

-------------------------

TikariSakari | 2017-01-02 01:03:35 UTC | #4

[quote="setzer22"]To clarify a bit more, basically Good Ol' C++ just converted your int to a char (truncated, if bigger than 255) and added it to the String as a single character, whatever that character might be, which isn't clearly what you wanted. Unfortunately C++ doesn't provide a protection mechanism to differentiate an unsigned byte from a string character.[/quote]

Actually after thinking this a bit more, I feel like what happened is that the String is just a pointer and it accessed a random place in memory and created a string from it, so it gave completely random string for names. I suppose that's what I get for not coding C++ for so long time.

edit: Yup I completely forgot that string literal in c++ is char[], and if you add number to a pointer, it changes the starting position.

-------------------------

