sabotage3d | 2017-01-02 01:07:53 UTC | #1

Hi guys,
I am seeking advice if my approach is correct. I have a Car and CarGenerator derived from LogicComponent, the CarGenerator will generate cars based on random time interval. I am also generating lanes randomly and every lane will need a new CarGenerator instance, currently I am calling new CarGenerator(context_) for every lane. Is that a good approach is there other way? I also need to delete lanes when I delete lane can I automatically delete the CarGenerator?
[b]Update:[/b]
Thanks to Ehnex I solved this issue by attaching CarGenerator as a new second component to the Lanes.

-------------------------

