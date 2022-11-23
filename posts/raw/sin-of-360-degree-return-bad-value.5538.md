AntiLoxy | 2019-08-31 23:27:44 UTC | #1

Please someone can tell me why std::sin(M_PI * 2); or Urho3D::Sin(360.0f) return a bad value.
I expect return equal to 0.

Sample of a returned values: 1.74845553e-07.

-------------------------

Sinoid | 2019-08-31 23:49:05 UTC | #2

It's the table maker's dilemma. The transcendental functions are well known to be unreliable if you're after accuracy (they have consistency and precision though).

It's *super* fun when you're dealing Q-numbers.

-------------------------

Modanung | 2019-09-01 08:09:18 UTC | #3

I use quadratic approximation. Maybe it behaves more how you would expect your sine functions to work.
[details=Code]
```
float LucKey::Sine(float x)
{
    x = Cycle(x, -M_PI, M_PI);

    float sin{};

    if (x < 0.0f)
        sin = 1.27323954f * x + 0.405284735f * x * x;
    else
        sin = 1.27323954f * x - 0.405284735f * x * x;

    if (sin < 0)
        sin = 0.225f * (sin *-sin - sin) + sin;
    else
        sin = 0.225f * (sin * sin - sin) + sin;

    return sin;
}
float LucKey::Cosine(float x)
{
    return Sine(x + M_PI * 0.5f);
}
```
```
float LucKey::Cycle(float x, float min, float max)
{
    float res{ x };
    if (min > max) {

        float temp{ min };
        min = max;
        max = temp;
    }

    float range{max - min};

    if (x < min)
        res += range * abs(ceil((min - x) / range));
    else if (x > max)
        res -= range * abs(ceil((x - max) / range));

    return res;
}
```
[/details]

-------------------------

johnnycable | 2019-09-01 09:20:34 UTC | #4

[quote="AntiLoxy, post:1, topic:5538"]
1.74845553e-07.
[/quote]

**That** is Zero!
[20 char filler]

-------------------------

Modanung | 2019-09-01 09:35:43 UTC | #5

Actually it's 0,000000174845553... which *is* pretty close. :slightly_smiling_face:

-------------------------

AntiLoxy | 2019-09-01 11:23:06 UTC | #6

Ok, so it's normal that is not a perfect 0, thanks for all !

-------------------------

codexhound | 2019-09-02 01:22:16 UTC | #7

That's not incorrect. Those functions are approximations as you can only go so far. 1.749*10e-07 is essentially zero. Just insert a tolerance that turns anything close to 0 into 0.

-------------------------

Valdar | 2019-09-02 06:03:02 UTC | #8

And to clarify, it’s basically a roundoff error and not specific to Urho.
The result of some calculations (especially trigonometry) would require infinite space to hold in floating-point notation. Due to the finite length of memory locations, those results get truncated and you lose a slight amount of accuracy. In most cases, you won’t notice, but in calculations that repeat many times, you should be aware. The error will accumulate each time and potentially become an issue. In those cases, you may want to manually mitigate the error as @codexhound mentioned.

-------------------------

johnnycable | 2019-09-02 15:01:01 UTC | #9

Yes. There's no such thing as a discrete zero value in computer calculations, unless you use something like http://www.mpir.org/

more madness here: https://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition/

-------------------------

Modanung | 2019-09-02 17:45:23 UTC | #10

Interesting links

> #### [Don't store that float](https://randomascii.wordpress.com/2012/02/13/dont-store-that-in-a-float/)
> "Elapsed game time should never be stored in a float. Use a double instead."

Urho uses `float`s because of backwards compatibility, right? Since - as I understand it - it makes no difference, performance-wise, on modern (64-bit?) architecture.

-------------------------

