szamq | 2018-12-17 21:47:01 UTC | #1

I have successfully implemented Oculus Rift SDK in Urho3D. [gfycat.com/TightPlaintiveJumpingbean](https://gfycat.com/TightPlaintiveJumpingbean)
There are two things to talk about, if we want to create Oculus application:

[b]1. Rendering for Oculus[/b]
If you have Oculus Runtime installed on your PC then you know that Oculus supports two types of display modes: direct mode where application renders directly to oculus head mounted display, and extended mode where your Oculus display is recognized as additional monitor and all you have to do is to put our application window there and render. You need to render the scene twice, one time for left eye and the second one for the right eye, and the render results should be merged together side by side. I achieved that by creating two nodes with cameras with some offset and with specified Viewport(half a screen)
```
renderer.viewports[0] = Viewport(scene, left_eye_camera,IntRect(0, 0, graphics.width /2, graphics.height));  
renderer.viewports[1] = Viewport(scene, right_eye_camera,IntRect(graphics.width /2, 0,graphics.width, graphics.height)); 
```

this gives us stereo view on the screen and such setup already would work on oculus display tricking our eyes into 3d view. However, it would be nice to compensate the side effects of the lenses inside oculus. To achieve that I have modified oculus dk1 shader to match dk2( because dk2 doesn't use pixel shader to create the distortion, instead they are using some custom mesh with uv maps.

Here is the postprocess shader(only glsl).

```
#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"

varying vec4 vScreenPos;

uniform vec2 cScale;
uniform vec2 cScaleIn;
uniform vec4 cHmdWarpParam;
uniform vec4 cChromAbParam;
uniform vec2 cLensCenter;
uniform vec2 cScreenCenter;
uniform vec2 cOffset;


void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vScreenPos = GetScreenPos(gl_Position);
}


void PS()
{ 
   vec2 oTexCoord =  vScreenPos.xy*vec2(0.5,1.0)+cOffset;

   vec2 theta = (oTexCoord - cLensCenter) * cScaleIn; // cScales to [-1, 1]
   float rSq = theta.x * theta.x + theta.y * theta.y;
   vec2 theta1 = theta * (cHmdWarpParam.x + cHmdWarpParam.y * rSq +
   cHmdWarpParam.z * rSq * rSq +
   cHmdWarpParam.w * rSq * rSq * rSq);
   
   vec2 thetaBlue=theta1 * (cChromAbParam.z + cChromAbParam.w *rSq);
   vec2 tc = cLensCenter + cScale *  thetaBlue;
   
   vec2 distanceFromCenter=tc-cScreenCenter;

   // This "if" can be deleted
   if(distanceFromCenter.x<-0.25 || distanceFromCenter.y<-0.5 || distanceFromCenter.x>0.25 || distanceFromCenter.y>0.5)
   {
      gl_FragColor = vec4(vec3(0.0), 1.0);
      return;
   }
   
   float tint=min(min(min(clamp((distanceFromCenter.x+0.25 )*30.0,0.0,1.0),clamp((-distanceFromCenter.x+0.25 )*30.0,0.0,1.0))
   ,clamp((distanceFromCenter.y+0.5 )*30.0,0.0,1.0)),clamp((-distanceFromCenter.y+0.5 )*30.0,0.0,1.0));

   tc.x = 2.0 * (tc.x - cOffset.x);
   float blue= texture2D(sDiffMap, tc).b;
   
   float2 tcGreen= cLensCenter + cScale *  theta1;
   tcGreen.x = 2.0 * (tcGreen.x - cOffset.x);
   float green= texture2D(sDiffMap, tcGreen).g;
   
   float2 thetaRed= theta1 *(cChromAbParam.x + cChromAbParam.y *rSq);
   float2 tcRed= cLensCenter + cScale *  thetaRed;
   tcRed.x = 2.0 * (tcRed.x - cOffset.x);

   float red= texture2D(sDiffMap, tcRed).r;
   gl_FragColor = vec4(red*tint,green*tint,blue*tint, 1.0);
}
```

and the postprocess xml with parameters for dk2

```
<renderpath>
    <command type="quad" tag="BarrelDistortion" vs="BarrelDistortion" ps="BarrelDistortion" output="viewport">
        <parameter name="LensCenter" value="0.25 0.5" />
        <parameter name="ScreenCenter" value="0.25 0.5" />
        <parameter name="Offset" value="0.0 0.0" />
        <parameter name="Scale" value="0.1469278 0.2350845" />
        <parameter name="ScaleIn" value="4.2 2.35" />
        <parameter name="HmdWarpParam" value="1.0 0.22 0.24 0.0" />
        <parameter name="ChromAbParam" value="0.986 0.0124 1.029 0.0" />
        <texture unit="diffuse" name="viewport" />
    </command>
</renderpath>
```
one thing you want to set differently for the right camera renderpath is to set different shader parameters 
```
"ScreenCenter",Variant(Vector2(0.75,0.5)));
"LensCenter",Variant(Vector2(0.75,0.5)));
"Offset",Variant(Vector2(0.5,0.0)),2);
```

And that's all for the rendering, this gives us something like this image [github.com/OculusRiftInAction/O ... isplay.cpp](https://github.com/OculusRiftInAction/OculusRiftInAction/blob/master/examples/cpp/Example_2_3_Display.cpp) )


[b]2. Rotations/Position from Oculus[/b]

We know how to render and send the render result to oculus, but we need also interaction from oculus hmd to our application to get the head rotation and apply that to the cameras to see the interaction. Optionally, we can also use position from IR camera. I just added ovr_lib to my visual studio project and created very simple functions in urho input class and bindings to the angelscript.

```
//   input.h
    int SetupOculus();
    Quaternion GetOculusRotation();
    Vector3 GetOculusPosition();
    void RecenterPose();

//input.cpp

int Input::SetupOculus()
{
    if (!ovr_Initialize()) { 
          LOGINFO("Failed to initialize the Oculus SDK"); 
          return -1; 
      }

      hmd = ovrHmd_Create(0);
      if (!hmd || !ovrHmd_ConfigureTracking(hmd, ovrTrackingCap_Orientation| ovrTrackingCap_MagYawCorrection | ovrTrackingCap_Position, 0)) {
      LOGINFO("Unable to detect Rift head tracker");
      return -1;
    }

    return 0;
}
Quaternion Input::GetOculusRotation()
{
    ovrTrackingState state = ovrHmd_GetTrackingState(hmd, 0);  
    ovrQuatf orientation = state.HeadPose.ThePose.Orientation;
    return Quaternion(orientation.w,orientation.x,orientation.y,orientation.z);
}

Vector3 Input::GetOculusPosition()
{
    ovrTrackingState state = ovrHmd_GetTrackingState(hmd, 0);  
    ovrVector3f position = state.HeadPose.ThePose.Position;
    return Vector3(position.x,position.y,position.z);
}

void Input::RecenterPose()
{
    ovrHmd_RecenterPose(hmd); 
}

//inputAPI.cpp
    engine->RegisterObjectMethod("Input", "int SetupOculus()", asMETHOD(Input, SetupOculus), asCALL_THISCALL);
    engine->RegisterObjectMethod("Input", "int RecenterPose()", asMETHOD(Input, RecenterPose), asCALL_THISCALL);
    engine->RegisterObjectMethod("Input", "Quaternion GetOculusRotation()", asMETHOD(Input, GetOculusRotation), asCALL_THISCALL);
    engine->RegisterObjectMethod("Input", "Vector3 GetOculusPosition()", asMETHOD(Input, GetOculusPosition), asCALL_THISCALL);

```

and that's all. Pretty easy if we dont care about the direct to rift renderer. 
Let me know what you think

-------------------------

GoogleBot42 | 2017-01-02 01:04:33 UTC | #2

Nice!  Great job!   :wink:  :smiley:

-------------------------

yushli | 2017-01-02 01:11:26 UTC | #3

Thank you for sharing this. Any updates on this interesting topic?

-------------------------

