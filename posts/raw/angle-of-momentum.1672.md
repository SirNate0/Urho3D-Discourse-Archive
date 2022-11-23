lukaszml | 2017-01-02 01:09:25 UTC | #1

Hello I have problem with getting angle of momentum..
I try,
[code]atan2f(rb_car->GetLinearVelocity().z_, rb_car->GetLinearVelocity().y_)*(180.0f/MATH_PI_f)[/code]
but in result angle is sometime various.
[quote]90 0
86.8584 0
89.4495 0
92.0204 0
88.3266 0
90.9573 0
88.9929 0
90.3807 0
88.314 0
90.9475 0
89.0523 0
89.7019 0
87.9325 0
88.4162 0
92.6041 0
88.2135 0
89.1015 0
90.2773 0
90.4791 0
90.3192 0
90.2573 0
90.2098 0
90.2577 0
90.207 0
90.0368 0
90.0591 0
90.0433 0
90.0309 0
90.3281 0
93.2592 0
94.6764 0
95.9842 0
88.3735 0
84.8422 0
88.0211 0
91.1479 0
87.8885 0
91.0308 0
88.3128 0
91.924 0
88.7121 0
91.9258 0
87.7296 0
90.9954 0
88.2126 0
91.4525 0
86.1206 0
90.2706 0
92.9855 0
94.4474 0
86.9647 0
90.4604 0
87.9629 0
89.0636 0
89.0923 0
89.3138 0
89.461 0
89.5649 0
89.7147 0
89.768 0
89.7574 0
89.8213 0
89.8571 0
89.8871 0
89.9102 0
89.9309 0
90.6152 0
93.3258 0
94.6627 0
91.3123 0
84.5502 0
85.4823 0
88.2816 0
92.1724 0
89.2238 0
90.1235 0
89.8867 0
89.9726 0
89.9759 0
90.3984 0
90.4271 0
89.8219 0
89.7846 0
89.8914 0
89.8837 0
89.928 0
90.371 0
90.2964 0
87.8739 0
88.9125 0
89.239 0
93.5719 0
91.8887 0
90.7394 0
94.414 0
86.9725 0
91.7013 0
87.8652 0
92.6233 0
87.5722 0
92.4746 0
87.4988 0
92.4564 0
87.5251 0
92.6016 0
87.4284 0
92.5506 0
87.3956 0
87.0201 0
90.5878 0
82.186 0
93.6725 0
78.439 0
82.0083 0
84.2658 0
85.4207 0
92.6069 0
84.8407 0
86.3338 0
101.943 0
96.3925 0
101.198 0
89.2773 0
80.7922 0
95.3657 0
79.4658 0
96.3329 0
79.8507 0
97.2567 0
79.5661 0
98.3715 0
79.2131 0
99.5731 0
78.6107 0
100.617 0
77.7765 0
101.904 0
76.6828 0
103.211 0
75.3056 0
104.902 0
73.558 0
75.826 0
110.873 0
72.29 0
74.4631 0
117.812 0
68.8545 0
[b]70.9105 0
72.5382 0
73.7361 0
139.373 0
58.9024 0
58.9044 0
57.0267 0
51.2917 0
34.7038 0
1.56268 0
0.571785 0
0.715206 0
0.894669 0
1.12266 0
1.41137 0
1.77371 0
2.2315 0
2.79286 0
3.48745 0
4.31134 0
5.3891 0
6.72752 0
8.39058 0
10.4507 0
13.0001 0
16.1566 0
19.8808 0
24.1938 0
29.3192 0
35.054 0[/b]
41.1825 0
47.5173 0
53.858 0
59.7332 0
65.0347 0
69.5963 0
73.4226 0
76.318 0
79.1997 0
81.4119 0
82.8636 0
84.3231 0
85.4725 0
86.2074 0
87.2595 0
79.1521 0
90.8852 0
90.3046 0
89.8405 0
89.0146 0
91.6942 0
87.7426 0
90.2315 0
89.3781 0
89.258 0
0 0[/quote]

car is still 90degre and I get result like that 5.3891.... I don't know what.

Someone can help ?

-------------------------

thebluefish | 2017-01-02 01:09:25 UTC | #2

Can you record what rb_car->GetLinearVelocity().z_ and rb_car->GetLinearVelocity().y_ are for each of these?

I have a feeling that you will need to normalize your linear velocity first. Something like:

[code]auto linearVelocity = rb_car->GetLinearVelocity().Normalized();

atan2f(linearVelocity .z_, linearVelocity .y_)*(180.0f/MATH_PI_f)[/code]

Additionally, please note that physics is done in world-space, whereas each node will have its own local space as defined by its parent.

-------------------------

lukaszml | 2017-01-02 01:09:25 UTC | #3

After normalize nothing changes, same problem :frowning:

log of rb_ca->GetLinearVelocity(): [url]http://ctrlv.it/id/3923/4044105720[/url]

Why X axis oscillates - and +  (3.30514e-005  next -5.59745e-005 ) I dont understand this ..

-------------------------

Enhex | 2017-01-02 01:09:25 UTC | #4

is GetAngularVelocity() relevant?

-------------------------

lukaszml | 2017-01-02 01:09:25 UTC | #5

I want make [b]simple [/b]movement model of car.
When car go forward , not turn left or right, then friction as if very small.
So all racing track as a model have small friction 0.1, car as well.
But when momentum of car and car direction is opposite then friction increase. In case, momentum 0 degree, car direction 90 degree. They are somewhat orthogonal then friction goes 0.8(of cource all is interpolated when angle 78 the friction 0.62 for instance).
I want simualte friction by "ApplyForce" but I need angle :frowning:

PS. I know that I have sample of vechicle in examples but I don't want this denouement..

-------------------------

Enhex | 2017-01-02 01:09:26 UTC | #6

You could try to use relative rotation constraint with a cylinder or capsule to create a wheel with high friction and let the physics happen organically.
Not sure how stable this solution will be, or if it will be able to achieve good control.

-------------------------

thebluefish | 2017-01-02 01:09:26 UTC | #7

Try averaging the info over a set of frames. I'm sure you're going to get better results over 5 frames than your per-frame results.

-------------------------

