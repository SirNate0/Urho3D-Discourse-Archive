nergal | 2017-11-23 15:18:28 UTC | #1

I've developed a lot with ThreeJS (WebGL) and in ThreeJS there is a type called "Point" which holds a geometry that consists of vertices, "points", with VertexColors. It's really basic and all points always points towards the camera as a flat surface. I believe the indie game "Fugl" uses this technique.

This is how I create such in ThreeJS:
>     var material = new THREE.PointsMaterial( { size: this.particle_size, vertexColors: THREE.VertexColors} );
>     this.obj = new THREE.Points( geometry, material );
And this is how it looks like when drawn: [https://www.dropbox.com/s/ijddw4e74al7y6m/Screenshot%202017-11-23%2016.17.16.png?dl=0](https://www.dropbox.com/s/ijddw4e74al7y6m/Screenshot%202017-11-23%2016.17.16.png?dl=0)

How can I do the same in Urho3d? Particle system?

-------------------------

Eugene | 2017-11-23 15:47:58 UTC | #2

[quote="nergal, post:1, topic:3771"]
How can I do the same in Urho3d? Particle system?
[/quote]

Check for `BillboardSet` component.

-------------------------

nergal | 2017-11-23 18:09:15 UTC | #3

Thanks, that was exactly what I was after!

However, I can't see in the Urho3d source why the max billboards in a set is just 16384. In the code it just seems to check for M_MAX_INT.

    billboardObject->SetNumBillboards(2147483643);
    cout << "BILLBOARDS: " << billboardObject->GetNumBillboards() << " MAX: " << M_MAX_INT<< endl;

Output is:
BILLBOARDS: 16384 MAX: 2147483647

Enlighten me please!

-------------------------

Eugene | 2017-11-23 18:29:57 UTC | #4

[quote="nergal, post:3, topic:3771"]
However, I can’t see in the Urho3d source why the max billboards in a set is just 16384.
[/quote]
I managed to create 2147483 of them.

[quote="nergal, post:3, topic:3771"]
2147483647
[/quote]
Holy crap! 160 GB of f~n RAM for billboards... I wash my hands.

-------------------------

nergal | 2017-11-23 18:43:26 UTC | #5

hum, strange. Hehe, yeah, well I set that value just to test. But can you show your code how you initiated it? Any different than mine?

-------------------------

Eugene | 2017-11-23 18:51:46 UTC | #6

[quote="nergal, post:5, topic:3771"]
Any different than mine?
[/quote]

Nope, just this:

    auto bs = planeNode->CreateComponent<BillboardSet>();
    bs->SetNumBillboards(2147483/*643*/);
    unsigned t = bs->GetNumBillboards();

-------------------------

nergal | 2017-11-23 19:08:57 UTC | #7

Hum, that's really strange!

I tested with your code:
>     Node * planeNode = scene_->CreateChild("test");
>     auto bs = planeNode->CreateComponent<BillboardSet>();
>     bs->SetNumBillboards(2147483/*643*/);
>     unsigned t = bs->GetNumBillboards();
>     cout << "Billboard size: " << t << endl;

And the output becomes:

>   Billboard size: 16384

Edit: That's 16*32*32 but that doesn't add up to any particular type size? Btw, I'm developing on OSX, if that might be some difference.

-------------------------

Eugene | 2017-11-23 19:25:12 UTC | #8

Could you debug it? Just step into SetNumBillboards and check the code line by line. Maybe some type or constant problems. I'll debug it tooo.
There is only _one_ place where number of billboards is set.

-------------------------

nergal | 2017-11-23 20:30:24 UTC | #9

I'm using prebuilt binaries of Urho3d and they are compiled without debug. So I can't view any variables in the function. But looking at the asm given in the debug state it seems to compare with 0x4000 (which is 16384 dec.). And then it sets 16384 (if my novice-asm skills are enough to understand)

    Process 11076 stopped
    * thread #1, queue = 'com.apple.main-thread', stop reason = instruction step into
        frame #0: 0x00000001000e11e4 thegame`Urho3D::BillboardSet::SetNumBillboards(unsigned int) + 20
    thegame`Urho3D::BillboardSet::SetNumBillboards:
    ->  0x1000e11e4 <+20>: xorl   %eax, %eax
        0x1000e11e6 <+22>: testl  %r14d, %r14d
        0x1000e11e9 <+25>: cmovnsl %r14d, %eax
        0x1000e11ed <+29>: cmpl   $0x4000, %eax             ; imm = 0x4000 # Compares
        0x1000e11f2 <+34>: movl   $0x4000, %ebx             ; imm = 0x4000  # sets 16384

I just realised that I use Urho3D-1.6-OSX-64bit-STATIC and not 1.7. However, the function in 1.6 seems pretty much alike 1.7, just some minor change:

     // Prevent negative value being assigned from the editor
        if (num > M_MAX_INT)
            num = 0;

        unsigned oldNum = billboards_.Size();
        if (num == oldNum)
            return;

        billboards_.Resize(num);

Can't really see how that may affect since I enter num > 0x4000 and since oldNum might be 0x4000 it will go to Resize(num) and set my specified number?

-------------------------

nergal | 2017-11-24 06:19:44 UTC | #10

Ok, so It was the 1.6 version that had this limitation somehow. When I switched to 1.7 I got "Billboard size: 2147483".

Case closed!

Thanks for all help!

-------------------------

