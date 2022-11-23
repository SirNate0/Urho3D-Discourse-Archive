GodMan | 2022-02-05 00:28:45 UTC | #1

So I have a method that is suppose to constantly cast a ray directly in front of my character to check if an enemy is within range. The trouble I have is the the raycast does not follow the characters rotation. I must disclose that I am trash with the physics part of the API. Some of the values below are just me testing my issue. 


```
void EnergySword::MeleeLunge(StringHash eventType, VariantMap& eventData)
{
	PhysicsWorld* physicsWorld_ = scene_->GetComponent<PhysicsWorld>();
	PhysicsRaycastResult result;

	Vector3 charPos = node_->GetWorldPosition();
	Quaternion rot = node_->GetWorldRotation();
	Quaternion dir = rot * Quaternion(45.0f, Vector3::FORWARD);
	Vector3 rayDir = dir * Vector3::FORWARD;
	Vector3 aimPoint = node_->GetWorldDirection() + rot * Vector3(0, 1.7f, 0);

	Ray ray(charPos, rayDir);
	physicsWorld_->RaycastSingle(result, ray, 8.0f, 1);
	if (result.body_)
	{
		debug->AddLine(charPos, aimPoint, Color::CYAN, false);
	}
}
```

-------------------------

SirNate0 | 2022-02-05 03:59:15 UTC | #2

[quote="GodMan, post:1, topic:7185"]
```Vector3 aimPoint = node_->GetWorldDirection() + rot * Vector3(0, 1.7f, 0);```
[/quote]

Shouldn't that be `node_->GetWorldPosition()`?

Also, what are you trying to do with this Quaternion?

[quote="GodMan, post:1, topic:7185"]
`Quaternion dir = rot * Quaternion(45.0f, Vector3::FORWARD);`
[/quote]

-------------------------

GodMan | 2022-02-05 04:23:39 UTC | #3

@SirNate0 Thanks for the reply. That 2nd line you quoted was probably me just trying to find the correct way to get the nodes forward facing.

I changed the aimPoint like you suggested. The only issue is the raycast only works when my character is facing a certain direction. If my character rotates any other direction. The debug line that represents the ray never renders.

![Screenshot_Fri_Feb_04_22_18_01_2022|690x291](upload://7xpK0Ef5YyeKjNOZBdWn8BucXFc.jpeg)


```
	PhysicsWorld* physicsWorld_ = scene_->GetComponent<PhysicsWorld>();
	PhysicsRaycastResult result;

	Vector3 charPos = node_->GetWorldPosition();
	Quaternion rot = node_->GetWorldRotation();
	Vector3 aimPoint = node_->GetWorldPosition();

	Ray ray(charPos, aimPoint);
	physicsWorld_->RaycastSingle(result, ray, 8.0f, 1);
	if (result.body_)
	{
		debug->AddLine(charPos, result.position_, Color::CYAN, false);
	}
```

-------------------------

SirNate0 | 2022-02-05 13:27:06 UTC | #4

My bad. When I said you should change it to GetWorldPosition I meant just the GetWorldDirection call, not the entire right hand side. Additionally, Ray is constructed with a position and a direction, so if you want to call it with the aimPoint and not an aimDirection you need to subtract the starting position (`Ray ray(charPos, aimPoint-charPos);`).

Here's what I'd recommend (note, I've not compiled this to test it):
```
	PhysicsWorld* physicsWorld_ = scene_->GetComponent<PhysicsWorld>();
	PhysicsRaycastResult result;

	Vector3 charPos = node_->GetWorldPosition();
	Vector3 aimDir = node_->GetWorldDirection();

	Ray ray(charPos, aimDir);
	physicsWorld_->RaycastSingle(result, ray, 8.0f, 1);
	if (result.body_)
		debug->AddLine(charPos, result.position_, Color::CYAN, false);
	else
		debug->AddLine(charPos, charPos + 8.0f * aimDir, Color::RED, false);
```

-------------------------

GodMan | 2022-02-05 20:19:51 UTC | #5

@SirNate0 Thanks this seems to be working much better. The only issue is the ray is in the wrong direction. I believe this is because the node is the hand bone. So it's rotation is awkward. Can I use a Quaternion to fix this?

![Screenshot_Sat_Feb_05_14_15_33_2022|690x291](upload://vstnyFyUr8kmNC1Q8WoEOc1rEAW.jpeg)

-------------------------

