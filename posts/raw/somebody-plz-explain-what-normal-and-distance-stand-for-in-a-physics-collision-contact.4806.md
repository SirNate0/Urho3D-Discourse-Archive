Virgo | 2019-01-13 14:47:54 UTC | #1

And how to properly extract data from this "Contacts" buffer thing

-------------------------

Virgo | 2019-01-12 18:49:52 UTC | #2

    void Character::HandleNodeCollision(StringHash eventType, VariantMap& eventData)
    {
        // Check collision contacts and see if character is standing on ground (look for a contact that has near vertical normal)
        using namespace NodeCollision;

        MemoryBuffer contacts(eventData[P_CONTACTS].GetBuffer());

        while (!contacts.IsEof())
        {
            Vector3 contactPosition = contacts.ReadVector3();
            Vector3 contactNormal = contacts.ReadVector3();
            /*float contactDistance = */contacts.ReadFloat();
            /*float contactImpulse = */contacts.ReadFloat();

            // If contact is below node center and pointing up, assume it's a ground contact
            if (contactPosition.y_ < (node_->GetPosition().y_ + 1.0f))
            {
                float level = contactNormal.y_;
                if (level > 0.75)
                    onGround_ = true;
            }
        }
    }

I found these codes in example 18_CharacterDemo, it demonstrates the way to extract data from the buffer, but why is it skipping 2 float variables' data here?

-------------------------

SirNate0 | 2019-01-12 20:32:16 UTC | #3

Because those floats aren't used. The floats are still stored in the buffer, so they have to be read to advance to the next contact position location in the buffer, but the code doesn't actually use the distance or impulse so the variable declaration/assignments were commented out leaving only the readFloat calls in the executed code.

-------------------------

I3DB | 2019-01-13 00:32:03 UTC | #4

There'a a csharp version of that routine:
```
void HandleNodeCollision(NodeCollisionEventArgs args)
{
	foreach (var contact in args.Contacts)
		if (contact.ContactPosition.Y < (Node.Position.Y + 1.0f))
                    onGround = Math.Abs(contact.ContactNormal.Y) > 0.75;

}
```
It is off topic, but an interesting example of why c# is popular and a good way to get introduced to urho3.

-------------------------

Virgo | 2019-01-13 02:18:33 UTC | #5

:joy: My bad... i just saw the start of multi line comment `/*` and thought that the whole line is commented out subconsciously. I was reading codes on github web, without the help of code highlighting.

-------------------------

