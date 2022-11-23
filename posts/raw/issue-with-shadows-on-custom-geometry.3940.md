nergal | 2018-01-12 07:18:14 UTC | #1

I have an small issue with strange shadows in my custom geometries. The shadows looks jagged at some places as you can see in the images below. What causes this, wrong normals when I build my mesh? I use VertexColors.

![54|656x500](upload://rhJasn15DwS6aoTawBxIoYryym1.png)

(Zoomed in version)
![05|690x390](upload://dVQu17OG8QePd4Yd43ssO3xAO6T.png)

-------------------------

Eugene | 2018-01-12 11:47:05 UTC | #2

Tune biases and offsets for your `Light` source.

-------------------------

