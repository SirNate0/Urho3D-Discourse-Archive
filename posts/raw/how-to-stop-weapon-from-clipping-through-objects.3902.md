Zyie | 2017-12-30 20:58:06 UTC | #1

Hi im creating an FSP game and i was wondering how you stop the gun from clipping through other objects.

I've looked at this thread:

[https://discourse.urho3d.io/t/how-to-control-render-order/1240/11](https://discourse.urho3d.io/t/how-to-control-render-order/1240/11)

However I'm new to all this and have no idea what they are on about.

Can anyone explain how to achieve this with a beginner in mind?

EDIT::
ok so based off this post [https://discourse.urho3d.io/t/how-to-layer-scenes/740/4](https://discourse.urho3d.io/t/how-to-layer-scenes/740/4)

I have tried setting up two scenes with one of the cameras using a render path that removes this line of code

    <command type="clear" color="fog" depth="1.0" stencil="0" />

This is how i have set it up currently

    	mScene = new Scene(mContext);
	mScene->CreateComponent<Octree>();
	mScene->CreateComponent<PhysicsWorld>();

	mScene2 = new Scene(mContext);
	mScene2->CreateComponent<Octree>();
	mScene2->CreateComponent<PhysicsWorld>();

	mCameraNode = mScene->CreateChild("Camera");
	mCameraNode2 = mScene2->CreateChild("Camera2");

	mCamera = mCameraNode->CreateComponent<Camera>();
	mCameraNode->SetPosition(Vector3(0.0f, 15.0f, 0.0f));
	mCamera->SetFarClip(300.0f);

	Camera* mCamera2 = mCameraNode2->CreateComponent<Camera>();
	mCameraNode->SetPosition(Vector3(0.0f, 15.0f, 0.0f));
	mCamera->SetFarClip(300.0f);

	Viewport* viewport = new Viewport(mContext, mScene, mCamera);
	Viewport* viewport2 = new Viewport(mContext, mScene2, mCamera2);

	XMLFile* overlayRenderPath = cache->GetResource<XMLFile>("MyRenderPath/Forward2.xml");
	viewport2->SetRenderPath(overlayRenderPath);

	renderer->SetNumViewports(2);
	renderer->SetViewport(0, viewport);
	renderer->SetViewport(1, viewport2);

However this still does not stop the weapon from clipping through the terrain. Anyone got any ideas how to fix this

-------------------------

1vanK | 2017-12-31 14:17:09 UTC | #2

 https://discourse.urho3d.io/t/depthhack-for-weapon-rendering/2202

-------------------------

