josuemnb | 2020-12-13 15:34:43 UTC | #1

hello.
i'm trying to mix strip, fan and list of triangles into one model.

what is the best approach?
one custom geometry for each triangle type? Wouldn't performance slow down?

-------------------------

SirNate0 | 2020-12-13 16:03:34 UTC | #2

As someone who is not an expert on graphics by any stretch of the imagination, I would guess the best approach would be to just use an index buffer and handle it all with indexed triangles.

-------------------------

josuemnb | 2020-12-13 18:44:36 UTC | #3

thanks for reply.
but the same kind of indexed order isn't available.

-------------------------

SirNate0 | 2020-12-14 18:39:26 UTC | #4

I'm saying that you should just use an index buffer rather than using lists, strips, and fans. Per the below link, it looks like triangle fans, at least, aren't actually that beneficial. Perhaps the others might be better, that I can't speak to (and even the triangle fans one my knowledge only extends to a recent google search) .
https://gamedev.stackexchange.com/questions/35547/why-are-triangle-fans-not-supported-in-direct3d-10-or-later/35564

-------------------------

josuemnb | 2020-12-14 19:14:51 UTC | #5

i raised this question only because i'm trying to use a 3d model we're it mixes strip fan and list.
is just for file size performance.
and before i start to transform somehow strip to list, i remember to question it.

-------------------------

