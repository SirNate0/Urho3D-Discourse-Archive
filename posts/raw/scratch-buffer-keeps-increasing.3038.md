TheComet | 2017-04-23 02:59:33 UTC | #1

I'm a little bit concerned. Whenever I select the algorithm from the dropdown in the UI, the scratch buffer increases by a bit.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/fe80bb574baeb082b89c0b84ea879479b7c5e927.png" width="346" height="123">

All I'm doing is clicking on this dropdown over and over, and this is what I see in the log. Is this a problem?

    [Sun Apr 23 04:54:41 2017] INFO: [IK] Rebuilding effector nodes list
    [Sun Apr 23 04:54:41 2017] INFO: [IK] There are 1 effector(s) involving 4 node(s). 0 chain(s) were created
    [Sun Apr 23 04:54:41 2017] DEBUG: Resized scratch buffer to size 74176
    [Sun Apr 23 04:54:57 2017] INFO: [IK] Rebuilding effector nodes list
    [Sun Apr 23 04:54:57 2017] INFO: [IK] There are 1 effector(s) involving 4 node(s). 0 chain(s) were created
    [Sun Apr 23 04:54:57 2017] DEBUG: Resized scratch buffer to size 94784
    [Sun Apr 23 04:54:59 2017] INFO: [IK] Rebuilding effector nodes list
    [Sun Apr 23 04:54:59 2017] INFO: [IK] There are 1 effector(s) involving 4 node(s). 0 chain(s) were created
    [Sun Apr 23 04:54:59 2017] DEBUG: Resized scratch buffer to size 115392
    [Sun Apr 23 04:55:00 2017] INFO: [IK] Rebuilding effector nodes list
    [Sun Apr 23 04:55:00 2017] INFO: [IK] There are 1 effector(s) involving 4 node(s). 0 chain(s) were created
    [Sun Apr 23 04:55:00 2017] DEBUG: Resized scratch buffer to size 136000
    [Sun Apr 23 04:55:01 2017] INFO: [IK] Rebuilding effector nodes list
    [Sun Apr 23 04:55:01 2017] INFO: [IK] There are 1 effector(s) involving 4 node(s). 0 chain(s) were created
    [Sun Apr 23 04:55:01 2017] DEBUG: Resized scratch buffer to size 156608
    [Sun Apr 23 04:55:02 2017] INFO: [IK] Rebuilding effector nodes list
    [Sun Apr 23 04:55:02 2017] INFO: [IK] There are 1 effector(s) involving 4 node(s). 0 chain(s) were created
    [Sun Apr 23 04:55:02 2017] DEBUG: Resized scratch buffer to size 177216
    [Sun Apr 23 04:55:02 2017] INFO: [IK] Rebuilding effector nodes list
    [Sun Apr 23 04:55:02 2017] INFO: [IK] There are 1 effector(s) involving 4 node(s). 0 chain(s) were created
    [Sun Apr 23 04:55:02 2017] DEBUG: Resized scratch buffer to size 197824
    [Sun Apr 23 04:55:03 2017] INFO: [IK] Rebuilding effector nodes list
    [Sun Apr 23 04:55:03 2017] INFO: [IK] There are 1 effector(s) involving 4 node(s). 0 chain(s) were created
    [Sun Apr 23 04:55:03 2017] DEBUG: Resized scratch buffer to size 218432
    [Sun Apr 23 04:55:04 2017] INFO: [IK] Rebuilding effector nodes list
    [Sun Apr 23 04:55:04 2017] INFO: [IK] There are 1 effector(s) involving 4 node(s). 0 chain(s) were created
    [Sun Apr 23 04:55:04 2017] DEBUG: Resized scratch buffer to size 239040
    [Sun Apr 23 04:55:05 2017] INFO: [IK] Rebuilding effector nodes list
    [Sun Apr 23 04:55:05 2017] INFO: [IK] There are 1 effector(s) involving 4 node(s). 0 chain(s) were created
    [Sun Apr 23 04:55:05 2017] DEBUG: Resized scratch buffer to size 259648

-------------------------

Eugene | 2017-04-23 18:45:28 UTC | #2

Is scratch buffer used for drawing debug stuff and/or UI?
If I were you, I'd re-check debug drawing ops.

-------------------------

TheComet | 2017-04-23 20:12:45 UTC | #3

Thanks for the hint about debug drawing, that was all I needed to know to fix it. It turns out I wasn't clearing a list of effector components when the solver gets destroyed, so every time I changed the solver I was debug drawing the same effectors more and more.

-------------------------

