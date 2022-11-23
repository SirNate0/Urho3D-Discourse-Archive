smellymumbler | 2018-01-11 17:22:25 UTC | #1

So, I've been trying to customize the 18th example of Urho to match the procedural animation technique by Wolfire Games as shown here: 

https://www.youtube.com/watch?v=SAtwQa8t_3g
https://www.youtube.com/watch?v=BsrRRJXI4BQ

I've been applying a small rotation to the hip bone based on the key that is being pressed: W, A, S or D. However, it's not as smooth as that. The rotation is very abrubt and doesn't sway to the direction. Does anyone know how to do this, technically? It is really a hip bone rotation?

-------------------------

George1 | 2018-01-12 10:45:43 UTC | #2

You need the accelaration factor to make it smooth.
Maybe increase the angles by x^2. It will be more smooth.

-------------------------

