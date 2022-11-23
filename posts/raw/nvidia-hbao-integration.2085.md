franck22000 | 2017-01-02 01:12:55 UTC | #1

Hello, 

i am trying to implement Nvidia HBAO+ into urho3D and i got some questions :slight_smile: 

Here is the official online documentaiton: [docs.nvidia.com/gameworks/conten ... ng-started](http://docs.nvidia.com/gameworks/content/gameworkslibrary/visualfx/hbao/product.html#getting-started) (slightly outdated)

First i am initializing the library like that: 

[code]GFSDK_SSAO_CustomHeap _HBAOCustomHeap;
_HBAOCustomHeap.new_ = ::operator new;
_HBAOCustomHeap.delete_ = ::operator delete;

GFSDK_SSAO_Status _HBAOInitStatus;
_HBAOInitStatus = GFSDK_SSAO_CreateContext_D3D11(m_pGraphics->GetImpl()->GetDevice(), &m_pHBAOContext, &_HBAOCustomHeap);[/code]

Everything is fine and the library is initialized correctly. Then depth input information is asked.

[code]GFSDK_SSAO_InputData_D3D11 Input;
Input.DepthData.DepthTextureType = GFSDK_SSAO_VIEW_DEPTHS;
Input.DepthData.pFullResDepthTextureSRV = ???
Input.DepthData.ProjectionMatrix.Data = GFSDK_SSAO_Float4x4(this->GetMainCamera()->GetProjection().Transpose().Data());
Input.DepthData.ProjectionMatrix.Layout = GFSDK_SSAO_ROW_MAJOR_ORDER;
Input.DepthData.MetersToViewSpaceUnits = 1.0f;[/code]

Input.DepthData.DepthTextureType can be: 

[code]GFSDK_SSAO_HARDWARE_DEPTHS,                             // Non-linear depths in the range [0.f,1.f]
GFSDK_SSAO_HARDWARE_DEPTHS_SUB_RANGE,                   // Non-linear depths in the range [Viewport.MinDepth,Viewport.MaxDepth]
GFSDK_SSAO_VIEW_DEPTHS,                                 // Linear depths in the range [ZNear,ZFar][/code]

Input.DepthData.pFullResDepthTextureSRV is expecting a ID3D11ShaderResourceView*. [b]My question is how to get it from Urho3D[/b] ? 

Notes: I am using standard DX11 deferred renderpath and not deferred hardware depth renderpath.

Thank you for you help ! If i get this to work i will post the whole code in this forum. :slight_smile:

-------------------------

cadaver | 2017-01-02 01:12:56 UTC | #2

When you have Urho's Texture object, call GetShaderResourceView() on it when Urho is built for D3D11 API. This returns a void pointer which you can cast to the expected type.

Getting the texture is nontrivial, since the function in question (FindNamedTexture) is currently a private function in View, and textures may get arbitrarily reused between view renders on the same frame.

For now it's probably easiest creating the depth texture manually (in the same format as the renderpath does), giving it a name (for example "MyDepth"), storing it to the resource cache as a manual resource, and assigning the renderpath to refer to the texture by name. The renderpath should then look like this: (note that the renderpath no longer defines the depth texture by itself)

[code]
<renderpath>
    <rendertarget name="albedo" sizedivisor="1 1" format="rgba" />
    <rendertarget name="normal" sizedivisor="1 1" format="rgba" />
    <command type="clear" color="fog" depth="1.0" stencil="0" />
    <command type="scenepass" pass="deferred" marktostencil="true" vertexlights="true" metadata="gbuffer">
        <output index="0" name="viewport" />
        <output index="1" name="albedo" />
        <output index="2" name="normal" />
        <output index="3" name="MyDepth" />
    </command>
    <command type="lightvolumes" vs="DeferredLight" ps="DeferredLight">
        <texture unit="albedo" name="albedo" />
        <texture unit="normal" name="normal" />
        <texture unit="depth" name="MyDepth" />
    </command>
    <command type="scenepass" pass="postopaque" />
    <command type="scenepass" pass="refract">
        <texture unit="environment" name="viewport" />
    </command>
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
    <command type="scenepass" pass="postalpha" sort="backtofront" />
</renderpath>
[/code]

However the final hurdle will be to call the HBAO code during the view rendering, so that you're able to apply it to the final render. For this I don't have an easy answer, you likely have to modify Urho. For example, add a new renderpath command that does nothing, but just sends an event whose name you can configure. Then you'd call HBAO inside the event handler. It'd be a lot easier if Nvidia just gave the shader code that you could call inside a Urho quad postprocess command.

The "send event" renderpath command would be acceptable as a PR, by the way. You could also make View::FindNamedTexture public if it helps you. You can get the View object from the Viewport, but it may be null in case the viewport has never been rendered yet.

-------------------------

franck22000 | 2017-01-02 01:12:57 UTC | #3

Thanks for this detailled answers ! 

Pull requests for making FindNamedTexture() function public and for sending events in the render path would be quite usefull.

I will need to learn how to make PR's :slight_smile:

-------------------------

franck22000 | 2017-01-02 01:12:59 UTC | #4

I have done a pull request for the new renderpath command here: [github.com/urho3d/Urho3D/pull/1436](https://github.com/urho3d/Urho3D/pull/1436)

-------------------------

