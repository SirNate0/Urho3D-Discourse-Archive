Xero | 2017-01-02 00:58:19 UTC | #1

Is there anyway to increase the shadow detail in the editor? Right now i am using a point light in my scene and all the shadows being cast look like black blobs

-------------------------

friesencr | 2017-01-02 00:58:19 UTC | #2

There are some parameters in the "Editor Settings" for the shadow map size/bit depth.  There are also settings on the lights for getting better results.  It is the CSM splits.  I don't understand what the CSM splits do so I can't help you there.

-------------------------

Xero | 2017-01-02 00:58:19 UTC | #3

thanks got better results, im sure the csm splits does something but i cant see a difference when using it

-------------------------

ZachGriffin | 2017-01-02 00:58:20 UTC | #4

CSM (Cascaded Shadow Mapping) allows you to segment the shadow texture so that more of the texture is given to shadows closer to the screen. i.e There is no point giving away a large amount of the texture to a shadow that only takes up 10 pixels. It allows for higher quality and sharper shadows closer to the camera. Adjusting the split (Any arbitrary amount although there are generally 4) distance sets how far away from the camera the drop in effective shadow resolution happens.

-------------------------

