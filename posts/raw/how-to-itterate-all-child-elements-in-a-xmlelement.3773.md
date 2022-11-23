SeeSoftware | 2017-11-23 19:20:03 UTC | #1

i try to load a XML file and i want to itterate all of its elements to do something with them and i tried to do it like this:

    for (XMLElement element = source.NextResult(); element.NotNull(); element = element.NextResult())

but it doesnt itterate anything and i have seen some XPathResult but i dont know how to use it.

-------------------------

Eugene | 2017-11-23 20:27:08 UTC | #2

[quote="SeeSoftware, post:1, topic:3773"]
i try to load a XML file and i want to itterate all of its elements to do something with them and i tried to do it like this:
[/quote]

I suppose that you have no result because you have no query to iterate.
Use `NextChild` to iterate over elements witout query.

-------------------------

Modanung | 2017-11-24 02:20:33 UTC | #3

Hm... shouldn't this method actually be called `NextSibling`? :confused:

-------------------------

Eugene | 2017-11-24 07:16:51 UTC | #4

I mis-recalled the name /_-
It was `GetNext`.

-------------------------

