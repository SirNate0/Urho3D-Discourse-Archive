Askhento | 2020-02-01 13:36:21 UTC | #1

Hello, I want to attach a Node to other Node with smooth transition. Is there any built in features to use in Urho3d?

-------------------------

Askhento | 2020-02-01 14:51:10 UTC | #2

I've found this formula in case anyone is interested in : 
```
       newPosition =  targetPos * alpha + prevPos * (1 - alpha);
```
Alpha is something like damping factor.

-------------------------

WangKai | 2020-02-01 17:36:14 UTC | #3

You could just use Easing to get the every interpolation state. There are tons of implementations of different languages 
https://easings.net/

E.g. I use easing function to control the move of camera, any `Urho3D::Node` should be similar -
```c++
    if (elapsedTime_ <= duration_)
    {
        float factor = Expo::easeOut(elapsedTime_, 0.0f, 1.0f, duration_); //  (epapsed-time, start-value, end-value, total-time)

        if (interpLookAtPos_)
            cameraLookAtNode_->SetWorldPosition(lookAtBeginPos_ + (lookAtEndPos_ - lookAtBeginPos_) * factor);
        // ...
    }
```

Edit: in your case, you can just the Exponential easing function.

-------------------------

WangKai | 2020-02-01 17:37:35 UTC | #4

The formula you use is **linear**.

-------------------------

Askhento | 2020-02-01 18:57:07 UTC | #5

What does Expo mean? How to use it?

-------------------------

Modanung | 2020-02-01 22:32:11 UTC | #6

Did you look into Urho's attribute animation capability?

https://urho3d.github.io/documentation/1.7.1/_attribute_animation.html

Setting the value animation's interpolation method to `IM_SPLINE` you might be able to achieve the result you are looking for with the right spline tension.

-------------------------

Askhento | 2020-02-01 23:56:22 UTC | #7

I will take a look. Thank you.

-------------------------

WangKai | 2020-02-02 03:33:26 UTC | #8

Expo means Exponential.
https://stackoverflow.com/questions/8316882/what-is-an-easing-function

-------------------------

Sinoid | 2020-02-06 04:09:32 UTC | #9

There's no such thing as straight exponential interpolation.

Do you mean MKCB curves? 

M = slope
K = exponent

Is this the thing you're after?

```
    struct ResponseCurve
    {
        CurveType type_;
        float xIntercept_;
        float yIntercept_;
        float slopeIntercept_;
        float exponent_;
        bool flipX_;
        bool flipY_;
    
        ResponseCurve() : type_(CT_Linear), xIntercept_(0.0f), yIntercept_(0.0f), slopeIntercept_(1.0f), exponent_(1.0f), flipX_(false), flipY_(false)
        {
            xIntercept_ = yIntercept_ = 0.0f;
        }
    
        float GetValue(float x) const
        {
            if (flipX_)
                x = 1.0f - x;
    
            // Evaluate the curve function for the given inputs.
            float value = 0.0f;
            switch (type_)
            {
            case CT_Constant:
                value = yIntercept_;
                break;
            case CT_Linear:
                // y = m(x - c) + b ... x expanded from standard mx+b
                value = (slopeIntercept_ * (x - xIntercept_)) + yIntercept_;
                break;
            case CT_Quadratic:
                // y = mx * (x - c)^K + b
                value = ((slopeIntercept_ * x) * powf(abs(x + xIntercept_), exponent_)) + yIntercept_;
                break;
            case CT_Logistic:
                // y = (k * (1 / (1 + (1000m^-1*x + c))) + b
                value = (exponent_ * (1.0f / (1.0f + powf(abs(1000.0f * slopeIntercept_), (-1.0f * x) + xIntercept_ + 0.5f)))) + yIntercept_; // Note, addition of 0.5 to keep default 0 XIntercept sane
                break;
            case CT_Logit:
                // y = -log(1 / (x + c)^K - 1) * m + b
                value = (-logf((1.0f / powf(abs(x - xIntercept_), exponent_)) - 1.0f) * 0.05f * slopeIntercept_) + (0.5f + yIntercept_); // Note, addition of 0.5f to keep default 0 XIntercept sane
                break;
            case CT_Threshold:
                value = x > xIntercept_ ? (1.0f - yIntercept_) : (0.0f - (1.0f - slopeIntercept_));
                break;
            case CT_Sine:
                // y = sin(m * (x + c)^K + b
                value = (sinf(slopeIntercept_ * powf(x + xIntercept_, exponent_)) * 0.5f) + 0.5f + yIntercept_;
                break;
            case CT_Parabolic:
                // y = mx^2 + K * (x + c) + b
                value = powf(slopeIntercept_ * (x + xIntercept_), 2) + (exponent_ * (x + xIntercept_)) + yIntercept_;
                break;
            case CT_NormalDistribution:
                // y = K / sqrt(2 * PI) * 2^-(1/m * (x - c)^2) + b
                value = (exponent_ / (sqrtf(2 * 3.141596f))) * powf(2.0f, (-(1.0f / (abs(slopeIntercept_) * 0.01f)) * powf(x - (xIntercept_ + 0.5f), 2.0f))) + yIntercept_;
                break;
            case CT_Bounce:
                value = abs(sinf((6.28f * exponent_) * (x + xIntercept_ + 1.0f) * (x + xIntercept_ + 1.0f)) * (1.0f - x) * slopeIntercept_) + yIntercept_;
                break;
            }
    
            // Invert the value if specified as an inverse.
            if (flipY_)
                value = 1.0f - value;
    
            // Constrain the return to a normal 0-1 range.
            return CLAMP01(value);
        }
    };
```

-------------------------

Askhento | 2020-02-06 12:59:22 UTC | #10

Thanks to all of the response! 
I've checked my approach and it looks like it works! Aknow it looks like a linear interpolation, but it's just a matter of view angle.
Here is a test in excel of my function. Step function as target input. The main thing here is prevPos is not target previous position but the output of smoothing function itself.
Sorry my question was not supper clear(

![image|690x363](upload://2qxqHQWJoKatXqzgw2eRCpTPfTB.png)

-------------------------

