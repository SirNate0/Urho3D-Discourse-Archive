qwertysam | 2019-05-23 13:20:01 UTC | #1

Hello! So my question is quite simple to ask (perhaps more difficult to answer); is it possible to select the type of filtering that applies to my StaticSprite2D objects? 

For example, this is what I've been working on:

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/eacf74b9b68a641575bf3993f98b190c49b1a701.png'>

The ship looks great. What I want is a 23 pixel high image that I can scale up by 4 in the code to achieve a 92 pixel high result on the screen. When I do that, this is the result that I get:

![Screenshot from 2017-08-05 13-24-13|117x121](upload://kI2Kgoohrrmz2X1DOFzzqJWder1.png)

Pretty gross, right? It appears to be using a Linear or Cubic scaling algorithm, which is not what I want. I would like to tell it to use a Nearest Neighbour scaling algorithm so that I can get those crisp pixels that will compliment the art. After about a week of searching, the documentation left me struck with no leads. 

My current workaround is to scale the image before-hand and load up a much larger image to be rendered. It's quite extraneous and not particularly fun or optimised for loading. 

Is there any proper or better solution that I'm missing?

Thanks!

-------------------------

Modanung | 2017-08-08 16:51:50 UTC | #2

Try this:
https://discourse.urho3d.io/t/tile-maps-seeing-neighbor-tiles/2931/2?u=modanung

And welcome to the forums! :slight_smile:

-------------------------

qwertysam | 2017-08-05 23:06:06 UTC | #3

Thank you so much for your help!

-------------------------

kostik1337 | 2017-08-08 16:51:46 UTC | #4

Well, this already has an answer, but I'd like to add - I fixed the same problem with
`engineParameters_["TextureFilterMode"] = FILTER_NEAREST;`
at Setup() of your Application, this sets filtering type for all textures, if they don't have an xml file

-------------------------

