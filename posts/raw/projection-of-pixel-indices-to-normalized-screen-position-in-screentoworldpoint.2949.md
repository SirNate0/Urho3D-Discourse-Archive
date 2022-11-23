bobor | 2017-03-24 14:16:27 UTC | #1


Hi! I have question about the projection of xPixel yPixel pixels passed to `viewport.ScreenToWorldPoint(xPixel, yPixel, depth)` to normalized screen positions passed to `camera.ScreenToWorldPoint(Vector3(xPos, yPos, depth))`.

I would expect the projection this way:
    `xPos = (xPixel + 0.5f) / viewportWidth;`
    `yPos = (yPixel + 0.5f) / viewportHeight;`

The result positions are located in pixels' center. This can be an issue in precise mouse picking query (using GetScreenRay) when projecting to pixel corner. Is there any reason why the position is projected to the pixel corner?

Thanks for answer.

-------------------------

