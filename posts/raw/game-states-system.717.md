rogerdv | 2017-01-02 01:02:23 UTC | #1

I started to implement a game state system for my project, and managed to make 2 simple states. But basically, my states can only manage going to next, I havent figured out a way to go back to previous, or stay in a state if it doesn has scene updates. For example, I dont know how to make the conversation state to loop while user is interacting with dialog choices, as it is pure ui stuff, it doesn has a scene update event. How can I workaround this? I tried a while loop, but it simply puts the game in an endless loop.

-------------------------

