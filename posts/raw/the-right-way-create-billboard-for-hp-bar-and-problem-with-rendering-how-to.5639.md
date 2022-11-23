Elendil | 2019-10-02 10:23:38 UTC | #1

I want display HP above object and update texture each frame. I use billboard for that. Are there any another posibilities to display HP bar instead use billboards? Or billboards are the best way? 
Can I use Sprite in 3D scene instead billboards? With sprite I can use texture directly instead Billboards where are material used.

Problem with this is, when two or more HP bars are displayed it render only one bar. That means if HP is decreased, hpoints are decrease for all displayed HP bars. I think this is because billboards share same one texture. Or be more precise, material. I think this is problematic: `m_material = cache->GetResource<Material>("Materials/MyEmptyBillboard2.xml");` but when I use 

    m_material = new Material(ctx); 
    m_material->SetTexture(TextureUnit::TU_DIFFUSE, m_texture);

it show billboard with gray color.

This is how I display HP bar above my cubes (each cube have own billboard)

    	m_texture = new Texture2D(ctx);
    	m_texture->SetFilterMode(Urho3D::TextureFilterMode::FILTER_BILINEAR);
    	m_texture->SetNumLevels(1);
    	m_texture->SetSize(m_i_width, m_i_height, Urho3D::Graphics::GetRGBAFormat(), Urho3D::TEXTURE_DYNAMIC);
    	m_texture->SetData(0, 0, 0, m_i_width, m_i_height, m_idata_converted);


    	// billboard
    	m_node_billboard = m_node->CreateChild("HealthBar");
    	m_node_billboard->SetPosition(Vector3(0, 0.8, 0));
    	m_bs = m_node_billboard->CreateComponent<BillboardSet>();
    	m_bs->SetNumBillboards(1);

    	m_material = cache->GetResource<Material>("Materials/MyEmptyBillboard2.xml");
    	m_material->SetTexture(TextureUnit::TU_DIFFUSE, m_texture);
    	m_bs->SetMaterial(m_material);
    	
    	m_bs->SetSorted(true);

    	m_bb = m_bs->GetBillboard(0);
    	float fx = 0.5;
    	float fy = fx / (m_i_width / m_i_height);
    	m_bb->size_ = Vector2(fx, fy);
    	m_bb->enabled_ = SHOW_HEALTHBAR;

    	m_bs->Commit();

and how I update billboard

	ArmorHealthBar->Render((double)m_i_width, (double)m_i_height, m_idata);
	ConvertRGBA();
	m_texture->SetData(0, 0, 0, m_i_width, m_i_height, m_idata_converted);
	m_material->SetTexture(TextureUnit::TU_DIFFUSE, m_texture);

-------------------------

jmiller | 2019-10-02 13:49:18 UTC | #2

Hello / mae govannen,

@Miegamicis' [New Project Template](https://discourse.urho3d.io/t/new-project-template/4428) has a progress bar (seen later in [screenshots](https://github.com/ArnisLielturks/Urho3D-Project-Template/blob/master/Screenshots)) which uses Sprites:
  https://github.com/ArnisLielturks/Urho3D-Project-Template/blob/master/Source/Levels/Loading.cpp

-------------------------

JTippetts | 2019-10-02 14:04:40 UTC | #3

In an [ARPG](https://github.com/JTippetts/DungeonBot3000) I did for a game jam recently, I used regular old UI elements for the lifebars. The lifebar widget comprised 2 BorderImage, one for the gray background and one for the green bar, then a [custom component](https://github.com/JTippetts/DungeonBot3000/blob/master/src/Components/enemylifebar.cpp) attached to the enemy object handles Update, and uses the camera to project the enemy's location to the screen, adds an offset to put it above the head, and changes the widget's position to the projected position. Then it queries health and max health to adjust the size of the green BorderImage. It worked pretty well:
![image|666x500](upload://loWMzsIyLVj127oqB6XNLxYmkdG.jpeg) 

One characteristic of doing it this way is that the life bar stays a constant size, despite the enemy's distance from the camera. If that is not desired, you could probably do something with the [UIComponent](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/UI/UIComponent.h) component, which can be used to render a UI on a static model in the scene. Check the [48_Hello3DUI](https://github.com/urho3d/Urho3D/tree/master/Source/Samples/48_Hello3DUI) sample for a demonstration of how to set something like that up. You would likely need to include code, perhaps in a custom component attached to the same node, that would re-orient the static model to mimic billboarding behavior. This custom component could listen for Update, calculate the direction to the camera, and adjust the node's rotation. Be sure to disable shadows on that model so the lifebar wont cast a shadow.

-------------------------

Elendil | 2019-10-02 14:49:23 UTC | #4

Thanks all for answers.

[JTippetts](https://discourse.urho3d.io/u/JTippetts) good idea, Hello3DUI sample helped me what I did wrong with material, now it is displaying correctly, when bullet hit cube and two or more HP bars are displayed.

I am going to try create UI element inside 3D space.

-------------------------

Elendil | 2019-10-02 22:08:34 UTC | #5

I am creating UI element on box but without success. It display texture on UI instead on box. Box are black or transparent (invisible).

	Node * bb = m_node->CreateChild("HealthBox");
	bb->SetScale(Vector3(1.2f, 0.6f, 1.2f));
	bb->SetPosition(Vector3(0.0f, 1.2f, 0.0f));
	StaticModel * sbb = bb->CreateComponent<StaticModel>();
	sbb->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
	
	m_comp = bb->CreateComponent<UIComponent>();
	m_comp->GetMaterial()->SetTechnique(0, cache->GetResource<Technique>("Techniques/DiffUnlitParticleAlpha.xml"));
	
	m_uie = m_comp->GetRoot();
	m_uie->SetSize(100, 50);

	m_sprite = m_uie->CreateChild<Sprite>(); //e->CreateChild<Sprite>();
	m_sprite->SetTexture(m_texture);
	m_sprite->SetSize(m_i_width, m_i_height);
	m_sprite->SetBlendMode(Urho3D::BlendMode::BLEND_ALPHA);
	m_uie->SetEnabled(true);

-------------------------

SirNate0 | 2019-10-03 14:59:06 UTC | #6

No idea if this is it or not, but what happens if you remove this line?
```
m_comp->GetMaterial()->SetTechnique(0, cache->GetResource<Technique>("Techniques/DiffUnlitParticleAlpha.xml"))
```

-------------------------

Elendil | 2019-10-03 15:12:56 UTC | #7

Unfortunately nothing. Just boxes are black.

-------------------------

JTippetts | 2019-10-03 23:31:37 UTC | #8

Can you provide full source for a minimal example the demonstrates the issue? It's possible something else is going on outside what you show.

-------------------------

Elendil | 2019-10-04 10:00:21 UTC | #9

I discover a problem. The size of sprite and UIElement must be minimum 64 x 64. That means if I have 100 x 50 it is not working.

    m_uie->SetSize(128, 64);
    m_sprite->SetSize(128, 64);

After that it display my sprite on box.

-------------------------

Elendil | 2019-10-04 10:45:53 UTC | #10

I found using materials directly is more lighter on render as Sprite on box or plane if 400 boxes are displayed. Maybe there is some technique which increase FPS with lot of object displayed with HP bar?
I create my MyCube object same as regular static model.

-------------------------

JTippetts1 | 2019-10-08 07:40:11 UTC | #11

One potential issue with using UIComponent is that each one is a render-to-texture, so when you do 400 of them you're adding a lot of overhead. Might be better to try the trick I suggested initially, or roll your own alternative solution instead.

-------------------------

