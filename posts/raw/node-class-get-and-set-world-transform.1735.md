atai | 2017-01-02 01:09:47 UTC | #1

This is not a major issue... just a small comment on the node class.

It has a method 

[code]const Matrix3x4 & 	GetWorldTransform () const ;

[/code]

but there is no corresponding SetWorldTransform() method that takes a Matrix3x4 (or any matrix) as the parameter.  This is based on the current git source.
For the sake of consistency, should there be such a set method?

Thanks

-------------------------

