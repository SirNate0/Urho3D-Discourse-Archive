sheinb | 2019-01-15 16:46:04 UTC | #1

I am trying to digest the context within which AngelScript functions are callable.  In particular, I'd like to be able to pass an AngelScript function call in from a network client.  I can get the text into a network handler and then pass the text (e.g. "MyFunc();") to be executed by the controlling script using script.Execute(text), but I get a "No matching symbol" error.  Is it possible to allow a script to execute functions defined within itself using "Execute()"?

(As a workaround, I can parse the incoming text and dispatch the call, but it would be great if I could just call Execute directly.)

Thanks!

-------------------------

