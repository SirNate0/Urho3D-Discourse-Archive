codingmonkey | 2017-01-02 01:09:44 UTC | #1

I found that different types of light have different geometries I suppose for light optimization ?
so, spot light have this geometry

file: Renderer.cpp 
line: 150

static const float spotLightVertexData[] =
{
    0.00001f, 0.00001f, 0.00001f,
    0.00001f, -0.00001f, 0.00001f,
    -0.00001f, -0.00001f, 0.00001f,
    -0.00001f, 0.00001f, 0.00001f,
    1.00000f, 1.00000f, 0.99999f,
    1.00000f, -1.00000f, 0.99999f,
    -1.00000f, -1.00000f, 0.99999f,
    -1.00000f, 1.00000f, 0.99999f,
};

Is this some kind of frustum geometry ?
and if it are frustum, is area light must have cube default geometry in similar case ?

Edit:
I made this changes for this light geometry, I guessing what I'm right )
[code]
static const float areaLightVertexData[] =
{
    1.00000f, 1.00000f, 0.00001f,
    1.00000f, -1.00000f, 0.00001f,
    -1.00000f, -1.00000f, 0.00001f,
    -1.00001f, 1.00000f, 0.00001f,
    1.00000f, 1.00000f, 0.99999f,
    1.00000f, -1.00000f, 0.99999f,
    -1.00000f, -1.00000f, 0.99999f,
    -1.00000f, 1.00000f, 0.99999f,
};
[/code]

-------------------------

codingmonkey | 2017-01-02 01:09:45 UTC | #2

I prepare workable behavior for testing AreaLight and try to push new defines into shader (when I switch light from DirLight to AreaLight) but got LitSolid with empty definitions (only NOUV in VS)  
So what I'm doing wrong ?
[url=http://savepic.ru/8503505.htm][img]http://savepic.ru/8503505m.png[/img][/url]

I add new defs in 

[code]
void Renderer::SetLightVolumeBatchShaders(Batch& batch, Camera* camera, const String& vsName, const String& psName, const String& vsDefines,
    case LIGHT_AREA:
        psi += DLPS_AREA;
        break;

void Renderer::SetBatchShaders(Batch& batch, Technique* tech, bool allowShadows)
 case LIGHT_AREA:
                psi += LPS_AREA;
                vsi += LVS_AREA;
                break;

[/code]

[code]
static const char* lightVSVariations[] =
{
    "PERPIXEL DIRLIGHT ",
    "PERPIXEL SPOTLIGHT ",
    "PERPIXEL AREALIGHT ",
    "PERPIXEL POINTLIGHT ",
    "PERPIXEL DIRLIGHT SHADOW ",
    "PERPIXEL SPOTLIGHT SHADOW ",
    "PERPIXEL AREALIGHT SHADOW ",
    "PERPIXEL POINTLIGHT SHADOW ",
};

static const char* lightPSVariations[] =
{
    "PERPIXEL DIRLIGHT ",
    "PERPIXEL SPOTLIGHT ",
    "PERPIXEL AREALIGHT ",
    "PERPIXEL POINTLIGHT ",
    "PERPIXEL POINTLIGHT CUBEMASK ",
    "PERPIXEL DIRLIGHT SPECULAR ",
    "PERPIXEL SPOTLIGHT SPECULAR ",
    "PERPIXEL AREALIGHT SPECULAR ",
    "PERPIXEL POINTLIGHT SPECULAR ",
    "PERPIXEL POINTLIGHT CUBEMASK SPECULAR ",
    "PERPIXEL DIRLIGHT SHADOW ",
    "PERPIXEL SPOTLIGHT SHADOW ",
    "PERPIXEL AREALIGHT SHADOW ",
    "PERPIXEL POINTLIGHT SHADOW ",
    "PERPIXEL POINTLIGHT CUBEMASK SHADOW ",
    "PERPIXEL DIRLIGHT SPECULAR SHADOW ",
    "PERPIXEL SPOTLIGHT SPECULAR SHADOW ",
    "PERPIXEL AREALIGHT SPECULAR SHADOW ",
    "PERPIXEL POINTLIGHT SPECULAR SHADOW ",
    "PERPIXEL POINTLIGHT CUBEMASK SPECULAR SHADOW "
};

[/code]

-------------------------

