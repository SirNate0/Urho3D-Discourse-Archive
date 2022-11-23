TikariSakari | 2017-01-02 01:04:53 UTC | #1

I booted to windows10 and was trying out the d3d11, and I noticed that for some reasons some of the objects were completely invisible + there are some weird graphic glitches with d3d11. It adds some weird polygons close to 0,0,0.

Glitched d3d11:
[url]http://i.imgur.com/9P16nXG.png[/url]

Correct d3d9, opengl2 and opengl3:
[url]http://i.imgur.com/j3VPjcS.png[/url]

I kind of think that it has something to do with the notexture material, because also the ground is completely unvisible. Here is the material file for the red attack tiles:
[code]
<material>
    <technique name="Techniques/NoTextureUnlit.xml" />
    <parameter name="MatDiffColor" value="1 0 0 1" />
</material>
[/code]

And this is the green grass tile material:
[code]
<?xml version="1.0"?>
<material>
	<technique name="Techniques/NoTexture.xml" />
	<parameter name="MatDiffColor" value="0.0110063 0.0660488 0 1" />
</material>
[/code]

For creating the tiles I use following code, which basically just creates planes next to each other:
[code]
void MainGame::createAttackGrid()
{
    LOGINFO("Creates attack grid!");
    attackSquaresNode_->RemoveAllChildren();

    if( selectedUnit_ )
    {
        Urho3D::Vector2 pos;

        unsigned int mapSize = selectedUnit_->getAttackTiles().Size();

        for( unsigned int i = 0; i < mapSize; ++i )
        {
            pos = selectedUnit_->getAttackTiles()[i]->getMapPos();
            createActionTile( attackSquaresNode_, "AttackTile", pos, "Materials/attackTile.xml" );
        }
    }
}

void MainGame::createActionTile( Urho3D::Node* actionNode, const Urho3D::String& tileName, Urho3D::Vector2 pos, const Urho3D::String& matName )
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    Urho3D::Node* planeNode = actionNode->CreateChild( tileName + "_" + String(pos.x_) + "_" + String(pos.y_) );

    planeNode->SetScale(Urho3D::Vector3(SQUARE_SIZE.x_, 1.0f, SQUARE_SIZE.y_));
    Urho3D::StaticModel* planeObject = planeNode->CreateComponent<Urho3D::StaticModel>();
    planeObject->SetModel(cache->GetResource<Urho3D::Model>("Models/Plane.mdl"));
    planeObject->SetMaterial(cache->GetResource<Urho3D::Material>(matName));
    planeNode->SetPosition( Urho3D::Vector3( (pos.x_ + 0.5f ) * SQUARE_SIZE.x_, 0.025f, ( pos.y_ + 0.5f ) * SQUARE_SIZE.y_ ) );

}
[/code]

So basically I am just creating planes side by side without trying to combine the geometry.

I tried deleting the cache-folder from bin/coredata/shaders/hlsl

Also on the middle of a map there are suppose to be few random weird "grass" polygons, but they also seem to be oddly streched out. I guess it could be because of not importing stuff correctly from blender. 

Any ideas what could cause this kind of phenomenom or could it just be my gpu / windows10 / gpu drivers acting weird?

Edit: The moment I wrote something I figured out what was causing the weird graphical glitch with the red squares. The problem is that I create models for outlines and use a certain material for outlines. The problem is that there is HLSL shader for the outline, only GLSL one, and thus it doesn't really have any kind of material to use. So when the instancing is on, it kind of messes up the whole outline thing, and if I turn the instancing off, it creates the model with the previous material I think, but at least the model itself looks correct. On the other hand on d3d9, the instancing completely removes the whole character when the material is wrong, but if I turn off instancing even on d3d9, the character acts the same as on d3d11.

-------------------------

cadaver | 2017-01-02 01:04:53 UTC | #2

Check if you are getting errors to the log. D3D11 will refuse to render (or basically, refuse to create an input layout) if the model does not supply all the vertex elements the shader needs. I will check the requirements of notexture / notexture-unlit shaders, in theory they should not need eg. texcoords or normals, but these may be hard to untangle from the shader code, as it uses some generic helper functions to do the setup work in the vertex shader.

You should be safe if your vertex data always specifies positions, normals and texcoords (UVs can be just 0,0 for each vertex if you're using notexture)

-------------------------

cadaver | 2017-01-02 01:04:53 UTC | #3

The UV coordinate requirement should now be eliminated from LitSolid, LitParticle & Unlit shaders, when using the corresponding notexture techniques.

-------------------------

TikariSakari | 2017-01-02 01:04:53 UTC | #4

Thank you, seems that this does fix the problem with the map. The map is now visible with d3d11. Even the water-color with the specularity value works. So this seems to be solved now.

-------------------------

