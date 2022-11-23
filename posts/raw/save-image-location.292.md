ucupumar | 2017-01-02 00:59:26 UTC | #1

I want to take screenshot (using graphics->TakeScreenshoot()) and save the Image using image.SaveJPG(), the function returns true but I couldn't find the saved image file anywhere. 
I tried to search using explorer but got nothing. I tried to input simple path 'E:\imagesaved.jpg' or 'imagesaved.jpg' and still got nothing. 
Did I miss something?  :question: 
I'm using Windows 7 x64.

-------------------------

ucupumar | 2017-01-02 00:59:26 UTC | #2

I found it, but file name is wrong. It saved as something random number like '778727527.jpg'. I called the function with: [code]testImage.SaveJPG(String('abcdefg123.jpg'))[/code]Is it a bug?

-------------------------

friesencr | 2017-01-02 00:59:26 UTC | #3

Does it work if you use " instead of '

-------------------------

Mike | 2017-01-02 00:59:26 UTC | #4

You can take Bin/Data/Scripts/Editor/EditorUI.as or Bin/Data/Scripts/Utilities/Sample.as as examples to start from and adapt to your path (both feature taking screenshots).

-------------------------

ucupumar | 2017-01-02 00:59:28 UTC | #5

Thanks for the replies. I think I found it, you don't need to cast String on function. Just use:[code]SaveJPG("testCapture.jpg", 100)[/code] It works for me now. :smiley:

-------------------------

weitjong | 2017-01-02 00:59:29 UTC | #6

Actually you can use the String() constructor explicitly or not. It does not really matter, provided you use the correct string literal in C/C++. The string literal is double quoted, as already pointed out by Chris.

-------------------------

