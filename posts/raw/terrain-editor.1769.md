Lumak | 2017-01-02 01:09:59 UTC | #1

What I had originally planned to create a simple terrain height map editor, something to just tweak the height, has now turned into a full terrain editor.  
This is my first attempt working with a terrain editor, and it turned out to be a fun project to work on. 

The original source code is listed below, but since then I've added a lot more features and have included binary releases for Windows and Linux.
[b][size=150]Binary release[/size][/b] - [url=https://drive.google.com/open?id=0B2Yd1AZoTDywX20wTVVzUF9wZzg]TerrainEdit-V0.03.zip[/url].
Unzip it in your <urho3d/project>/bin folder.

[b][size=150]Features:[/size][/b] items in [color=#0000FF]blue[/color] are included in the binary release
---------------------------------------------
[ul]
[li]Edit
[list]
[*] raise/lower[/li]
[li] smooth[/li]
[li] flatten[/li]
[li] set height[/li]
[li] edit terrain weights(color) map[/li]
[li] undo edit[/li]
[li] [color=#0000FF]add light noise[/color][/li]
[li] [color=#0000FF] add noise[/color][/li]
[li] [color=#0000FF] add erosion[/color][/li][/ul][/*:m][/list:u]
 [color=#0000FF][ul] [li]Terraform
[list]
[*] minimal[/li]
[li] smooth[/li]
[li] rough[/li]
[li] very rough[/li]
[li] auto-paint height layers[/li][/ul][/*:m][/list:u]
[ul] [li] DDS texture support[/li][/ul]
[/color]---------------------------------------------

[b]**NOTE**[/b] in the source code listed below the terrain paint feature paints the terrain weight image but you'll need to use PNG file or JPG. Detail images still can be dds files.
Here is the png file that I used [url=http://wikisend.com/download/759326/TerrainWeights.png]TerrainWeights.png[/url]  The binary release has no limitations.

[spoiler][b]TerrainEdit.cpp[/b]
[code]
//
// Copyright (c) 2008-2015 the Urho3D project.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.
//

#include <Urho3D/Urho3D.h>

#include <Urho3D/Graphics/Camera.h>
#include <Urho3D/Physics/CollisionShape.h>
#include <Urho3D/Physics/Constraint.h>
#include <Urho3D/Core/CoreEvents.h>
#include <Urho3D/Engine/Engine.h>
#include <Urho3D/IO/FileSystem.h>
#include <Urho3D/UI/Font.h>
#include <Urho3D/Input/Input.h>
#include <Urho3D/Graphics/Light.h>
#include <Urho3D/Graphics/Material.h>
#include <Urho3D/Graphics/Model.h>
#include <Urho3D/Graphics/Octree.h>
#include <Urho3D/Physics/PhysicsWorld.h>
#include <Urho3D/Core/ProcessUtils.h>
#include <Urho3D/Graphics/Renderer.h>
#include <Urho3D/Physics/RigidBody.h>
#include <Urho3D/Resource/ResourceCache.h>
#include <Urho3D/Scene/Scene.h>
#include <Urho3D/Graphics/StaticModel.h>
#include <Urho3D/Graphics/Terrain.h>
#include <Urho3D/UI/Text.h>
#include <Urho3D/UI/UI.h>
#include <Urho3D/Graphics/Zone.h>
#include <Urho3D/Graphics/DebugRenderer.h>
#include <Urho3D/Graphics/TerrainPatch.h>
#include <Urho3D/Graphics/Skybox.h>
#include <Urho3D/UI/Slider.h>
#include <Urho3D/UI/UIEvents.h>
#include <Urho3D\UI\Window.h>

#include "TerrainEdit.h"

#include <Urho3D/DebugNew.h>
#include <SDL/SDL_log.h>

//=============================================================================
//=============================================================================

DEFINE_APPLICATION_MAIN(TerrainEdit)
//=============================================================================
//=============================================================================
// debug defines
#define DBG_TERRAIN_POS         // realign the world position by calling InvWorldToHeightMap()
//#define DBG_DRAW_PIX_LINES    // show pixel lines

#define RAYCAST_DISTANCE             600.0f  // make this user adjustable or just set it to 1k?
#define INCREMENTAL_VALUE            0.012f  // make this user adjustable
#define INCREMENTAL_VALUE_SMOOTH     0.060f  // make this user adjustable
#define INCREMENTAL_VALUE_PAINT      0.300f  // make this user adjustable
#define DEFAULT_SCALER_VAL           0.100f

#define PAINT_TIMER_RATE             100
#define PAINT_UNDO_RATE              100
#define DEBOUNCE_TIMER               200

//=============================================================================
//=============================================================================
TerrainEdit::TerrainEdit(Context* context) :
    Sample(context)
{
    // terrain
    terrMode = kTerrainMode_Increase;
    terrRadius = 10.0f;
    terrMinSphSize = 2.0f;
    terrMaxSphSize = 40.0f;

    // terrain paint
    colorMap_ = NULL;
    m_iTerrPaintMode = kPaintWeight_Red;
    
    // history
    historyInIdx = 0;
    historyStartIdx = 0;
}

//=============================================================================
//=============================================================================
void TerrainEdit::Setup()
{
    // Modify engine startup parameters
    engineParameters_["WindowTitle"]  = GetTypeName();
    engineParameters_["LogName"]      = GetSubsystem<FileSystem>()->GetAppPreferencesDir("urho3d", "logs") + GetTypeName() + ".log";
    engineParameters_["FullScreen"]   = false;
    engineParameters_["Headless"]     = false;
    engineParameters_["WindowWidth"]  = 1280; 
    engineParameters_["WindowHeight"] = 720;
}

//=============================================================================
//=============================================================================
void TerrainEdit::Start()
{
    // Execute base class startup
    Sample::Start();

    // Create static scene content
    CreateScene();

    // Create the UI content
    CreateInstructions();

    // Subscribe to necessary events
    SubscribeToEvents();
}

//=============================================================================
//=============================================================================
void TerrainEdit::CreateScene()
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();

    scene_ = new Scene(context_);

    // Create scene subsystem components
    dbgRenderer = scene_->CreateComponent<DebugRenderer>();
    scene_->CreateComponent<Octree>();
    scene_->CreateComponent<PhysicsWorld>();
	PhysicsWorld *pPhysicsWorld = scene_->GetComponent<PhysicsWorld>();
    pPhysicsWorld->SetDebugRenderer( dbgRenderer );

    // Create camera and define viewport. We will be doing load / save, so it's convenient to create the camera outside the scene,
    // so that it won't be destroyed and recreated, and we don't have to redefine the viewport on load
    cameraNode_ = new Node(context_);
    Camera* camera = cameraNode_->CreateComponent<Camera>();
    camera->SetFarClip(1000.0f);
    GetSubsystem<Renderer>()->SetViewport(0, new Viewport(context_, scene_, camera));
    
    // Set an initial position for the camera scene node above the plane
    cameraNode_->SetPosition(Vector3(0.0f, 30.0f, 0.0f));

    // Create static scene content. First create a zone for ambient lighting and fog control
    Node* zoneNode = scene_->CreateChild("Zone");
    Zone* zone = zoneNode->CreateComponent<Zone>();
    zone->SetAmbientColor(Color(0.7f, 0.7f, 0.7f));
    zone->SetFogColor(Color(0.8f, 0.8f, 0.8f));
    zone->SetFogStart(800.0f);
    zone->SetFogEnd(900.0f);
    zone->SetBoundingBox(BoundingBox(-2000.0f, 2000.0f));

    Node* skyNode = scene_->CreateChild("Sky");
    skyNode->SetScale(500.0f); // The scale actually does not matter
    Skybox* skybox = skyNode->CreateComponent<Skybox>();
    skybox->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
    skybox->SetMaterial(cache->GetResource<Material>("Materials/Skybox.xml"));

    // Create a directional light with cascaded shadow mapping
    Node* lightNode = scene_->CreateChild("DirectionalLight");
    lightNode->SetDirection(Vector3(0.1f, -0.1f, 0.825f));
    Light* light = lightNode->CreateComponent<Light>();
    light->SetLightType(LIGHT_DIRECTIONAL);
	//light->SetColor(Color(0.99f, 0.99f, 0.99f));
    light->SetCastShadows(true);
    light->SetShadowBias(BiasParameters(0.00025f, 0.5f));
    light->SetShadowCascade(CascadeParameters(10.0f, 50.0f, 200.0f, 0.0f, 0.8f));
    light->SetSpecularIntensity(0.1f);

    // Create heightmap terrain with collision
    // **dbg init patchSize_, spacing_, numPatches_, numVertices_, patchWorldSize_ and patchWorldOrigin_
    patchSize_ = 32;
    spacing_ = Vector3(2.0f, 0.6f, 2.0f);

    terrainNode_ = scene_->CreateChild("Terrain");
    terrainNode_->SetPosition(Vector3::ZERO);
    terrain_ = terrainNode_->CreateComponent<Terrain>();
    terrain_->SetPatchSize( patchSize_ );
    terrain_->SetSpacing( spacing_ ); // Spacing between vertices and vertical resolution of the height map
    terrain_->SetSmoothing(true);
    terrain_->SetHeightMap(cache->GetResource<Image>("Textures/HeightMap.png"));
    terrain_->SetMaterial(cache->GetResource<Material>("Materials/Terrain.xml"));
    terrain_->SetOccluder(true);

    RigidBody* body = terrainNode_->CreateComponent<RigidBody>();
    body->SetCollisionLayer(2); // Use layer bitmask 2 for static geometry
    CollisionShape* shape = terrainNode_->CreateComponent<CollisionShape>();
    shape->SetTerrain();

    // **dbg - equations from Terrain.cpp
    numPatches_ = IntVector2( (terrain_->GetHeightMap()->GetWidth() - 1) / patchSize_, (terrain_->GetHeightMap()->GetHeight() - 1) / patchSize_ );
    numVertices_ = IntVector2( numPatches_.x_ * patchSize_ + 1, numPatches_.y_ * patchSize_ + 1 );
    patchWorldSize_ = Vector2( spacing_.x_ * (float)patchSize_, spacing_.z_ * (float)patchSize_ );
    patchWorldOrigin_ = Vector2( -0.5f * (float)numPatches_.x_ * patchWorldSize_.x_, -0.5f * (float)numPatches_.y_ *patchWorldSize_.y_ );

    // gradient map
    m_pImageGraient = cache->GetResource<Image>("Textures/Ramp.png");

    // terrain paint
    Texture2D *pTextureTerrainWeight = (Texture2D*)terrain_->GetMaterial()->GetTexture( TU_DIFFUSE );
    colorMap_ = new ColorMap( context_ );
    colorMap_->SetSourceColorMap( pTextureTerrainWeight );

    // slider
    m_pSliderScaler = CreateSlider(300, 650, 400, 20, "Scaler");
    m_pSliderScaler->SetValue( DEFAULT_SCALER_VAL );
    m_pTextSliderVal->SetText( String( DEFAULT_SCALER_VAL ) );
    scalerColor = Color( DEFAULT_SCALER_VAL, DEFAULT_SCALER_VAL, DEFAULT_SCALER_VAL );
    SubscribeToEvent(m_pSliderScaler, E_SLIDERCHANGED, HANDLER(TerrainEdit, HandleSliderChanged));
}

//=============================================================================
//=============================================================================
void TerrainEdit::CreateInstructions()
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    UI* ui = GetSubsystem<UI>();

    // Create a Cursor UI element because we want to be able to hide and show it at will. When hidden, the mouse cursor will
    // control the camera, and when visible, it will point the raycast target
    XMLFile* style = cache->GetResource<XMLFile>("UI/DefaultStyle.xml");
    Font *fontAnonymous = cache->GetResource<Font>("Fonts/Anonymous Pro.ttf");

    SharedPtr<Cursor> cursor(new Cursor(context_));
    cursor->SetStyleAuto(style);
    ui->SetCursor(cursor);

    // Construct new Text object, set string to display and font to use
    Text* instructionText = ui->GetRoot()->CreateChild<Text>();
    instructionText->SetText(
        "Edit Modes:\n"
        "F5/F6 - inc/dec sphere size\n"
        "F7  - elevate, lower, smooth,\n"
        "      flatten, set height\n"
        "F8  - paint (cycle rgb)\n"
        "F11 - save heightmap\n"
        "F12 - save colormap\n"
        "LMB - edit terrain\n"
        "Z   - undo edit"
    );
    instructionText->SetFont( fontAnonymous, 15 );
    // The text has multiple rows. Center them in relation to each other
    instructionText->SetTextAlignment(HA_LEFT);

    // Position the text relative to the screen center
    instructionText->SetHorizontalAlignment(HA_LEFT);
    instructionText->SetVerticalAlignment(VA_TOP);
    instructionText->SetPosition(30, 450);

    // terrain text
    terrText = ui->GetRoot()->CreateChild<Text>();
    terrText->SetFont( fontAnonymous, 18 );
    terrText->SetHorizontalAlignment(HA_LEFT);
    terrText->SetVerticalAlignment(VA_TOP);
    terrText->SetPosition(30, 350);
    terrText->SetColor( Color::CYAN );

    terrRayText = ui->GetRoot()->CreateChild<Text>();
    terrRayText->SetFont( fontAnonymous, 14 );
    terrRayText->SetHorizontalAlignment(HA_LEFT);
    terrRayText->SetVerticalAlignment(VA_TOP);
    terrRayText->SetPosition(30, 410);
    terrRayText->SetColor( Color::YELLOW );

    // update text
    UpdateTerrainSetText();
}

//=============================================================================
//=============================================================================
void TerrainEdit::SubscribeToEvents()
{
    // Subscribe to Update event for setting the vehicle controls before physics simulation
    SubscribeToEvent(E_UPDATE, HANDLER(TerrainEdit, HandleUpdate));

    // Unsubscribe the SceneUpdate event from base class as the camera node is being controlled in HandlePostUpdate() in this sample
    UnsubscribeFromEvent(E_SCENEUPDATE);
}

//=============================================================================
//=============================================================================
void TerrainEdit::UpdateTerrMode()
{
    Input* input = GetSubsystem<Input>();

    // sph radius
    if ( input->GetKeyDown(KEY_F5 ) )
    {
        terrRadius += 0.1f;
    }
    if ( input->GetKeyDown(KEY_F6) )
    {
        terrRadius -= 0.1f;
    }
    terrRadius = Clamp( terrRadius, terrMinSphSize, terrMaxSphSize );

    // cycle modes
    if ( input->GetKeyPress(KEY_F7) )
    {
        if ( m_TimerDebounce.GetMSec( false ) > DEBOUNCE_TIMER )
        {
            if ( ++terrMode > kTerrainMode_SetHeight )
            {
                terrMode = kTerrainMode_Increase;
            }

            m_TimerDebounce.Reset();

            // change desc
            switch ( terrMode )
            {
            case kTerrainMode_Increase:
            case kTerrainMode_Decrease:
            case kTerrainMode_Smooth:
                m_pTextSliderDesc->SetText( "Scaler" );
                m_pSliderScaler->SetVisible( true );
                break;

            case kTerrainMode_Flatten:
                m_pSliderScaler->SetVisible( false );
                break;

            case kTerrainMode_SetHeight:
                m_pTextSliderDesc->SetText( "Height" );
                m_pSliderScaler->SetVisible( true );
                break;
            }
        }
    }

    // cycle paint color
    if ( input->GetKeyPress( KEY_F8 ) )
    {
        if ( m_TimerDebounce.GetMSec( false ) > DEBOUNCE_TIMER )
        {
            if ( terrMode != kTerrainMode_Paint )
            {
                terrMode = kTerrainMode_Paint;
            }
            else
            {
                ++m_iTerrPaintMode %= kPaintWeight_End;
            }
            m_pTextSliderDesc->SetText( "Scaler" );
            m_pSliderScaler->SetVisible( true );

            m_TimerDebounce.Reset();
        }
    }

    // update text
    UpdateTerrainSetText();
}

//=============================================================================
//=============================================================================
void TerrainEdit::UpdateTerrainSetText()
{
    const char *terrModeDesc[ kTerrainMode_End ] = { "elevate", "lower", "smooth", "flatten", "set height", "paint" };

    char rbuf[10];
    sprintf( rbuf, "%4.1f", terrRadius );
    String strTerr;

    if ( terrMode == kTerrainMode_Paint )
    {
        const char *terrColorDesc[ kPaintWeight_End ] = { "red", "green", "blue" };
        strTerr = "mode: " + String(terrModeDesc[terrMode]) + ", "+ String( terrColorDesc[m_iTerrPaintMode] )+ "\nradius: " + String(rbuf);
    }
    else
    {
        strTerr = "mode: " + String(terrModeDesc[terrMode]) + "\nradius: " + String(rbuf);
    }

    terrText->SetText( strTerr );
}

//=============================================================================
//=============================================================================
void TerrainEdit::EditTerrain()
{
    Vector3 hitPos;

    if ( Raycast( RAYCAST_DISTANCE, hitPos ) )
    {
        // prevent unintentional fast over painting
        if ( terrMode == kTerrainMode_Paint )
        {
            if ( m_TimerColorMap.GetMSec( false ) < PAINT_TIMER_RATE )
            {
                return;
            }

            m_TimerColorMap.Reset();
        }

        if ( GetSubsystem<Input>()->GetMouseButtonDown( MOUSEB_LEFT ) )
        {
            Image *terrHeightMap = terrain_->GetHeightMap();
            int terrModRadius = (int)terrRadius;

            IntVector2 pixelPos = WorldToHeightMap( hitPos );
            int startPosLeft = pixelPos.x_ - terrModRadius/2;
            int startPosTop = pixelPos.y_ - terrModRadius/2;

            Vector3 outerCir = Vector3( hitPos.x_ + terrRadius, hitPos.y_, hitPos.z_ + terrRadius );
            IntVector2 deltaCir = pixelPos - WorldToHeightMap( outerCir );
            float fCircleRadiusSq = (float)( deltaCir.x_*deltaCir.x_ + deltaCir.y_*deltaCir.y_ );
            Color avgColor( Color::BLACK );
            int iAvgCnt = 0;
            float fScaler = scalerColor.Average();

            #ifdef DBG_DRAW_PIX_LINES
            m_vHtPos.Clear();
            #endif

            // history done flag
            HistoryData histData;
            histData.doneAndMode = kHistoryMask_Done | terrMode;
            InsertHistData( histData );

            // find avg for smooth mode and flatten
            if ( ( terrMode == kTerrainMode_Flatten && !bFlattenHeightSet ) || terrMode == kTerrainMode_Smooth )
            {
                for ( int y = 0; y < 2*terrModRadius; ++y )
                {
                    for ( int x = 0; x < 2*terrModRadius; ++x )
                    {
                        IntVector2 pos = IntVector2( x + startPosLeft, y + startPosTop );
                        IntVector2 diff = pixelPos - pos;
                        float fPixRadiusSq = (float)( diff.x_*diff.x_ + diff.y_*diff.y_ );

                        if ( pos.x_ < 0 || pos.y_ < 0 || pos.x_ >= terrHeightMap->GetWidth() || pos.y_ >= terrHeightMap->GetHeight() )
                        {
                            continue;
                        }

                        if ( fPixRadiusSq > fCircleRadiusSq )
                        {
                            continue;
                        }

                        avgColor += terrHeightMap->GetPixel( pos.x_, pos.y_ );
                        iAvgCnt++;
                    }
                }
                
                if ( iAvgCnt )
                {
                    avgColor = avgColor * (1.0f / (float)iAvgCnt);
                }

                // flatten height
                bFlattenHeightSet = true;
                flattenColor = avgColor;
            }

            // modify
            for ( int y = 0; y < terrModRadius; ++y )
            {
                for ( int x = 0; x < terrModRadius; ++x )
                {
                    IntVector2 pos = IntVector2( x + startPosLeft, y + startPosTop );
                    IntVector2 diff = pixelPos - pos;
                    float fPixRadiusSq = (float)( diff.x_*diff.x_ + diff.y_*diff.y_ );

                    if ( pos.x_ < 0 || pos.y_ < 0 || pos.x_ >= terrHeightMap->GetWidth() || pos.y_ >= terrHeightMap->GetHeight() )
                    {
                        continue;
                    }

                    if ( fPixRadiusSq > fCircleRadiusSq )
                    {
                        continue;
                    }

                    // move the point more towards where the gradient will be darker
                    fPixRadiusSq += fCircleRadiusSq * 0.4f;
                    if ( fPixRadiusSq > fCircleRadiusSq )
                    {
                        fPixRadiusSq = fCircleRadiusSq;
                    }

                    #ifdef DBG_DRAW_PIX_LINES
                    // **dbg show pix lines
                    Vector3 vRpos = InvWorldToHeightMap( pos );
                    m_vHtPos.Push( vRpos );
                    #endif

                    // get pix and gradient
                    Color htColor = (terrMode!=kTerrainMode_Paint) ? terrHeightMap->GetPixel( pos.x_, pos.y_ ) : colorMap_->GetPixel( pos.x_, pos.y_ );
                    int iGradPos = (int)( (float)(m_pImageGraient->GetWidth() - 1) * fPixRadiusSq/fCircleRadiusSq );
                    Color grdColor = m_pImageGraient->GetPixel( iGradPos, 0 );

                    // history pix
                    HistoryData histData;
                    histData.doneAndMode = terrMode;
                    histData.pos = pos;
                    histData.color = htColor;
                    InsertHistData( histData );
            
                    // edit
                    switch ( terrMode )
                    {
                    case kTerrainMode_Increase:
                        htColor += grdColor * fScaler;
                        break;

                    case kTerrainMode_Decrease:
                        htColor += grdColor * -fScaler;
                        break;

                    case kTerrainMode_Smooth:
                        htColor += (avgColor - htColor) * grdColor.Average() * fScaler;
                        break;

                    case kTerrainMode_Flatten:
                        htColor = flattenColor;
                        break;

                    case kTerrainMode_SetHeight:
                        htColor = scalerColor;
                        break;

                    case kTerrainMode_Paint:
                        {
                            float fIncrAvg = grdColor.Average() * fScaler;

                            // paint
                            switch ( m_iTerrPaintMode )
                            {
                            case kPaintWeight_Red:
                                htColor = htColor * ( 1.0f - fIncrAvg ) + Color::RED * fIncrAvg;
                                break;

                            case kPaintWeight_Green:
                                htColor = htColor * ( 1.0f - fIncrAvg ) + Color::GREEN * fIncrAvg;
                                break;

                            case kPaintWeight_Blue:
                                htColor = htColor * ( 1.0f - fIncrAvg ) + Color::BLUE * fIncrAvg;
                                break;
                            }
                        }
                        break;
                    }
            
                    // update pix
                    if ( terrMode != kTerrainMode_Paint )
                    {
                        terrHeightMap->SetPixel( pos.x_, pos.y_, htColor );
                    }
                    else
                    {
                        colorMap_->SetPixel( pos.x_, pos.y_, htColor );
                    }
                }
            }

            // refresh
            if ( terrMode != kTerrainMode_Paint )
            {
                terrain_->ApplyHeightMap();
            }
            else
            {
                colorMap_->ApplyColorMap() ;
            }
        }
        else
        {
            bFlattenHeightSet = false;
        }
    }
}

//=============================================================================
// the same function in terrain.cpp has bugs -- this change was added to the head of master branch
//=============================================================================
IntVector2 TerrainEdit::WorldToHeightMap(const Vector3& worldPosition) const
{
    if ( !terrainNode_ || !terrain_ )
    {
        return IntVector2::ZERO;
    }

    Vector3 position = terrainNode_->GetWorldTransform().Inverse() * worldPosition;
    int xPos = (int)((position.x_ - patchWorldOrigin_.x_) / spacing_.x_ + 0.5f);
    int zPos = (int)((position.z_ - patchWorldOrigin_.y_) / spacing_.z_ + 0.5f);
    xPos = Clamp(xPos, 0, numVertices_.x_ - 1);
    zPos = Clamp(zPos, 0, numVertices_.y_ - 1);

    return IntVector2(xPos, numVertices_.y_ - 1 - zPos);
}

//=============================================================================
// reverse function of the WorldToHeightMap()
//=============================================================================
Vector3 TerrainEdit::InvWorldToHeightMap(const IntVector2& pixelPosition) const
{
    if ( !terrainNode_ || !terrain_ )
    {
        return Vector3::ZERO;
    }

    IntVector2 v2pos( pixelPosition.x_, numVertices_.y_ - 1 - pixelPosition.y_ );
    float xPos = (float)(v2pos.x_ * spacing_.x_ + patchWorldOrigin_.x_);
    float zPos = (float)(v2pos.y_ * spacing_.z_ + patchWorldOrigin_.y_);
    Vector3 Lpos( xPos, 0, zPos );
    Vector3 WPos = terrainNode_->GetWorldTransform() * Lpos;
    WPos.y_ = terrain_->GetHeight( WPos );

    return WPos;
}

//=============================================================================
//=============================================================================
bool TerrainEdit::Raycast(float maxDistance, Vector3& hitPos)
{
    UI* ui = GetSubsystem<UI>();
    Graphics* graphics = GetSubsystem<Graphics>();
    IntVector2 pos = ui->GetCursorPosition();

    // Check the cursor is visible and there is no UI element in front of the cursor
    if ( !ui->GetCursor()->IsVisible() || ui->GetElementAt(pos, true) )
    {
        return false;
    }
    
    Camera* camera = cameraNode_->GetComponent<Camera>();
    Ray cameraRay = camera->GetScreenRay((float)pos.x_ / graphics->GetWidth(), (float)pos.y_ / graphics->GetHeight());
    // Pick only geometry objects, not eg. zones or lights, only get the first (closest) hit
    PODVector<RayQueryResult> results;
    RayOctreeQuery query(results, cameraRay, RAY_TRIANGLE, maxDistance, DRAWABLE_GEOMETRY);
    scene_->GetComponent<Octree>()->RaycastSingle(query);

    if ( results.Size() )
    {
        RayQueryResult& result = results[0];

        if ( result.drawable_->GetType() != TerrainPatch::GetTypeStatic() )
        {
            return false;
        }

        hitPos = result.position_;

        #ifdef DBG_TERRAIN_POS
        //** WorldToHeightMap() func returns a pixel position that is pixel aligned, which means it's not exactly the world 
        // position that we give it, so we're going to convert the pixel pos back to world position and use that as the hitPos
        IntVector2 pixelPos = WorldToHeightMap( hitPos );
        hitPos = InvWorldToHeightMap( pixelPos );
        terrRayText->SetText( "Pix Pos:" + String( pixelPos.x_ ) + "," + String( pixelPos.y_ ) );
        #endif

        #ifdef DBG_DRAW_PIX_LINES
        // **dbg render pix lines
        for ( unsigned i = 0; i < m_vHtPos.Size(); ++i )
        {
            dbgRenderer->AddLine( m_vHtPos[ i ], m_vHtPos[ i ] + Vector3::UP * 2.0f, Color::BLUE );
        }
        #endif

        dbgRenderer->AddLine( result.position_, result.position_ + Vector3::UP * 2.0f, Color::BLACK );
        dbgRenderer->AddLine( hitPos, hitPos + Vector3::UP * 2.0f, Color::RED );
        Sphere sph( hitPos, terrRadius );
        dbgRenderer->AddSphere( sph, Color::GREEN );
    }
    
    return ( results.Size() > 0 );
}

//=============================================================================
//=============================================================================
void TerrainEdit::HandleUpdate(StringHash eventType, VariantMap& eventData)
{
    using namespace Update;

    Input *input = GetSubsystem<Input>();
    UI *ui = GetSubsystem<UI>();

    // exit if the UI has a focused element (the console)
    if ( ui->GetFocusElement() )
    {
        return;
    }

    // mouse
    MouseMove( eventData[P_TIMESTEP].GetFloat() );

    // history
    if ( input->GetKeyDown( 'Z' ) )
    {
        UndoHistory();
    }
    else
    {
        // update terrain
        UpdateTerrMode();

        EditTerrain();

        if ( input->GetKeyDown( KEY_F11 ) )
        {
            SaveHeightMapImage();
        }

        if ( input->GetKeyDown( KEY_F12 ) )
        {
            SaveColorMapImage();
        }
    }
}

//=============================================================================
//=============================================================================
void TerrainEdit::SaveHeightMapImage()
{
    if ( terrain_ && terrain_->GetHeightMap() )
    {
        String filename = GetSubsystem<FileSystem>()->GetProgramDir() + "Data/Textures/HeightMapNew01.png";
        terrain_->GetHeightMap()->SavePNG( filename );
    }
}

//=============================================================================
//=============================================================================
void TerrainEdit::SaveColorMapImage()
{
    if ( colorMap_ )
    {
        String filename = GetSubsystem<FileSystem>()->GetProgramDir() + "Data/Textures/TerrainColorMap01.png";
        colorMap_->SavePNG( filename );
    }
}

//=============================================================================
//=============================================================================
void TerrainEdit::InsertHistData(HistoryData &histData)
{
    historyBuf[ historyInIdx ] = histData;

    ++historyInIdx %= kHistoryBufSize;

    // move the starting idx forward if the in-ptr has completely wrapped
    if ( historyInIdx == historyStartIdx )
    {
        ++historyStartIdx %= kHistoryBufSize;

        // set the terminator flag
        historyBuf[ historyStartIdx ].doneAndMode |= kHistoryMask_Done;
    }
}

//=============================================================================
//=============================================================================
void TerrainEdit::UndoHistory()
{
    if ( historyStartIdx != historyInIdx )
    {
        // control paint undo rate - allow a chance to single step
        if ( m_TimerPaintUndoRate.GetMSec( false ) < PAINT_UNDO_RATE )
        {
            return;
        }

        if ( --historyInIdx < 0 )
        {
            historyInIdx = kHistoryBufSize - 1;
        }

        // the pattern here is pix, ..., pix, done flag, where a done flag marks a single undo
        while ( !( historyBuf[ historyInIdx ].doneAndMode & kHistoryMask_Done ) )
        {
            if ( (historyBuf[ historyInIdx ].doneAndMode & kHistoryMask_Mode) != kTerrainMode_Paint)
            {
                terrain_->GetHeightMap()->SetPixel( historyBuf[ historyInIdx ].pos.x_,
                                                    historyBuf[ historyInIdx ].pos.y_, 
                                                    historyBuf[ historyInIdx ].color );
            }
            else
            {
                colorMap_->SetPixel( historyBuf[ historyInIdx ].pos.x_, 
                                     historyBuf[ historyInIdx ].pos.y_,
                                     historyBuf[ historyInIdx ].color );
            }

            if ( --historyInIdx < 0 )
            {
                historyInIdx = kHistoryBufSize - 1;
            }
        }

        // refresh
        if ( (historyBuf[ historyInIdx ].doneAndMode & kHistoryMask_Mode) != kTerrainMode_Paint)
        {
            terrain_->ApplyHeightMap();
        }
        else
        {
            colorMap_->ApplyColorMap();

            // reset undo timer
            m_TimerPaintUndoRate.Reset();
        }
    }
}

//=============================================================================
//=============================================================================
void TerrainEdit::MouseMove(float timeStep)
{
    // Right mouse button controls mouse cursor visibility: hide when pressed
    UI* ui = GetSubsystem<UI>();
    Input* input = GetSubsystem<Input>();
    ui->GetCursor()->SetVisible(!input->GetMouseButtonDown(MOUSEB_RIGHT));

    // Movement speed as world units per second
    const float MOVE_SPEED = 80.0f;
    // Mouse sensitivity as degrees per pixel
    const float MOUSE_SENSITIVITY = 0.1f;

    // Use this frame's mouse motion to adjust camera node yaw and pitch. Clamp the pitch between -90 and 90 degrees
    // Only move the camera when the cursor is hidden
    if (!ui->GetCursor()->IsVisible())
    {
        IntVector2 mouseMove = input->GetMouseMove();
        yaw_ += MOUSE_SENSITIVITY * mouseMove.x_;
        pitch_ += MOUSE_SENSITIVITY * mouseMove.y_;
        pitch_ = Clamp(pitch_, -90.0f, 90.0f);

        // Construct new orientation for the camera scene node from yaw and pitch. Roll is fixed to zero
        cameraNode_->SetRotation(Quaternion(pitch_, yaw_, 0.0f));
    }

    // Read WASD keys and move the camera scene node to the corresponding direction if they are pressed
    if (input->GetKeyDown('W'))
        cameraNode_->Translate(Vector3::FORWARD * MOVE_SPEED * timeStep);
    if (input->GetKeyDown('S'))
        cameraNode_->Translate(Vector3::BACK * MOVE_SPEED * timeStep);
    if (input->GetKeyDown('A'))
        cameraNode_->Translate(Vector3::LEFT * MOVE_SPEED * timeStep);
    if (input->GetKeyDown('D'))
        cameraNode_->Translate(Vector3::RIGHT * MOVE_SPEED * timeStep);
}

//=============================================================================
//=============================================================================
Slider* TerrainEdit::CreateSlider(int x, int y, int xSize, int ySize, const String& text)
{
    UIElement* root = GetSubsystem<UI>()->GetRoot();
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    Font* font = cache->GetResource<Font>("Fonts/Anonymous Pro.ttf");
    root->SetDefaultStyle( cache->GetResource<XMLFile>("UI/DefaultStyle.xml") );

    // add a transparent window around the slider to expand the 
    // ui focus area and minimize accidental terrain editing
    Window *pWin = root->CreateChild<Window>();
    root->AddChild( pWin );
    pWin->SetPosition( x - 20, y - 40 );
    pWin->SetSize( xSize+40, ySize+80 );
    pWin->SetColor( Color( 1, 1, 1, 0) );

    Slider* slider = pWin->CreateChild<Slider>();
    slider->SetStyleAuto();
    slider->SetPosition( 20, 50);
    slider->SetSize(xSize, ySize);
    slider->SetRange( 1.0f );
 
    m_pTextSliderDesc = slider->CreateChild<Text>();
    m_pTextSliderDesc->SetPosition( 0, -20 );
    m_pTextSliderDesc->SetFont(font, 12);
    m_pTextSliderDesc->SetText(text);
    m_pTextSliderDesc->SetColor(Color::YELLOW);
    
    m_pTextSliderVal = slider->CreateChild<Text>();
    m_pTextSliderVal->SetPosition( xSize/2, 20 );
    m_pTextSliderVal->SetFont(font, 12);
    m_pTextSliderVal->SetText( "0.5" );
    m_pTextSliderVal->SetColor(Color::YELLOW);
    
    return slider;
}

//=============================================================================
//=============================================================================
void TerrainEdit::HandleSliderChanged(StringHash eventType, VariantMap& eventData)
{
    using namespace SliderChanged;
    
    float fVal = eventData[P_VALUE].GetFloat();
    fVal = Clamp( fVal, 0.0f, 1.0f );
    scalerColor = Color( fVal, fVal, fVal );

    char buf[10];
    sprintf( buf, "%5.3f", fVal );
    m_pTextSliderVal->SetText( String( buf ) );
}

//=============================================================================
//=============================================================================
void ColorMap::SetSourceColorMap(Texture2D *_pTexture2DSource)
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    SharedPtr<Image> imageSource;

    m_pTexture2DSource = _pTexture2DSource;
    imageSource = cache->GetResource<Image>( m_pTexture2DSource->GetName() );

    SetSize( imageSource->GetWidth(), imageSource->GetHeight(), imageSource->GetDepth(), imageSource->GetComponents() );
    SetData( imageSource->GetData() );
}

//=============================================================================
//=============================================================================
void ColorMap::ApplyColorMap()
{
    if ( m_pTexture2DSource )
    {
        m_pTexture2DSource->SetData( 0, 0, 0, GetWidth(), GetHeight(), GetData() );
    }
}



[/code]
[b]TerranEdit.h[/b]
[code]
//
// Copyright (c) 2008-2015 the Urho3D project.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.
//

#pragma once

#include "Sample.h"

namespace Urho3D
{

class Node;
class Scene;

}
//=============================================================================
//=============================================================================
class ColorMap : public Image
{
    OBJECT(ColorMap);

public:
    ColorMap(Context *_pContext) 
        : Image( _pContext )
        , m_pTexture2DSource( NULL )
    {
    }

    virtual ~ColorMap()
    {
        m_pTexture2DSource = NULL;
    }

    void SetSourceColorMap(Texture2D *_pTexture2DOrigin);
    void ApplyColorMap();

protected:
    SharedPtr<Texture2D> m_pTexture2DSource;
};

//=============================================================================
//=============================================================================
class TerrainEdit : public Sample
{
    OBJECT(TerrainEdit);

    enum TerrainMode
    {
        kTerrainMode_Increase,
        kTerrainMode_Decrease,
        kTerrainMode_Smooth,
        kTerrainMode_Flatten,
        kTerrainMode_SetHeight,
        kTerrainMode_Paint,
        kTerrainMode_End,
    };

    enum PaintWeight
    {
        kPaintWeight_Red,
        kPaintWeight_Green,
        kPaintWeight_Blue,
        kPaintWeight_End,
    };

    enum HistorySize
    {
        kHistoryBufSize = 200000 // this seems huge but it's not when the sphere radius is at max
    };

    enum HistoryMasks
    {
        kHistoryMask_Mode = 0xf,
        kHistoryMask_Done = 0x80000000,
    };

    struct HistoryData
    {
        HistoryData() : doneAndMode( 0 ){}
        
        unsigned int doneAndMode;
        IntVector2   pos;
        Color        color;
    };

public:
    /// Construct.
    TerrainEdit(Context* context);
    virtual ~TerrainEdit()
    {
        if ( colorMap_ )
        {
            delete colorMap_;
            colorMap_ = NULL;
        }
    }
    
    /// Setup after engine initialization and before running the main loop.
    virtual void Setup();
    virtual void Start();
    
private:
    /// Create static scene content.
    void CreateScene();
    /// Construct an instruction text to the UI.
    void CreateInstructions();
    /// Subscribe to necessary events.
    void SubscribeToEvents();
    /// Handle application update.
    void HandleUpdate(StringHash eventType, VariantMap& eventData);
    
    void EditTerrain();
    void UpdateTerrMode();
    void UpdateTerrainSetText();
    IntVector2 WorldToHeightMap(const Vector3& worldPosition) const;
    Vector3 InvWorldToHeightMap(const IntVector2& pixelPosition) const;
    bool Raycast(float maxDistance, Vector3& hitPos);
    void SaveHeightMapImage();
    void SaveColorMapImage();
    void InsertHistData(HistoryData &histData);
    void UndoHistory();
    void MouseMove(float timeStep);

    Slider* CreateSlider(int x, int y, int xSize, int ySize, const String& text);
    void HandleSliderChanged(StringHash eventType, VariantMap& eventData);

private:
    DebugRenderer *dbgRenderer;

    // terrain
    SharedPtr<Terrain> terrain_;
    float       terrRadius;
    int         terrMode;

    Text        *terrText;
    float       terrMinSphSize;
    float       terrMaxSphSize;

    SharedPtr<Image> m_pImageGraient;

    // dbg - same vars from terrain.cpp/.h
    SharedPtr<Node> terrainNode_;
    int patchSize_;
    Vector3 spacing_;
    IntVector2 numPatches_;
    IntVector2 numVertices_;
    Vector2 patchWorldSize_;
    Vector2 patchWorldOrigin_;

    Vector<Vector3> m_vHtPos;
    Text        *terrRayText;

    // paint texture
    ColorMap        *colorMap_;
    int             m_iTerrPaintMode;

    // timers
    Timer           m_TimerColorMap;
    Timer           m_TimerDebounce;
    Timer           m_TimerPaintUndoRate;

    // history - using a circular FILO with a moving start idx
    HistoryData historyBuf[ kHistoryBufSize ]; // 28 bytes * 200k = 5.34 MB, radius of 40 will push 1600 hist data each iteration 
                                               // and thus results in -> 200k buffer / 1601 hist data = 125 iterations 
                                               // minimum undo cnt = 125 at radius of 40
                                               // maximum undo cnt = 40k at radius of 2
    int historyStartIdx;
    int historyInIdx;

    // slider
    SharedPtr<Slider> m_pSliderScaler;
    SharedPtr<Text>   m_pTextSliderDesc;
    SharedPtr<Text>   m_pTextSliderVal;

    Color       scalerColor;
    Color       flattenColor;
    bool        bFlattenHeightSet;


};



[/code][/spoiler]

Video
[video]https://www.youtube.com/watch?v=1yCcTjSnaG4[/video]

Edit: June 3, 2016 - added a googledrive link for binary release.

-------------------------

Lumak | 2017-01-02 01:10:00 UTC | #2

Changed the code a bit and added gradient using Ramp.png.  I think it works better, maybe.

-------------------------

esak | 2017-01-02 01:10:00 UTC | #3

Very nice!  :smiley: 

I think this should be added to the official Urho3D samples.

Are you going to work with painting the terrain also? With this addition I think this is a very useful tool.

-------------------------

Lumak | 2017-01-02 01:10:01 UTC | #4

I will be adding the texture paint feature. Not sure when, though.

I think this implementation works okay, but I have nothing to compare it to.  
There should be a minor adjustment that should be made is in the smoothing section, where:
[code]
                    case kTerrainMode_Smooth:
                        htColor += (avgColor - htColor) * grdAvg * INCREMENTAL_VALUE;
                        break;
[/code]

should be changed to
[code]
                    case kTerrainMode_Smooth:
                        htColor += (avgColor - htColor) * grdAvg * 0.05f; // maybe even a bit higher -- play with it and see
                        break;
[/code]

-------------------------

Lumak | 2017-01-02 01:10:01 UTC | #5

Source and header files updated. rewrote WorldToHeightMap() locally due to the one in terrain.cpp had bugs: rounding and index offset error

-------------------------

rasteron | 2017-01-02 01:10:02 UTC | #6

Nice feature! Generally, I'm using 3rd party tools for this type of stuff, but I think this will make a good addition with the default Urho3D editor. :slight_smile:

-------------------------

Lumak | 2017-01-02 01:10:02 UTC | #7

[quote="rasteron"]Nice feature! Generally, I'm using 3rd party tools for this type of stuff, but I think this will make a good addition with the default Urho3D editor. :slight_smile:[/quote]

Thanks. I had nothing to work with and found painting a heightmap in photoshop was just too time consuming to see it come out wrong. This will help me shape the terrain much faster.

-------------------------

Lumak | 2017-01-02 01:10:03 UTC | #8

Updated source and header - added history for undo edit

-------------------------

Lumak | 2017-01-02 01:10:03 UTC | #9

Updated source and header - added a terrain paint feature - paints the terrainWeight image, not the details.

The terrainWeight image does not work with DDS file, use png or jpg.

-------------------------

Lumak | 2017-01-02 01:10:05 UTC | #10

Final edit on source and header.

End of post.

-------------------------

Lumak | 2017-01-02 01:10:10 UTC | #11

Ok, maybe not the end of post.  I did get a chance to look into other engine's terrain editor and found there are additional editing functions such as 'flatten' and 'set height'.
I think those functions are useful.  I won't be adding those features anytime soon, but all the fixed INCREMENTAL_XX values should also be exposed and have them user controlled.  
Need to wrap all the features and setting in something like TurboBadger would be nice.

-------------------------

Lumak | 2017-01-02 01:10:10 UTC | #12

I guess there wouldn't be a point of doing this if Atomic Game Engine already has a terrain editor.

-------------------------

thebluefish | 2017-01-02 01:10:10 UTC | #13

[quote="Lumak"]I guess there wouldn't be a point of doing this if Atomic Game Engine already has a terrain editor.[/quote]

Their editor has a much more restrictive license. I certainly wouldn't want to fork it if I planned to keep my stuff open source and under a permissive license.

-------------------------

Lumak | 2017-01-02 01:10:10 UTC | #14

[quote="thebluefish"]

Their editor has a much more restrictive license. I certainly wouldn't want to fork it if I planned to keep my stuff open source and under a permissive license.[/quote]

I see your point.  But what I was getting at was that Atomic/jenge already has a TB level editor, and even though I haven't use it, it looks pretty good and having a terrain editor feature would be an integral part of his editor, if it doesn't have one already.  No need to have multiple variations of Urho3D TB terrain editors is what I was getting at.

Of course, what I have submitted on this thread is open source and anyone can wrap it with a fancy gui or enhance it however they like.

-------------------------

thebluefish | 2017-01-02 01:10:10 UTC | #15

[quote="Lumak"]Of course, what I have submitted on this thread is open source and anyone can wrap it with a fancy gui or enhance it however they like.[/quote]

This is why I appreciate everything you've released so far man  :smiley:

-------------------------

weitjong | 2017-01-02 01:10:10 UTC | #16

Not intended to steal the thunder but there is also another terrain editor implemented by JTippetts which support 8-detail tri-planar shaders for both HLSL and GLSL. One can only hope that someone would step forward to put all the good bits into one place, preferably in current Urho3D editor.

-------------------------

rasteron | 2017-01-02 01:10:10 UTC | #17

[quote="weitjong"]Not intended to steal the thunder but there is also another terrain editor implemented by JTippetts which support 8-detail tri-planar shaders for both HLSL and GLSL. One can only hope that someone would step forward to put all the good bits into one place, preferably in current Urho3D editor.[/quote]

Agreed and looking forward to this as well. :slight_smile:

[quote="Lumak"]Thanks. I had nothing to work with and found painting a heightmap in photoshop was just too time consuming to see it come out wrong. This will help me shape the terrain much faster.[/quote]

I have made a post [url=http://discourse.urho3d.io/t/free-terrain-editors/1790/1]resource here[/url] about a few free terrain editors that I have tested since I got started, but still having an integrated terrain editor in Urho3D would be awesome! :slight_smile:

-------------------------

Lumak | 2017-01-02 01:10:16 UTC | #18

Final source edit - added flatten, set height, and scaler.

I just saw JTippets terrain editor in Showcase.  That editor looks nice and more extensive than what I have here.  You may want to give that a try.

-------------------------

Lumak | 2017-01-02 01:10:17 UTC | #19

One last minor tweak.

-------------------------

Lumak | 2017-01-02 01:10:17 UTC | #20

History bug fix.

-------------------------

Lumak | 2017-01-02 01:10:21 UTC | #21

source change: clean up and added a transparent window around the slider to increase UI focus area.

-------------------------

Lumak | 2017-01-02 01:12:47 UTC | #22

I decide to wrap this with Urho GUI stuff (direct port of some editor's .as code). Something that I'll be using often due to an offroad racing game I'm attempting to make.

pic - best icons I ever made  :wink: 
[img]http://i.imgur.com/1aXemfH.jpg?1[/img]

-------------------------

Lumak | 2017-01-02 01:12:52 UTC | #23

Windows beta release - [url=http://wikisend.com/download/468018/TerrainEditor.zip]TerrainEditor.zip[/url].
Unzip it in your [b][color=#0000FF]<Urho3D project>/bin[/color][/b] folder.

Provide any feedback, thx.

-------------------------

namic | 2017-01-02 01:12:52 UTC | #24

Linux?  :smiley:

-------------------------

Lumak | 2017-01-02 01:12:53 UTC | #25

I'd probably release the linux version much later.  For now, I'm just creating a tool that I need to create my game, but I wouldn't mind sharing it.

-------------------------

TheComet | 2017-01-02 01:12:54 UTC | #26

This looks pretty cool, nice job!

-------------------------

Modanung | 2017-01-02 01:12:54 UTC | #27

[quote="Lumak"]I'd probably release the linux version much later. For now, I'm just creating a tool that I need to create my game, but I wouldn't mind sharing it.[/quote]
Does sharing it mean you're planning on making it open-source? If you do people could compile it for any supported platform, and send in pull requests on top of that. :slight_smile:
Looks good.

-------------------------

Lumak | 2017-01-02 01:12:54 UTC | #28

[quote]Does sharing it mean you're planning on making it open-source?[/quote]

I will eventually. Working on tools is not my favorite thing to do, and I don't think it is for most ppl either - it's a necessity, hah.  If I thought someone was eager to work on this then I'd open source it sooner.

As it stands, there are some algorithms that I still don't like and will be writing some experimental code to see it works any better. One example is smoothing, the getsmoothpixel() function found in terrain.cpp - which is a common function in terrain editing, so I found.  While the operation works okay when the y_ spacing is <= 0.4f, it falls apart when > ~0.6f, and very obvious when y_ >= 1.0f.  Also, I'd like to add some terraform processes to transform the entire heightmap instead of just using brush operations.  

And lastly, the gui code is direct port of Editor.as code and all its related .as code, and I've only ported small portion of the entire thing.  What I've ported requires some restructuring and refactoring. I'd love it if I can port the entire .as code to c++. I gotta admit that I've learned a lot more about what's in the engine what other features/functionalities are in it by porting the .as code.

-------------------------

Lumak | 2017-01-02 01:13:01 UTC | #29

Latest update: terraform generation, terrain height layer auto-coloring, minor fixes and added more error checking.

Windows and Linux binary release - [url=http://wikisend.com/download/424486/TerrainEdit.zip]TerrainEdit.zip[/url]

Unzip in your <URHO3D/projects>/bin folder, as before.

pics:

[imgur.com/a/yT3ye](http://imgur.com/a/yT3ye)

Edit: June 25, 2016 - updated the binary release to include Windows and Linux.

-------------------------

vovchik7ful | 2017-01-02 01:13:05 UTC | #30

When the file is no link, please post it on Google drive.

-------------------------

Modanung | 2017-01-02 01:13:05 UTC | #31

[quote="vovchik7ful"]When the file is no link, please post it on Google drive.[/quote]
...or any other cloud service. Preferably one that respects people's privacy. The zip download doesn't work for me either.

-------------------------

Lumak | 2017-01-02 01:13:06 UTC | #32

Posted a google drive link on the first page.

-------------------------

vovchik7ful | 2017-01-02 01:13:06 UTC | #33

[quote="Lumak"]Posted a google drive link on the first page.[/quote]
Many thanks!  :sunglasses:

-------------------------

