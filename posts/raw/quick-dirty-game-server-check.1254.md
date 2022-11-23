vivienneanthony | 2017-01-02 01:06:25 UTC | #1

Hi,
Is there a quick and dirty way to see if a game server is online.
Vivivenne

-------------------------

weitjong | 2017-01-02 01:06:25 UTC | #2

The easiest way I can think of is using *nix "telnet" command.

EDIT: That is if your server is using TCP. If you are using UDP as what has been provided by Urho3D network subsystem then probably you can use 'netstat' on the server side and 'nc' on the client side.

-------------------------

