SirNate0 | 2018-04-29 20:34:14 UTC | #1

I'm playing around with generating python bindings for urho using pybind11 and clang (to parse the source and automagically generate the bindings), and I was wondering what is the basis for exporting (or not) certain symbols, in this particular instance, Urho3D::String::NPOS (I get an ImportError undefined symbol "_ZN6Urho3D6String4NPOSE" when I try to import the created module). Should NPOS, for example, be exported?

-------------------------

