cin | 2017-01-02 00:57:31 UTC | #1

I think what need move spline to core and separate for types which can be Lerp'ed -float, vector2, vector3, vector4 and color. I don't know how to make it optimal and right in common case.
Next for scene need rename Spline to Spline3DPath, it must use core Spline class for calculations.  Add auto move parent node when we click Autoupdate in editor. Also debug geometry needed for Spline3DPath.
Why Spline must be moved into core - it can be used in other places, ex. in 2D gui contol which return interpolated value by time. Or for connect nodes as showed here:
[img]http://i.imgur.com/lq2gHv0.png[/img]
Next we can use spline to interpolate colour of light (for flash) over time. RampGenerator can use spline function for allow generate not linear gradient textures.

-------------------------

Azalrion | 2017-01-02 00:57:31 UTC | #2

It should be easy to create the specific implementations using specialized templates so thats not a problem and I did originally have it in math so I'm not against it being there. I do think we need to be careful with the components though because we don't want them to look like they are replacing the path finding, I'll think a bit about naming and especially auto-movement. I'm not a fan of the lack of control that would cause but maybe if the functionality is available elsewhere its not such an issue. Although as Lasse pointed out in my pull request there are some benefits to not having auto-movment.

-------------------------

cadaver | 2017-01-02 00:57:32 UTC | #3

Because Attributes already operate on Variants it might make sense to have the interpolator / animator (or whatever it is called) also operate on them. Of course it only makes sense on the numeric types and when the control points are all of the same type (for example all Vector3, or all Color). Then you could target any suitable attribute in any component, and changing the attribute also activates the required side-effects, such as scene graph dirtying.

-------------------------

Azalrion | 2017-01-02 00:57:32 UTC | #4

Hm thats an interesting alternative to specialized templates. Is there anyway to know with the variant which base type has been set?

Edit: Nevermind found it.

-------------------------

Azalrion | 2017-01-02 00:57:32 UTC | #5

*shameless double post*

So I was thinking something like this for the "Spline" class in Math:

[code]Variant Spline::BezierInterpolation(const VariantVector& knots, float t, VariantType type)
{
    if (knots.Size() == 2)
    {
        switch (type)
        {
        case VAR_FLOAT:
        case VAR_VECTOR2:
        case VAR_VECTOR3:
        case VAR_VECTOR4:
        case VAR_COLOR:
            return LinearInterpolation(knots[0], knots[1], t, type);
        default:
            return Variant::EMPTY;
        }
    }
    else
    {
        VariantVector interpolatedKnots;
        for (unsigned i = 1; i < knots.Size(); i++)
        {
            switch (type)
            {
            case VAR_FLOAT:
            case VAR_VECTOR2:
            case VAR_VECTOR3:
            case VAR_VECTOR4:
            case VAR_COLOR:
                interpolatedKnots.Push(LinearInterpolation(knots[i - 1], knots[i], t, type));
                break;
            default:
                return Variant::EMPTY;
            }
        }
        return BezierInterpolation(interpolatedKnots, t, type);
    }
}

Variant Spline::LinearInterpolation(const Variant& lhs, const Variant& rhs, float t, VariantType type)
{
    switch (type)
    {
    case VAR_FLOAT:
        return Lerp(lhs.GetFloat(), rhs.GetFloat(), t);
    case VAR_VECTOR2:
        return lhs.GetVector2().Lerp(rhs.GetVector2(), t);
    case VAR_VECTOR3:
        return lhs.GetVector3().Lerp(rhs.GetVector3(), t);
    case VAR_VECTOR4:
        return lhs.GetVector4().Lerp(rhs.GetVector4(), t);
    case VAR_COLOR:
        return lhs.GetColor().Lerp(rhs.GetColor(), t);
    default:
        return Variant::EMPTY;
    }
}[/code]

It removes any reliance on templates and makes use of the Variant types and would fit pretty seemlessly into a "SplinePath" component in the scene graph, where the "SplinePath" would calculate all the length, distance traveled functions etc and pass that factor to the "Spline" class. Perhaps with a few more controls on what VariantTypes are suitable when adding "Knots" (its the proper technical term *faceplam).

-------------------------

