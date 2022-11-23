dada0526 | 2019-09-11 13:43:08 UTC | #1

![1|442x421](upload://ftLJJwcIH1IPjkUUbcZ1cWLsSCY.png) 

As You can see I got a material text list file from Blender(Props.txt),but How I Can use it? Which folder should I put it in? I tried to use staticmodel->ApplyMaterialList(),and put the file name as the first parameter,but it doesn't work.Can anyone help me to solve this problem?

-------------------------

Leith | 2019-09-11 13:25:30 UTC | #2

I can help you!
Show me props.txt
We need to make it proper XML formatting, then we can use the api you suggested to load it!

-------------------------

Modanung | 2019-09-11 13:29:23 UTC | #3

Welcome to the forums! :confetti_ball: :slightly_smiling_face:

When using `ApplyMaterialList` without any arguments the material list txt should be located in the same folder as the model file and carry the same name before the extension.
Also, are there any errors being logged about resources not found maybe?

-------------------------

