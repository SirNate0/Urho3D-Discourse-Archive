Xero | 2017-01-02 00:58:16 UTC | #1

im not exactly sure how to use the shader system in urho. I have written a post processed shader but not sure how to get it running in game. Can someone explain how its done?

-------------------------

friesencr | 2017-01-02 00:58:16 UTC | #2

the multiple viewport example (09_MultipleViewports) shows how to use post shaders.  they are attached to the viewport's renderpath.  there is a name that is registered via xml that you use to toggle the shader on/off but the example does it better justice then i can.

-------------------------

Xero | 2017-01-02 00:58:17 UTC | #3

ok thanks i will take a look

-------------------------

