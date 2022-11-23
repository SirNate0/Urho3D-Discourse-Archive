thebluefish | 2017-01-02 01:05:01 UTC | #1

I'm not too familiar with lighting, so I hope someone can shed some light on this problem.

I have 4 stretched cubes, each with a separate light mask. I also have 4 lights for each cube. These lights also have their light mask set appropriately so that 4 lights affect each cube. These lights are set to a single color, so that each cube is uniformly colored. The colors for all 4 are (1, 0, 0), (1, 1, 0), (1, 0, 1), and (0, 1, 1). The brightness and specular intensity is set to 0.6 for all lights, and the FOV is set to 90.

My problem seems to be that the red cube is not lit nearly as well as the others. I believe this may be a result of the fact that I am using 2 color channels for the other lights besides the red light. Doubling the red color channel or brightness seems to be too bright to match the other 3. Is there any formula or way of getting these to match?

[url=http://i.imgur.com/IIxp229.jpg][img]http://i.imgur.com/IIxp229m.jpg[/img][/url]

-------------------------

TikariSakari | 2017-01-02 01:05:01 UTC | #2

This is most likely very off, but maybe your colors in monitor aren't correctly configured or maybe you have partial color blindness to red? I think I read somewhere that roughly 8% of men are color blind, and I think it might have been roughly 0.5% of women. I have 2 monitors, and they have completely different calibration for colors. One is newer 23" IPS one, and the other is very old 24" LCD and even if I use my phone to compare the picture you used in the post all 3 of them have slightly different color calibration.

Up to my understanding you probably want to use HSL-colors ( Hue-saturation-lightness), and keeping saturation as 1 to get the biggest color differences. Altho I am not completely sure if this would solve the problem, but at least to my understanding that is at least partially what hsl is for? [url]http://en.wikipedia.org/wiki/HSL_and_HSV[/url]  looking that wikipedia, maybe the luma chrome hue would give the most accurate brightness function.

So if we use the luma rgb-calculator, maybe it works, maybe it doesn't:
luma = 0.21R + 0.72G + 0.07B, and if we set that to 0.6, then some possible values are, if I counted correctly:
1* 0.21R + x* (0.72 + 0.07) = 0.6 => x = 0.49 => 1.0R +  0.49G + 0.49B
0*0.21R + x*0.72G + 0*0.07B = 0.6 => x = 0.83 => 0.0R + 0.83G + 0.0B 
x*(0.21 + 0.72) + 1*0.07B = 0.6 => x = 0.57 => 0.57R + 0.57G + 1.0B

I think I have read/heard somewhere that in general people are more sensitive to green-yellowish color, so maybe that could be one reason for sensing higher intensity from certain colors than others. If you look from wikipedia there are few color conversions from rbg to grayscale: [url]http://en.wikipedia.org/wiki/Grayscale[/url]. In both cases the Green color has significantly higher multiplier than red or green color.

Edit: Correction roughly 0.5% females and 8% of males instead of 5% / 8% has some sort of color blindness
Edit2: HSV -> HSL / luma-chrome-hue?

-------------------------

