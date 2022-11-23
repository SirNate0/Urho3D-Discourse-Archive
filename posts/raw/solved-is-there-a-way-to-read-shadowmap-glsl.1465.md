Bananaft | 2017-01-02 01:07:53 UTC | #1

I want to read values from shdowmap texture (directional light) in GLSL shader to compare it with fragment position "by hand" with some extra math. However because it set to GL_TEXTURE_COMPARE_MODE, it won't give you it's value, only comparison answer. Is there an easy way to hack this around? (preferably without changing engine sources)

-------------------------

cadaver | 2017-01-02 01:07:54 UTC | #2

How the shadow textures are setup is currently hardcoded. I recommend to just modify the engine and if you can make it as something that could be generally useful (and configurable) submit a PR.

Note that on D3D9 the comparison mode rather depends on the texture format, and on D3D11 the comparison mode and the sampler type need to match.

-------------------------

Bananaft | 2017-01-02 01:07:55 UTC | #3

Thanks for explanation. I ended up commenting " newShadowMap->SetShadowCompare(true);" line in Renderer.cpp. And that's was my first and only C++ coding experience. So, I'm far from making useful (and configurable) PRs. :slight_smile:

-------------------------

