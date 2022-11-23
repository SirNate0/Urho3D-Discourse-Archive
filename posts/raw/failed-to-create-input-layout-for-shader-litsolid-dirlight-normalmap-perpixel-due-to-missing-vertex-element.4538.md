RockRockWhite | 2018-09-15 11:21:30 UTC | #1

I'd importered a model from FBX with one of a alpha texture(*.png) just now.Then I loaded the model,setting the material(with the alpha texture).I sadly found that the material didn't work probably while it worked normally in Material Edit.The error code is 'Failed to create input layout for shader LitSolid(DIRLIGHT NORMALMAP PERPIXEL) due to missing vertex element'.What was the matter?How can I deal with it?


![%40%7BW0W%7B%5BN9X75D8L505LEHHK|690x29](upload://fwijrfJb3PyH22hkKGDznrEvLsu.png) 
![1%5DZ9N_YY%7D%405X%40YRVCJM(BNH|294x499](upload://xR4U2zPelJq1B4Ath3Rryai8F14.png) ![C6MBN%5D0JUFB7MOPF%60SW%241~R|690x376](upload://hFbUx8iHxGUrK2MGQIEeINx4lzQ.jpeg)

-------------------------

lezak | 2018-09-15 12:01:19 UTC | #2

It means exactly what is written in the error message - Your model is missing some vertex element required by the technique You are using (<a href="https://urho3d.github.io/documentation/HEAD/_vertex_buffers.html">here</a> is the list of all vertex elements). I can see that You have uvs, so it propably would be normal and/or tangents (those are required for normal map). 
Also to make use of alpha from the texture You'll have to define ALPHAMASK in technique or use one of the predefined techniques with alpha - Your current setup is not using alpha.

-------------------------

RockRockWhite | 2018-09-15 14:31:46 UTC | #3

So how can I do?I tried to set PetVerText true,but if I do so,the normal Texture will not work.

-------------------------

Modanung | 2018-09-15 14:38:47 UTC | #4

Common advice around here in these situations is to take it through [Blender](https://www.blender.org/):
https://github.com/reattiva/Urho3D-Blender
...and mark the right checkboxes.

-------------------------

RockRockWhite | 2018-09-15 14:41:15 UTC | #5

However,'Jack.mdl' has the same problem when set material "Materials/StoneSmall.xml"

-------------------------

Modanung | 2018-09-15 15:30:59 UTC | #6

Jack never intended to put on a normal map, or anything else for that matter. ;P
Feel free to give Jack some tangent data and submit it as a pull request. I don't think there would be objections to the model working correctly with normal maps.

-------------------------

RockRockWhite | 2018-09-15 15:31:52 UTC | #7

Well,by the way.How can I mark the right checkboxes?

-------------------------

Modanung | 2018-09-15 15:37:05 UTC | #8

You will find them in the _Render_ tab of the properties panel.
In your case the settings should be something like this:
![image|217x500](upload://2Y0rZA1Yfns0CgGfkRgjxqK0Q1c.png)

-------------------------

RockRockWhite | 2018-09-15 16:56:31 UTC | #9

But it dosen't work all the same.Only if setting PetVerText true can it work normally,but if I do so,the normal Texture will not work.

-------------------------

Modanung | 2018-09-15 17:15:39 UTC | #10

[quote="RockRockWhite, post:9, topic:4538"]
PetVerText
[/quote]

What do you mean by this?
Would you mind sharing the assets so I (or someone else) could have a look and try?
To get transparency to show you'll need to use the `DiffNormalSpecAlpha` technique, btw.

-------------------------

RockRockWhite | 2018-09-15 23:43:16 UTC | #11

谢谢你一直热心解答. :grinning: 算了,敲英文太累了,看了你的主页我想中文你应该看得懂的.我这个模型只是随便从网上下载下来试用的.是fbx带有法线贴图的那种.我导出成mdl后在编辑器试用,但是如果我不设置灯光Pet VerTex为True的话,模型的纹理就会像图上一样莫名变黑 ![_YBW%7BNV%7BEF53~%7DCUVX%5DP%25NJ|690x376](upload://yEtj38PWuh2I5CjGO1DJeihiTyS.png)  ,如果我设置了Pet VerTex为True,模型能正常看到,但是法线贴图就无效了.但是我发现同样的纹理在box.mdl等基本模型上面就就没有任何问题. 我贴上我网上下载的模型,和转换后的模型

-------------------------

RockRockWhite | 2018-09-15 23:44:20 UTC | #12

下载的fbx模型和转换后的模型:https://pan.baidu.com/s/17DoY4DiEqblo5vso_MMbIQ

-------------------------

RockRockWhite | 2018-09-22 10:27:23 UTC | #13

Solved.Thank you very much!Using the Editor (File -&gt; Import Model),everything is all right!

-------------------------

Modanung | 2018-09-16 07:17:59 UTC | #14

我只懂中文，因为机器会为我翻译。 :wink:
Glad you solved it.

-------------------------

RockRockWhite | 2018-09-18 11:31:56 UTC | #15

I saw in your page "魔大农' ，which made me think you are know chinese

-------------------------

Modanung | 2018-09-19 14:09:41 UTC | #16

I made up the name Modanung - from the top of my head - when I was about thirteen years old, with no intention of it having any meaning beyond it being my nickname in virtual environments. About a year ago I found out (while translating lines from [Firefly](https://www.themoviedb.org/tv/1437-firefly?language=zh-CN) and being twice as old) these three Chinese characters closely dictate the intended pronunciation. Seeing that many people are more familiar with Chinese characters than Latin characters I figured I'd use both. Also it's shorter and I think it looks cool. :sunglasses:

-------------------------

RockRockWhite | 2018-09-19 14:00:19 UTC | #17

So it does.And the two characters pronounced similarly.It's really cool! :grinning:

-------------------------

RockRockWhite | 2018-09-19 14:09:26 UTC | #18

But I'm poor in English and have difficulty to read the web in English .:disappointed_relieved:

-------------------------

Modanung | 2018-09-19 16:19:08 UTC | #19

叢林中掙扎激勵鋪平道路 :)
[spoiler]Struggling through the jungle motivates to pave the road[/spoiler]
(A minimum of 20 characters is quite a high bar in Chinese, btw.)

-------------------------

