godan | 2017-04-13 21:16:40 UTC | #1

https://youtu.be/aGd5D_gwLPA

Here is the single pass blur glsl:

```
float normpdf(in float x, in float sigma)
{
	return 0.39894*exp(-0.5*x*x/(sigma*sigma))/sigma;
}

vec3 OnePassBlur(sampler2D texSampler, vec2 texCoord, float blurScale)
{
	//declare stuff
	const int mSize = 7;
	const int kSize = (mSize-1)/2;
	float kernel[mSize];
	vec3 final_colour = vec3(0.0);
	
	//create the 1-D kernel
	float sigma = 7.0;
	float Z = 0.0;
	for (int j = 0; j <= kSize; ++j)
	{
		kernel[kSize+j] = kernel[kSize-j] = normpdf(float(j), sigma);
	}
	
	//get the normalization factor (as the gaussian has been clamped)
	for (int j = 0; j < mSize; ++j)
	{
		Z += kernel[j];
	}
	
	//read out the texels
	for (int i=-kSize; i <= kSize; ++i)
	{
		for (int j=-kSize; j <= kSize; ++j)
		{
			final_colour += kernel[kSize+j]*kernel[kSize+i]*texture2D(texSampler, (texCoord.xy+ blurScale * vec2(float(i),float(j)))).rgb;

		}
	}
		
		
	return final_colour/(Z*Z);
}
```

-------------------------

