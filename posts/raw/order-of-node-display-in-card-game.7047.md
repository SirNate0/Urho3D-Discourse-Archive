bayganik | 2021-11-06 15:42:26 UTC | #1

I am writing a 2D card game and am stuck on how to display nodes in a particular order.  Is there a field to manipulate? 

 ![image|608x500](upload://b8Zy1OPz0zIZ27mh07Ncsf272aJ.png)

-------------------------

Modanung | 2021-11-05 14:53:46 UTC | #2

Welcome to the forums! :confetti_ball: :slightly_smiling_face: 

All classes that derive from `Drawable2D` have `SetLayer` and `SetOrderInLayer` functions. I would assume these do what you're looking for.

-------------------------

Modanung | 2021-11-05 14:57:58 UTC | #3

Also, **developer talk** is for discussing development _of_ the engine not _with_. Questions about using the engine are best be asked in **discussions -> support**, where they can be marked as solved.

-------------------------

bayganik | 2021-11-05 15:43:34 UTC | #4

Thank you so very much, that worked.  I'll go to the support discussion next time.

-------------------------

