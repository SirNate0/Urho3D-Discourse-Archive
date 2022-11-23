ab4daa | 2019-03-09 06:47:28 UTC | #1

Reproduced the generator of [space-3d](http://wwwtyro.github.io/space-3d). ([its repo](https://github.com/wwwtyro/space-3d))

[Urho3D version](https://github.com/ab4daa/space-Urho3D)

https://github.com/ab4daa/space-Urho3D/blob/master/screen.png?raw=true

I made a SpaceBoxGen class to help generate texturecube.
E_SPACEBOXGEN event will send parameters of sun, maybe can use them to setup directional light.
The RTT scene in SpaceBoxGen will be destroyed in E_ENDFRAME.
<pre><code>
{
  SubscribeToEvent(E_SPACEBOXGEN, URHO3D_HANDLER(RenderToTexture, ChangeLight));
  Node * space = scene_->CreateChild("Space Box");
  space->SetScale(500.0f); // The scale actually does not matter
  auto* spacebox = space->CreateComponent&lt;Skybox>();
  spacebox->SetModel(cache->GetResource&lt;Model>("Models/Box.mdl"));
  SharedPtr&lt;Material> space_mat = MakeShared&lt;Material>(GetContext());
  space_mat->SetCullMode(CULL_NONE);
  space_mat->SetNumTechniques(1);
  space_mat->SetTechnique(0, cache->GetResource&lt;Technique>("Techniques/DiffSkybox.xml"), QUALITY_MAX);
  gen = MakeShared&lt;SpaceBoxGen>(context_);
  space_mat->SetTexture(TU_DIFFUSE, gen->SpaceCube);
  gen->Generate();
  spacebox->SetMaterial(space_mat);
}
</code></pre>

Maybe it's not as epic as recent games, it's already too good to keep consistency with my other self-made assets :\

-------------------------

