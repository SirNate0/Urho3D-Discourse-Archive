1vanK | 2017-01-02 01:14:46 UTC | #1

In my tests it always has same values. When should I use GetQuadTexCoord, and when GetScreenPosPreDiv ?

-------------------------

cadaver | 2017-01-02 01:14:46 UTC | #2

GetScreenPos() is when you want to sample a "G-buffer" style whole viewport texture. On D3D9 this adds the half-pixel offset. 

GetQuadTexCoord() when you don't need to care of the half-pixel offset, for example sampling a downscaled blur texture.

The distinction used to be greater when in the past the G-buffer would be always same size as the destination texture. Now it's instead sized according to the viewport, so that if your viewport is smaller than the screen or texture, you don't have to fear that your sampling operations leak unwanted pixels from an adjacent viewport. So practically the transform uniform (GBufferOffsets) which used to do the view partitioning now just always returns 0 at the left edge and 1 at the right.

On OpenGL there indeed would be no difference what to use.

-------------------------

1vanK | 2017-01-02 01:14:46 UTC | #3

Thank you!

-------------------------

