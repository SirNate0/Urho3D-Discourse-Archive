slapin | 2017-03-19 16:04:48 UTC | #1

Hi, all! 
There is so nice piece in Urho which is left-out from documentation. It is really shame
there's no example on usage. It is so nice and powerful feature. I hope my post will help someone.
I'm using AngelScript below.

Well, first we create spline just by

    Spline sp;

Now we just need to add control point - they are called knots in Urho.

    Vector3 p1(0, 0, 1);
    Vector3 p2(0, 0, 0);
    Vector3 p3(1, 0, 0);
    sp.AddKnot(Variant(p1));
    sp.AddKnot(Variant(p2));
    sp.AddKnot(Variant(p3));

Now you have working spline, so you can get points for it using sp.GetPoint(),
the value for argument is from 0.0f to 1.0f. The following will plot the resulting spline data on image and save as .png:

        Image img;
        img.SetSize(200, 200, 3);
        img.ClearInt(0);
        for (float d = 0.0f; d <= 1.0f; d += 0.2f) {
                Vector3 vec = sp.GetPoint(d).GetVector3();
                Print(vec.ToString());
                img.SetPixel(100 + vec.x * 100, 100 + vec.z * 100, Color(1, 1, 1));
        }

The more complete copy-pastable example:

    void Start()
    {
            Image img;
            Spline sp;
            Array<Vector3> data = {
                    Vector3(0, 0, 0),
                    Vector3(1, 0, 0),
                    Vector3(1, 0, 1)
            };
            for (int i = 0; i < data.length; i++) {
                    sp.AddKnot(Variant(data[i]));
            }
            img.SetSize(200, 200, 3);
            img.ClearInt(0);
            for (float d = 0.0f; d <= 1.0f; d += 0.2f) {
                    Vector3 vec = sp.GetPoint(d).GetVector3();
                    Print(vec.ToString());
                    img.SetPixel(100 + vec.x * 100, 100 + vec.z * 100, Color(1, 1, 1));
            }
            img.SavePNG("splinetest.png");
            engine.Exit();
    }

Hope that will be useful to someone.

-------------------------

