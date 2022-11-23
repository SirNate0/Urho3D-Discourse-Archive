rogerdv | 2017-01-02 01:01:52 UTC | #1

While editing my scenes I found that enabling "Per vertex" in the light properties disables shadows for everything. First I thought it was that intel gfraphics didnt support something, but later at home, I confirmed it with my R7 250. Why does this happens, are they mutually exclusive?

-------------------------

cadaver | 2017-01-02 01:01:52 UTC | #2

As the attribute name implies, it switches light calculation for that light completely to the vertex shader, while shadows are a (per-pixel) operation executed in the pixel shader, so the end result is that per vertex lights cannot produce shadows.

-------------------------

rogerdv | 2017-01-02 01:01:52 UTC | #3

then, whats the advantage of per vertex lights? Perhaps having better perfomance for lights that wont cast shadows?

-------------------------

cadaver | 2017-01-02 01:01:53 UTC | #4

Yes, better performance for
- simpler pixel shader code
- less batches in forward rendering (normally each per-pixel light is an additional additive pass, but vertex lights are all performed at once in the ambient pass)

The main concern is whether the effect of the light looks good enough with per vertex lighting. For example, if you have normal mapping and specular in your material, those will not be included in per vertex light calculations either, so it arguably looks uglier. Light attenuation will also be inaccurate, though this depends on how closely spaced your vertices are. For something like adjusting the ambient color subtly, vertex lights can work OK.

-------------------------

