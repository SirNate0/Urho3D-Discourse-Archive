Shylon | 2017-01-02 01:11:13 UTC | #1

how Can I get  Inverse Projection Matrix  in quad pass shader? I want to use GBuffers, also for world position should i create render-target?

-------------------------

jmiller | 2017-01-02 01:11:13 UTC | #2

[quote="Shylon"]how Can I get  Inverse Projection Matrix  in quad pass shader?[/quote]
I just wrote my own for a quad [url=http://discourse.urho3d.io/t/procsky/1168/1]shader[/url].
PS:
uniform mat4 cInvProj;

cam->GetProjection(false).Inverse(); // in this implementation, apiSpecific = false

-------------------------

Shylon | 2017-01-02 01:11:18 UTC | #3

Thank you, your code was very useful :slight_smile:, and my main problem was I should have set name on parameter in xml.

-------------------------

