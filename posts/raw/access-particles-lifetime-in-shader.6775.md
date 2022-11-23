Dave82 | 2021-03-31 17:42:11 UTC | #1

So i'm working on a dissolve effect for better blood spill and splash effects. Is the particle lifetime already accessible in the shader or do i need to implement it ? if so is there a "unused float" somewhere in the particle's vertex element structure that i could use without heavily modifying the ParticleEmitter or do i need to extend the current vertex data structure ?

-------------------------

Eugene | 2021-03-31 18:51:03 UTC | #2

Since `ParticleEmitter` is literally just `BillboardSet` with some automatic management, no, it doesn't have an easy way to get TTL in shader. Your best bet would be to utilize bilboard color... or rewrite _both_ `ParticleEmitter` and `BillboardSet` to pass some extra stuff to shader.

-------------------------

