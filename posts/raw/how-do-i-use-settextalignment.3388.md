behindcurtain3 | 2017-07-26 20:49:09 UTC | #1

Hello, I'm trying to align a Text to the right. Whenever I set:

text->SetTextAlignment(HA_RIGHT); 

or

text->SetTextAlignment(HA_CENTER);

It makes the text disappear completely. Is there something simple I'm missing to align the text to the right or center?

-------------------------

1vanK | 2017-07-26 21:01:21 UTC | #2

try use text->SetSize() first

-------------------------

behindcurtain3 | 2017-07-26 21:07:59 UTC | #3

Thanks 1vanK, it turns out I needed text->SetFixedSize() to get it working properly.

-------------------------

