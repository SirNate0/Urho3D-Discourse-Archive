NiteLordz | 2017-01-02 01:12:43 UTC | #1

If you enable the debug layer for Direct3D 11, and try to run example SkeletalAnimation sample (others as well), you will see the Debug Layer output 

D3D11 WARNING: ID3D11DeviceContext::DrawIndexed: The Pixel Shader expects a Render Target View bound to slot 0, but none is bound. This is OK, as writes of an unbound Render Target View are discarded. It is also possible the developer knows the data will not be used anyway. This is only a problem if the developer actually intended to bind a Render Target View here. [ EXECUTION WARNING #3146081: DEVICE_DRAW_RENDERTARGETVIEW_NOT_SET]

To enable the debug layer

in file D3D11Graphics, modify the D3D11CreateDevice method call as follows

[code]HRESULT hr = D3D11CreateDevice(
            0,
            D3D_DRIVER_TYPE_HARDWARE,
            0,
			D3D11_CREATE_DEVICE_DEBUG,
            0,
            0,
            D3D11_SDK_VERSION,
            &impl_->device_,
            0,
            &impl_->deviceContext_
        );[/code]

-------------------------

cadaver | 2017-01-02 01:12:43 UTC | #2

I suspect this is from shadow rendering, which deliberately renders depth only. You can ignore this message.

-------------------------

NiteLordz | 2017-01-02 01:12:44 UTC | #3

Yea, have found that if shadows are disabled, then the messages no longer display.

-------------------------

