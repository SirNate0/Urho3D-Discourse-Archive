thebluefish | 2017-01-02 01:00:28 UTC | #1

Hi all,

I wanted to make a post about this before making any changes to the engine itself. It seems that if I register a remote event, it registers that event for both inbound and outbound events.

Therefore if I want to limit the events my game server can receive, suddenly my server can no longer send client-related events to the game client. IMO it would be best for the whitelist to only affect inbound remote events. I don't see a reason why we would want to filter outbound events as well.

Alternatively we could have 2 separate lists of whitelisted remote events, one for inbound and one for outbound. That way we can control which events get fired when we receive an event, and we can also set limitations on events that we can send.

Thought/opinions?

-------------------------

cadaver | 2017-01-02 01:00:28 UTC | #2

I believe you're right that sending whatever remote event could be allowed. Because remote events can be registered from script, not allowing would not increase security (a rogue script could first register event, then send it anyway).

I should be able to make that change to master branch soon.

-------------------------

