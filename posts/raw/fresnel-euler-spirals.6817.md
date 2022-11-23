Modanung | 2021-04-19 23:08:19 UTC | #1

My witching experiments led me to *clothoids*. Has anyone here ever worked with these?

https://en.wikipedia.org/wiki/Euler_spiral

https://webee.technion.ac.il/~ayellet/Ps/10-HT.pdf

Apparently Inkscape _does_ use the technique I was looking for (spiro path) it just lacks controls.

-------------------------

SirNate0 | 2021-04-20 01:45:46 UTC | #2

I've not, but I came across them at some point when learning about Bezier curves. It might have been this thesis where I saw them mentioned, I'm not sure. In any case, it gives an intro to multiple splines/curves, so it might be a useful resource to you or someone else.

https://www.levien.com/phd/phd.html

-------------------------

Modanung | 2021-04-20 10:35:39 UTC | #3

Yes, I ran into that one as well. Apparently that is the implementation used by both Inkscape and FontForge. I don't think I like his recursive solver very much, but I might be missing something. Mainly the input method seems needlessly counterintuitive, while causing problems by effectively being too automated. But since these curves are so widely used (roads, train tracks, racing) and - to me - appear ubiquitous in nature, it might make sense to add them to the `Math` section. They'd be great for things like smooth paths, subdivisions and custom geometry.

----

[Here](https://luckeyproductions.nl/CurvePapers.zip)'s all eight possibly relevant papers I saved for study/reference.

-------------------------

Modanung | 2021-04-20 11:24:29 UTC | #4

...so I'm back to Processing:
![WitchCloth|690x453](upload://wcOGq09wR9gdyaicxHgwZit4syL.png)

-------------------------

Modanung | 2021-04-23 12:25:49 UTC | #5

Apparently Levien has been [working](https://raphlinus.github.io/curves/2018/12/21/new-spline.html) on his curves in the meantime. It addresses the "lack of controls" I mentioned, but not as I imagine. Based on the demo, I wouldn't call it an improvement... or clothoid.

> "_And, in fact, I don't just use the Euler spirals, I use a mixture of curves_ [...]" -- **Raph Levien**

-------------------------

