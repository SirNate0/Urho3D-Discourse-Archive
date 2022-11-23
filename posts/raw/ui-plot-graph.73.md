carlomaker | 2017-01-02 00:57:47 UTC | #1

HI guys,
I'd like to see how to create UI  plot  graph / charts in U3D.

-------------------------

cadaver | 2017-01-02 00:57:47 UTC | #2

I see two routes:

- Create UI elements (eg. BorderImage) that represent the individual bars. This is somewhat limited, basically only for simple bar charts.
- Integrate some 3D party plot/graph package, which can output as a RGB image. Copy the RGB data into an Image object, and use Texture2D::Load() to upload into a texture for rendering.

-------------------------

carlomaker | 2017-01-02 00:57:48 UTC | #3

ok , the is very limited also for me, and 2 nd seems ok , but is not useful for  dynamic / scrollable charts,
 i remember that in ogre , i used a useful feature taked from  wiki,
shader based [url=http://www.ogre3d.org/tikiwiki/tiki-index.php?page=Ogre%20Line%20Chart]here[/url] , but i  have some difficult to porting ogre material/shaders in u3d , someone can do it  ?

-------------------------

