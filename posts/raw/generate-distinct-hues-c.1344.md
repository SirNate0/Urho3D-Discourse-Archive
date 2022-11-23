jmiller | 2020-04-25 17:15:39 UTC | #1

My entry for most trivial but possibly useful code. :stuck_out_tongue:
Pass it a vector of Colors to fill, how many to generate, and specify fixed saturation, value, and alpha.

[code]
#include <cmath>

void GenerateDistinctHues(Vector<Color>& colors, unsigned num, float s, float v, float a) {
  // Fibonacci hashing: It is a property of the golden ratio that each subsequent hash value divides the interval into which it falls according to the golden ratio. I.e., consecutive hash keys are evenly spaced.
  const double golden_ratio_conjugate(0.618033988749895);
  double h(Random());
  for (unsigned i(0); i < num; ++i) {
    h += golden_ratio_conjugate;
    h = fmod(h, 1.0f);
    Color c;
    c.FromHSV(h, s, v, a);
    colors.Push(c);
  }
}
[/code]

Color constants from @SirNate0:
  https://discourse.urho3d.io/t/html-color-constants/6119

-------------------------

