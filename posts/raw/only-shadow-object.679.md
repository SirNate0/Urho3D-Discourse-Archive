ucupumar | 2017-01-02 01:02:04 UTC | #1

Do anyone know how to set objects to casts shadow but invisible to camera?  :question:

-------------------------

cadaver | 2017-01-02 01:02:05 UTC | #2

This should be possible by creating a technique (you can use existing ones as a base) where you nuke all passes except the shadow pass, then use that technique in your material.

-------------------------

ucupumar | 2017-01-02 01:02:05 UTC | #3

That's really what I looking for! Thanks!  :mrgreen:

-------------------------

