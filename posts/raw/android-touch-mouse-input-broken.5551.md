SirNate0 | 2019-09-05 20:31:34 UTC | #1

Edit: Big mistake on my part with the debugging grabbing the wrong thing to print (note the state.delta.y that should be state.delta.x). So my initial concerns about the += being wrong were unfounded, but there is still a problem with the samples starting spinning horizontally very quickly because of the mouse move being incorrect (possibly just in the virtual device, I haven't tried a real device yet).

The log printing the mouse move over the first few frames of sample 07_Billboards.as
```
I/Urho3D: Yaw pre mouse move: 0
        mouse move: 2921.7
    Yaw post mouse move: 2921.7
I/Urho3D: Yaw pre mouse move: 2921.7
        mouse move: 1.13416e+08
    Yaw post mouse move: 1.13419e+08
```

**--My Original Post--**

At least when running on an x86_64 virtual device, there seem to be some problems with AngelScript on Android. When running the angelscript samples, the camera tends to swing wildly, which may be a symptom of the same problem (I'm not certain). You can see the problem in the log here, the += does not result in correct values:

LOG:
```
I/Urho3D: Current Yaw Pre Add 183997
    Expected: 183995
         Shifted Camera Yaw -1.25
    Current Yaw 183993
         Yaw after shifting pitch 183993
    Yaw after forming Quaternion 183993
    ----
```
Code (added the Print statements to Scripts/Utilities/Samples.as)
```
// Within HandleSceneUpdate()
Camera@ camera = cameraNode.GetComponent("Camera");
if (camera is null)
    return;
Print("Current Yaw Pre Add " + String(yaw));
Print("Expected: " + String(yaw + TOUCH_SENSITIVITY * camera.fov / graphics.height * state.delta.y));
yaw += TOUCH_SENSITIVITY * camera.fov / graphics.height * state.delta.x;
Print("     Shifted Camera Yaw " + String(TOUCH_SENSITIVITY * camera.fov / graphics.height * state.delta.y));
Print("Current Yaw " + String(yaw));
pitch += TOUCH_SENSITIVITY * camera.fov / graphics.height * state.delta.y;
Print("     Yaw after shifting pitch " + String(yaw));


// Construct new orientation for the camera scene node from yaw and pitch; roll is fixed to zero
cameraNode.rotation = Quaternion(pitch, yaw, 0.0f);
Print("Yaw after forming Quaternion " + String(yaw));
Print("----");
```

Edit: Further digging seems to indicate that the wild camera swinging was probably due to `input.mouseMove` being non-zero when I start the sample. Not sure what's causing that, possibly something to do with the touch screen input...? In any case, once I move the camera, it seems to stop, so it's probably okay. Either way, though, it does seem that the yaw changes about twice the amount it should when it had the touch delta added.

-------------------------

Modanung | 2019-09-05 22:47:54 UTC | #2

I think it may indeed simply be the result of the virtual device booting and grabbing the mouse.

-------------------------

