ghidra | 2017-01-02 01:03:58 UTC | #1

Sometimes when I have a single mesh that has some polys that are close together I am getting weird depth sorting issues, where the back plane rendering infront of the front plane.

Is there a way to enforce precision of the depth sorting.

Now that I think about it, maybe its just a matter of lowering the far clipping plane of the camera. but maybe there is another better way.

-------------------------

weitjong | 2017-01-02 01:03:58 UTC | #2

Have you tried to adjust the depth bias? The SetDepthBias() method can be found in the Graphics subsystem.

I look up this subject in the internet and find this interesting article [aras-p.info/blog/2008/06/12/dept ... -yourself/](http://aras-p.info/blog/2008/06/12/depth-bias-and-the-power-of-deceiving-yourself/) (although it is quite dated now). It claims (or claimed) that there [b]was[/b] a defect in the D3D9 documentation on the depth bias value range. If I understand the article correctly then it says that OpenGL -1 is equivalent to D3D9 -1.0/(2^n-1) where n is the depth buffer bitdepth which could be 16 or 24. I then cross check the OGL/Graphics and D3D9/Graphics class implementation and found nothing in the code to account for this revelation. On the contrary, the comment in the OGL/Graphics::SetDepthBias() says it is the OpenGL that is dependent on the bitdepth and not the other way round. @cadaver So, which one is correct?

-------------------------

