dertom | 2020-01-03 23:12:19 UTC | #1

Hi, here is the problem:
![image|635x499](upload://6J8xe8qcK67yrANEu2H1FgT4879.jpeg) 

The shadow appears on the floor but also on the wall of the floor beneath. I know that this is a common problem. But is there any solution? Maybe another kind of shadow-rendering? I'm using the default way, as it is used in all the samples.

Greetz,Tom

-------------------------

Sinoid | 2020-01-03 23:49:17 UTC | #2

Shadow-map can only mask out light for what it knows about (what was rendered into it).

Either your walls need to be marked as not to receive shadows or your upper-floors need to be set to also cast shadows so the shadow-map is *more complete*.

-------------------------

dertom | 2020-01-04 00:30:00 UTC | #3

Thx for your advice. Since ceiling and wall are one mesh (atm) I go for setting the wallparts to cast shadows as well. And it works as intended.... :+1:

@Sinoid : Hmm,...how exactly would I mark an object as "not to receive shadows"? Would this be done with the shadowmask?

-------------------------

