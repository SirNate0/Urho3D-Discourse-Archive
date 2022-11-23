zedraken | 2019-01-07 18:54:20 UTC | #1

Hello all,

here is a short preview of a small app that I use to test a  component that I am currently designing to create forests.

[http://ingels.me/~charles/videos/island_preview.mp4](http://ingels.me/~charles/videos/island_preview.mp4)

Here, the trees are palm trees, homebrewed tree model.

The forest component is useable under Urho3D like any other component:

    ...
    Node* node = scene_->CreateChild("Palm forest");
    palmForest = node->CreateComponent<Forest>();
    palmForest->Init(scene_, "Models/PalmTree.mdl", 200, 800);
    ...

Then, some parameters can be set like the inner radius, the outer radius, the spread angle and the sector. The model file (with its materials and texture) is also specified, along with the maximum number of trees to place.
Each tree is randomly vertically scaled using a scaling factor that has a default value but that can also be altered.
Finally, each tree is randomly rotated around the Y axis.

The component will try to put as much trees as possible in the area defined by the parameters (or by the default ones if no specific parameter is modified). This means that since each tree needs a space around it (another parameter that can be specified), there might be some situations where all the requested trees cannot be inserted and the component returns with the actual number of trees it has successfully put. 
Another constraint is that the scene shall contain one terrain (otherwise nothing will be done). The component will land each tree on the terrain taking into account the terrain height at the tree location.

As you can see, the palm tree is not fully finished, and I plan to design other type of trees to create forests with different densities of trees.

Enjoy!

-------------------------

Bananaft | 2019-01-20 07:52:31 UTC | #2

Looks good. Any reason you don't use cascaded shadow maps?

-------------------------

zedraken | 2019-01-20 08:08:04 UTC | #3

Hi Bananaft,
frankly speaking, I have never used cascading shadow map, so I am not really aware to what it is and how to use it.
Anyway, I am going to have a look…
Thanks

-------------------------

Leith | 2019-01-20 09:54:30 UTC | #4

The palm trees are great! The shadows are indeed a problem. Have you ever heard of L-Systems? It's a perfect fit for making procedural vegetation, though not too useful for palm trees, it is the basis of speed-tree.

-------------------------

QBkGames | 2019-01-21 06:11:28 UTC | #5

Nice. I've been looking for months for a good (realistic) and preferably simple (to understand and implement) vegetation distribution algorithm. What are you using? Is there any source code we can look at? Thanks.

Brave lady, trying to catch a huge shark with her bare hands :grinning:.

-------------------------

zedraken | 2019-01-27 15:19:10 UTC | #6

Hi,
sorry for my late answer.

You can have access to the source code on Gitlab where the project is hosted:
[https://gitlab.com/zedraken/island](https://gitlab.com/zedraken/island)

The tree placement algorithm is quite simple and can be surely improved. Unfortunately, I have not written a documentation yet on the _Forest_ class, but this is something I have in mind. However, I have drawn a scheme that explains some of the useable parameters:

![classe_Forest|493x500](upload://oUPZ4cwE08fkJATpkCQgiBTjsxY.png) 


Basically, you specify the number of trees you want to be placed, and also the area (within a circular ring defined by an inner and by an outer radius, and an angle range - default is 0° to 360° - and an angle sector in case angle range is less than 360°), you also specify minimum ground space required for one tree (to avoid having two or more trees placed at very closed locations), and the class will randomly place the trees around a central point (that you also specify).
At some point (depending on your parameters), the random values will trigger more and more tree collisions. If there are too much collisions, then the class returns with the actual number of placed trees.
Consequently, if you are lucky, the returned number of trees will exactly match the number of requested trees. Otherwise, you have to extend your area, or use smaller trees…
And last think, you need to have a terrain in your scene otherwise the class will not do anything.

I have some improvements in mind but not implemented yet, like the possibility to set an array of trees instead of one single tree, or to use a gaussian distribution around the central point instead of a purely random distribution. 

Feel free to comment the source code and you are welcome if you want to suggest improvements!

Thanks

-------------------------

QBkGames | 2019-01-28 01:03:11 UTC | #7

Thanks for the reply (better late than never :) ). The algorithm is a good, simple start.

What I have in mind (but didn't get around to doing it yet, it's just at the 'design' stage), is something more fractal in nature. Starting with the big circle, select a number of smaller circles inside it, then a number of even smaller circles inside the small circles (I think 3 levels should be enough), then place the trees/vegetation only in the smallest circles. This will give the forest a more fractal/natural look.

Combine this with a Gaussian distribution across the big circle so you have higher density at the center and lower at the edges and it should look pretty good (in theory at least :) ).

-------------------------

Leith | 2019-01-28 05:28:31 UTC | #8

I typically use perlin noise, or variations on it, to generate noisemap textures that tell us about the distribution of vegetation - I find a pattern I like, and save the bitmap.  If I need to adjust the bitmap, I can paint it using any image editing application, to create trails, to reduce vegetation in particular areas, or to increase it, as I see fit. But it generally starts with a noise map.

-------------------------

zedraken | 2019-01-28 17:08:42 UTC | #9

Maybe it can be foreseen to cut the original circle in four regular and equal quarters, then inside each quarter you virtually draw a circle which is in turn cut down into 4 smaller quarters and so on until you reach a depth. Then, in each atomic circle, you randomly distribute trees or you can rely on a gaussian curve.
This is definitely to be tested.

-------------------------

QBkGames | 2019-01-29 01:13:11 UTC | #10

So how do you use the noise map to create actual objects in the game world? Do you go through each pixel of the map and place an appropriate object based on the pixel grey level, or is there another algorithm?

-------------------------

Leith | 2019-01-29 02:47:34 UTC | #11

I assign each vegetative model to a specific pixel intensity, then scan the noise image for pixels whose RGB intensity matches my mapping. When I find a match, I instantiate the relevant model at an XZ position that maps from the 2D noise image to my world size (plus a small random adjustment), and finally,  raycast down onto the terrain to find the appropriate Y value. Note that I end up ignoring most of the pixels on the noisemap, as I don't tend to have too many kinds of vegetation (so most pixel intensities are not mapped to anything), and I deliberately choose pixel intensities that are dissimilar to get a nicer distribution.
This is somewhat of a simplification: I manually touch up the noise image to ensure buildings, roads etc. can't have vegetation, and for some models, I also perform a late collision test to ensure that instances don't overlap/intersect. I never bothered to project my buildings back onto the noisemap but that could work too.

-------------------------

zedraken | 2019-01-29 13:15:15 UTC | #12

Thanks for the description of your algorithm. I think that it is worth giving it a try.

-------------------------

