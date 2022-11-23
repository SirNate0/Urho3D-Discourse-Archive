sabotage3d | 2017-01-02 01:15:11 UTC | #1

Hi,
Is it possible to use Urho3D::Image in texture unit directly? For example if I have Urho3D::Image can I pass it to the diffuse texture unit?

-------------------------

sabotage3d | 2017-01-02 01:15:12 UTC | #2

This seems to work but it looks wrong. If I remove SetData it is not longer flipping the texture. What would be the correct way?

[code]ResourceCache* cache = GetSubsystem<ResourceCache>();
Texture2D* texture = cache->GetResource<Texture2D>(filepath);
Image* image = cache->GetResource<Image>(filepath);
image->FlipVertical();
texture->SetData(image);

Renderer* renderer = GetSubsystem<Renderer>();
Viewport* viewport = renderer->GetViewport(0);

RenderPath * rp = viewport->GetRenderPath();
  for ( int i = 0; i < rp->GetNumCommands(); i++ )
  {
     RenderPathCommand * cmd = rp->GetCommand( i );
     if ( cmd->type_ == RenderCommandType::CMD_QUAD )
     {
        cmd->SetTextureName(TextureUnit::TU_DIFFUSE, image->GetName());


     }

  }[/code]

-------------------------

Eugene | 2017-01-02 01:15:12 UTC | #3

The correct way is to understand that Image and Texture2D are completely different under the skin.
You should consider them as unrelated resources that may be loaded from the same file and converted into each other through SetData/GetImage.
So if you change (i.e. flip) one, antoher remains unchanged.

-------------------------

