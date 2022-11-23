Modanung | 2021-03-19 20:38:55 UTC | #1

I've been experimenting with PHP lately and decided to [rewrite](https://dry.luckeyproductions.nl/tools/anido/) my `anido` [C snippet](https://gitlab.com/-/snippets/1860709) for making texture animations. No more need to download and compile. :slightly_smiling_face:

Parameters:
> **c** = columns
> **r** = rows
> **w** = frameWidth
> **h** = frameHeight
> **i** = interval

Example use:
```
curl "https://dry.luckeyproductions.nl/tools/anido/?c=5&r=3&i=1.25" > animation.xml
```

Example output:
```
<texanim uv="0 0 0.2 0.333" time="0" />
<texanim uv="0.2 0 0.4 0.333" time="1.25" />
<texanim uv="0.4 0 0.6 0.333" time="2.5" />
<texanim uv="0.6 0 0.8 0.333" time="3.75" />
<texanim uv="0.8 0 1 0.333" time="5" />
<texanim uv="0 0.333 0.2 0.667" time="6.25" />
<texanim uv="0.2 0.333 0.4 0.667" time="7.5" />
<texanim uv="0.4 0.333 0.6 0.667" time="8.75" />
<texanim uv="0.6 0.333 0.8 0.667" time="1" />
<texanim uv="0.8 0.333 1 0.667" time="11.25" />
<texanim uv="0 0.667 0.2 1" time="12.5" />
<texanim uv="0.2 0.667 0.4 1" time="13.75" />
<texanim uv="0.4 0.667 0.6 1" time="15" />
<texanim uv="0.6 0.667 0.8 1" time="16.25" />
<texanim uv="0.8 0.667 1 1" time="17.5" />
```

-------------------------

